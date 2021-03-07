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

__all__ = ['FirewallPolicyRuleCollectionGroup']


class FirewallPolicyRuleCollectionGroup(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_rule_collections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyRuleCollectionGroupApplicationRuleCollectionArgs']]]]] = None,
                 firewall_policy_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nat_rule_collections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyRuleCollectionGroupNatRuleCollectionArgs']]]]] = None,
                 network_rule_collections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyRuleCollectionGroupNetworkRuleCollectionArgs']]]]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Firewall Policy Rule Collection Group.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_firewall_policy = azure.network.FirewallPolicy("exampleFirewallPolicy",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location)
        example_firewall_policy_rule_collection_group = azure.network.FirewallPolicyRuleCollectionGroup("exampleFirewallPolicyRuleCollectionGroup",
            firewall_policy_id=example_firewall_policy.id,
            priority=500,
            application_rule_collections=[azure.network.FirewallPolicyRuleCollectionGroupApplicationRuleCollectionArgs(
                name="app_rule_collection1",
                priority=500,
                action="Deny",
                rules=[azure.network.FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleArgs(
                    name="app_rule_collection1_rule1",
                    protocols=[
                        azure.network.FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocolArgs(
                            type="Http",
                            port=80,
                        ),
                        azure.network.FirewallPolicyRuleCollectionGroupApplicationRuleCollectionRuleProtocolArgs(
                            type="Https",
                            port=443,
                        ),
                    ],
                    source_addresses=["10.0.0.1"],
                    destination_fqdns=[".microsoft.com"],
                )],
            )],
            network_rule_collections=[azure.network.FirewallPolicyRuleCollectionGroupNetworkRuleCollectionArgs(
                name="network_rule_collection1",
                priority=400,
                action="Deny",
                rules=[azure.network.FirewallPolicyRuleCollectionGroupNetworkRuleCollectionRuleArgs(
                    name="network_rule_collection1_rule1",
                    protocols=[
                        "TCP",
                        "UDP",
                    ],
                    source_addresses=["10.0.0.1"],
                    destination_addresses=[
                        "192.168.1.1",
                        "192.168.1.2",
                    ],
                    destination_ports=[
                        "80",
                        "1000-2000",
                    ],
                )],
            )],
            nat_rule_collections=[azure.network.FirewallPolicyRuleCollectionGroupNatRuleCollectionArgs(
                name="nat_rule_collection1",
                priority=300,
                action="Dnat",
                rules=[azure.network.FirewallPolicyRuleCollectionGroupNatRuleCollectionRuleArgs(
                    name="nat_rule_collection1_rule1",
                    protocols=[
                        "TCP",
                        "UDP",
                    ],
                    source_addresses=[
                        "10.0.0.1",
                        "10.0.0.2",
                    ],
                    destination_address="192.168.1.1",
                    destination_ports=[
                        "80",
                        "1000-2000",
                    ],
                    translated_address="192.168.0.1",
                    translated_port=8080,
                )],
            )])
        ```

        ## Import

        Firewall Policy Rule Collection Groups can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:network/firewallPolicyRuleCollectionGroup:FirewallPolicyRuleCollectionGroup example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Network/firewallPolicies/policy1/ruleCollectionGroups/gruop1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyRuleCollectionGroupApplicationRuleCollectionArgs']]]] application_rule_collections: One or more `application_rule_collection` blocks as defined below.
        :param pulumi.Input[str] firewall_policy_id: The ID of the Firewall Policy where the Firewall Policy Rule Collection Group should exist. Changing this forces a new Firewall Policy Rule Collection Group to be created.
        :param pulumi.Input[str] name: The name which should be used for this Firewall Policy Rule Collection Group. Changing this forces a new Firewall Policy Rule Collection Group to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyRuleCollectionGroupNatRuleCollectionArgs']]]] nat_rule_collections: One or more `nat_rule_collection` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyRuleCollectionGroupNetworkRuleCollectionArgs']]]] network_rule_collections: One or more `network_rule_collection` blocks as defined below.
        :param pulumi.Input[int] priority: The priority of the Firewall Policy Rule Collection Group. The range is 100-65000.
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

            __props__['application_rule_collections'] = application_rule_collections
            if firewall_policy_id is None and not opts.urn:
                raise TypeError("Missing required property 'firewall_policy_id'")
            __props__['firewall_policy_id'] = firewall_policy_id
            __props__['name'] = name
            __props__['nat_rule_collections'] = nat_rule_collections
            __props__['network_rule_collections'] = network_rule_collections
            if priority is None and not opts.urn:
                raise TypeError("Missing required property 'priority'")
            __props__['priority'] = priority
        super(FirewallPolicyRuleCollectionGroup, __self__).__init__(
            'azure:network/firewallPolicyRuleCollectionGroup:FirewallPolicyRuleCollectionGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            application_rule_collections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyRuleCollectionGroupApplicationRuleCollectionArgs']]]]] = None,
            firewall_policy_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            nat_rule_collections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyRuleCollectionGroupNatRuleCollectionArgs']]]]] = None,
            network_rule_collections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyRuleCollectionGroupNetworkRuleCollectionArgs']]]]] = None,
            priority: Optional[pulumi.Input[int]] = None) -> 'FirewallPolicyRuleCollectionGroup':
        """
        Get an existing FirewallPolicyRuleCollectionGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyRuleCollectionGroupApplicationRuleCollectionArgs']]]] application_rule_collections: One or more `application_rule_collection` blocks as defined below.
        :param pulumi.Input[str] firewall_policy_id: The ID of the Firewall Policy where the Firewall Policy Rule Collection Group should exist. Changing this forces a new Firewall Policy Rule Collection Group to be created.
        :param pulumi.Input[str] name: The name which should be used for this Firewall Policy Rule Collection Group. Changing this forces a new Firewall Policy Rule Collection Group to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyRuleCollectionGroupNatRuleCollectionArgs']]]] nat_rule_collections: One or more `nat_rule_collection` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyRuleCollectionGroupNetworkRuleCollectionArgs']]]] network_rule_collections: One or more `network_rule_collection` blocks as defined below.
        :param pulumi.Input[int] priority: The priority of the Firewall Policy Rule Collection Group. The range is 100-65000.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["application_rule_collections"] = application_rule_collections
        __props__["firewall_policy_id"] = firewall_policy_id
        __props__["name"] = name
        __props__["nat_rule_collections"] = nat_rule_collections
        __props__["network_rule_collections"] = network_rule_collections
        __props__["priority"] = priority
        return FirewallPolicyRuleCollectionGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationRuleCollections")
    def application_rule_collections(self) -> pulumi.Output[Optional[Sequence['outputs.FirewallPolicyRuleCollectionGroupApplicationRuleCollection']]]:
        """
        One or more `application_rule_collection` blocks as defined below.
        """
        return pulumi.get(self, "application_rule_collections")

    @property
    @pulumi.getter(name="firewallPolicyId")
    def firewall_policy_id(self) -> pulumi.Output[str]:
        """
        The ID of the Firewall Policy where the Firewall Policy Rule Collection Group should exist. Changing this forces a new Firewall Policy Rule Collection Group to be created.
        """
        return pulumi.get(self, "firewall_policy_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Firewall Policy Rule Collection Group. Changing this forces a new Firewall Policy Rule Collection Group to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="natRuleCollections")
    def nat_rule_collections(self) -> pulumi.Output[Optional[Sequence['outputs.FirewallPolicyRuleCollectionGroupNatRuleCollection']]]:
        """
        One or more `nat_rule_collection` blocks as defined below.
        """
        return pulumi.get(self, "nat_rule_collections")

    @property
    @pulumi.getter(name="networkRuleCollections")
    def network_rule_collections(self) -> pulumi.Output[Optional[Sequence['outputs.FirewallPolicyRuleCollectionGroupNetworkRuleCollection']]]:
        """
        One or more `network_rule_collection` blocks as defined below.
        """
        return pulumi.get(self, "network_rule_collections")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[int]:
        """
        The priority of the Firewall Policy Rule Collection Group. The range is 100-65000.
        """
        return pulumi.get(self, "priority")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

