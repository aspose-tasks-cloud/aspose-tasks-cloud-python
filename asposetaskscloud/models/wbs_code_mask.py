# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="WBSCodeMask.py">
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


class WBSCodeMask(object):
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
        'level': 'int',
        'length': 'int',
        'sequence': 'WBSSequence',
        'separator': 'str'
    }

    attribute_map = {
        'level': 'level',
        'length': 'length',
        'sequence': 'sequence',
        'separator': 'separator'
    }

    def __init__(self, level=None, length=None, sequence=None, separator=None):  # noqa: E501
        """WBSCodeMask - a model defined in Swagger"""  # noqa: E501

        self._level = None
        self._length = None
        self._sequence = None
        self._separator = None
        self.discriminator = None

        if level is not None:
            self.level = level
        if length is not None:
            self.length = length
        if sequence is not None:
            self.sequence = sequence
        if separator is not None:
            self.separator = separator

    @property
    def level(self):
        """Gets the level of this WBSCodeMask.  # noqa: E501

        Mask level.  # noqa: E501

        :return: The level of this WBSCodeMask.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this WBSCodeMask.

        Mask level.  # noqa: E501

        :param level: The level of this WBSCodeMask.  # noqa: E501
        :type: int
        """
        if level is None:
            raise ValueError("Invalid value for `level`, must not be `None`")  # noqa: E501
        self._level = level
    @property
    def length(self):
        """Gets the length of this WBSCodeMask.  # noqa: E501

        The number of characters of the code string.  # noqa: E501

        :return: The length of this WBSCodeMask.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this WBSCodeMask.

        The number of characters of the code string.  # noqa: E501

        :param length: The length of this WBSCodeMask.  # noqa: E501
        :type: int
        """
        if length is None:
            raise ValueError("Invalid value for `length`, must not be `None`")  # noqa: E501
        self._length = length
    @property
    def sequence(self):
        """Gets the sequence of this WBSCodeMask.  # noqa: E501

        Specifies  the type of character of the code string.  # noqa: E501

        :return: The sequence of this WBSCodeMask.  # noqa: E501
        :rtype: WBSSequence
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this WBSCodeMask.

        Specifies  the type of character of the code string.  # noqa: E501

        :param sequence: The sequence of this WBSCodeMask.  # noqa: E501
        :type: WBSSequence
        """
        if sequence is None:
            raise ValueError("Invalid value for `sequence`, must not be `None`")  # noqa: E501
        self._sequence = sequence
    @property
    def separator(self):
        """Gets the separator of this WBSCodeMask.  # noqa: E501

        Specifies the separator of the code string. Default value is Period.  # noqa: E501

        :return: The separator of this WBSCodeMask.  # noqa: E501
        :rtype: str
        """
        return self._separator

    @separator.setter
    def separator(self, separator):
        """Sets the separator of this WBSCodeMask.

        Specifies the separator of the code string. Default value is Period.  # noqa: E501

        :param separator: The separator of this WBSCodeMask.  # noqa: E501
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
        if not isinstance(other, WBSCodeMask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
