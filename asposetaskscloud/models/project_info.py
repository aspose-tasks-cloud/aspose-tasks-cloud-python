# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="ProjectInfo.py">
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


class ProjectInfo(object):
    """Brief info about the published project available on Project Online.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'created_date': 'datetime',
        'is_checked_out': 'bool',
        'last_published_date': 'datetime',
        'last_saved_date': 'datetime',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'created_date': 'createdDate',
        'is_checked_out': 'isCheckedOut',
        'last_published_date': 'lastPublishedDate',
        'last_saved_date': 'lastSavedDate',
        'description': 'description'
    }

    def __init__(self, id=None, name=None, created_date=None, is_checked_out=None, last_published_date=None, last_saved_date=None, description=None):  # noqa: E501
        """ProjectInfo - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._created_date = None
        self._is_checked_out = None
        self._last_published_date = None
        self._last_saved_date = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if created_date is not None:
            self.created_date = created_date
        if is_checked_out is not None:
            self.is_checked_out = is_checked_out
        if last_published_date is not None:
            self.last_published_date = last_published_date
        if last_saved_date is not None:
            self.last_saved_date = last_saved_date
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this ProjectInfo.  # noqa: E501

        The unique identifier of the project.  # noqa: E501

        :return: The id of this ProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectInfo.

        The unique identifier of the project.  # noqa: E501

        :param id: The id of this ProjectInfo.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        self._id = id
    @property
    def name(self):
        """Gets the name of this ProjectInfo.  # noqa: E501

        The name of the project.  # noqa: E501

        :return: The name of this ProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectInfo.

        The name of the project.  # noqa: E501

        :param name: The name of this ProjectInfo.  # noqa: E501
        :type: str
        """
        self._name = name
    @property
    def created_date(self):
        """Gets the created_date of this ProjectInfo.  # noqa: E501

        The date and time when the project was created.  # noqa: E501

        :return: The created_date of this ProjectInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this ProjectInfo.

        The date and time when the project was created.  # noqa: E501

        :param created_date: The created_date of this ProjectInfo.  # noqa: E501
        :type: datetime
        """
        if created_date is None:
            raise ValueError("Invalid value for `created_date`, must not be `None`")  # noqa: E501
        self._created_date = created_date
    @property
    def is_checked_out(self):
        """Gets the is_checked_out of this ProjectInfo.  # noqa: E501

        Value indicating whether the project is checked out.  # noqa: E501

        :return: The is_checked_out of this ProjectInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_checked_out

    @is_checked_out.setter
    def is_checked_out(self, is_checked_out):
        """Sets the is_checked_out of this ProjectInfo.

        Value indicating whether the project is checked out.  # noqa: E501

        :param is_checked_out: The is_checked_out of this ProjectInfo.  # noqa: E501
        :type: bool
        """
        if is_checked_out is None:
            raise ValueError("Invalid value for `is_checked_out`, must not be `None`")  # noqa: E501
        self._is_checked_out = is_checked_out
    @property
    def last_published_date(self):
        """Gets the last_published_date of this ProjectInfo.  # noqa: E501

        The most recent date when the project was published.  # noqa: E501

        :return: The last_published_date of this ProjectInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._last_published_date

    @last_published_date.setter
    def last_published_date(self, last_published_date):
        """Sets the last_published_date of this ProjectInfo.

        The most recent date when the project was published.  # noqa: E501

        :param last_published_date: The last_published_date of this ProjectInfo.  # noqa: E501
        :type: datetime
        """
        if last_published_date is None:
            raise ValueError("Invalid value for `last_published_date`, must not be `None`")  # noqa: E501
        self._last_published_date = last_published_date
    @property
    def last_saved_date(self):
        """Gets the last_saved_date of this ProjectInfo.  # noqa: E501

        The most recent date when the project was saved.  # noqa: E501

        :return: The last_saved_date of this ProjectInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._last_saved_date

    @last_saved_date.setter
    def last_saved_date(self, last_saved_date):
        """Sets the last_saved_date of this ProjectInfo.

        The most recent date when the project was saved.  # noqa: E501

        :param last_saved_date: The last_saved_date of this ProjectInfo.  # noqa: E501
        :type: datetime
        """
        if last_saved_date is None:
            raise ValueError("Invalid value for `last_saved_date`, must not be `None`")  # noqa: E501
        self._last_saved_date = last_saved_date
    @property
    def description(self):
        """Gets the description of this ProjectInfo.  # noqa: E501

        The description of the project.  # noqa: E501

        :return: The description of this ProjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectInfo.

        The description of the project.  # noqa: E501

        :param description: The description of this ProjectInfo.  # noqa: E501
        :type: str
        """
        self._description = description
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
        if not isinstance(other, ProjectInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
