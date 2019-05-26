# coding: utf-8

"""
    Kleister OpenAPI

    API definition for Kleister, manage mod packs for Minecraft  # noqa: E501

    The version of the OpenAPI document: 1.0.0-alpha1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class UserModParams(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'user': 'str',
        'mod': 'str',
        'perm': 'str'
    }

    attribute_map = {
        'user': 'user',
        'mod': 'mod',
        'perm': 'perm'
    }

    def __init__(self, user=None, mod=None, perm=None):  # noqa: E501
        """UserModParams - a model defined in OpenAPI"""  # noqa: E501

        self._user = None
        self._mod = None
        self._perm = None
        self.discriminator = None

        self.user = user
        self.mod = mod
        self.perm = perm

    @property
    def user(self):
        """Gets the user of this UserModParams.  # noqa: E501


        :return: The user of this UserModParams.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this UserModParams.


        :param user: The user of this UserModParams.  # noqa: E501
        :type: str
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def mod(self):
        """Gets the mod of this UserModParams.  # noqa: E501


        :return: The mod of this UserModParams.  # noqa: E501
        :rtype: str
        """
        return self._mod

    @mod.setter
    def mod(self, mod):
        """Sets the mod of this UserModParams.


        :param mod: The mod of this UserModParams.  # noqa: E501
        :type: str
        """
        if mod is None:
            raise ValueError("Invalid value for `mod`, must not be `None`")  # noqa: E501

        self._mod = mod

    @property
    def perm(self):
        """Gets the perm of this UserModParams.  # noqa: E501


        :return: The perm of this UserModParams.  # noqa: E501
        :rtype: str
        """
        return self._perm

    @perm.setter
    def perm(self, perm):
        """Sets the perm of this UserModParams.


        :param perm: The perm of this UserModParams.  # noqa: E501
        :type: str
        """
        if perm is None:
            raise ValueError("Invalid value for `perm`, must not be `None`")  # noqa: E501

        self._perm = perm

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserModParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
