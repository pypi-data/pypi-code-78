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

__all__ = ['Definition']


class Definition(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorizations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DefinitionAuthorizationArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 lighthouse_definition_id: Optional[pulumi.Input[str]] = None,
                 managing_tenant_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a [Lighthouse](https://docs.microsoft.com/en-us/azure/lighthouse) Definition.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        contributor = azure.authorization.get_role_definition(role_definition_id="b24988ac-6180-42a0-ab88-20f7382dd24c")
        example = azure.lighthouse.Definition("example",
            description="This is a lighthouse definition created IaC",
            managing_tenant_id="00000000-0000-0000-0000-000000000000",
            authorizations=[azure.lighthouse.DefinitionAuthorizationArgs(
                principal_id="00000000-0000-0000-0000-000000000000",
                role_definition_id=contributor.role_definition_id,
                principal_display_name="Tier 1 Support",
            )])
        ```

        ## Import

        Lighthouse Definitions can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:lighthouse/definition:Definition example /subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.ManagedServices/registrationDefinitions/00000000-0000-0000-0000-000000000000
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DefinitionAuthorizationArgs']]]] authorizations: An authorization block as defined below.
        :param pulumi.Input[str] description: A description of the Lighthouse Definition.
        :param pulumi.Input[str] lighthouse_definition_id: A unique UUID/GUID which identifies this lighthouse definition - one will be generated if not specified. Changing this forces a new resource to be created.
        :param pulumi.Input[str] managing_tenant_id: The ID of the managing tenant.
        :param pulumi.Input[str] name: The name of the Lighthouse Definition.
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

            if authorizations is None and not opts.urn:
                raise TypeError("Missing required property 'authorizations'")
            __props__['authorizations'] = authorizations
            __props__['description'] = description
            __props__['lighthouse_definition_id'] = lighthouse_definition_id
            if managing_tenant_id is None and not opts.urn:
                raise TypeError("Missing required property 'managing_tenant_id'")
            __props__['managing_tenant_id'] = managing_tenant_id
            __props__['name'] = name
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__['scope'] = scope
        super(Definition, __self__).__init__(
            'azure:lighthouse/definition:Definition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            authorizations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DefinitionAuthorizationArgs']]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            lighthouse_definition_id: Optional[pulumi.Input[str]] = None,
            managing_tenant_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            scope: Optional[pulumi.Input[str]] = None) -> 'Definition':
        """
        Get an existing Definition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DefinitionAuthorizationArgs']]]] authorizations: An authorization block as defined below.
        :param pulumi.Input[str] description: A description of the Lighthouse Definition.
        :param pulumi.Input[str] lighthouse_definition_id: A unique UUID/GUID which identifies this lighthouse definition - one will be generated if not specified. Changing this forces a new resource to be created.
        :param pulumi.Input[str] managing_tenant_id: The ID of the managing tenant.
        :param pulumi.Input[str] name: The name of the Lighthouse Definition.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["authorizations"] = authorizations
        __props__["description"] = description
        __props__["lighthouse_definition_id"] = lighthouse_definition_id
        __props__["managing_tenant_id"] = managing_tenant_id
        __props__["name"] = name
        __props__["scope"] = scope
        return Definition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def authorizations(self) -> pulumi.Output[Sequence['outputs.DefinitionAuthorization']]:
        """
        An authorization block as defined below.
        """
        return pulumi.get(self, "authorizations")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the Lighthouse Definition.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lighthouseDefinitionId")
    def lighthouse_definition_id(self) -> pulumi.Output[str]:
        """
        A unique UUID/GUID which identifies this lighthouse definition - one will be generated if not specified. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "lighthouse_definition_id")

    @property
    @pulumi.getter(name="managingTenantId")
    def managing_tenant_id(self) -> pulumi.Output[str]:
        """
        The ID of the managing tenant.
        """
        return pulumi.get(self, "managing_tenant_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Lighthouse Definition.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[str]:
        return pulumi.get(self, "scope")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

