# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .asset import *
from .content_key_policy import *
from .job import *
from .service_account import *
from .streaming_endpoint import *
from .streaming_locator import *
from .streaming_policy import *
from .transform import *
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
            if typ == "azure:media/asset:Asset":
                return Asset(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:media/contentKeyPolicy:ContentKeyPolicy":
                return ContentKeyPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:media/job:Job":
                return Job(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:media/serviceAccount:ServiceAccount":
                return ServiceAccount(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:media/streamingEndpoint:StreamingEndpoint":
                return StreamingEndpoint(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:media/streamingLocator:StreamingLocator":
                return StreamingLocator(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:media/streamingPolicy:StreamingPolicy":
                return StreamingPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:media/transform:Transform":
                return Transform(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure", "media/asset", _module_instance)
    pulumi.runtime.register_resource_module("azure", "media/contentKeyPolicy", _module_instance)
    pulumi.runtime.register_resource_module("azure", "media/job", _module_instance)
    pulumi.runtime.register_resource_module("azure", "media/serviceAccount", _module_instance)
    pulumi.runtime.register_resource_module("azure", "media/streamingEndpoint", _module_instance)
    pulumi.runtime.register_resource_module("azure", "media/streamingLocator", _module_instance)
    pulumi.runtime.register_resource_module("azure", "media/streamingPolicy", _module_instance)
    pulumi.runtime.register_resource_module("azure", "media/transform", _module_instance)

_register_module()
