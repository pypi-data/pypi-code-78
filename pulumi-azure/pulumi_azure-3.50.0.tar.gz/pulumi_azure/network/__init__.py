# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .application_gateway import *
from .application_security_group import *
from .bgp_connection import *
from .ddos_protection_plan import *
from .express_route_circuit import *
from .express_route_circuit_authorization import *
from .express_route_circuit_peering import *
from .express_route_gateway import *
from .firewall import *
from .firewall_application_rule_collection import *
from .firewall_nat_rule_collection import *
from .firewall_network_rule_collection import *
from .firewall_policy import *
from .firewall_policy_rule_collection_group import *
from .get_application_gateway import *
from .get_application_security_group import *
from .get_express_route_circuit import *
from .get_firewall import *
from .get_firewall_policy import *
from .get_gateway_connection import *
from .get_ip_group import *
from .get_nat_gateway import *
from .get_network_ddos_protection_plan import *
from .get_network_interface import *
from .get_network_security_group import *
from .get_network_watcher import *
from .get_public_i_ps import *
from .get_public_ip import *
from .get_public_ip_prefix import *
from .get_route_filter import *
from .get_route_table import *
from .get_service_tags import *
from .get_subnet import *
from .get_traffic_manager import *
from .get_traffic_manager_profile import *
from .get_virtual_hub import *
from .get_virtual_network import *
from .get_virtual_network_gateway import *
from .get_virtual_wan import *
from .ip_group import *
from .local_network_gateway import *
from .nat_gateway import *
from .nat_gateway_public_ip_association import *
from .network_connection_monitor import *
from .network_interface import *
from .network_interface_application_gateway_backend_address_pool_association import *
from .network_interface_application_security_group_association import *
from .network_interface_backend_address_pool_association import *
from .network_interface_nat_rule_association import *
from .network_interface_security_group_association import *
from .network_packet_capture import *
from .network_security_group import *
from .network_security_rule import *
from .network_watcher import *
from .network_watcher_flow_log import *
from .packet_capture import *
from .point_to_point_vpn_gateway import *
from .profile import *
from .public_ip import *
from .public_ip_prefix import *
from .route import *
from .route_filter import *
from .route_table import *
from .security_partner_provider import *
from .subnet import *
from .subnet_nat_gateway_association import *
from .subnet_network_security_group_association import *
from .subnet_route_table_association import *
from .subnet_service_endpoint_storage_policy import *
from .traffic_manager_endpoint import *
from .traffic_manager_profile import *
from .virtual_hub import *
from .virtual_hub_connection import *
from .virtual_hub_ip import *
from .virtual_hub_route_table import *
from .virtual_network import *
from .virtual_network_gateway import *
from .virtual_network_gateway_connection import *
from .virtual_network_peering import *
from .virtual_wan import *
from .vpn_gateway import *
from .vpn_gateway_connection import *
from .vpn_server_configuration import *
from .vpn_site import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "azure:network/applicationGateway:ApplicationGateway":
                return ApplicationGateway(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/applicationSecurityGroup:ApplicationSecurityGroup":
                return ApplicationSecurityGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/bgpConnection:BgpConnection":
                return BgpConnection(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/ddosProtectionPlan:DdosProtectionPlan":
                return DdosProtectionPlan(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/expressRouteCircuit:ExpressRouteCircuit":
                return ExpressRouteCircuit(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/expressRouteCircuitAuthorization:ExpressRouteCircuitAuthorization":
                return ExpressRouteCircuitAuthorization(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/expressRouteCircuitPeering:ExpressRouteCircuitPeering":
                return ExpressRouteCircuitPeering(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/expressRouteGateway:ExpressRouteGateway":
                return ExpressRouteGateway(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/firewall:Firewall":
                return Firewall(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/firewallApplicationRuleCollection:FirewallApplicationRuleCollection":
                return FirewallApplicationRuleCollection(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/firewallNatRuleCollection:FirewallNatRuleCollection":
                return FirewallNatRuleCollection(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/firewallNetworkRuleCollection:FirewallNetworkRuleCollection":
                return FirewallNetworkRuleCollection(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/firewallPolicy:FirewallPolicy":
                return FirewallPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/firewallPolicyRuleCollectionGroup:FirewallPolicyRuleCollectionGroup":
                return FirewallPolicyRuleCollectionGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/iPGroup:IPGroup":
                return IPGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/localNetworkGateway:LocalNetworkGateway":
                return LocalNetworkGateway(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/natGateway:NatGateway":
                return NatGateway(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/natGatewayPublicIpAssociation:NatGatewayPublicIpAssociation":
                return NatGatewayPublicIpAssociation(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/networkConnectionMonitor:NetworkConnectionMonitor":
                return NetworkConnectionMonitor(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/networkInterface:NetworkInterface":
                return NetworkInterface(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/networkInterfaceApplicationGatewayBackendAddressPoolAssociation:NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation":
                return NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/networkInterfaceApplicationSecurityGroupAssociation:NetworkInterfaceApplicationSecurityGroupAssociation":
                return NetworkInterfaceApplicationSecurityGroupAssociation(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/networkInterfaceBackendAddressPoolAssociation:NetworkInterfaceBackendAddressPoolAssociation":
                return NetworkInterfaceBackendAddressPoolAssociation(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/networkInterfaceNatRuleAssociation:NetworkInterfaceNatRuleAssociation":
                return NetworkInterfaceNatRuleAssociation(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/networkInterfaceSecurityGroupAssociation:NetworkInterfaceSecurityGroupAssociation":
                return NetworkInterfaceSecurityGroupAssociation(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/networkPacketCapture:NetworkPacketCapture":
                return NetworkPacketCapture(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/networkSecurityGroup:NetworkSecurityGroup":
                return NetworkSecurityGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/networkSecurityRule:NetworkSecurityRule":
                return NetworkSecurityRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/networkWatcher:NetworkWatcher":
                return NetworkWatcher(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/networkWatcherFlowLog:NetworkWatcherFlowLog":
                return NetworkWatcherFlowLog(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/packetCapture:PacketCapture":
                return PacketCapture(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/pointToPointVpnGateway:PointToPointVpnGateway":
                return PointToPointVpnGateway(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/profile:Profile":
                return Profile(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/publicIp:PublicIp":
                return PublicIp(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/publicIpPrefix:PublicIpPrefix":
                return PublicIpPrefix(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/route:Route":
                return Route(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/routeFilter:RouteFilter":
                return RouteFilter(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/routeTable:RouteTable":
                return RouteTable(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/securityPartnerProvider:SecurityPartnerProvider":
                return SecurityPartnerProvider(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/subnet:Subnet":
                return Subnet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/subnetNatGatewayAssociation:SubnetNatGatewayAssociation":
                return SubnetNatGatewayAssociation(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/subnetNetworkSecurityGroupAssociation:SubnetNetworkSecurityGroupAssociation":
                return SubnetNetworkSecurityGroupAssociation(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/subnetRouteTableAssociation:SubnetRouteTableAssociation":
                return SubnetRouteTableAssociation(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/subnetServiceEndpointStoragePolicy:SubnetServiceEndpointStoragePolicy":
                return SubnetServiceEndpointStoragePolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/trafficManagerEndpoint:TrafficManagerEndpoint":
                return TrafficManagerEndpoint(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/trafficManagerProfile:TrafficManagerProfile":
                return TrafficManagerProfile(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/virtualHub:VirtualHub":
                return VirtualHub(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/virtualHubConnection:VirtualHubConnection":
                return VirtualHubConnection(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/virtualHubIp:VirtualHubIp":
                return VirtualHubIp(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/virtualHubRouteTable:VirtualHubRouteTable":
                return VirtualHubRouteTable(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/virtualNetwork:VirtualNetwork":
                return VirtualNetwork(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/virtualNetworkGateway:VirtualNetworkGateway":
                return VirtualNetworkGateway(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/virtualNetworkGatewayConnection:VirtualNetworkGatewayConnection":
                return VirtualNetworkGatewayConnection(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/virtualNetworkPeering:VirtualNetworkPeering":
                return VirtualNetworkPeering(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/virtualWan:VirtualWan":
                return VirtualWan(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/vpnGateway:VpnGateway":
                return VpnGateway(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/vpnGatewayConnection:VpnGatewayConnection":
                return VpnGatewayConnection(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/vpnServerConfiguration:VpnServerConfiguration":
                return VpnServerConfiguration(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:network/vpnSite:VpnSite":
                return VpnSite(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure", "network/applicationGateway", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/applicationSecurityGroup", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/bgpConnection", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/ddosProtectionPlan", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/expressRouteCircuit", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/expressRouteCircuitAuthorization", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/expressRouteCircuitPeering", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/expressRouteGateway", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/firewall", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/firewallApplicationRuleCollection", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/firewallNatRuleCollection", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/firewallNetworkRuleCollection", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/firewallPolicy", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/firewallPolicyRuleCollectionGroup", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/iPGroup", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/localNetworkGateway", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/natGateway", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/natGatewayPublicIpAssociation", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/networkConnectionMonitor", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/networkInterface", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/networkInterfaceApplicationGatewayBackendAddressPoolAssociation", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/networkInterfaceApplicationSecurityGroupAssociation", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/networkInterfaceBackendAddressPoolAssociation", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/networkInterfaceNatRuleAssociation", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/networkInterfaceSecurityGroupAssociation", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/networkPacketCapture", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/networkSecurityGroup", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/networkSecurityRule", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/networkWatcher", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/networkWatcherFlowLog", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/packetCapture", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/pointToPointVpnGateway", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/profile", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/publicIp", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/publicIpPrefix", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/route", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/routeFilter", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/routeTable", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/securityPartnerProvider", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/subnet", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/subnetNatGatewayAssociation", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/subnetNetworkSecurityGroupAssociation", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/subnetRouteTableAssociation", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/subnetServiceEndpointStoragePolicy", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/trafficManagerEndpoint", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/trafficManagerProfile", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/virtualHub", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/virtualHubConnection", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/virtualHubIp", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/virtualHubRouteTable", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/virtualNetwork", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/virtualNetworkGateway", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/virtualNetworkGatewayConnection", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/virtualNetworkPeering", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/virtualWan", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/vpnGateway", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/vpnGatewayConnection", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/vpnServerConfiguration", _module_instance)
    pulumi.runtime.register_resource_module("azure", "network/vpnSite", _module_instance)

_register_module()
