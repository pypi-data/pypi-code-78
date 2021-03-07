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

__all__ = ['FailoverGroup']


class FailoverGroup(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 databases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 partner_servers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FailoverGroupPartnerServerArgs']]]]] = None,
                 read_write_endpoint_failover_policy: Optional[pulumi.Input[pulumi.InputType['FailoverGroupReadWriteEndpointFailoverPolicyArgs']]] = None,
                 readonly_endpoint_failover_policy: Optional[pulumi.Input[pulumi.InputType['FailoverGroupReadonlyEndpointFailoverPolicyArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a failover group of databases on a collection of Azure SQL servers.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        primary = azure.sql.SqlServer("primary",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            version="12.0",
            administrator_login="sqladmin",
            administrator_login_password="pa$$w0rd")
        secondary = azure.sql.SqlServer("secondary",
            resource_group_name=example_resource_group.name,
            location="northeurope",
            version="12.0",
            administrator_login="sqladmin",
            administrator_login_password="pa$$w0rd")
        db1 = azure.sql.Database("db1",
            resource_group_name=primary.resource_group_name,
            location=primary.location,
            server_name=primary.name)
        example_failover_group = azure.sql.FailoverGroup("exampleFailoverGroup",
            resource_group_name=primary.resource_group_name,
            server_name=primary.name,
            databases=[db1.id],
            partner_servers=[azure.sql.FailoverGroupPartnerServerArgs(
                id=secondary.id,
            )],
            read_write_endpoint_failover_policy=azure.sql.FailoverGroupReadWriteEndpointFailoverPolicyArgs(
                mode="Automatic",
                grace_minutes=60,
            ))
        ```

        ## Import

        SQL Failover Groups can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:sql/failoverGroup:FailoverGroup example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myresourcegroup/providers/Microsoft.Sql/servers/myserver/failovergroups/group1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] databases: A list of database ids to add to the failover group
        :param pulumi.Input[str] name: The name of the failover group. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FailoverGroupPartnerServerArgs']]]] partner_servers: A list of secondary servers as documented below
        :param pulumi.Input[pulumi.InputType['FailoverGroupReadWriteEndpointFailoverPolicyArgs']] read_write_endpoint_failover_policy: A read/write policy as documented below
        :param pulumi.Input[pulumi.InputType['FailoverGroupReadonlyEndpointFailoverPolicyArgs']] readonly_endpoint_failover_policy: a read-only policy as documented below
        :param pulumi.Input[str] resource_group_name: The name of the resource group containing the SQL server
        :param pulumi.Input[str] server_name: The name of the primary SQL server. Changing this forces a new resource to be created.
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

            __props__['databases'] = databases
            __props__['name'] = name
            if partner_servers is None and not opts.urn:
                raise TypeError("Missing required property 'partner_servers'")
            __props__['partner_servers'] = partner_servers
            if read_write_endpoint_failover_policy is None and not opts.urn:
                raise TypeError("Missing required property 'read_write_endpoint_failover_policy'")
            __props__['read_write_endpoint_failover_policy'] = read_write_endpoint_failover_policy
            __props__['readonly_endpoint_failover_policy'] = readonly_endpoint_failover_policy
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if server_name is None and not opts.urn:
                raise TypeError("Missing required property 'server_name'")
            __props__['server_name'] = server_name
            __props__['tags'] = tags
            __props__['location'] = None
            __props__['role'] = None
        super(FailoverGroup, __self__).__init__(
            'azure:sql/failoverGroup:FailoverGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            databases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            partner_servers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FailoverGroupPartnerServerArgs']]]]] = None,
            read_write_endpoint_failover_policy: Optional[pulumi.Input[pulumi.InputType['FailoverGroupReadWriteEndpointFailoverPolicyArgs']]] = None,
            readonly_endpoint_failover_policy: Optional[pulumi.Input[pulumi.InputType['FailoverGroupReadonlyEndpointFailoverPolicyArgs']]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            role: Optional[pulumi.Input[str]] = None,
            server_name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'FailoverGroup':
        """
        Get an existing FailoverGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] databases: A list of database ids to add to the failover group
        :param pulumi.Input[str] location: the location of the failover group.
        :param pulumi.Input[str] name: The name of the failover group. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FailoverGroupPartnerServerArgs']]]] partner_servers: A list of secondary servers as documented below
        :param pulumi.Input[pulumi.InputType['FailoverGroupReadWriteEndpointFailoverPolicyArgs']] read_write_endpoint_failover_policy: A read/write policy as documented below
        :param pulumi.Input[pulumi.InputType['FailoverGroupReadonlyEndpointFailoverPolicyArgs']] readonly_endpoint_failover_policy: a read-only policy as documented below
        :param pulumi.Input[str] resource_group_name: The name of the resource group containing the SQL server
        :param pulumi.Input[str] role: local replication role of the failover group instance.
        :param pulumi.Input[str] server_name: The name of the primary SQL server. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["databases"] = databases
        __props__["location"] = location
        __props__["name"] = name
        __props__["partner_servers"] = partner_servers
        __props__["read_write_endpoint_failover_policy"] = read_write_endpoint_failover_policy
        __props__["readonly_endpoint_failover_policy"] = readonly_endpoint_failover_policy
        __props__["resource_group_name"] = resource_group_name
        __props__["role"] = role
        __props__["server_name"] = server_name
        __props__["tags"] = tags
        return FailoverGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def databases(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of database ids to add to the failover group
        """
        return pulumi.get(self, "databases")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        the location of the failover group.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the failover group. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partnerServers")
    def partner_servers(self) -> pulumi.Output[Sequence['outputs.FailoverGroupPartnerServer']]:
        """
        A list of secondary servers as documented below
        """
        return pulumi.get(self, "partner_servers")

    @property
    @pulumi.getter(name="readWriteEndpointFailoverPolicy")
    def read_write_endpoint_failover_policy(self) -> pulumi.Output['outputs.FailoverGroupReadWriteEndpointFailoverPolicy']:
        """
        A read/write policy as documented below
        """
        return pulumi.get(self, "read_write_endpoint_failover_policy")

    @property
    @pulumi.getter(name="readonlyEndpointFailoverPolicy")
    def readonly_endpoint_failover_policy(self) -> pulumi.Output['outputs.FailoverGroupReadonlyEndpointFailoverPolicy']:
        """
        a read-only policy as documented below
        """
        return pulumi.get(self, "readonly_endpoint_failover_policy")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group containing the SQL server
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        local replication role of the failover group instance.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Output[str]:
        """
        The name of the primary SQL server. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "server_name")

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

