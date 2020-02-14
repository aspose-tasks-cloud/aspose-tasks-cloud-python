# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="Value.py">
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


class Value(object):
    """Represents a lookup value of an extended attribute.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'val': 'str',
        'date_time_value': 'datetime',
        'duration_value': 'int',
        'description': 'str',
        'phonetic': 'str'
    }

    attribute_map = {
        'id': 'id',
        'val': 'val',
        'date_time_value': 'dateTimeValue',
        'duration_value': 'durationValue',
        'description': 'description',
        'phonetic': 'phonetic'
    }

    def __init__(self, id=None, val=None, date_time_value=None, duration_value=None, description=None, phonetic=None):  # noqa: E501
        """Value - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._val = None
        self._date_time_value = None
        self._duration_value = None
        self._description = None
        self._phonetic = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if val is not None:
            self.val = val
        if date_time_value is not None:
            self.date_time_value = date_time_value
        if duration_value is not None:
            self.duration_value = duration_value
        if description is not None:
            self.description = description
        if phonetic is not None:
            self.phonetic = phonetic

    @property
    def id(self):
        """Gets the id of this Value.  # noqa: E501

        The unique Id of a value across a project.  # noqa: E501

        :return: The id of this Value.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Value.

        The unique Id of a value across a project.  # noqa: E501

        :param id: The id of this Value.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        self._id = id
    @property
    def val(self):
        """Gets the val of this Value.  # noqa: E501

        The actual value.  # noqa: E501

        :return: The val of this Value.  # noqa: E501
        :rtype: str
        """
        return self._val

    @val.setter
    def val(self, val):
        """Sets the val of this Value.

        The actual value.  # noqa: E501

        :param val: The val of this Value.  # noqa: E501
        :type: str
        """
        self._val = val
    @property
    def date_time_value(self):
        """Gets the date_time_value of this Value.  # noqa: E501

        The value in case of datetime type  # noqa: E501

        :return: The date_time_value of this Value.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time_value

    @date_time_value.setter
    def date_time_value(self, date_time_value):
        """Sets the date_time_value of this Value.

        The value in case of datetime type  # noqa: E501

        :param date_time_value: The date_time_value of this Value.  # noqa: E501
        :type: datetime
        """
        self._date_time_value = date_time_value
    @property
    def duration_value(self):
        """Gets the duration_value of this Value.  # noqa: E501

        The value in case of duration type  # noqa: E501

        :return: The duration_value of this Value.  # noqa: E501
        :rtype: int
        """
        return self._duration_value

    @duration_value.setter
    def duration_value(self, duration_value):
        """Sets the duration_value of this Value.

        The value in case of duration type  # noqa: E501

        :param duration_value: The duration_value of this Value.  # noqa: E501
        :type: int
        """
        self._duration_value = duration_value
    @property
    def description(self):
        """Gets the description of this Value.  # noqa: E501

        The description of a value.  # noqa: E501

        :return: The description of this Value.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Value.

        The description of a value.  # noqa: E501

        :param description: The description of this Value.  # noqa: E501
        :type: str
        """
        self._description = description
    @property
    def phonetic(self):
        """Gets the phonetic of this Value.  # noqa: E501

        The phonetic information about custom field name.  # noqa: E501

        :return: The phonetic of this Value.  # noqa: E501
        :rtype: str
        """
        return self._phonetic

    @phonetic.setter
    def phonetic(self, phonetic):
        """Sets the phonetic of this Value.

        The phonetic information about custom field name.  # noqa: E501

        :param phonetic: The phonetic of this Value.  # noqa: E501
        :type: str
        """
        self._phonetic = phonetic
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
        if not isinstance(other, Value):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
