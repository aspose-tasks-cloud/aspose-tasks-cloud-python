# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="ExtendedAttributeItem.py">
#   Copyright (c) 2020 Aspose.Tasks Cloud
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------
import pprint
import re  # noqa: F401

import six


class ExtendedAttributeItem(object):
    """
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'link': 'Link',
        'index': 'int',
        'field_name': 'str',
        'alias': 'str',
        'field_id': 'str'
    }

    attribute_map = {
        'link': 'link',
        'index': 'index',
        'field_name': 'fieldName',
        'alias': 'alias',
        'field_id': 'fieldId'
    }

    def __init__(self, link=None, index=None, field_name=None, alias=None, field_id=None):  # noqa: E501
        """ExtendedAttributeItem - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._index = None
        self._field_name = None
        self._alias = None
        self._field_id = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if index is not None:
            self.index = index
        if field_name is not None:
            self.field_name = field_name
        if alias is not None:
            self.alias = alias
        if field_id is not None:
            self.field_id = field_id

    @property
    def link(self):
        """Gets the link of this ExtendedAttributeItem.  # noqa: E501


        :return: The link of this ExtendedAttributeItem.  # noqa: E501
        :rtype: Link
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this ExtendedAttributeItem.


        :param link: The link of this ExtendedAttributeItem.  # noqa: E501
        :type: Link
        """
        self._link = link
    @property
    def index(self):
        """Gets the index of this ExtendedAttributeItem.  # noqa: E501


        :return: The index of this ExtendedAttributeItem.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this ExtendedAttributeItem.


        :param index: The index of this ExtendedAttributeItem.  # noqa: E501
        :type: int
        """
        if index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501
        self._index = index
    @property
    def field_name(self):
        """Gets the field_name of this ExtendedAttributeItem.  # noqa: E501


        :return: The field_name of this ExtendedAttributeItem.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this ExtendedAttributeItem.


        :param field_name: The field_name of this ExtendedAttributeItem.  # noqa: E501
        :type: str
        """
        self._field_name = field_name
    @property
    def alias(self):
        """Gets the alias of this ExtendedAttributeItem.  # noqa: E501


        :return: The alias of this ExtendedAttributeItem.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this ExtendedAttributeItem.


        :param alias: The alias of this ExtendedAttributeItem.  # noqa: E501
        :type: str
        """
        self._alias = alias
    @property
    def field_id(self):
        """Gets the field_id of this ExtendedAttributeItem.  # noqa: E501


        :return: The field_id of this ExtendedAttributeItem.  # noqa: E501
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this ExtendedAttributeItem.


        :param field_id: The field_id of this ExtendedAttributeItem.  # noqa: E501
        :type: str
        """
        self._field_id = field_id
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExtendedAttributeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
