# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['FirewallPolicy']


class FirewallPolicy(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base_policy_id: Optional[pulumi.Input[str]] = None,
                 dns: Optional[pulumi.Input[pulumi.InputType['FirewallPolicyDnsArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 threat_intelligence_allowlist: Optional[pulumi.Input[pulumi.InputType['FirewallPolicyThreatIntelligenceAllowlistArgs']]] = None,
                 threat_intelligence_mode: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Firewall Policy.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.network.FirewallPolicy("example",
            location="West Europe",
            resource_group_name="example")
        ```

        ## Import

        networks can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:network/firewallPolicy:FirewallPolicy example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Network/firewallPolicies/policy1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] base_policy_id: The ID of the base Firewall Policy.
        :param pulumi.Input[pulumi.InputType['FirewallPolicyDnsArgs']] dns: A `dns` block as defined below.
        :param pulumi.Input[str] location: The Azure Region where the Firewall Policy should exist. Changing this forces a new Firewall Policy to be created.
        :param pulumi.Input[str] name: The name which should be used for this Firewall Policy. Changing this forces a new Firewall Policy to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Firewall Policy should exist. Changing this forces a new Firewall Policy to be created.
        :param pulumi.Input[str] sku: The SKU Tier of the Firewall Policy. Possible values are `Standard`, `Premium`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Firewall Policy.
        :param pulumi.Input[pulumi.InputType['FirewallPolicyThreatIntelligenceAllowlistArgs']] threat_intelligence_allowlist: A `threat_intelligence_allowlist` block as defined below.
        :param pulumi.Input[str] threat_intelligence_mode: The operation mode for Threat Intelligence. Possible values are `Alert`, `Deny` and `Off`. Defaults to `Alert`.
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

            __props__['base_policy_id'] = base_policy_id
            __props__['dns'] = dns
            __props__['location'] = location
            __props__['name'] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['sku'] = sku
            __props__['tags'] = tags
            __props__['threat_intelligence_allowlist'] = threat_intelligence_allowlist
            __props__['threat_intelligence_mode'] = threat_intelligence_mode
            __props__['child_policies'] = None
            __props__['firewalls'] = None
            __props__['rule_collection_groups'] = None
        super(FirewallPolicy, __self__).__init__(
            'azure:network/firewallPolicy:FirewallPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            base_policy_id: Optional[pulumi.Input[str]] = None,
            child_policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            dns: Optional[pulumi.Input[pulumi.InputType['FirewallPolicyDnsArgs']]] = None,
            firewalls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            rule_collection_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            sku: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            threat_intelligence_allowlist: Optional[pulumi.Input[pulumi.InputType['FirewallPolicyThreatIntelligenceAllowlistArgs']]] = None,
            threat_intelligence_mode: Optional[pulumi.Input[str]] = None) -> 'FirewallPolicy':
        """
        Get an existing FirewallPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] base_policy_id: The ID of the base Firewall Policy.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] child_policies: A list of reference to child Firewall Policies of this Firewall Policy.
        :param pulumi.Input[pulumi.InputType['FirewallPolicyDnsArgs']] dns: A `dns` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] firewalls: A list of references to Azure Firewalls that this Firewall Policy is associated with.
        :param pulumi.Input[str] location: The Azure Region where the Firewall Policy should exist. Changing this forces a new Firewall Policy to be created.
        :param pulumi.Input[str] name: The name which should be used for this Firewall Policy. Changing this forces a new Firewall Policy to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Firewall Policy should exist. Changing this forces a new Firewall Policy to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] rule_collection_groups: A list of references to Firewall Policy Rule Collection Groups that belongs to this Firewall Policy.
        :param pulumi.Input[str] sku: The SKU Tier of the Firewall Policy. Possible values are `Standard`, `Premium`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Firewall Policy.
        :param pulumi.Input[pulumi.InputType['FirewallPolicyThreatIntelligenceAllowlistArgs']] threat_intelligence_allowlist: A `threat_intelligence_allowlist` block as defined below.
        :param pulumi.Input[str] threat_intelligence_mode: The operation mode for Threat Intelligence. Possible values are `Alert`, `Deny` and `Off`. Defaults to `Alert`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["base_policy_id"] = base_policy_id
        __props__["child_policies"] = child_policies
        __props__["dns"] = dns
        __props__["firewalls"] = firewalls
        __props__["location"] = location
        __props__["name"] = name
        __props__["resource_group_name"] = resource_group_name
        __props__["rule_collection_groups"] = rule_collection_groups
        __props__["sku"] = sku
        __props__["tags"] = tags
        __props__["threat_intelligence_allowlist"] = threat_intelligence_allowlist
        __props__["threat_intelligence_mode"] = threat_intelligence_mode
        return FirewallPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="basePolicyId")
    def base_policy_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the base Firewall Policy.
        """
        return pulumi.get(self, "base_policy_id")

    @property
    @pulumi.getter(name="childPolicies")
    def child_policies(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of reference to child Firewall Policies of this Firewall Policy.
        """
        return pulumi.get(self, "child_policies")

    @property
    @pulumi.getter
    def dns(self) -> pulumi.Output[Optional['outputs.FirewallPolicyDns']]:
        """
        A `dns` block as defined below.
        """
        return pulumi.get(self, "dns")

    @property
    @pulumi.getter
    def firewalls(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of references to Azure Firewalls that this Firewall Policy is associated with.
        """
        return pulumi.get(self, "firewalls")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The Azure Region where the Firewall Policy should exist. Changing this forces a new Firewall Policy to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Firewall Policy. Changing this forces a new Firewall Policy to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group where the Firewall Policy should exist. Changing this forces a new Firewall Policy to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="ruleCollectionGroups")
    def rule_collection_groups(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of references to Firewall Policy Rule Collection Groups that belongs to this Firewall Policy.
        """
        return pulumi.get(self, "rule_collection_groups")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[str]:
        """
        The SKU Tier of the Firewall Policy. Possible values are `Standard`, `Premium`.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags which should be assigned to the Firewall Policy.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="threatIntelligenceAllowlist")
    def threat_intelligence_allowlist(self) -> pulumi.Output[Optional['outputs.FirewallPolicyThreatIntelligenceAllowlist']]:
        """
        A `threat_intelligence_allowlist` block as defined below.
        """
        return pulumi.get(self, "threat_intelligence_allowlist")

    @property
    @pulumi.getter(name="threatIntelligenceMode")
    def threat_intelligence_mode(self) -> pulumi.Output[Optional[str]]:
        """
        The operation mode for Threat Intelligence. Possible values are `Alert`, `Deny` and `Off`. Defaults to `Alert`.
        """
        return pulumi.get(self, "threat_intelligence_mode")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

