# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="Colors.py">
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


class Colors(object):
    """
    """

    """
    allowed enum values
    """
    MEDIUMAQUAMARINE = "MediumAquamarine"
    MEDIUMBLUE = "MediumBlue"
    MEDIUMORCHID = "MediumOrchid"
    MEDIUMPURPLE = "MediumPurple"
    MEDIUMSEAGREEN = "MediumSeaGreen"
    MEDIUMSLATEBLUE = "MediumSlateBlue"
    MEDIUMSPRINGGREEN = "MediumSpringGreen"
    MAROON = "Maroon"
    MEDIUMTURQUOISE = "MediumTurquoise"
    MIDNIGHTBLUE = "MidnightBlue"
    MINTCREAM = "MintCream"
    MISTYROSE = "MistyRose"
    MOCCASIN = "Moccasin"
    NAVAJOWHITE = "NavajoWhite"
    NAVY = "Navy"
    OLDLACE = "OldLace"
    MEDIUMVIOLETRED = "MediumVioletRed"
    MAGENTA = "Magenta"
    LINEN = "Linen"
    LIMEGREEN = "LimeGreen"
    LAVENDERBLUSH = "LavenderBlush"
    LAWNGREEN = "LawnGreen"
    LEMONCHIFFON = "LemonChiffon"
    LIGHTBLUE = "LightBlue"
    LIGHTCORAL = "LightCoral"
    LIGHTCYAN = "LightCyan"
    LIGHTGOLDENRODYELLOW = "LightGoldenrodYellow"
    LIGHTGRAY = "LightGray"
    LIGHTGREEN = "LightGreen"
    LIGHTPINK = "LightPink"
    LIGHTSALMON = "LightSalmon"
    LIGHTSEAGREEN = "LightSeaGreen"
    LIGHTSKYBLUE = "LightSkyBlue"
    LIGHTSLATEGRAY = "LightSlateGray"
    LIGHTSTEELBLUE = "LightSteelBlue"
    LIGHTYELLOW = "LightYellow"
    LIME = "Lime"
    OLIVE = "Olive"
    OLIVEDRAB = "OliveDrab"
    ORANGE = "Orange"
    ORANGERED = "OrangeRed"
    SILVER = "Silver"
    SKYBLUE = "SkyBlue"
    SLATEBLUE = "SlateBlue"
    SLATEGRAY = "SlateGray"
    SNOW = "Snow"
    SPRINGGREEN = "SpringGreen"
    STEELBLUE = "SteelBlue"
    TAN = "Tan"
    TEAL = "Teal"
    THISTLE = "Thistle"
    TOMATO = "Tomato"
    TRANSPARENT = "Transparent"
    TURQUOISE = "Turquoise"
    VIOLET = "Violet"
    WHEAT = "Wheat"
    WHITE = "White"
    WHITESMOKE = "WhiteSmoke"
    SIENNA = "Sienna"
    LAVENDER = "Lavender"
    SEASHELL = "SeaShell"
    SANDYBROWN = "SandyBrown"
    ORCHID = "Orchid"
    PALEGOLDENROD = "PaleGoldenrod"
    PALEGREEN = "PaleGreen"
    PALETURQUOISE = "PaleTurquoise"
    PALEVIOLETRED = "PaleVioletRed"
    PAPAYAWHIP = "PapayaWhip"
    PEACHPUFF = "PeachPuff"
    PERU = "Peru"
    PINK = "Pink"
    PLUM = "Plum"
    POWDERBLUE = "PowderBlue"
    PURPLE = "Purple"
    RED = "Red"
    ROSYBROWN = "RosyBrown"
    ROYALBLUE = "RoyalBlue"
    SADDLEBROWN = "SaddleBrown"
    SALMON = "Salmon"
    SEAGREEN = "SeaGreen"
    YELLOW = "Yellow"
    KHAKI = "Khaki"
    CYAN = "Cyan"
    DARKMAGENTA = "DarkMagenta"
    DARKKHAKI = "DarkKhaki"
    DARKGREEN = "DarkGreen"
    DARKGRAY = "DarkGray"
    DARKGOLDENROD = "DarkGoldenrod"
    DARKCYAN = "DarkCyan"
    DARKBLUE = "DarkBlue"
    IVORY = "Ivory"
    CRIMSON = "Crimson"
    CORNSILK = "Cornsilk"
    CORNFLOWERBLUE = "CornflowerBlue"
    CORAL = "Coral"
    CHOCOLATE = "Chocolate"
    DARKOLIVEGREEN = "DarkOliveGreen"
    CHARTREUSE = "Chartreuse"
    BURLYWOOD = "BurlyWood"
    BROWN = "Brown"
    BLUEVIOLET = "BlueViolet"
    BLUE = "Blue"
    BLANCHEDALMOND = "BlanchedAlmond"
    BLACK = "Black"
    BISQUE = "Bisque"
    BEIGE = "Beige"
    AZURE = "Azure"
    AQUAMARINE = "Aquamarine"
    AQUA = "Aqua"
    ANTIQUEWHITE = "AntiqueWhite"
    ALICEBLUE = "AliceBlue"
    CADETBLUE = "CadetBlue"
    DARKORANGE = "DarkOrange"
    YELLOWGREEN = "YellowGreen"
    DARKRED = "DarkRed"
    INDIGO = "Indigo"
    INDIANRED = "IndianRed"
    DARKORCHID = "DarkOrchid"
    HONEYDEW = "Honeydew"
    GREENYELLOW = "GreenYellow"
    GREEN = "Green"
    GRAY = "Gray"
    GOLDENROD = "Goldenrod"
    GOLD = "Gold"
    GHOSTWHITE = "GhostWhite"
    GAINSBORO = "Gainsboro"
    FUCHSIA = "Fuchsia"
    FORESTGREEN = "ForestGreen"
    HOTPINK = "HotPink"
    FIREBRICK = "Firebrick"
    FLORALWHITE = "FloralWhite"
    DODGERBLUE = "DodgerBlue"
    DIMGRAY = "DimGray"
    DEEPSKYBLUE = "DeepSkyBlue"
    DEEPPINK = "DeepPink"
    DARKVIOLET = "DarkViolet"
    DARKTURQUOISE = "DarkTurquoise"
    DARKSLATEGRAY = "DarkSlateGray"
    DARKSLATEBLUE = "DarkSlateBlue"
    DARKSEAGREEN = "DarkSeaGreen"
    DARKSALMON = "DarkSalmon"

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
        """Colors - a model defined in Swagger"""  # noqa: E501
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
        if not isinstance(other, Colors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
