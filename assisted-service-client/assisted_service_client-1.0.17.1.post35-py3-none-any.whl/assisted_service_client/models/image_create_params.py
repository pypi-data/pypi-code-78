# coding: utf-8

"""
    AssistedInstall

    Assisted installation  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ImageCreateParams(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ssh_public_key': 'str',
        'static_network_config': 'list[str]',
        'image_type': 'ImageType'
    }

    attribute_map = {
        'ssh_public_key': 'ssh_public_key',
        'static_network_config': 'static_network_config',
        'image_type': 'image_type'
    }

    def __init__(self, ssh_public_key=None, static_network_config=None, image_type=None):  # noqa: E501
        """ImageCreateParams - a model defined in Swagger"""  # noqa: E501

        self._ssh_public_key = None
        self._static_network_config = None
        self._image_type = None
        self.discriminator = None

        if ssh_public_key is not None:
            self.ssh_public_key = ssh_public_key
        if static_network_config is not None:
            self.static_network_config = static_network_config
        if image_type is not None:
            self.image_type = image_type

    @property
    def ssh_public_key(self):
        """Gets the ssh_public_key of this ImageCreateParams.  # noqa: E501

        SSH public key for debugging the installation.  # noqa: E501

        :return: The ssh_public_key of this ImageCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._ssh_public_key

    @ssh_public_key.setter
    def ssh_public_key(self, ssh_public_key):
        """Sets the ssh_public_key of this ImageCreateParams.

        SSH public key for debugging the installation.  # noqa: E501

        :param ssh_public_key: The ssh_public_key of this ImageCreateParams.  # noqa: E501
        :type: str
        """

        self._ssh_public_key = ssh_public_key

    @property
    def static_network_config(self):
        """Gets the static_network_config of this ImageCreateParams.  # noqa: E501


        :return: The static_network_config of this ImageCreateParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._static_network_config

    @static_network_config.setter
    def static_network_config(self, static_network_config):
        """Sets the static_network_config of this ImageCreateParams.


        :param static_network_config: The static_network_config of this ImageCreateParams.  # noqa: E501
        :type: list[str]
        """

        self._static_network_config = static_network_config

    @property
    def image_type(self):
        """Gets the image_type of this ImageCreateParams.  # noqa: E501

        Type of image that should be generated.  # noqa: E501

        :return: The image_type of this ImageCreateParams.  # noqa: E501
        :rtype: ImageType
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this ImageCreateParams.

        Type of image that should be generated.  # noqa: E501

        :param image_type: The image_type of this ImageCreateParams.  # noqa: E501
        :type: ImageType
        """

        self._image_type = image_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ImageCreateParams, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImageCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
