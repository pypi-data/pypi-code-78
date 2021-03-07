# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'AutomationActionArgs',
    'AutomationSourceArgs',
    'AutomationSourceRuleSetArgs',
    'AutomationSourceRuleSetRuleArgs',
]

@pulumi.input_type
class AutomationActionArgs:
    def __init__(__self__, *,
                 resource_id: pulumi.Input[str],
                 type: pulumi.Input[str],
                 connection_string: Optional[pulumi.Input[str]] = None,
                 trigger_url: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] resource_id: The resource id of the target Logic App, Event Hub namespace or Log Analytics workspace.
        :param pulumi.Input[str] type: Type of Azure resource to send data to. Must be set to one of: `LogicApp`, `EventHub` or `LogAnalytics`.
        :param pulumi.Input[str] connection_string: A connection string to send data to the target Event Hub namespace, this should include a key with send permissions.
        :param pulumi.Input[str] trigger_url: The callback URL to trigger the Logic App that will receive and process data sent by this automation. This can be found in the Azure Portal under "See trigger history"
        """
        pulumi.set(__self__, "resource_id", resource_id)
        pulumi.set(__self__, "type", type)
        if connection_string is not None:
            pulumi.set(__self__, "connection_string", connection_string)
        if trigger_url is not None:
            pulumi.set(__self__, "trigger_url", trigger_url)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[str]:
        """
        The resource id of the target Logic App, Event Hub namespace or Log Analytics workspace.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Type of Azure resource to send data to. Must be set to one of: `LogicApp`, `EventHub` or `LogAnalytics`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> Optional[pulumi.Input[str]]:
        """
        A connection string to send data to the target Event Hub namespace, this should include a key with send permissions.
        """
        return pulumi.get(self, "connection_string")

    @connection_string.setter
    def connection_string(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_string", value)

    @property
    @pulumi.getter(name="triggerUrl")
    def trigger_url(self) -> Optional[pulumi.Input[str]]:
        """
        The callback URL to trigger the Logic App that will receive and process data sent by this automation. This can be found in the Azure Portal under "See trigger history"
        """
        return pulumi.get(self, "trigger_url")

    @trigger_url.setter
    def trigger_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "trigger_url", value)


@pulumi.input_type
class AutomationSourceArgs:
    def __init__(__self__, *,
                 event_source: pulumi.Input[str],
                 rule_sets: Optional[pulumi.Input[Sequence[pulumi.Input['AutomationSourceRuleSetArgs']]]] = None):
        """
        :param pulumi.Input[str] event_source: Type of data that will trigger this automation. Must be one of `Alerts`, `Assessments`, `SecureScoreControls`, `SecureScores` or `SubAssessments`. Note. assessments are also referred to as recommendations
        :param pulumi.Input[Sequence[pulumi.Input['AutomationSourceRuleSetArgs']]] rule_sets: A set of rules which evaluate upon event and data interception. This is defined in one or more `rule_set` blocks as defined below.
        """
        pulumi.set(__self__, "event_source", event_source)
        if rule_sets is not None:
            pulumi.set(__self__, "rule_sets", rule_sets)

    @property
    @pulumi.getter(name="eventSource")
    def event_source(self) -> pulumi.Input[str]:
        """
        Type of data that will trigger this automation. Must be one of `Alerts`, `Assessments`, `SecureScoreControls`, `SecureScores` or `SubAssessments`. Note. assessments are also referred to as recommendations
        """
        return pulumi.get(self, "event_source")

    @event_source.setter
    def event_source(self, value: pulumi.Input[str]):
        pulumi.set(self, "event_source", value)

    @property
    @pulumi.getter(name="ruleSets")
    def rule_sets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AutomationSourceRuleSetArgs']]]]:
        """
        A set of rules which evaluate upon event and data interception. This is defined in one or more `rule_set` blocks as defined below.
        """
        return pulumi.get(self, "rule_sets")

    @rule_sets.setter
    def rule_sets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AutomationSourceRuleSetArgs']]]]):
        pulumi.set(self, "rule_sets", value)


@pulumi.input_type
class AutomationSourceRuleSetArgs:
    def __init__(__self__, *,
                 rules: pulumi.Input[Sequence[pulumi.Input['AutomationSourceRuleSetRuleArgs']]]):
        """
        :param pulumi.Input[Sequence[pulumi.Input['AutomationSourceRuleSetRuleArgs']]] rules: One or more `rule` blocks as defined below.
        """
        pulumi.set(__self__, "rules", rules)

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Input[Sequence[pulumi.Input['AutomationSourceRuleSetRuleArgs']]]:
        """
        One or more `rule` blocks as defined below.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: pulumi.Input[Sequence[pulumi.Input['AutomationSourceRuleSetRuleArgs']]]):
        pulumi.set(self, "rules", value)


@pulumi.input_type
class AutomationSourceRuleSetRuleArgs:
    def __init__(__self__, *,
                 expected_value: pulumi.Input[str],
                 operator: pulumi.Input[str],
                 property_path: pulumi.Input[str],
                 property_type: pulumi.Input[str]):
        """
        :param pulumi.Input[str] expected_value: A value that will be compared with the value in `property_path`.
        :param pulumi.Input[str] operator: The comparison operator to use, must be one of: `Contains`, `EndsWith`, `Equals`, `GreaterThan`, `GreaterThanOrEqualTo`, `LesserThan`, `LesserThanOrEqualTo`, `NotEquals`, `StartsWith`
        :param pulumi.Input[str] property_path: The JPath of the entity model property that should be checked.
        :param pulumi.Input[str] property_type: The data type of the compared operands, must be one of: `Integer`, `String`, `Boolean` or `Number`.
        """
        pulumi.set(__self__, "expected_value", expected_value)
        pulumi.set(__self__, "operator", operator)
        pulumi.set(__self__, "property_path", property_path)
        pulumi.set(__self__, "property_type", property_type)

    @property
    @pulumi.getter(name="expectedValue")
    def expected_value(self) -> pulumi.Input[str]:
        """
        A value that will be compared with the value in `property_path`.
        """
        return pulumi.get(self, "expected_value")

    @expected_value.setter
    def expected_value(self, value: pulumi.Input[str]):
        pulumi.set(self, "expected_value", value)

    @property
    @pulumi.getter
    def operator(self) -> pulumi.Input[str]:
        """
        The comparison operator to use, must be one of: `Contains`, `EndsWith`, `Equals`, `GreaterThan`, `GreaterThanOrEqualTo`, `LesserThan`, `LesserThanOrEqualTo`, `NotEquals`, `StartsWith`
        """
        return pulumi.get(self, "operator")

    @operator.setter
    def operator(self, value: pulumi.Input[str]):
        pulumi.set(self, "operator", value)

    @property
    @pulumi.getter(name="propertyPath")
    def property_path(self) -> pulumi.Input[str]:
        """
        The JPath of the entity model property that should be checked.
        """
        return pulumi.get(self, "property_path")

    @property_path.setter
    def property_path(self, value: pulumi.Input[str]):
        pulumi.set(self, "property_path", value)

    @property
    @pulumi.getter(name="propertyType")
    def property_type(self) -> pulumi.Input[str]:
        """
        The data type of the compared operands, must be one of: `Integer`, `String`, `Boolean` or `Number`.
        """
        return pulumi.get(self, "property_type")

    @property_type.setter
    def property_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "property_type", value)


