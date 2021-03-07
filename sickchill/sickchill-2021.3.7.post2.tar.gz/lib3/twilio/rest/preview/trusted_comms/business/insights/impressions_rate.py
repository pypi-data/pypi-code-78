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


class ImpressionsRateList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, business_sid):
        """
        Initialize the ImpressionsRateList

        :param Version version: Version that contains the resource
        :param business_sid: A string that uniquely identifies this Business.

        :returns: twilio.rest.preview.trusted_comms.business.insights.impressions_rate.ImpressionsRateList
        :rtype: twilio.rest.preview.trusted_comms.business.insights.impressions_rate.ImpressionsRateList
        """
        super(ImpressionsRateList, self).__init__(version)

        # Path Solution
        self._solution = {'business_sid': business_sid, }

    def get(self):
        """
        Constructs a ImpressionsRateContext

        :returns: twilio.rest.preview.trusted_comms.business.insights.impressions_rate.ImpressionsRateContext
        :rtype: twilio.rest.preview.trusted_comms.business.insights.impressions_rate.ImpressionsRateContext
        """
        return ImpressionsRateContext(self._version, business_sid=self._solution['business_sid'], )

    def __call__(self):
        """
        Constructs a ImpressionsRateContext

        :returns: twilio.rest.preview.trusted_comms.business.insights.impressions_rate.ImpressionsRateContext
        :rtype: twilio.rest.preview.trusted_comms.business.insights.impressions_rate.ImpressionsRateContext
        """
        return ImpressionsRateContext(self._version, business_sid=self._solution['business_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.TrustedComms.ImpressionsRateList>'


class ImpressionsRatePage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the ImpressionsRatePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param business_sid: A string that uniquely identifies this Business.

        :returns: twilio.rest.preview.trusted_comms.business.insights.impressions_rate.ImpressionsRatePage
        :rtype: twilio.rest.preview.trusted_comms.business.insights.impressions_rate.ImpressionsRatePage
        """
        super(ImpressionsRatePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ImpressionsRateInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.trusted_comms.business.insights.impressions_rate.ImpressionsRateInstance
        :rtype: twilio.rest.preview.trusted_comms.business.insights.impressions_rate.ImpressionsRateInstance
        """
        return ImpressionsRateInstance(self._version, payload, business_sid=self._solution['business_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.TrustedComms.ImpressionsRatePage>'


class ImpressionsRateContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, business_sid):
        """
        Initialize the ImpressionsRateContext

        :param Version version: Version that contains the resource
        :param business_sid: Business Sid.

        :returns: twilio.rest.preview.trusted_comms.business.insights.impressions_rate.ImpressionsRateContext
        :rtype: twilio.rest.preview.trusted_comms.business.insights.impressions_rate.ImpressionsRateContext
        """
        super(ImpressionsRateContext, self).__init__(version)

        # Path Solution
        self._solution = {'business_sid': business_sid, }
        self._uri = '/Businesses/{business_sid}/Insights/ImpressionsRate'.format(**self._solution)

    def fetch(self, brand_sid=values.unset, branded_channel_sid=values.unset,
              phone_number_sid=values.unset, country=values.unset,
              start=values.unset, end=values.unset, interval=values.unset):
        """
        Fetch the ImpressionsRateInstance

        :param unicode brand_sid: Brand Sid.
        :param unicode branded_channel_sid: Branded Channel Sid.
        :param unicode phone_number_sid: Phone Number Sid.
        :param unicode country: Country 2-letter ISO 3166 code.
        :param datetime start: The start date that for this Impressions Rate.
        :param datetime end: The end date that for this Impressions Rate.
        :param ImpressionsRateInstance.Intervals interval: The Interval of this Impressions Rate.

        :returns: The fetched ImpressionsRateInstance
        :rtype: twilio.rest.preview.trusted_comms.business.insights.impressions_rate.ImpressionsRateInstance
        """
        data = values.of({
            'BrandSid': brand_sid,
            'BrandedChannelSid': branded_channel_sid,
            'PhoneNumberSid': phone_number_sid,
            'Country': country,
            'Start': serialize.iso8601_datetime(start),
            'End': serialize.iso8601_datetime(end),
            'Interval': interval,
        })

        payload = self._version.fetch(method='GET', uri=self._uri, params=data, )

        return ImpressionsRateInstance(self._version, payload, business_sid=self._solution['business_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.TrustedComms.ImpressionsRateContext {}>'.format(context)


class ImpressionsRateInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    class Intervals(object):
        MINUTE = "minute"
        HOUR = "hour"
        DAY = "day"
        WEEK = "week"
        MONTH = "month"

    def __init__(self, version, payload, business_sid):
        """
        Initialize the ImpressionsRateInstance

        :returns: twilio.rest.preview.trusted_comms.business.insights.impressions_rate.ImpressionsRateInstance
        :rtype: twilio.rest.preview.trusted_comms.business.insights.impressions_rate.ImpressionsRateInstance
        """
        super(ImpressionsRateInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'business_sid': payload.get('business_sid'),
            'end': deserialize.iso8601_datetime(payload.get('end')),
            'interval': payload.get('interval'),
            'reports': payload.get('reports'),
            'start': deserialize.iso8601_datetime(payload.get('start')),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'business_sid': business_sid, }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: ImpressionsRateContext for this ImpressionsRateInstance
        :rtype: twilio.rest.preview.trusted_comms.business.insights.impressions_rate.ImpressionsRateContext
        """
        if self._context is None:
            self._context = ImpressionsRateContext(self._version, business_sid=self._solution['business_sid'], )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: Account Sid.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def business_sid(self):
        """
        :returns: Business Sid.
        :rtype: unicode
        """
        return self._properties['business_sid']

    @property
    def end(self):
        """
        :returns: The end date that for this Impressions Rate.
        :rtype: datetime
        """
        return self._properties['end']

    @property
    def interval(self):
        """
        :returns: The Interval of this Impressions Rate.
        :rtype: ImpressionsRateInstance.Intervals
        """
        return self._properties['interval']

    @property
    def reports(self):
        """
        :returns: Values of Impressions Rate per interval.
        :rtype: dict
        """
        return self._properties['reports']

    @property
    def start(self):
        """
        :returns: The start date that for this Impressions Rate.
        :rtype: datetime
        """
        return self._properties['start']

    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self, brand_sid=values.unset, branded_channel_sid=values.unset,
              phone_number_sid=values.unset, country=values.unset,
              start=values.unset, end=values.unset, interval=values.unset):
        """
        Fetch the ImpressionsRateInstance

        :param unicode brand_sid: Brand Sid.
        :param unicode branded_channel_sid: Branded Channel Sid.
        :param unicode phone_number_sid: Phone Number Sid.
        :param unicode country: Country 2-letter ISO 3166 code.
        :param datetime start: The start date that for this Impressions Rate.
        :param datetime end: The end date that for this Impressions Rate.
        :param ImpressionsRateInstance.Intervals interval: The Interval of this Impressions Rate.

        :returns: The fetched ImpressionsRateInstance
        :rtype: twilio.rest.preview.trusted_comms.business.insights.impressions_rate.ImpressionsRateInstance
        """
        return self._proxy.fetch(
            brand_sid=brand_sid,
            branded_channel_sid=branded_channel_sid,
            phone_number_sid=phone_number_sid,
            country=country,
            start=start,
            end=end,
            interval=interval,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.TrustedComms.ImpressionsRateInstance {}>'.format(context)
