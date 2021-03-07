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


class WebhookList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, service_sid):
        """
        Initialize the WebhookList

        :param Version version: Version that contains the resource
        :param service_sid: Service Sid.

        :returns: twilio.rest.verify.v2.service.webhook.WebhookList
        :rtype: twilio.rest.verify.v2.service.webhook.WebhookList
        """
        super(WebhookList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, }
        self._uri = '/Services/{service_sid}/Webhooks'.format(**self._solution)

    def create(self, friendly_name, event_types, webhook_url, status=values.unset):
        """
        Create the WebhookInstance

        :param unicode friendly_name: The string that you assigned to describe the webhook
        :param unicode event_types: The array of events that this Webhook is subscribed to.
        :param unicode webhook_url: The URL associated with this Webhook.
        :param WebhookInstance.Status status: The webhook status

        :returns: The created WebhookInstance
        :rtype: twilio.rest.verify.v2.service.webhook.WebhookInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'EventTypes': serialize.map(event_types, lambda e: e),
            'WebhookUrl': webhook_url,
            'Status': status,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return WebhookInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def stream(self, limit=None, page_size=None):
        """
        Streams WebhookInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.verify.v2.service.webhook.WebhookInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists WebhookInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.service.webhook.WebhookInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of WebhookInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of WebhookInstance
        :rtype: twilio.rest.verify.v2.service.webhook.WebhookPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return WebhookPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of WebhookInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of WebhookInstance
        :rtype: twilio.rest.verify.v2.service.webhook.WebhookPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return WebhookPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a WebhookContext

        :param sid: The unique string that identifies the resource to fetch

        :returns: twilio.rest.verify.v2.service.webhook.WebhookContext
        :rtype: twilio.rest.verify.v2.service.webhook.WebhookContext
        """
        return WebhookContext(self._version, service_sid=self._solution['service_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a WebhookContext

        :param sid: The unique string that identifies the resource to fetch

        :returns: twilio.rest.verify.v2.service.webhook.WebhookContext
        :rtype: twilio.rest.verify.v2.service.webhook.WebhookContext
        """
        return WebhookContext(self._version, service_sid=self._solution['service_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.WebhookList>'


class WebhookPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the WebhookPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: Service Sid.

        :returns: twilio.rest.verify.v2.service.webhook.WebhookPage
        :rtype: twilio.rest.verify.v2.service.webhook.WebhookPage
        """
        super(WebhookPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of WebhookInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.verify.v2.service.webhook.WebhookInstance
        :rtype: twilio.rest.verify.v2.service.webhook.WebhookInstance
        """
        return WebhookInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.WebhookPage>'


class WebhookContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, service_sid, sid):
        """
        Initialize the WebhookContext

        :param Version version: Version that contains the resource
        :param service_sid: Service Sid.
        :param sid: The unique string that identifies the resource to fetch

        :returns: twilio.rest.verify.v2.service.webhook.WebhookContext
        :rtype: twilio.rest.verify.v2.service.webhook.WebhookContext
        """
        super(WebhookContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'sid': sid, }
        self._uri = '/Services/{service_sid}/Webhooks/{sid}'.format(**self._solution)

    def update(self, friendly_name=values.unset, event_types=values.unset,
               webhook_url=values.unset, status=values.unset):
        """
        Update the WebhookInstance

        :param unicode friendly_name: The string that you assigned to describe the webhook
        :param unicode event_types: The array of events that this Webhook is subscribed to.
        :param unicode webhook_url: The URL associated with this Webhook.
        :param WebhookInstance.Status status: The webhook status

        :returns: The updated WebhookInstance
        :rtype: twilio.rest.verify.v2.service.webhook.WebhookInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'EventTypes': serialize.map(event_types, lambda e: e),
            'WebhookUrl': webhook_url,
            'Status': status,
        })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return WebhookInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the WebhookInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    def fetch(self):
        """
        Fetch the WebhookInstance

        :returns: The fetched WebhookInstance
        :rtype: twilio.rest.verify.v2.service.webhook.WebhookInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return WebhookInstance(
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
        return '<Twilio.Verify.V2.WebhookContext {}>'.format(context)


class WebhookInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    class Status(object):
        ENABLED = "enabled"
        DISABLED = "disabled"

    class Methods(object):
        GET = "GET"
        POST = "POST"

    def __init__(self, version, payload, service_sid, sid=None):
        """
        Initialize the WebhookInstance

        :returns: twilio.rest.verify.v2.service.webhook.WebhookInstance
        :rtype: twilio.rest.verify.v2.service.webhook.WebhookInstance
        """
        super(WebhookInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'service_sid': payload.get('service_sid'),
            'account_sid': payload.get('account_sid'),
            'friendly_name': payload.get('friendly_name'),
            'event_types': payload.get('event_types'),
            'status': payload.get('status'),
            'webhook_url': payload.get('webhook_url'),
            'webhook_method': payload.get('webhook_method'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
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

        :returns: WebhookContext for this WebhookInstance
        :rtype: twilio.rest.verify.v2.service.webhook.WebhookContext
        """
        if self._context is None:
            self._context = WebhookContext(
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
    def service_sid(self):
        """
        :returns: Service Sid.
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the webhook
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def event_types(self):
        """
        :returns: The array of events that this Webhook is subscribed to.
        :rtype: unicode
        """
        return self._properties['event_types']

    @property
    def status(self):
        """
        :returns: The webhook status
        :rtype: WebhookInstance.Status
        """
        return self._properties['status']

    @property
    def webhook_url(self):
        """
        :returns: The URL associated with this Webhook.
        :rtype: unicode
        """
        return self._properties['webhook_url']

    @property
    def webhook_method(self):
        """
        :returns: The method used when calling the webhook's URL.
        :rtype: WebhookInstance.Methods
        """
        return self._properties['webhook_method']

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
        :returns: The absolute URL of the Webhook resource
        :rtype: unicode
        """
        return self._properties['url']

    def update(self, friendly_name=values.unset, event_types=values.unset,
               webhook_url=values.unset, status=values.unset):
        """
        Update the WebhookInstance

        :param unicode friendly_name: The string that you assigned to describe the webhook
        :param unicode event_types: The array of events that this Webhook is subscribed to.
        :param unicode webhook_url: The URL associated with this Webhook.
        :param WebhookInstance.Status status: The webhook status

        :returns: The updated WebhookInstance
        :rtype: twilio.rest.verify.v2.service.webhook.WebhookInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            event_types=event_types,
            webhook_url=webhook_url,
            status=status,
        )

    def delete(self):
        """
        Deletes the WebhookInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def fetch(self):
        """
        Fetch the WebhookInstance

        :returns: The fetched WebhookInstance
        :rtype: twilio.rest.verify.v2.service.webhook.WebhookInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.WebhookInstance {}>'.format(context)
