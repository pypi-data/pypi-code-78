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


class PhoneNumberList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid):
        """
        Initialize the PhoneNumberList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service that the resource is associated with

        :returns: twilio.rest.messaging.v1.service.phone_number.PhoneNumberList
        :rtype: twilio.rest.messaging.v1.service.phone_number.PhoneNumberList
        """
        super(PhoneNumberList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, }
        self._uri = '/Services/{service_sid}/PhoneNumbers'.format(**self._solution)

    def create(self, phone_number_sid):
        """
        Create the PhoneNumberInstance

        :param unicode phone_number_sid: The SID of the Phone Number being added to the Service

        :returns: The created PhoneNumberInstance
        :rtype: twilio.rest.messaging.v1.service.phone_number.PhoneNumberInstance
        """
        data = values.of({'PhoneNumberSid': phone_number_sid, })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return PhoneNumberInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def stream(self, limit=None, page_size=None):
        """
        Streams PhoneNumberInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.messaging.v1.service.phone_number.PhoneNumberInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists PhoneNumberInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.messaging.v1.service.phone_number.PhoneNumberInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of PhoneNumberInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of PhoneNumberInstance
        :rtype: twilio.rest.messaging.v1.service.phone_number.PhoneNumberPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return PhoneNumberPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of PhoneNumberInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of PhoneNumberInstance
        :rtype: twilio.rest.messaging.v1.service.phone_number.PhoneNumberPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return PhoneNumberPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a PhoneNumberContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.messaging.v1.service.phone_number.PhoneNumberContext
        :rtype: twilio.rest.messaging.v1.service.phone_number.PhoneNumberContext
        """
        return PhoneNumberContext(self._version, service_sid=self._solution['service_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a PhoneNumberContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.messaging.v1.service.phone_number.PhoneNumberContext
        :rtype: twilio.rest.messaging.v1.service.phone_number.PhoneNumberContext
        """
        return PhoneNumberContext(self._version, service_sid=self._solution['service_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.PhoneNumberList>'


class PhoneNumberPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the PhoneNumberPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The SID of the Service that the resource is associated with

        :returns: twilio.rest.messaging.v1.service.phone_number.PhoneNumberPage
        :rtype: twilio.rest.messaging.v1.service.phone_number.PhoneNumberPage
        """
        super(PhoneNumberPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of PhoneNumberInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.messaging.v1.service.phone_number.PhoneNumberInstance
        :rtype: twilio.rest.messaging.v1.service.phone_number.PhoneNumberInstance
        """
        return PhoneNumberInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.PhoneNumberPage>'


class PhoneNumberContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, sid):
        """
        Initialize the PhoneNumberContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the resource from
        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.messaging.v1.service.phone_number.PhoneNumberContext
        :rtype: twilio.rest.messaging.v1.service.phone_number.PhoneNumberContext
        """
        super(PhoneNumberContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'sid': sid, }
        self._uri = '/Services/{service_sid}/PhoneNumbers/{sid}'.format(**self._solution)

    def delete(self):
        """
        Deletes the PhoneNumberInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    def fetch(self):
        """
        Fetch the PhoneNumberInstance

        :returns: The fetched PhoneNumberInstance
        :rtype: twilio.rest.messaging.v1.service.phone_number.PhoneNumberInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return PhoneNumberInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.PhoneNumberContext {}>'.format(context)


class PhoneNumberInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, payload, service_sid, sid=None):
        """
        Initialize the PhoneNumberInstance

        :returns: twilio.rest.messaging.v1.service.phone_number.PhoneNumberInstance
        :rtype: twilio.rest.messaging.v1.service.phone_number.PhoneNumberInstance
        """
        super(PhoneNumberInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'phone_number': payload.get('phone_number'),
            'country_code': payload.get('country_code'),
            'capabilities': payload.get('capabilities'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'service_sid': service_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: PhoneNumberContext for this PhoneNumberInstance
        :rtype: twilio.rest.messaging.v1.service.phone_number.PhoneNumberContext
        """
        if self._context is None:
            self._context = PhoneNumberContext(
                self._version,
                service_sid=self._solution['service_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The SID of the Service that the resource is associated with
        :rtype: unicode
        """
        return self._properties['service_sid']

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
        :returns: The ISO 8601 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def phone_number(self):
        """
        :returns: The phone number in E.164 format
        :rtype: unicode
        """
        return self._properties['phone_number']

    @property
    def country_code(self):
        """
        :returns: The 2-character ISO Country Code of the number
        :rtype: unicode
        """
        return self._properties['country_code']

    @property
    def capabilities(self):
        """
        :returns: An array of values that describe whether the number can receive calls or messages
        :rtype: unicode
        """
        return self._properties['capabilities']

    @property
    def url(self):
        """
        :returns: The absolute URL of the PhoneNumber resource
        :rtype: unicode
        """
        return self._properties['url']

    def delete(self):
        """
        Deletes the PhoneNumberInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def fetch(self):
        """
        Fetch the PhoneNumberInstance

        :returns: The fetched PhoneNumberInstance
        :rtype: twilio.rest.messaging.v1.service.phone_number.PhoneNumberInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.PhoneNumberInstance {}>'.format(context)
