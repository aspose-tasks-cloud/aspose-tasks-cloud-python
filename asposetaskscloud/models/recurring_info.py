# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="RecurringInfo.py">
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


class RecurringInfo(object):
    """Represents the details of a recurring task in a project.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'recurrence_pattern': 'RecurrencePattern',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'duration': 'str',
        'occurrences': 'int',
        'use_end_date': 'bool',
        'daily_repetitions': 'int',
        'daily_use_workdays': 'bool',
        'weekly_repetitions': 'int',
        'weekly_days': 'WeekDayType',
        'monthly_use_ordinal_day': 'bool',
        'monthly_ordinal_number': 'OrdinalNumber',
        'monthly_ordinal_day': 'DayOfWeek',
        'monthly_ordinal_repetitions': 'int',
        'monthly_day': 'int',
        'monthly_repetitions': 'int',
        'yearly_use_ordinal_day': 'bool',
        'yearly_date': 'datetime',
        'yearly_ordinal_number': 'OrdinalNumber',
        'yearly_ordinal_day': 'DayOfWeek',
        'yearly_ordinal_month': 'Month'
    }

    attribute_map = {
        'recurrence_pattern': 'recurrencePattern',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'duration': 'duration',
        'occurrences': 'occurrences',
        'use_end_date': 'useEndDate',
        'daily_repetitions': 'dailyRepetitions',
        'daily_use_workdays': 'dailyUseWorkdays',
        'weekly_repetitions': 'weeklyRepetitions',
        'weekly_days': 'weeklyDays',
        'monthly_use_ordinal_day': 'monthlyUseOrdinalDay',
        'monthly_ordinal_number': 'monthlyOrdinalNumber',
        'monthly_ordinal_day': 'monthlyOrdinalDay',
        'monthly_ordinal_repetitions': 'monthlyOrdinalRepetitions',
        'monthly_day': 'monthlyDay',
        'monthly_repetitions': 'monthlyRepetitions',
        'yearly_use_ordinal_day': 'yearlyUseOrdinalDay',
        'yearly_date': 'yearlyDate',
        'yearly_ordinal_number': 'yearlyOrdinalNumber',
        'yearly_ordinal_day': 'yearlyOrdinalDay',
        'yearly_ordinal_month': 'yearlyOrdinalMonth'
    }

    def __init__(self, recurrence_pattern=None, start_date=None, end_date=None, duration=None, occurrences=None, use_end_date=None, daily_repetitions=None, daily_use_workdays=None, weekly_repetitions=None, weekly_days=None, monthly_use_ordinal_day=None, monthly_ordinal_number=None, monthly_ordinal_day=None, monthly_ordinal_repetitions=None, monthly_day=None, monthly_repetitions=None, yearly_use_ordinal_day=None, yearly_date=None, yearly_ordinal_number=None, yearly_ordinal_day=None, yearly_ordinal_month=None):  # noqa: E501
        """RecurringInfo - a model defined in Swagger"""  # noqa: E501

        self._recurrence_pattern = None
        self._start_date = None
        self._end_date = None
        self._duration = None
        self._occurrences = None
        self._use_end_date = None
        self._daily_repetitions = None
        self._daily_use_workdays = None
        self._weekly_repetitions = None
        self._weekly_days = None
        self._monthly_use_ordinal_day = None
        self._monthly_ordinal_number = None
        self._monthly_ordinal_day = None
        self._monthly_ordinal_repetitions = None
        self._monthly_day = None
        self._monthly_repetitions = None
        self._yearly_use_ordinal_day = None
        self._yearly_date = None
        self._yearly_ordinal_number = None
        self._yearly_ordinal_day = None
        self._yearly_ordinal_month = None
        self.discriminator = None

        if recurrence_pattern is not None:
            self.recurrence_pattern = recurrence_pattern
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if duration is not None:
            self.duration = duration
        if occurrences is not None:
            self.occurrences = occurrences
        if use_end_date is not None:
            self.use_end_date = use_end_date
        if daily_repetitions is not None:
            self.daily_repetitions = daily_repetitions
        if daily_use_workdays is not None:
            self.daily_use_workdays = daily_use_workdays
        if weekly_repetitions is not None:
            self.weekly_repetitions = weekly_repetitions
        if weekly_days is not None:
            self.weekly_days = weekly_days
        if monthly_use_ordinal_day is not None:
            self.monthly_use_ordinal_day = monthly_use_ordinal_day
        if monthly_ordinal_number is not None:
            self.monthly_ordinal_number = monthly_ordinal_number
        if monthly_ordinal_day is not None:
            self.monthly_ordinal_day = monthly_ordinal_day
        if monthly_ordinal_repetitions is not None:
            self.monthly_ordinal_repetitions = monthly_ordinal_repetitions
        if monthly_day is not None:
            self.monthly_day = monthly_day
        if monthly_repetitions is not None:
            self.monthly_repetitions = monthly_repetitions
        if yearly_use_ordinal_day is not None:
            self.yearly_use_ordinal_day = yearly_use_ordinal_day
        if yearly_date is not None:
            self.yearly_date = yearly_date
        if yearly_ordinal_number is not None:
            self.yearly_ordinal_number = yearly_ordinal_number
        if yearly_ordinal_day is not None:
            self.yearly_ordinal_day = yearly_ordinal_day
        if yearly_ordinal_month is not None:
            self.yearly_ordinal_month = yearly_ordinal_month

    @property
    def recurrence_pattern(self):
        """Gets the recurrence_pattern of this RecurringInfo.  # noqa: E501

        Represents a recurrence pattern of the recurring task. Can be one of the values of  enum.  # noqa: E501

        :return: The recurrence_pattern of this RecurringInfo.  # noqa: E501
        :rtype: RecurrencePattern
        """
        return self._recurrence_pattern

    @recurrence_pattern.setter
    def recurrence_pattern(self, recurrence_pattern):
        """Sets the recurrence_pattern of this RecurringInfo.

        Represents a recurrence pattern of the recurring task. Can be one of the values of  enum.  # noqa: E501

        :param recurrence_pattern: The recurrence_pattern of this RecurringInfo.  # noqa: E501
        :type: RecurrencePattern
        """
        if recurrence_pattern is None:
            raise ValueError("Invalid value for `recurrence_pattern`, must not be `None`")  # noqa: E501
        self._recurrence_pattern = recurrence_pattern
    @property
    def start_date(self):
        """Gets the start_date of this RecurringInfo.  # noqa: E501

        Specifies the date for the occurrences to begin.  # noqa: E501

        :return: The start_date of this RecurringInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this RecurringInfo.

        Specifies the date for the occurrences to begin.  # noqa: E501

        :param start_date: The start_date of this RecurringInfo.  # noqa: E501
        :type: datetime
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501
        self._start_date = start_date
    @property
    def end_date(self):
        """Gets the end_date of this RecurringInfo.  # noqa: E501

        Specifies the date for the occurrences to end.  # noqa: E501

        :return: The end_date of this RecurringInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this RecurringInfo.

        Specifies the date for the occurrences to end.  # noqa: E501

        :param end_date: The end_date of this RecurringInfo.  # noqa: E501
        :type: datetime
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501
        self._end_date = end_date
    @property
    def duration(self):
        """Gets the duration of this RecurringInfo.  # noqa: E501

        Specifies the duration for one occurrence of the recurring task. the instance of  class.  # noqa: E501

        :return: The duration of this RecurringInfo.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this RecurringInfo.

        Specifies the duration for one occurrence of the recurring task. the instance of  class.  # noqa: E501

        :param duration: The duration of this RecurringInfo.  # noqa: E501
        :type: str
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501
        self._duration = duration
    @property
    def occurrences(self):
        """Gets the occurrences of this RecurringInfo.  # noqa: E501

        Specifies a number of occurrences of the recurring task.  # noqa: E501

        :return: The occurrences of this RecurringInfo.  # noqa: E501
        :rtype: int
        """
        return self._occurrences

    @occurrences.setter
    def occurrences(self, occurrences):
        """Sets the occurrences of this RecurringInfo.

        Specifies a number of occurrences of the recurring task.  # noqa: E501

        :param occurrences: The occurrences of this RecurringInfo.  # noqa: E501
        :type: int
        """
        if occurrences is None:
            raise ValueError("Invalid value for `occurrences`, must not be `None`")  # noqa: E501
        self._occurrences = occurrences
    @property
    def use_end_date(self):
        """Gets the use_end_date of this RecurringInfo.  # noqa: E501

        Determines whether to use the end date or a number of occurrences for the recurring task.  # noqa: E501

        :return: The use_end_date of this RecurringInfo.  # noqa: E501
        :rtype: bool
        """
        return self._use_end_date

    @use_end_date.setter
    def use_end_date(self, use_end_date):
        """Sets the use_end_date of this RecurringInfo.

        Determines whether to use the end date or a number of occurrences for the recurring task.  # noqa: E501

        :param use_end_date: The use_end_date of this RecurringInfo.  # noqa: E501
        :type: bool
        """
        if use_end_date is None:
            raise ValueError("Invalid value for `use_end_date`, must not be `None`")  # noqa: E501
        self._use_end_date = use_end_date
    @property
    def daily_repetitions(self):
        """Gets the daily_repetitions of this RecurringInfo.  # noqa: E501

        Specifies an interval between repetitions for the daily recurrence pattern.  # noqa: E501

        :return: The daily_repetitions of this RecurringInfo.  # noqa: E501
        :rtype: int
        """
        return self._daily_repetitions

    @daily_repetitions.setter
    def daily_repetitions(self, daily_repetitions):
        """Sets the daily_repetitions of this RecurringInfo.

        Specifies an interval between repetitions for the daily recurrence pattern.  # noqa: E501

        :param daily_repetitions: The daily_repetitions of this RecurringInfo.  # noqa: E501
        :type: int
        """
        if daily_repetitions is None:
            raise ValueError("Invalid value for `daily_repetitions`, must not be `None`")  # noqa: E501
        self._daily_repetitions = daily_repetitions
    @property
    def daily_use_workdays(self):
        """Gets the daily_use_workdays of this RecurringInfo.  # noqa: E501

        Determines whether to use workdays for the daily recurrence pattern.  # noqa: E501

        :return: The daily_use_workdays of this RecurringInfo.  # noqa: E501
        :rtype: bool
        """
        return self._daily_use_workdays

    @daily_use_workdays.setter
    def daily_use_workdays(self, daily_use_workdays):
        """Sets the daily_use_workdays of this RecurringInfo.

        Determines whether to use workdays for the daily recurrence pattern.  # noqa: E501

        :param daily_use_workdays: The daily_use_workdays of this RecurringInfo.  # noqa: E501
        :type: bool
        """
        if daily_use_workdays is None:
            raise ValueError("Invalid value for `daily_use_workdays`, must not be `None`")  # noqa: E501
        self._daily_use_workdays = daily_use_workdays
    @property
    def weekly_repetitions(self):
        """Gets the weekly_repetitions of this RecurringInfo.  # noqa: E501

        Specifies an interval between repetitions for the weekly recurrence pattern.  # noqa: E501

        :return: The weekly_repetitions of this RecurringInfo.  # noqa: E501
        :rtype: int
        """
        return self._weekly_repetitions

    @weekly_repetitions.setter
    def weekly_repetitions(self, weekly_repetitions):
        """Sets the weekly_repetitions of this RecurringInfo.

        Specifies an interval between repetitions for the weekly recurrence pattern.  # noqa: E501

        :param weekly_repetitions: The weekly_repetitions of this RecurringInfo.  # noqa: E501
        :type: int
        """
        if weekly_repetitions is None:
            raise ValueError("Invalid value for `weekly_repetitions`, must not be `None`")  # noqa: E501
        self._weekly_repetitions = weekly_repetitions
    @property
    def weekly_days(self):
        """Gets the weekly_days of this RecurringInfo.  # noqa: E501

        Specifies a collection of days used in the weekly recurrence pattern.  # noqa: E501

        :return: The weekly_days of this RecurringInfo.  # noqa: E501
        :rtype: WeekDayType
        """
        return self._weekly_days

    @weekly_days.setter
    def weekly_days(self, weekly_days):
        """Sets the weekly_days of this RecurringInfo.

        Specifies a collection of days used in the weekly recurrence pattern.  # noqa: E501

        :param weekly_days: The weekly_days of this RecurringInfo.  # noqa: E501
        :type: WeekDayType
        """
        if weekly_days is None:
            raise ValueError("Invalid value for `weekly_days`, must not be `None`")  # noqa: E501
        self._weekly_days = weekly_days
    @property
    def monthly_use_ordinal_day(self):
        """Gets the monthly_use_ordinal_day of this RecurringInfo.  # noqa: E501

        Determines whether to use ordinal day for the monthly recurrence pattern.  # noqa: E501

        :return: The monthly_use_ordinal_day of this RecurringInfo.  # noqa: E501
        :rtype: bool
        """
        return self._monthly_use_ordinal_day

    @monthly_use_ordinal_day.setter
    def monthly_use_ordinal_day(self, monthly_use_ordinal_day):
        """Sets the monthly_use_ordinal_day of this RecurringInfo.

        Determines whether to use ordinal day for the monthly recurrence pattern.  # noqa: E501

        :param monthly_use_ordinal_day: The monthly_use_ordinal_day of this RecurringInfo.  # noqa: E501
        :type: bool
        """
        if monthly_use_ordinal_day is None:
            raise ValueError("Invalid value for `monthly_use_ordinal_day`, must not be `None`")  # noqa: E501
        self._monthly_use_ordinal_day = monthly_use_ordinal_day
    @property
    def monthly_ordinal_number(self):
        """Gets the monthly_ordinal_number of this RecurringInfo.  # noqa: E501

        Specifies an ordinal number of the monthly recurrence pattern. Can be one of the values of  enum.  # noqa: E501

        :return: The monthly_ordinal_number of this RecurringInfo.  # noqa: E501
        :rtype: OrdinalNumber
        """
        return self._monthly_ordinal_number

    @monthly_ordinal_number.setter
    def monthly_ordinal_number(self, monthly_ordinal_number):
        """Sets the monthly_ordinal_number of this RecurringInfo.

        Specifies an ordinal number of the monthly recurrence pattern. Can be one of the values of  enum.  # noqa: E501

        :param monthly_ordinal_number: The monthly_ordinal_number of this RecurringInfo.  # noqa: E501
        :type: OrdinalNumber
        """
        if monthly_ordinal_number is None:
            raise ValueError("Invalid value for `monthly_ordinal_number`, must not be `None`")  # noqa: E501
        self._monthly_ordinal_number = monthly_ordinal_number
    @property
    def monthly_ordinal_day(self):
        """Gets the monthly_ordinal_day of this RecurringInfo.  # noqa: E501

        Specifies a day of the monthly recurrence pattern when using ordinal day. Can be one of the values of  enum.  # noqa: E501

        :return: The monthly_ordinal_day of this RecurringInfo.  # noqa: E501
        :rtype: DayOfWeek
        """
        return self._monthly_ordinal_day

    @monthly_ordinal_day.setter
    def monthly_ordinal_day(self, monthly_ordinal_day):
        """Sets the monthly_ordinal_day of this RecurringInfo.

        Specifies a day of the monthly recurrence pattern when using ordinal day. Can be one of the values of  enum.  # noqa: E501

        :param monthly_ordinal_day: The monthly_ordinal_day of this RecurringInfo.  # noqa: E501
        :type: DayOfWeek
        """
        if monthly_ordinal_day is None:
            raise ValueError("Invalid value for `monthly_ordinal_day`, must not be `None`")  # noqa: E501
        self._monthly_ordinal_day = monthly_ordinal_day
    @property
    def monthly_ordinal_repetitions(self):
        """Gets the monthly_ordinal_repetitions of this RecurringInfo.  # noqa: E501

        Specifies a number of repetitions for the monthly recurrence pattern when using ordinal day.  # noqa: E501

        :return: The monthly_ordinal_repetitions of this RecurringInfo.  # noqa: E501
        :rtype: int
        """
        return self._monthly_ordinal_repetitions

    @monthly_ordinal_repetitions.setter
    def monthly_ordinal_repetitions(self, monthly_ordinal_repetitions):
        """Sets the monthly_ordinal_repetitions of this RecurringInfo.

        Specifies a number of repetitions for the monthly recurrence pattern when using ordinal day.  # noqa: E501

        :param monthly_ordinal_repetitions: The monthly_ordinal_repetitions of this RecurringInfo.  # noqa: E501
        :type: int
        """
        if monthly_ordinal_repetitions is None:
            raise ValueError("Invalid value for `monthly_ordinal_repetitions`, must not be `None`")  # noqa: E501
        self._monthly_ordinal_repetitions = monthly_ordinal_repetitions
    @property
    def monthly_day(self):
        """Gets the monthly_day of this RecurringInfo.  # noqa: E501

        Specifies a number of day of the monthly recurrence pattern.  # noqa: E501

        :return: The monthly_day of this RecurringInfo.  # noqa: E501
        :rtype: int
        """
        return self._monthly_day

    @monthly_day.setter
    def monthly_day(self, monthly_day):
        """Sets the monthly_day of this RecurringInfo.

        Specifies a number of day of the monthly recurrence pattern.  # noqa: E501

        :param monthly_day: The monthly_day of this RecurringInfo.  # noqa: E501
        :type: int
        """
        if monthly_day is None:
            raise ValueError("Invalid value for `monthly_day`, must not be `None`")  # noqa: E501
        self._monthly_day = monthly_day
    @property
    def monthly_repetitions(self):
        """Gets the monthly_repetitions of this RecurringInfo.  # noqa: E501

        Specifies a number of repetitions for the monthly recurrence pattern.  # noqa: E501

        :return: The monthly_repetitions of this RecurringInfo.  # noqa: E501
        :rtype: int
        """
        return self._monthly_repetitions

    @monthly_repetitions.setter
    def monthly_repetitions(self, monthly_repetitions):
        """Sets the monthly_repetitions of this RecurringInfo.

        Specifies a number of repetitions for the monthly recurrence pattern.  # noqa: E501

        :param monthly_repetitions: The monthly_repetitions of this RecurringInfo.  # noqa: E501
        :type: int
        """
        if monthly_repetitions is None:
            raise ValueError("Invalid value for `monthly_repetitions`, must not be `None`")  # noqa: E501
        self._monthly_repetitions = monthly_repetitions
    @property
    def yearly_use_ordinal_day(self):
        """Gets the yearly_use_ordinal_day of this RecurringInfo.  # noqa: E501

        Determines whether to use ordinal day for the yearly recurrence pattern.  # noqa: E501

        :return: The yearly_use_ordinal_day of this RecurringInfo.  # noqa: E501
        :rtype: bool
        """
        return self._yearly_use_ordinal_day

    @yearly_use_ordinal_day.setter
    def yearly_use_ordinal_day(self, yearly_use_ordinal_day):
        """Sets the yearly_use_ordinal_day of this RecurringInfo.

        Determines whether to use ordinal day for the yearly recurrence pattern.  # noqa: E501

        :param yearly_use_ordinal_day: The yearly_use_ordinal_day of this RecurringInfo.  # noqa: E501
        :type: bool
        """
        if yearly_use_ordinal_day is None:
            raise ValueError("Invalid value for `yearly_use_ordinal_day`, must not be `None`")  # noqa: E501
        self._yearly_use_ordinal_day = yearly_use_ordinal_day
    @property
    def yearly_date(self):
        """Gets the yearly_date of this RecurringInfo.  # noqa: E501

        Specifies a date for the yearly recurrence pattern.  # noqa: E501

        :return: The yearly_date of this RecurringInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._yearly_date

    @yearly_date.setter
    def yearly_date(self, yearly_date):
        """Sets the yearly_date of this RecurringInfo.

        Specifies a date for the yearly recurrence pattern.  # noqa: E501

        :param yearly_date: The yearly_date of this RecurringInfo.  # noqa: E501
        :type: datetime
        """
        if yearly_date is None:
            raise ValueError("Invalid value for `yearly_date`, must not be `None`")  # noqa: E501
        self._yearly_date = yearly_date
    @property
    def yearly_ordinal_number(self):
        """Gets the yearly_ordinal_number of this RecurringInfo.  # noqa: E501

        Specifies an ordinal number of the yearly recurrence pattern. Can be one of the values of  enum.  # noqa: E501

        :return: The yearly_ordinal_number of this RecurringInfo.  # noqa: E501
        :rtype: OrdinalNumber
        """
        return self._yearly_ordinal_number

    @yearly_ordinal_number.setter
    def yearly_ordinal_number(self, yearly_ordinal_number):
        """Sets the yearly_ordinal_number of this RecurringInfo.

        Specifies an ordinal number of the yearly recurrence pattern. Can be one of the values of  enum.  # noqa: E501

        :param yearly_ordinal_number: The yearly_ordinal_number of this RecurringInfo.  # noqa: E501
        :type: OrdinalNumber
        """
        if yearly_ordinal_number is None:
            raise ValueError("Invalid value for `yearly_ordinal_number`, must not be `None`")  # noqa: E501
        self._yearly_ordinal_number = yearly_ordinal_number
    @property
    def yearly_ordinal_day(self):
        """Gets the yearly_ordinal_day of this RecurringInfo.  # noqa: E501

        Specifies a weekday of the yearly recurrence pattern when using ordinal day. Can be one of the values of  enum.  # noqa: E501

        :return: The yearly_ordinal_day of this RecurringInfo.  # noqa: E501
        :rtype: DayOfWeek
        """
        return self._yearly_ordinal_day

    @yearly_ordinal_day.setter
    def yearly_ordinal_day(self, yearly_ordinal_day):
        """Sets the yearly_ordinal_day of this RecurringInfo.

        Specifies a weekday of the yearly recurrence pattern when using ordinal day. Can be one of the values of  enum.  # noqa: E501

        :param yearly_ordinal_day: The yearly_ordinal_day of this RecurringInfo.  # noqa: E501
        :type: DayOfWeek
        """
        if yearly_ordinal_day is None:
            raise ValueError("Invalid value for `yearly_ordinal_day`, must not be `None`")  # noqa: E501
        self._yearly_ordinal_day = yearly_ordinal_day
    @property
    def yearly_ordinal_month(self):
        """Gets the yearly_ordinal_month of this RecurringInfo.  # noqa: E501

        Specifies a month of the yearly recurrence pattern when using ordinal day. Can be one of the values of  enum.  # noqa: E501

        :return: The yearly_ordinal_month of this RecurringInfo.  # noqa: E501
        :rtype: Month
        """
        return self._yearly_ordinal_month

    @yearly_ordinal_month.setter
    def yearly_ordinal_month(self, yearly_ordinal_month):
        """Sets the yearly_ordinal_month of this RecurringInfo.

        Specifies a month of the yearly recurrence pattern when using ordinal day. Can be one of the values of  enum.  # noqa: E501

        :param yearly_ordinal_month: The yearly_ordinal_month of this RecurringInfo.  # noqa: E501
        :type: Month
        """
        if yearly_ordinal_month is None:
            raise ValueError("Invalid value for `yearly_ordinal_month`, must not be `None`")  # noqa: E501
        self._yearly_ordinal_month = yearly_ordinal_month
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
        if not isinstance(other, RecurringInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
