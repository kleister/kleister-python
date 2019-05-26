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


class ModTeamParams(object):
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
        'mod': 'str',
        'team': 'str',
        'perm': 'str'
    }

    attribute_map = {
        'mod': 'mod',
        'team': 'team',
        'perm': 'perm'
    }

    def __init__(self, mod=None, team=None, perm=None):  # noqa: E501
        """ModTeamParams - a model defined in OpenAPI"""  # noqa: E501

        self._mod = None
        self._team = None
        self._perm = None
        self.discriminator = None

        self.mod = mod
        self.team = team
        self.perm = perm

    @property
    def mod(self):
        """Gets the mod of this ModTeamParams.  # noqa: E501


        :return: The mod of this ModTeamParams.  # noqa: E501
        :rtype: str
        """
        return self._mod

    @mod.setter
    def mod(self, mod):
        """Sets the mod of this ModTeamParams.


        :param mod: The mod of this ModTeamParams.  # noqa: E501
        :type: str
        """
        if mod is None:
            raise ValueError("Invalid value for `mod`, must not be `None`")  # noqa: E501

        self._mod = mod

    @property
    def team(self):
        """Gets the team of this ModTeamParams.  # noqa: E501


        :return: The team of this ModTeamParams.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this ModTeamParams.


        :param team: The team of this ModTeamParams.  # noqa: E501
        :type: str
        """
        if team is None:
            raise ValueError("Invalid value for `team`, must not be `None`")  # noqa: E501

        self._team = team

    @property
    def perm(self):
        """Gets the perm of this ModTeamParams.  # noqa: E501


        :return: The perm of this ModTeamParams.  # noqa: E501
        :rtype: str
        """
        return self._perm

    @perm.setter
    def perm(self, perm):
        """Sets the perm of this ModTeamParams.


        :param perm: The perm of this ModTeamParams.  # noqa: E501
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
        if not isinstance(other, ModTeamParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
