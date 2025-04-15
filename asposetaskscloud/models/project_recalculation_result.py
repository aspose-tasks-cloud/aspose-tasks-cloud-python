# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="ProjectRecalculationResult.py">
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


class ProjectRecalculationResult(object):
    """Specifies the  result of recalculation of the project;
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'validation_state': 'ProjectValidationState',
        'validation_error_message': 'str',
        'failed_task_uid': 'int'
    }

    attribute_map = {
        'validation_state': 'validationState',
        'validation_error_message': 'validationErrorMessage',
        'failed_task_uid': 'failedTaskUid'
    }

    def __init__(self, validation_state=None, validation_error_message=None, failed_task_uid=None):  # noqa: E501
        """ProjectRecalculationResult - a model defined in Swagger"""  # noqa: E501

        self._validation_state = None
        self._validation_error_message = None
        self._failed_task_uid = None
        self.discriminator = None

        if validation_state is not None:
            self.validation_state = validation_state
        if validation_error_message is not None:
            self.validation_error_message = validation_error_message
        if failed_task_uid is not None:
            self.failed_task_uid = failed_task_uid

    @property
    def validation_state(self):
        """Gets the validation_state of this ProjectRecalculationResult.  # noqa: E501


        :return: The validation_state of this ProjectRecalculationResult.  # noqa: E501
        :rtype: ProjectValidationState
        """
        return self._validation_state

    @validation_state.setter
    def validation_state(self, validation_state):
        """Sets the validation_state of this ProjectRecalculationResult.


        :param validation_state: The validation_state of this ProjectRecalculationResult.  # noqa: E501
        :type: ProjectValidationState
        """
        if validation_state is None:
            raise ValueError("Invalid value for `validation_state`, must not be `None`")  # noqa: E501
        self._validation_state = validation_state
    @property
    def validation_error_message(self):
        """Gets the validation_error_message of this ProjectRecalculationResult.  # noqa: E501


        :return: The validation_error_message of this ProjectRecalculationResult.  # noqa: E501
        :rtype: str
        """
        return self._validation_error_message

    @validation_error_message.setter
    def validation_error_message(self, validation_error_message):
        """Sets the validation_error_message of this ProjectRecalculationResult.


        :param validation_error_message: The validation_error_message of this ProjectRecalculationResult.  # noqa: E501
        :type: str
        """
        self._validation_error_message = validation_error_message
    @property
    def failed_task_uid(self):
        """Gets the failed_task_uid of this ProjectRecalculationResult.  # noqa: E501

        Gets the task uid which caused the validation error.  # noqa: E501

        :return: The failed_task_uid of this ProjectRecalculationResult.  # noqa: E501
        :rtype: int
        """
        return self._failed_task_uid

    @failed_task_uid.setter
    def failed_task_uid(self, failed_task_uid):
        """Sets the failed_task_uid of this ProjectRecalculationResult.

        Gets the task uid which caused the validation error.  # noqa: E501

        :param failed_task_uid: The failed_task_uid of this ProjectRecalculationResult.  # noqa: E501
        :type: int
        """
        self._failed_task_uid = failed_task_uid
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
        if not isinstance(other, ProjectRecalculationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
