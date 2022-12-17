# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="PrimaveraTaskProperties.py">
#   Copyright (c) 2022 Aspose.Tasks Cloud
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


class PrimaveraTaskProperties(object):
    """Represents Primavera-specific properties for a task read from Primavera format (XER of P6XML).
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'sequence_number': 'int',
        'activity_id': 'str',
        'remaining_early_finish': 'datetime',
        'remaining_early_start': 'datetime',
        'remaining_late_start': 'datetime',
        'remaining_late_finish': 'datetime',
        'raw_duration_type': 'str',
        'raw_activity_type': 'str',
        'raw_complete_percent_type': 'str',
        'raw_status': 'str'
    }

    attribute_map = {
        'sequence_number': 'sequenceNumber',
        'activity_id': 'activityId',
        'remaining_early_finish': 'remainingEarlyFinish',
        'remaining_early_start': 'remainingEarlyStart',
        'remaining_late_start': 'remainingLateStart',
        'remaining_late_finish': 'remainingLateFinish',
        'raw_duration_type': 'rawDurationType',
        'raw_activity_type': 'rawActivityType',
        'raw_complete_percent_type': 'rawCompletePercentType',
        'raw_status': 'rawStatus'
    }

    def __init__(self, sequence_number=None, activity_id=None, remaining_early_finish=None, remaining_early_start=None, remaining_late_start=None, remaining_late_finish=None, raw_duration_type=None, raw_activity_type=None, raw_complete_percent_type=None, raw_status=None):  # noqa: E501
        """PrimaveraTaskProperties - a model defined in Swagger"""  # noqa: E501

        self._sequence_number = None
        self._activity_id = None
        self._remaining_early_finish = None
        self._remaining_early_start = None
        self._remaining_late_start = None
        self._remaining_late_finish = None
        self._raw_duration_type = None
        self._raw_activity_type = None
        self._raw_complete_percent_type = None
        self._raw_status = None
        self.discriminator = None

        if sequence_number is not None:
            self.sequence_number = sequence_number
        if activity_id is not None:
            self.activity_id = activity_id
        if remaining_early_finish is not None:
            self.remaining_early_finish = remaining_early_finish
        if remaining_early_start is not None:
            self.remaining_early_start = remaining_early_start
        if remaining_late_start is not None:
            self.remaining_late_start = remaining_late_start
        if remaining_late_finish is not None:
            self.remaining_late_finish = remaining_late_finish
        if raw_duration_type is not None:
            self.raw_duration_type = raw_duration_type
        if raw_activity_type is not None:
            self.raw_activity_type = raw_activity_type
        if raw_complete_percent_type is not None:
            self.raw_complete_percent_type = raw_complete_percent_type
        if raw_status is not None:
            self.raw_status = raw_status

    @property
    def sequence_number(self):
        """Gets the sequence_number of this PrimaveraTaskProperties.  # noqa: E501

        The sequence number of the WBS item (summary tasks). It is used to sort summary tasks in Primavera.  # noqa: E501

        :return: The sequence_number of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: int
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """Sets the sequence_number of this PrimaveraTaskProperties.

        The sequence number of the WBS item (summary tasks). It is used to sort summary tasks in Primavera.  # noqa: E501

        :param sequence_number: The sequence_number of this PrimaveraTaskProperties.  # noqa: E501
        :type: int
        """
        if sequence_number is None:
            raise ValueError("Invalid value for `sequence_number`, must not be `None`")  # noqa: E501
        self._sequence_number = sequence_number
    @property
    def activity_id(self):
        """Gets the activity_id of this PrimaveraTaskProperties.  # noqa: E501

        Activity id field - a task's unique identifier used by Primavera.  # noqa: E501

        :return: The activity_id of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: str
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """Sets the activity_id of this PrimaveraTaskProperties.

        Activity id field - a task's unique identifier used by Primavera.  # noqa: E501

        :param activity_id: The activity_id of this PrimaveraTaskProperties.  # noqa: E501
        :type: str
        """
        self._activity_id = activity_id
    @property
    def remaining_early_finish(self):
        """Gets the remaining_early_finish of this PrimaveraTaskProperties.  # noqa: E501

        Remaining early finish date - the date when the remaining work for the activity is scheduled to be finished.  # noqa: E501

        :return: The remaining_early_finish of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: datetime
        """
        return self._remaining_early_finish

    @remaining_early_finish.setter
    def remaining_early_finish(self, remaining_early_finish):
        """Sets the remaining_early_finish of this PrimaveraTaskProperties.

        Remaining early finish date - the date when the remaining work for the activity is scheduled to be finished.  # noqa: E501

        :param remaining_early_finish: The remaining_early_finish of this PrimaveraTaskProperties.  # noqa: E501
        :type: datetime
        """
        if remaining_early_finish is None:
            raise ValueError("Invalid value for `remaining_early_finish`, must not be `None`")  # noqa: E501
        self._remaining_early_finish = remaining_early_finish
    @property
    def remaining_early_start(self):
        """Gets the remaining_early_start of this PrimaveraTaskProperties.  # noqa: E501

        Remaining early start date - the date when the remaining work for the activity is scheduled to begin.  # noqa: E501

        :return: The remaining_early_start of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: datetime
        """
        return self._remaining_early_start

    @remaining_early_start.setter
    def remaining_early_start(self, remaining_early_start):
        """Sets the remaining_early_start of this PrimaveraTaskProperties.

        Remaining early start date - the date when the remaining work for the activity is scheduled to begin.  # noqa: E501

        :param remaining_early_start: The remaining_early_start of this PrimaveraTaskProperties.  # noqa: E501
        :type: datetime
        """
        if remaining_early_start is None:
            raise ValueError("Invalid value for `remaining_early_start`, must not be `None`")  # noqa: E501
        self._remaining_early_start = remaining_early_start
    @property
    def remaining_late_start(self):
        """Gets the remaining_late_start of this PrimaveraTaskProperties.  # noqa: E501

        Remaining late start date.  # noqa: E501

        :return: The remaining_late_start of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: datetime
        """
        return self._remaining_late_start

    @remaining_late_start.setter
    def remaining_late_start(self, remaining_late_start):
        """Sets the remaining_late_start of this PrimaveraTaskProperties.

        Remaining late start date.  # noqa: E501

        :param remaining_late_start: The remaining_late_start of this PrimaveraTaskProperties.  # noqa: E501
        :type: datetime
        """
        if remaining_late_start is None:
            raise ValueError("Invalid value for `remaining_late_start`, must not be `None`")  # noqa: E501
        self._remaining_late_start = remaining_late_start
    @property
    def remaining_late_finish(self):
        """Gets the remaining_late_finish of this PrimaveraTaskProperties.  # noqa: E501

        Remaining late finish date.  # noqa: E501

        :return: The remaining_late_finish of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: datetime
        """
        return self._remaining_late_finish

    @remaining_late_finish.setter
    def remaining_late_finish(self, remaining_late_finish):
        """Sets the remaining_late_finish of this PrimaveraTaskProperties.

        Remaining late finish date.  # noqa: E501

        :param remaining_late_finish: The remaining_late_finish of this PrimaveraTaskProperties.  # noqa: E501
        :type: datetime
        """
        if remaining_late_finish is None:
            raise ValueError("Invalid value for `remaining_late_finish`, must not be `None`")  # noqa: E501
        self._remaining_late_finish = remaining_late_finish
    @property
    def raw_duration_type(self):
        """Gets the raw_duration_type of this PrimaveraTaskProperties.  # noqa: E501

        Raw text representation (as in source file) of 'Duration Type' field of the activity.  # noqa: E501

        :return: The raw_duration_type of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: str
        """
        return self._raw_duration_type

    @raw_duration_type.setter
    def raw_duration_type(self, raw_duration_type):
        """Sets the raw_duration_type of this PrimaveraTaskProperties.

        Raw text representation (as in source file) of 'Duration Type' field of the activity.  # noqa: E501

        :param raw_duration_type: The raw_duration_type of this PrimaveraTaskProperties.  # noqa: E501
        :type: str
        """
        self._raw_duration_type = raw_duration_type
    @property
    def raw_activity_type(self):
        """Gets the raw_activity_type of this PrimaveraTaskProperties.  # noqa: E501

        Raw text representation (as in source file) of 'Activity Type' field of the activity.  # noqa: E501

        :return: The raw_activity_type of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: str
        """
        return self._raw_activity_type

    @raw_activity_type.setter
    def raw_activity_type(self, raw_activity_type):
        """Sets the raw_activity_type of this PrimaveraTaskProperties.

        Raw text representation (as in source file) of 'Activity Type' field of the activity.  # noqa: E501

        :param raw_activity_type: The raw_activity_type of this PrimaveraTaskProperties.  # noqa: E501
        :type: str
        """
        self._raw_activity_type = raw_activity_type
    @property
    def raw_complete_percent_type(self):
        """Gets the raw_complete_percent_type of this PrimaveraTaskProperties.  # noqa: E501

        Raw text representation (as in source file) of '% Complete Type' field of the activity.  # noqa: E501

        :return: The raw_complete_percent_type of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: str
        """
        return self._raw_complete_percent_type

    @raw_complete_percent_type.setter
    def raw_complete_percent_type(self, raw_complete_percent_type):
        """Sets the raw_complete_percent_type of this PrimaveraTaskProperties.

        Raw text representation (as in source file) of '% Complete Type' field of the activity.  # noqa: E501

        :param raw_complete_percent_type: The raw_complete_percent_type of this PrimaveraTaskProperties.  # noqa: E501
        :type: str
        """
        self._raw_complete_percent_type = raw_complete_percent_type
    @property
    def raw_status(self):
        """Gets the raw_status of this PrimaveraTaskProperties.  # noqa: E501

        Raw text representation (as in source file) of 'Status' field of the activity.  # noqa: E501

        :return: The raw_status of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: str
        """
        return self._raw_status

    @raw_status.setter
    def raw_status(self, raw_status):
        """Sets the raw_status of this PrimaveraTaskProperties.

        Raw text representation (as in source file) of 'Status' field of the activity.  # noqa: E501

        :param raw_status: The raw_status of this PrimaveraTaskProperties.  # noqa: E501
        :type: str
        """
        self._raw_status = raw_status
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
        if not isinstance(other, PrimaveraTaskProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
