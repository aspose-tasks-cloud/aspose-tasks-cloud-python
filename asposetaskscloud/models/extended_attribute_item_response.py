# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="ExtendedAttributeItemResponse.py">
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


class ExtendedAttributeItemResponse(object):
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
        'extended_attribute': 'ExtendedAttributeItem'
    }

    attribute_map = {
        'extended_attribute': 'extendedAttribute'
    }

    def __init__(self, extended_attribute=None):  # noqa: E501
        """ExtendedAttributeItemResponse - a model defined in Swagger"""  # noqa: E501

        self._extended_attribute = None
        self.discriminator = None

        if extended_attribute is not None:
            self.extended_attribute = extended_attribute

    @property
    def extended_attribute(self):
        """Gets the extended_attribute of this ExtendedAttributeItemResponse.  # noqa: E501

        Extended attribute definition info.  # noqa: E501

        :return: The extended_attribute of this ExtendedAttributeItemResponse.  # noqa: E501
        :rtype: ExtendedAttributeItem
        """
        return self._extended_attribute

    @extended_attribute.setter
    def extended_attribute(self, extended_attribute):
        """Sets the extended_attribute of this ExtendedAttributeItemResponse.

        Extended attribute definition info.  # noqa: E501

        :param extended_attribute: The extended_attribute of this ExtendedAttributeItemResponse.  # noqa: E501
        :type: ExtendedAttributeItem
        """
        self._extended_attribute = extended_attribute
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
        if not isinstance(other, ExtendedAttributeItemResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
