# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="TableTextStyle.py">
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


class TableTextStyle(object):
    """Represents a text style in a view table.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'row_uid': 'int',
        'field': 'Field',
        'item_type': 'TextItemType',
        'color': 'Colors',
        'background_pattern': 'BackgroundPattern',
        'background_color': 'Colors'
    }

    attribute_map = {
        'row_uid': 'rowUid',
        'field': 'field',
        'item_type': 'itemType',
        'color': 'color',
        'background_pattern': 'backgroundPattern',
        'background_color': 'backgroundColor'
    }

    def __init__(self, row_uid=None, field=None, item_type=None, color=None, background_pattern=None, background_color=None):  # noqa: E501
        """TableTextStyle - a model defined in Swagger"""  # noqa: E501

        self._row_uid = None
        self._field = None
        self._item_type = None
        self._color = None
        self._background_pattern = None
        self._background_color = None
        self.discriminator = None

        if row_uid is not None:
            self.row_uid = row_uid
        if field is not None:
            self.field = field
        if item_type is not None:
            self.item_type = item_type
        if color is not None:
            self.color = color
        if background_pattern is not None:
            self.background_pattern = background_pattern
        if background_color is not None:
            self.background_color = background_color

    @property
    def row_uid(self):
        """Gets the row_uid of this TableTextStyle.  # noqa: E501

        Gets a row unique id. Return -1 if the style is to be applied to all rows of a view.  # noqa: E501

        :return: The row_uid of this TableTextStyle.  # noqa: E501
        :rtype: int
        """
        return self._row_uid

    @row_uid.setter
    def row_uid(self, row_uid):
        """Sets the row_uid of this TableTextStyle.

        Gets a row unique id. Return -1 if the style is to be applied to all rows of a view.  # noqa: E501

        :param row_uid: The row_uid of this TableTextStyle.  # noqa: E501
        :type: int
        """
        if row_uid is None:
            raise ValueError("Invalid value for `row_uid`, must not be `None`")  # noqa: E501
        self._row_uid = row_uid
    @property
    def field(self):
        """Gets the field of this TableTextStyle.  # noqa: E501

        Gets or sets a field the style is to be applied to.  # noqa: E501

        :return: The field of this TableTextStyle.  # noqa: E501
        :rtype: Field
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this TableTextStyle.

        Gets or sets a field the style is to be applied to.  # noqa: E501

        :param field: The field of this TableTextStyle.  # noqa: E501
        :type: Field
        """
        if field is None:
            raise ValueError("Invalid value for `field`, must not be `None`")  # noqa: E501
        self._field = field
    @property
    def item_type(self):
        """Gets the item_type of this TableTextStyle.  # noqa: E501

        Returns a value of the TextItemType enum.  # noqa: E501

        :return: The item_type of this TableTextStyle.  # noqa: E501
        :rtype: TextItemType
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type):
        """Sets the item_type of this TableTextStyle.

        Returns a value of the TextItemType enum.  # noqa: E501

        :param item_type: The item_type of this TableTextStyle.  # noqa: E501
        :type: TextItemType
        """
        if item_type is None:
            raise ValueError("Invalid value for `item_type`, must not be `None`")  # noqa: E501
        self._item_type = item_type
    @property
    def color(self):
        """Gets the color of this TableTextStyle.  # noqa: E501

        Gets or sets color of the text.  # noqa: E501

        :return: The color of this TableTextStyle.  # noqa: E501
        :rtype: Colors
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this TableTextStyle.

        Gets or sets color of the text.  # noqa: E501

        :param color: The color of this TableTextStyle.  # noqa: E501
        :type: Colors
        """
        if color is None:
            raise ValueError("Invalid value for `color`, must not be `None`")  # noqa: E501
        self._color = color
    @property
    def background_pattern(self):
        """Gets the background_pattern of this TableTextStyle.  # noqa: E501

        Gets or sets background pattern of the text style.  # noqa: E501

        :return: The background_pattern of this TableTextStyle.  # noqa: E501
        :rtype: BackgroundPattern
        """
        return self._background_pattern

    @background_pattern.setter
    def background_pattern(self, background_pattern):
        """Sets the background_pattern of this TableTextStyle.

        Gets or sets background pattern of the text style.  # noqa: E501

        :param background_pattern: The background_pattern of this TableTextStyle.  # noqa: E501
        :type: BackgroundPattern
        """
        if background_pattern is None:
            raise ValueError("Invalid value for `background_pattern`, must not be `None`")  # noqa: E501
        self._background_pattern = background_pattern
    @property
    def background_color(self):
        """Gets the background_color of this TableTextStyle.  # noqa: E501

        Gets or sets background color of the text style.  # noqa: E501

        :return: The background_color of this TableTextStyle.  # noqa: E501
        :rtype: Colors
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """Sets the background_color of this TableTextStyle.

        Gets or sets background color of the text style.  # noqa: E501

        :param background_color: The background_color of this TableTextStyle.  # noqa: E501
        :type: Colors
        """
        if background_color is None:
            raise ValueError("Invalid value for `background_color`, must not be `None`")  # noqa: E501
        self._background_color = background_color
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
        if not isinstance(other, TableTextStyle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
