# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="WorkingTime.py">
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


class WorkingTime(object):
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
        'from_time': 'datetime',
        'to_time': 'datetime'
    }

    attribute_map = {
        'from_time': 'fromTime',
        'to_time': 'toTime'
    }

    def __init__(self, from_time=None, to_time=None):  # noqa: E501
        """WorkingTime - a model defined in Swagger"""  # noqa: E501

        self._from_time = None
        self._to_time = None
        self.discriminator = None

        if from_time is not None:
            self.from_time = from_time
        if to_time is not None:
            self.to_time = to_time

    @property
    def from_time(self):
        """Gets the from_time of this WorkingTime.  # noqa: E501

        Returns or sets the beginning of a working time. Read/write DateTime.  # noqa: E501

        :return: The from_time of this WorkingTime.  # noqa: E501
        :rtype: datetime
        """
        return self._from_time

    @from_time.setter
    def from_time(self, from_time):
        """Sets the from_time of this WorkingTime.

        Returns or sets the beginning of a working time. Read/write DateTime.  # noqa: E501

        :param from_time: The from_time of this WorkingTime.  # noqa: E501
        :type: datetime
        """
        if from_time is None:
            raise ValueError("Invalid value for `from_time`, must not be `None`")  # noqa: E501
        self._from_time = from_time
    @property
    def to_time(self):
        """Gets the to_time of this WorkingTime.  # noqa: E501

        Returns or sets the end of a working time. Read/write DateTime.  # noqa: E501

        :return: The to_time of this WorkingTime.  # noqa: E501
        :rtype: datetime
        """
        return self._to_time

    @to_time.setter
    def to_time(self, to_time):
        """Sets the to_time of this WorkingTime.

        Returns or sets the end of a working time. Read/write DateTime.  # noqa: E501

        :param to_time: The to_time of this WorkingTime.  # noqa: E501
        :type: datetime
        """
        if to_time is None:
            raise ValueError("Invalid value for `to_time`, must not be `None`")  # noqa: E501
        self._to_time = to_time
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
        if not isinstance(other, WorkingTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
