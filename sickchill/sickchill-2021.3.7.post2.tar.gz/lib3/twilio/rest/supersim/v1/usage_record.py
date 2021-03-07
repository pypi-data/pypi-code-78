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
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class UsageRecordList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the UsageRecordList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.supersim.v1.usage_record.UsageRecordList
        :rtype: twilio.rest.supersim.v1.usage_record.UsageRecordList
        """
        super(UsageRecordList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/UsageRecords'.format(**self._solution)

    def stream(self, sim=values.unset, fleet=values.unset, network=values.unset,
               iso_country=values.unset, group=values.unset,
               granularity=values.unset, start_time=values.unset,
               end_time=values.unset, limit=None, page_size=None):
        """
        Streams UsageRecordInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode sim: SID or unique name of a Sim resource. Only show UsageRecords representing usage incurred by this Super SIM.
        :param unicode fleet: SID or unique name of a Fleet resource. Only show UsageRecords representing usage for Super SIMs belonging to this Fleet resource at the time the usage occurred.
        :param unicode network: SID of a Network resource. Only show UsageRecords representing usage on this network.
        :param unicode iso_country: Alpha-2 ISO Country Code. Only show UsageRecords representing usage in this country.
        :param UsageRecordInstance.Group group: Dimension over which to aggregate usage records.
        :param UsageRecordInstance.Granularity granularity: Time-based grouping that UsageRecords should be aggregated by. Can be: `hour`, `day`, or `all`. Default is `all`.
        :param datetime start_time: Only include usage that occurred at or after this time.
        :param datetime end_time: Only include usage that occurred before this time.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.usage_record.UsageRecordInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            sim=sim,
            fleet=fleet,
            network=network,
            iso_country=iso_country,
            group=group,
            granularity=granularity,
            start_time=start_time,
            end_time=end_time,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'])

    def list(self, sim=values.unset, fleet=values.unset, network=values.unset,
             iso_country=values.unset, group=values.unset, granularity=values.unset,
             start_time=values.unset, end_time=values.unset, limit=None,
             page_size=None):
        """
        Lists UsageRecordInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode sim: SID or unique name of a Sim resource. Only show UsageRecords representing usage incurred by this Super SIM.
        :param unicode fleet: SID or unique name of a Fleet resource. Only show UsageRecords representing usage for Super SIMs belonging to this Fleet resource at the time the usage occurred.
        :param unicode network: SID of a Network resource. Only show UsageRecords representing usage on this network.
        :param unicode iso_country: Alpha-2 ISO Country Code. Only show UsageRecords representing usage in this country.
        :param UsageRecordInstance.Group group: Dimension over which to aggregate usage records.
        :param UsageRecordInstance.Granularity granularity: Time-based grouping that UsageRecords should be aggregated by. Can be: `hour`, `day`, or `all`. Default is `all`.
        :param datetime start_time: Only include usage that occurred at or after this time.
        :param datetime end_time: Only include usage that occurred before this time.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.usage_record.UsageRecordInstance]
        """
        return list(self.stream(
            sim=sim,
            fleet=fleet,
            network=network,
            iso_country=iso_country,
            group=group,
            granularity=granularity,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, sim=values.unset, fleet=values.unset, network=values.unset,
             iso_country=values.unset, group=values.unset, granularity=values.unset,
             start_time=values.unset, end_time=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of UsageRecordInstance records from the API.
        Request is executed immediately

        :param unicode sim: SID or unique name of a Sim resource. Only show UsageRecords representing usage incurred by this Super SIM.
        :param unicode fleet: SID or unique name of a Fleet resource. Only show UsageRecords representing usage for Super SIMs belonging to this Fleet resource at the time the usage occurred.
        :param unicode network: SID of a Network resource. Only show UsageRecords representing usage on this network.
        :param unicode iso_country: Alpha-2 ISO Country Code. Only show UsageRecords representing usage in this country.
        :param UsageRecordInstance.Group group: Dimension over which to aggregate usage records.
        :param UsageRecordInstance.Granularity granularity: Time-based grouping that UsageRecords should be aggregated by. Can be: `hour`, `day`, or `all`. Default is `all`.
        :param datetime start_time: Only include usage that occurred at or after this time.
        :param datetime end_time: Only include usage that occurred before this time.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UsageRecordInstance
        :rtype: twilio.rest.supersim.v1.usage_record.UsageRecordPage
        """
        data = values.of({
            'Sim': sim,
            'Fleet': fleet,
            'Network': network,
            'IsoCountry': iso_country,
            'Group': group,
            'Granularity': granularity,
            'StartTime': serialize.iso8601_datetime(start_time),
            'EndTime': serialize.iso8601_datetime(end_time),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return UsageRecordPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of UsageRecordInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UsageRecordInstance
        :rtype: twilio.rest.supersim.v1.usage_record.UsageRecordPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return UsageRecordPage(self._version, response, self._solution)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.UsageRecordList>'


class UsageRecordPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the UsageRecordPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.supersim.v1.usage_record.UsageRecordPage
        :rtype: twilio.rest.supersim.v1.usage_record.UsageRecordPage
        """
        super(UsageRecordPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of UsageRecordInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.supersim.v1.usage_record.UsageRecordInstance
        :rtype: twilio.rest.supersim.v1.usage_record.UsageRecordInstance
        """
        return UsageRecordInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.UsageRecordPage>'


class UsageRecordInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    class Granularity(object):
        HOUR = "hour"
        DAY = "day"
        ALL = "all"

    class Group(object):
        SIM = "sim"
        FLEET = "fleet"
        NETWORK = "network"
        ISOCOUNTRY = "isoCountry"

    class SortBy(object):
        TIME = "time"

    def __init__(self, version, payload):
        """
        Initialize the UsageRecordInstance

        :returns: twilio.rest.supersim.v1.usage_record.UsageRecordInstance
        :rtype: twilio.rest.supersim.v1.usage_record.UsageRecordInstance
        """
        super(UsageRecordInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'sim_sid': payload.get('sim_sid'),
            'network_sid': payload.get('network_sid'),
            'fleet_sid': payload.get('fleet_sid'),
            'iso_country': payload.get('iso_country'),
            'period': payload.get('period'),
            'data_upload': deserialize.integer(payload.get('data_upload')),
            'data_download': deserialize.integer(payload.get('data_download')),
            'data_total': deserialize.integer(payload.get('data_total')),
        }

        # Context
        self._context = None
        self._solution = {}

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that incurred the usage.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def sim_sid(self):
        """
        :returns: SID of a Sim resource to which the UsageRecord belongs.
        :rtype: unicode
        """
        return self._properties['sim_sid']

    @property
    def network_sid(self):
        """
        :returns: SID of the Network resource on which the usage occurred.
        :rtype: unicode
        """
        return self._properties['network_sid']

    @property
    def fleet_sid(self):
        """
        :returns: SID of the Fleet resource on which the usage occurred.
        :rtype: unicode
        """
        return self._properties['fleet_sid']

    @property
    def iso_country(self):
        """
        :returns: Alpha-2 ISO Country Code of the country the usage occurred in.
        :rtype: unicode
        """
        return self._properties['iso_country']

    @property
    def period(self):
        """
        :returns: The time period for which the usage is reported.
        :rtype: dict
        """
        return self._properties['period']

    @property
    def data_upload(self):
        """
        :returns: Total data uploaded in bytes, aggregated by the query parameters.
        :rtype: unicode
        """
        return self._properties['data_upload']

    @property
    def data_download(self):
        """
        :returns: Total data downloaded in bytes, aggregated by the query parameters.
        :rtype: unicode
        """
        return self._properties['data_download']

    @property
    def data_total(self):
        """
        :returns: Total of data_upload and data_download.
        :rtype: unicode
        """
        return self._properties['data_total']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.UsageRecordInstance>'
