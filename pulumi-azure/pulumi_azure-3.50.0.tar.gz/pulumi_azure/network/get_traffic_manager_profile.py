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
    'GetTrafficManagerProfileResult',
    'AwaitableGetTrafficManagerProfileResult',
    'get_traffic_manager_profile',
]

@pulumi.output_type
class GetTrafficManagerProfileResult:
    """
    A collection of values returned by getTrafficManagerProfile.
    """
    def __init__(__self__, dns_configs=None, fqdn=None, id=None, monitor_configs=None, name=None, profile_status=None, resource_group_name=None, tags=None, traffic_routing_method=None, traffic_view_enabled=None):
        if dns_configs and not isinstance(dns_configs, list):
            raise TypeError("Expected argument 'dns_configs' to be a list")
        pulumi.set(__self__, "dns_configs", dns_configs)
        if fqdn and not isinstance(fqdn, str):
            raise TypeError("Expected argument 'fqdn' to be a str")
        pulumi.set(__self__, "fqdn", fqdn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if monitor_configs and not isinstance(monitor_configs, list):
            raise TypeError("Expected argument 'monitor_configs' to be a list")
        pulumi.set(__self__, "monitor_configs", monitor_configs)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if profile_status and not isinstance(profile_status, str):
            raise TypeError("Expected argument 'profile_status' to be a str")
        pulumi.set(__self__, "profile_status", profile_status)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if traffic_routing_method and not isinstance(traffic_routing_method, str):
            raise TypeError("Expected argument 'traffic_routing_method' to be a str")
        pulumi.set(__self__, "traffic_routing_method", traffic_routing_method)
        if traffic_view_enabled and not isinstance(traffic_view_enabled, bool):
            raise TypeError("Expected argument 'traffic_view_enabled' to be a bool")
        pulumi.set(__self__, "traffic_view_enabled", traffic_view_enabled)

    @property
    @pulumi.getter(name="dnsConfigs")
    def dns_configs(self) -> Sequence['outputs.GetTrafficManagerProfileDnsConfigResult']:
        """
        This block specifies the DNS configuration of the Profile.
        """
        return pulumi.get(self, "dns_configs")

    @property
    @pulumi.getter
    def fqdn(self) -> str:
        """
        The FQDN of the created Profile.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="monitorConfigs")
    def monitor_configs(self) -> Sequence['outputs.GetTrafficManagerProfileMonitorConfigResult']:
        """
        This block specifies the Endpoint monitoring configuration for the Profile.
        """
        return pulumi.get(self, "monitor_configs")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the custom header.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="profileStatus")
    def profile_status(self) -> str:
        """
        The status of the profile.
        """
        return pulumi.get(self, "profile_status")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trafficRoutingMethod")
    def traffic_routing_method(self) -> str:
        """
        Specifies the algorithm used to route traffic.
        """
        return pulumi.get(self, "traffic_routing_method")

    @property
    @pulumi.getter(name="trafficViewEnabled")
    def traffic_view_enabled(self) -> Optional[bool]:
        """
        Indicates whether Traffic View is enabled for the Traffic Manager profile.
        """
        return pulumi.get(self, "traffic_view_enabled")


class AwaitableGetTrafficManagerProfileResult(GetTrafficManagerProfileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTrafficManagerProfileResult(
            dns_configs=self.dns_configs,
            fqdn=self.fqdn,
            id=self.id,
            monitor_configs=self.monitor_configs,
            name=self.name,
            profile_status=self.profile_status,
            resource_group_name=self.resource_group_name,
            tags=self.tags,
            traffic_routing_method=self.traffic_routing_method,
            traffic_view_enabled=self.traffic_view_enabled)


def get_traffic_manager_profile(name: Optional[str] = None,
                                resource_group_name: Optional[str] = None,
                                tags: Optional[Mapping[str, str]] = None,
                                traffic_view_enabled: Optional[bool] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTrafficManagerProfileResult:
    """
    Use this data source to access information about an existing Traffic Manager Profile.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.network.get_traffic_manager_profile(name="test",
        resource_group_name="test")
    pulumi.export("trafficRoutingMethod", data["azurerm_traffic_manager_profile"]["traffic_routing_method"])
    ```


    :param str name: Specifies the name of the Traffic Manager Profile.
    :param str resource_group_name: Specifies the name of the resource group the Traffic Manager Profile is located in.
    :param Mapping[str, str] tags: A mapping of tags to assign to the resource.
    :param bool traffic_view_enabled: Indicates whether Traffic View is enabled for the Traffic Manager profile.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['tags'] = tags
    __args__['trafficViewEnabled'] = traffic_view_enabled
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:network/getTrafficManagerProfile:getTrafficManagerProfile', __args__, opts=opts, typ=GetTrafficManagerProfileResult).value

    return AwaitableGetTrafficManagerProfileResult(
        dns_configs=__ret__.dns_configs,
        fqdn=__ret__.fqdn,
        id=__ret__.id,
        monitor_configs=__ret__.monitor_configs,
        name=__ret__.name,
        profile_status=__ret__.profile_status,
        resource_group_name=__ret__.resource_group_name,
        tags=__ret__.tags,
        traffic_routing_method=__ret__.traffic_routing_method,
        traffic_view_enabled=__ret__.traffic_view_enabled)
