# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['RegistryWebook']

warnings.warn("""azure.containerservice.RegistryWebook has been deprecated in favor of azure.containerservice.RegistryWebhook""", DeprecationWarning)


class RegistryWebook(pulumi.CustomResource):
    warnings.warn("""azure.containerservice.RegistryWebook has been deprecated in favor of azure.containerservice.RegistryWebhook""", DeprecationWarning)

    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 custom_headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 registry_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 service_uri: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an Azure Container Registry Webhook.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        rg = azure.core.ResourceGroup("rg", location="West Europe")
        acr = azure.containerservice.Registry("acr",
            resource_group_name=rg.name,
            location=rg.location,
            sku="Standard",
            admin_enabled=False)
        webhook = azure.containerservice.RegistryWebhook("webhook",
            resource_group_name=rg.name,
            registry_name=acr.name,
            location=rg.location,
            service_uri="https://mywebhookreceiver.example/mytag",
            status="enabled",
            scope="mytag:*",
            actions=["push"],
            custom_headers={
                "Content-Type": "application/json",
            })
        ```

        ## Import

        Container Registry Webhooks can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:containerservice/registryWebook:RegistryWebook example /subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/mygroup1/providers/Microsoft.ContainerRegistry/registries/myregistry1/webhooks/mywebhook1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] actions: A list of actions that trigger the Webhook to post notifications. At least one action needs to be specified. Valid values are: `push`, `delete`, `quarantine`, `chart_push`, `chart_delete`
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] custom_headers: Custom headers that will be added to the webhook notifications request.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Container Registry Webhook. Changing this forces a new resource to be created.
        :param pulumi.Input[str] registry_name: The Name of Container registry this Webhook belongs to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Container Registry Webhook. Changing this forces a new resource to be created.
        :param pulumi.Input[str] scope: Specifies the scope of repositories that can trigger an event. For example, `foo:*` means events for all tags under repository `foo`. `foo:bar` means events for 'foo:bar' only. `foo` is equivalent to `foo:latest`. Empty means all events.
        :param pulumi.Input[str] service_uri: Specifies the service URI for the Webhook to post notifications.
        :param pulumi.Input[str] status: Specifies if this Webhook triggers notifications or not. Valid values: `enabled` and `disabled`. Default is `enabled`.
        """
        pulumi.log.warn("RegistryWebook is deprecated: azure.containerservice.RegistryWebook has been deprecated in favor of azure.containerservice.RegistryWebhook")
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

            if actions is None and not opts.urn:
                raise TypeError("Missing required property 'actions'")
            __props__['actions'] = actions
            __props__['custom_headers'] = custom_headers
            __props__['location'] = location
            __props__['name'] = name
            if registry_name is None and not opts.urn:
                raise TypeError("Missing required property 'registry_name'")
            __props__['registry_name'] = registry_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['scope'] = scope
            if service_uri is None and not opts.urn:
                raise TypeError("Missing required property 'service_uri'")
            __props__['service_uri'] = service_uri
            __props__['status'] = status
            __props__['tags'] = tags
        super(RegistryWebook, __self__).__init__(
            'azure:containerservice/registryWebook:RegistryWebook',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            custom_headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            registry_name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            scope: Optional[pulumi.Input[str]] = None,
            service_uri: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'RegistryWebook':
        """
        Get an existing RegistryWebook resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] actions: A list of actions that trigger the Webhook to post notifications. At least one action needs to be specified. Valid values are: `push`, `delete`, `quarantine`, `chart_push`, `chart_delete`
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] custom_headers: Custom headers that will be added to the webhook notifications request.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Container Registry Webhook. Changing this forces a new resource to be created.
        :param pulumi.Input[str] registry_name: The Name of Container registry this Webhook belongs to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Container Registry Webhook. Changing this forces a new resource to be created.
        :param pulumi.Input[str] scope: Specifies the scope of repositories that can trigger an event. For example, `foo:*` means events for all tags under repository `foo`. `foo:bar` means events for 'foo:bar' only. `foo` is equivalent to `foo:latest`. Empty means all events.
        :param pulumi.Input[str] service_uri: Specifies the service URI for the Webhook to post notifications.
        :param pulumi.Input[str] status: Specifies if this Webhook triggers notifications or not. Valid values: `enabled` and `disabled`. Default is `enabled`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["actions"] = actions
        __props__["custom_headers"] = custom_headers
        __props__["location"] = location
        __props__["name"] = name
        __props__["registry_name"] = registry_name
        __props__["resource_group_name"] = resource_group_name
        __props__["scope"] = scope
        __props__["service_uri"] = service_uri
        __props__["status"] = status
        __props__["tags"] = tags
        return RegistryWebook(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of actions that trigger the Webhook to post notifications. At least one action needs to be specified. Valid values are: `push`, `delete`, `quarantine`, `chart_push`, `chart_delete`
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Custom headers that will be added to the webhook notifications request.
        """
        return pulumi.get(self, "custom_headers")

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
        Specifies the name of the Container Registry Webhook. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> pulumi.Output[str]:
        """
        The Name of Container registry this Webhook belongs to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "registry_name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to create the Container Registry Webhook. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the scope of repositories that can trigger an event. For example, `foo:*` means events for all tags under repository `foo`. `foo:bar` means events for 'foo:bar' only. `foo` is equivalent to `foo:latest`. Empty means all events.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="serviceUri")
    def service_uri(self) -> pulumi.Output[str]:
        """
        Specifies the service URI for the Webhook to post notifications.
        """
        return pulumi.get(self, "service_uri")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies if this Webhook triggers notifications or not. Valid values: `enabled` and `disabled`. Default is `enabled`.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

