# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="TaskCreationRequest.py">
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


class TaskCreationRequest(object):
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
        'task_name': 'str',
        'parent_task_uid': 'int',
        'before_task_id': 'int'
    }

    attribute_map = {
        'task_name': 'taskName',
        'parent_task_uid': 'parentTaskUid',
        'before_task_id': 'beforeTaskId'
    }

    def __init__(self, task_name=None, parent_task_uid=None, before_task_id=None):  # noqa: E501
        """TaskCreationRequest - a model defined in Swagger"""  # noqa: E501

        self._task_name = None
        self._parent_task_uid = None
        self._before_task_id = None
        self.discriminator = None

        if task_name is not None:
            self.task_name = task_name
        if parent_task_uid is not None:
            self.parent_task_uid = parent_task_uid
        if before_task_id is not None:
            self.before_task_id = before_task_id

    @property
    def task_name(self):
        """Gets the task_name of this TaskCreationRequest.  # noqa: E501

        The name for the new task.  # noqa: E501

        :return: The task_name of this TaskCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this TaskCreationRequest.

        The name for the new task.  # noqa: E501

        :param task_name: The task_name of this TaskCreationRequest.  # noqa: E501
        :type: str
        """
        self._task_name = task_name
    @property
    def parent_task_uid(self):
        """Gets the parent_task_uid of this TaskCreationRequest.  # noqa: E501

        Uid for parent task.  # noqa: E501

        :return: The parent_task_uid of this TaskCreationRequest.  # noqa: E501
        :rtype: int
        """
        return self._parent_task_uid

    @parent_task_uid.setter
    def parent_task_uid(self, parent_task_uid):
        """Sets the parent_task_uid of this TaskCreationRequest.

        Uid for parent task.  # noqa: E501

        :param parent_task_uid: The parent_task_uid of this TaskCreationRequest.  # noqa: E501
        :type: int
        """
        self._parent_task_uid = parent_task_uid
    @property
    def before_task_id(self):
        """Gets the before_task_id of this TaskCreationRequest.  # noqa: E501

        Id of task before which new task will be inserted.  # noqa: E501

        :return: The before_task_id of this TaskCreationRequest.  # noqa: E501
        :rtype: int
        """
        return self._before_task_id

    @before_task_id.setter
    def before_task_id(self, before_task_id):
        """Sets the before_task_id of this TaskCreationRequest.

        Id of task before which new task will be inserted.  # noqa: E501

        :param before_task_id: The before_task_id of this TaskCreationRequest.  # noqa: E501
        :type: int
        """
        self._before_task_id = before_task_id
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
        if not isinstance(other, TaskCreationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
