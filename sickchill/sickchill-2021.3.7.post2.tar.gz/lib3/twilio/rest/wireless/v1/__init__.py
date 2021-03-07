# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.version import Version
from twilio.rest.wireless.v1.command import CommandList
from twilio.rest.wireless.v1.rate_plan import RatePlanList
from twilio.rest.wireless.v1.sim import SimList
from twilio.rest.wireless.v1.usage_record import UsageRecordList


class V1(Version):

    def __init__(self, domain):
        """
        Initialize the V1 version of Wireless

        :returns: V1 version of Wireless
        :rtype: twilio.rest.wireless.v1.V1.V1
        """
        super(V1, self).__init__(domain)
        self.version = 'v1'
        self._usage_records = None
        self._commands = None
        self._rate_plans = None
        self._sims = None

    @property
    def usage_records(self):
        """
        :rtype: twilio.rest.wireless.v1.usage_record.UsageRecordList
        """
        if self._usage_records is None:
            self._usage_records = UsageRecordList(self)
        return self._usage_records

    @property
    def commands(self):
        """
        :rtype: twilio.rest.wireless.v1.command.CommandList
        """
        if self._commands is None:
            self._commands = CommandList(self)
        return self._commands

    @property
    def rate_plans(self):
        """
        :rtype: twilio.rest.wireless.v1.rate_plan.RatePlanList
        """
        if self._rate_plans is None:
            self._rate_plans = RatePlanList(self)
        return self._rate_plans

    @property
    def sims(self):
        """
        :rtype: twilio.rest.wireless.v1.sim.SimList
        """
        if self._sims is None:
            self._sims = SimList(self)
        return self._sims

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Wireless.V1>'
