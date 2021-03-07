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

__all__ = ['Service']


class Service(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_locations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceAdditionalLocationArgs']]]]] = None,
                 certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceCertificateArgs']]]]] = None,
                 hostname_configuration: Optional[pulumi.Input[pulumi.InputType['ServiceHostnameConfigurationArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ServiceIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_sender_email: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[pulumi.InputType['ServicePolicyArgs']]] = None,
                 protocols: Optional[pulumi.Input[pulumi.InputType['ServiceProtocolsArgs']]] = None,
                 publisher_email: Optional[pulumi.Input[str]] = None,
                 publisher_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 security: Optional[pulumi.Input[pulumi.InputType['ServiceSecurityArgs']]] = None,
                 sign_in: Optional[pulumi.Input[pulumi.InputType['ServiceSignInArgs']]] = None,
                 sign_up: Optional[pulumi.Input[pulumi.InputType['ServiceSignUpArgs']]] = None,
                 sku_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tenant_access: Optional[pulumi.Input[pulumi.InputType['ServiceTenantAccessArgs']]] = None,
                 virtual_network_configuration: Optional[pulumi.Input[pulumi.InputType['ServiceVirtualNetworkConfigurationArgs']]] = None,
                 virtual_network_type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an API Management Service.

        ## Disclaimers

        > **Note:** It's possible to define Custom Domains both within the `apimanagement.Service` resource via the `hostname_configurations` block and by using the `apimanagement.CustomDomain` resource. However it's not possible to use both methods to manage Custom Domains within an API Management Service, since there'll be conflicts.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_service = azure.apimanagement.Service("exampleService",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            publisher_name="My Company",
            publisher_email="company@exmaple.com",
            sku_name="Developer_1",
            policy=azure.apimanagement.ServicePolicyArgs(
                xml_content=\"\"\"    <policies>
              <inbound />
              <backend />
              <outbound />
              <on-error />
            </policies>
        \"\"\",
            ))
        ```

        ## Import

        API Management Services can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:apimanagement/service:Service example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.ApiManagement/service/instance1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceAdditionalLocationArgs']]]] additional_locations: One or more `additional_location` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceCertificateArgs']]]] certificates: One or more (up to 10) `certificate` blocks as defined below.
        :param pulumi.Input[pulumi.InputType['ServiceHostnameConfigurationArgs']] hostname_configuration: A `hostname_configuration` block as defined below.
        :param pulumi.Input[pulumi.InputType['ServiceIdentityArgs']] identity: An `identity` block is documented below.
        :param pulumi.Input[str] location: The Azure location where the API Management Service exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the API Management Service. Changing this forces a new resource to be created.
        :param pulumi.Input[str] notification_sender_email: Email address from which the notification will be sent.
        :param pulumi.Input[pulumi.InputType['ServicePolicyArgs']] policy: A `policy` block as defined below.
        :param pulumi.Input[pulumi.InputType['ServiceProtocolsArgs']] protocols: A `protocols` block as defined below.
        :param pulumi.Input[str] publisher_email: The email of publisher/company.
        :param pulumi.Input[str] publisher_name: The name of publisher/company.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['ServiceSecurityArgs']] security: A `security` block as defined below.
        :param pulumi.Input[pulumi.InputType['ServiceSignInArgs']] sign_in: A `sign_in` block as defined below.
        :param pulumi.Input[pulumi.InputType['ServiceSignUpArgs']] sign_up: A `sign_up` block as defined below.
        :param pulumi.Input[str] sku_name: `sku_name` is a string consisting of two parts separated by an underscore(\_). The first part is the `name`, valid values include: `Consumption`, `Developer`, `Basic`, `Standard` and `Premium`. The second part is the `capacity` (e.g. the number of deployed units of the `sku`), which must be a positive `integer` (e.g. `Developer_1`).
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags assigned to the resource.
        :param pulumi.Input[pulumi.InputType['ServiceTenantAccessArgs']] tenant_access: A `tenant_access` block as defined below.
        :param pulumi.Input[pulumi.InputType['ServiceVirtualNetworkConfigurationArgs']] virtual_network_configuration: A `virtual_network_configuration` block as defined below. Required when `virtual_network_type` is `External` or `Internal`.
        :param pulumi.Input[str] virtual_network_type: The type of virtual network you want to use, valid values include: `None`, `External`, `Internal`. 
               > **NOTE:** Please ensure that in the subnet, inbound port 3443 is open when `virtual_network_type` is `Internal` or `External`. And please ensure other necessary ports are open according to [api management network configuration](https://docs.microsoft.com/en-us/azure/api-management/api-management-using-with-vnet#-common-network-configuration-issues).
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

            __props__['additional_locations'] = additional_locations
            __props__['certificates'] = certificates
            __props__['hostname_configuration'] = hostname_configuration
            __props__['identity'] = identity
            __props__['location'] = location
            __props__['name'] = name
            __props__['notification_sender_email'] = notification_sender_email
            __props__['policy'] = policy
            __props__['protocols'] = protocols
            if publisher_email is None and not opts.urn:
                raise TypeError("Missing required property 'publisher_email'")
            __props__['publisher_email'] = publisher_email
            if publisher_name is None and not opts.urn:
                raise TypeError("Missing required property 'publisher_name'")
            __props__['publisher_name'] = publisher_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['security'] = security
            __props__['sign_in'] = sign_in
            __props__['sign_up'] = sign_up
            if sku_name is None and not opts.urn:
                raise TypeError("Missing required property 'sku_name'")
            __props__['sku_name'] = sku_name
            __props__['tags'] = tags
            __props__['tenant_access'] = tenant_access
            __props__['virtual_network_configuration'] = virtual_network_configuration
            __props__['virtual_network_type'] = virtual_network_type
            __props__['developer_portal_url'] = None
            __props__['gateway_regional_url'] = None
            __props__['gateway_url'] = None
            __props__['management_api_url'] = None
            __props__['portal_url'] = None
            __props__['private_ip_addresses'] = None
            __props__['public_ip_addresses'] = None
            __props__['scm_url'] = None
        super(Service, __self__).__init__(
            'azure:apimanagement/service:Service',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            additional_locations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceAdditionalLocationArgs']]]]] = None,
            certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceCertificateArgs']]]]] = None,
            developer_portal_url: Optional[pulumi.Input[str]] = None,
            gateway_regional_url: Optional[pulumi.Input[str]] = None,
            gateway_url: Optional[pulumi.Input[str]] = None,
            hostname_configuration: Optional[pulumi.Input[pulumi.InputType['ServiceHostnameConfigurationArgs']]] = None,
            identity: Optional[pulumi.Input[pulumi.InputType['ServiceIdentityArgs']]] = None,
            location: Optional[pulumi.Input[str]] = None,
            management_api_url: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            notification_sender_email: Optional[pulumi.Input[str]] = None,
            policy: Optional[pulumi.Input[pulumi.InputType['ServicePolicyArgs']]] = None,
            portal_url: Optional[pulumi.Input[str]] = None,
            private_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            protocols: Optional[pulumi.Input[pulumi.InputType['ServiceProtocolsArgs']]] = None,
            public_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            publisher_email: Optional[pulumi.Input[str]] = None,
            publisher_name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            scm_url: Optional[pulumi.Input[str]] = None,
            security: Optional[pulumi.Input[pulumi.InputType['ServiceSecurityArgs']]] = None,
            sign_in: Optional[pulumi.Input[pulumi.InputType['ServiceSignInArgs']]] = None,
            sign_up: Optional[pulumi.Input[pulumi.InputType['ServiceSignUpArgs']]] = None,
            sku_name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tenant_access: Optional[pulumi.Input[pulumi.InputType['ServiceTenantAccessArgs']]] = None,
            virtual_network_configuration: Optional[pulumi.Input[pulumi.InputType['ServiceVirtualNetworkConfigurationArgs']]] = None,
            virtual_network_type: Optional[pulumi.Input[str]] = None) -> 'Service':
        """
        Get an existing Service resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceAdditionalLocationArgs']]]] additional_locations: One or more `additional_location` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceCertificateArgs']]]] certificates: One or more (up to 10) `certificate` blocks as defined below.
        :param pulumi.Input[str] developer_portal_url: The URL for the Developer Portal associated with this API Management service.
        :param pulumi.Input[str] gateway_regional_url: The URL of the Regional Gateway for the API Management Service in the specified region.
        :param pulumi.Input[str] gateway_url: The URL of the Gateway for the API Management Service.
        :param pulumi.Input[pulumi.InputType['ServiceHostnameConfigurationArgs']] hostname_configuration: A `hostname_configuration` block as defined below.
        :param pulumi.Input[pulumi.InputType['ServiceIdentityArgs']] identity: An `identity` block is documented below.
        :param pulumi.Input[str] location: The Azure location where the API Management Service exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] management_api_url: The URL for the Management API associated with this API Management service.
        :param pulumi.Input[str] name: The name of the API Management Service. Changing this forces a new resource to be created.
        :param pulumi.Input[str] notification_sender_email: Email address from which the notification will be sent.
        :param pulumi.Input[pulumi.InputType['ServicePolicyArgs']] policy: A `policy` block as defined below.
        :param pulumi.Input[str] portal_url: The URL for the Publisher Portal associated with this API Management service.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] private_ip_addresses: The Private IP addresses of the API Management Service.  Available only when the API Manager instance is using Virtual Network mode.
        :param pulumi.Input[pulumi.InputType['ServiceProtocolsArgs']] protocols: A `protocols` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] public_ip_addresses: Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.
        :param pulumi.Input[str] publisher_email: The email of publisher/company.
        :param pulumi.Input[str] publisher_name: The name of publisher/company.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] scm_url: The URL for the SCM (Source Code Management) Endpoint associated with this API Management service.
        :param pulumi.Input[pulumi.InputType['ServiceSecurityArgs']] security: A `security` block as defined below.
        :param pulumi.Input[pulumi.InputType['ServiceSignInArgs']] sign_in: A `sign_in` block as defined below.
        :param pulumi.Input[pulumi.InputType['ServiceSignUpArgs']] sign_up: A `sign_up` block as defined below.
        :param pulumi.Input[str] sku_name: `sku_name` is a string consisting of two parts separated by an underscore(\_). The first part is the `name`, valid values include: `Consumption`, `Developer`, `Basic`, `Standard` and `Premium`. The second part is the `capacity` (e.g. the number of deployed units of the `sku`), which must be a positive `integer` (e.g. `Developer_1`).
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags assigned to the resource.
        :param pulumi.Input[pulumi.InputType['ServiceTenantAccessArgs']] tenant_access: A `tenant_access` block as defined below.
        :param pulumi.Input[pulumi.InputType['ServiceVirtualNetworkConfigurationArgs']] virtual_network_configuration: A `virtual_network_configuration` block as defined below. Required when `virtual_network_type` is `External` or `Internal`.
        :param pulumi.Input[str] virtual_network_type: The type of virtual network you want to use, valid values include: `None`, `External`, `Internal`. 
               > **NOTE:** Please ensure that in the subnet, inbound port 3443 is open when `virtual_network_type` is `Internal` or `External`. And please ensure other necessary ports are open according to [api management network configuration](https://docs.microsoft.com/en-us/azure/api-management/api-management-using-with-vnet#-common-network-configuration-issues).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["additional_locations"] = additional_locations
        __props__["certificates"] = certificates
        __props__["developer_portal_url"] = developer_portal_url
        __props__["gateway_regional_url"] = gateway_regional_url
        __props__["gateway_url"] = gateway_url
        __props__["hostname_configuration"] = hostname_configuration
        __props__["identity"] = identity
        __props__["location"] = location
        __props__["management_api_url"] = management_api_url
        __props__["name"] = name
        __props__["notification_sender_email"] = notification_sender_email
        __props__["policy"] = policy
        __props__["portal_url"] = portal_url
        __props__["private_ip_addresses"] = private_ip_addresses
        __props__["protocols"] = protocols
        __props__["public_ip_addresses"] = public_ip_addresses
        __props__["publisher_email"] = publisher_email
        __props__["publisher_name"] = publisher_name
        __props__["resource_group_name"] = resource_group_name
        __props__["scm_url"] = scm_url
        __props__["security"] = security
        __props__["sign_in"] = sign_in
        __props__["sign_up"] = sign_up
        __props__["sku_name"] = sku_name
        __props__["tags"] = tags
        __props__["tenant_access"] = tenant_access
        __props__["virtual_network_configuration"] = virtual_network_configuration
        __props__["virtual_network_type"] = virtual_network_type
        return Service(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalLocations")
    def additional_locations(self) -> pulumi.Output[Optional[Sequence['outputs.ServiceAdditionalLocation']]]:
        """
        One or more `additional_location` blocks as defined below.
        """
        return pulumi.get(self, "additional_locations")

    @property
    @pulumi.getter
    def certificates(self) -> pulumi.Output[Optional[Sequence['outputs.ServiceCertificate']]]:
        """
        One or more (up to 10) `certificate` blocks as defined below.
        """
        return pulumi.get(self, "certificates")

    @property
    @pulumi.getter(name="developerPortalUrl")
    def developer_portal_url(self) -> pulumi.Output[str]:
        """
        The URL for the Developer Portal associated with this API Management service.
        """
        return pulumi.get(self, "developer_portal_url")

    @property
    @pulumi.getter(name="gatewayRegionalUrl")
    def gateway_regional_url(self) -> pulumi.Output[str]:
        """
        The URL of the Regional Gateway for the API Management Service in the specified region.
        """
        return pulumi.get(self, "gateway_regional_url")

    @property
    @pulumi.getter(name="gatewayUrl")
    def gateway_url(self) -> pulumi.Output[str]:
        """
        The URL of the Gateway for the API Management Service.
        """
        return pulumi.get(self, "gateway_url")

    @property
    @pulumi.getter(name="hostnameConfiguration")
    def hostname_configuration(self) -> pulumi.Output[Optional['outputs.ServiceHostnameConfiguration']]:
        """
        A `hostname_configuration` block as defined below.
        """
        return pulumi.get(self, "hostname_configuration")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ServiceIdentity']]:
        """
        An `identity` block is documented below.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The Azure location where the API Management Service exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managementApiUrl")
    def management_api_url(self) -> pulumi.Output[str]:
        """
        The URL for the Management API associated with this API Management service.
        """
        return pulumi.get(self, "management_api_url")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the API Management Service. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notificationSenderEmail")
    def notification_sender_email(self) -> pulumi.Output[str]:
        """
        Email address from which the notification will be sent.
        """
        return pulumi.get(self, "notification_sender_email")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output['outputs.ServicePolicy']:
        """
        A `policy` block as defined below.
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter(name="portalUrl")
    def portal_url(self) -> pulumi.Output[str]:
        """
        The URL for the Publisher Portal associated with this API Management service.
        """
        return pulumi.get(self, "portal_url")

    @property
    @pulumi.getter(name="privateIpAddresses")
    def private_ip_addresses(self) -> pulumi.Output[Sequence[str]]:
        """
        The Private IP addresses of the API Management Service.  Available only when the API Manager instance is using Virtual Network mode.
        """
        return pulumi.get(self, "private_ip_addresses")

    @property
    @pulumi.getter
    def protocols(self) -> pulumi.Output['outputs.ServiceProtocols']:
        """
        A `protocols` block as defined below.
        """
        return pulumi.get(self, "protocols")

    @property
    @pulumi.getter(name="publicIpAddresses")
    def public_ip_addresses(self) -> pulumi.Output[Sequence[str]]:
        """
        Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.
        """
        return pulumi.get(self, "public_ip_addresses")

    @property
    @pulumi.getter(name="publisherEmail")
    def publisher_email(self) -> pulumi.Output[str]:
        """
        The email of publisher/company.
        """
        return pulumi.get(self, "publisher_email")

    @property
    @pulumi.getter(name="publisherName")
    def publisher_name(self) -> pulumi.Output[str]:
        """
        The name of publisher/company.
        """
        return pulumi.get(self, "publisher_name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="scmUrl")
    def scm_url(self) -> pulumi.Output[str]:
        """
        The URL for the SCM (Source Code Management) Endpoint associated with this API Management service.
        """
        return pulumi.get(self, "scm_url")

    @property
    @pulumi.getter
    def security(self) -> pulumi.Output['outputs.ServiceSecurity']:
        """
        A `security` block as defined below.
        """
        return pulumi.get(self, "security")

    @property
    @pulumi.getter(name="signIn")
    def sign_in(self) -> pulumi.Output['outputs.ServiceSignIn']:
        """
        A `sign_in` block as defined below.
        """
        return pulumi.get(self, "sign_in")

    @property
    @pulumi.getter(name="signUp")
    def sign_up(self) -> pulumi.Output['outputs.ServiceSignUp']:
        """
        A `sign_up` block as defined below.
        """
        return pulumi.get(self, "sign_up")

    @property
    @pulumi.getter(name="skuName")
    def sku_name(self) -> pulumi.Output[str]:
        """
        `sku_name` is a string consisting of two parts separated by an underscore(\_). The first part is the `name`, valid values include: `Consumption`, `Developer`, `Basic`, `Standard` and `Premium`. The second part is the `capacity` (e.g. the number of deployed units of the `sku`), which must be a positive `integer` (e.g. `Developer_1`).
        """
        return pulumi.get(self, "sku_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags assigned to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tenantAccess")
    def tenant_access(self) -> pulumi.Output['outputs.ServiceTenantAccess']:
        """
        A `tenant_access` block as defined below.
        """
        return pulumi.get(self, "tenant_access")

    @property
    @pulumi.getter(name="virtualNetworkConfiguration")
    def virtual_network_configuration(self) -> pulumi.Output[Optional['outputs.ServiceVirtualNetworkConfiguration']]:
        """
        A `virtual_network_configuration` block as defined below. Required when `virtual_network_type` is `External` or `Internal`.
        """
        return pulumi.get(self, "virtual_network_configuration")

    @property
    @pulumi.getter(name="virtualNetworkType")
    def virtual_network_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of virtual network you want to use, valid values include: `None`, `External`, `Internal`. 
        > **NOTE:** Please ensure that in the subnet, inbound port 3443 is open when `virtual_network_type` is `Internal` or `External`. And please ensure other necessary ports are open according to [api management network configuration](https://docs.microsoft.com/en-us/azure/api-management/api-management-using-with-vnet#-common-network-configuration-issues).
        """
        return pulumi.get(self, "virtual_network_type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

