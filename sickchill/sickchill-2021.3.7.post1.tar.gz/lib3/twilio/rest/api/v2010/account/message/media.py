# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class MediaList(ListResource):

    def __init__(self, version, account_sid, message_sid):
        """
        Initialize the MediaList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the Account that created this resource
        :param message_sid: The unique string that identifies the resource

        :returns: twilio.rest.api.v2010.account.message.media.MediaList
        :rtype: twilio.rest.api.v2010.account.message.media.MediaList
        """
        super(MediaList, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'message_sid': message_sid, }
        self._uri = '/Accounts/{account_sid}/Messages/{message_sid}/Media.json'.format(**self._solution)

    def stream(self, date_created_before=values.unset, date_created=values.unset,
               date_created_after=values.unset, limit=None, page_size=None):
        """
        Streams MediaInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param datetime date_created_before: Only include media that was created on this date
        :param datetime date_created: Only include media that was created on this date
        :param datetime date_created_after: Only include media that was created on this date
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.message.media.MediaInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            date_created_before=date_created_before,
            date_created=date_created,
            date_created_after=date_created_after,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'])

    def list(self, date_created_before=values.unset, date_created=values.unset,
             date_created_after=values.unset, limit=None, page_size=None):
        """
        Lists MediaInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param datetime date_created_before: Only include media that was created on this date
        :param datetime date_created: Only include media that was created on this date
        :param datetime date_created_after: Only include media that was created on this date
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.message.media.MediaInstance]
        """
        return list(self.stream(
            date_created_before=date_created_before,
            date_created=date_created,
            date_created_after=date_created_after,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, date_created_before=values.unset, date_created=values.unset,
             date_created_after=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of MediaInstance records from the API.
        Request is executed immediately

        :param datetime date_created_before: Only include media that was created on this date
        :param datetime date_created: Only include media that was created on this date
        :param datetime date_created_after: Only include media that was created on this date
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MediaInstance
        :rtype: twilio.rest.api.v2010.account.message.media.MediaPage
        """
        data = values.of({
            'DateCreated<': serialize.iso8601_datetime(date_created_before),
            'DateCreated': serialize.iso8601_datetime(date_created),
            'DateCreated>': serialize.iso8601_datetime(date_created_after),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return MediaPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of MediaInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MediaInstance
        :rtype: twilio.rest.api.v2010.account.message.media.MediaPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return MediaPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a MediaContext

        :param sid: The unique string that identifies this resource

        :returns: twilio.rest.api.v2010.account.message.media.MediaContext
        :rtype: twilio.rest.api.v2010.account.message.media.MediaContext
        """
        return MediaContext(
            self._version,
            account_sid=self._solution['account_sid'],
            message_sid=self._solution['message_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a MediaContext

        :param sid: The unique string that identifies this resource

        :returns: twilio.rest.api.v2010.account.message.media.MediaContext
        :rtype: twilio.rest.api.v2010.account.message.media.MediaContext
        """
        return MediaContext(
            self._version,
            account_sid=self._solution['account_sid'],
            message_sid=self._solution['message_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.MediaList>'


class MediaPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the MediaPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The SID of the Account that created this resource
        :param message_sid: The unique string that identifies the resource

        :returns: twilio.rest.api.v2010.account.message.media.MediaPage
        :rtype: twilio.rest.api.v2010.account.message.media.MediaPage
        """
        super(MediaPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of MediaInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.message.media.MediaInstance
        :rtype: twilio.rest.api.v2010.account.message.media.MediaInstance
        """
        return MediaInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            message_sid=self._solution['message_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.MediaPage>'


class MediaContext(InstanceContext):

    def __init__(self, version, account_sid, message_sid, sid):
        """
        Initialize the MediaContext

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the Account that created the resource(s) to fetch
        :param message_sid: The SID of the Message resource that this Media resource belongs to
        :param sid: The unique string that identifies this resource

        :returns: twilio.rest.api.v2010.account.message.media.MediaContext
        :rtype: twilio.rest.api.v2010.account.message.media.MediaContext
        """
        super(MediaContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'message_sid': message_sid, 'sid': sid, }
        self._uri = '/Accounts/{account_sid}/Messages/{message_sid}/Media/{sid}.json'.format(**self._solution)

    def delete(self):
        """
        Deletes the MediaInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    def fetch(self):
        """
        Fetch the MediaInstance

        :returns: The fetched MediaInstance
        :rtype: twilio.rest.api.v2010.account.message.media.MediaInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return MediaInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            message_sid=self._solution['message_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.MediaContext {}>'.format(context)


class MediaInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, message_sid, sid=None):
        """
        Initialize the MediaInstance

        :returns: twilio.rest.api.v2010.account.message.media.MediaInstance
        :rtype: twilio.rest.api.v2010.account.message.media.MediaInstance
        """
        super(MediaInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'content_type': payload.get('content_type'),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
            'parent_sid': payload.get('parent_sid'),
            'sid': payload.get('sid'),
            'uri': payload.get('uri'),
        }

        # Context
        self._context = None
        self._solution = {
            'account_sid': account_sid,
            'message_sid': message_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: MediaContext for this MediaInstance
        :rtype: twilio.rest.api.v2010.account.message.media.MediaContext
        """
        if self._context is None:
            self._context = MediaContext(
                self._version,
                account_sid=self._solution['account_sid'],
                message_sid=self._solution['message_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created this resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def content_type(self):
        """
        :returns: The default mime-type of the media
        :rtype: unicode
        """
        return self._properties['content_type']

    @property
    def date_created(self):
        """
        :returns: The RFC 2822 date and time in GMT that this resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The RFC 2822 date and time in GMT that this resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def parent_sid(self):
        """
        :returns: The SID of the resource that created the media
        :rtype: unicode
        """
        return self._properties['parent_sid']

    @property
    def sid(self):
        """
        :returns: The unique string that identifies this resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def uri(self):
        """
        :returns: The URI of this resource, relative to `https://api.twilio.com`
        :rtype: unicode
        """
        return self._properties['uri']

    def delete(self):
        """
        Deletes the MediaInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def fetch(self):
        """
        Fetch the MediaInstance

        :returns: The fetched MediaInstance
        :rtype: twilio.rest.api.v2010.account.message.media.MediaInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.MediaInstance {}>'.format(context)
