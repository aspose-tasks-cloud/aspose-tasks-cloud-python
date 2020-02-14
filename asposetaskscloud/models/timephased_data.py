# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="TimephasedData.py">
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


class TimephasedData(object):
    """Represents a time phased data.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'uid': 'int',
        'start': 'datetime',
        'finish': 'datetime',
        'unit': 'TimeUnitType',
        'value': 'str',
        'timephased_data_type': 'TimephasedDataType'
    }

    attribute_map = {
        'uid': 'uid',
        'start': 'start',
        'finish': 'finish',
        'unit': 'unit',
        'value': 'value',
        'timephased_data_type': 'timephasedDataType'
    }

    def __init__(self, uid=None, start=None, finish=None, unit=None, value=None, timephased_data_type=None):  # noqa: E501
        """TimephasedData - a model defined in Swagger"""  # noqa: E501

        self._uid = None
        self._start = None
        self._finish = None
        self._unit = None
        self._value = None
        self._timephased_data_type = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if start is not None:
            self.start = start
        if finish is not None:
            self.finish = finish
        if unit is not None:
            self.unit = unit
        if value is not None:
            self.value = value
        if timephased_data_type is not None:
            self.timephased_data_type = timephased_data_type

    @property
    def uid(self):
        """Gets the uid of this TimephasedData.  # noqa: E501

        The unique identifier of a timephased data  # noqa: E501

        :return: The uid of this TimephasedData.  # noqa: E501
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this TimephasedData.

        The unique identifier of a timephased data  # noqa: E501

        :param uid: The uid of this TimephasedData.  # noqa: E501
        :type: int
        """
        if uid is None:
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501
        self._uid = uid
    @property
    def start(self):
        """Gets the start of this TimephasedData.  # noqa: E501

        The start date of a timephased data period.  # noqa: E501

        :return: The start of this TimephasedData.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this TimephasedData.

        The start date of a timephased data period.  # noqa: E501

        :param start: The start of this TimephasedData.  # noqa: E501
        :type: datetime
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501
        self._start = start
    @property
    def finish(self):
        """Gets the finish of this TimephasedData.  # noqa: E501

        The finish date of a timephased data period.  # noqa: E501

        :return: The finish of this TimephasedData.  # noqa: E501
        :rtype: datetime
        """
        return self._finish

    @finish.setter
    def finish(self, finish):
        """Sets the finish of this TimephasedData.

        The finish date of a timephased data period.  # noqa: E501

        :param finish: The finish of this TimephasedData.  # noqa: E501
        :type: datetime
        """
        if finish is None:
            raise ValueError("Invalid value for `finish`, must not be `None`")  # noqa: E501
        self._finish = finish
    @property
    def unit(self):
        """Gets the unit of this TimephasedData.  # noqa: E501

        The time unit of a timephased data period.  # noqa: E501

        :return: The unit of this TimephasedData.  # noqa: E501
        :rtype: TimeUnitType
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this TimephasedData.

        The time unit of a timephased data period.  # noqa: E501

        :param unit: The unit of this TimephasedData.  # noqa: E501
        :type: TimeUnitType
        """
        if unit is None:
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501
        self._unit = unit
    @property
    def value(self):
        """Gets the value of this TimephasedData.  # noqa: E501

        The value per unit of time for a timephased data period.  # noqa: E501

        :return: The value of this TimephasedData.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TimephasedData.

        The value per unit of time for a timephased data period.  # noqa: E501

        :param value: The value of this TimephasedData.  # noqa: E501
        :type: str
        """
        self._value = value
    @property
    def timephased_data_type(self):
        """Gets the timephased_data_type of this TimephasedData.  # noqa: E501

        The type of a timephased data.  # noqa: E501

        :return: The timephased_data_type of this TimephasedData.  # noqa: E501
        :rtype: TimephasedDataType
        """
        return self._timephased_data_type

    @timephased_data_type.setter
    def timephased_data_type(self, timephased_data_type):
        """Sets the timephased_data_type of this TimephasedData.

        The type of a timephased data.  # noqa: E501

        :param timephased_data_type: The timephased_data_type of this TimephasedData.  # noqa: E501
        :type: TimephasedDataType
        """
        if timephased_data_type is None:
            raise ValueError("Invalid value for `timephased_data_type`, must not be `None`")  # noqa: E501
        self._timephased_data_type = timephased_data_type
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
        if not isinstance(other, TimephasedData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
