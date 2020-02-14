# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="OutlineValue.py">
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


class OutlineValue(object):
    """Represents an outline value.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'value_id': 'int',
        'field_guid': 'str',
        'type': 'OutlineValueType',
        'parent_value_id': 'int',
        'value': 'str',
        'description': 'str',
        'is_collapsed': 'bool'
    }

    attribute_map = {
        'value_id': 'valueId',
        'field_guid': 'fieldGuid',
        'type': 'type',
        'parent_value_id': 'parentValueId',
        'value': 'value',
        'description': 'description',
        'is_collapsed': 'isCollapsed'
    }

    def __init__(self, value_id=None, field_guid=None, type=None, parent_value_id=None, value=None, description=None, is_collapsed=None):  # noqa: E501
        """OutlineValue - a model defined in Swagger"""  # noqa: E501

        self._value_id = None
        self._field_guid = None
        self._type = None
        self._parent_value_id = None
        self._value = None
        self._description = None
        self._is_collapsed = None
        self.discriminator = None

        if value_id is not None:
            self.value_id = value_id
        if field_guid is not None:
            self.field_guid = field_guid
        if type is not None:
            self.type = type
        if parent_value_id is not None:
            self.parent_value_id = parent_value_id
        if value is not None:
            self.value = value
        if description is not None:
            self.description = description
        if is_collapsed is not None:
            self.is_collapsed = is_collapsed

    @property
    def value_id(self):
        """Gets the value_id of this OutlineValue.  # noqa: E501

        The unique Id of an outline code value within a project.  # noqa: E501

        :return: The value_id of this OutlineValue.  # noqa: E501
        :rtype: int
        """
        return self._value_id

    @value_id.setter
    def value_id(self, value_id):
        """Sets the value_id of this OutlineValue.

        The unique Id of an outline code value within a project.  # noqa: E501

        :param value_id: The value_id of this OutlineValue.  # noqa: E501
        :type: int
        """
        if value_id is None:
            raise ValueError("Invalid value for `value_id`, must not be `None`")  # noqa: E501
        self._value_id = value_id
    @property
    def field_guid(self):
        """Gets the field_guid of this OutlineValue.  # noqa: E501

        The Guid of an outline code value.  # noqa: E501

        :return: The field_guid of this OutlineValue.  # noqa: E501
        :rtype: str
        """
        return self._field_guid

    @field_guid.setter
    def field_guid(self, field_guid):
        """Sets the field_guid of this OutlineValue.

        The Guid of an outline code value.  # noqa: E501

        :param field_guid: The field_guid of this OutlineValue.  # noqa: E501
        :type: str
        """
        self._field_guid = field_guid
    @property
    def type(self):
        """Gets the type of this OutlineValue.  # noqa: E501

        The outline code type.  # noqa: E501

        :return: The type of this OutlineValue.  # noqa: E501
        :rtype: OutlineValueType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OutlineValue.

        The outline code type.  # noqa: E501

        :param type: The type of this OutlineValue.  # noqa: E501
        :type: OutlineValueType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type
    @property
    def parent_value_id(self):
        """Gets the parent_value_id of this OutlineValue.  # noqa: E501

        The Id of a parent node of an outline code.  # noqa: E501

        :return: The parent_value_id of this OutlineValue.  # noqa: E501
        :rtype: int
        """
        return self._parent_value_id

    @parent_value_id.setter
    def parent_value_id(self, parent_value_id):
        """Sets the parent_value_id of this OutlineValue.

        The Id of a parent node of an outline code.  # noqa: E501

        :param parent_value_id: The parent_value_id of this OutlineValue.  # noqa: E501
        :type: int
        """
        if parent_value_id is None:
            raise ValueError("Invalid value for `parent_value_id`, must not be `None`")  # noqa: E501
        self._parent_value_id = parent_value_id
    @property
    def value(self):
        """Gets the value of this OutlineValue.  # noqa: E501

        The actual value.  # noqa: E501

        :return: The value of this OutlineValue.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this OutlineValue.

        The actual value.  # noqa: E501

        :param value: The value of this OutlineValue.  # noqa: E501
        :type: str
        """
        self._value = value
    @property
    def description(self):
        """Gets the description of this OutlineValue.  # noqa: E501

        The description of an outline value.  # noqa: E501

        :return: The description of this OutlineValue.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OutlineValue.

        The description of an outline value.  # noqa: E501

        :param description: The description of this OutlineValue.  # noqa: E501
        :type: str
        """
        self._description = description
    @property
    def is_collapsed(self):
        """Gets the is_collapsed of this OutlineValue.  # noqa: E501

        Determines whether outline value is collapsed or not.  # noqa: E501

        :return: The is_collapsed of this OutlineValue.  # noqa: E501
        :rtype: bool
        """
        return self._is_collapsed

    @is_collapsed.setter
    def is_collapsed(self, is_collapsed):
        """Sets the is_collapsed of this OutlineValue.

        Determines whether outline value is collapsed or not.  # noqa: E501

        :param is_collapsed: The is_collapsed of this OutlineValue.  # noqa: E501
        :type: bool
        """
        if is_collapsed is None:
            raise ValueError("Invalid value for `is_collapsed`, must not be `None`")  # noqa: E501
        self._is_collapsed = is_collapsed
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
        if not isinstance(other, OutlineValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
