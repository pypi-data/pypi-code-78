# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.wireless.v1.sim.data_session import DataSessionList
from twilio.rest.wireless.v1.sim.usage_record import UsageRecordList


class SimList(ListResource):

    def __init__(self, version):
        """
        Initialize the SimList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.wireless.v1.sim.SimList
        :rtype: twilio.rest.wireless.v1.sim.SimList
        """
        super(SimList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Sims'.format(**self._solution)

    def stream(self, status=values.unset, iccid=values.unset,
               rate_plan=values.unset, e_id=values.unset,
               sim_registration_code=values.unset, limit=None, page_size=None):
        """
        Streams SimInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param SimInstance.Status status: Only return Sim resources with this status
        :param unicode iccid: Only return Sim resources with this ICCID
        :param unicode rate_plan: Only return Sim resources assigned to this RatePlan resource
        :param unicode e_id: Deprecated
        :param unicode sim_registration_code: Only return Sim resources with this registration code
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.wireless.v1.sim.SimInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            status=status,
            iccid=iccid,
            rate_plan=rate_plan,
            e_id=e_id,
            sim_registration_code=sim_registration_code,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'])

    def list(self, status=values.unset, iccid=values.unset, rate_plan=values.unset,
             e_id=values.unset, sim_registration_code=values.unset, limit=None,
             page_size=None):
        """
        Lists SimInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param SimInstance.Status status: Only return Sim resources with this status
        :param unicode iccid: Only return Sim resources with this ICCID
        :param unicode rate_plan: Only return Sim resources assigned to this RatePlan resource
        :param unicode e_id: Deprecated
        :param unicode sim_registration_code: Only return Sim resources with this registration code
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.wireless.v1.sim.SimInstance]
        """
        return list(self.stream(
            status=status,
            iccid=iccid,
            rate_plan=rate_plan,
            e_id=e_id,
            sim_registration_code=sim_registration_code,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, status=values.unset, iccid=values.unset, rate_plan=values.unset,
             e_id=values.unset, sim_registration_code=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of SimInstance records from the API.
        Request is executed immediately

        :param SimInstance.Status status: Only return Sim resources with this status
        :param unicode iccid: Only return Sim resources with this ICCID
        :param unicode rate_plan: Only return Sim resources assigned to this RatePlan resource
        :param unicode e_id: Deprecated
        :param unicode sim_registration_code: Only return Sim resources with this registration code
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SimInstance
        :rtype: twilio.rest.wireless.v1.sim.SimPage
        """
        data = values.of({
            'Status': status,
            'Iccid': iccid,
            'RatePlan': rate_plan,
            'EId': e_id,
            'SimRegistrationCode': sim_registration_code,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return SimPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SimInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SimInstance
        :rtype: twilio.rest.wireless.v1.sim.SimPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return SimPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a SimContext

        :param sid: The SID of the Sim resource to fetch

        :returns: twilio.rest.wireless.v1.sim.SimContext
        :rtype: twilio.rest.wireless.v1.sim.SimContext
        """
        return SimContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a SimContext

        :param sid: The SID of the Sim resource to fetch

        :returns: twilio.rest.wireless.v1.sim.SimContext
        :rtype: twilio.rest.wireless.v1.sim.SimContext
        """
        return SimContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Wireless.V1.SimList>'


class SimPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the SimPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.wireless.v1.sim.SimPage
        :rtype: twilio.rest.wireless.v1.sim.SimPage
        """
        super(SimPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SimInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.wireless.v1.sim.SimInstance
        :rtype: twilio.rest.wireless.v1.sim.SimInstance
        """
        return SimInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Wireless.V1.SimPage>'


class SimContext(InstanceContext):

    def __init__(self, version, sid):
        """
        Initialize the SimContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the Sim resource to fetch

        :returns: twilio.rest.wireless.v1.sim.SimContext
        :rtype: twilio.rest.wireless.v1.sim.SimContext
        """
        super(SimContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/Sims/{sid}'.format(**self._solution)

        # Dependents
        self._usage_records = None
        self._data_sessions = None

    def fetch(self):
        """
        Fetch the SimInstance

        :returns: The fetched SimInstance
        :rtype: twilio.rest.wireless.v1.sim.SimInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return SimInstance(self._version, payload, sid=self._solution['sid'], )

    def update(self, unique_name=values.unset, callback_method=values.unset,
               callback_url=values.unset, friendly_name=values.unset,
               rate_plan=values.unset, status=values.unset,
               commands_callback_method=values.unset,
               commands_callback_url=values.unset, sms_fallback_method=values.unset,
               sms_fallback_url=values.unset, sms_method=values.unset,
               sms_url=values.unset, voice_fallback_method=values.unset,
               voice_fallback_url=values.unset, voice_method=values.unset,
               voice_url=values.unset, reset_status=values.unset,
               account_sid=values.unset):
        """
        Update the SimInstance

        :param unicode unique_name: An application-defined string that uniquely identifies the resource
        :param unicode callback_method: The HTTP method we should use to call callback_url
        :param unicode callback_url: The URL we should call when the Sim resource has finished updating
        :param unicode friendly_name: A string to describe the Sim resource
        :param unicode rate_plan: The SID or unique name of the RatePlan resource to which the Sim resource should be assigned
        :param SimInstance.Status status: The new status of the Sim resource
        :param unicode commands_callback_method: The HTTP method we should use to call commands_callback_url
        :param unicode commands_callback_url: The URL we should call when the SIM sends a Command
        :param unicode sms_fallback_method: The HTTP method we should use to call sms_fallback_url
        :param unicode sms_fallback_url: The URL we should call when an error occurs while retrieving or executing the TwiML requested from sms_url
        :param unicode sms_method: The HTTP method we should use to call sms_url
        :param unicode sms_url: The URL we should call when the SIM-connected device sends an SMS message that is not a Command
        :param unicode voice_fallback_method: The HTTP method we should use to call voice_fallback_url
        :param unicode voice_fallback_url: The URL we should call when an error occurs while retrieving or executing the TwiML requested from voice_url
        :param unicode voice_method: The HTTP method we should use when we call voice_url
        :param unicode voice_url: The URL we should call when the SIM-connected device makes a voice call
        :param SimInstance.ResetStatus reset_status: Initiate a connectivity reset on a SIM
        :param unicode account_sid: The SID of the Account to which the Sim resource should belong

        :returns: The updated SimInstance
        :rtype: twilio.rest.wireless.v1.sim.SimInstance
        """
        data = values.of({
            'UniqueName': unique_name,
            'CallbackMethod': callback_method,
            'CallbackUrl': callback_url,
            'FriendlyName': friendly_name,
            'RatePlan': rate_plan,
            'Status': status,
            'CommandsCallbackMethod': commands_callback_method,
            'CommandsCallbackUrl': commands_callback_url,
            'SmsFallbackMethod': sms_fallback_method,
            'SmsFallbackUrl': sms_fallback_url,
            'SmsMethod': sms_method,
            'SmsUrl': sms_url,
            'VoiceFallbackMethod': voice_fallback_method,
            'VoiceFallbackUrl': voice_fallback_url,
            'VoiceMethod': voice_method,
            'VoiceUrl': voice_url,
            'ResetStatus': reset_status,
            'AccountSid': account_sid,
        })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return SimInstance(self._version, payload, sid=self._solution['sid'], )

    def delete(self):
        """
        Deletes the SimInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    @property
    def usage_records(self):
        """
        Access the usage_records

        :returns: twilio.rest.wireless.v1.sim.usage_record.UsageRecordList
        :rtype: twilio.rest.wireless.v1.sim.usage_record.UsageRecordList
        """
        if self._usage_records is None:
            self._usage_records = UsageRecordList(self._version, sim_sid=self._solution['sid'], )
        return self._usage_records

    @property
    def data_sessions(self):
        """
        Access the data_sessions

        :returns: twilio.rest.wireless.v1.sim.data_session.DataSessionList
        :rtype: twilio.rest.wireless.v1.sim.data_session.DataSessionList
        """
        if self._data_sessions is None:
            self._data_sessions = DataSessionList(self._version, sim_sid=self._solution['sid'], )
        return self._data_sessions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Wireless.V1.SimContext {}>'.format(context)


class SimInstance(InstanceResource):

    class Status(object):
        NEW = "new"
        READY = "ready"
        ACTIVE = "active"
        SUSPENDED = "suspended"
        DEACTIVATED = "deactivated"
        CANCELED = "canceled"
        SCHEDULED = "scheduled"
        UPDATING = "updating"

    class ResetStatus(object):
        RESETTING = "resetting"

    def __init__(self, version, payload, sid=None):
        """
        Initialize the SimInstance

        :returns: twilio.rest.wireless.v1.sim.SimInstance
        :rtype: twilio.rest.wireless.v1.sim.SimInstance
        """
        super(SimInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'unique_name': payload.get('unique_name'),
            'account_sid': payload.get('account_sid'),
            'rate_plan_sid': payload.get('rate_plan_sid'),
            'friendly_name': payload.get('friendly_name'),
            'iccid': payload.get('iccid'),
            'e_id': payload.get('e_id'),
            'status': payload.get('status'),
            'reset_status': payload.get('reset_status'),
            'commands_callback_url': payload.get('commands_callback_url'),
            'commands_callback_method': payload.get('commands_callback_method'),
            'sms_fallback_method': payload.get('sms_fallback_method'),
            'sms_fallback_url': payload.get('sms_fallback_url'),
            'sms_method': payload.get('sms_method'),
            'sms_url': payload.get('sms_url'),
            'voice_fallback_method': payload.get('voice_fallback_method'),
            'voice_fallback_url': payload.get('voice_fallback_url'),
            'voice_method': payload.get('voice_method'),
            'voice_url': payload.get('voice_url'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
            'links': payload.get('links'),
            'ip_address': payload.get('ip_address'),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: SimContext for this SimInstance
        :rtype: twilio.rest.wireless.v1.sim.SimContext
        """
        if self._context is None:
            self._context = SimContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the Sim resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account to which the Sim resource belongs
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def rate_plan_sid(self):
        """
        :returns: The SID of the RatePlan resource to which the Sim resource is assigned.
        :rtype: unicode
        """
        return self._properties['rate_plan_sid']

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the Sim resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def iccid(self):
        """
        :returns: The ICCID associated with the SIM
        :rtype: unicode
        """
        return self._properties['iccid']

    @property
    def e_id(self):
        """
        :returns: Deprecated
        :rtype: unicode
        """
        return self._properties['e_id']

    @property
    def status(self):
        """
        :returns: The status of the Sim resource
        :rtype: SimInstance.Status
        """
        return self._properties['status']

    @property
    def reset_status(self):
        """
        :returns: The connectivity reset status of the SIM
        :rtype: SimInstance.ResetStatus
        """
        return self._properties['reset_status']

    @property
    def commands_callback_url(self):
        """
        :returns: The URL we call when the SIM originates a machine-to-machine Command
        :rtype: unicode
        """
        return self._properties['commands_callback_url']

    @property
    def commands_callback_method(self):
        """
        :returns: The HTTP method we use to call commands_callback_url
        :rtype: unicode
        """
        return self._properties['commands_callback_method']

    @property
    def sms_fallback_method(self):
        """
        :returns: The HTTP method we use to call sms_fallback_url
        :rtype: unicode
        """
        return self._properties['sms_fallback_method']

    @property
    def sms_fallback_url(self):
        """
        :returns: The URL we call when an error occurs while retrieving or executing the TwiML requested from the sms_url
        :rtype: unicode
        """
        return self._properties['sms_fallback_url']

    @property
    def sms_method(self):
        """
        :returns: The HTTP method we use to call sms_url
        :rtype: unicode
        """
        return self._properties['sms_method']

    @property
    def sms_url(self):
        """
        :returns: The URL we call when the SIM-connected device sends an SMS message that is not a Command
        :rtype: unicode
        """
        return self._properties['sms_url']

    @property
    def voice_fallback_method(self):
        """
        :returns: The HTTP method we use to call voice_fallback_url
        :rtype: unicode
        """
        return self._properties['voice_fallback_method']

    @property
    def voice_fallback_url(self):
        """
        :returns: The URL we call when an error occurs while retrieving or executing the TwiML requested from voice_url
        :rtype: unicode
        """
        return self._properties['voice_fallback_url']

    @property
    def voice_method(self):
        """
        :returns: The HTTP method we use to call voice_url
        :rtype: unicode
        """
        return self._properties['voice_method']

    @property
    def voice_url(self):
        """
        :returns: The URL we call when the SIM-connected device makes a voice call
        :rtype: unicode
        """
        return self._properties['voice_url']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The ISO 8601 date and time in GMT when the Sim resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The absolute URL of the resource
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The URLs of related subresources
        :rtype: unicode
        """
        return self._properties['links']

    @property
    def ip_address(self):
        """
        :returns: Deprecated
        :rtype: unicode
        """
        return self._properties['ip_address']

    def fetch(self):
        """
        Fetch the SimInstance

        :returns: The fetched SimInstance
        :rtype: twilio.rest.wireless.v1.sim.SimInstance
        """
        return self._proxy.fetch()

    def update(self, unique_name=values.unset, callback_method=values.unset,
               callback_url=values.unset, friendly_name=values.unset,
               rate_plan=values.unset, status=values.unset,
               commands_callback_method=values.unset,
               commands_callback_url=values.unset, sms_fallback_method=values.unset,
               sms_fallback_url=values.unset, sms_method=values.unset,
               sms_url=values.unset, voice_fallback_method=values.unset,
               voice_fallback_url=values.unset, voice_method=values.unset,
               voice_url=values.unset, reset_status=values.unset,
               account_sid=values.unset):
        """
        Update the SimInstance

        :param unicode unique_name: An application-defined string that uniquely identifies the resource
        :param unicode callback_method: The HTTP method we should use to call callback_url
        :param unicode callback_url: The URL we should call when the Sim resource has finished updating
        :param unicode friendly_name: A string to describe the Sim resource
        :param unicode rate_plan: The SID or unique name of the RatePlan resource to which the Sim resource should be assigned
        :param SimInstance.Status status: The new status of the Sim resource
        :param unicode commands_callback_method: The HTTP method we should use to call commands_callback_url
        :param unicode commands_callback_url: The URL we should call when the SIM sends a Command
        :param unicode sms_fallback_method: The HTTP method we should use to call sms_fallback_url
        :param unicode sms_fallback_url: The URL we should call when an error occurs while retrieving or executing the TwiML requested from sms_url
        :param unicode sms_method: The HTTP method we should use to call sms_url
        :param unicode sms_url: The URL we should call when the SIM-connected device sends an SMS message that is not a Command
        :param unicode voice_fallback_method: The HTTP method we should use to call voice_fallback_url
        :param unicode voice_fallback_url: The URL we should call when an error occurs while retrieving or executing the TwiML requested from voice_url
        :param unicode voice_method: The HTTP method we should use when we call voice_url
        :param unicode voice_url: The URL we should call when the SIM-connected device makes a voice call
        :param SimInstance.ResetStatus reset_status: Initiate a connectivity reset on a SIM
        :param unicode account_sid: The SID of the Account to which the Sim resource should belong

        :returns: The updated SimInstance
        :rtype: twilio.rest.wireless.v1.sim.SimInstance
        """
        return self._proxy.update(
            unique_name=unique_name,
            callback_method=callback_method,
            callback_url=callback_url,
            friendly_name=friendly_name,
            rate_plan=rate_plan,
            status=status,
            commands_callback_method=commands_callback_method,
            commands_callback_url=commands_callback_url,
            sms_fallback_method=sms_fallback_method,
            sms_fallback_url=sms_fallback_url,
            sms_method=sms_method,
            sms_url=sms_url,
            voice_fallback_method=voice_fallback_method,
            voice_fallback_url=voice_fallback_url,
            voice_method=voice_method,
            voice_url=voice_url,
            reset_status=reset_status,
            account_sid=account_sid,
        )

    def delete(self):
        """
        Deletes the SimInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def usage_records(self):
        """
        Access the usage_records

        :returns: twilio.rest.wireless.v1.sim.usage_record.UsageRecordList
        :rtype: twilio.rest.wireless.v1.sim.usage_record.UsageRecordList
        """
        return self._proxy.usage_records

    @property
    def data_sessions(self):
        """
        Access the data_sessions

        :returns: twilio.rest.wireless.v1.sim.data_session.DataSessionList
        :rtype: twilio.rest.wireless.v1.sim.data_session.DataSessionList
        """
        return self._proxy.data_sessions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Wireless.V1.SimInstance {}>'.format(context)
