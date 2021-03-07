# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = [
    'ProviderFeaturesArgs',
    'ProviderFeaturesKeyVaultArgs',
    'ProviderFeaturesLogAnalyticsWorkspaceArgs',
    'ProviderFeaturesNetworkArgs',
    'ProviderFeaturesTemplateDeploymentArgs',
    'ProviderFeaturesVirtualMachineArgs',
    'ProviderFeaturesVirtualMachineScaleSetArgs',
]

@pulumi.input_type
class ProviderFeaturesArgs:
    def __init__(__self__, *,
                 key_vault: Optional[pulumi.Input['ProviderFeaturesKeyVaultArgs']] = None,
                 log_analytics_workspace: Optional[pulumi.Input['ProviderFeaturesLogAnalyticsWorkspaceArgs']] = None,
                 network: Optional[pulumi.Input['ProviderFeaturesNetworkArgs']] = None,
                 template_deployment: Optional[pulumi.Input['ProviderFeaturesTemplateDeploymentArgs']] = None,
                 virtual_machine: Optional[pulumi.Input['ProviderFeaturesVirtualMachineArgs']] = None,
                 virtual_machine_scale_set: Optional[pulumi.Input['ProviderFeaturesVirtualMachineScaleSetArgs']] = None):
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
    def key_vault(self) -> Optional[pulumi.Input['ProviderFeaturesKeyVaultArgs']]:
        return pulumi.get(self, "key_vault")

    @key_vault.setter
    def key_vault(self, value: Optional[pulumi.Input['ProviderFeaturesKeyVaultArgs']]):
        pulumi.set(self, "key_vault", value)

    @property
    @pulumi.getter(name="logAnalyticsWorkspace")
    def log_analytics_workspace(self) -> Optional[pulumi.Input['ProviderFeaturesLogAnalyticsWorkspaceArgs']]:
        return pulumi.get(self, "log_analytics_workspace")

    @log_analytics_workspace.setter
    def log_analytics_workspace(self, value: Optional[pulumi.Input['ProviderFeaturesLogAnalyticsWorkspaceArgs']]):
        pulumi.set(self, "log_analytics_workspace", value)

    @property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input['ProviderFeaturesNetworkArgs']]:
        return pulumi.get(self, "network")

    @network.setter
    def network(self, value: Optional[pulumi.Input['ProviderFeaturesNetworkArgs']]):
        pulumi.set(self, "network", value)

    @property
    @pulumi.getter(name="templateDeployment")
    def template_deployment(self) -> Optional[pulumi.Input['ProviderFeaturesTemplateDeploymentArgs']]:
        return pulumi.get(self, "template_deployment")

    @template_deployment.setter
    def template_deployment(self, value: Optional[pulumi.Input['ProviderFeaturesTemplateDeploymentArgs']]):
        pulumi.set(self, "template_deployment", value)

    @property
    @pulumi.getter(name="virtualMachine")
    def virtual_machine(self) -> Optional[pulumi.Input['ProviderFeaturesVirtualMachineArgs']]:
        return pulumi.get(self, "virtual_machine")

    @virtual_machine.setter
    def virtual_machine(self, value: Optional[pulumi.Input['ProviderFeaturesVirtualMachineArgs']]):
        pulumi.set(self, "virtual_machine", value)

    @property
    @pulumi.getter(name="virtualMachineScaleSet")
    def virtual_machine_scale_set(self) -> Optional[pulumi.Input['ProviderFeaturesVirtualMachineScaleSetArgs']]:
        return pulumi.get(self, "virtual_machine_scale_set")

    @virtual_machine_scale_set.setter
    def virtual_machine_scale_set(self, value: Optional[pulumi.Input['ProviderFeaturesVirtualMachineScaleSetArgs']]):
        pulumi.set(self, "virtual_machine_scale_set", value)


@pulumi.input_type
class ProviderFeaturesKeyVaultArgs:
    def __init__(__self__, *,
                 purge_soft_delete_on_destroy: Optional[pulumi.Input[bool]] = None,
                 recover_soft_deleted_key_vaults: Optional[pulumi.Input[bool]] = None):
        if purge_soft_delete_on_destroy is not None:
            pulumi.set(__self__, "purge_soft_delete_on_destroy", purge_soft_delete_on_destroy)
        if recover_soft_deleted_key_vaults is not None:
            pulumi.set(__self__, "recover_soft_deleted_key_vaults", recover_soft_deleted_key_vaults)

    @property
    @pulumi.getter(name="purgeSoftDeleteOnDestroy")
    def purge_soft_delete_on_destroy(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "purge_soft_delete_on_destroy")

    @purge_soft_delete_on_destroy.setter
    def purge_soft_delete_on_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "purge_soft_delete_on_destroy", value)

    @property
    @pulumi.getter(name="recoverSoftDeletedKeyVaults")
    def recover_soft_deleted_key_vaults(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "recover_soft_deleted_key_vaults")

    @recover_soft_deleted_key_vaults.setter
    def recover_soft_deleted_key_vaults(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "recover_soft_deleted_key_vaults", value)


@pulumi.input_type
class ProviderFeaturesLogAnalyticsWorkspaceArgs:
    def __init__(__self__, *,
                 permanently_delete_on_destroy: pulumi.Input[bool]):
        pulumi.set(__self__, "permanently_delete_on_destroy", permanently_delete_on_destroy)

    @property
    @pulumi.getter(name="permanentlyDeleteOnDestroy")
    def permanently_delete_on_destroy(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "permanently_delete_on_destroy")

    @permanently_delete_on_destroy.setter
    def permanently_delete_on_destroy(self, value: pulumi.Input[bool]):
        pulumi.set(self, "permanently_delete_on_destroy", value)


@pulumi.input_type
class ProviderFeaturesNetworkArgs:
    def __init__(__self__, *,
                 relaxed_locking: pulumi.Input[bool]):
        pulumi.set(__self__, "relaxed_locking", relaxed_locking)

    @property
    @pulumi.getter(name="relaxedLocking")
    def relaxed_locking(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "relaxed_locking")

    @relaxed_locking.setter
    def relaxed_locking(self, value: pulumi.Input[bool]):
        pulumi.set(self, "relaxed_locking", value)


@pulumi.input_type
class ProviderFeaturesTemplateDeploymentArgs:
    def __init__(__self__, *,
                 delete_nested_items_during_deletion: pulumi.Input[bool]):
        pulumi.set(__self__, "delete_nested_items_during_deletion", delete_nested_items_during_deletion)

    @property
    @pulumi.getter(name="deleteNestedItemsDuringDeletion")
    def delete_nested_items_during_deletion(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "delete_nested_items_during_deletion")

    @delete_nested_items_during_deletion.setter
    def delete_nested_items_during_deletion(self, value: pulumi.Input[bool]):
        pulumi.set(self, "delete_nested_items_during_deletion", value)


@pulumi.input_type
class ProviderFeaturesVirtualMachineArgs:
    def __init__(__self__, *,
                 delete_os_disk_on_deletion: Optional[pulumi.Input[bool]] = None,
                 graceful_shutdown: Optional[pulumi.Input[bool]] = None):
        if delete_os_disk_on_deletion is not None:
            pulumi.set(__self__, "delete_os_disk_on_deletion", delete_os_disk_on_deletion)
        if graceful_shutdown is not None:
            pulumi.set(__self__, "graceful_shutdown", graceful_shutdown)

    @property
    @pulumi.getter(name="deleteOsDiskOnDeletion")
    def delete_os_disk_on_deletion(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "delete_os_disk_on_deletion")

    @delete_os_disk_on_deletion.setter
    def delete_os_disk_on_deletion(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "delete_os_disk_on_deletion", value)

    @property
    @pulumi.getter(name="gracefulShutdown")
    def graceful_shutdown(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "graceful_shutdown")

    @graceful_shutdown.setter
    def graceful_shutdown(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "graceful_shutdown", value)


@pulumi.input_type
class ProviderFeaturesVirtualMachineScaleSetArgs:
    def __init__(__self__, *,
                 roll_instances_when_required: pulumi.Input[bool]):
        pulumi.set(__self__, "roll_instances_when_required", roll_instances_when_required)

    @property
    @pulumi.getter(name="rollInstancesWhenRequired")
    def roll_instances_when_required(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "roll_instances_when_required")

    @roll_instances_when_required.setter
    def roll_instances_when_required(self, value: pulumi.Input[bool]):
        pulumi.set(self, "roll_instances_when_required", value)


