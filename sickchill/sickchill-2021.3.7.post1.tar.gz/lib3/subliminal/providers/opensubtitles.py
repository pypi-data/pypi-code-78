# -*- coding: utf-8 -*-
import base64
import logging
import os
import re
import zlib

from babelfish import Language, language_converters
from guessit import guessit
from six.moves.xmlrpc_client import ServerProxy

from . import Provider, TimeoutSafeTransport
from .. import __short_version__
from ..exceptions import (AuthenticationError, ConfigurationError, DownloadLimitExceeded, ProviderError,
                          ServiceUnavailable)
from ..matches import guess_matches
from ..subtitle import Subtitle, fix_line_ending
from ..video import Episode, Movie

logger = logging.getLogger(__name__)


class OpenSubtitlesSubtitle(Subtitle):
    """OpenSubtitles Subtitle."""
    provider_name = 'opensubtitles'
    series_re = re.compile(r'^"(?P<series_name>.*)" (?P<series_title>.*)$')

    def __init__(self, language, hearing_impaired, page_link, subtitle_id, matched_by, movie_kind, hash, movie_name,
                 movie_release_name, movie_year, movie_imdb_id, series_season, series_episode, filename, encoding):
        super(OpenSubtitlesSubtitle, self).__init__(language, hearing_impaired=hearing_impaired,
                                                    page_link=page_link, encoding=encoding)
        self.subtitle_id = subtitle_id
        self.matched_by = matched_by
        self.movie_kind = movie_kind
        self.hash = hash
        self.movie_name = movie_name
        self.movie_release_name = movie_release_name
        self.movie_year = movie_year
        self.movie_imdb_id = movie_imdb_id
        self.series_season = series_season
        self.series_episode = series_episode
        self.filename = filename

    @property
    def id(self):
        return str(self.subtitle_id)

    @property
    def info(self):
        if not self.filename and not self.movie_release_name:
            return self.subtitle_id
        if self.movie_release_name and len(self.movie_release_name) > len(self.filename):
            return self.movie_release_name
        return self.filename

    @property
    def series_name(self):
        return self.series_re.match(self.movie_name).group('series_name')

    @property
    def series_title(self):
        return self.series_re.match(self.movie_name).group('series_title')

    def get_matches(self, video):
        if (isinstance(video, Episode) and self.movie_kind != 'episode') or (
                isinstance(video, Movie) and self.movie_kind != 'movie'):
            logger.info('%r is not a valid movie_kind', self.movie_kind)
            return set()

        matches = guess_matches(video, {
            'title': self.series_name if self.movie_kind == 'episode' else self.movie_name,
            'episode_title': self.series_title if self.movie_kind == 'episode' else None,
            'year': self.movie_year,
            'season': self.series_season,
            'episode': self.series_episode
        })

        # tag
        if self.matched_by == 'tag':
            if not video.imdb_id or self.movie_imdb_id == video.imdb_id:
                if self.movie_kind == 'episode':
                    matches |= {'series', 'year', 'season', 'episode'}
                elif self.movie_kind == 'movie':
                    matches |= {'title', 'year'}

        # guess
        matches |= guess_matches(video, guessit(self.movie_release_name, {'type': self.movie_kind}))
        matches |= guess_matches(video, guessit(self.filename, {'type': self.movie_kind}))

        # hash
        if 'opensubtitles' in video.hashes and self.hash == video.hashes['opensubtitles']:
            if self.movie_kind == 'movie' and 'title' in matches:
                matches.add('hash')
            elif self.movie_kind == 'episode' and 'series' in matches and 'season' in matches and 'episode' in matches:
                matches.add('hash')
            else:
                logger.debug('Match on hash discarded')

        # imdb_id
        if video.imdb_id and self.movie_imdb_id == video.imdb_id:
            matches.add('imdb_id')

        return matches


class OpenSubtitlesProvider(Provider):
    """OpenSubtitles Provider.

    :param str username: username.
    :param str password: password.

    """
    languages = {Language.fromopensubtitles(l) for l in language_converters['opensubtitles'].codes}
    server_url = 'https://api.opensubtitles.org/xml-rpc'
    subtitle_class = OpenSubtitlesSubtitle
    user_agent = 'subliminal v%s' % __short_version__

    def __init__(self, username=None, password=None):
        self.server = ServerProxy(self.server_url, TimeoutSafeTransport(10))
        if any((username, password)) and not all((username, password)):
            raise ConfigurationError('Username and password must be specified')
        # None values not allowed for logging in, so replace it by ''
        self.username = username or ''
        self.password = password or ''
        self.token = None

    def initialize(self):
        logger.info('Logging in')
        response = checked(self.server.LogIn(self.username, self.password, 'eng', self.user_agent))
        self.token = response['token']
        logger.debug('Logged in with token %r', self.token)

    def terminate(self):
        logger.info('Logging out')
        checked(self.server.LogOut(self.token))
        self.server.close()
        self.token = None
        logger.debug('Logged out')

    def no_operation(self):
        logger.debug('No operation')
        checked(self.server.NoOperation(self.token))

    def query(self, languages, hash=None, size=None, imdb_id=None, query=None, season=None, episode=None, tag=None):
        # fill the search criteria
        criteria = []
        if hash and size:
            criteria.append({'moviehash': hash, 'moviebytesize': str(size)})
        if imdb_id:
            if season and episode:
                criteria.append({'imdbid': imdb_id[2:], 'season': season, 'episode': episode})
            else:
                criteria.append({'imdbid': imdb_id[2:]})
        if tag:
            criteria.append({'tag': tag})
        if query and season and episode:
            criteria.append({'query': query.replace('\'', ''), 'season': season, 'episode': episode})
        elif query:
            criteria.append({'query': query.replace('\'', '')})
        if not criteria:
            raise ValueError('Not enough information')

        # add the language
        for criterion in criteria:
            criterion['sublanguageid'] = ','.join(sorted(l.opensubtitles for l in languages))

        # query the server
        logger.info('Searching subtitles %r', criteria)
        response = checked(self.server.SearchSubtitles(self.token, criteria))
        subtitles = []

        # exit if no data
        if not response['data']:
            logger.debug('No subtitles found')
            return subtitles

        # loop over subtitle items
        for subtitle_item in response['data']:
            # read the item
            language = Language.fromopensubtitles(subtitle_item['SubLanguageID'])
            hearing_impaired = bool(int(subtitle_item['SubHearingImpaired']))
            page_link = subtitle_item['SubtitlesLink']
            subtitle_id = int(subtitle_item['IDSubtitleFile'])
            matched_by = subtitle_item['MatchedBy']
            movie_kind = subtitle_item['MovieKind']
            hash = subtitle_item['MovieHash']
            movie_name = subtitle_item['MovieName']
            movie_release_name = subtitle_item['MovieReleaseName']
            movie_year = int(subtitle_item['MovieYear']) if subtitle_item['MovieYear'] else None
            movie_imdb_id = 'tt' + subtitle_item['IDMovieImdb']
            series_season = int(subtitle_item['SeriesSeason']) if subtitle_item['SeriesSeason'] else None
            series_episode = int(subtitle_item['SeriesEpisode']) if subtitle_item['SeriesEpisode'] else None
            filename = subtitle_item['SubFileName']
            encoding = subtitle_item.get('SubEncoding') or None

            subtitle = self.subtitle_class(language, hearing_impaired, page_link, subtitle_id, matched_by, movie_kind,
                                           hash, movie_name, movie_release_name, movie_year, movie_imdb_id,
                                           series_season, series_episode, filename, encoding)
            logger.debug('Found subtitle %r by %s', subtitle, matched_by)
            subtitles.append(subtitle)

        return subtitles

    def list_subtitles(self, video, languages):
        season = episode = None
        if isinstance(video, Episode):
            query = video.series
            season = video.season
            episode = video.episode
        else:
            query = video.title

        return self.query(languages, hash=video.hashes.get('opensubtitles'), size=video.size, imdb_id=video.imdb_id,
                          query=query, season=season, episode=episode, tag=os.path.basename(video.name))

    def download_subtitle(self, subtitle):
        logger.info('Downloading subtitle %r', subtitle)
        response = checked(self.server.DownloadSubtitles(self.token, [str(subtitle.subtitle_id)]))
        subtitle.content = fix_line_ending(zlib.decompress(base64.b64decode(response['data'][0]['data']), 47))


class OpenSubtitlesVipSubtitle(OpenSubtitlesSubtitle):
    """OpenSubtitles Subtitle."""
    provider_name = 'opensubtitlesvip'


class OpenSubtitlesVipProvider(OpenSubtitlesProvider):
    """OpenSubtitles Provider using VIP url."""
    server_url = 'https://vip-api.opensubtitles.org/xml-rpc'
    subtitle_class = OpenSubtitlesVipSubtitle


class OpenSubtitlesError(ProviderError):
    """Base class for non-generic :class:`OpenSubtitlesProvider` exceptions."""
    pass


class Unauthorized(OpenSubtitlesError, AuthenticationError):
    """Exception raised when status is '401 Unauthorized'."""
    pass


class NoSession(OpenSubtitlesError, AuthenticationError):
    """Exception raised when status is '406 No session'."""
    pass


class DownloadLimitReached(OpenSubtitlesError, DownloadLimitExceeded):
    """Exception raised when status is '407 Download limit reached'."""
    pass


class InvalidImdbid(OpenSubtitlesError):
    """Exception raised when status is '413 Invalid ImdbID'."""
    pass


class UnknownUserAgent(OpenSubtitlesError, AuthenticationError):
    """Exception raised when status is '414 Unknown User Agent'."""
    pass


class DisabledUserAgent(OpenSubtitlesError, AuthenticationError):
    """Exception raised when status is '415 Disabled user agent'."""
    pass


def checked(response):
    """Check a response status before returning it.

    :param response: a response from a XMLRPC call to OpenSubtitles.
    :return: the response.
    :raise: :class:`OpenSubtitlesError`

    """
    status_code = int(response['status'][:3])
    if status_code == 401:
        raise Unauthorized
    if status_code == 406:
        raise NoSession
    if status_code == 407:
        raise DownloadLimitReached
    if status_code == 413:
        raise InvalidImdbid
    if status_code == 414:
        raise UnknownUserAgent
    if status_code == 415:
        raise DisabledUserAgent
    if status_code == 503:
        raise ServiceUnavailable
    if status_code != 200:
        raise OpenSubtitlesError(response['status'])

    return response
