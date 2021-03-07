# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Rule']


class Rule(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backend_address_pool_id: Optional[pulumi.Input[str]] = None,
                 backend_port: Optional[pulumi.Input[int]] = None,
                 disable_outbound_snat: Optional[pulumi.Input[bool]] = None,
                 enable_floating_ip: Optional[pulumi.Input[bool]] = None,
                 enable_tcp_reset: Optional[pulumi.Input[bool]] = None,
                 frontend_ip_configuration_name: Optional[pulumi.Input[str]] = None,
                 frontend_port: Optional[pulumi.Input[int]] = None,
                 idle_timeout_in_minutes: Optional[pulumi.Input[int]] = None,
                 load_distribution: Optional[pulumi.Input[str]] = None,
                 loadbalancer_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 probe_id: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Load Balancer Rule.

        > **NOTE** When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_public_ip = azure.network.PublicIp("examplePublicIp",
            location="West US",
            resource_group_name=example_resource_group.name,
            allocation_method="Static")
        example_load_balancer = azure.lb.LoadBalancer("exampleLoadBalancer",
            location="West US",
            resource_group_name=example_resource_group.name,
            frontend_ip_configurations=[azure.lb.LoadBalancerFrontendIpConfigurationArgs(
                name="PublicIPAddress",
                public_ip_address_id=example_public_ip.id,
            )])
        example_rule = azure.lb.Rule("exampleRule",
            resource_group_name=example_resource_group.name,
            loadbalancer_id=example_load_balancer.id,
            protocol="Tcp",
            frontend_port=3389,
            backend_port=3389,
            frontend_ip_configuration_name="PublicIPAddress")
        ```

        ## Import

        Load Balancer Rules can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:lb/rule:Rule example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Network/loadBalancers/lb1/loadBalancingRules/rule1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] backend_address_pool_id: A reference to a Backend Address Pool over which this Load Balancing Rule operates.
        :param pulumi.Input[int] backend_port: The port used for internal connections on the endpoint. Possible values range between 0 and 65535, inclusive.
        :param pulumi.Input[bool] disable_outbound_snat: Is snat enabled for this Load Balancer Rule? Default `false`.
        :param pulumi.Input[bool] enable_floating_ip: Are the Floating IPs enabled for this Load Balncer Rule? A "floating” IP is reassigned to a secondary server in case the primary server fails. Required to configure a SQL AlwaysOn Availability Group. Defaults to `false`.
        :param pulumi.Input[bool] enable_tcp_reset: Is TCP Reset enabled for this Load Balancer Rule? Defaults to `false`.
        :param pulumi.Input[str] frontend_ip_configuration_name: The name of the frontend IP configuration to which the rule is associated.
        :param pulumi.Input[int] frontend_port: The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 0 and 65534, inclusive.
        :param pulumi.Input[int] idle_timeout_in_minutes: Specifies the idle timeout in minutes for TCP connections. Valid values are between `4` and `30` minutes. Defaults to `4` minutes.
        :param pulumi.Input[str] load_distribution: Specifies the load balancing distribution type to be used by the Load Balancer. Possible values are: `Default` – The load balancer is configured to use a 5 tuple hash to map traffic to available servers. `SourceIP` – The load balancer is configured to use a 2 tuple hash to map traffic to available servers. `SourceIPProtocol` – The load balancer is configured to use a 3 tuple hash to map traffic to available servers. Also known as Session Persistence, where  the options are called `None`, `Client IP` and `Client IP and Protocol` respectively.
        :param pulumi.Input[str] loadbalancer_id: The ID of the Load Balancer in which to create the Rule.
        :param pulumi.Input[str] name: Specifies the name of the LB Rule.
        :param pulumi.Input[str] probe_id: A reference to a Probe used by this Load Balancing Rule.
        :param pulumi.Input[str] protocol: The transport protocol for the external endpoint. Possible values are `Tcp`, `Udp` or `All`.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the resource.
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

            __props__['backend_address_pool_id'] = backend_address_pool_id
            if backend_port is None and not opts.urn:
                raise TypeError("Missing required property 'backend_port'")
            __props__['backend_port'] = backend_port
            __props__['disable_outbound_snat'] = disable_outbound_snat
            __props__['enable_floating_ip'] = enable_floating_ip
            __props__['enable_tcp_reset'] = enable_tcp_reset
            if frontend_ip_configuration_name is None and not opts.urn:
                raise TypeError("Missing required property 'frontend_ip_configuration_name'")
            __props__['frontend_ip_configuration_name'] = frontend_ip_configuration_name
            if frontend_port is None and not opts.urn:
                raise TypeError("Missing required property 'frontend_port'")
            __props__['frontend_port'] = frontend_port
            __props__['idle_timeout_in_minutes'] = idle_timeout_in_minutes
            __props__['load_distribution'] = load_distribution
            if loadbalancer_id is None and not opts.urn:
                raise TypeError("Missing required property 'loadbalancer_id'")
            __props__['loadbalancer_id'] = loadbalancer_id
            __props__['name'] = name
            __props__['probe_id'] = probe_id
            if protocol is None and not opts.urn:
                raise TypeError("Missing required property 'protocol'")
            __props__['protocol'] = protocol
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['frontend_ip_configuration_id'] = None
        super(Rule, __self__).__init__(
            'azure:lb/rule:Rule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            backend_address_pool_id: Optional[pulumi.Input[str]] = None,
            backend_port: Optional[pulumi.Input[int]] = None,
            disable_outbound_snat: Optional[pulumi.Input[bool]] = None,
            enable_floating_ip: Optional[pulumi.Input[bool]] = None,
            enable_tcp_reset: Optional[pulumi.Input[bool]] = None,
            frontend_ip_configuration_id: Optional[pulumi.Input[str]] = None,
            frontend_ip_configuration_name: Optional[pulumi.Input[str]] = None,
            frontend_port: Optional[pulumi.Input[int]] = None,
            idle_timeout_in_minutes: Optional[pulumi.Input[int]] = None,
            load_distribution: Optional[pulumi.Input[str]] = None,
            loadbalancer_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            probe_id: Optional[pulumi.Input[str]] = None,
            protocol: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None) -> 'Rule':
        """
        Get an existing Rule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] backend_address_pool_id: A reference to a Backend Address Pool over which this Load Balancing Rule operates.
        :param pulumi.Input[int] backend_port: The port used for internal connections on the endpoint. Possible values range between 0 and 65535, inclusive.
        :param pulumi.Input[bool] disable_outbound_snat: Is snat enabled for this Load Balancer Rule? Default `false`.
        :param pulumi.Input[bool] enable_floating_ip: Are the Floating IPs enabled for this Load Balncer Rule? A "floating” IP is reassigned to a secondary server in case the primary server fails. Required to configure a SQL AlwaysOn Availability Group. Defaults to `false`.
        :param pulumi.Input[bool] enable_tcp_reset: Is TCP Reset enabled for this Load Balancer Rule? Defaults to `false`.
        :param pulumi.Input[str] frontend_ip_configuration_name: The name of the frontend IP configuration to which the rule is associated.
        :param pulumi.Input[int] frontend_port: The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 0 and 65534, inclusive.
        :param pulumi.Input[int] idle_timeout_in_minutes: Specifies the idle timeout in minutes for TCP connections. Valid values are between `4` and `30` minutes. Defaults to `4` minutes.
        :param pulumi.Input[str] load_distribution: Specifies the load balancing distribution type to be used by the Load Balancer. Possible values are: `Default` – The load balancer is configured to use a 5 tuple hash to map traffic to available servers. `SourceIP` – The load balancer is configured to use a 2 tuple hash to map traffic to available servers. `SourceIPProtocol` – The load balancer is configured to use a 3 tuple hash to map traffic to available servers. Also known as Session Persistence, where  the options are called `None`, `Client IP` and `Client IP and Protocol` respectively.
        :param pulumi.Input[str] loadbalancer_id: The ID of the Load Balancer in which to create the Rule.
        :param pulumi.Input[str] name: Specifies the name of the LB Rule.
        :param pulumi.Input[str] probe_id: A reference to a Probe used by this Load Balancing Rule.
        :param pulumi.Input[str] protocol: The transport protocol for the external endpoint. Possible values are `Tcp`, `Udp` or `All`.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["backend_address_pool_id"] = backend_address_pool_id
        __props__["backend_port"] = backend_port
        __props__["disable_outbound_snat"] = disable_outbound_snat
        __props__["enable_floating_ip"] = enable_floating_ip
        __props__["enable_tcp_reset"] = enable_tcp_reset
        __props__["frontend_ip_configuration_id"] = frontend_ip_configuration_id
        __props__["frontend_ip_configuration_name"] = frontend_ip_configuration_name
        __props__["frontend_port"] = frontend_port
        __props__["idle_timeout_in_minutes"] = idle_timeout_in_minutes
        __props__["load_distribution"] = load_distribution
        __props__["loadbalancer_id"] = loadbalancer_id
        __props__["name"] = name
        __props__["probe_id"] = probe_id
        __props__["protocol"] = protocol
        __props__["resource_group_name"] = resource_group_name
        return Rule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="backendAddressPoolId")
    def backend_address_pool_id(self) -> pulumi.Output[str]:
        """
        A reference to a Backend Address Pool over which this Load Balancing Rule operates.
        """
        return pulumi.get(self, "backend_address_pool_id")

    @property
    @pulumi.getter(name="backendPort")
    def backend_port(self) -> pulumi.Output[int]:
        """
        The port used for internal connections on the endpoint. Possible values range between 0 and 65535, inclusive.
        """
        return pulumi.get(self, "backend_port")

    @property
    @pulumi.getter(name="disableOutboundSnat")
    def disable_outbound_snat(self) -> pulumi.Output[Optional[bool]]:
        """
        Is snat enabled for this Load Balancer Rule? Default `false`.
        """
        return pulumi.get(self, "disable_outbound_snat")

    @property
    @pulumi.getter(name="enableFloatingIp")
    def enable_floating_ip(self) -> pulumi.Output[Optional[bool]]:
        """
        Are the Floating IPs enabled for this Load Balncer Rule? A "floating” IP is reassigned to a secondary server in case the primary server fails. Required to configure a SQL AlwaysOn Availability Group. Defaults to `false`.
        """
        return pulumi.get(self, "enable_floating_ip")

    @property
    @pulumi.getter(name="enableTcpReset")
    def enable_tcp_reset(self) -> pulumi.Output[Optional[bool]]:
        """
        Is TCP Reset enabled for this Load Balancer Rule? Defaults to `false`.
        """
        return pulumi.get(self, "enable_tcp_reset")

    @property
    @pulumi.getter(name="frontendIpConfigurationId")
    def frontend_ip_configuration_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "frontend_ip_configuration_id")

    @property
    @pulumi.getter(name="frontendIpConfigurationName")
    def frontend_ip_configuration_name(self) -> pulumi.Output[str]:
        """
        The name of the frontend IP configuration to which the rule is associated.
        """
        return pulumi.get(self, "frontend_ip_configuration_name")

    @property
    @pulumi.getter(name="frontendPort")
    def frontend_port(self) -> pulumi.Output[int]:
        """
        The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 0 and 65534, inclusive.
        """
        return pulumi.get(self, "frontend_port")

    @property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> pulumi.Output[int]:
        """
        Specifies the idle timeout in minutes for TCP connections. Valid values are between `4` and `30` minutes. Defaults to `4` minutes.
        """
        return pulumi.get(self, "idle_timeout_in_minutes")

    @property
    @pulumi.getter(name="loadDistribution")
    def load_distribution(self) -> pulumi.Output[str]:
        """
        Specifies the load balancing distribution type to be used by the Load Balancer. Possible values are: `Default` – The load balancer is configured to use a 5 tuple hash to map traffic to available servers. `SourceIP` – The load balancer is configured to use a 2 tuple hash to map traffic to available servers. `SourceIPProtocol` – The load balancer is configured to use a 3 tuple hash to map traffic to available servers. Also known as Session Persistence, where  the options are called `None`, `Client IP` and `Client IP and Protocol` respectively.
        """
        return pulumi.get(self, "load_distribution")

    @property
    @pulumi.getter(name="loadbalancerId")
    def loadbalancer_id(self) -> pulumi.Output[str]:
        """
        The ID of the Load Balancer in which to create the Rule.
        """
        return pulumi.get(self, "loadbalancer_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the LB Rule.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="probeId")
    def probe_id(self) -> pulumi.Output[str]:
        """
        A reference to a Probe used by this Load Balancing Rule.
        """
        return pulumi.get(self, "probe_id")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[str]:
        """
        The transport protocol for the external endpoint. Possible values are `Tcp`, `Udp` or `All`.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to create the resource.
        """
        return pulumi.get(self, "resource_group_name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

