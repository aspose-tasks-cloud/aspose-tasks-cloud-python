# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="OutlineCodeDefinition.py">
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


class OutlineCodeDefinition(object):
    """Represents an outline code definition.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'guid': 'str',
        'field_id': 'str',
        'field_name': 'str',
        'alias': 'str',
        'phonetic_alias': 'str',
        'values': 'list[OutlineValue]',
        'enterprise': 'bool',
        'enterprise_outline_code_alias': 'int',
        'resource_substitution_enabled': 'bool',
        'leaf_only': 'bool',
        'all_levels_required': 'bool',
        'only_table_values_allowed': 'bool',
        'masks': 'list[OutlineMask]',
        'show_indent': 'bool'
    }

    attribute_map = {
        'guid': 'guid',
        'field_id': 'fieldId',
        'field_name': 'fieldName',
        'alias': 'alias',
        'phonetic_alias': 'phoneticAlias',
        'values': 'values',
        'enterprise': 'enterprise',
        'enterprise_outline_code_alias': 'enterpriseOutlineCodeAlias',
        'resource_substitution_enabled': 'resourceSubstitutionEnabled',
        'leaf_only': 'leafOnly',
        'all_levels_required': 'allLevelsRequired',
        'only_table_values_allowed': 'onlyTableValuesAllowed',
        'masks': 'masks',
        'show_indent': 'showIndent'
    }

    def __init__(self, guid=None, field_id=None, field_name=None, alias=None, phonetic_alias=None, values=None, enterprise=None, enterprise_outline_code_alias=None, resource_substitution_enabled=None, leaf_only=None, all_levels_required=None, only_table_values_allowed=None, masks=None, show_indent=None):  # noqa: E501
        """OutlineCodeDefinition - a model defined in Swagger"""  # noqa: E501

        self._guid = None
        self._field_id = None
        self._field_name = None
        self._alias = None
        self._phonetic_alias = None
        self._values = None
        self._enterprise = None
        self._enterprise_outline_code_alias = None
        self._resource_substitution_enabled = None
        self._leaf_only = None
        self._all_levels_required = None
        self._only_table_values_allowed = None
        self._masks = None
        self._show_indent = None
        self.discriminator = None

        if guid is not None:
            self.guid = guid
        if field_id is not None:
            self.field_id = field_id
        if field_name is not None:
            self.field_name = field_name
        if alias is not None:
            self.alias = alias
        if phonetic_alias is not None:
            self.phonetic_alias = phonetic_alias
        if values is not None:
            self.values = values
        if enterprise is not None:
            self.enterprise = enterprise
        if enterprise_outline_code_alias is not None:
            self.enterprise_outline_code_alias = enterprise_outline_code_alias
        if resource_substitution_enabled is not None:
            self.resource_substitution_enabled = resource_substitution_enabled
        if leaf_only is not None:
            self.leaf_only = leaf_only
        if all_levels_required is not None:
            self.all_levels_required = all_levels_required
        if only_table_values_allowed is not None:
            self.only_table_values_allowed = only_table_values_allowed
        if masks is not None:
            self.masks = masks
        if show_indent is not None:
            self.show_indent = show_indent

    @property
    def guid(self):
        """Gets the guid of this OutlineCodeDefinition.  # noqa: E501

        The Guid of an outline code.  # noqa: E501

        :return: The guid of this OutlineCodeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this OutlineCodeDefinition.

        The Guid of an outline code.  # noqa: E501

        :param guid: The guid of this OutlineCodeDefinition.  # noqa: E501
        :type: str
        """
        self._guid = guid
    @property
    def field_id(self):
        """Gets the field_id of this OutlineCodeDefinition.  # noqa: E501

        Corresponds to the field number of an outline code.  # noqa: E501

        :return: The field_id of this OutlineCodeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this OutlineCodeDefinition.

        Corresponds to the field number of an outline code.  # noqa: E501

        :param field_id: The field_id of this OutlineCodeDefinition.  # noqa: E501
        :type: str
        """
        self._field_id = field_id
    @property
    def field_name(self):
        """Gets the field_name of this OutlineCodeDefinition.  # noqa: E501

        The name of a custom outline code.  # noqa: E501

        :return: The field_name of this OutlineCodeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this OutlineCodeDefinition.

        The name of a custom outline code.  # noqa: E501

        :param field_name: The field_name of this OutlineCodeDefinition.  # noqa: E501
        :type: str
        """
        self._field_name = field_name
    @property
    def alias(self):
        """Gets the alias of this OutlineCodeDefinition.  # noqa: E501

        The alias of a custom outline code.  # noqa: E501

        :return: The alias of this OutlineCodeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this OutlineCodeDefinition.

        The alias of a custom outline code.  # noqa: E501

        :param alias: The alias of this OutlineCodeDefinition.  # noqa: E501
        :type: str
        """
        self._alias = alias
    @property
    def phonetic_alias(self):
        """Gets the phonetic_alias of this OutlineCodeDefinition.  # noqa: E501

        The phonetic pronunciation of the alias of the custom outline code.  # noqa: E501

        :return: The phonetic_alias of this OutlineCodeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._phonetic_alias

    @phonetic_alias.setter
    def phonetic_alias(self, phonetic_alias):
        """Sets the phonetic_alias of this OutlineCodeDefinition.

        The phonetic pronunciation of the alias of the custom outline code.  # noqa: E501

        :param phonetic_alias: The phonetic_alias of this OutlineCodeDefinition.  # noqa: E501
        :type: str
        """
        self._phonetic_alias = phonetic_alias
    @property
    def values(self):
        """Gets the values of this OutlineCodeDefinition.  # noqa: E501

        Returns List&lt;OutlineValue&gt; Values. The values of the table associated with this outline code.  # noqa: E501

        :return: The values of this OutlineCodeDefinition.  # noqa: E501
        :rtype: list[OutlineValue]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this OutlineCodeDefinition.

        Returns List&lt;OutlineValue&gt; Values. The values of the table associated with this outline code.  # noqa: E501

        :param values: The values of this OutlineCodeDefinition.  # noqa: E501
        :type: list[OutlineValue]
        """
        self._values = values
    @property
    def enterprise(self):
        """Gets the enterprise of this OutlineCodeDefinition.  # noqa: E501

        Determines whether a custom outline code is an enterprise custom outline code.  # noqa: E501

        :return: The enterprise of this OutlineCodeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._enterprise

    @enterprise.setter
    def enterprise(self, enterprise):
        """Sets the enterprise of this OutlineCodeDefinition.

        Determines whether a custom outline code is an enterprise custom outline code.  # noqa: E501

        :param enterprise: The enterprise of this OutlineCodeDefinition.  # noqa: E501
        :type: bool
        """
        if enterprise is None:
            raise ValueError("Invalid value for `enterprise`, must not be `None`")  # noqa: E501
        self._enterprise = enterprise
    @property
    def enterprise_outline_code_alias(self):
        """Gets the enterprise_outline_code_alias of this OutlineCodeDefinition.  # noqa: E501

        The reference to another custom field for which this outline code definition is an alias.  # noqa: E501

        :return: The enterprise_outline_code_alias of this OutlineCodeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._enterprise_outline_code_alias

    @enterprise_outline_code_alias.setter
    def enterprise_outline_code_alias(self, enterprise_outline_code_alias):
        """Sets the enterprise_outline_code_alias of this OutlineCodeDefinition.

        The reference to another custom field for which this outline code definition is an alias.  # noqa: E501

        :param enterprise_outline_code_alias: The enterprise_outline_code_alias of this OutlineCodeDefinition.  # noqa: E501
        :type: int
        """
        if enterprise_outline_code_alias is None:
            raise ValueError("Invalid value for `enterprise_outline_code_alias`, must not be `None`")  # noqa: E501
        self._enterprise_outline_code_alias = enterprise_outline_code_alias
    @property
    def resource_substitution_enabled(self):
        """Gets the resource_substitution_enabled of this OutlineCodeDefinition.  # noqa: E501

        Determines whether the custom outline code can be used by the Resource Substitution Wizard in Microsoft Project.  # noqa: E501

        :return: The resource_substitution_enabled of this OutlineCodeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._resource_substitution_enabled

    @resource_substitution_enabled.setter
    def resource_substitution_enabled(self, resource_substitution_enabled):
        """Sets the resource_substitution_enabled of this OutlineCodeDefinition.

        Determines whether the custom outline code can be used by the Resource Substitution Wizard in Microsoft Project.  # noqa: E501

        :param resource_substitution_enabled: The resource_substitution_enabled of this OutlineCodeDefinition.  # noqa: E501
        :type: bool
        """
        if resource_substitution_enabled is None:
            raise ValueError("Invalid value for `resource_substitution_enabled`, must not be `None`")  # noqa: E501
        self._resource_substitution_enabled = resource_substitution_enabled
    @property
    def leaf_only(self):
        """Gets the leaf_only of this OutlineCodeDefinition.  # noqa: E501

        Determines whether the values specified in this outline code field must be leaf values.  # noqa: E501

        :return: The leaf_only of this OutlineCodeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._leaf_only

    @leaf_only.setter
    def leaf_only(self, leaf_only):
        """Sets the leaf_only of this OutlineCodeDefinition.

        Determines whether the values specified in this outline code field must be leaf values.  # noqa: E501

        :param leaf_only: The leaf_only of this OutlineCodeDefinition.  # noqa: E501
        :type: bool
        """
        if leaf_only is None:
            raise ValueError("Invalid value for `leaf_only`, must not be `None`")  # noqa: E501
        self._leaf_only = leaf_only
    @property
    def all_levels_required(self):
        """Gets the all_levels_required of this OutlineCodeDefinition.  # noqa: E501

        Determines whether the new codes must have all levels. Not available for Enterprise Codes.  # noqa: E501

        :return: The all_levels_required of this OutlineCodeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._all_levels_required

    @all_levels_required.setter
    def all_levels_required(self, all_levels_required):
        """Sets the all_levels_required of this OutlineCodeDefinition.

        Determines whether the new codes must have all levels. Not available for Enterprise Codes.  # noqa: E501

        :param all_levels_required: The all_levels_required of this OutlineCodeDefinition.  # noqa: E501
        :type: bool
        """
        if all_levels_required is None:
            raise ValueError("Invalid value for `all_levels_required`, must not be `None`")  # noqa: E501
        self._all_levels_required = all_levels_required
    @property
    def only_table_values_allowed(self):
        """Gets the only_table_values_allowed of this OutlineCodeDefinition.  # noqa: E501

        Determines whether the values specified must come from values table.  # noqa: E501

        :return: The only_table_values_allowed of this OutlineCodeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._only_table_values_allowed

    @only_table_values_allowed.setter
    def only_table_values_allowed(self, only_table_values_allowed):
        """Sets the only_table_values_allowed of this OutlineCodeDefinition.

        Determines whether the values specified must come from values table.  # noqa: E501

        :param only_table_values_allowed: The only_table_values_allowed of this OutlineCodeDefinition.  # noqa: E501
        :type: bool
        """
        if only_table_values_allowed is None:
            raise ValueError("Invalid value for `only_table_values_allowed`, must not be `None`")  # noqa: E501
        self._only_table_values_allowed = only_table_values_allowed
    @property
    def masks(self):
        """Gets the masks of this OutlineCodeDefinition.  # noqa: E501

        Returns List&lt;OutlineMask&gt; Masks. The table of entries that define the outline code mask.  # noqa: E501

        :return: The masks of this OutlineCodeDefinition.  # noqa: E501
        :rtype: list[OutlineMask]
        """
        return self._masks

    @masks.setter
    def masks(self, masks):
        """Sets the masks of this OutlineCodeDefinition.

        Returns List&lt;OutlineMask&gt; Masks. The table of entries that define the outline code mask.  # noqa: E501

        :param masks: The masks of this OutlineCodeDefinition.  # noqa: E501
        :type: list[OutlineMask]
        """
        self._masks = masks
    @property
    def show_indent(self):
        """Gets the show_indent of this OutlineCodeDefinition.  # noqa: E501

        Determines whether the indents of this outline code must be shown.  # noqa: E501

        :return: The show_indent of this OutlineCodeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._show_indent

    @show_indent.setter
    def show_indent(self, show_indent):
        """Sets the show_indent of this OutlineCodeDefinition.

        Determines whether the indents of this outline code must be shown.  # noqa: E501

        :param show_indent: The show_indent of this OutlineCodeDefinition.  # noqa: E501
        :type: bool
        """
        if show_indent is None:
            raise ValueError("Invalid value for `show_indent`, must not be `None`")  # noqa: E501
        self._show_indent = show_indent
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
        if not isinstance(other, OutlineCodeDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
