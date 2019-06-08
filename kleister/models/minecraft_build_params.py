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


class MinecraftBuildParams(object):
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
        'pack': 'str',
        'build': 'str'
    }

    attribute_map = {
        'pack': 'pack',
        'build': 'build'
    }

    def __init__(self, pack=None, build=None):  # noqa: E501
        """MinecraftBuildParams - a model defined in OpenAPI"""  # noqa: E501

        self._pack = None
        self._build = None
        self.discriminator = None

        self.pack = pack
        self.build = build

    @property
    def pack(self):
        """Gets the pack of this MinecraftBuildParams.  # noqa: E501


        :return: The pack of this MinecraftBuildParams.  # noqa: E501
        :rtype: str
        """
        return self._pack

    @pack.setter
    def pack(self, pack):
        """Sets the pack of this MinecraftBuildParams.


        :param pack: The pack of this MinecraftBuildParams.  # noqa: E501
        :type: str
        """
        if pack is None:
            raise ValueError("Invalid value for `pack`, must not be `None`")  # noqa: E501

        self._pack = pack

    @property
    def build(self):
        """Gets the build of this MinecraftBuildParams.  # noqa: E501


        :return: The build of this MinecraftBuildParams.  # noqa: E501
        :rtype: str
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this MinecraftBuildParams.


        :param build: The build of this MinecraftBuildParams.  # noqa: E501
        :type: str
        """
        if build is None:
            raise ValueError("Invalid value for `build`, must not be `None`")  # noqa: E501

        self._build = build

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
        if not isinstance(other, MinecraftBuildParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
