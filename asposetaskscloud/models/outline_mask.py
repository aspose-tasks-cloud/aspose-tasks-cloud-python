# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="OutlineMask.py">
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


class OutlineMask(object):
    """Represents four elements of a mask which defines an outline code format.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'level': 'int',
        'type': 'MaskType',
        'length': 'int',
        'separator': 'str'
    }

    attribute_map = {
        'level': 'level',
        'type': 'type',
        'length': 'length',
        'separator': 'separator'
    }

    def __init__(self, level=None, type=None, length=None, separator=None):  # noqa: E501
        """OutlineMask - a model defined in Swagger"""  # noqa: E501

        self._level = None
        self._type = None
        self._length = None
        self._separator = None
        self.discriminator = None

        if level is not None:
            self.level = level
        if type is not None:
            self.type = type
        if length is not None:
            self.length = length
        if separator is not None:
            self.separator = separator

    @property
    def level(self):
        """Gets the level of this OutlineMask.  # noqa: E501

        The level of a mask.  # noqa: E501

        :return: The level of this OutlineMask.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this OutlineMask.

        The level of a mask.  # noqa: E501

        :param level: The level of this OutlineMask.  # noqa: E501
        :type: int
        """
        if level is None:
            raise ValueError("Invalid value for `level`, must not be `None`")  # noqa: E501
        self._level = level
    @property
    def type(self):
        """Gets the type of this OutlineMask.  # noqa: E501

        The type of a mask.  # noqa: E501

        :return: The type of this OutlineMask.  # noqa: E501
        :rtype: MaskType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OutlineMask.

        The type of a mask.  # noqa: E501

        :param type: The type of this OutlineMask.  # noqa: E501
        :type: MaskType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type
    @property
    def length(self):
        """Gets the length of this OutlineMask.  # noqa: E501

        The maximum length (in characters) of the outline code values. 0 if length is not defined.  # noqa: E501

        :return: The length of this OutlineMask.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this OutlineMask.

        The maximum length (in characters) of the outline code values. 0 if length is not defined.  # noqa: E501

        :param length: The length of this OutlineMask.  # noqa: E501
        :type: int
        """
        if length is None:
            raise ValueError("Invalid value for `length`, must not be `None`")  # noqa: E501
        self._length = length
    @property
    def separator(self):
        """Gets the separator of this OutlineMask.  # noqa: E501

        The separator of code values.  # noqa: E501

        :return: The separator of this OutlineMask.  # noqa: E501
        :rtype: str
        """
        return self._separator

    @separator.setter
    def separator(self, separator):
        """Sets the separator of this OutlineMask.

        The separator of code values.  # noqa: E501

        :param separator: The separator of this OutlineMask.  # noqa: E501
        :type: str
        """
        self._separator = separator
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
        if not isinstance(other, OutlineMask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
