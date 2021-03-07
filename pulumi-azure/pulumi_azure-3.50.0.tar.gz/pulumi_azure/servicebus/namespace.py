# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Namespace']


class Namespace(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capacity: Optional[pulumi.Input[int]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zone_redundant: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a ServiceBus Namespace.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_namespace = azure.servicebus.Namespace("exampleNamespace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="Standard",
            tags={
                "source": "example",
            })
        ```

        ## Import

        Service Bus Namespace can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:servicebus/namespace:Namespace example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/microsoft.servicebus/namespaces/sbns1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] capacity: Specifies the capacity. When `sku` is `Premium`, capacity can be `1`, `2`, `4`, `8` or `16`. When `sku` is `Basic` or `Standard`, capacity can be `0` only.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the ServiceBus Namespace resource . Changing this forces a
               new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to
               create the namespace.
        :param pulumi.Input[str] sku: Defines which tier to use. Options are basic, standard or premium. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[bool] zone_redundant: Whether or not this resource is zone redundant. `sku` needs to be `Premium`. Defaults to `false`.
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

            __props__['capacity'] = capacity
            __props__['location'] = location
            __props__['name'] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__['sku'] = sku
            __props__['tags'] = tags
            __props__['zone_redundant'] = zone_redundant
            __props__['default_primary_connection_string'] = None
            __props__['default_primary_key'] = None
            __props__['default_secondary_connection_string'] = None
            __props__['default_secondary_key'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure:eventhub/namespace:Namespace")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Namespace, __self__).__init__(
            'azure:servicebus/namespace:Namespace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            capacity: Optional[pulumi.Input[int]] = None,
            default_primary_connection_string: Optional[pulumi.Input[str]] = None,
            default_primary_key: Optional[pulumi.Input[str]] = None,
            default_secondary_connection_string: Optional[pulumi.Input[str]] = None,
            default_secondary_key: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            sku: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            zone_redundant: Optional[pulumi.Input[bool]] = None) -> 'Namespace':
        """
        Get an existing Namespace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] capacity: Specifies the capacity. When `sku` is `Premium`, capacity can be `1`, `2`, `4`, `8` or `16`. When `sku` is `Basic` or `Standard`, capacity can be `0` only.
        :param pulumi.Input[str] default_primary_connection_string: The primary connection string for the authorization
               rule `RootManageSharedAccessKey`.
        :param pulumi.Input[str] default_primary_key: The primary access key for the authorization rule `RootManageSharedAccessKey`.
        :param pulumi.Input[str] default_secondary_connection_string: The secondary connection string for the
               authorization rule `RootManageSharedAccessKey`.
        :param pulumi.Input[str] default_secondary_key: The secondary access key for the authorization rule `RootManageSharedAccessKey`.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the ServiceBus Namespace resource . Changing this forces a
               new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to
               create the namespace.
        :param pulumi.Input[str] sku: Defines which tier to use. Options are basic, standard or premium. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[bool] zone_redundant: Whether or not this resource is zone redundant. `sku` needs to be `Premium`. Defaults to `false`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["capacity"] = capacity
        __props__["default_primary_connection_string"] = default_primary_connection_string
        __props__["default_primary_key"] = default_primary_key
        __props__["default_secondary_connection_string"] = default_secondary_connection_string
        __props__["default_secondary_key"] = default_secondary_key
        __props__["location"] = location
        __props__["name"] = name
        __props__["resource_group_name"] = resource_group_name
        __props__["sku"] = sku
        __props__["tags"] = tags
        __props__["zone_redundant"] = zone_redundant
        return Namespace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def capacity(self) -> pulumi.Output[Optional[int]]:
        """
        Specifies the capacity. When `sku` is `Premium`, capacity can be `1`, `2`, `4`, `8` or `16`. When `sku` is `Basic` or `Standard`, capacity can be `0` only.
        """
        return pulumi.get(self, "capacity")

    @property
    @pulumi.getter(name="defaultPrimaryConnectionString")
    def default_primary_connection_string(self) -> pulumi.Output[str]:
        """
        The primary connection string for the authorization
        rule `RootManageSharedAccessKey`.
        """
        return pulumi.get(self, "default_primary_connection_string")

    @property
    @pulumi.getter(name="defaultPrimaryKey")
    def default_primary_key(self) -> pulumi.Output[str]:
        """
        The primary access key for the authorization rule `RootManageSharedAccessKey`.
        """
        return pulumi.get(self, "default_primary_key")

    @property
    @pulumi.getter(name="defaultSecondaryConnectionString")
    def default_secondary_connection_string(self) -> pulumi.Output[str]:
        """
        The secondary connection string for the
        authorization rule `RootManageSharedAccessKey`.
        """
        return pulumi.get(self, "default_secondary_connection_string")

    @property
    @pulumi.getter(name="defaultSecondaryKey")
    def default_secondary_key(self) -> pulumi.Output[str]:
        """
        The secondary access key for the authorization rule `RootManageSharedAccessKey`.
        """
        return pulumi.get(self, "default_secondary_key")

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
        Specifies the name of the ServiceBus Namespace resource . Changing this forces a
        new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to
        create the namespace.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[str]:
        """
        Defines which tier to use. Options are basic, standard or premium. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether or not this resource is zone redundant. `sku` needs to be `Premium`. Defaults to `false`.
        """
        return pulumi.get(self, "zone_redundant")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

