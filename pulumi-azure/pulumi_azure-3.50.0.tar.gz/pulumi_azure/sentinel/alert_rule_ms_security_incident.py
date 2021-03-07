# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['AlertRuleMsSecurityIncident']


class AlertRuleMsSecurityIncident(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alert_rule_template_guid: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 display_name_exclude_filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 display_name_filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 log_analytics_workspace_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 product_filter: Optional[pulumi.Input[str]] = None,
                 severity_filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 text_whitelists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Sentinel MS Security Incident Alert Rule.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_analytics_workspace = azure.operationalinsights.AnalyticsWorkspace("exampleAnalyticsWorkspace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="pergb2018")
        example_alert_rule_ms_security_incident = azure.sentinel.AlertRuleMsSecurityIncident("exampleAlertRuleMsSecurityIncident",
            log_analytics_workspace_id=example_analytics_workspace.id,
            product_filter="Microsoft Cloud App Security",
            display_name="example rule",
            severity_filters=["High"])
        ```

        ## Import

        Sentinel MS Security Incident Alert Rules can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:sentinel/alertRuleMsSecurityIncident:AlertRuleMsSecurityIncident example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.OperationalInsights/workspaces/workspace1/providers/Microsoft.SecurityInsights/alertRules/rule1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alert_rule_template_guid: The GUID of the alert rule template which is used to create this Sentinel Scheduled Alert Rule. Changing this forces a new Sentinel MS Security Incident Alert Rule to be created.
        :param pulumi.Input[str] description: The description of this Sentinel MS Security Incident Alert Rule.
        :param pulumi.Input[str] display_name: The friendly name of this Sentinel MS Security Incident Alert Rule.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] display_name_exclude_filters: Only create incidents when the alert display name doesn't contain text from this list.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] display_name_filters: Only create incidents when the alert display name contain text from this list, leave empty to apply no filter.
        :param pulumi.Input[bool] enabled: Should this Sentinel MS Security Incident Alert Rule be enabled? Defaults to `true`.
        :param pulumi.Input[str] log_analytics_workspace_id: The ID of the Log Analytics Workspace this Sentinel MS Security Incident Alert Rule belongs to. Changing this forces a new Sentinel MS Security Incident Alert Rule to be created.
        :param pulumi.Input[str] name: The name which should be used for this Sentinel MS Security Incident Alert Rule. Changing this forces a new Sentinel MS Security Incident Alert Rule to be created.
        :param pulumi.Input[str] product_filter: The Microsoft Security Service from where the alert will be generated. Possible values are `Azure Active Directory Identity Protection`, `Azure Advanced Threat Protection`, `Azure Security Center`, `Azure Security Center for IoT`, `Microsoft Cloud App Security`, `Microsoft Defender Advanced Threat Protection` and `Office 365 Advanced Threat Protection`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] severity_filters: Only create incidents from alerts when alert severity level is contained in this list. Possible values are `High`, `Medium`, `Low` and `Informational`.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['alert_rule_template_guid'] = alert_rule_template_guid
            __props__['description'] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__['display_name'] = display_name
            __props__['display_name_exclude_filters'] = display_name_exclude_filters
            __props__['display_name_filters'] = display_name_filters
            __props__['enabled'] = enabled
            if log_analytics_workspace_id is None and not opts.urn:
                raise TypeError("Missing required property 'log_analytics_workspace_id'")
            __props__['log_analytics_workspace_id'] = log_analytics_workspace_id
            __props__['name'] = name
            if product_filter is None and not opts.urn:
                raise TypeError("Missing required property 'product_filter'")
            __props__['product_filter'] = product_filter
            if severity_filters is None and not opts.urn:
                raise TypeError("Missing required property 'severity_filters'")
            __props__['severity_filters'] = severity_filters
            if text_whitelists is not None and not opts.urn:
                warnings.warn("""this property has been renamed to display_name_filter to better match the SDK & API""", DeprecationWarning)
                pulumi.log.warn("text_whitelists is deprecated: this property has been renamed to display_name_filter to better match the SDK & API")
            __props__['text_whitelists'] = text_whitelists
        super(AlertRuleMsSecurityIncident, __self__).__init__(
            'azure:sentinel/alertRuleMsSecurityIncident:AlertRuleMsSecurityIncident',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            alert_rule_template_guid: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            display_name_exclude_filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            display_name_filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            log_analytics_workspace_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            product_filter: Optional[pulumi.Input[str]] = None,
            severity_filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            text_whitelists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'AlertRuleMsSecurityIncident':
        """
        Get an existing AlertRuleMsSecurityIncident resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alert_rule_template_guid: The GUID of the alert rule template which is used to create this Sentinel Scheduled Alert Rule. Changing this forces a new Sentinel MS Security Incident Alert Rule to be created.
        :param pulumi.Input[str] description: The description of this Sentinel MS Security Incident Alert Rule.
        :param pulumi.Input[str] display_name: The friendly name of this Sentinel MS Security Incident Alert Rule.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] display_name_exclude_filters: Only create incidents when the alert display name doesn't contain text from this list.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] display_name_filters: Only create incidents when the alert display name contain text from this list, leave empty to apply no filter.
        :param pulumi.Input[bool] enabled: Should this Sentinel MS Security Incident Alert Rule be enabled? Defaults to `true`.
        :param pulumi.Input[str] log_analytics_workspace_id: The ID of the Log Analytics Workspace this Sentinel MS Security Incident Alert Rule belongs to. Changing this forces a new Sentinel MS Security Incident Alert Rule to be created.
        :param pulumi.Input[str] name: The name which should be used for this Sentinel MS Security Incident Alert Rule. Changing this forces a new Sentinel MS Security Incident Alert Rule to be created.
        :param pulumi.Input[str] product_filter: The Microsoft Security Service from where the alert will be generated. Possible values are `Azure Active Directory Identity Protection`, `Azure Advanced Threat Protection`, `Azure Security Center`, `Azure Security Center for IoT`, `Microsoft Cloud App Security`, `Microsoft Defender Advanced Threat Protection` and `Office 365 Advanced Threat Protection`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] severity_filters: Only create incidents from alerts when alert severity level is contained in this list. Possible values are `High`, `Medium`, `Low` and `Informational`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["alert_rule_template_guid"] = alert_rule_template_guid
        __props__["description"] = description
        __props__["display_name"] = display_name
        __props__["display_name_exclude_filters"] = display_name_exclude_filters
        __props__["display_name_filters"] = display_name_filters
        __props__["enabled"] = enabled
        __props__["log_analytics_workspace_id"] = log_analytics_workspace_id
        __props__["name"] = name
        __props__["product_filter"] = product_filter
        __props__["severity_filters"] = severity_filters
        __props__["text_whitelists"] = text_whitelists
        return AlertRuleMsSecurityIncident(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="alertRuleTemplateGuid")
    def alert_rule_template_guid(self) -> pulumi.Output[Optional[str]]:
        """
        The GUID of the alert rule template which is used to create this Sentinel Scheduled Alert Rule. Changing this forces a new Sentinel MS Security Incident Alert Rule to be created.
        """
        return pulumi.get(self, "alert_rule_template_guid")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of this Sentinel MS Security Incident Alert Rule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The friendly name of this Sentinel MS Security Incident Alert Rule.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="displayNameExcludeFilters")
    def display_name_exclude_filters(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Only create incidents when the alert display name doesn't contain text from this list.
        """
        return pulumi.get(self, "display_name_exclude_filters")

    @property
    @pulumi.getter(name="displayNameFilters")
    def display_name_filters(self) -> pulumi.Output[Sequence[str]]:
        """
        Only create incidents when the alert display name contain text from this list, leave empty to apply no filter.
        """
        return pulumi.get(self, "display_name_filters")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Should this Sentinel MS Security Incident Alert Rule be enabled? Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="logAnalyticsWorkspaceId")
    def log_analytics_workspace_id(self) -> pulumi.Output[str]:
        """
        The ID of the Log Analytics Workspace this Sentinel MS Security Incident Alert Rule belongs to. Changing this forces a new Sentinel MS Security Incident Alert Rule to be created.
        """
        return pulumi.get(self, "log_analytics_workspace_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Sentinel MS Security Incident Alert Rule. Changing this forces a new Sentinel MS Security Incident Alert Rule to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="productFilter")
    def product_filter(self) -> pulumi.Output[str]:
        """
        The Microsoft Security Service from where the alert will be generated. Possible values are `Azure Active Directory Identity Protection`, `Azure Advanced Threat Protection`, `Azure Security Center`, `Azure Security Center for IoT`, `Microsoft Cloud App Security`, `Microsoft Defender Advanced Threat Protection` and `Office 365 Advanced Threat Protection`.
        """
        return pulumi.get(self, "product_filter")

    @property
    @pulumi.getter(name="severityFilters")
    def severity_filters(self) -> pulumi.Output[Sequence[str]]:
        """
        Only create incidents from alerts when alert severity level is contained in this list. Possible values are `High`, `Medium`, `Low` and `Informational`.
        """
        return pulumi.get(self, "severity_filters")

    @property
    @pulumi.getter(name="textWhitelists")
    def text_whitelists(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "text_whitelists")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

