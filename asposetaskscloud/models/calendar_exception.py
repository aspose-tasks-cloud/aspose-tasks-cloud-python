# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="CalendarException.py">
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


class CalendarException(object):
    """Represent exceptional time periods in a calendar.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'index': 'int',
        'entered_by_occurrences': 'bool',
        'from_date': 'datetime',
        'to_date': 'datetime',
        'occurrences': 'int',
        'name': 'str',
        'type': 'CalendarExceptionType',
        'period': 'int',
        'days_of_week': 'list[DayType]',
        'month_item': 'MonthItemType',
        'month_position': 'MonthPosition',
        'month': 'Month',
        'month_day': 'int',
        'day_working': 'bool',
        'working_times': 'list[WorkingTime]'
    }

    attribute_map = {
        'index': 'index',
        'entered_by_occurrences': 'enteredByOccurrences',
        'from_date': 'fromDate',
        'to_date': 'toDate',
        'occurrences': 'occurrences',
        'name': 'name',
        'type': 'type',
        'period': 'period',
        'days_of_week': 'daysOfWeek',
        'month_item': 'monthItem',
        'month_position': 'monthPosition',
        'month': 'month',
        'month_day': 'monthDay',
        'day_working': 'dayWorking',
        'working_times': 'workingTimes'
    }

    def __init__(self, index=None, entered_by_occurrences=None, from_date=None, to_date=None, occurrences=None, name=None, type=None, period=None, days_of_week=None, month_item=None, month_position=None, month=None, month_day=None, day_working=None, working_times=None):  # noqa: E501
        """CalendarException - a model defined in Swagger"""  # noqa: E501

        self._index = None
        self._entered_by_occurrences = None
        self._from_date = None
        self._to_date = None
        self._occurrences = None
        self._name = None
        self._type = None
        self._period = None
        self._days_of_week = None
        self._month_item = None
        self._month_position = None
        self._month = None
        self._month_day = None
        self._day_working = None
        self._working_times = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if entered_by_occurrences is not None:
            self.entered_by_occurrences = entered_by_occurrences
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date
        if occurrences is not None:
            self.occurrences = occurrences
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if period is not None:
            self.period = period
        if days_of_week is not None:
            self.days_of_week = days_of_week
        if month_item is not None:
            self.month_item = month_item
        if month_position is not None:
            self.month_position = month_position
        if month is not None:
            self.month = month
        if month_day is not None:
            self.month_day = month_day
        if day_working is not None:
            self.day_working = day_working
        if working_times is not None:
            self.working_times = working_times

    @property
    def index(self):
        """Gets the index of this CalendarException.  # noqa: E501

        Index of the current item in the collection of calendar's exceptions.  # noqa: E501

        :return: The index of this CalendarException.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this CalendarException.

        Index of the current item in the collection of calendar's exceptions.  # noqa: E501

        :param index: The index of this CalendarException.  # noqa: E501
        :type: int
        """
        if index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501
        self._index = index
    @property
    def entered_by_occurrences(self):
        """Gets the entered_by_occurrences of this CalendarException.  # noqa: E501

        Determines whether the range of recurrence is defined by entering a number of occurrences. False specifies that the range of recurrence is defined by entering a finish date.  # noqa: E501

        :return: The entered_by_occurrences of this CalendarException.  # noqa: E501
        :rtype: bool
        """
        return self._entered_by_occurrences

    @entered_by_occurrences.setter
    def entered_by_occurrences(self, entered_by_occurrences):
        """Sets the entered_by_occurrences of this CalendarException.

        Determines whether the range of recurrence is defined by entering a number of occurrences. False specifies that the range of recurrence is defined by entering a finish date.  # noqa: E501

        :param entered_by_occurrences: The entered_by_occurrences of this CalendarException.  # noqa: E501
        :type: bool
        """
        if entered_by_occurrences is None:
            raise ValueError("Invalid value for `entered_by_occurrences`, must not be `None`")  # noqa: E501
        self._entered_by_occurrences = entered_by_occurrences
    @property
    def from_date(self):
        """Gets the from_date of this CalendarException.  # noqa: E501

        The beginning of the exception time.  # noqa: E501

        :return: The from_date of this CalendarException.  # noqa: E501
        :rtype: datetime
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this CalendarException.

        The beginning of the exception time.  # noqa: E501

        :param from_date: The from_date of this CalendarException.  # noqa: E501
        :type: datetime
        """
        if from_date is None:
            raise ValueError("Invalid value for `from_date`, must not be `None`")  # noqa: E501
        self._from_date = from_date
    @property
    def to_date(self):
        """Gets the to_date of this CalendarException.  # noqa: E501

        The end of the exception time.  # noqa: E501

        :return: The to_date of this CalendarException.  # noqa: E501
        :rtype: datetime
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this CalendarException.

        The end of the exception time.  # noqa: E501

        :param to_date: The to_date of this CalendarException.  # noqa: E501
        :type: datetime
        """
        if to_date is None:
            raise ValueError("Invalid value for `to_date`, must not be `None`")  # noqa: E501
        self._to_date = to_date
    @property
    def occurrences(self):
        """Gets the occurrences of this CalendarException.  # noqa: E501

        The number of occurrences for which the calendar exception is valid.  # noqa: E501

        :return: The occurrences of this CalendarException.  # noqa: E501
        :rtype: int
        """
        return self._occurrences

    @occurrences.setter
    def occurrences(self, occurrences):
        """Sets the occurrences of this CalendarException.

        The number of occurrences for which the calendar exception is valid.  # noqa: E501

        :param occurrences: The occurrences of this CalendarException.  # noqa: E501
        :type: int
        """
        if occurrences is None:
            raise ValueError("Invalid value for `occurrences`, must not be `None`")  # noqa: E501
        self._occurrences = occurrences
    @property
    def name(self):
        """Gets the name of this CalendarException.  # noqa: E501

        The name of the exception.  # noqa: E501

        :return: The name of this CalendarException.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CalendarException.

        The name of the exception.  # noqa: E501

        :param name: The name of this CalendarException.  # noqa: E501
        :type: str
        """
        self._name = name
    @property
    def type(self):
        """Gets the type of this CalendarException.  # noqa: E501

        The exception type.  # noqa: E501

        :return: The type of this CalendarException.  # noqa: E501
        :rtype: CalendarExceptionType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CalendarException.

        The exception type.  # noqa: E501

        :param type: The type of this CalendarException.  # noqa: E501
        :type: CalendarExceptionType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type
    @property
    def period(self):
        """Gets the period of this CalendarException.  # noqa: E501

        The period of recurrence for the exception.  # noqa: E501

        :return: The period of this CalendarException.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this CalendarException.

        The period of recurrence for the exception.  # noqa: E501

        :param period: The period of this CalendarException.  # noqa: E501
        :type: int
        """
        if period is None:
            raise ValueError("Invalid value for `period`, must not be `None`")  # noqa: E501
        self._period = period
    @property
    def days_of_week(self):
        """Gets the days_of_week of this CalendarException.  # noqa: E501

        The days of the week on which the exception is valid.  # noqa: E501

        :return: The days_of_week of this CalendarException.  # noqa: E501
        :rtype: list[DayType]
        """
        return self._days_of_week

    @days_of_week.setter
    def days_of_week(self, days_of_week):
        """Sets the days_of_week of this CalendarException.

        The days of the week on which the exception is valid.  # noqa: E501

        :param days_of_week: The days_of_week of this CalendarException.  # noqa: E501
        :type: list[DayType]
        """
        self._days_of_week = days_of_week
    @property
    def month_item(self):
        """Gets the month_item of this CalendarException.  # noqa: E501

        The month item for which an exception recurrence is scheduled.  # noqa: E501

        :return: The month_item of this CalendarException.  # noqa: E501
        :rtype: MonthItemType
        """
        return self._month_item

    @month_item.setter
    def month_item(self, month_item):
        """Sets the month_item of this CalendarException.

        The month item for which an exception recurrence is scheduled.  # noqa: E501

        :param month_item: The month_item of this CalendarException.  # noqa: E501
        :type: MonthItemType
        """
        if month_item is None:
            raise ValueError("Invalid value for `month_item`, must not be `None`")  # noqa: E501
        self._month_item = month_item
    @property
    def month_position(self):
        """Gets the month_position of this CalendarException.  # noqa: E501

        The position of a month item within a month.  # noqa: E501

        :return: The month_position of this CalendarException.  # noqa: E501
        :rtype: MonthPosition
        """
        return self._month_position

    @month_position.setter
    def month_position(self, month_position):
        """Sets the month_position of this CalendarException.

        The position of a month item within a month.  # noqa: E501

        :param month_position: The month_position of this CalendarException.  # noqa: E501
        :type: MonthPosition
        """
        if month_position is None:
            raise ValueError("Invalid value for `month_position`, must not be `None`")  # noqa: E501
        self._month_position = month_position
    @property
    def month(self):
        """Gets the month of this CalendarException.  # noqa: E501

        The month for which an exception recurrence is scheduled.  # noqa: E501

        :return: The month of this CalendarException.  # noqa: E501
        :rtype: Month
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this CalendarException.

        The month for which an exception recurrence is scheduled.  # noqa: E501

        :param month: The month of this CalendarException.  # noqa: E501
        :type: Month
        """
        if month is None:
            raise ValueError("Invalid value for `month`, must not be `None`")  # noqa: E501
        self._month = month
    @property
    def month_day(self):
        """Gets the month_day of this CalendarException.  # noqa: E501

        The day of a month on which an exception recurrence is scheduled.  # noqa: E501

        :return: The month_day of this CalendarException.  # noqa: E501
        :rtype: int
        """
        return self._month_day

    @month_day.setter
    def month_day(self, month_day):
        """Sets the month_day of this CalendarException.

        The day of a month on which an exception recurrence is scheduled.  # noqa: E501

        :param month_day: The month_day of this CalendarException.  # noqa: E501
        :type: int
        """
        if month_day is None:
            raise ValueError("Invalid value for `month_day`, must not be `None`")  # noqa: E501
        self._month_day = month_day
    @property
    def day_working(self):
        """Gets the day_working of this CalendarException.  # noqa: E501

        Determines whether the specified date or day type is working.  # noqa: E501

        :return: The day_working of this CalendarException.  # noqa: E501
        :rtype: bool
        """
        return self._day_working

    @day_working.setter
    def day_working(self, day_working):
        """Sets the day_working of this CalendarException.

        Determines whether the specified date or day type is working.  # noqa: E501

        :param day_working: The day_working of this CalendarException.  # noqa: E501
        :type: bool
        """
        if day_working is None:
            raise ValueError("Invalid value for `day_working`, must not be `None`")  # noqa: E501
        self._day_working = day_working
    @property
    def working_times(self):
        """Gets the working_times of this CalendarException.  # noqa: E501

        The collection of working times that defines the time worked on the weekday.  At least one working time must present, and there can't be more than five.  # noqa: E501

        :return: The working_times of this CalendarException.  # noqa: E501
        :rtype: list[WorkingTime]
        """
        return self._working_times

    @working_times.setter
    def working_times(self, working_times):
        """Sets the working_times of this CalendarException.

        The collection of working times that defines the time worked on the weekday.  At least one working time must present, and there can't be more than five.  # noqa: E501

        :param working_times: The working_times of this CalendarException.  # noqa: E501
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
        if not isinstance(other, CalendarException):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
