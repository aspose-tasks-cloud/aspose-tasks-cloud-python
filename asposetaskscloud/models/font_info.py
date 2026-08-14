# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="FontInfo.py">
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


class FontInfo(object):
    """Represents a brief read-only information about a font used in a group criterion.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'font_family': 'str',
        'size': 'float',
        'style': 'str'
    }

    attribute_map = {
        'font_family': 'fontFamily',
        'size': 'size',
        'style': 'style'
    }

    def __init__(self, font_family=None, size=None, style=None):  # noqa: E501
        """FontInfo - a model defined in Swagger"""  # noqa: E501

        self._font_family = None
        self._size = None
        self._style = None
        self.discriminator = None

        if font_family is not None:
            self.font_family = font_family
        if size is not None:
            self.size = size
        if style is not None:
            self.style = style

    @property
    def font_family(self):
        """Gets the font_family of this FontInfo.  # noqa: E501

        Gets or sets the font family name.  # noqa: E501

        :return: The font_family of this FontInfo.  # noqa: E501
        :rtype: str
        """
        return self._font_family

    @font_family.setter
    def font_family(self, font_family):
        """Sets the font_family of this FontInfo.

        Gets or sets the font family name.  # noqa: E501

        :param font_family: The font_family of this FontInfo.  # noqa: E501
        :type: str
        """
        self._font_family = font_family
    @property
    def size(self):
        """Gets the size of this FontInfo.  # noqa: E501

        Gets or sets the em-size of the font.  # noqa: E501

        :return: The size of this FontInfo.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FontInfo.

        Gets or sets the em-size of the font.  # noqa: E501

        :param size: The size of this FontInfo.  # noqa: E501
        :type: float
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501
        self._size = size
    @property
    def style(self):
        """Gets the style of this FontInfo.  # noqa: E501

        Gets or sets the style information applied to the font.  # noqa: E501

        :return: The style of this FontInfo.  # noqa: E501
        :rtype: str
        """
        return self._style

    @style.setter
    def style(self, style):
        """Sets the style of this FontInfo.

        Gets or sets the style information applied to the font.  # noqa: E501

        :param style: The style of this FontInfo.  # noqa: E501
        :type: str
        """
        self._style = style
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
        if not isinstance(other, FontInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
