# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="LevelingOptions.py">
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


class LevelingOptions(object):
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
        'start_date': 'datetime',
        'finish_date': 'datetime',
        'resource_uids': 'list[int]',
        'leveling_order': 'LevelingOrder'
    }

    attribute_map = {
        'start_date': 'startDate',
        'finish_date': 'finishDate',
        'resource_uids': 'resourceUids',
        'leveling_order': 'levelingOrder'
    }

    def __init__(self, start_date=None, finish_date=None, resource_uids=None, leveling_order=None):  # noqa: E501
        """LevelingOptions - a model defined in Swagger"""  # noqa: E501

        self._start_date = None
        self._finish_date = None
        self._resource_uids = None
        self._leveling_order = None
        self.discriminator = None

        if start_date is not None:
            self.start_date = start_date
        if finish_date is not None:
            self.finish_date = finish_date
        if resource_uids is not None:
            self.resource_uids = resource_uids
        if leveling_order is not None:
            self.leveling_order = leveling_order

    @property
    def start_date(self):
        """Gets the start_date of this LevelingOptions.  # noqa: E501

        Leveling period start date. The default value is the project`s start date.  # noqa: E501

        :return: The start_date of this LevelingOptions.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this LevelingOptions.

        Leveling period start date. The default value is the project`s start date.  # noqa: E501

        :param start_date: The start_date of this LevelingOptions.  # noqa: E501
        :type: datetime
        """
        self._start_date = start_date
    @property
    def finish_date(self):
        """Gets the finish_date of this LevelingOptions.  # noqa: E501

        Leveling period end date. The default value is the project`s finish date.  # noqa: E501

        :return: The finish_date of this LevelingOptions.  # noqa: E501
        :rtype: datetime
        """
        return self._finish_date

    @finish_date.setter
    def finish_date(self, finish_date):
        """Sets the finish_date of this LevelingOptions.

        Leveling period end date. The default value is the project`s finish date.  # noqa: E501

        :param finish_date: The finish_date of this LevelingOptions.  # noqa: E501
        :type: datetime
        """
        self._finish_date = finish_date
    @property
    def resource_uids(self):
        """Gets the resource_uids of this LevelingOptions.  # noqa: E501

        The list of the resource uids which will be leveled. If null is set,  all project resources will be leveled.  # noqa: E501

        :return: The resource_uids of this LevelingOptions.  # noqa: E501
        :rtype: list[int]
        """
        return self._resource_uids

    @resource_uids.setter
    def resource_uids(self, resource_uids):
        """Sets the resource_uids of this LevelingOptions.

        The list of the resource uids which will be leveled. If null is set,  all project resources will be leveled.  # noqa: E501

        :param resource_uids: The resource_uids of this LevelingOptions.  # noqa: E501
        :type: list[int]
        """
        self._resource_uids = resource_uids
    @property
    def leveling_order(self):
        """Gets the leveling_order of this LevelingOptions.  # noqa: E501

        The order in which the leveling algorithm delays tasks that have overallocations. After determination of tasks causing the overallocation and which tasks can be delayed, the specified order is used which task should be delayed first.  # noqa: E501

        :return: The leveling_order of this LevelingOptions.  # noqa: E501
        :rtype: LevelingOrder
        """
        return self._leveling_order

    @leveling_order.setter
    def leveling_order(self, leveling_order):
        """Sets the leveling_order of this LevelingOptions.

        The order in which the leveling algorithm delays tasks that have overallocations. After determination of tasks causing the overallocation and which tasks can be delayed, the specified order is used which task should be delayed first.  # noqa: E501

        :param leveling_order: The leveling_order of this LevelingOptions.  # noqa: E501
        :type: LevelingOrder
        """
        if leveling_order is None:
            raise ValueError("Invalid value for `leveling_order`, must not be `None`")  # noqa: E501
        self._leveling_order = leveling_order
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
        if not isinstance(other, LevelingOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
