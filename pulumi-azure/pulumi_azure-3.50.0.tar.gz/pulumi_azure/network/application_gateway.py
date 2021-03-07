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

__all__ = ['ApplicationGateway']


class ApplicationGateway(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayAuthenticationCertificateArgs']]]]] = None,
                 autoscale_configuration: Optional[pulumi.Input[pulumi.InputType['ApplicationGatewayAutoscaleConfigurationArgs']]] = None,
                 backend_address_pools: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayBackendAddressPoolArgs']]]]] = None,
                 backend_http_settings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayBackendHttpSettingArgs']]]]] = None,
                 custom_error_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayCustomErrorConfigurationArgs']]]]] = None,
                 enable_http2: Optional[pulumi.Input[bool]] = None,
                 firewall_policy_id: Optional[pulumi.Input[str]] = None,
                 frontend_ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayFrontendIpConfigurationArgs']]]]] = None,
                 frontend_ports: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayFrontendPortArgs']]]]] = None,
                 gateway_ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayGatewayIpConfigurationArgs']]]]] = None,
                 http_listeners: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayHttpListenerArgs']]]]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ApplicationGatewayIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 probes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayProbeArgs']]]]] = None,
                 redirect_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayRedirectConfigurationArgs']]]]] = None,
                 request_routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayRequestRoutingRuleArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rewrite_rule_sets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayRewriteRuleSetArgs']]]]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['ApplicationGatewaySkuArgs']]] = None,
                 ssl_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewaySslCertificateArgs']]]]] = None,
                 ssl_policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewaySslPolicyArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 trusted_root_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayTrustedRootCertificateArgs']]]]] = None,
                 url_path_maps: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayUrlPathMapArgs']]]]] = None,
                 waf_configuration: Optional[pulumi.Input[pulumi.InputType['ApplicationGatewayWafConfigurationArgs']]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an Application Gateway.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            address_spaces=["10.254.0.0/16"])
        frontend = azure.network.Subnet("frontend",
            resource_group_name=example_resource_group.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.254.0.0/24"])
        backend = azure.network.Subnet("backend",
            resource_group_name=example_resource_group.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.254.2.0/24"])
        example_public_ip = azure.network.PublicIp("examplePublicIp",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            allocation_method="Dynamic")
        backend_address_pool_name = example_virtual_network.name.apply(lambda name: f"{name}-beap")
        frontend_port_name = example_virtual_network.name.apply(lambda name: f"{name}-feport")
        frontend_ip_configuration_name = example_virtual_network.name.apply(lambda name: f"{name}-feip")
        http_setting_name = example_virtual_network.name.apply(lambda name: f"{name}-be-htst")
        listener_name = example_virtual_network.name.apply(lambda name: f"{name}-httplstn")
        request_routing_rule_name = example_virtual_network.name.apply(lambda name: f"{name}-rqrt")
        redirect_configuration_name = example_virtual_network.name.apply(lambda name: f"{name}-rdrcfg")
        network = azure.network.ApplicationGateway("network",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            sku=azure.network.ApplicationGatewaySkuArgs(
                name="Standard_Small",
                tier="Standard",
                capacity=2,
            ),
            gateway_ip_configurations=[azure.network.ApplicationGatewayGatewayIpConfigurationArgs(
                name="my-gateway-ip-configuration",
                subnet_id=frontend.id,
            )],
            frontend_ports=[azure.network.ApplicationGatewayFrontendPortArgs(
                name=frontend_port_name,
                port=80,
            )],
            frontend_ip_configurations=[azure.network.ApplicationGatewayFrontendIpConfigurationArgs(
                name=frontend_ip_configuration_name,
                public_ip_address_id=example_public_ip.id,
            )],
            backend_address_pools=[azure.network.ApplicationGatewayBackendAddressPoolArgs(
                name=backend_address_pool_name,
            )],
            backend_http_settings=[azure.network.ApplicationGatewayBackendHttpSettingArgs(
                name=http_setting_name,
                cookie_based_affinity="Disabled",
                path="/path1/",
                port=80,
                protocol="Http",
                request_timeout=60,
            )],
            http_listeners=[azure.network.ApplicationGatewayHttpListenerArgs(
                name=listener_name,
                frontend_ip_configuration_name=frontend_ip_configuration_name,
                frontend_port_name=frontend_port_name,
                protocol="Http",
            )],
            request_routing_rules=[azure.network.ApplicationGatewayRequestRoutingRuleArgs(
                name=request_routing_rule_name,
                rule_type="Basic",
                http_listener_name=listener_name,
                backend_address_pool_name=backend_address_pool_name,
                backend_http_settings_name=http_setting_name,
            )])
        ```

        ## Import

        Application Gateway's can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:network/applicationGateway:ApplicationGateway example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Network/applicationGateways/myGateway1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayAuthenticationCertificateArgs']]]] authentication_certificates: One or more `authentication_certificate` blocks as defined below.
        :param pulumi.Input[pulumi.InputType['ApplicationGatewayAutoscaleConfigurationArgs']] autoscale_configuration: A `autoscale_configuration` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayBackendAddressPoolArgs']]]] backend_address_pools: One or more `backend_address_pool` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayBackendHttpSettingArgs']]]] backend_http_settings: One or more `backend_http_settings` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayCustomErrorConfigurationArgs']]]] custom_error_configurations: One or more `custom_error_configuration` blocks as defined below.
        :param pulumi.Input[bool] enable_http2: Is HTTP2 enabled on the application gateway resource? Defaults to `false`.
        :param pulumi.Input[str] firewall_policy_id: The ID of the Web Application Firewall Policy.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayFrontendIpConfigurationArgs']]]] frontend_ip_configurations: One or more `frontend_ip_configuration` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayFrontendPortArgs']]]] frontend_ports: One or more `frontend_port` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayGatewayIpConfigurationArgs']]]] gateway_ip_configurations: One or more `gateway_ip_configuration` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayHttpListenerArgs']]]] http_listeners: One or more `http_listener` blocks as defined below.
        :param pulumi.Input[pulumi.InputType['ApplicationGatewayIdentityArgs']] identity: A `identity` block.
        :param pulumi.Input[str] location: The Azure region where the Application Gateway should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Application Gateway. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayProbeArgs']]]] probes: One or more `probe` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayRedirectConfigurationArgs']]]] redirect_configurations: A `redirect_configuration` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayRequestRoutingRuleArgs']]]] request_routing_rules: One or more `request_routing_rule` blocks as defined below.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to the Application Gateway should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayRewriteRuleSetArgs']]]] rewrite_rule_sets: One or more `rewrite_rule_set` blocks as defined below. Only valid for v2 SKUs.
        :param pulumi.Input[pulumi.InputType['ApplicationGatewaySkuArgs']] sku: A `sku` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewaySslCertificateArgs']]]] ssl_certificates: One or more `ssl_certificate` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewaySslPolicyArgs']]]] ssl_policies: a `ssl policy` block as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayTrustedRootCertificateArgs']]]] trusted_root_certificates: One or more `trusted_root_certificate` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayUrlPathMapArgs']]]] url_path_maps: One or more `url_path_map` blocks as defined below.
        :param pulumi.Input[pulumi.InputType['ApplicationGatewayWafConfigurationArgs']] waf_configuration: A `waf_configuration` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: A collection of availability zones to spread the Application Gateway over.
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

            __props__['authentication_certificates'] = authentication_certificates
            __props__['autoscale_configuration'] = autoscale_configuration
            if backend_address_pools is None and not opts.urn:
                raise TypeError("Missing required property 'backend_address_pools'")
            __props__['backend_address_pools'] = backend_address_pools
            if backend_http_settings is None and not opts.urn:
                raise TypeError("Missing required property 'backend_http_settings'")
            __props__['backend_http_settings'] = backend_http_settings
            __props__['custom_error_configurations'] = custom_error_configurations
            __props__['enable_http2'] = enable_http2
            __props__['firewall_policy_id'] = firewall_policy_id
            if frontend_ip_configurations is None and not opts.urn:
                raise TypeError("Missing required property 'frontend_ip_configurations'")
            __props__['frontend_ip_configurations'] = frontend_ip_configurations
            if frontend_ports is None and not opts.urn:
                raise TypeError("Missing required property 'frontend_ports'")
            __props__['frontend_ports'] = frontend_ports
            if gateway_ip_configurations is None and not opts.urn:
                raise TypeError("Missing required property 'gateway_ip_configurations'")
            __props__['gateway_ip_configurations'] = gateway_ip_configurations
            if http_listeners is None and not opts.urn:
                raise TypeError("Missing required property 'http_listeners'")
            __props__['http_listeners'] = http_listeners
            __props__['identity'] = identity
            __props__['location'] = location
            __props__['name'] = name
            __props__['probes'] = probes
            __props__['redirect_configurations'] = redirect_configurations
            if request_routing_rules is None and not opts.urn:
                raise TypeError("Missing required property 'request_routing_rules'")
            __props__['request_routing_rules'] = request_routing_rules
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['rewrite_rule_sets'] = rewrite_rule_sets
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__['sku'] = sku
            __props__['ssl_certificates'] = ssl_certificates
            __props__['ssl_policies'] = ssl_policies
            __props__['tags'] = tags
            __props__['trusted_root_certificates'] = trusted_root_certificates
            __props__['url_path_maps'] = url_path_maps
            __props__['waf_configuration'] = waf_configuration
            __props__['zones'] = zones
        super(ApplicationGateway, __self__).__init__(
            'azure:network/applicationGateway:ApplicationGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            authentication_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayAuthenticationCertificateArgs']]]]] = None,
            autoscale_configuration: Optional[pulumi.Input[pulumi.InputType['ApplicationGatewayAutoscaleConfigurationArgs']]] = None,
            backend_address_pools: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayBackendAddressPoolArgs']]]]] = None,
            backend_http_settings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayBackendHttpSettingArgs']]]]] = None,
            custom_error_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayCustomErrorConfigurationArgs']]]]] = None,
            enable_http2: Optional[pulumi.Input[bool]] = None,
            firewall_policy_id: Optional[pulumi.Input[str]] = None,
            frontend_ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayFrontendIpConfigurationArgs']]]]] = None,
            frontend_ports: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayFrontendPortArgs']]]]] = None,
            gateway_ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayGatewayIpConfigurationArgs']]]]] = None,
            http_listeners: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayHttpListenerArgs']]]]] = None,
            identity: Optional[pulumi.Input[pulumi.InputType['ApplicationGatewayIdentityArgs']]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            probes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayProbeArgs']]]]] = None,
            redirect_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayRedirectConfigurationArgs']]]]] = None,
            request_routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayRequestRoutingRuleArgs']]]]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            rewrite_rule_sets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayRewriteRuleSetArgs']]]]] = None,
            sku: Optional[pulumi.Input[pulumi.InputType['ApplicationGatewaySkuArgs']]] = None,
            ssl_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewaySslCertificateArgs']]]]] = None,
            ssl_policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewaySslPolicyArgs']]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            trusted_root_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayTrustedRootCertificateArgs']]]]] = None,
            url_path_maps: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayUrlPathMapArgs']]]]] = None,
            waf_configuration: Optional[pulumi.Input[pulumi.InputType['ApplicationGatewayWafConfigurationArgs']]] = None,
            zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'ApplicationGateway':
        """
        Get an existing ApplicationGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayAuthenticationCertificateArgs']]]] authentication_certificates: One or more `authentication_certificate` blocks as defined below.
        :param pulumi.Input[pulumi.InputType['ApplicationGatewayAutoscaleConfigurationArgs']] autoscale_configuration: A `autoscale_configuration` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayBackendAddressPoolArgs']]]] backend_address_pools: One or more `backend_address_pool` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayBackendHttpSettingArgs']]]] backend_http_settings: One or more `backend_http_settings` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayCustomErrorConfigurationArgs']]]] custom_error_configurations: One or more `custom_error_configuration` blocks as defined below.
        :param pulumi.Input[bool] enable_http2: Is HTTP2 enabled on the application gateway resource? Defaults to `false`.
        :param pulumi.Input[str] firewall_policy_id: The ID of the Web Application Firewall Policy.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayFrontendIpConfigurationArgs']]]] frontend_ip_configurations: One or more `frontend_ip_configuration` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayFrontendPortArgs']]]] frontend_ports: One or more `frontend_port` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayGatewayIpConfigurationArgs']]]] gateway_ip_configurations: One or more `gateway_ip_configuration` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayHttpListenerArgs']]]] http_listeners: One or more `http_listener` blocks as defined below.
        :param pulumi.Input[pulumi.InputType['ApplicationGatewayIdentityArgs']] identity: A `identity` block.
        :param pulumi.Input[str] location: The Azure region where the Application Gateway should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Application Gateway. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayProbeArgs']]]] probes: One or more `probe` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayRedirectConfigurationArgs']]]] redirect_configurations: A `redirect_configuration` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayRequestRoutingRuleArgs']]]] request_routing_rules: One or more `request_routing_rule` blocks as defined below.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to the Application Gateway should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayRewriteRuleSetArgs']]]] rewrite_rule_sets: One or more `rewrite_rule_set` blocks as defined below. Only valid for v2 SKUs.
        :param pulumi.Input[pulumi.InputType['ApplicationGatewaySkuArgs']] sku: A `sku` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewaySslCertificateArgs']]]] ssl_certificates: One or more `ssl_certificate` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewaySslPolicyArgs']]]] ssl_policies: a `ssl policy` block as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayTrustedRootCertificateArgs']]]] trusted_root_certificates: One or more `trusted_root_certificate` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayUrlPathMapArgs']]]] url_path_maps: One or more `url_path_map` blocks as defined below.
        :param pulumi.Input[pulumi.InputType['ApplicationGatewayWafConfigurationArgs']] waf_configuration: A `waf_configuration` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: A collection of availability zones to spread the Application Gateway over.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["authentication_certificates"] = authentication_certificates
        __props__["autoscale_configuration"] = autoscale_configuration
        __props__["backend_address_pools"] = backend_address_pools
        __props__["backend_http_settings"] = backend_http_settings
        __props__["custom_error_configurations"] = custom_error_configurations
        __props__["enable_http2"] = enable_http2
        __props__["firewall_policy_id"] = firewall_policy_id
        __props__["frontend_ip_configurations"] = frontend_ip_configurations
        __props__["frontend_ports"] = frontend_ports
        __props__["gateway_ip_configurations"] = gateway_ip_configurations
        __props__["http_listeners"] = http_listeners
        __props__["identity"] = identity
        __props__["location"] = location
        __props__["name"] = name
        __props__["probes"] = probes
        __props__["redirect_configurations"] = redirect_configurations
        __props__["request_routing_rules"] = request_routing_rules
        __props__["resource_group_name"] = resource_group_name
        __props__["rewrite_rule_sets"] = rewrite_rule_sets
        __props__["sku"] = sku
        __props__["ssl_certificates"] = ssl_certificates
        __props__["ssl_policies"] = ssl_policies
        __props__["tags"] = tags
        __props__["trusted_root_certificates"] = trusted_root_certificates
        __props__["url_path_maps"] = url_path_maps
        __props__["waf_configuration"] = waf_configuration
        __props__["zones"] = zones
        return ApplicationGateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authenticationCertificates")
    def authentication_certificates(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayAuthenticationCertificate']]]:
        """
        One or more `authentication_certificate` blocks as defined below.
        """
        return pulumi.get(self, "authentication_certificates")

    @property
    @pulumi.getter(name="autoscaleConfiguration")
    def autoscale_configuration(self) -> pulumi.Output[Optional['outputs.ApplicationGatewayAutoscaleConfiguration']]:
        """
        A `autoscale_configuration` block as defined below.
        """
        return pulumi.get(self, "autoscale_configuration")

    @property
    @pulumi.getter(name="backendAddressPools")
    def backend_address_pools(self) -> pulumi.Output[Sequence['outputs.ApplicationGatewayBackendAddressPool']]:
        """
        One or more `backend_address_pool` blocks as defined below.
        """
        return pulumi.get(self, "backend_address_pools")

    @property
    @pulumi.getter(name="backendHttpSettings")
    def backend_http_settings(self) -> pulumi.Output[Sequence['outputs.ApplicationGatewayBackendHttpSetting']]:
        """
        One or more `backend_http_settings` blocks as defined below.
        """
        return pulumi.get(self, "backend_http_settings")

    @property
    @pulumi.getter(name="customErrorConfigurations")
    def custom_error_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayCustomErrorConfiguration']]]:
        """
        One or more `custom_error_configuration` blocks as defined below.
        """
        return pulumi.get(self, "custom_error_configurations")

    @property
    @pulumi.getter(name="enableHttp2")
    def enable_http2(self) -> pulumi.Output[Optional[bool]]:
        """
        Is HTTP2 enabled on the application gateway resource? Defaults to `false`.
        """
        return pulumi.get(self, "enable_http2")

    @property
    @pulumi.getter(name="firewallPolicyId")
    def firewall_policy_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the Web Application Firewall Policy.
        """
        return pulumi.get(self, "firewall_policy_id")

    @property
    @pulumi.getter(name="frontendIpConfigurations")
    def frontend_ip_configurations(self) -> pulumi.Output[Sequence['outputs.ApplicationGatewayFrontendIpConfiguration']]:
        """
        One or more `frontend_ip_configuration` blocks as defined below.
        """
        return pulumi.get(self, "frontend_ip_configurations")

    @property
    @pulumi.getter(name="frontendPorts")
    def frontend_ports(self) -> pulumi.Output[Sequence['outputs.ApplicationGatewayFrontendPort']]:
        """
        One or more `frontend_port` blocks as defined below.
        """
        return pulumi.get(self, "frontend_ports")

    @property
    @pulumi.getter(name="gatewayIpConfigurations")
    def gateway_ip_configurations(self) -> pulumi.Output[Sequence['outputs.ApplicationGatewayGatewayIpConfiguration']]:
        """
        One or more `gateway_ip_configuration` blocks as defined below.
        """
        return pulumi.get(self, "gateway_ip_configurations")

    @property
    @pulumi.getter(name="httpListeners")
    def http_listeners(self) -> pulumi.Output[Sequence['outputs.ApplicationGatewayHttpListener']]:
        """
        One or more `http_listener` blocks as defined below.
        """
        return pulumi.get(self, "http_listeners")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ApplicationGatewayIdentity']]:
        """
        A `identity` block.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The Azure region where the Application Gateway should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Application Gateway. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def probes(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayProbe']]]:
        """
        One or more `probe` blocks as defined below.
        """
        return pulumi.get(self, "probes")

    @property
    @pulumi.getter(name="redirectConfigurations")
    def redirect_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayRedirectConfiguration']]]:
        """
        A `redirect_configuration` block as defined below.
        """
        return pulumi.get(self, "redirect_configurations")

    @property
    @pulumi.getter(name="requestRoutingRules")
    def request_routing_rules(self) -> pulumi.Output[Sequence['outputs.ApplicationGatewayRequestRoutingRule']]:
        """
        One or more `request_routing_rule` blocks as defined below.
        """
        return pulumi.get(self, "request_routing_rules")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to the Application Gateway should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="rewriteRuleSets")
    def rewrite_rule_sets(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayRewriteRuleSet']]]:
        """
        One or more `rewrite_rule_set` blocks as defined below. Only valid for v2 SKUs.
        """
        return pulumi.get(self, "rewrite_rule_sets")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.ApplicationGatewaySku']:
        """
        A `sku` block as defined below.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="sslCertificates")
    def ssl_certificates(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewaySslCertificate']]]:
        """
        One or more `ssl_certificate` blocks as defined below.
        """
        return pulumi.get(self, "ssl_certificates")

    @property
    @pulumi.getter(name="sslPolicies")
    def ssl_policies(self) -> pulumi.Output[Sequence['outputs.ApplicationGatewaySslPolicy']]:
        """
        a `ssl policy` block as defined below.
        """
        return pulumi.get(self, "ssl_policies")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trustedRootCertificates")
    def trusted_root_certificates(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayTrustedRootCertificate']]]:
        """
        One or more `trusted_root_certificate` blocks as defined below.
        """
        return pulumi.get(self, "trusted_root_certificates")

    @property
    @pulumi.getter(name="urlPathMaps")
    def url_path_maps(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayUrlPathMap']]]:
        """
        One or more `url_path_map` blocks as defined below.
        """
        return pulumi.get(self, "url_path_maps")

    @property
    @pulumi.getter(name="wafConfiguration")
    def waf_configuration(self) -> pulumi.Output[Optional['outputs.ApplicationGatewayWafConfiguration']]:
        """
        A `waf_configuration` block as defined below.
        """
        return pulumi.get(self, "waf_configuration")

    @property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A collection of availability zones to spread the Application Gateway over.
        """
        return pulumi.get(self, "zones")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

