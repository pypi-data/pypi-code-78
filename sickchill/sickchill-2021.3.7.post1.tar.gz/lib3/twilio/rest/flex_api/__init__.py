# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.domain import Domain
from twilio.rest.flex_api.v1 import V1


class FlexApi(Domain):

    def __init__(self, twilio):
        """
        Initialize the FlexApi Domain

        :returns: Domain for FlexApi
        :rtype: twilio.rest.flex_api.FlexApi
        """
        super(FlexApi, self).__init__(twilio)

        self.base_url = 'https://flex-api.twilio.com'

        # Versions
        self._v1 = None

    @property
    def v1(self):
        """
        :returns: Version v1 of flex_api
        :rtype: twilio.rest.flex_api.v1.V1
        """
        if self._v1 is None:
            self._v1 = V1(self)
        return self._v1

    @property
    def channel(self):
        """
        :rtype: twilio.rest.flex_api.v1.channel.ChannelList
        """
        return self.v1.channel

    @property
    def configuration(self):
        """
        :rtype: twilio.rest.flex_api.v1.configuration.ConfigurationList
        """
        return self.v1.configuration

    @property
    def flex_flow(self):
        """
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowList
        """
        return self.v1.flex_flow

    @property
    def web_channel(self):
        """
        :rtype: twilio.rest.flex_api.v1.web_channel.WebChannelList
        """
        return self.v1.web_channel

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi>'
