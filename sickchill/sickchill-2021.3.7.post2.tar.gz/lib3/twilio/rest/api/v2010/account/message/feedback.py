# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class FeedbackList(ListResource):

    def __init__(self, version, account_sid, message_sid):
        """
        Initialize the FeedbackList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the Account that created the resource
        :param message_sid: The SID of the Message resource for which the feedback was provided

        :returns: twilio.rest.api.v2010.account.message.feedback.FeedbackList
        :rtype: twilio.rest.api.v2010.account.message.feedback.FeedbackList
        """
        super(FeedbackList, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'message_sid': message_sid, }
        self._uri = '/Accounts/{account_sid}/Messages/{message_sid}/Feedback.json'.format(**self._solution)

    def create(self, outcome=values.unset):
        """
        Create the FeedbackInstance

        :param FeedbackInstance.Outcome outcome: Whether the feedback has arrived

        :returns: The created FeedbackInstance
        :rtype: twilio.rest.api.v2010.account.message.feedback.FeedbackInstance
        """
        data = values.of({'Outcome': outcome, })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return FeedbackInstance(
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
        return '<Twilio.Api.V2010.FeedbackList>'


class FeedbackPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the FeedbackPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The SID of the Account that created the resource
        :param message_sid: The SID of the Message resource for which the feedback was provided

        :returns: twilio.rest.api.v2010.account.message.feedback.FeedbackPage
        :rtype: twilio.rest.api.v2010.account.message.feedback.FeedbackPage
        """
        super(FeedbackPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FeedbackInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.message.feedback.FeedbackInstance
        :rtype: twilio.rest.api.v2010.account.message.feedback.FeedbackInstance
        """
        return FeedbackInstance(
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
        return '<Twilio.Api.V2010.FeedbackPage>'


class FeedbackInstance(InstanceResource):

    class Outcome(object):
        CONFIRMED = "confirmed"
        UNCONFIRMED = "unconfirmed"

    def __init__(self, version, payload, account_sid, message_sid):
        """
        Initialize the FeedbackInstance

        :returns: twilio.rest.api.v2010.account.message.feedback.FeedbackInstance
        :rtype: twilio.rest.api.v2010.account.message.feedback.FeedbackInstance
        """
        super(FeedbackInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'message_sid': payload.get('message_sid'),
            'outcome': payload.get('outcome'),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
            'uri': payload.get('uri'),
        }

        # Context
        self._context = None
        self._solution = {'account_sid': account_sid, 'message_sid': message_sid, }

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def message_sid(self):
        """
        :returns: The SID of the Message resource for which the feedback was provided
        :rtype: unicode
        """
        return self._properties['message_sid']

    @property
    def outcome(self):
        """
        :returns: Whether the feedback has arrived
        :rtype: FeedbackInstance.Outcome
        """
        return self._properties['outcome']

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
    def uri(self):
        """
        :returns: The URI of the resource, relative to `https://api.twilio.com`
        :rtype: unicode
        """
        return self._properties['uri']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.FeedbackInstance>'
