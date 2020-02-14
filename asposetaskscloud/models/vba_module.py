# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="VbaModule.py">
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


class VbaModule(object):
    """Represents a vba module 
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'attributes': 'list[VbaModuleAttribute]',
        'name': 'str',
        'source_code': 'str'
    }

    attribute_map = {
        'attributes': 'attributes',
        'name': 'name',
        'source_code': 'sourceCode'
    }

    def __init__(self, attributes=None, name=None, source_code=None):  # noqa: E501
        """VbaModule - a model defined in Swagger"""  # noqa: E501

        self._attributes = None
        self._name = None
        self._source_code = None
        self.discriminator = None

        if attributes is not None:
            self.attributes = attributes
        if name is not None:
            self.name = name
        if source_code is not None:
            self.source_code = source_code

    @property
    def attributes(self):
        """Gets the attributes of this VbaModule.  # noqa: E501

        Gets a collection of  VbaModuleAttributeCollection  # noqa: E501

        :return: The attributes of this VbaModule.  # noqa: E501
        :rtype: list[VbaModuleAttribute]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this VbaModule.

        Gets a collection of  VbaModuleAttributeCollection  # noqa: E501

        :param attributes: The attributes of this VbaModule.  # noqa: E501
        :type: list[VbaModuleAttribute]
        """
        self._attributes = attributes
    @property
    def name(self):
        """Gets the name of this VbaModule.  # noqa: E501

        Gets the name of the module.  # noqa: E501

        :return: The name of this VbaModule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VbaModule.

        Gets the name of the module.  # noqa: E501

        :param name: The name of this VbaModule.  # noqa: E501
        :type: str
        """
        self._name = name
    @property
    def source_code(self):
        """Gets the source_code of this VbaModule.  # noqa: E501

        Gets a source code of the module  # noqa: E501

        :return: The source_code of this VbaModule.  # noqa: E501
        :rtype: str
        """
        return self._source_code

    @source_code.setter
    def source_code(self, source_code):
        """Sets the source_code of this VbaModule.

        Gets a source code of the module  # noqa: E501

        :param source_code: The source_code of this VbaModule.  # noqa: E501
        :type: str
        """
        self._source_code = source_code
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
        if not isinstance(other, VbaModule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
