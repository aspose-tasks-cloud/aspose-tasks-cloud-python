# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="TaskLink.py">
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


class TaskLink(object):
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
        'link': 'Link',
        'index': 'int',
        'predecessor_uid': 'int',
        'successor_uid': 'int',
        'link_type': 'TaskLinkType',
        'lag': 'int',
        'lag_format': 'TimeUnitType'
    }

    attribute_map = {
        'link': 'link',
        'index': 'index',
        'predecessor_uid': 'predecessorUid',
        'successor_uid': 'successorUid',
        'link_type': 'linkType',
        'lag': 'lag',
        'lag_format': 'lagFormat'
    }

    def __init__(self, link=None, index=None, predecessor_uid=None, successor_uid=None, link_type=None, lag=None, lag_format=None):  # noqa: E501
        """TaskLink - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._index = None
        self._predecessor_uid = None
        self._successor_uid = None
        self._link_type = None
        self._lag = None
        self._lag_format = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if index is not None:
            self.index = index
        if predecessor_uid is not None:
            self.predecessor_uid = predecessor_uid
        if successor_uid is not None:
            self.successor_uid = successor_uid
        if link_type is not None:
            self.link_type = link_type
        if lag is not None:
            self.lag = lag
        if lag_format is not None:
            self.lag_format = lag_format

    @property
    def link(self):
        """Gets the link of this TaskLink.  # noqa: E501


        :return: The link of this TaskLink.  # noqa: E501
        :rtype: Link
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this TaskLink.


        :param link: The link of this TaskLink.  # noqa: E501
        :type: Link
        """
        self._link = link
    @property
    def index(self):
        """Gets the index of this TaskLink.  # noqa: E501


        :return: The index of this TaskLink.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this TaskLink.


        :param index: The index of this TaskLink.  # noqa: E501
        :type: int
        """
        if index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501
        self._index = index
    @property
    def predecessor_uid(self):
        """Gets the predecessor_uid of this TaskLink.  # noqa: E501


        :return: The predecessor_uid of this TaskLink.  # noqa: E501
        :rtype: int
        """
        return self._predecessor_uid

    @predecessor_uid.setter
    def predecessor_uid(self, predecessor_uid):
        """Sets the predecessor_uid of this TaskLink.


        :param predecessor_uid: The predecessor_uid of this TaskLink.  # noqa: E501
        :type: int
        """
        if predecessor_uid is None:
            raise ValueError("Invalid value for `predecessor_uid`, must not be `None`")  # noqa: E501
        self._predecessor_uid = predecessor_uid
    @property
    def successor_uid(self):
        """Gets the successor_uid of this TaskLink.  # noqa: E501


        :return: The successor_uid of this TaskLink.  # noqa: E501
        :rtype: int
        """
        return self._successor_uid

    @successor_uid.setter
    def successor_uid(self, successor_uid):
        """Sets the successor_uid of this TaskLink.


        :param successor_uid: The successor_uid of this TaskLink.  # noqa: E501
        :type: int
        """
        if successor_uid is None:
            raise ValueError("Invalid value for `successor_uid`, must not be `None`")  # noqa: E501
        self._successor_uid = successor_uid
    @property
    def link_type(self):
        """Gets the link_type of this TaskLink.  # noqa: E501


        :return: The link_type of this TaskLink.  # noqa: E501
        :rtype: TaskLinkType
        """
        return self._link_type

    @link_type.setter
    def link_type(self, link_type):
        """Sets the link_type of this TaskLink.


        :param link_type: The link_type of this TaskLink.  # noqa: E501
        :type: TaskLinkType
        """
        if link_type is None:
            raise ValueError("Invalid value for `link_type`, must not be `None`")  # noqa: E501
        self._link_type = link_type
    @property
    def lag(self):
        """Gets the lag of this TaskLink.  # noqa: E501


        :return: The lag of this TaskLink.  # noqa: E501
        :rtype: int
        """
        return self._lag

    @lag.setter
    def lag(self, lag):
        """Sets the lag of this TaskLink.


        :param lag: The lag of this TaskLink.  # noqa: E501
        :type: int
        """
        if lag is None:
            raise ValueError("Invalid value for `lag`, must not be `None`")  # noqa: E501
        self._lag = lag
    @property
    def lag_format(self):
        """Gets the lag_format of this TaskLink.  # noqa: E501


        :return: The lag_format of this TaskLink.  # noqa: E501
        :rtype: TimeUnitType
        """
        return self._lag_format

    @lag_format.setter
    def lag_format(self, lag_format):
        """Sets the lag_format of this TaskLink.


        :param lag_format: The lag_format of this TaskLink.  # noqa: E501
        :type: TimeUnitType
        """
        if lag_format is None:
            raise ValueError("Invalid value for `lag_format`, must not be `None`")  # noqa: E501
        self._lag_format = lag_format
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
        if not isinstance(other, TaskLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
