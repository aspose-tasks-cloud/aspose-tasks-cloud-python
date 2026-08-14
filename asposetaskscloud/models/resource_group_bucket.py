# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="ResourceGroupBucket.py">
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


class ResourceGroupBucket(object):
    """Represents a single bucket of a resource grouping result: the resources sharing the same group key.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'key': 'str',
        'resources': 'list[ResourceItem]'
    }

    attribute_map = {
        'key': 'key',
        'resources': 'resources'
    }

    def __init__(self, key=None, resources=None):  # noqa: E501
        """ResourceGroupBucket - a model defined in Swagger"""  # noqa: E501

        self._key = None
        self._resources = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if resources is not None:
            self.resources = resources

    @property
    def key(self):
        """Gets the key of this ResourceGroupBucket.  # noqa: E501

        The group key the bucketed resources share.  # noqa: E501

        :return: The key of this ResourceGroupBucket.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ResourceGroupBucket.

        The group key the bucketed resources share.  # noqa: E501

        :param key: The key of this ResourceGroupBucket.  # noqa: E501
        :type: str
        """
        self._key = key
    @property
    def resources(self):
        """Gets the resources of this ResourceGroupBucket.  # noqa: E501

        Resources falling into this bucket.  # noqa: E501

        :return: The resources of this ResourceGroupBucket.  # noqa: E501
        :rtype: list[ResourceItem]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ResourceGroupBucket.

        Resources falling into this bucket.  # noqa: E501

        :param resources: The resources of this ResourceGroupBucket.  # noqa: E501
        :type: list[ResourceItem]
        """
        self._resources = resources
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
        if not isinstance(other, ResourceGroupBucket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
