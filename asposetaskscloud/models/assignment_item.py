# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="AssignmentItem.py">
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


class AssignmentItem(object):
    """Resource&#39;s assignment brief into.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'link': 'Link',
        'uid': 'int',
        'task_uid': 'int',
        'resource_uid': 'int'
    }

    attribute_map = {
        'link': 'link',
        'uid': 'uid',
        'task_uid': 'taskUid',
        'resource_uid': 'resourceUid'
    }

    def __init__(self, link=None, uid=None, task_uid=None, resource_uid=None):  # noqa: E501
        """AssignmentItem - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._uid = None
        self._task_uid = None
        self._resource_uid = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if uid is not None:
            self.uid = uid
        if task_uid is not None:
            self.task_uid = task_uid
        if resource_uid is not None:
            self.resource_uid = resource_uid

    @property
    def link(self):
        """Gets the link of this AssignmentItem.  # noqa: E501


        :return: The link of this AssignmentItem.  # noqa: E501
        :rtype: Link
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this AssignmentItem.


        :param link: The link of this AssignmentItem.  # noqa: E501
        :type: Link
        """
        self._link = link
    @property
    def uid(self):
        """Gets the uid of this AssignmentItem.  # noqa: E501

        The unique id (Uid) of the resource's assignment.  # noqa: E501

        :return: The uid of this AssignmentItem.  # noqa: E501
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this AssignmentItem.

        The unique id (Uid) of the resource's assignment.  # noqa: E501

        :param uid: The uid of this AssignmentItem.  # noqa: E501
        :type: int
        """
        if uid is None:
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501
        self._uid = uid
    @property
    def task_uid(self):
        """Gets the task_uid of this AssignmentItem.  # noqa: E501

        Uid of the task.  # noqa: E501

        :return: The task_uid of this AssignmentItem.  # noqa: E501
        :rtype: int
        """
        return self._task_uid

    @task_uid.setter
    def task_uid(self, task_uid):
        """Sets the task_uid of this AssignmentItem.

        Uid of the task.  # noqa: E501

        :param task_uid: The task_uid of this AssignmentItem.  # noqa: E501
        :type: int
        """
        if task_uid is None:
            raise ValueError("Invalid value for `task_uid`, must not be `None`")  # noqa: E501
        self._task_uid = task_uid
    @property
    def resource_uid(self):
        """Gets the resource_uid of this AssignmentItem.  # noqa: E501

        Uid of the resource.  # noqa: E501

        :return: The resource_uid of this AssignmentItem.  # noqa: E501
        :rtype: int
        """
        return self._resource_uid

    @resource_uid.setter
    def resource_uid(self, resource_uid):
        """Sets the resource_uid of this AssignmentItem.

        Uid of the resource.  # noqa: E501

        :param resource_uid: The resource_uid of this AssignmentItem.  # noqa: E501
        :type: int
        """
        if resource_uid is None:
            raise ValueError("Invalid value for `resource_uid`, must not be `None`")  # noqa: E501
        self._resource_uid = resource_uid
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
        if not isinstance(other, AssignmentItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
