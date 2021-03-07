import json

from starlette.requests import Request
from starlette.responses import Response, JSONResponse

import otree
import otree.bots.browser
import otree.views.cbv
from otree import settings
from otree.channels import utils as channel_utils
from otree.common import GlobalState
from otree.currency import json_dumps
from otree.database import db
from otree.models import Session, Participant
from otree.models_concrete import ParticipantVarsFromREST
from otree.room import ROOM_DICT
from otree.session import create_session, SESSION_CONFIGS_DICT, CreateSessionInvalidArgs
from .cbv import BaseRESTView


class PostParticipantVarsThroughREST(BaseRESTView):

    url_pattern = '/api/participant_vars'

    def inner_post(self, room_name, participant_label, vars):
        if room_name not in ROOM_DICT:
            return Response(f'Room {room_name} not found', status_code=404)
        room = ROOM_DICT[room_name]
        session = room.get_session()
        if session:
            participant = session.pp_set.filter_by(label=participant_label).first()
            if participant:
                participant.vars.update(vars)
                return Response('ok')
        kwargs = dict(participant_label=participant_label, room_name=room_name,)
        _json_data = json.dumps(vars)
        obj = ParticipantVarsFromREST.objects_first(**kwargs)
        if obj:
            obj._json_data = _json_data
        else:
            obj = ParticipantVarsFromREST(**kwargs, _json_data=_json_data)
            db.add(obj)
        return JSONResponse({})


class RESTSessionVars(BaseRESTView):
    url_pattern = '/api/session_vars'

    def inner_post(self, room_name, vars):
        if room_name not in ROOM_DICT:
            return Response(f'Room {room_name} not found', status_code=404)
        room = ROOM_DICT[room_name]
        session = room.get_session()
        if not session:
            return Response(f'No current session in room {room_name}', 404)
        session.vars.update(vars)
        return JSONResponse({})


def get_session_urls(session: Session, request: Request) -> dict:
    d = dict(
        session_url=request.url_for(
            'JoinSessionAnonymously', anonymous_code=session._anonymous_code
        )
    )
    room = session.get_room()
    if room:
        d['room_url'] = room.get_room_wide_url(request)
    return d


class RESTSession(BaseRESTView):

    url_pattern = '/api/sessions'

    def inner_post(self, **kwargs):
        try:
            session = create_session(**kwargs)
        except CreateSessionInvalidArgs as exc:
            return Response(str(exc), status_code=400)
        room_name = kwargs.get('room_name')

        response_payload = dict(code=session.code)
        if room_name:
            channel_utils.sync_group_send(
                group=channel_utils.room_participants_group_name(room_name),
                data={'status': 'session_ready'},
            )

        response_payload.update(get_session_urls(session, self.request))

        return JSONResponse(response_payload)

    def inner_get(self, code, participant_labels=None):
        session = db.get_or_404(Session, code=code)
        pp_set = session.pp_set
        if participant_labels is not None:
            print('participant_labels is', participant_labels)
            pp_set = pp_set.filter(Participant.label.in_(participant_labels))
        pdata = []
        for id_in_session, code, label, payoff in pp_set.with_entities(
            Participant.id_in_session,
            Participant.code,
            Participant.label,
            Participant.payoff,
        ):
            pdata.append(
                dict(
                    id_in_session=id_in_session,
                    code=code,
                    label=label,
                    payoff_in_real_world_currency=payoff.to_real_world_currency(
                        session
                    ),
                )
            )

        # need custom json_dumps for currency values
        return Response(
            json_dumps(
                dict(
                    # we need the session config for mturk settings and participation fee
                    # technically, other parts of session config might not be JSON serializable
                    config=session.config,
                    num_participants=session.num_participants,
                    REAL_WORLD_CURRENCY_CODE=settings.REAL_WORLD_CURRENCY_CODE,
                    participants=pdata,
                    **get_session_urls(session, self.request),
                )
            )
        )


class RESTSessionConfigs(BaseRESTView):
    url_pattern = '/api/session_configs'

    def inner_get(self):
        return Response(json_dumps(list(SESSION_CONFIGS_DICT.values())))


class RESTOTreeVersion(BaseRESTView):
    url_pattern = '/api/otree_version'

    def inner_get(self):
        return JSONResponse(dict(version=otree.__version__))


class RESTCreateSessionLegacy(RESTSession):
    url_pattern = '/api/v1/sessions'


class RESTSessionVarsLegacy(RESTSessionVars):
    url_pattern = '/api/v1/session_vars'


class RESTParticipantVarsLegacy(PostParticipantVarsThroughREST):
    url_pattern = '/api/v1/participant_vars'


launcher_session_code = None


class CreateBrowserBotsSession(BaseRESTView):
    url_pattern = '/create_browser_bots_session'

    def inner_post(
        self, num_participants, session_config_name, case_number,
    ):
        session = create_session(
            session_config_name=session_config_name, num_participants=num_participants
        )
        otree.bots.browser.initialize_session(
            session_pk=session.id, case_number=case_number
        )
        GlobalState.browser_bots_launcher_session_code = session.code
        channel_utils.sync_group_send(
            group='browser_bot_wait', data={'status': 'session_ready'}
        )

        return Response(session.code)


class CloseBrowserBotsSession(BaseRESTView):
    url_pattern = '/close_browser_bots_session'

    def inner_post(self, **kwargs):
        GlobalState.browser_bots_launcher_session_code = None
        return Response('ok')
