# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="Calendar.py">
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


class Calendar(object):
    """Represents a calendar used in a project.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'guid': 'str',
        'name': 'str',
        'uid': 'int',
        'days': 'list[WeekDay]',
        'is_base_calendar': 'bool',
        'base_calendar': 'Calendar',
        'is_baseline_calendar': 'bool'
    }

    attribute_map = {
        'guid': 'guid',
        'name': 'name',
        'uid': 'uid',
        'days': 'days',
        'is_base_calendar': 'isBaseCalendar',
        'base_calendar': 'baseCalendar',
        'is_baseline_calendar': 'isBaselineCalendar'
    }

    def __init__(self, guid=None, name=None, uid=None, days=None, is_base_calendar=None, base_calendar=None, is_baseline_calendar=None):  # noqa: E501
        """Calendar - a model defined in Swagger"""  # noqa: E501

        self._guid = None
        self._name = None
        self._uid = None
        self._days = None
        self._is_base_calendar = None
        self._base_calendar = None
        self._is_baseline_calendar = None
        self.discriminator = None

        if guid is not None:
            self.guid = guid
        if name is not None:
            self.name = name
        if uid is not None:
            self.uid = uid
        if days is not None:
            self.days = days
        if is_base_calendar is not None:
            self.is_base_calendar = is_base_calendar
        if base_calendar is not None:
            self.base_calendar = base_calendar
        if is_baseline_calendar is not None:
            self.is_baseline_calendar = is_baseline_calendar

    @property
    def guid(self):
        """Gets the guid of this Calendar.  # noqa: E501

        Gets calendar's Guid.  # noqa: E501

        :return: The guid of this Calendar.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this Calendar.

        Gets calendar's Guid.  # noqa: E501

        :param guid: The guid of this Calendar.  # noqa: E501
        :type: str
        """
        self._guid = guid
    @property
    def name(self):
        """Gets the name of this Calendar.  # noqa: E501

        The name of the calendar.  # noqa: E501

        :return: The name of this Calendar.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Calendar.

        The name of the calendar.  # noqa: E501

        :param name: The name of this Calendar.  # noqa: E501
        :type: str
        """
        self._name = name
    @property
    def uid(self):
        """Gets the uid of this Calendar.  # noqa: E501

        The unique identifier of the calendar.  # noqa: E501

        :return: The uid of this Calendar.  # noqa: E501
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this Calendar.

        The unique identifier of the calendar.  # noqa: E501

        :param uid: The uid of this Calendar.  # noqa: E501
        :type: int
        """
        if uid is None:
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501
        self._uid = uid
    @property
    def days(self):
        """Gets the days of this Calendar.  # noqa: E501

        The collection of weekdays that defines the calendar.  # noqa: E501

        :return: The days of this Calendar.  # noqa: E501
        :rtype: list[WeekDay]
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this Calendar.

        The collection of weekdays that defines the calendar.  # noqa: E501

        :param days: The days of this Calendar.  # noqa: E501
        :type: list[WeekDay]
        """
        self._days = days
    @property
    def is_base_calendar(self):
        """Gets the is_base_calendar of this Calendar.  # noqa: E501

        Determines whether the calendar is a base calendar.  # noqa: E501

        :return: The is_base_calendar of this Calendar.  # noqa: E501
        :rtype: bool
        """
        return self._is_base_calendar

    @is_base_calendar.setter
    def is_base_calendar(self, is_base_calendar):
        """Sets the is_base_calendar of this Calendar.

        Determines whether the calendar is a base calendar.  # noqa: E501

        :param is_base_calendar: The is_base_calendar of this Calendar.  # noqa: E501
        :type: bool
        """
        if is_base_calendar is None:
            raise ValueError("Invalid value for `is_base_calendar`, must not be `None`")  # noqa: E501
        self._is_base_calendar = is_base_calendar
    @property
    def base_calendar(self):
        """Gets the base_calendar of this Calendar.  # noqa: E501

        The base calendar on which this calendar depends. Only applicable if the calendar is not a base calendar.  # noqa: E501

        :return: The base_calendar of this Calendar.  # noqa: E501
        :rtype: Calendar
        """
        return self._base_calendar

    @base_calendar.setter
    def base_calendar(self, base_calendar):
        """Sets the base_calendar of this Calendar.

        The base calendar on which this calendar depends. Only applicable if the calendar is not a base calendar.  # noqa: E501

        :param base_calendar: The base_calendar of this Calendar.  # noqa: E501
        :type: Calendar
        """
        self._base_calendar = base_calendar
    @property
    def is_baseline_calendar(self):
        """Gets the is_baseline_calendar of this Calendar.  # noqa: E501

        Specifies whether the calendar is a baseline calendar.  # noqa: E501

        :return: The is_baseline_calendar of this Calendar.  # noqa: E501
        :rtype: bool
        """
        return self._is_baseline_calendar

    @is_baseline_calendar.setter
    def is_baseline_calendar(self, is_baseline_calendar):
        """Sets the is_baseline_calendar of this Calendar.

        Specifies whether the calendar is a baseline calendar.  # noqa: E501

        :param is_baseline_calendar: The is_baseline_calendar of this Calendar.  # noqa: E501
        :type: bool
        """
        if is_baseline_calendar is None:
            raise ValueError("Invalid value for `is_baseline_calendar`, must not be `None`")  # noqa: E501
        self._is_baseline_calendar = is_baseline_calendar
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
        if not isinstance(other, Calendar):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
