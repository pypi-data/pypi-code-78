# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Application']


class Application(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 allow_updates: Optional[pulumi.Input[bool]] = None,
                 default_version: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages Azure Batch Application instance.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_batch_account_account = azure.batch.Account("exampleBatch/accountAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            pool_allocation_mode="BatchService",
            storage_account_id=example_account.id)
        example_application = azure.batch.Application("exampleApplication",
            resource_group_name=example_resource_group.name,
            account_name=example_batch / account_account["name"])
        ```

        ## Import

        Batch Applications can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:batch/application:Application example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/example-rg/providers/Microsoft.Batch/batchAccounts/exampleba/applications/example-batch-application
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the Batch account. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] allow_updates: A value indicating whether packages within the application may be overwritten using the same version string. Defaults to `true`.
        :param pulumi.Input[str] default_version: The package to use if a client requests the application but does not specify a version. This property can only be set to the name of an existing package.
        :param pulumi.Input[str] display_name: The display name for the application.
        :param pulumi.Input[str] name: The name of the application. This must be unique within the account. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the Batch account. Changing this forces a new resource to be created.
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

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__['account_name'] = account_name
            __props__['allow_updates'] = allow_updates
            __props__['default_version'] = default_version
            __props__['display_name'] = display_name
            __props__['name'] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
        super(Application, __self__).__init__(
            'azure:batch/application:Application',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_name: Optional[pulumi.Input[str]] = None,
            allow_updates: Optional[pulumi.Input[bool]] = None,
            default_version: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None) -> 'Application':
        """
        Get an existing Application resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the Batch account. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] allow_updates: A value indicating whether packages within the application may be overwritten using the same version string. Defaults to `true`.
        :param pulumi.Input[str] default_version: The package to use if a client requests the application but does not specify a version. This property can only be set to the name of an existing package.
        :param pulumi.Input[str] display_name: The display name for the application.
        :param pulumi.Input[str] name: The name of the application. This must be unique within the account. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the Batch account. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["account_name"] = account_name
        __props__["allow_updates"] = allow_updates
        __props__["default_version"] = default_version
        __props__["display_name"] = display_name
        __props__["name"] = name
        __props__["resource_group_name"] = resource_group_name
        return Application(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Output[str]:
        """
        The name of the Batch account. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "account_name")

    @property
    @pulumi.getter(name="allowUpdates")
    def allow_updates(self) -> pulumi.Output[Optional[bool]]:
        """
        A value indicating whether packages within the application may be overwritten using the same version string. Defaults to `true`.
        """
        return pulumi.get(self, "allow_updates")

    @property
    @pulumi.getter(name="defaultVersion")
    def default_version(self) -> pulumi.Output[Optional[str]]:
        """
        The package to use if a client requests the application but does not specify a version. This property can only be set to the name of an existing package.
        """
        return pulumi.get(self, "default_version")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The display name for the application.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the application. This must be unique within the account. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group that contains the Batch account. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

