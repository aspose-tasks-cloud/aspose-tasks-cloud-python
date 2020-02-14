# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="Baseline.py">
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


class Baseline(object):
    """Represents baseline values of a resource or a task.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'baseline_number': 'BaselineType',
        'work': 'str',
        'cost': 'float',
        'bcws': 'float',
        'bcwp': 'float'
    }

    attribute_map = {
        'baseline_number': 'baselineNumber',
        'work': 'work',
        'cost': 'cost',
        'bcws': 'bcws',
        'bcwp': 'bcwp'
    }

    discriminator_value_class_map = {
        'AssignmentBaseline': 'AssignmentBaseline',
        'TaskBaseline': 'TaskBaseline'
    }

    def __init__(self, baseline_number=None, work=None, cost=None, bcws=None, bcwp=None):  # noqa: E501
        """Baseline - a model defined in Swagger"""  # noqa: E501

        self._baseline_number = None
        self._work = None
        self._cost = None
        self._bcws = None
        self._bcwp = None
        self.discriminator = 'Type'

        if baseline_number is not None:
            self.baseline_number = baseline_number
        if work is not None:
            self.work = work
        if cost is not None:
            self.cost = cost
        if bcws is not None:
            self.bcws = bcws
        if bcwp is not None:
            self.bcwp = bcwp

    @property
    def baseline_number(self):
        """Gets the baseline_number of this Baseline.  # noqa: E501

        The unique number of a baseline data record.  # noqa: E501

        :return: The baseline_number of this Baseline.  # noqa: E501
        :rtype: BaselineType
        """
        return self._baseline_number

    @baseline_number.setter
    def baseline_number(self, baseline_number):
        """Sets the baseline_number of this Baseline.

        The unique number of a baseline data record.  # noqa: E501

        :param baseline_number: The baseline_number of this Baseline.  # noqa: E501
        :type: BaselineType
        """
        if baseline_number is None:
            raise ValueError("Invalid value for `baseline_number`, must not be `None`")  # noqa: E501
        self._baseline_number = baseline_number
    @property
    def work(self):
        """Gets the work of this Baseline.  # noqa: E501

        The work assigned to a resource when the baseline is saved.  # noqa: E501

        :return: The work of this Baseline.  # noqa: E501
        :rtype: str
        """
        return self._work

    @work.setter
    def work(self, work):
        """Sets the work of this Baseline.

        The work assigned to a resource when the baseline is saved.  # noqa: E501

        :param work: The work of this Baseline.  # noqa: E501
        :type: str
        """
        if work is None:
            raise ValueError("Invalid value for `work`, must not be `None`")  # noqa: E501
        self._work = work
    @property
    def cost(self):
        """Gets the cost of this Baseline.  # noqa: E501

        The projected cost of a resource when the baseline is saved.  # noqa: E501

        :return: The cost of this Baseline.  # noqa: E501
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this Baseline.

        The projected cost of a resource when the baseline is saved.  # noqa: E501

        :param cost: The cost of this Baseline.  # noqa: E501
        :type: float
        """
        if cost is None:
            raise ValueError("Invalid value for `cost`, must not be `None`")  # noqa: E501
        self._cost = cost
    @property
    def bcws(self):
        """Gets the bcws of this Baseline.  # noqa: E501

        The budget cost of a work scheduled for a resource.  # noqa: E501

        :return: The bcws of this Baseline.  # noqa: E501
        :rtype: float
        """
        return self._bcws

    @bcws.setter
    def bcws(self, bcws):
        """Sets the bcws of this Baseline.

        The budget cost of a work scheduled for a resource.  # noqa: E501

        :param bcws: The bcws of this Baseline.  # noqa: E501
        :type: float
        """
        if bcws is None:
            raise ValueError("Invalid value for `bcws`, must not be `None`")  # noqa: E501
        self._bcws = bcws
    @property
    def bcwp(self):
        """Gets the bcwp of this Baseline.  # noqa: E501

        The budgeted cost of a work performed by a resource for a project to-date.  # noqa: E501

        :return: The bcwp of this Baseline.  # noqa: E501
        :rtype: float
        """
        return self._bcwp

    @bcwp.setter
    def bcwp(self, bcwp):
        """Sets the bcwp of this Baseline.

        The budgeted cost of a work performed by a resource for a project to-date.  # noqa: E501

        :param bcwp: The bcwp of this Baseline.  # noqa: E501
        :type: float
        """
        if bcwp is None:
            raise ValueError("Invalid value for `bcwp`, must not be `None`")  # noqa: E501
        self._bcwp = bcwp
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
        if not isinstance(other, Baseline):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
