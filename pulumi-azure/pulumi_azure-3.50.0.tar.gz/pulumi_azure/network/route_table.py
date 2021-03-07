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

__all__ = ['RouteTable']


class RouteTable(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disable_bgp_route_propagation: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 routes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RouteTableRouteArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Route Table

        > **NOTE on Route Tables and Routes:** There is both a standalone `route` resource, and allows for Routes to be defined in-line within the `route_table` resource.
        At this time you cannot use a Route Table with in-line Routes in conjunction with any Route resources. Doing so will cause a conflict of Route configurations and will overwrite Routes.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_route_table = azure.network.RouteTable("exampleRouteTable",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            disable_bgp_route_propagation=False,
            routes=[azure.network.RouteTableRouteArgs(
                name="route1",
                address_prefix="10.1.0.0/16",
                next_hop_type="vnetlocal",
            )],
            tags={
                "environment": "Production",
            })
        ```

        ## Import

        Route Tables can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:network/routeTable:RouteTable example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Network/routeTables/mytable1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] disable_bgp_route_propagation: Boolean flag which controls propagation of routes learned by BGP on that route table. True means disable.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the route.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the route table. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RouteTableRouteArgs']]]] routes: A list of objects representing routes. Each object accepts the arguments documented below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
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

            __props__['disable_bgp_route_propagation'] = disable_bgp_route_propagation
            __props__['location'] = location
            __props__['name'] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['routes'] = routes
            __props__['tags'] = tags
            __props__['subnets'] = None
        super(RouteTable, __self__).__init__(
            'azure:network/routeTable:RouteTable',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            disable_bgp_route_propagation: Optional[pulumi.Input[bool]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            routes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RouteTableRouteArgs']]]]] = None,
            subnets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'RouteTable':
        """
        Get an existing RouteTable resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] disable_bgp_route_propagation: Boolean flag which controls propagation of routes learned by BGP on that route table. True means disable.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the route.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the route table. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RouteTableRouteArgs']]]] routes: A list of objects representing routes. Each object accepts the arguments documented below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnets: The collection of Subnets associated with this route table.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["disable_bgp_route_propagation"] = disable_bgp_route_propagation
        __props__["location"] = location
        __props__["name"] = name
        __props__["resource_group_name"] = resource_group_name
        __props__["routes"] = routes
        __props__["subnets"] = subnets
        __props__["tags"] = tags
        return RouteTable(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="disableBgpRoutePropagation")
    def disable_bgp_route_propagation(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean flag which controls propagation of routes learned by BGP on that route table. True means disable.
        """
        return pulumi.get(self, "disable_bgp_route_propagation")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the route.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to create the route table. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def routes(self) -> pulumi.Output[Sequence['outputs.RouteTableRoute']]:
        """
        A list of objects representing routes. Each object accepts the arguments documented below.
        """
        return pulumi.get(self, "routes")

    @property
    @pulumi.getter
    def subnets(self) -> pulumi.Output[Sequence[str]]:
        """
        The collection of Subnets associated with this route table.
        """
        return pulumi.get(self, "subnets")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

