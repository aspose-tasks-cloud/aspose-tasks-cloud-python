# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="WorkWeek.py">
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


class WorkWeek(object):
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
        'name': 'str',
        'from_date': 'datetime',
        'to_date': 'datetime',
        'week_days': 'list[WeekDay]'
    }

    attribute_map = {
        'name': 'name',
        'from_date': 'fromDate',
        'to_date': 'toDate',
        'week_days': 'weekDays'
    }

    def __init__(self, name=None, from_date=None, to_date=None, week_days=None):  # noqa: E501
        """WorkWeek - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._from_date = None
        self._to_date = None
        self._week_days = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date
        if week_days is not None:
            self.week_days = week_days

    @property
    def name(self):
        """Gets the name of this WorkWeek.  # noqa: E501

        Determines the name of a work week.  # noqa: E501

        :return: The name of this WorkWeek.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkWeek.

        Determines the name of a work week.  # noqa: E501

        :param name: The name of this WorkWeek.  # noqa: E501
        :type: str
        """
        self._name = name
    @property
    def from_date(self):
        """Gets the from_date of this WorkWeek.  # noqa: E501

        Returns or sets the beginning of a work week.  # noqa: E501

        :return: The from_date of this WorkWeek.  # noqa: E501
        :rtype: datetime
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this WorkWeek.

        Returns or sets the beginning of a work week.  # noqa: E501

        :param from_date: The from_date of this WorkWeek.  # noqa: E501
        :type: datetime
        """
        if from_date is None:
            raise ValueError("Invalid value for `from_date`, must not be `None`")  # noqa: E501
        self._from_date = from_date
    @property
    def to_date(self):
        """Gets the to_date of this WorkWeek.  # noqa: E501

        Returns or sets the end of a work week.  # noqa: E501

        :return: The to_date of this WorkWeek.  # noqa: E501
        :rtype: datetime
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this WorkWeek.

        Returns or sets the end of a work week.  # noqa: E501

        :param to_date: The to_date of this WorkWeek.  # noqa: E501
        :type: datetime
        """
        if to_date is None:
            raise ValueError("Invalid value for `to_date`, must not be `None`")  # noqa: E501
        self._to_date = to_date
    @property
    def week_days(self):
        """Gets the week_days of this WorkWeek.  # noqa: E501

        The collection of week days that define the working time of current working week.  # noqa: E501

        :return: The week_days of this WorkWeek.  # noqa: E501
        :rtype: list[WeekDay]
        """
        return self._week_days

    @week_days.setter
    def week_days(self, week_days):
        """Sets the week_days of this WorkWeek.

        The collection of week days that define the working time of current working week.  # noqa: E501

        :param week_days: The week_days of this WorkWeek.  # noqa: E501
        :type: list[WeekDay]
        """
        self._week_days = week_days
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
        if not isinstance(other, WorkWeek):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
