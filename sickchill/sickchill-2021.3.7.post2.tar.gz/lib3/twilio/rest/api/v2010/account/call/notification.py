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


class NotificationList(ListResource):

    def __init__(self, version, account_sid, call_sid):
        """
        Initialize the NotificationList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the Account that created the resource
        :param call_sid: The SID of the Call the resource is associated with

        :returns: twilio.rest.api.v2010.account.call.notification.NotificationList
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationList
        """
        super(NotificationList, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'call_sid': call_sid, }
        self._uri = '/Accounts/{account_sid}/Calls/{call_sid}/Notifications.json'.format(**self._solution)

    def stream(self, log=values.unset, message_date_before=values.unset,
               message_date=values.unset, message_date_after=values.unset,
               limit=None, page_size=None):
        """
        Streams NotificationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode log: Filter by log level
        :param date message_date_before: Filter by date
        :param date message_date: Filter by date
        :param date message_date_after: Filter by date
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.call.notification.NotificationInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            log=log,
            message_date_before=message_date_before,
            message_date=message_date,
            message_date_after=message_date_after,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'])

    def list(self, log=values.unset, message_date_before=values.unset,
             message_date=values.unset, message_date_after=values.unset, limit=None,
             page_size=None):
        """
        Lists NotificationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode log: Filter by log level
        :param date message_date_before: Filter by date
        :param date message_date: Filter by date
        :param date message_date_after: Filter by date
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.call.notification.NotificationInstance]
        """
        return list(self.stream(
            log=log,
            message_date_before=message_date_before,
            message_date=message_date,
            message_date_after=message_date_after,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, log=values.unset, message_date_before=values.unset,
             message_date=values.unset, message_date_after=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of NotificationInstance records from the API.
        Request is executed immediately

        :param unicode log: Filter by log level
        :param date message_date_before: Filter by date
        :param date message_date: Filter by date
        :param date message_date_after: Filter by date
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of NotificationInstance
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationPage
        """
        data = values.of({
            'Log': log,
            'MessageDate<': serialize.iso8601_date(message_date_before),
            'MessageDate': serialize.iso8601_date(message_date),
            'MessageDate>': serialize.iso8601_date(message_date_after),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return NotificationPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of NotificationInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of NotificationInstance
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return NotificationPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a NotificationContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.api.v2010.account.call.notification.NotificationContext
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationContext
        """
        return NotificationContext(
            self._version,
            account_sid=self._solution['account_sid'],
            call_sid=self._solution['call_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a NotificationContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.api.v2010.account.call.notification.NotificationContext
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationContext
        """
        return NotificationContext(
            self._version,
            account_sid=self._solution['account_sid'],
            call_sid=self._solution['call_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.NotificationList>'


class NotificationPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the NotificationPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The SID of the Account that created the resource
        :param call_sid: The SID of the Call the resource is associated with

        :returns: twilio.rest.api.v2010.account.call.notification.NotificationPage
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationPage
        """
        super(NotificationPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of NotificationInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.call.notification.NotificationInstance
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationInstance
        """
        return NotificationInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            call_sid=self._solution['call_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.NotificationPage>'


class NotificationContext(InstanceContext):

    def __init__(self, version, account_sid, call_sid, sid):
        """
        Initialize the NotificationContext

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the Account that created the resource to fetch
        :param call_sid: The Call SID of the resource to fetch
        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.api.v2010.account.call.notification.NotificationContext
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationContext
        """
        super(NotificationContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'call_sid': call_sid, 'sid': sid, }
        self._uri = '/Accounts/{account_sid}/Calls/{call_sid}/Notifications/{sid}.json'.format(**self._solution)

    def fetch(self):
        """
        Fetch the NotificationInstance

        :returns: The fetched NotificationInstance
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return NotificationInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            call_sid=self._solution['call_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.NotificationContext {}>'.format(context)


class NotificationInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, call_sid, sid=None):
        """
        Initialize the NotificationInstance

        :returns: twilio.rest.api.v2010.account.call.notification.NotificationInstance
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationInstance
        """
        super(NotificationInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'api_version': payload.get('api_version'),
            'call_sid': payload.get('call_sid'),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
            'error_code': payload.get('error_code'),
            'log': payload.get('log'),
            'message_date': deserialize.rfc2822_datetime(payload.get('message_date')),
            'message_text': payload.get('message_text'),
            'more_info': payload.get('more_info'),
            'request_method': payload.get('request_method'),
            'request_url': payload.get('request_url'),
            'request_variables': payload.get('request_variables'),
            'response_body': payload.get('response_body'),
            'response_headers': payload.get('response_headers'),
            'sid': payload.get('sid'),
            'uri': payload.get('uri'),
        }

        # Context
        self._context = None
        self._solution = {
            'account_sid': account_sid,
            'call_sid': call_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: NotificationContext for this NotificationInstance
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationContext
        """
        if self._context is None:
            self._context = NotificationContext(
                self._version,
                account_sid=self._solution['account_sid'],
                call_sid=self._solution['call_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def api_version(self):
        """
        :returns: The API version used to create the Call Notification resource
        :rtype: unicode
        """
        return self._properties['api_version']

    @property
    def call_sid(self):
        """
        :returns: The SID of the Call the resource is associated with
        :rtype: unicode
        """
        return self._properties['call_sid']

    @property
    def date_created(self):
        """
        :returns: The RFC 2822 date and time in GMT that the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The RFC 2822 date and time in GMT that the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def error_code(self):
        """
        :returns: A unique error code corresponding to the notification
        :rtype: unicode
        """
        return self._properties['error_code']

    @property
    def log(self):
        """
        :returns: An integer log level
        :rtype: unicode
        """
        return self._properties['log']

    @property
    def message_date(self):
        """
        :returns: The date the notification was generated
        :rtype: datetime
        """
        return self._properties['message_date']

    @property
    def message_text(self):
        """
        :returns: The text of the notification
        :rtype: unicode
        """
        return self._properties['message_text']

    @property
    def more_info(self):
        """
        :returns: A URL for more information about the error code
        :rtype: unicode
        """
        return self._properties['more_info']

    @property
    def request_method(self):
        """
        :returns: HTTP method used with the request url
        :rtype: unicode
        """
        return self._properties['request_method']

    @property
    def request_url(self):
        """
        :returns: URL of the resource that generated the notification
        :rtype: unicode
        """
        return self._properties['request_url']

    @property
    def request_variables(self):
        """
        :returns: Twilio-generated HTTP variables sent to the server
        :rtype: unicode
        """
        return self._properties['request_variables']

    @property
    def response_body(self):
        """
        :returns: The HTTP body returned by your server
        :rtype: unicode
        """
        return self._properties['response_body']

    @property
    def response_headers(self):
        """
        :returns: The HTTP headers returned by your server
        :rtype: unicode
        """
        return self._properties['response_headers']

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def uri(self):
        """
        :returns: The URI of the resource, relative to `https://api.twilio.com`
        :rtype: unicode
        """
        return self._properties['uri']

    def fetch(self):
        """
        Fetch the NotificationInstance

        :returns: The fetched NotificationInstance
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.NotificationInstance {}>'.format(context)
