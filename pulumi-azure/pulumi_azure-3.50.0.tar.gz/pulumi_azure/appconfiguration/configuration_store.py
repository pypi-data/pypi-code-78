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

__all__ = ['ConfigurationStore']


class ConfigurationStore(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ConfigurationStoreIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an Azure App Configuration.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        rg = azure.core.ResourceGroup("rg", location="West Europe")
        appconf = azure.appconfiguration.ConfigurationStore("appconf",
            resource_group_name=rg.name,
            location=rg.location)
        ```

        ## Import

        App Configurations can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appconfiguration/configurationStore:ConfigurationStore appconf /subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/resourceGroup1/providers/Microsoft.AppConfiguration/configurationStores/appConf1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ConfigurationStoreIdentityArgs']] identity: An `identity` block as defined below.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the App Configuration. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the App Configuration. Changing this forces a new resource to be created.
        :param pulumi.Input[str] sku: The SKU name of the the App Configuration. Possible values are `free` and `standard`.
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

            __props__['identity'] = identity
            __props__['location'] = location
            __props__['name'] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['sku'] = sku
            __props__['tags'] = tags
            __props__['endpoint'] = None
            __props__['primary_read_keys'] = None
            __props__['primary_write_keys'] = None
            __props__['secondary_read_keys'] = None
            __props__['secondary_write_keys'] = None
        super(ConfigurationStore, __self__).__init__(
            'azure:appconfiguration/configurationStore:ConfigurationStore',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            endpoint: Optional[pulumi.Input[str]] = None,
            identity: Optional[pulumi.Input[pulumi.InputType['ConfigurationStoreIdentityArgs']]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            primary_read_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigurationStorePrimaryReadKeyArgs']]]]] = None,
            primary_write_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigurationStorePrimaryWriteKeyArgs']]]]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            secondary_read_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigurationStoreSecondaryReadKeyArgs']]]]] = None,
            secondary_write_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigurationStoreSecondaryWriteKeyArgs']]]]] = None,
            sku: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'ConfigurationStore':
        """
        Get an existing ConfigurationStore resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] endpoint: The URL of the App Configuration.
        :param pulumi.Input[pulumi.InputType['ConfigurationStoreIdentityArgs']] identity: An `identity` block as defined below.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the App Configuration. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigurationStorePrimaryReadKeyArgs']]]] primary_read_keys: A `primary_read_key` block as defined below containing the primary read access key.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigurationStorePrimaryWriteKeyArgs']]]] primary_write_keys: A `primary_write_key` block as defined below containing the primary write access key.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the App Configuration. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigurationStoreSecondaryReadKeyArgs']]]] secondary_read_keys: A `secondary_read_key` block as defined below containing the secondary read access key.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigurationStoreSecondaryWriteKeyArgs']]]] secondary_write_keys: A `secondary_write_key` block as defined below containing the secondary write access key.
        :param pulumi.Input[str] sku: The SKU name of the the App Configuration. Possible values are `free` and `standard`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["endpoint"] = endpoint
        __props__["identity"] = identity
        __props__["location"] = location
        __props__["name"] = name
        __props__["primary_read_keys"] = primary_read_keys
        __props__["primary_write_keys"] = primary_write_keys
        __props__["resource_group_name"] = resource_group_name
        __props__["secondary_read_keys"] = secondary_read_keys
        __props__["secondary_write_keys"] = secondary_write_keys
        __props__["sku"] = sku
        __props__["tags"] = tags
        return ConfigurationStore(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[str]:
        """
        The URL of the App Configuration.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ConfigurationStoreIdentity']]:
        """
        An `identity` block as defined below.
        """
        return pulumi.get(self, "identity")

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
        Specifies the name of the App Configuration. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="primaryReadKeys")
    def primary_read_keys(self) -> pulumi.Output[Sequence['outputs.ConfigurationStorePrimaryReadKey']]:
        """
        A `primary_read_key` block as defined below containing the primary read access key.
        """
        return pulumi.get(self, "primary_read_keys")

    @property
    @pulumi.getter(name="primaryWriteKeys")
    def primary_write_keys(self) -> pulumi.Output[Sequence['outputs.ConfigurationStorePrimaryWriteKey']]:
        """
        A `primary_write_key` block as defined below containing the primary write access key.
        """
        return pulumi.get(self, "primary_write_keys")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to create the App Configuration. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="secondaryReadKeys")
    def secondary_read_keys(self) -> pulumi.Output[Sequence['outputs.ConfigurationStoreSecondaryReadKey']]:
        """
        A `secondary_read_key` block as defined below containing the secondary read access key.
        """
        return pulumi.get(self, "secondary_read_keys")

    @property
    @pulumi.getter(name="secondaryWriteKeys")
    def secondary_write_keys(self) -> pulumi.Output[Sequence['outputs.ConfigurationStoreSecondaryWriteKey']]:
        """
        A `secondary_write_key` block as defined below containing the secondary write access key.
        """
        return pulumi.get(self, "secondary_write_keys")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[str]]:
        """
        The SKU name of the the App Configuration. Possible values are `free` and `standard`.
        """
        return pulumi.get(self, "sku")

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

