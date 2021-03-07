# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables
from . import outputs

__all__ = [
    'ProviderFeatures',
    'ProviderFeaturesKeyVault',
    'ProviderFeaturesLogAnalyticsWorkspace',
    'ProviderFeaturesNetwork',
    'ProviderFeaturesTemplateDeployment',
    'ProviderFeaturesVirtualMachine',
    'ProviderFeaturesVirtualMachineScaleSet',
]

@pulumi.output_type
class ProviderFeatures(dict):
    def __init__(__self__, *,
                 key_vault: Optional['outputs.ProviderFeaturesKeyVault'] = None,
                 log_analytics_workspace: Optional['outputs.ProviderFeaturesLogAnalyticsWorkspace'] = None,
                 network: Optional['outputs.ProviderFeaturesNetwork'] = None,
                 template_deployment: Optional['outputs.ProviderFeaturesTemplateDeployment'] = None,
                 virtual_machine: Optional['outputs.ProviderFeaturesVirtualMachine'] = None,
                 virtual_machine_scale_set: Optional['outputs.ProviderFeaturesVirtualMachineScaleSet'] = None):
        if key_vault is not None:
            pulumi.set(__self__, "key_vault", key_vault)
        if log_analytics_workspace is not None:
            pulumi.set(__self__, "log_analytics_workspace", log_analytics_workspace)
        if network is not None:
            pulumi.set(__self__, "network", network)
        if template_deployment is not None:
            pulumi.set(__self__, "template_deployment", template_deployment)
        if virtual_machine is not None:
            pulumi.set(__self__, "virtual_machine", virtual_machine)
        if virtual_machine_scale_set is not None:
            pulumi.set(__self__, "virtual_machine_scale_set", virtual_machine_scale_set)

    @property
    @pulumi.getter(name="keyVault")
    def key_vault(self) -> Optional['outputs.ProviderFeaturesKeyVault']:
        return pulumi.get(self, "key_vault")

    @property
    @pulumi.getter(name="logAnalyticsWorkspace")
    def log_analytics_workspace(self) -> Optional['outputs.ProviderFeaturesLogAnalyticsWorkspace']:
        return pulumi.get(self, "log_analytics_workspace")

    @property
    @pulumi.getter
    def network(self) -> Optional['outputs.ProviderFeaturesNetwork']:
        return pulumi.get(self, "network")

    @property
    @pulumi.getter(name="templateDeployment")
    def template_deployment(self) -> Optional['outputs.ProviderFeaturesTemplateDeployment']:
        return pulumi.get(self, "template_deployment")

    @property
    @pulumi.getter(name="virtualMachine")
    def virtual_machine(self) -> Optional['outputs.ProviderFeaturesVirtualMachine']:
        return pulumi.get(self, "virtual_machine")

    @property
    @pulumi.getter(name="virtualMachineScaleSet")
    def virtual_machine_scale_set(self) -> Optional['outputs.ProviderFeaturesVirtualMachineScaleSet']:
        return pulumi.get(self, "virtual_machine_scale_set")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProviderFeaturesKeyVault(dict):
    def __init__(__self__, *,
                 purge_soft_delete_on_destroy: Optional[bool] = None,
                 recover_soft_deleted_key_vaults: Optional[bool] = None):
        if purge_soft_delete_on_destroy is not None:
            pulumi.set(__self__, "purge_soft_delete_on_destroy", purge_soft_delete_on_destroy)
        if recover_soft_deleted_key_vaults is not None:
            pulumi.set(__self__, "recover_soft_deleted_key_vaults", recover_soft_deleted_key_vaults)

    @property
    @pulumi.getter(name="purgeSoftDeleteOnDestroy")
    def purge_soft_delete_on_destroy(self) -> Optional[bool]:
        return pulumi.get(self, "purge_soft_delete_on_destroy")

    @property
    @pulumi.getter(name="recoverSoftDeletedKeyVaults")
    def recover_soft_deleted_key_vaults(self) -> Optional[bool]:
        return pulumi.get(self, "recover_soft_deleted_key_vaults")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProviderFeaturesLogAnalyticsWorkspace(dict):
    def __init__(__self__, *,
                 permanently_delete_on_destroy: bool):
        pulumi.set(__self__, "permanently_delete_on_destroy", permanently_delete_on_destroy)

    @property
    @pulumi.getter(name="permanentlyDeleteOnDestroy")
    def permanently_delete_on_destroy(self) -> bool:
        return pulumi.get(self, "permanently_delete_on_destroy")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProviderFeaturesNetwork(dict):
    def __init__(__self__, *,
                 relaxed_locking: bool):
        pulumi.set(__self__, "relaxed_locking", relaxed_locking)

    @property
    @pulumi.getter(name="relaxedLocking")
    def relaxed_locking(self) -> bool:
        return pulumi.get(self, "relaxed_locking")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProviderFeaturesTemplateDeployment(dict):
    def __init__(__self__, *,
                 delete_nested_items_during_deletion: bool):
        pulumi.set(__self__, "delete_nested_items_during_deletion", delete_nested_items_during_deletion)

    @property
    @pulumi.getter(name="deleteNestedItemsDuringDeletion")
    def delete_nested_items_during_deletion(self) -> bool:
        return pulumi.get(self, "delete_nested_items_during_deletion")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProviderFeaturesVirtualMachine(dict):
    def __init__(__self__, *,
                 delete_os_disk_on_deletion: Optional[bool] = None,
                 graceful_shutdown: Optional[bool] = None):
        if delete_os_disk_on_deletion is not None:
            pulumi.set(__self__, "delete_os_disk_on_deletion", delete_os_disk_on_deletion)
        if graceful_shutdown is not None:
            pulumi.set(__self__, "graceful_shutdown", graceful_shutdown)

    @property
    @pulumi.getter(name="deleteOsDiskOnDeletion")
    def delete_os_disk_on_deletion(self) -> Optional[bool]:
        return pulumi.get(self, "delete_os_disk_on_deletion")

    @property
    @pulumi.getter(name="gracefulShutdown")
    def graceful_shutdown(self) -> Optional[bool]:
        return pulumi.get(self, "graceful_shutdown")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProviderFeaturesVirtualMachineScaleSet(dict):
    def __init__(__self__, *,
                 roll_instances_when_required: bool):
        pulumi.set(__self__, "roll_instances_when_required", roll_instances_when_required)

    @property
    @pulumi.getter(name="rollInstancesWhenRequired")
    def roll_instances_when_required(self) -> bool:
        return pulumi.get(self, "roll_instances_when_required")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


