# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="GroupCriterion.py">
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


class GroupCriterion(object):
    """Represents a criterion in a group definition.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'field': 'Field',
        'ascending': 'bool',
        'group_on': 'GroupOn',
        'group_interval': 'str',
        'start_at': 'str',
        'cell_color': 'Colors',
        'font_color': 'Colors',
        'pattern': 'BackgroundPattern',
        'font': 'FontInfo'
    }

    attribute_map = {
        'field': 'field',
        'ascending': 'ascending',
        'group_on': 'groupOn',
        'group_interval': 'groupInterval',
        'start_at': 'startAt',
        'cell_color': 'cellColor',
        'font_color': 'fontColor',
        'pattern': 'pattern',
        'font': 'font'
    }

    def __init__(self, field=None, ascending=None, group_on=None, group_interval=None, start_at=None, cell_color=None, font_color=None, pattern=None, font=None):  # noqa: E501
        """GroupCriterion - a model defined in Swagger"""  # noqa: E501

        self._field = None
        self._ascending = None
        self._group_on = None
        self._group_interval = None
        self._start_at = None
        self._cell_color = None
        self._font_color = None
        self._pattern = None
        self._font = None
        self.discriminator = None

        if field is not None:
            self.field = field
        if ascending is not None:
            self.ascending = ascending
        if group_on is not None:
            self.group_on = group_on
        if group_interval is not None:
            self.group_interval = group_interval
        if start_at is not None:
            self.start_at = start_at
        if cell_color is not None:
            self.cell_color = cell_color
        if font_color is not None:
            self.font_color = font_color
        if pattern is not None:
            self.pattern = pattern
        if font is not None:
            self.font = font

    @property
    def field(self):
        """Gets the field of this GroupCriterion.  # noqa: E501

        Gets or sets the field being grouped by.  # noqa: E501

        :return: The field of this GroupCriterion.  # noqa: E501
        :rtype: Field
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this GroupCriterion.

        Gets or sets the field being grouped by.  # noqa: E501

        :param field: The field of this GroupCriterion.  # noqa: E501
        :type: Field
        """
        if field is None:
            raise ValueError("Invalid value for `field`, must not be `None`")  # noqa: E501
        self._field = field
    @property
    def ascending(self):
        """Gets the ascending of this GroupCriterion.  # noqa: E501

        Gets or sets a value indicating whether a field used as a criterion in a group definition is sorted in ascending order. False if the field is sorted in descending order.  # noqa: E501

        :return: The ascending of this GroupCriterion.  # noqa: E501
        :rtype: bool
        """
        return self._ascending

    @ascending.setter
    def ascending(self, ascending):
        """Sets the ascending of this GroupCriterion.

        Gets or sets a value indicating whether a field used as a criterion in a group definition is sorted in ascending order. False if the field is sorted in descending order.  # noqa: E501

        :param ascending: The ascending of this GroupCriterion.  # noqa: E501
        :type: bool
        """
        if ascending is None:
            raise ValueError("Invalid value for `ascending`, must not be `None`")  # noqa: E501
        self._ascending = ascending
    @property
    def group_on(self):
        """Gets the group_on of this GroupCriterion.  # noqa: E501

        Gets or sets the type of grouping for a field used as a criterion in a group definition.  # noqa: E501

        :return: The group_on of this GroupCriterion.  # noqa: E501
        :rtype: GroupOn
        """
        return self._group_on

    @group_on.setter
    def group_on(self, group_on):
        """Sets the group_on of this GroupCriterion.

        Gets or sets the type of grouping for a field used as a criterion in a group definition.  # noqa: E501

        :param group_on: The group_on of this GroupCriterion.  # noqa: E501
        :type: GroupOn
        """
        if group_on is None:
            raise ValueError("Invalid value for `group_on`, must not be `None`")  # noqa: E501
        self._group_on = group_on
    @property
    def group_interval(self):
        """Gets the group_interval of this GroupCriterion.  # noqa: E501

        Gets or sets the interval for a field used as a criterion in a group definition.  # noqa: E501

        :return: The group_interval of this GroupCriterion.  # noqa: E501
        :rtype: str
        """
        return self._group_interval

    @group_interval.setter
    def group_interval(self, group_interval):
        """Sets the group_interval of this GroupCriterion.

        Gets or sets the interval for a field used as a criterion in a group definition.  # noqa: E501

        :param group_interval: The group_interval of this GroupCriterion.  # noqa: E501
        :type: str
        """
        self._group_interval = group_interval
    @property
    def start_at(self):
        """Gets the start_at of this GroupCriterion.  # noqa: E501

        Gets or sets the start of the intervals for a field used as a criterion in a group definition.  # noqa: E501

        :return: The start_at of this GroupCriterion.  # noqa: E501
        :rtype: str
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        """Sets the start_at of this GroupCriterion.

        Gets or sets the start of the intervals for a field used as a criterion in a group definition.  # noqa: E501

        :param start_at: The start_at of this GroupCriterion.  # noqa: E501
        :type: str
        """
        self._start_at = start_at
    @property
    def cell_color(self):
        """Gets the cell_color of this GroupCriterion.  # noqa: E501

        Gets or sets the color of the cell background for a field used as a criterion in a group definition.  # noqa: E501

        :return: The cell_color of this GroupCriterion.  # noqa: E501
        :rtype: Colors
        """
        return self._cell_color

    @cell_color.setter
    def cell_color(self, cell_color):
        """Sets the cell_color of this GroupCriterion.

        Gets or sets the color of the cell background for a field used as a criterion in a group definition.  # noqa: E501

        :param cell_color: The cell_color of this GroupCriterion.  # noqa: E501
        :type: Colors
        """
        if cell_color is None:
            raise ValueError("Invalid value for `cell_color`, must not be `None`")  # noqa: E501
        self._cell_color = cell_color
    @property
    def font_color(self):
        """Gets the font_color of this GroupCriterion.  # noqa: E501

        Gets or sets the color of the font for a field used as a criterion in a group definition.  # noqa: E501

        :return: The font_color of this GroupCriterion.  # noqa: E501
        :rtype: Colors
        """
        return self._font_color

    @font_color.setter
    def font_color(self, font_color):
        """Sets the font_color of this GroupCriterion.

        Gets or sets the color of the font for a field used as a criterion in a group definition.  # noqa: E501

        :param font_color: The font_color of this GroupCriterion.  # noqa: E501
        :type: Colors
        """
        if font_color is None:
            raise ValueError("Invalid value for `font_color`, must not be `None`")  # noqa: E501
        self._font_color = font_color
    @property
    def pattern(self):
        """Gets the pattern of this GroupCriterion.  # noqa: E501

        Gets or sets the pattern of the cell for a field used as a criterion in a group definition.  # noqa: E501

        :return: The pattern of this GroupCriterion.  # noqa: E501
        :rtype: BackgroundPattern
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this GroupCriterion.

        Gets or sets the pattern of the cell for a field used as a criterion in a group definition.  # noqa: E501

        :param pattern: The pattern of this GroupCriterion.  # noqa: E501
        :type: BackgroundPattern
        """
        if pattern is None:
            raise ValueError("Invalid value for `pattern`, must not be `None`")  # noqa: E501
        self._pattern = pattern
    @property
    def font(self):
        """Gets the font of this GroupCriterion.  # noqa: E501

        Gets or sets the font for a criterion in a group definition.  # noqa: E501

        :return: The font of this GroupCriterion.  # noqa: E501
        :rtype: FontInfo
        """
        return self._font

    @font.setter
    def font(self, font):
        """Sets the font of this GroupCriterion.

        Gets or sets the font for a criterion in a group definition.  # noqa: E501

        :param font: The font of this GroupCriterion.  # noqa: E501
        :type: FontInfo
        """
        self._font = font
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
        if not isinstance(other, GroupCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
