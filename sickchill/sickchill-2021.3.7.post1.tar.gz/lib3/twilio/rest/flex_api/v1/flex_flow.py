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


class FlexFlowList(ListResource):

    def __init__(self, version):
        """
        Initialize the FlexFlowList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.flex_api.v1.flex_flow.FlexFlowList
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowList
        """
        super(FlexFlowList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/FlexFlows'.format(**self._solution)

    def stream(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Streams FlexFlowInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode friendly_name: The `friendly_name` of the FlexFlow resources to read
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.flex_flow.FlexFlowInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(friendly_name=friendly_name, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Lists FlexFlowInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode friendly_name: The `friendly_name` of the FlexFlow resources to read
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.flex_flow.FlexFlowInstance]
        """
        return list(self.stream(friendly_name=friendly_name, limit=limit, page_size=page_size, ))

    def page(self, friendly_name=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of FlexFlowInstance records from the API.
        Request is executed immediately

        :param unicode friendly_name: The `friendly_name` of the FlexFlow resources to read
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FlexFlowInstance
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowPage
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return FlexFlowPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of FlexFlowInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FlexFlowInstance
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return FlexFlowPage(self._version, response, self._solution)

    def create(self, friendly_name, chat_service_sid, channel_type,
               contact_identity=values.unset, enabled=values.unset,
               integration_type=values.unset, integration_flow_sid=values.unset,
               integration_url=values.unset, integration_workspace_sid=values.unset,
               integration_workflow_sid=values.unset,
               integration_channel=values.unset, integration_timeout=values.unset,
               integration_priority=values.unset,
               integration_creation_on_message=values.unset,
               long_lived=values.unset, janitor_enabled=values.unset,
               integration_retry_count=values.unset):
        """
        Create the FlexFlowInstance

        :param unicode friendly_name: A string to describe the resource
        :param unicode chat_service_sid: The SID of the chat service
        :param FlexFlowInstance.ChannelType channel_type: The channel type
        :param unicode contact_identity: The channel contact's Identity
        :param bool enabled: Whether the new FlexFlow is enabled
        :param FlexFlowInstance.IntegrationType integration_type: The integration type
        :param unicode integration_flow_sid: The SID of the Flow
        :param unicode integration_url: The External Webhook URL
        :param unicode integration_workspace_sid: The Workspace SID for a new task
        :param unicode integration_workflow_sid: The Workflow SID for a new task
        :param unicode integration_channel: The task channel for a new task
        :param unicode integration_timeout: The task timeout in seconds for a new task
        :param unicode integration_priority: The task priority of a new task
        :param bool integration_creation_on_message: Whether to create a task when the first message arrives
        :param bool long_lived: Reuse this chat channel for future interactions with a contact
        :param bool janitor_enabled: Remove active Proxy sessions if the corresponding Task is deleted
        :param unicode integration_retry_count: The number of times to retry the webhook if the first attempt fails

        :returns: The created FlexFlowInstance
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'ChatServiceSid': chat_service_sid,
            'ChannelType': channel_type,
            'ContactIdentity': contact_identity,
            'Enabled': enabled,
            'IntegrationType': integration_type,
            'Integration.FlowSid': integration_flow_sid,
            'Integration.Url': integration_url,
            'Integration.WorkspaceSid': integration_workspace_sid,
            'Integration.WorkflowSid': integration_workflow_sid,
            'Integration.Channel': integration_channel,
            'Integration.Timeout': integration_timeout,
            'Integration.Priority': integration_priority,
            'Integration.CreationOnMessage': integration_creation_on_message,
            'LongLived': long_lived,
            'JanitorEnabled': janitor_enabled,
            'Integration.RetryCount': integration_retry_count,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return FlexFlowInstance(self._version, payload, )

    def get(self, sid):
        """
        Constructs a FlexFlowContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.flex_api.v1.flex_flow.FlexFlowContext
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowContext
        """
        return FlexFlowContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a FlexFlowContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.flex_api.v1.flex_flow.FlexFlowContext
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowContext
        """
        return FlexFlowContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.FlexFlowList>'


class FlexFlowPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the FlexFlowPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.flex_api.v1.flex_flow.FlexFlowPage
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowPage
        """
        super(FlexFlowPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FlexFlowInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.flex_api.v1.flex_flow.FlexFlowInstance
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowInstance
        """
        return FlexFlowInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.FlexFlowPage>'


class FlexFlowContext(InstanceContext):

    def __init__(self, version, sid):
        """
        Initialize the FlexFlowContext

        :param Version version: Version that contains the resource
        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.flex_api.v1.flex_flow.FlexFlowContext
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowContext
        """
        super(FlexFlowContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/FlexFlows/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch the FlexFlowInstance

        :returns: The fetched FlexFlowInstance
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return FlexFlowInstance(self._version, payload, sid=self._solution['sid'], )

    def update(self, friendly_name=values.unset, chat_service_sid=values.unset,
               channel_type=values.unset, contact_identity=values.unset,
               enabled=values.unset, integration_type=values.unset,
               integration_flow_sid=values.unset, integration_url=values.unset,
               integration_workspace_sid=values.unset,
               integration_workflow_sid=values.unset,
               integration_channel=values.unset, integration_timeout=values.unset,
               integration_priority=values.unset,
               integration_creation_on_message=values.unset,
               long_lived=values.unset, janitor_enabled=values.unset,
               integration_retry_count=values.unset):
        """
        Update the FlexFlowInstance

        :param unicode friendly_name: A string to describe the resource
        :param unicode chat_service_sid: The SID of the chat service
        :param FlexFlowInstance.ChannelType channel_type: The channel type
        :param unicode contact_identity: The channel contact's Identity
        :param bool enabled: Whether the FlexFlow is enabled
        :param FlexFlowInstance.IntegrationType integration_type: The integration type
        :param unicode integration_flow_sid: The SID of the Flow
        :param unicode integration_url: The External Webhook URL
        :param unicode integration_workspace_sid: The Workspace SID for a new task
        :param unicode integration_workflow_sid: The Workflow SID for a new task
        :param unicode integration_channel: task channel for a new task
        :param unicode integration_timeout: The task timeout in seconds for a new task
        :param unicode integration_priority: The task priority of a new task
        :param bool integration_creation_on_message: Whether to create a task when the first message arrives
        :param bool long_lived: Reuse this chat channel for future interactions with a contact
        :param bool janitor_enabled: Remove active Proxy sessions if the corresponding Task is deleted.
        :param unicode integration_retry_count: The number of times to retry the webhook if the first attempt fails

        :returns: The updated FlexFlowInstance
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'ChatServiceSid': chat_service_sid,
            'ChannelType': channel_type,
            'ContactIdentity': contact_identity,
            'Enabled': enabled,
            'IntegrationType': integration_type,
            'Integration.FlowSid': integration_flow_sid,
            'Integration.Url': integration_url,
            'Integration.WorkspaceSid': integration_workspace_sid,
            'Integration.WorkflowSid': integration_workflow_sid,
            'Integration.Channel': integration_channel,
            'Integration.Timeout': integration_timeout,
            'Integration.Priority': integration_priority,
            'Integration.CreationOnMessage': integration_creation_on_message,
            'LongLived': long_lived,
            'JanitorEnabled': janitor_enabled,
            'Integration.RetryCount': integration_retry_count,
        })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return FlexFlowInstance(self._version, payload, sid=self._solution['sid'], )

    def delete(self):
        """
        Deletes the FlexFlowInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.FlexFlowContext {}>'.format(context)


class FlexFlowInstance(InstanceResource):

    class ChannelType(object):
        WEB = "web"
        SMS = "sms"
        FACEBOOK = "facebook"
        WHATSAPP = "whatsapp"
        LINE = "line"
        CUSTOM = "custom"

    class IntegrationType(object):
        STUDIO = "studio"
        EXTERNAL = "external"
        TASK = "task"

    def __init__(self, version, payload, sid=None):
        """
        Initialize the FlexFlowInstance

        :returns: twilio.rest.flex_api.v1.flex_flow.FlexFlowInstance
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowInstance
        """
        super(FlexFlowInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'sid': payload.get('sid'),
            'friendly_name': payload.get('friendly_name'),
            'chat_service_sid': payload.get('chat_service_sid'),
            'channel_type': payload.get('channel_type'),
            'contact_identity': payload.get('contact_identity'),
            'enabled': payload.get('enabled'),
            'integration_type': payload.get('integration_type'),
            'integration': payload.get('integration'),
            'long_lived': payload.get('long_lived'),
            'janitor_enabled': payload.get('janitor_enabled'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: FlexFlowContext for this FlexFlowInstance
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowContext
        """
        if self._context is None:
            self._context = FlexFlowContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

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
    def chat_service_sid(self):
        """
        :returns: The SID of the chat service
        :rtype: unicode
        """
        return self._properties['chat_service_sid']

    @property
    def channel_type(self):
        """
        :returns: The channel type
        :rtype: FlexFlowInstance.ChannelType
        """
        return self._properties['channel_type']

    @property
    def contact_identity(self):
        """
        :returns: The channel contact's Identity
        :rtype: unicode
        """
        return self._properties['contact_identity']

    @property
    def enabled(self):
        """
        :returns: Whether the FlexFlow is enabled
        :rtype: bool
        """
        return self._properties['enabled']

    @property
    def integration_type(self):
        """
        :returns: The integration type
        :rtype: FlexFlowInstance.IntegrationType
        """
        return self._properties['integration_type']

    @property
    def integration(self):
        """
        :returns: An object that contains specific parameters for the integration
        :rtype: dict
        """
        return self._properties['integration']

    @property
    def long_lived(self):
        """
        :returns: Re-use this chat channel for future interactions with a contact
        :rtype: bool
        """
        return self._properties['long_lived']

    @property
    def janitor_enabled(self):
        """
        :returns: Remove active Proxy sessions if the corresponding Task is deleted.
        :rtype: bool
        """
        return self._properties['janitor_enabled']

    @property
    def url(self):
        """
        :returns: The absolute URL of the FlexFlow resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch the FlexFlowInstance

        :returns: The fetched FlexFlowInstance
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowInstance
        """
        return self._proxy.fetch()

    def update(self, friendly_name=values.unset, chat_service_sid=values.unset,
               channel_type=values.unset, contact_identity=values.unset,
               enabled=values.unset, integration_type=values.unset,
               integration_flow_sid=values.unset, integration_url=values.unset,
               integration_workspace_sid=values.unset,
               integration_workflow_sid=values.unset,
               integration_channel=values.unset, integration_timeout=values.unset,
               integration_priority=values.unset,
               integration_creation_on_message=values.unset,
               long_lived=values.unset, janitor_enabled=values.unset,
               integration_retry_count=values.unset):
        """
        Update the FlexFlowInstance

        :param unicode friendly_name: A string to describe the resource
        :param unicode chat_service_sid: The SID of the chat service
        :param FlexFlowInstance.ChannelType channel_type: The channel type
        :param unicode contact_identity: The channel contact's Identity
        :param bool enabled: Whether the FlexFlow is enabled
        :param FlexFlowInstance.IntegrationType integration_type: The integration type
        :param unicode integration_flow_sid: The SID of the Flow
        :param unicode integration_url: The External Webhook URL
        :param unicode integration_workspace_sid: The Workspace SID for a new task
        :param unicode integration_workflow_sid: The Workflow SID for a new task
        :param unicode integration_channel: task channel for a new task
        :param unicode integration_timeout: The task timeout in seconds for a new task
        :param unicode integration_priority: The task priority of a new task
        :param bool integration_creation_on_message: Whether to create a task when the first message arrives
        :param bool long_lived: Reuse this chat channel for future interactions with a contact
        :param bool janitor_enabled: Remove active Proxy sessions if the corresponding Task is deleted.
        :param unicode integration_retry_count: The number of times to retry the webhook if the first attempt fails

        :returns: The updated FlexFlowInstance
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            chat_service_sid=chat_service_sid,
            channel_type=channel_type,
            contact_identity=contact_identity,
            enabled=enabled,
            integration_type=integration_type,
            integration_flow_sid=integration_flow_sid,
            integration_url=integration_url,
            integration_workspace_sid=integration_workspace_sid,
            integration_workflow_sid=integration_workflow_sid,
            integration_channel=integration_channel,
            integration_timeout=integration_timeout,
            integration_priority=integration_priority,
            integration_creation_on_message=integration_creation_on_message,
            long_lived=long_lived,
            janitor_enabled=janitor_enabled,
            integration_retry_count=integration_retry_count,
        )

    def delete(self):
        """
        Deletes the FlexFlowInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.FlexFlowInstance {}>'.format(context)
