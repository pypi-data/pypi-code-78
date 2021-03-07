# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'GetUserResult',
    'AwaitableGetUserResult',
    'get_user',
]

@pulumi.output_type
class GetUserResult:
    """
    A collection of values returned by getUser.
    """
    def __init__(__self__, api_management_name=None, email=None, first_name=None, id=None, last_name=None, note=None, resource_group_name=None, state=None, user_id=None):
        if api_management_name and not isinstance(api_management_name, str):
            raise TypeError("Expected argument 'api_management_name' to be a str")
        pulumi.set(__self__, "api_management_name", api_management_name)
        if email and not isinstance(email, str):
            raise TypeError("Expected argument 'email' to be a str")
        pulumi.set(__self__, "email", email)
        if first_name and not isinstance(first_name, str):
            raise TypeError("Expected argument 'first_name' to be a str")
        pulumi.set(__self__, "first_name", first_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_name and not isinstance(last_name, str):
            raise TypeError("Expected argument 'last_name' to be a str")
        pulumi.set(__self__, "last_name", last_name)
        if note and not isinstance(note, str):
            raise TypeError("Expected argument 'note' to be a str")
        pulumi.set(__self__, "note", note)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if user_id and not isinstance(user_id, str):
            raise TypeError("Expected argument 'user_id' to be a str")
        pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter(name="apiManagementName")
    def api_management_name(self) -> str:
        return pulumi.get(self, "api_management_name")

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        The Email Address used for this User.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> str:
        """
        The First Name for the User.
        """
        return pulumi.get(self, "first_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> str:
        """
        The Last Name for the User.
        """
        return pulumi.get(self, "last_name")

    @property
    @pulumi.getter
    def note(self) -> str:
        """
        Any notes about this User.
        """
        return pulumi.get(self, "note")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of this User, for example `active`, `blocked` or `pending`.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> str:
        return pulumi.get(self, "user_id")


class AwaitableGetUserResult(GetUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserResult(
            api_management_name=self.api_management_name,
            email=self.email,
            first_name=self.first_name,
            id=self.id,
            last_name=self.last_name,
            note=self.note,
            resource_group_name=self.resource_group_name,
            state=self.state,
            user_id=self.user_id)


def get_user(api_management_name: Optional[str] = None,
             resource_group_name: Optional[str] = None,
             user_id: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUserResult:
    """
    Use this data source to access information about an existing API Management User.


    :param str api_management_name: The Name of the API Management Service in which this User exists.
    :param str resource_group_name: The Name of the Resource Group in which the API Management Service exists.
    :param str user_id: The Identifier for the User.
    """
    __args__ = dict()
    __args__['apiManagementName'] = api_management_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['userId'] = user_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:apimanagement/getUser:getUser', __args__, opts=opts, typ=GetUserResult).value

    return AwaitableGetUserResult(
        api_management_name=__ret__.api_management_name,
        email=__ret__.email,
        first_name=__ret__.first_name,
        id=__ret__.id,
        last_name=__ret__.last_name,
        note=__ret__.note,
        resource_group_name=__ret__.resource_group_name,
        state=__ret__.state,
        user_id=__ret__.user_id)
