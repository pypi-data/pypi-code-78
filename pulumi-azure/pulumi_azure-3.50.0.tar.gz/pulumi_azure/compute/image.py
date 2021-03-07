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

__all__ = ['Image']


class Image(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_disks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ImageDataDiskArgs']]]]] = None,
                 hyper_v_generation: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 os_disk: Optional[pulumi.Input[pulumi.InputType['ImageOsDiskArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_virtual_machine_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zone_resilient: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a custom virtual machine image that can be used to create virtual machines.

        ## Example Usage
        ### Creating From VHD

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_image = azure.compute.Image("exampleImage",
            location="West US",
            resource_group_name=example_resource_group.name,
            os_disk=azure.compute.ImageOsDiskArgs(
                os_type="Linux",
                os_state="Generalized",
                blob_uri="{blob_uri}",
                size_gb=30,
            ))
        ```
        ### Creating From Virtual Machine (VM Must Be Generalized Beforehand)

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_image = azure.compute.Image("exampleImage",
            location="West US",
            resource_group_name=example_resource_group.name,
            source_virtual_machine_id="{vm_id}")
        ```

        ## Import

        Images can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:compute/image:Image example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/microsoft.compute/images/image1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ImageDataDiskArgs']]]] data_disks: One or more `data_disk` elements as defined below.
        :param pulumi.Input[str] hyper_v_generation: The HyperVGenerationType of the VirtualMachine created from the image as `V1`, `V2`. The default is `V1`.
        :param pulumi.Input[str] location: Specified the supported Azure location where the resource exists.
               Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the image. Changing this forces a
               new resource to be created.
        :param pulumi.Input[pulumi.InputType['ImageOsDiskArgs']] os_disk: One or more `os_disk` elements as defined below.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create
               the image. Changing this forces a new resource to be created.
        :param pulumi.Input[str] source_virtual_machine_id: The Virtual Machine ID from which to create the image.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[bool] zone_resilient: Is zone resiliency enabled?  Defaults to `false`.  Changing this forces a new resource to be created.
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

            __props__['data_disks'] = data_disks
            __props__['hyper_v_generation'] = hyper_v_generation
            __props__['location'] = location
            __props__['name'] = name
            __props__['os_disk'] = os_disk
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['source_virtual_machine_id'] = source_virtual_machine_id
            __props__['tags'] = tags
            __props__['zone_resilient'] = zone_resilient
        super(Image, __self__).__init__(
            'azure:compute/image:Image',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            data_disks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ImageDataDiskArgs']]]]] = None,
            hyper_v_generation: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            os_disk: Optional[pulumi.Input[pulumi.InputType['ImageOsDiskArgs']]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            source_virtual_machine_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            zone_resilient: Optional[pulumi.Input[bool]] = None) -> 'Image':
        """
        Get an existing Image resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ImageDataDiskArgs']]]] data_disks: One or more `data_disk` elements as defined below.
        :param pulumi.Input[str] hyper_v_generation: The HyperVGenerationType of the VirtualMachine created from the image as `V1`, `V2`. The default is `V1`.
        :param pulumi.Input[str] location: Specified the supported Azure location where the resource exists.
               Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the image. Changing this forces a
               new resource to be created.
        :param pulumi.Input[pulumi.InputType['ImageOsDiskArgs']] os_disk: One or more `os_disk` elements as defined below.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create
               the image. Changing this forces a new resource to be created.
        :param pulumi.Input[str] source_virtual_machine_id: The Virtual Machine ID from which to create the image.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[bool] zone_resilient: Is zone resiliency enabled?  Defaults to `false`.  Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["data_disks"] = data_disks
        __props__["hyper_v_generation"] = hyper_v_generation
        __props__["location"] = location
        __props__["name"] = name
        __props__["os_disk"] = os_disk
        __props__["resource_group_name"] = resource_group_name
        __props__["source_virtual_machine_id"] = source_virtual_machine_id
        __props__["tags"] = tags
        __props__["zone_resilient"] = zone_resilient
        return Image(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dataDisks")
    def data_disks(self) -> pulumi.Output[Optional[Sequence['outputs.ImageDataDisk']]]:
        """
        One or more `data_disk` elements as defined below.
        """
        return pulumi.get(self, "data_disks")

    @property
    @pulumi.getter(name="hyperVGeneration")
    def hyper_v_generation(self) -> pulumi.Output[Optional[str]]:
        """
        The HyperVGenerationType of the VirtualMachine created from the image as `V1`, `V2`. The default is `V1`.
        """
        return pulumi.get(self, "hyper_v_generation")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specified the supported Azure location where the resource exists.
        Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the image. Changing this forces a
        new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="osDisk")
    def os_disk(self) -> pulumi.Output[Optional['outputs.ImageOsDisk']]:
        """
        One or more `os_disk` elements as defined below.
        """
        return pulumi.get(self, "os_disk")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to create
        the image. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="sourceVirtualMachineId")
    def source_virtual_machine_id(self) -> pulumi.Output[Optional[str]]:
        """
        The Virtual Machine ID from which to create the image.
        """
        return pulumi.get(self, "source_virtual_machine_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="zoneResilient")
    def zone_resilient(self) -> pulumi.Output[Optional[bool]]:
        """
        Is zone resiliency enabled?  Defaults to `false`.  Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone_resilient")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

