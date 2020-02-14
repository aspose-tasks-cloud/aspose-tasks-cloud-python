# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="Duration.py">
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


class Duration(object):
    """Represents a duration value.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'time_span': 'str',
        'time_unit': 'TimeUnitType'
    }

    attribute_map = {
        'time_span': 'timeSpan',
        'time_unit': 'timeUnit'
    }

    def __init__(self, time_span=None, time_unit=None):  # noqa: E501
        """Duration - a model defined in Swagger"""  # noqa: E501

        self._time_span = None
        self._time_unit = None
        self.discriminator = None

        if time_span is not None:
            self.time_span = time_span
        if time_unit is not None:
            self.time_unit = time_unit

    @property
    def time_span(self):
        """Gets the time_span of this Duration.  # noqa: E501

        Gets or sets the time interval of duration.  # noqa: E501

        :return: The time_span of this Duration.  # noqa: E501
        :rtype: str
        """
        return self._time_span

    @time_span.setter
    def time_span(self, time_span):
        """Sets the time_span of this Duration.

        Gets or sets the time interval of duration.  # noqa: E501

        :param time_span: The time_span of this Duration.  # noqa: E501
        :type: str
        """
        if time_span is None:
            raise ValueError("Invalid value for `time_span`, must not be `None`")  # noqa: E501
        self._time_span = time_span
    @property
    def time_unit(self):
        """Gets the time_unit of this Duration.  # noqa: E501

        Gets or sets the time units which will be used to display duration in MS Project.  # noqa: E501

        :return: The time_unit of this Duration.  # noqa: E501
        :rtype: TimeUnitType
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        """Sets the time_unit of this Duration.

        Gets or sets the time units which will be used to display duration in MS Project.  # noqa: E501

        :param time_unit: The time_unit of this Duration.  # noqa: E501
        :type: TimeUnitType
        """
        if time_unit is None:
            raise ValueError("Invalid value for `time_unit`, must not be `None`")  # noqa: E501
        self._time_unit = time_unit
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
        if not isinstance(other, Duration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
