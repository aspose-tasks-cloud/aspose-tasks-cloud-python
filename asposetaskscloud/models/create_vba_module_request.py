# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="CreateVbaModuleRequest.py">
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


class CreateVbaModuleRequest(object):
    """Represents the body of a request that creates a new VBA module.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'type': 'VbaModuleType',
        'source_code': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'source_code': 'sourceCode'
    }

    def __init__(self, name=None, type=None, source_code=None):  # noqa: E501
        """CreateVbaModuleRequest - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._type = None
        self._source_code = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if source_code is not None:
            self.source_code = source_code

    @property
    def name(self):
        """Gets the name of this CreateVbaModuleRequest.  # noqa: E501

        Gets or sets the name of the VBA module to create.  # noqa: E501

        :return: The name of this CreateVbaModuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateVbaModuleRequest.

        Gets or sets the name of the VBA module to create.  # noqa: E501

        :param name: The name of this CreateVbaModuleRequest.  # noqa: E501
        :type: str
        """
        self._name = name
    @property
    def type(self):
        """Gets the type of this CreateVbaModuleRequest.  # noqa: E501

        Gets or sets the type of the VBA module to create. Only ProceduralModule and ClassModule can be created; other values are rejected.  # noqa: E501

        :return: The type of this CreateVbaModuleRequest.  # noqa: E501
        :rtype: VbaModuleType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateVbaModuleRequest.

        Gets or sets the type of the VBA module to create. Only ProceduralModule and ClassModule can be created; other values are rejected.  # noqa: E501

        :param type: The type of this CreateVbaModuleRequest.  # noqa: E501
        :type: VbaModuleType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type
    @property
    def source_code(self):
        """Gets the source_code of this CreateVbaModuleRequest.  # noqa: E501

        Gets or sets the source code to store in the new VBA module.  # noqa: E501

        :return: The source_code of this CreateVbaModuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._source_code

    @source_code.setter
    def source_code(self, source_code):
        """Sets the source_code of this CreateVbaModuleRequest.

        Gets or sets the source code to store in the new VBA module.  # noqa: E501

        :param source_code: The source_code of this CreateVbaModuleRequest.  # noqa: E501
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
        if not isinstance(other, CreateVbaModuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
