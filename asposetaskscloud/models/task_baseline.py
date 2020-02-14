# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="TaskBaseline.py">
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


class TaskBaseline(object):
    """Represents baseline values of a task.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'start': 'datetime',
        'finish': 'datetime',
        'duration': 'str',
        'fixed_cost': 'float',
        'duration_format': 'TimeUnitType',
        'estimated_duration': 'bool'
    }

    attribute_map = {
        'start': 'start',
        'finish': 'finish',
        'duration': 'duration',
        'fixed_cost': 'fixedCost',
        'duration_format': 'durationFormat',
        'estimated_duration': 'estimatedDuration'
    }

    def __init__(self, start=None, finish=None, duration=None, fixed_cost=None, duration_format=None, estimated_duration=None):  # noqa: E501
        """TaskBaseline - a model defined in Swagger"""  # noqa: E501

        self._start = None
        self._finish = None
        self._duration = None
        self._fixed_cost = None
        self._duration_format = None
        self._estimated_duration = None
        self.discriminator = None

        if start is not None:
            self.start = start
        if finish is not None:
            self.finish = finish
        if duration is not None:
            self.duration = duration
        if fixed_cost is not None:
            self.fixed_cost = fixed_cost
        if duration_format is not None:
            self.duration_format = duration_format
        if estimated_duration is not None:
            self.estimated_duration = estimated_duration

    @property
    def start(self):
        """Gets the start of this TaskBaseline.  # noqa: E501

        The scheduled start date of the task when the baseline was saved.  # noqa: E501

        :return: The start of this TaskBaseline.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this TaskBaseline.

        The scheduled start date of the task when the baseline was saved.  # noqa: E501

        :param start: The start of this TaskBaseline.  # noqa: E501
        :type: datetime
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501
        self._start = start
    @property
    def finish(self):
        """Gets the finish of this TaskBaseline.  # noqa: E501

        The scheduled finish date of the task when the baseline was saved.  # noqa: E501

        :return: The finish of this TaskBaseline.  # noqa: E501
        :rtype: datetime
        """
        return self._finish

    @finish.setter
    def finish(self, finish):
        """Sets the finish of this TaskBaseline.

        The scheduled finish date of the task when the baseline was saved.  # noqa: E501

        :param finish: The finish of this TaskBaseline.  # noqa: E501
        :type: datetime
        """
        if finish is None:
            raise ValueError("Invalid value for `finish`, must not be `None`")  # noqa: E501
        self._finish = finish
    @property
    def duration(self):
        """Gets the duration of this TaskBaseline.  # noqa: E501

        The scheduled duration of the task when the baseline was saved.  # noqa: E501

        :return: The duration of this TaskBaseline.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TaskBaseline.

        The scheduled duration of the task when the baseline was saved.  # noqa: E501

        :param duration: The duration of this TaskBaseline.  # noqa: E501
        :type: str
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501
        self._duration = duration
    @property
    def fixed_cost(self):
        """Gets the fixed_cost of this TaskBaseline.  # noqa: E501

        The fixed cost of the task when the baseline was saved.  # noqa: E501

        :return: The fixed_cost of this TaskBaseline.  # noqa: E501
        :rtype: float
        """
        return self._fixed_cost

    @fixed_cost.setter
    def fixed_cost(self, fixed_cost):
        """Sets the fixed_cost of this TaskBaseline.

        The fixed cost of the task when the baseline was saved.  # noqa: E501

        :param fixed_cost: The fixed_cost of this TaskBaseline.  # noqa: E501
        :type: float
        """
        if fixed_cost is None:
            raise ValueError("Invalid value for `fixed_cost`, must not be `None`")  # noqa: E501
        self._fixed_cost = fixed_cost
    @property
    def duration_format(self):
        """Gets the duration_format of this TaskBaseline.  # noqa: E501

        The format for expressing the duration of the task baseline.  # noqa: E501

        :return: The duration_format of this TaskBaseline.  # noqa: E501
        :rtype: TimeUnitType
        """
        return self._duration_format

    @duration_format.setter
    def duration_format(self, duration_format):
        """Sets the duration_format of this TaskBaseline.

        The format for expressing the duration of the task baseline.  # noqa: E501

        :param duration_format: The duration_format of this TaskBaseline.  # noqa: E501
        :type: TimeUnitType
        """
        if duration_format is None:
            raise ValueError("Invalid value for `duration_format`, must not be `None`")  # noqa: E501
        self._duration_format = duration_format
    @property
    def estimated_duration(self):
        """Gets the estimated_duration of this TaskBaseline.  # noqa: E501

        Indicates whether the baseline duration of the task was estimated.  # noqa: E501

        :return: The estimated_duration of this TaskBaseline.  # noqa: E501
        :rtype: bool
        """
        return self._estimated_duration

    @estimated_duration.setter
    def estimated_duration(self, estimated_duration):
        """Sets the estimated_duration of this TaskBaseline.

        Indicates whether the baseline duration of the task was estimated.  # noqa: E501

        :param estimated_duration: The estimated_duration of this TaskBaseline.  # noqa: E501
        :type: bool
        """
        if estimated_duration is None:
            raise ValueError("Invalid value for `estimated_duration`, must not be `None`")  # noqa: E501
        self._estimated_duration = estimated_duration
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
        if not isinstance(other, TaskBaseline):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
