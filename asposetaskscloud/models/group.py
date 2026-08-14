# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="Group.py">
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


class Group(object):
    """Represents a group definition. A Group object is a member of the ResourceGroups collection or the TaskGroups collection.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'uid': 'int',
        'name': 'str',
        'show_in_menu': 'bool',
        'show_summary': 'bool',
        'maintain_hierarchy': 'bool',
        'group_assignments': 'bool',
        'group_criteria': 'list[GroupCriterion]'
    }

    attribute_map = {
        'uid': 'uid',
        'name': 'name',
        'show_in_menu': 'showInMenu',
        'show_summary': 'showSummary',
        'maintain_hierarchy': 'maintainHierarchy',
        'group_assignments': 'groupAssignments',
        'group_criteria': 'groupCriteria'
    }

    def __init__(self, uid=None, name=None, show_in_menu=None, show_summary=None, maintain_hierarchy=None, group_assignments=None, group_criteria=None):  # noqa: E501
        """Group - a model defined in Swagger"""  # noqa: E501

        self._uid = None
        self._name = None
        self._show_in_menu = None
        self._show_summary = None
        self._maintain_hierarchy = None
        self._group_assignments = None
        self._group_criteria = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if name is not None:
            self.name = name
        if show_in_menu is not None:
            self.show_in_menu = show_in_menu
        if show_summary is not None:
            self.show_summary = show_summary
        if maintain_hierarchy is not None:
            self.maintain_hierarchy = maintain_hierarchy
        if group_assignments is not None:
            self.group_assignments = group_assignments
        if group_criteria is not None:
            self.group_criteria = group_criteria

    @property
    def uid(self):
        """Gets the uid of this Group.  # noqa: E501

        Gets or sets a unique identifier of a group.  # noqa: E501

        :return: The uid of this Group.  # noqa: E501
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this Group.

        Gets or sets a unique identifier of a group.  # noqa: E501

        :param uid: The uid of this Group.  # noqa: E501
        :type: int
        """
        if uid is None:
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501
        self._uid = uid
    @property
    def name(self):
        """Gets the name of this Group.  # noqa: E501

        Gets or sets a name of a Group object.  # noqa: E501

        :return: The name of this Group.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Group.

        Gets or sets a name of a Group object.  # noqa: E501

        :param name: The name of this Group.  # noqa: E501
        :type: str
        """
        self._name = name
    @property
    def show_in_menu(self):
        """Gets the show_in_menu of this Group.  # noqa: E501

        Gets or sets a value indicating whether Project shows the group name in the Group drop-down list in the Ribbon.  # noqa: E501

        :return: The show_in_menu of this Group.  # noqa: E501
        :rtype: bool
        """
        return self._show_in_menu

    @show_in_menu.setter
    def show_in_menu(self, show_in_menu):
        """Sets the show_in_menu of this Group.

        Gets or sets a value indicating whether Project shows the group name in the Group drop-down list in the Ribbon.  # noqa: E501

        :param show_in_menu: The show_in_menu of this Group.  # noqa: E501
        :type: bool
        """
        if show_in_menu is None:
            raise ValueError("Invalid value for `show_in_menu`, must not be `None`")  # noqa: E501
        self._show_in_menu = show_in_menu
    @property
    def show_summary(self):
        """Gets the show_summary of this Group.  # noqa: E501

        Gets or sets a value indicating whether summary rows are displayed for the group.  # noqa: E501

        :return: The show_summary of this Group.  # noqa: E501
        :rtype: bool
        """
        return self._show_summary

    @show_summary.setter
    def show_summary(self, show_summary):
        """Sets the show_summary of this Group.

        Gets or sets a value indicating whether summary rows are displayed for the group.  # noqa: E501

        :param show_summary: The show_summary of this Group.  # noqa: E501
        :type: bool
        """
        if show_summary is None:
            raise ValueError("Invalid value for `show_summary`, must not be `None`")  # noqa: E501
        self._show_summary = show_summary
    @property
    def maintain_hierarchy(self):
        """Gets the maintain_hierarchy of this Group.  # noqa: E501

        Gets or sets a value indicating whether to show all the levels of summary tasks for subtasks within group.  # noqa: E501

        :return: The maintain_hierarchy of this Group.  # noqa: E501
        :rtype: bool
        """
        return self._maintain_hierarchy

    @maintain_hierarchy.setter
    def maintain_hierarchy(self, maintain_hierarchy):
        """Sets the maintain_hierarchy of this Group.

        Gets or sets a value indicating whether to show all the levels of summary tasks for subtasks within group.  # noqa: E501

        :param maintain_hierarchy: The maintain_hierarchy of this Group.  # noqa: E501
        :type: bool
        """
        if maintain_hierarchy is None:
            raise ValueError("Invalid value for `maintain_hierarchy`, must not be `None`")  # noqa: E501
        self._maintain_hierarchy = maintain_hierarchy
    @property
    def group_assignments(self):
        """Gets the group_assignments of this Group.  # noqa: E501

        Gets or sets a value indicating whether assignments should be grouped instead of tasks.  # noqa: E501

        :return: The group_assignments of this Group.  # noqa: E501
        :rtype: bool
        """
        return self._group_assignments

    @group_assignments.setter
    def group_assignments(self, group_assignments):
        """Sets the group_assignments of this Group.

        Gets or sets a value indicating whether assignments should be grouped instead of tasks.  # noqa: E501

        :param group_assignments: The group_assignments of this Group.  # noqa: E501
        :type: bool
        """
        if group_assignments is None:
            raise ValueError("Invalid value for `group_assignments`, must not be `None`")  # noqa: E501
        self._group_assignments = group_assignments
    @property
    def group_criteria(self):
        """Gets the group_criteria of this Group.  # noqa: E501

        Gets or sets a collection of criteria representing the fields in a group definition.  # noqa: E501

        :return: The group_criteria of this Group.  # noqa: E501
        :rtype: list[GroupCriterion]
        """
        return self._group_criteria

    @group_criteria.setter
    def group_criteria(self, group_criteria):
        """Sets the group_criteria of this Group.

        Gets or sets a collection of criteria representing the fields in a group definition.  # noqa: E501

        :param group_criteria: The group_criteria of this Group.  # noqa: E501
        :type: list[GroupCriterion]
        """
        self._group_criteria = group_criteria
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
        if not isinstance(other, Group):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
