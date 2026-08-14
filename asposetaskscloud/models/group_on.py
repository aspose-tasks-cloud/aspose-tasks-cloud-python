# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="GroupOn.py">
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


class GroupOn(object):
    """Specifies the type of grouping for a field used as a criterion in a group definition.
    """

    """
    allowed enum values
    """
    EACHVALUE = "EachValue"
    INTERVAL = "Interval"
    DATEEACHVALUE = "DateEachValue"
    DATEMINUTE = "DateMinute"
    DATEHOUR = "DateHour"
    DATEDAY = "DateDay"
    DATEWEEK = "DateWeek"
    DATETHIRDOFMONTH = "DateThirdOfMonth"
    DATEMONTH = "DateMonth"
    DATEQTR = "DateQtr"
    DATEYEAR = "DateYear"
    DURATIONEACHVALUE = "DurationEachValue"
    DURATIONMINUTES = "DurationMinutes"
    DURATIONHOURS = "DurationHours"
    DURATIONDAYS = "DurationDays"
    DURATIONWEEKS = "DurationWeeks"
    DURATIONMONTHS = "DurationMonths"
    OUTLINEEACHVALUE = "OutlineEachValue"
    OUTLINELEVEL = "OutlineLevel"
    PCTEACHVALUE = "PctEachValue"
    PCTINTERVAL = "PctInterval"
    PCT199 = "Pct199"
    PCT150 = "Pct150"
    PCT125 = "Pct125"
    PCT110 = "Pct110"
    TEXTEACHVALUE = "TextEachValue"
    TEXTPREFIX = "TextPrefix"

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """GroupOn - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

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
        if not isinstance(other, GroupOn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
