# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['UserAssignedIdentity']

warnings.warn("""azure.msi.UserAssignedIdentity has been deprecated in favor of azure.authorization.UserAssignedIdentity""", DeprecationWarning)


class UserAssignedIdentity(pulumi.CustomResource):
    warnings.warn("""azure.msi.UserAssignedIdentity has been deprecated in favor of azure.authorization.UserAssignedIdentity""", DeprecationWarning)

    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a user assigned identity.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_user_assigned_identity = azure.authorization.UserAssignedIdentity("exampleUserAssignedIdentity",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location)
        ```

        ## Import

        User Assigned Identities can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:msi/userAssignedIdentity:UserAssignedIdentity exampleIdentity /subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/acceptanceTestResourceGroup1/providers/Microsoft.ManagedIdentity/userAssignedIdentities/testIdentity
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The location/region where the user assigned identity is
               created.
        :param pulumi.Input[str] name: The name of the user assigned identity. Changing this forces a
               new identity to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to
               create the user assigned identity.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        pulumi.log.warn("UserAssignedIdentity is deprecated: azure.msi.UserAssignedIdentity has been deprecated in favor of azure.authorization.UserAssignedIdentity")
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

            __props__['location'] = location
            __props__['name'] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['tags'] = tags
            __props__['client_id'] = None
            __props__['principal_id'] = None
        super(UserAssignedIdentity, __self__).__init__(
            'azure:msi/userAssignedIdentity:UserAssignedIdentity',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            client_id: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            principal_id: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'UserAssignedIdentity':
        """
        Get an existing UserAssignedIdentity resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] client_id: Client ID associated with the user assigned identity.
        :param pulumi.Input[str] location: The location/region where the user assigned identity is
               created.
        :param pulumi.Input[str] name: The name of the user assigned identity. Changing this forces a
               new identity to be created.
        :param pulumi.Input[str] principal_id: Service Principal ID associated with the user assigned identity.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to
               create the user assigned identity.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["client_id"] = client_id
        __props__["location"] = location
        __props__["name"] = name
        __props__["principal_id"] = principal_id
        __props__["resource_group_name"] = resource_group_name
        __props__["tags"] = tags
        return UserAssignedIdentity(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Output[str]:
        """
        Client ID associated with the user assigned identity.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location/region where the user assigned identity is
        created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the user assigned identity. Changing this forces a
        new identity to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Output[str]:
        """
        Service Principal ID associated with the user assigned identity.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to
        create the user assigned identity.
        """
        return pulumi.get(self, "resource_group_name")

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

