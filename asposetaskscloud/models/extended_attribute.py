# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="ExtendedAttribute.py">
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


class ExtendedAttribute(object):
    """Represents extended attribute.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'field_id': 'str',
        'attribute_type': 'CustomFieldType',
        'value_guid': 'str',
        'lookup_value_id': 'int',
        'duration_value': 'Duration',
        'numeric_value': 'float',
        'date_value': 'datetime',
        'flag_value': 'bool',
        'text_value': 'str',
        'is_error_value': 'bool'
    }

    attribute_map = {
        'field_id': 'fieldId',
        'attribute_type': 'attributeType',
        'value_guid': 'valueGuid',
        'lookup_value_id': 'lookupValueId',
        'duration_value': 'durationValue',
        'numeric_value': 'numericValue',
        'date_value': 'dateValue',
        'flag_value': 'flagValue',
        'text_value': 'textValue',
        'is_error_value': 'isErrorValue'
    }

    def __init__(self, field_id=None, attribute_type=None, value_guid=None, lookup_value_id=None, duration_value=None, numeric_value=None, date_value=None, flag_value=None, text_value=None, is_error_value=None):  # noqa: E501
        """ExtendedAttribute - a model defined in Swagger"""  # noqa: E501

        self._field_id = None
        self._attribute_type = None
        self._value_guid = None
        self._lookup_value_id = None
        self._duration_value = None
        self._numeric_value = None
        self._date_value = None
        self._flag_value = None
        self._text_value = None
        self._is_error_value = None
        self.discriminator = None

        if field_id is not None:
            self.field_id = field_id
        if attribute_type is not None:
            self.attribute_type = attribute_type
        if value_guid is not None:
            self.value_guid = value_guid
        if lookup_value_id is not None:
            self.lookup_value_id = lookup_value_id
        if duration_value is not None:
            self.duration_value = duration_value
        if numeric_value is not None:
            self.numeric_value = numeric_value
        if date_value is not None:
            self.date_value = date_value
        if flag_value is not None:
            self.flag_value = flag_value
        if text_value is not None:
            self.text_value = text_value
        if is_error_value is not None:
            self.is_error_value = is_error_value

    @property
    def field_id(self):
        """Gets the field_id of this ExtendedAttribute.  # noqa: E501

        Gets or sets the id of a field.  # noqa: E501

        :return: The field_id of this ExtendedAttribute.  # noqa: E501
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this ExtendedAttribute.

        Gets or sets the id of a field.  # noqa: E501

        :param field_id: The field_id of this ExtendedAttribute.  # noqa: E501
        :type: str
        """
        self._field_id = field_id
    @property
    def attribute_type(self):
        """Gets the attribute_type of this ExtendedAttribute.  # noqa: E501

        Gets the type of a custom field.  # noqa: E501

        :return: The attribute_type of this ExtendedAttribute.  # noqa: E501
        :rtype: CustomFieldType
        """
        return self._attribute_type

    @attribute_type.setter
    def attribute_type(self, attribute_type):
        """Sets the attribute_type of this ExtendedAttribute.

        Gets the type of a custom field.  # noqa: E501

        :param attribute_type: The attribute_type of this ExtendedAttribute.  # noqa: E501
        :type: CustomFieldType
        """
        if attribute_type is None:
            raise ValueError("Invalid value for `attribute_type`, must not be `None`")  # noqa: E501
        self._attribute_type = attribute_type
    @property
    def value_guid(self):
        """Gets the value_guid of this ExtendedAttribute.  # noqa: E501

        Gets or sets the guid of a value.  # noqa: E501

        :return: The value_guid of this ExtendedAttribute.  # noqa: E501
        :rtype: str
        """
        return self._value_guid

    @value_guid.setter
    def value_guid(self, value_guid):
        """Sets the value_guid of this ExtendedAttribute.

        Gets or sets the guid of a value.  # noqa: E501

        :param value_guid: The value_guid of this ExtendedAttribute.  # noqa: E501
        :type: str
        """
        self._value_guid = value_guid
    @property
    def lookup_value_id(self):
        """Gets the lookup_value_id of this ExtendedAttribute.  # noqa: E501

        Gets or sets Id of the lookup value (if value is lookup value)  # noqa: E501

        :return: The lookup_value_id of this ExtendedAttribute.  # noqa: E501
        :rtype: int
        """
        return self._lookup_value_id

    @lookup_value_id.setter
    def lookup_value_id(self, lookup_value_id):
        """Sets the lookup_value_id of this ExtendedAttribute.

        Gets or sets Id of the lookup value (if value is lookup value)  # noqa: E501

        :param lookup_value_id: The lookup_value_id of this ExtendedAttribute.  # noqa: E501
        :type: int
        """
        self._lookup_value_id = lookup_value_id
    @property
    def duration_value(self):
        """Gets the duration_value of this ExtendedAttribute.  # noqa: E501

        Gets or sets value for attributes with 'Duration' type.  # noqa: E501

        :return: The duration_value of this ExtendedAttribute.  # noqa: E501
        :rtype: Duration
        """
        return self._duration_value

    @duration_value.setter
    def duration_value(self, duration_value):
        """Sets the duration_value of this ExtendedAttribute.

        Gets or sets value for attributes with 'Duration' type.  # noqa: E501

        :param duration_value: The duration_value of this ExtendedAttribute.  # noqa: E501
        :type: Duration
        """
        self._duration_value = duration_value
    @property
    def numeric_value(self):
        """Gets the numeric_value of this ExtendedAttribute.  # noqa: E501

        Gets or sets a value for attributes with numeric types (Cost, Number).  # noqa: E501

        :return: The numeric_value of this ExtendedAttribute.  # noqa: E501
        :rtype: float
        """
        return self._numeric_value

    @numeric_value.setter
    def numeric_value(self, numeric_value):
        """Sets the numeric_value of this ExtendedAttribute.

        Gets or sets a value for attributes with numeric types (Cost, Number).  # noqa: E501

        :param numeric_value: The numeric_value of this ExtendedAttribute.  # noqa: E501
        :type: float
        """
        if numeric_value is None:
            raise ValueError("Invalid value for `numeric_value`, must not be `None`")  # noqa: E501
        self._numeric_value = numeric_value
    @property
    def date_value(self):
        """Gets the date_value of this ExtendedAttribute.  # noqa: E501

        Gets or sets a value for attributes with date types (Date, Start, Finish).  # noqa: E501

        :return: The date_value of this ExtendedAttribute.  # noqa: E501
        :rtype: datetime
        """
        return self._date_value

    @date_value.setter
    def date_value(self, date_value):
        """Sets the date_value of this ExtendedAttribute.

        Gets or sets a value for attributes with date types (Date, Start, Finish).  # noqa: E501

        :param date_value: The date_value of this ExtendedAttribute.  # noqa: E501
        :type: datetime
        """
        if date_value is None:
            raise ValueError("Invalid value for `date_value`, must not be `None`")  # noqa: E501
        self._date_value = date_value
    @property
    def flag_value(self):
        """Gets the flag_value of this ExtendedAttribute.  # noqa: E501

        Gets or sets a value indicating whether a flag is set for an attribute with 'Flag' type.  # noqa: E501

        :return: The flag_value of this ExtendedAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._flag_value

    @flag_value.setter
    def flag_value(self, flag_value):
        """Sets the flag_value of this ExtendedAttribute.

        Gets or sets a value indicating whether a flag is set for an attribute with 'Flag' type.  # noqa: E501

        :param flag_value: The flag_value of this ExtendedAttribute.  # noqa: E501
        :type: bool
        """
        if flag_value is None:
            raise ValueError("Invalid value for `flag_value`, must not be `None`")  # noqa: E501
        self._flag_value = flag_value
    @property
    def text_value(self):
        """Gets the text_value of this ExtendedAttribute.  # noqa: E501

        Gets or sets a value for attributes with 'Text' type.  # noqa: E501

        :return: The text_value of this ExtendedAttribute.  # noqa: E501
        :rtype: str
        """
        return self._text_value

    @text_value.setter
    def text_value(self, text_value):
        """Sets the text_value of this ExtendedAttribute.

        Gets or sets a value for attributes with 'Text' type.  # noqa: E501

        :param text_value: The text_value of this ExtendedAttribute.  # noqa: E501
        :type: str
        """
        self._text_value = text_value
    @property
    def is_error_value(self):
        """Gets the is_error_value of this ExtendedAttribute.  # noqa: E501

        Gets whether calculation of extended attribute's value resulted in an error.               # noqa: E501

        :return: The is_error_value of this ExtendedAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._is_error_value

    @is_error_value.setter
    def is_error_value(self, is_error_value):
        """Sets the is_error_value of this ExtendedAttribute.

        Gets whether calculation of extended attribute's value resulted in an error.               # noqa: E501

        :param is_error_value: The is_error_value of this ExtendedAttribute.  # noqa: E501
        :type: bool
        """
        if is_error_value is None:
            raise ValueError("Invalid value for `is_error_value`, must not be `None`")  # noqa: E501
        self._is_error_value = is_error_value
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
        if not isinstance(other, ExtendedAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
