# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .channel_direct_line import *
from .channel_email import *
from .channel_slack import *
from .channel_teams import *
from .channels_registration import *
from .connection import *
from .web_app import *
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
            if typ == "azure:bot/channelDirectLine:ChannelDirectLine":
                return ChannelDirectLine(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:bot/channelEmail:ChannelEmail":
                return ChannelEmail(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:bot/channelSlack:ChannelSlack":
                return ChannelSlack(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:bot/channelTeams:ChannelTeams":
                return ChannelTeams(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:bot/channelsRegistration:ChannelsRegistration":
                return ChannelsRegistration(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:bot/connection:Connection":
                return Connection(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:bot/webApp:WebApp":
                return WebApp(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure", "bot/channelDirectLine", _module_instance)
    pulumi.runtime.register_resource_module("azure", "bot/channelEmail", _module_instance)
    pulumi.runtime.register_resource_module("azure", "bot/channelSlack", _module_instance)
    pulumi.runtime.register_resource_module("azure", "bot/channelTeams", _module_instance)
    pulumi.runtime.register_resource_module("azure", "bot/channelsRegistration", _module_instance)
    pulumi.runtime.register_resource_module("azure", "bot/connection", _module_instance)
    pulumi.runtime.register_resource_module("azure", "bot/webApp", _module_instance)

_register_module()
