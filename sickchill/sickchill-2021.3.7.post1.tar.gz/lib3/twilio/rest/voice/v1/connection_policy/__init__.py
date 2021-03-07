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
from twilio.rest.voice.v1.connection_policy.connection_policy_target import ConnectionPolicyTargetList


class ConnectionPolicyList(ListResource):

    def __init__(self, version):
        """
        Initialize the ConnectionPolicyList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.voice.v1.connection_policy.ConnectionPolicyList
        :rtype: twilio.rest.voice.v1.connection_policy.ConnectionPolicyList
        """
        super(ConnectionPolicyList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/ConnectionPolicies'.format(**self._solution)

    def create(self, friendly_name=values.unset):
        """
        Create the ConnectionPolicyInstance

        :param unicode friendly_name: A string to describe the resource

        :returns: The created ConnectionPolicyInstance
        :rtype: twilio.rest.voice.v1.connection_policy.ConnectionPolicyInstance
        """
        data = values.of({'FriendlyName': friendly_name, })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return ConnectionPolicyInstance(self._version, payload, )

    def stream(self, limit=None, page_size=None):
        """
        Streams ConnectionPolicyInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.voice.v1.connection_policy.ConnectionPolicyInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ConnectionPolicyInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.voice.v1.connection_policy.ConnectionPolicyInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of ConnectionPolicyInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ConnectionPolicyInstance
        :rtype: twilio.rest.voice.v1.connection_policy.ConnectionPolicyPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return ConnectionPolicyPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ConnectionPolicyInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ConnectionPolicyInstance
        :rtype: twilio.rest.voice.v1.connection_policy.ConnectionPolicyPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return ConnectionPolicyPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a ConnectionPolicyContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.voice.v1.connection_policy.ConnectionPolicyContext
        :rtype: twilio.rest.voice.v1.connection_policy.ConnectionPolicyContext
        """
        return ConnectionPolicyContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a ConnectionPolicyContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.voice.v1.connection_policy.ConnectionPolicyContext
        :rtype: twilio.rest.voice.v1.connection_policy.ConnectionPolicyContext
        """
        return ConnectionPolicyContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Voice.V1.ConnectionPolicyList>'


class ConnectionPolicyPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ConnectionPolicyPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.voice.v1.connection_policy.ConnectionPolicyPage
        :rtype: twilio.rest.voice.v1.connection_policy.ConnectionPolicyPage
        """
        super(ConnectionPolicyPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ConnectionPolicyInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.voice.v1.connection_policy.ConnectionPolicyInstance
        :rtype: twilio.rest.voice.v1.connection_policy.ConnectionPolicyInstance
        """
        return ConnectionPolicyInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Voice.V1.ConnectionPolicyPage>'


class ConnectionPolicyContext(InstanceContext):

    def __init__(self, version, sid):
        """
        Initialize the ConnectionPolicyContext

        :param Version version: Version that contains the resource
        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.voice.v1.connection_policy.ConnectionPolicyContext
        :rtype: twilio.rest.voice.v1.connection_policy.ConnectionPolicyContext
        """
        super(ConnectionPolicyContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/ConnectionPolicies/{sid}'.format(**self._solution)

        # Dependents
        self._targets = None

    def fetch(self):
        """
        Fetch the ConnectionPolicyInstance

        :returns: The fetched ConnectionPolicyInstance
        :rtype: twilio.rest.voice.v1.connection_policy.ConnectionPolicyInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ConnectionPolicyInstance(self._version, payload, sid=self._solution['sid'], )

    def update(self, friendly_name=values.unset):
        """
        Update the ConnectionPolicyInstance

        :param unicode friendly_name: A string to describe the resource

        :returns: The updated ConnectionPolicyInstance
        :rtype: twilio.rest.voice.v1.connection_policy.ConnectionPolicyInstance
        """
        data = values.of({'FriendlyName': friendly_name, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return ConnectionPolicyInstance(self._version, payload, sid=self._solution['sid'], )

    def delete(self):
        """
        Deletes the ConnectionPolicyInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    @property
    def targets(self):
        """
        Access the targets

        :returns: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetList
        :rtype: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetList
        """
        if self._targets is None:
            self._targets = ConnectionPolicyTargetList(
                self._version,
                connection_policy_sid=self._solution['sid'],
            )
        return self._targets

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Voice.V1.ConnectionPolicyContext {}>'.format(context)


class ConnectionPolicyInstance(InstanceResource):

    def __init__(self, version, payload, sid=None):
        """
        Initialize the ConnectionPolicyInstance

        :returns: twilio.rest.voice.v1.connection_policy.ConnectionPolicyInstance
        :rtype: twilio.rest.voice.v1.connection_policy.ConnectionPolicyInstance
        """
        super(ConnectionPolicyInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'sid': payload.get('sid'),
            'friendly_name': payload.get('friendly_name'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: ConnectionPolicyContext for this ConnectionPolicyInstance
        :rtype: twilio.rest.voice.v1.connection_policy.ConnectionPolicyContext
        """
        if self._context is None:
            self._context = ConnectionPolicyContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def date_created(self):
        """
        :returns: The RFC 2822 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The RFC 2822 date and time in GMT when the resource was last updated
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
        :returns: The URLs of related resources
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch the ConnectionPolicyInstance

        :returns: The fetched ConnectionPolicyInstance
        :rtype: twilio.rest.voice.v1.connection_policy.ConnectionPolicyInstance
        """
        return self._proxy.fetch()

    def update(self, friendly_name=values.unset):
        """
        Update the ConnectionPolicyInstance

        :param unicode friendly_name: A string to describe the resource

        :returns: The updated ConnectionPolicyInstance
        :rtype: twilio.rest.voice.v1.connection_policy.ConnectionPolicyInstance
        """
        return self._proxy.update(friendly_name=friendly_name, )

    def delete(self):
        """
        Deletes the ConnectionPolicyInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def targets(self):
        """
        Access the targets

        :returns: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetList
        :rtype: twilio.rest.voice.v1.connection_policy.connection_policy_target.ConnectionPolicyTargetList
        """
        return self._proxy.targets

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Voice.V1.ConnectionPolicyInstance {}>'.format(context)
