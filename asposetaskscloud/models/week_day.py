# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="WeekDay.py">
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


class WeekDay(object):
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
        'day_type': 'DayType',
        'day_working': 'bool',
        'from_date': 'datetime',
        'to_date': 'datetime',
        'working_times': 'list[WorkingTime]'
    }

    attribute_map = {
        'day_type': 'dayType',
        'day_working': 'dayWorking',
        'from_date': 'fromDate',
        'to_date': 'toDate',
        'working_times': 'workingTimes'
    }

    def __init__(self, day_type=None, day_working=None, from_date=None, to_date=None, working_times=None):  # noqa: E501
        """WeekDay - a model defined in Swagger"""  # noqa: E501

        self._day_type = None
        self._day_working = None
        self._from_date = None
        self._to_date = None
        self._working_times = None
        self.discriminator = None

        if day_type is not None:
            self.day_type = day_type
        if day_working is not None:
            self.day_working = day_working
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date
        if working_times is not None:
            self.working_times = working_times

    @property
    def day_type(self):
        """Gets the day_type of this WeekDay.  # noqa: E501

        Returns or sets the type of a day.  # noqa: E501

        :return: The day_type of this WeekDay.  # noqa: E501
        :rtype: DayType
        """
        return self._day_type

    @day_type.setter
    def day_type(self, day_type):
        """Sets the day_type of this WeekDay.

        Returns or sets the type of a day.  # noqa: E501

        :param day_type: The day_type of this WeekDay.  # noqa: E501
        :type: DayType
        """
        if day_type is None:
            raise ValueError("Invalid value for `day_type`, must not be `None`")  # noqa: E501
        self._day_type = day_type
    @property
    def day_working(self):
        """Gets the day_working of this WeekDay.  # noqa: E501

        Determines whether the specified date or day type is working.  # noqa: E501

        :return: The day_working of this WeekDay.  # noqa: E501
        :rtype: bool
        """
        return self._day_working

    @day_working.setter
    def day_working(self, day_working):
        """Sets the day_working of this WeekDay.

        Determines whether the specified date or day type is working.  # noqa: E501

        :param day_working: The day_working of this WeekDay.  # noqa: E501
        :type: bool
        """
        if day_working is None:
            raise ValueError("Invalid value for `day_working`, must not be `None`")  # noqa: E501
        self._day_working = day_working
    @property
    def from_date(self):
        """Gets the from_date of this WeekDay.  # noqa: E501

        Returns or sets the beginning of an exception time.  # noqa: E501

        :return: The from_date of this WeekDay.  # noqa: E501
        :rtype: datetime
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this WeekDay.

        Returns or sets the beginning of an exception time.  # noqa: E501

        :param from_date: The from_date of this WeekDay.  # noqa: E501
        :type: datetime
        """
        if from_date is None:
            raise ValueError("Invalid value for `from_date`, must not be `None`")  # noqa: E501
        self._from_date = from_date
    @property
    def to_date(self):
        """Gets the to_date of this WeekDay.  # noqa: E501

        Returns or sets the end of an exception time.  # noqa: E501

        :return: The to_date of this WeekDay.  # noqa: E501
        :rtype: datetime
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this WeekDay.

        Returns or sets the end of an exception time.  # noqa: E501

        :param to_date: The to_date of this WeekDay.  # noqa: E501
        :type: datetime
        """
        if to_date is None:
            raise ValueError("Invalid value for `to_date`, must not be `None`")  # noqa: E501
        self._to_date = to_date
    @property
    def working_times(self):
        """Gets the working_times of this WeekDay.  # noqa: E501

        The collection of working times that define the time worked on the weekday.  # noqa: E501

        :return: The working_times of this WeekDay.  # noqa: E501
        :rtype: list[WorkingTime]
        """
        return self._working_times

    @working_times.setter
    def working_times(self, working_times):
        """Sets the working_times of this WeekDay.

        The collection of working times that define the time worked on the weekday.  # noqa: E501

        :param working_times: The working_times of this WeekDay.  # noqa: E501
        :type: list[WorkingTime]
        """
        self._working_times = working_times
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
        if not isinstance(other, WeekDay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
