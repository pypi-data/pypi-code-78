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
from twilio.rest.ip_messaging.v2.service.channel.invite import InviteList
from twilio.rest.ip_messaging.v2.service.channel.member import MemberList
from twilio.rest.ip_messaging.v2.service.channel.message import MessageList
from twilio.rest.ip_messaging.v2.service.channel.webhook import WebhookList


class ChannelList(ListResource):

    def __init__(self, version, service_sid):
        """
        Initialize the ChannelList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service that the resource is associated with

        :returns: twilio.rest.chat.v2.service.channel.ChannelList
        :rtype: twilio.rest.chat.v2.service.channel.ChannelList
        """
        super(ChannelList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, }
        self._uri = '/Services/{service_sid}/Channels'.format(**self._solution)

    def create(self, friendly_name=values.unset, unique_name=values.unset,
               attributes=values.unset, type=values.unset,
               date_created=values.unset, date_updated=values.unset,
               created_by=values.unset, x_twilio_webhook_enabled=values.unset):
        """
        Create the ChannelInstance

        :param unicode friendly_name: A string to describe the new resource
        :param unicode unique_name: An application-defined string that uniquely identifies the Channel resource
        :param unicode attributes: A valid JSON string that contains application-specific data
        :param ChannelInstance.ChannelType type: The visibility of the channel
        :param datetime date_created: The ISO 8601 date and time in GMT when the resource was created
        :param datetime date_updated: The ISO 8601 date and time in GMT when the resource was updated
        :param unicode created_by: The identity of the User that created the Channel
        :param ChannelInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: The created ChannelInstance
        :rtype: twilio.rest.chat.v2.service.channel.ChannelInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'UniqueName': unique_name,
            'Attributes': attributes,
            'Type': type,
            'DateCreated': serialize.iso8601_datetime(date_created),
            'DateUpdated': serialize.iso8601_datetime(date_updated),
            'CreatedBy': created_by,
        })
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })

        payload = self._version.create(method='POST', uri=self._uri, data=data, headers=headers, )

        return ChannelInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def stream(self, type=values.unset, limit=None, page_size=None):
        """
        Streams ChannelInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param ChannelInstance.ChannelType type: The visibility of the channel to read
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v2.service.channel.ChannelInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(type=type, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, type=values.unset, limit=None, page_size=None):
        """
        Lists ChannelInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param ChannelInstance.ChannelType type: The visibility of the channel to read
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v2.service.channel.ChannelInstance]
        """
        return list(self.stream(type=type, limit=limit, page_size=page_size, ))

    def page(self, type=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ChannelInstance records from the API.
        Request is executed immediately

        :param ChannelInstance.ChannelType type: The visibility of the channel to read
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ChannelInstance
        :rtype: twilio.rest.chat.v2.service.channel.ChannelPage
        """
        data = values.of({
            'Type': serialize.map(type, lambda e: e),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return ChannelPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ChannelInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ChannelInstance
        :rtype: twilio.rest.chat.v2.service.channel.ChannelPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return ChannelPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a ChannelContext

        :param sid: The SID of the resource

        :returns: twilio.rest.chat.v2.service.channel.ChannelContext
        :rtype: twilio.rest.chat.v2.service.channel.ChannelContext
        """
        return ChannelContext(self._version, service_sid=self._solution['service_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a ChannelContext

        :param sid: The SID of the resource

        :returns: twilio.rest.chat.v2.service.channel.ChannelContext
        :rtype: twilio.rest.chat.v2.service.channel.ChannelContext
        """
        return ChannelContext(self._version, service_sid=self._solution['service_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V2.ChannelList>'


class ChannelPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ChannelPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The SID of the Service that the resource is associated with

        :returns: twilio.rest.chat.v2.service.channel.ChannelPage
        :rtype: twilio.rest.chat.v2.service.channel.ChannelPage
        """
        super(ChannelPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ChannelInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.chat.v2.service.channel.ChannelInstance
        :rtype: twilio.rest.chat.v2.service.channel.ChannelInstance
        """
        return ChannelInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V2.ChannelPage>'


class ChannelContext(InstanceContext):

    def __init__(self, version, service_sid, sid):
        """
        Initialize the ChannelContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the resource from
        :param sid: The SID of the resource

        :returns: twilio.rest.chat.v2.service.channel.ChannelContext
        :rtype: twilio.rest.chat.v2.service.channel.ChannelContext
        """
        super(ChannelContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'sid': sid, }
        self._uri = '/Services/{service_sid}/Channels/{sid}'.format(**self._solution)

        # Dependents
        self._members = None
        self._messages = None
        self._invites = None
        self._webhooks = None

    def fetch(self):
        """
        Fetch the ChannelInstance

        :returns: The fetched ChannelInstance
        :rtype: twilio.rest.chat.v2.service.channel.ChannelInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ChannelInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    def delete(self, x_twilio_webhook_enabled=values.unset):
        """
        Deletes the ChannelInstance

        :param ChannelInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })

        return self._version.delete(method='DELETE', uri=self._uri, headers=headers, )

    def update(self, friendly_name=values.unset, unique_name=values.unset,
               attributes=values.unset, date_created=values.unset,
               date_updated=values.unset, created_by=values.unset,
               x_twilio_webhook_enabled=values.unset):
        """
        Update the ChannelInstance

        :param unicode friendly_name: A string to describe the resource
        :param unicode unique_name: An application-defined string that uniquely identifies the resource
        :param unicode attributes: A valid JSON string that contains application-specific data
        :param datetime date_created: The ISO 8601 date and time in GMT when the resource was created
        :param datetime date_updated: The ISO 8601 date and time in GMT when the resource was updated
        :param unicode created_by: The identity of the User that created the Channel
        :param ChannelInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: The updated ChannelInstance
        :rtype: twilio.rest.chat.v2.service.channel.ChannelInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'UniqueName': unique_name,
            'Attributes': attributes,
            'DateCreated': serialize.iso8601_datetime(date_created),
            'DateUpdated': serialize.iso8601_datetime(date_updated),
            'CreatedBy': created_by,
        })
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, headers=headers, )

        return ChannelInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    @property
    def members(self):
        """
        Access the members

        :returns: twilio.rest.chat.v2.service.channel.member.MemberList
        :rtype: twilio.rest.chat.v2.service.channel.member.MemberList
        """
        if self._members is None:
            self._members = MemberList(
                self._version,
                service_sid=self._solution['service_sid'],
                channel_sid=self._solution['sid'],
            )
        return self._members

    @property
    def messages(self):
        """
        Access the messages

        :returns: twilio.rest.chat.v2.service.channel.message.MessageList
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageList
        """
        if self._messages is None:
            self._messages = MessageList(
                self._version,
                service_sid=self._solution['service_sid'],
                channel_sid=self._solution['sid'],
            )
        return self._messages

    @property
    def invites(self):
        """
        Access the invites

        :returns: twilio.rest.chat.v2.service.channel.invite.InviteList
        :rtype: twilio.rest.chat.v2.service.channel.invite.InviteList
        """
        if self._invites is None:
            self._invites = InviteList(
                self._version,
                service_sid=self._solution['service_sid'],
                channel_sid=self._solution['sid'],
            )
        return self._invites

    @property
    def webhooks(self):
        """
        Access the webhooks

        :returns: twilio.rest.chat.v2.service.channel.webhook.WebhookList
        :rtype: twilio.rest.chat.v2.service.channel.webhook.WebhookList
        """
        if self._webhooks is None:
            self._webhooks = WebhookList(
                self._version,
                service_sid=self._solution['service_sid'],
                channel_sid=self._solution['sid'],
            )
        return self._webhooks

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.IpMessaging.V2.ChannelContext {}>'.format(context)


class ChannelInstance(InstanceResource):

    class ChannelType(object):
        PUBLIC = "public"
        PRIVATE = "private"

    class WebhookEnabledType(object):
        TRUE = "true"
        FALSE = "false"

    def __init__(self, version, payload, service_sid, sid=None):
        """
        Initialize the ChannelInstance

        :returns: twilio.rest.chat.v2.service.channel.ChannelInstance
        :rtype: twilio.rest.chat.v2.service.channel.ChannelInstance
        """
        super(ChannelInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'friendly_name': payload.get('friendly_name'),
            'unique_name': payload.get('unique_name'),
            'attributes': payload.get('attributes'),
            'type': payload.get('type'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'created_by': payload.get('created_by'),
            'members_count': deserialize.integer(payload.get('members_count')),
            'messages_count': deserialize.integer(payload.get('messages_count')),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        # Context
        self._context = None
        self._solution = {'service_sid': service_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: ChannelContext for this ChannelInstance
        :rtype: twilio.rest.chat.v2.service.channel.ChannelContext
        """
        if self._context is None:
            self._context = ChannelContext(
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
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def attributes(self):
        """
        :returns: The JSON string that stores application-specific data
        :rtype: unicode
        """
        return self._properties['attributes']

    @property
    def type(self):
        """
        :returns: The visibility of the channel. Can be: `public` or `private`
        :rtype: ChannelInstance.ChannelType
        """
        return self._properties['type']

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
    def created_by(self):
        """
        :returns: The identity of the User that created the channel
        :rtype: unicode
        """
        return self._properties['created_by']

    @property
    def members_count(self):
        """
        :returns: The number of Members in the Channel
        :rtype: unicode
        """
        return self._properties['members_count']

    @property
    def messages_count(self):
        """
        :returns: The number of Messages that have been passed in the Channel
        :rtype: unicode
        """
        return self._properties['messages_count']

    @property
    def url(self):
        """
        :returns: The absolute URL of the Channel resource
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: Absolute URLs to access the Members, Messages , Invites and, if it exists, the last Message for the Channel
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch the ChannelInstance

        :returns: The fetched ChannelInstance
        :rtype: twilio.rest.chat.v2.service.channel.ChannelInstance
        """
        return self._proxy.fetch()

    def delete(self, x_twilio_webhook_enabled=values.unset):
        """
        Deletes the ChannelInstance

        :param ChannelInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete(x_twilio_webhook_enabled=x_twilio_webhook_enabled, )

    def update(self, friendly_name=values.unset, unique_name=values.unset,
               attributes=values.unset, date_created=values.unset,
               date_updated=values.unset, created_by=values.unset,
               x_twilio_webhook_enabled=values.unset):
        """
        Update the ChannelInstance

        :param unicode friendly_name: A string to describe the resource
        :param unicode unique_name: An application-defined string that uniquely identifies the resource
        :param unicode attributes: A valid JSON string that contains application-specific data
        :param datetime date_created: The ISO 8601 date and time in GMT when the resource was created
        :param datetime date_updated: The ISO 8601 date and time in GMT when the resource was updated
        :param unicode created_by: The identity of the User that created the Channel
        :param ChannelInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: The updated ChannelInstance
        :rtype: twilio.rest.chat.v2.service.channel.ChannelInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            unique_name=unique_name,
            attributes=attributes,
            date_created=date_created,
            date_updated=date_updated,
            created_by=created_by,
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
        )

    @property
    def members(self):
        """
        Access the members

        :returns: twilio.rest.chat.v2.service.channel.member.MemberList
        :rtype: twilio.rest.chat.v2.service.channel.member.MemberList
        """
        return self._proxy.members

    @property
    def messages(self):
        """
        Access the messages

        :returns: twilio.rest.chat.v2.service.channel.message.MessageList
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageList
        """
        return self._proxy.messages

    @property
    def invites(self):
        """
        Access the invites

        :returns: twilio.rest.chat.v2.service.channel.invite.InviteList
        :rtype: twilio.rest.chat.v2.service.channel.invite.InviteList
        """
        return self._proxy.invites

    @property
    def webhooks(self):
        """
        Access the webhooks

        :returns: twilio.rest.chat.v2.service.channel.webhook.WebhookList
        :rtype: twilio.rest.chat.v2.service.channel.webhook.WebhookList
        """
        return self._proxy.webhooks

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.IpMessaging.V2.ChannelInstance {}>'.format(context)
