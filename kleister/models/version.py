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


class Version(object):
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
        'id': 'str',
        'mod_id': 'str',
        'slug': 'str',
        'name': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'mod_id': 'mod_id',
        'slug': 'slug',
        'name': 'name',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, mod_id=None, slug=None, name=None, created_at=None, updated_at=None):  # noqa: E501
        """Version - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._mod_id = None
        self._slug = None
        self._name = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if mod_id is not None:
            self.mod_id = mod_id
        if slug is not None:
            self.slug = slug
        self.name = name
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this Version.  # noqa: E501


        :return: The id of this Version.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Version.


        :param id: The id of this Version.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def mod_id(self):
        """Gets the mod_id of this Version.  # noqa: E501


        :return: The mod_id of this Version.  # noqa: E501
        :rtype: str
        """
        return self._mod_id

    @mod_id.setter
    def mod_id(self, mod_id):
        """Sets the mod_id of this Version.


        :param mod_id: The mod_id of this Version.  # noqa: E501
        :type: str
        """

        self._mod_id = mod_id

    @property
    def slug(self):
        """Gets the slug of this Version.  # noqa: E501


        :return: The slug of this Version.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Version.


        :param slug: The slug of this Version.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def name(self):
        """Gets the name of this Version.  # noqa: E501


        :return: The name of this Version.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Version.


        :param name: The name of this Version.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this Version.  # noqa: E501


        :return: The created_at of this Version.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Version.


        :param created_at: The created_at of this Version.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Version.  # noqa: E501


        :return: The updated_at of this Version.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Version.


        :param updated_at: The updated_at of this Version.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, Version):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
