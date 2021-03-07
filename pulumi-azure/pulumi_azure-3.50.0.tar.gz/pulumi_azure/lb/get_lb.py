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
    'GetLBResult',
    'AwaitableGetLBResult',
    'get_lb',
]

@pulumi.output_type
class GetLBResult:
    """
    A collection of values returned by getLB.
    """
    def __init__(__self__, frontend_ip_configurations=None, id=None, location=None, name=None, private_ip_address=None, private_ip_addresses=None, resource_group_name=None, sku=None, tags=None):
        if frontend_ip_configurations and not isinstance(frontend_ip_configurations, list):
            raise TypeError("Expected argument 'frontend_ip_configurations' to be a list")
        pulumi.set(__self__, "frontend_ip_configurations", frontend_ip_configurations)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_ip_address and not isinstance(private_ip_address, str):
            raise TypeError("Expected argument 'private_ip_address' to be a str")
        pulumi.set(__self__, "private_ip_address", private_ip_address)
        if private_ip_addresses and not isinstance(private_ip_addresses, list):
            raise TypeError("Expected argument 'private_ip_addresses' to be a list")
        pulumi.set(__self__, "private_ip_addresses", private_ip_addresses)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if sku and not isinstance(sku, str):
            raise TypeError("Expected argument 'sku' to be a str")
        pulumi.set(__self__, "sku", sku)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="frontendIpConfigurations")
    def frontend_ip_configurations(self) -> Sequence['outputs.GetLBFrontendIpConfigurationResult']:
        """
        A `frontend_ip_configuration` block as documented below.
        """
        return pulumi.get(self, "frontend_ip_configurations")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The Azure location where the Load Balancer exists.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the Frontend IP Configuration.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> str:
        """
        Private IP Address to assign to the Load Balancer.
        """
        return pulumi.get(self, "private_ip_address")

    @property
    @pulumi.getter(name="privateIpAddresses")
    def private_ip_addresses(self) -> Sequence[str]:
        """
        The list of private IP address assigned to the load balancer in `frontend_ip_configuration` blocks, if any.
        """
        return pulumi.get(self, "private_ip_addresses")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def sku(self) -> str:
        """
        The SKU of the Load Balancer.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags assigned to the resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetLBResult(GetLBResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLBResult(
            frontend_ip_configurations=self.frontend_ip_configurations,
            id=self.id,
            location=self.location,
            name=self.name,
            private_ip_address=self.private_ip_address,
            private_ip_addresses=self.private_ip_addresses,
            resource_group_name=self.resource_group_name,
            sku=self.sku,
            tags=self.tags)


def get_lb(name: Optional[str] = None,
           resource_group_name: Optional[str] = None,
           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLBResult:
    """
    Use this data source to access information about an existing Load Balancer

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.lb.get_lb(name="example-lb",
        resource_group_name="example-resources")
    pulumi.export("loadbalancerId", example.id)
    ```


    :param str name: Specifies the name of the Load Balancer.
    :param str resource_group_name: The name of the Resource Group in which the Load Balancer exists.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:lb/getLB:getLB', __args__, opts=opts, typ=GetLBResult).value

    return AwaitableGetLBResult(
        frontend_ip_configurations=__ret__.frontend_ip_configurations,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        private_ip_address=__ret__.private_ip_address,
        private_ip_addresses=__ret__.private_ip_addresses,
        resource_group_name=__ret__.resource_group_name,
        sku=__ret__.sku,
        tags=__ret__.tags)
