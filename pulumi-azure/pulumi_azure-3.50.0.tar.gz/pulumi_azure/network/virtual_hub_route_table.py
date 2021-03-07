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

__all__ = ['VirtualHubRouteTable']


class VirtualHubRouteTable(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 routes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VirtualHubRouteTableRouteArgs']]]]] = None,
                 virtual_hub_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Virtual Hub Route Table.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            address_spaces=["10.5.0.0/16"],
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name)
        example_network_security_group = azure.network.NetworkSecurityGroup("exampleNetworkSecurityGroup",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name)
        example_subnet = azure.network.Subnet("exampleSubnet",
            resource_group_name=example_resource_group.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.5.1.0/24"])
        example_subnet_network_security_group_association = azure.network.SubnetNetworkSecurityGroupAssociation("exampleSubnetNetworkSecurityGroupAssociation",
            subnet_id=example_subnet.id,
            network_security_group_id=example_network_security_group.id)
        example_virtual_wan = azure.network.VirtualWan("exampleVirtualWan",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location)
        example_virtual_hub = azure.network.VirtualHub("exampleVirtualHub",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            virtual_wan_id=example_virtual_wan.id,
            address_prefix="10.0.2.0/24")
        example_virtual_hub_connection = azure.network.VirtualHubConnection("exampleVirtualHubConnection",
            virtual_hub_id=example_virtual_hub.id,
            remote_virtual_network_id=example_virtual_network.id)
        example_virtual_hub_route_table = azure.network.VirtualHubRouteTable("exampleVirtualHubRouteTable",
            virtual_hub_id=example_virtual_hub.id,
            labels=["label1"],
            routes=[azure.network.VirtualHubRouteTableRouteArgs(
                name="example-route",
                destinations_type="CIDR",
                destinations=["10.0.0.0/16"],
                next_hop_type="ResourceId",
                next_hop=example_virtual_hub_connection.id,
            )])
        ```

        ## Import

        Virtual Hub Route Tables can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:network/virtualHubRouteTable:VirtualHubRouteTable example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Network/virtualHubs/virtualHub1/hubRouteTables/routeTable1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] labels: List of labels associated with this route table.
        :param pulumi.Input[str] name: The name which should be used for Virtual Hub Route Table. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VirtualHubRouteTableRouteArgs']]]] routes: A `route` block as defined below.
        :param pulumi.Input[str] virtual_hub_id: The ID of the Virtual Hub within which this route table should be created. Changing this forces a new resource to be created.
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

            __props__['labels'] = labels
            __props__['name'] = name
            __props__['routes'] = routes
            if virtual_hub_id is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_hub_id'")
            __props__['virtual_hub_id'] = virtual_hub_id
        super(VirtualHubRouteTable, __self__).__init__(
            'azure:network/virtualHubRouteTable:VirtualHubRouteTable',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            labels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            routes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VirtualHubRouteTableRouteArgs']]]]] = None,
            virtual_hub_id: Optional[pulumi.Input[str]] = None) -> 'VirtualHubRouteTable':
        """
        Get an existing VirtualHubRouteTable resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] labels: List of labels associated with this route table.
        :param pulumi.Input[str] name: The name which should be used for Virtual Hub Route Table. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VirtualHubRouteTableRouteArgs']]]] routes: A `route` block as defined below.
        :param pulumi.Input[str] virtual_hub_id: The ID of the Virtual Hub within which this route table should be created. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["labels"] = labels
        __props__["name"] = name
        __props__["routes"] = routes
        __props__["virtual_hub_id"] = virtual_hub_id
        return VirtualHubRouteTable(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of labels associated with this route table.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for Virtual Hub Route Table. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def routes(self) -> pulumi.Output[Optional[Sequence['outputs.VirtualHubRouteTableRoute']]]:
        """
        A `route` block as defined below.
        """
        return pulumi.get(self, "routes")

    @property
    @pulumi.getter(name="virtualHubId")
    def virtual_hub_id(self) -> pulumi.Output[str]:
        """
        The ID of the Virtual Hub within which this route table should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "virtual_hub_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

