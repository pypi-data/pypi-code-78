# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'DatabaseExtendedAuditingPolicy',
    'DatabaseImport',
    'DatabaseThreatDetectionPolicy',
    'FailoverGroupPartnerServer',
    'FailoverGroupReadWriteEndpointFailoverPolicy',
    'FailoverGroupReadonlyEndpointFailoverPolicy',
    'SqlServerExtendedAuditingPolicy',
    'SqlServerIdentity',
    'GetServerIdentityResult',
]

@pulumi.output_type
class DatabaseExtendedAuditingPolicy(dict):
    def __init__(__self__, *,
                 log_monitoring_enabled: Optional[bool] = None,
                 retention_in_days: Optional[int] = None,
                 storage_account_access_key: Optional[str] = None,
                 storage_account_access_key_is_secondary: Optional[bool] = None,
                 storage_endpoint: Optional[str] = None):
        """
        :param int retention_in_days: Specifies the number of days to retain logs for in the storage account.
        :param str storage_account_access_key: Specifies the access key to use for the auditing storage account.
        :param bool storage_account_access_key_is_secondary: Specifies whether `storage_account_access_key` value is the storage's secondary key.
        :param str storage_endpoint: Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net).
        """
        if log_monitoring_enabled is not None:
            pulumi.set(__self__, "log_monitoring_enabled", log_monitoring_enabled)
        if retention_in_days is not None:
            pulumi.set(__self__, "retention_in_days", retention_in_days)
        if storage_account_access_key is not None:
            pulumi.set(__self__, "storage_account_access_key", storage_account_access_key)
        if storage_account_access_key_is_secondary is not None:
            pulumi.set(__self__, "storage_account_access_key_is_secondary", storage_account_access_key_is_secondary)
        if storage_endpoint is not None:
            pulumi.set(__self__, "storage_endpoint", storage_endpoint)

    @property
    @pulumi.getter(name="logMonitoringEnabled")
    def log_monitoring_enabled(self) -> Optional[bool]:
        return pulumi.get(self, "log_monitoring_enabled")

    @property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> Optional[int]:
        """
        Specifies the number of days to retain logs for in the storage account.
        """
        return pulumi.get(self, "retention_in_days")

    @property
    @pulumi.getter(name="storageAccountAccessKey")
    def storage_account_access_key(self) -> Optional[str]:
        """
        Specifies the access key to use for the auditing storage account.
        """
        return pulumi.get(self, "storage_account_access_key")

    @property
    @pulumi.getter(name="storageAccountAccessKeyIsSecondary")
    def storage_account_access_key_is_secondary(self) -> Optional[bool]:
        """
        Specifies whether `storage_account_access_key` value is the storage's secondary key.
        """
        return pulumi.get(self, "storage_account_access_key_is_secondary")

    @property
    @pulumi.getter(name="storageEndpoint")
    def storage_endpoint(self) -> Optional[str]:
        """
        Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net).
        """
        return pulumi.get(self, "storage_endpoint")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DatabaseImport(dict):
    def __init__(__self__, *,
                 administrator_login: str,
                 administrator_login_password: str,
                 authentication_type: str,
                 storage_key: str,
                 storage_key_type: str,
                 storage_uri: str,
                 operation_mode: Optional[str] = None):
        """
        :param str administrator_login: Specifies the name of the SQL administrator.
        :param str administrator_login_password: Specifies the password of the SQL administrator.
        :param str authentication_type: Specifies the type of authentication used to access the server. Valid values are `SQL` or `ADPassword`.
        :param str storage_key: Specifies the access key for the storage account.
        :param str storage_key_type: Specifies the type of access key for the storage account. Valid values are `StorageAccessKey` or `SharedAccessKey`.
        :param str storage_uri: Specifies the blob URI of the .bacpac file.
        :param str operation_mode: Specifies the type of import operation being performed. The only allowable value is `Import`.
        """
        pulumi.set(__self__, "administrator_login", administrator_login)
        pulumi.set(__self__, "administrator_login_password", administrator_login_password)
        pulumi.set(__self__, "authentication_type", authentication_type)
        pulumi.set(__self__, "storage_key", storage_key)
        pulumi.set(__self__, "storage_key_type", storage_key_type)
        pulumi.set(__self__, "storage_uri", storage_uri)
        if operation_mode is not None:
            pulumi.set(__self__, "operation_mode", operation_mode)

    @property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> str:
        """
        Specifies the name of the SQL administrator.
        """
        return pulumi.get(self, "administrator_login")

    @property
    @pulumi.getter(name="administratorLoginPassword")
    def administrator_login_password(self) -> str:
        """
        Specifies the password of the SQL administrator.
        """
        return pulumi.get(self, "administrator_login_password")

    @property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> str:
        """
        Specifies the type of authentication used to access the server. Valid values are `SQL` or `ADPassword`.
        """
        return pulumi.get(self, "authentication_type")

    @property
    @pulumi.getter(name="storageKey")
    def storage_key(self) -> str:
        """
        Specifies the access key for the storage account.
        """
        return pulumi.get(self, "storage_key")

    @property
    @pulumi.getter(name="storageKeyType")
    def storage_key_type(self) -> str:
        """
        Specifies the type of access key for the storage account. Valid values are `StorageAccessKey` or `SharedAccessKey`.
        """
        return pulumi.get(self, "storage_key_type")

    @property
    @pulumi.getter(name="storageUri")
    def storage_uri(self) -> str:
        """
        Specifies the blob URI of the .bacpac file.
        """
        return pulumi.get(self, "storage_uri")

    @property
    @pulumi.getter(name="operationMode")
    def operation_mode(self) -> Optional[str]:
        """
        Specifies the type of import operation being performed. The only allowable value is `Import`.
        """
        return pulumi.get(self, "operation_mode")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DatabaseThreatDetectionPolicy(dict):
    def __init__(__self__, *,
                 disabled_alerts: Optional[Sequence[str]] = None,
                 email_account_admins: Optional[str] = None,
                 email_addresses: Optional[Sequence[str]] = None,
                 retention_days: Optional[int] = None,
                 state: Optional[str] = None,
                 storage_account_access_key: Optional[str] = None,
                 storage_endpoint: Optional[str] = None,
                 use_server_default: Optional[str] = None):
        """
        :param Sequence[str] disabled_alerts: Specifies a list of alerts which should be disabled. Possible values include `Access_Anomaly`, `Sql_Injection` and `Sql_Injection_Vulnerability`.
        :param str email_account_admins: Should the account administrators be emailed when this alert is triggered?
        :param Sequence[str] email_addresses: A list of email addresses which alerts should be sent to.
        :param int retention_days: Specifies the number of days to keep in the Threat Detection audit logs.
        :param str state: The State of the Policy. Possible values are `Enabled`, `Disabled` or `New`.
        :param str storage_account_access_key: Specifies the identifier key of the Threat Detection audit storage account. Required if `state` is `Enabled`.
        :param str storage_endpoint: Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all Threat Detection audit logs. Required if `state` is `Enabled`.
        """
        if disabled_alerts is not None:
            pulumi.set(__self__, "disabled_alerts", disabled_alerts)
        if email_account_admins is not None:
            pulumi.set(__self__, "email_account_admins", email_account_admins)
        if email_addresses is not None:
            pulumi.set(__self__, "email_addresses", email_addresses)
        if retention_days is not None:
            pulumi.set(__self__, "retention_days", retention_days)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if storage_account_access_key is not None:
            pulumi.set(__self__, "storage_account_access_key", storage_account_access_key)
        if storage_endpoint is not None:
            pulumi.set(__self__, "storage_endpoint", storage_endpoint)
        if use_server_default is not None:
            pulumi.set(__self__, "use_server_default", use_server_default)

    @property
    @pulumi.getter(name="disabledAlerts")
    def disabled_alerts(self) -> Optional[Sequence[str]]:
        """
        Specifies a list of alerts which should be disabled. Possible values include `Access_Anomaly`, `Sql_Injection` and `Sql_Injection_Vulnerability`.
        """
        return pulumi.get(self, "disabled_alerts")

    @property
    @pulumi.getter(name="emailAccountAdmins")
    def email_account_admins(self) -> Optional[str]:
        """
        Should the account administrators be emailed when this alert is triggered?
        """
        return pulumi.get(self, "email_account_admins")

    @property
    @pulumi.getter(name="emailAddresses")
    def email_addresses(self) -> Optional[Sequence[str]]:
        """
        A list of email addresses which alerts should be sent to.
        """
        return pulumi.get(self, "email_addresses")

    @property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[int]:
        """
        Specifies the number of days to keep in the Threat Detection audit logs.
        """
        return pulumi.get(self, "retention_days")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The State of the Policy. Possible values are `Enabled`, `Disabled` or `New`.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="storageAccountAccessKey")
    def storage_account_access_key(self) -> Optional[str]:
        """
        Specifies the identifier key of the Threat Detection audit storage account. Required if `state` is `Enabled`.
        """
        return pulumi.get(self, "storage_account_access_key")

    @property
    @pulumi.getter(name="storageEndpoint")
    def storage_endpoint(self) -> Optional[str]:
        """
        Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all Threat Detection audit logs. Required if `state` is `Enabled`.
        """
        return pulumi.get(self, "storage_endpoint")

    @property
    @pulumi.getter(name="useServerDefault")
    def use_server_default(self) -> Optional[str]:
        return pulumi.get(self, "use_server_default")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FailoverGroupPartnerServer(dict):
    def __init__(__self__, *,
                 id: str,
                 location: Optional[str] = None,
                 role: Optional[str] = None):
        """
        :param str id: the SQL server ID
        :param str location: the location of the failover group.
        :param str role: local replication role of the failover group instance.
        """
        pulumi.set(__self__, "id", id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if role is not None:
            pulumi.set(__self__, "role", role)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        the SQL server ID
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        the location of the failover group.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def role(self) -> Optional[str]:
        """
        local replication role of the failover group instance.
        """
        return pulumi.get(self, "role")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FailoverGroupReadWriteEndpointFailoverPolicy(dict):
    def __init__(__self__, *,
                 mode: str,
                 grace_minutes: Optional[int] = None):
        """
        :param str mode: the failover mode. Possible values are `Manual`, `Automatic`
        :param int grace_minutes: Applies only if `mode` is `Automatic`. The grace period in minutes before failover with data loss is attempted
        """
        pulumi.set(__self__, "mode", mode)
        if grace_minutes is not None:
            pulumi.set(__self__, "grace_minutes", grace_minutes)

    @property
    @pulumi.getter
    def mode(self) -> str:
        """
        the failover mode. Possible values are `Manual`, `Automatic`
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter(name="graceMinutes")
    def grace_minutes(self) -> Optional[int]:
        """
        Applies only if `mode` is `Automatic`. The grace period in minutes before failover with data loss is attempted
        """
        return pulumi.get(self, "grace_minutes")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FailoverGroupReadonlyEndpointFailoverPolicy(dict):
    def __init__(__self__, *,
                 mode: str):
        """
        :param str mode: Failover policy for the read-only endpoint. Possible values are `Enabled`, and `Disabled`
        """
        pulumi.set(__self__, "mode", mode)

    @property
    @pulumi.getter
    def mode(self) -> str:
        """
        Failover policy for the read-only endpoint. Possible values are `Enabled`, and `Disabled`
        """
        return pulumi.get(self, "mode")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SqlServerExtendedAuditingPolicy(dict):
    def __init__(__self__, *,
                 log_monitoring_enabled: Optional[bool] = None,
                 retention_in_days: Optional[int] = None,
                 storage_account_access_key: Optional[str] = None,
                 storage_account_access_key_is_secondary: Optional[bool] = None,
                 storage_endpoint: Optional[str] = None):
        """
        :param bool log_monitoring_enabled: (Optional) Enable audit events to Azure Monitor? To enable server audit events to Azure Monitor, please enable its master database audit events to Azure Monitor.
        :param int retention_in_days: (Optional) Specifies the number of days to retain logs for in the storage account.
        :param str storage_account_access_key: (Optional)  Specifies the access key to use for the auditing storage account.
        :param bool storage_account_access_key_is_secondary: (Optional) Specifies whether `storage_account_access_key` value is the storage's secondary key.
        :param str storage_endpoint: (Optional) Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net).
        """
        if log_monitoring_enabled is not None:
            pulumi.set(__self__, "log_monitoring_enabled", log_monitoring_enabled)
        if retention_in_days is not None:
            pulumi.set(__self__, "retention_in_days", retention_in_days)
        if storage_account_access_key is not None:
            pulumi.set(__self__, "storage_account_access_key", storage_account_access_key)
        if storage_account_access_key_is_secondary is not None:
            pulumi.set(__self__, "storage_account_access_key_is_secondary", storage_account_access_key_is_secondary)
        if storage_endpoint is not None:
            pulumi.set(__self__, "storage_endpoint", storage_endpoint)

    @property
    @pulumi.getter(name="logMonitoringEnabled")
    def log_monitoring_enabled(self) -> Optional[bool]:
        """
        (Optional) Enable audit events to Azure Monitor? To enable server audit events to Azure Monitor, please enable its master database audit events to Azure Monitor.
        """
        return pulumi.get(self, "log_monitoring_enabled")

    @property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> Optional[int]:
        """
        (Optional) Specifies the number of days to retain logs for in the storage account.
        """
        return pulumi.get(self, "retention_in_days")

    @property
    @pulumi.getter(name="storageAccountAccessKey")
    def storage_account_access_key(self) -> Optional[str]:
        """
        (Optional)  Specifies the access key to use for the auditing storage account.
        """
        return pulumi.get(self, "storage_account_access_key")

    @property
    @pulumi.getter(name="storageAccountAccessKeyIsSecondary")
    def storage_account_access_key_is_secondary(self) -> Optional[bool]:
        """
        (Optional) Specifies whether `storage_account_access_key` value is the storage's secondary key.
        """
        return pulumi.get(self, "storage_account_access_key_is_secondary")

    @property
    @pulumi.getter(name="storageEndpoint")
    def storage_endpoint(self) -> Optional[str]:
        """
        (Optional) Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net).
        """
        return pulumi.get(self, "storage_endpoint")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SqlServerIdentity(dict):
    def __init__(__self__, *,
                 type: str,
                 principal_id: Optional[str] = None,
                 tenant_id: Optional[str] = None):
        """
        :param str type: Specifies the identity type of the Microsoft SQL Server. At this time the only allowed value is `SystemAssigned`.
        :param str principal_id: The Principal ID for the Service Principal associated with the Identity of this SQL Server.
        :param str tenant_id: The Tenant ID for the Service Principal associated with the Identity of this SQL Server.
        """
        pulumi.set(__self__, "type", type)
        if principal_id is not None:
            pulumi.set(__self__, "principal_id", principal_id)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Specifies the identity type of the Microsoft SQL Server. At this time the only allowed value is `SystemAssigned`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[str]:
        """
        The Principal ID for the Service Principal associated with the Identity of this SQL Server.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[str]:
        """
        The Tenant ID for the Service Principal associated with the Identity of this SQL Server.
        """
        return pulumi.get(self, "tenant_id")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetServerIdentityResult(dict):
    def __init__(__self__, *,
                 principal_id: str,
                 tenant_id: str,
                 type: str):
        """
        :param str principal_id: The ID of the Principal (Client) in Azure Active Directory.
        :param str tenant_id: The ID of the Azure Active Directory Tenant.
        :param str type: The identity type of the SQL Server.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The ID of the Principal (Client) in Azure Active Directory.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The ID of the Azure Active Directory Tenant.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The identity type of the SQL Server.
        """
        return pulumi.get(self, "type")


