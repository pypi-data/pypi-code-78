# coding: utf-8

"""
    EXACT - API

    API to interact with the EXACT Server  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class LogImageActions(object):
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
        'count': 'int',
        'next': 'str',
        'previous': 'str',
        'results': 'list[LogImageAction]'
    }

    attribute_map = {
        'count': 'count',
        'next': 'next',
        'previous': 'previous',
        'results': 'results'
    }

    def __init__(self, count=None, next=None, previous=None, results=None):  # noqa: E501
        """LogImageActions - a model defined in Swagger"""  # noqa: E501
        self._count = None
        self._next = None
        self._previous = None
        self._results = None
        self.discriminator = None
        if count is not None:
            self.count = count
        if next is not None:
            self.next = next
        if previous is not None:
            self.previous = previous
        if results is not None:
            self.results = results

    @property
    def count(self):
        """Gets the count of this LogImageActions.  # noqa: E501


        :return: The count of this LogImageActions.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this LogImageActions.


        :param count: The count of this LogImageActions.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def next(self):
        """Gets the next of this LogImageActions.  # noqa: E501


        :return: The next of this LogImageActions.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this LogImageActions.


        :param next: The next of this LogImageActions.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def previous(self):
        """Gets the previous of this LogImageActions.  # noqa: E501


        :return: The previous of this LogImageActions.  # noqa: E501
        :rtype: str
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Sets the previous of this LogImageActions.


        :param previous: The previous of this LogImageActions.  # noqa: E501
        :type: str
        """

        self._previous = previous

    @property
    def results(self):
        """Gets the results of this LogImageActions.  # noqa: E501


        :return: The results of this LogImageActions.  # noqa: E501
        :rtype: list[LogImageAction]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this LogImageActions.


        :param results: The results of this LogImageActions.  # noqa: E501
        :type: list[LogImageAction]
        """

        self._results = results

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
        if issubclass(LogImageActions, dict):
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
        if not isinstance(other, LogImageActions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
