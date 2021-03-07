# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.domain import Domain
from twilio.rest.events.v1 import V1


class Events(Domain):

    def __init__(self, twilio):
        """
        Initialize the Events Domain

        :returns: Domain for Events
        :rtype: twilio.rest.events.Events
        """
        super(Events, self).__init__(twilio)

        self.base_url = 'https://events.twilio.com'

        # Versions
        self._v1 = None

    @property
    def v1(self):
        """
        :returns: Version v1 of events
        :rtype: twilio.rest.events.v1.V1
        """
        if self._v1 is None:
            self._v1 = V1(self)
        return self._v1

    @property
    def sinks(self):
        """
        :rtype: twilio.rest.events.v1.sink.SinkList
        """
        return self.v1.sinks

    @property
    def subscriptions(self):
        """
        :rtype: twilio.rest.events.v1.subscription.SubscriptionList
        """
        return self.v1.subscriptions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Events>'
