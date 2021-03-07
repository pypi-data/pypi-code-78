# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'GetNetworkInterfaceResult',
    'AwaitableGetNetworkInterfaceResult',
    'get_network_interface',
]

@pulumi.output_type
class GetNetworkInterfaceResult:
    """
    A collection of values returned by getNetworkInterface.
    """
    def __init__(__self__, applied_dns_servers=None, dns_servers=None, enable_accelerated_networking=None, enable_ip_forwarding=None, id=None, internal_dns_name_label=None, ip_configurations=None, location=None, mac_address=None, name=None, network_security_group_id=None, private_ip_address=None, private_ip_addresses=None, resource_group_name=None, tags=None, virtual_machine_id=None):
        if applied_dns_servers and not isinstance(applied_dns_servers, list):
            raise TypeError("Expected argument 'applied_dns_servers' to be a list")
        pulumi.set(__self__, "applied_dns_servers", applied_dns_servers)
        if dns_servers and not isinstance(dns_servers, list):
            raise TypeError("Expected argument 'dns_servers' to be a list")
        pulumi.set(__self__, "dns_servers", dns_servers)
        if enable_accelerated_networking and not isinstance(enable_accelerated_networking, bool):
            raise TypeError("Expected argument 'enable_accelerated_networking' to be a bool")
        pulumi.set(__self__, "enable_accelerated_networking", enable_accelerated_networking)
        if enable_ip_forwarding and not isinstance(enable_ip_forwarding, bool):
            raise TypeError("Expected argument 'enable_ip_forwarding' to be a bool")
        pulumi.set(__self__, "enable_ip_forwarding", enable_ip_forwarding)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if internal_dns_name_label and not isinstance(internal_dns_name_label, str):
            raise TypeError("Expected argument 'internal_dns_name_label' to be a str")
        pulumi.set(__self__, "internal_dns_name_label", internal_dns_name_label)
        if ip_configurations and not isinstance(ip_configurations, list):
            raise TypeError("Expected argument 'ip_configurations' to be a list")
        pulumi.set(__self__, "ip_configurations", ip_configurations)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if mac_address and not isinstance(mac_address, str):
            raise TypeError("Expected argument 'mac_address' to be a str")
        pulumi.set(__self__, "mac_address", mac_address)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_security_group_id and not isinstance(network_security_group_id, str):
            raise TypeError("Expected argument 'network_security_group_id' to be a str")
        pulumi.set(__self__, "network_security_group_id", network_security_group_id)
        if private_ip_address and not isinstance(private_ip_address, str):
            raise TypeError("Expected argument 'private_ip_address' to be a str")
        pulumi.set(__self__, "private_ip_address", private_ip_address)
        if private_ip_addresses and not isinstance(private_ip_addresses, list):
            raise TypeError("Expected argument 'private_ip_addresses' to be a list")
        pulumi.set(__self__, "private_ip_addresses", private_ip_addresses)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if virtual_machine_id and not isinstance(virtual_machine_id, str):
            raise TypeError("Expected argument 'virtual_machine_id' to be a str")
        pulumi.set(__self__, "virtual_machine_id", virtual_machine_id)

    @property
    @pulumi.getter(name="appliedDnsServers")
    def applied_dns_servers(self) -> Sequence[str]:
        """
        List of DNS servers applied to the specified Network Interface.
        """
        return pulumi.get(self, "applied_dns_servers")

    @property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Sequence[str]:
        """
        The list of DNS servers used by the specified Network Interface.
        """
        return pulumi.get(self, "dns_servers")

    @property
    @pulumi.getter(name="enableAcceleratedNetworking")
    def enable_accelerated_networking(self) -> bool:
        """
        Indicates if accelerated networking is set on the specified Network Interface.
        """
        return pulumi.get(self, "enable_accelerated_networking")

    @property
    @pulumi.getter(name="enableIpForwarding")
    def enable_ip_forwarding(self) -> bool:
        """
        Indicate if IP forwarding is set on the specified Network Interface.
        """
        return pulumi.get(self, "enable_ip_forwarding")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="internalDnsNameLabel")
    def internal_dns_name_label(self) -> str:
        """
        The internal dns name label of the specified Network Interface.
        """
        return pulumi.get(self, "internal_dns_name_label")

    @property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> Sequence['outputs.GetNetworkInterfaceIpConfigurationResult']:
        """
        One or more `ip_configuration` blocks as defined below.
        """
        return pulumi.get(self, "ip_configurations")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The location of the specified Network Interface.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> str:
        """
        The MAC address used by the specified Network Interface.
        """
        return pulumi.get(self, "mac_address")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the IP Configuration.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkSecurityGroupId")
    def network_security_group_id(self) -> str:
        """
        The ID of the network security group associated to the specified Network Interface.
        """
        return pulumi.get(self, "network_security_group_id")

    @property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> str:
        """
        The Private IP Address assigned to this Network Interface.
        """
        return pulumi.get(self, "private_ip_address")

    @property
    @pulumi.getter(name="privateIpAddresses")
    def private_ip_addresses(self) -> Sequence[str]:
        """
        The list of private ip addresses associates to the specified Network Interface.
        """
        return pulumi.get(self, "private_ip_addresses")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        List the tags associated to the specified Network Interface.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> str:
        """
        The ID of the virtual machine that the specified Network Interface is attached to.
        """
        return pulumi.get(self, "virtual_machine_id")


class AwaitableGetNetworkInterfaceResult(GetNetworkInterfaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkInterfaceResult(
            applied_dns_servers=self.applied_dns_servers,
            dns_servers=self.dns_servers,
            enable_accelerated_networking=self.enable_accelerated_networking,
            enable_ip_forwarding=self.enable_ip_forwarding,
            id=self.id,
            internal_dns_name_label=self.internal_dns_name_label,
            ip_configurations=self.ip_configurations,
            location=self.location,
            mac_address=self.mac_address,
            name=self.name,
            network_security_group_id=self.network_security_group_id,
            private_ip_address=self.private_ip_address,
            private_ip_addresses=self.private_ip_addresses,
            resource_group_name=self.resource_group_name,
            tags=self.tags,
            virtual_machine_id=self.virtual_machine_id)


def get_network_interface(name: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkInterfaceResult:
    """
    Use this data source to access information about an existing Network Interface.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.network.get_network_interface(name="acctest-nic",
        resource_group_name="networking")
    pulumi.export("networkInterfaceId", example.id)
    ```


    :param str name: Specifies the name of the Network Interface.
    :param str resource_group_name: Specifies the name of the resource group the Network Interface is located in.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:network/getNetworkInterface:getNetworkInterface', __args__, opts=opts, typ=GetNetworkInterfaceResult).value

    return AwaitableGetNetworkInterfaceResult(
        applied_dns_servers=__ret__.applied_dns_servers,
        dns_servers=__ret__.dns_servers,
        enable_accelerated_networking=__ret__.enable_accelerated_networking,
        enable_ip_forwarding=__ret__.enable_ip_forwarding,
        id=__ret__.id,
        internal_dns_name_label=__ret__.internal_dns_name_label,
        ip_configurations=__ret__.ip_configurations,
        location=__ret__.location,
        mac_address=__ret__.mac_address,
        name=__ret__.name,
        network_security_group_id=__ret__.network_security_group_id,
        private_ip_address=__ret__.private_ip_address,
        private_ip_addresses=__ret__.private_ip_addresses,
        resource_group_name=__ret__.resource_group_name,
        tags=__ret__.tags,
        virtual_machine_id=__ret__.virtual_machine_id)
