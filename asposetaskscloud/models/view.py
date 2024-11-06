# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="View.py">
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


class View(object):
    """Represents a view in Project
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'show_in_menu': 'bool',
        'type': 'ItemType',
        'screen': 'ViewScreen',
        'name': 'str',
        'uid': 'int'
    }

    attribute_map = {
        'show_in_menu': 'showInMenu',
        'type': 'type',
        'screen': 'screen',
        'name': 'name',
        'uid': 'uid'
    }

    def __init__(self, show_in_menu=None, type=None, screen=None, name=None, uid=None):  # noqa: E501
        """View - a model defined in Swagger"""  # noqa: E501

        self._show_in_menu = None
        self._type = None
        self._screen = None
        self._name = None
        self._uid = None
        self.discriminator = None

        if show_in_menu is not None:
            self.show_in_menu = show_in_menu
        if type is not None:
            self.type = type
        if screen is not None:
            self.screen = screen
        if name is not None:
            self.name = name
        if uid is not None:
            self.uid = uid

    @property
    def show_in_menu(self):
        """Gets the show_in_menu of this View.  # noqa: E501

        Gets or sets a value indicating whether Microsoft Project shows the single view  name in the View or the Other Views drop-down lists in the Ribbon  # noqa: E501

        :return: The show_in_menu of this View.  # noqa: E501
        :rtype: bool
        """
        return self._show_in_menu

    @show_in_menu.setter
    def show_in_menu(self, show_in_menu):
        """Sets the show_in_menu of this View.

        Gets or sets a value indicating whether Microsoft Project shows the single view  name in the View or the Other Views drop-down lists in the Ribbon  # noqa: E501

        :param show_in_menu: The show_in_menu of this View.  # noqa: E501
        :type: bool
        """
        if show_in_menu is None:
            raise ValueError("Invalid value for `show_in_menu`, must not be `None`")  # noqa: E501
        self._show_in_menu = show_in_menu
    @property
    def type(self):
        """Gets the type of this View.  # noqa: E501

        Gets the type of item in the single view, such as tasks or resources. Read-only.  # noqa: E501

        :return: The type of this View.  # noqa: E501
        :rtype: ItemType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this View.

        Gets the type of item in the single view, such as tasks or resources. Read-only.  # noqa: E501

        :param type: The type of this View.  # noqa: E501
        :type: ItemType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type
    @property
    def screen(self):
        """Gets the screen of this View.  # noqa: E501

        Gets the screen type for the single view. Read-only.  # noqa: E501

        :return: The screen of this View.  # noqa: E501
        :rtype: ViewScreen
        """
        return self._screen

    @screen.setter
    def screen(self, screen):
        """Sets the screen of this View.

        Gets the screen type for the single view. Read-only.  # noqa: E501

        :param screen: The screen of this View.  # noqa: E501
        :type: ViewScreen
        """
        if screen is None:
            raise ValueError("Invalid value for `screen`, must not be `None`")  # noqa: E501
        self._screen = screen
    @property
    def name(self):
        """Gets the name of this View.  # noqa: E501

        Gets or sets the name of a view object.  # noqa: E501

        :return: The name of this View.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this View.

        Gets or sets the name of a view object.  # noqa: E501

        :param name: The name of this View.  # noqa: E501
        :type: str
        """
        self._name = name
    @property
    def uid(self):
        """Gets the uid of this View.  # noqa: E501

        Gets the unique identifier of a view.  # noqa: E501

        :return: The uid of this View.  # noqa: E501
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this View.

        Gets the unique identifier of a view.  # noqa: E501

        :param uid: The uid of this View.  # noqa: E501
        :type: int
        """
        if uid is None:
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501
        self._uid = uid
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
        if not isinstance(other, View):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
