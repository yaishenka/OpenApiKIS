# coding: utf-8

"""
    UrlShortener API

    Description  # noqa: E501

    OpenAPI spec version: v1
    Contact: gagarinovdaniil@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class Url(object):
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
        'short_url': 'str',
        'full_url': 'str',
        'creator': 'int',
        'date_created': 'datetime',
        'used': 'int'
    }

    attribute_map = {
        'short_url': 'short_url',
        'full_url': 'full_url',
        'creator': 'creator',
        'date_created': 'date_created',
        'used': 'used'
    }

    def __init__(self, short_url=None, full_url=None, creator=None, date_created=None, used=None, _configuration=None):  # noqa: E501
        """Url - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._short_url = None
        self._full_url = None
        self._creator = None
        self._date_created = None
        self._used = None
        self.discriminator = None

        self.short_url = short_url
        self.full_url = full_url
        if creator is not None:
            self.creator = creator
        if date_created is not None:
            self.date_created = date_created
        if used is not None:
            self.used = used

    @property
    def short_url(self):
        """Gets the short_url of this Url.  # noqa: E501


        :return: The short_url of this Url.  # noqa: E501
        :rtype: str
        """
        return self._short_url

    @short_url.setter
    def short_url(self, short_url):
        """Sets the short_url of this Url.


        :param short_url: The short_url of this Url.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and short_url is None:
            raise ValueError("Invalid value for `short_url`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                short_url is not None and len(short_url) > 50):
            raise ValueError("Invalid value for `short_url`, length must be less than or equal to `50`")  # noqa: E501
        if (self._configuration.client_side_validation and
                short_url is not None and len(short_url) < 1):
            raise ValueError("Invalid value for `short_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._short_url = short_url

    @property
    def full_url(self):
        """Gets the full_url of this Url.  # noqa: E501


        :return: The full_url of this Url.  # noqa: E501
        :rtype: str
        """
        return self._full_url

    @full_url.setter
    def full_url(self, full_url):
        """Sets the full_url of this Url.


        :param full_url: The full_url of this Url.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and full_url is None:
            raise ValueError("Invalid value for `full_url`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                full_url is not None and len(full_url) < 1):
            raise ValueError("Invalid value for `full_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._full_url = full_url

    @property
    def creator(self):
        """Gets the creator of this Url.  # noqa: E501


        :return: The creator of this Url.  # noqa: E501
        :rtype: int
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this Url.


        :param creator: The creator of this Url.  # noqa: E501
        :type: int
        """

        self._creator = creator

    @property
    def date_created(self):
        """Gets the date_created of this Url.  # noqa: E501


        :return: The date_created of this Url.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this Url.


        :param date_created: The date_created of this Url.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def used(self):
        """Gets the used of this Url.  # noqa: E501


        :return: The used of this Url.  # noqa: E501
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this Url.


        :param used: The used of this Url.  # noqa: E501
        :type: int
        """

        self._used = used

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
        if issubclass(Url, dict):
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
        if not isinstance(other, Url):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Url):
            return True

        return self.to_dict() != other.to_dict()