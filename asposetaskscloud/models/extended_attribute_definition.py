# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="ExtendedAttributeDefinition.py">
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


class ExtendedAttributeDefinition(object):
    """Extended attribute definition&#39;s brief into.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'field_id': 'str',
        'field_name': 'str',
        'cf_type': 'CustomFieldType',
        'guid': 'str',
        'element_type': 'ElementType',
        'max_multi_values': 'int',
        'user_def': 'bool',
        'alias': 'str',
        'secondary_pid': 'str',
        'auto_roll_down': 'bool',
        'default_guid': 'str',
        'lookup_uid': 'str',
        'phonetics_alias': 'str',
        'rollup_type': 'RollupType',
        'calculation_type': 'CalculationType',
        'formula': 'str',
        'restrict_values': 'bool',
        'valuelist_sort_order': 'int',
        'append_new_values': 'bool',
        'default': 'str',
        'value_list': 'list[Value]',
        'secondary_guid': 'str'
    }

    attribute_map = {
        'field_id': 'fieldId',
        'field_name': 'fieldName',
        'cf_type': 'cfType',
        'guid': 'guid',
        'element_type': 'elementType',
        'max_multi_values': 'maxMultiValues',
        'user_def': 'userDef',
        'alias': 'alias',
        'secondary_pid': 'secondaryPid',
        'auto_roll_down': 'autoRollDown',
        'default_guid': 'defaultGuid',
        'lookup_uid': 'lookupUid',
        'phonetics_alias': 'phoneticsAlias',
        'rollup_type': 'rollupType',
        'calculation_type': 'calculationType',
        'formula': 'formula',
        'restrict_values': 'restrictValues',
        'valuelist_sort_order': 'valuelistSortOrder',
        'append_new_values': 'appendNewValues',
        'default': 'default',
        'value_list': 'valueList',
        'secondary_guid': 'secondaryGuid'
    }

    def __init__(self, field_id=None, field_name=None, cf_type=None, guid=None, element_type=None, max_multi_values=None, user_def=None, alias=None, secondary_pid=None, auto_roll_down=None, default_guid=None, lookup_uid=None, phonetics_alias=None, rollup_type=None, calculation_type=None, formula=None, restrict_values=None, valuelist_sort_order=None, append_new_values=None, default=None, value_list=None, secondary_guid=None):  # noqa: E501
        """ExtendedAttributeDefinition - a model defined in Swagger"""  # noqa: E501

        self._field_id = None
        self._field_name = None
        self._cf_type = None
        self._guid = None
        self._element_type = None
        self._max_multi_values = None
        self._user_def = None
        self._alias = None
        self._secondary_pid = None
        self._auto_roll_down = None
        self._default_guid = None
        self._lookup_uid = None
        self._phonetics_alias = None
        self._rollup_type = None
        self._calculation_type = None
        self._formula = None
        self._restrict_values = None
        self._valuelist_sort_order = None
        self._append_new_values = None
        self._default = None
        self._value_list = None
        self._secondary_guid = None
        self.discriminator = None

        if field_id is not None:
            self.field_id = field_id
        if field_name is not None:
            self.field_name = field_name
        if cf_type is not None:
            self.cf_type = cf_type
        if guid is not None:
            self.guid = guid
        if element_type is not None:
            self.element_type = element_type
        if max_multi_values is not None:
            self.max_multi_values = max_multi_values
        if user_def is not None:
            self.user_def = user_def
        if alias is not None:
            self.alias = alias
        if secondary_pid is not None:
            self.secondary_pid = secondary_pid
        if auto_roll_down is not None:
            self.auto_roll_down = auto_roll_down
        if default_guid is not None:
            self.default_guid = default_guid
        if lookup_uid is not None:
            self.lookup_uid = lookup_uid
        if phonetics_alias is not None:
            self.phonetics_alias = phonetics_alias
        if rollup_type is not None:
            self.rollup_type = rollup_type
        if calculation_type is not None:
            self.calculation_type = calculation_type
        if formula is not None:
            self.formula = formula
        if restrict_values is not None:
            self.restrict_values = restrict_values
        if valuelist_sort_order is not None:
            self.valuelist_sort_order = valuelist_sort_order
        if append_new_values is not None:
            self.append_new_values = append_new_values
        if default is not None:
            self.default = default
        if value_list is not None:
            self.value_list = value_list
        if secondary_guid is not None:
            self.secondary_guid = secondary_guid

    @property
    def field_id(self):
        """Gets the field_id of this ExtendedAttributeDefinition.  # noqa: E501

        Corresponds to the Pid of a custom field.  # noqa: E501

        :return: The field_id of this ExtendedAttributeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this ExtendedAttributeDefinition.

        Corresponds to the Pid of a custom field.  # noqa: E501

        :param field_id: The field_id of this ExtendedAttributeDefinition.  # noqa: E501
        :type: str
        """
        self._field_id = field_id
    @property
    def field_name(self):
        """Gets the field_name of this ExtendedAttributeDefinition.  # noqa: E501

        The name of a custom field.  # noqa: E501

        :return: The field_name of this ExtendedAttributeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this ExtendedAttributeDefinition.

        The name of a custom field.  # noqa: E501

        :param field_name: The field_name of this ExtendedAttributeDefinition.  # noqa: E501
        :type: str
        """
        self._field_name = field_name
    @property
    def cf_type(self):
        """Gets the cf_type of this ExtendedAttributeDefinition.  # noqa: E501

        The type of a custom field.  # noqa: E501

        :return: The cf_type of this ExtendedAttributeDefinition.  # noqa: E501
        :rtype: CustomFieldType
        """
        return self._cf_type

    @cf_type.setter
    def cf_type(self, cf_type):
        """Sets the cf_type of this ExtendedAttributeDefinition.

        The type of a custom field.  # noqa: E501

        :param cf_type: The cf_type of this ExtendedAttributeDefinition.  # noqa: E501
        :type: CustomFieldType
        """
        if cf_type is None:
            raise ValueError("Invalid value for `cf_type`, must not be `None`")  # noqa: E501
        self._cf_type = cf_type
    @property
    def guid(self):
        """Gets the guid of this ExtendedAttributeDefinition.  # noqa: E501

        The Guid of a custom field.  # noqa: E501

        :return: The guid of this ExtendedAttributeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this ExtendedAttributeDefinition.

        The Guid of a custom field.  # noqa: E501

        :param guid: The guid of this ExtendedAttributeDefinition.  # noqa: E501
        :type: str
        """
        self._guid = guid
    @property
    def element_type(self):
        """Gets the element_type of this ExtendedAttributeDefinition.  # noqa: E501

        Determines whether the extended attribute is associated with a task or a resource  # noqa: E501

        :return: The element_type of this ExtendedAttributeDefinition.  # noqa: E501
        :rtype: ElementType
        """
        return self._element_type

    @element_type.setter
    def element_type(self, element_type):
        """Sets the element_type of this ExtendedAttributeDefinition.

        Determines whether the extended attribute is associated with a task or a resource  # noqa: E501

        :param element_type: The element_type of this ExtendedAttributeDefinition.  # noqa: E501
        :type: ElementType
        """
        if element_type is None:
            raise ValueError("Invalid value for `element_type`, must not be `None`")  # noqa: E501
        self._element_type = element_type
    @property
    def max_multi_values(self):
        """Gets the max_multi_values of this ExtendedAttributeDefinition.  # noqa: E501

        The maximum number of values you can set in a picklist.  # noqa: E501

        :return: The max_multi_values of this ExtendedAttributeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._max_multi_values

    @max_multi_values.setter
    def max_multi_values(self, max_multi_values):
        """Sets the max_multi_values of this ExtendedAttributeDefinition.

        The maximum number of values you can set in a picklist.  # noqa: E501

        :param max_multi_values: The max_multi_values of this ExtendedAttributeDefinition.  # noqa: E501
        :type: int
        """
        if max_multi_values is None:
            raise ValueError("Invalid value for `max_multi_values`, must not be `None`")  # noqa: E501
        self._max_multi_values = max_multi_values
    @property
    def user_def(self):
        """Gets the user_def of this ExtendedAttributeDefinition.  # noqa: E501

        Determines whether a custom field is user defined.  # noqa: E501

        :return: The user_def of this ExtendedAttributeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._user_def

    @user_def.setter
    def user_def(self, user_def):
        """Sets the user_def of this ExtendedAttributeDefinition.

        Determines whether a custom field is user defined.  # noqa: E501

        :param user_def: The user_def of this ExtendedAttributeDefinition.  # noqa: E501
        :type: bool
        """
        if user_def is None:
            raise ValueError("Invalid value for `user_def`, must not be `None`")  # noqa: E501
        self._user_def = user_def
    @property
    def alias(self):
        """Gets the alias of this ExtendedAttributeDefinition.  # noqa: E501

        The alias of a custom field.  # noqa: E501

        :return: The alias of this ExtendedAttributeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this ExtendedAttributeDefinition.

        The alias of a custom field.  # noqa: E501

        :param alias: The alias of this ExtendedAttributeDefinition.  # noqa: E501
        :type: str
        """
        self._alias = alias
    @property
    def secondary_pid(self):
        """Gets the secondary_pid of this ExtendedAttributeDefinition.  # noqa: E501

        The secondary Pid of a custom field.  # noqa: E501

        :return: The secondary_pid of this ExtendedAttributeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._secondary_pid

    @secondary_pid.setter
    def secondary_pid(self, secondary_pid):
        """Sets the secondary_pid of this ExtendedAttributeDefinition.

        The secondary Pid of a custom field.  # noqa: E501

        :param secondary_pid: The secondary_pid of this ExtendedAttributeDefinition.  # noqa: E501
        :type: str
        """
        self._secondary_pid = secondary_pid
    @property
    def auto_roll_down(self):
        """Gets the auto_roll_down of this ExtendedAttributeDefinition.  # noqa: E501

        Determines whether an automatic rolldown to assignments is enabled.  # noqa: E501

        :return: The auto_roll_down of this ExtendedAttributeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._auto_roll_down

    @auto_roll_down.setter
    def auto_roll_down(self, auto_roll_down):
        """Sets the auto_roll_down of this ExtendedAttributeDefinition.

        Determines whether an automatic rolldown to assignments is enabled.  # noqa: E501

        :param auto_roll_down: The auto_roll_down of this ExtendedAttributeDefinition.  # noqa: E501
        :type: bool
        """
        if auto_roll_down is None:
            raise ValueError("Invalid value for `auto_roll_down`, must not be `None`")  # noqa: E501
        self._auto_roll_down = auto_roll_down
    @property
    def default_guid(self):
        """Gets the default_guid of this ExtendedAttributeDefinition.  # noqa: E501

        The Guid of the default lookup table entry.  # noqa: E501

        :return: The default_guid of this ExtendedAttributeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._default_guid

    @default_guid.setter
    def default_guid(self, default_guid):
        """Sets the default_guid of this ExtendedAttributeDefinition.

        The Guid of the default lookup table entry.  # noqa: E501

        :param default_guid: The default_guid of this ExtendedAttributeDefinition.  # noqa: E501
        :type: str
        """
        self._default_guid = default_guid
    @property
    def lookup_uid(self):
        """Gets the lookup_uid of this ExtendedAttributeDefinition.  # noqa: E501

        The Guid of the lookup table associated with a custom field.  # noqa: E501

        :return: The lookup_uid of this ExtendedAttributeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._lookup_uid

    @lookup_uid.setter
    def lookup_uid(self, lookup_uid):
        """Sets the lookup_uid of this ExtendedAttributeDefinition.

        The Guid of the lookup table associated with a custom field.  # noqa: E501

        :param lookup_uid: The lookup_uid of this ExtendedAttributeDefinition.  # noqa: E501
        :type: str
        """
        self._lookup_uid = lookup_uid
    @property
    def phonetics_alias(self):
        """Gets the phonetics_alias of this ExtendedAttributeDefinition.  # noqa: E501

        The phonetic pronunciation of the alias of a custom field.  # noqa: E501

        :return: The phonetics_alias of this ExtendedAttributeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._phonetics_alias

    @phonetics_alias.setter
    def phonetics_alias(self, phonetics_alias):
        """Sets the phonetics_alias of this ExtendedAttributeDefinition.

        The phonetic pronunciation of the alias of a custom field.  # noqa: E501

        :param phonetics_alias: The phonetics_alias of this ExtendedAttributeDefinition.  # noqa: E501
        :type: str
        """
        self._phonetics_alias = phonetics_alias
    @property
    def rollup_type(self):
        """Gets the rollup_type of this ExtendedAttributeDefinition.  # noqa: E501

        The way rollups are calculated.  # noqa: E501

        :return: The rollup_type of this ExtendedAttributeDefinition.  # noqa: E501
        :rtype: RollupType
        """
        return self._rollup_type

    @rollup_type.setter
    def rollup_type(self, rollup_type):
        """Sets the rollup_type of this ExtendedAttributeDefinition.

        The way rollups are calculated.  # noqa: E501

        :param rollup_type: The rollup_type of this ExtendedAttributeDefinition.  # noqa: E501
        :type: RollupType
        """
        if rollup_type is None:
            raise ValueError("Invalid value for `rollup_type`, must not be `None`")  # noqa: E501
        self._rollup_type = rollup_type
    @property
    def calculation_type(self):
        """Gets the calculation_type of this ExtendedAttributeDefinition.  # noqa: E501

        Determines whether rollups are calculated for a task and group summary rows.  # noqa: E501

        :return: The calculation_type of this ExtendedAttributeDefinition.  # noqa: E501
        :rtype: CalculationType
        """
        return self._calculation_type

    @calculation_type.setter
    def calculation_type(self, calculation_type):
        """Sets the calculation_type of this ExtendedAttributeDefinition.

        Determines whether rollups are calculated for a task and group summary rows.  # noqa: E501

        :param calculation_type: The calculation_type of this ExtendedAttributeDefinition.  # noqa: E501
        :type: CalculationType
        """
        if calculation_type is None:
            raise ValueError("Invalid value for `calculation_type`, must not be `None`")  # noqa: E501
        self._calculation_type = calculation_type
    @property
    def formula(self):
        """Gets the formula of this ExtendedAttributeDefinition.  # noqa: E501

        The formula that Microsoft Project uses to populate a custom task field.  # noqa: E501

        :return: The formula of this ExtendedAttributeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        """Sets the formula of this ExtendedAttributeDefinition.

        The formula that Microsoft Project uses to populate a custom task field.  # noqa: E501

        :param formula: The formula of this ExtendedAttributeDefinition.  # noqa: E501
        :type: str
        """
        self._formula = formula
    @property
    def restrict_values(self):
        """Gets the restrict_values of this ExtendedAttributeDefinition.  # noqa: E501

        Determines whether only values in the list are allowed in a file.  # noqa: E501

        :return: The restrict_values of this ExtendedAttributeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._restrict_values

    @restrict_values.setter
    def restrict_values(self, restrict_values):
        """Sets the restrict_values of this ExtendedAttributeDefinition.

        Determines whether only values in the list are allowed in a file.  # noqa: E501

        :param restrict_values: The restrict_values of this ExtendedAttributeDefinition.  # noqa: E501
        :type: bool
        """
        if restrict_values is None:
            raise ValueError("Invalid value for `restrict_values`, must not be `None`")  # noqa: E501
        self._restrict_values = restrict_values
    @property
    def valuelist_sort_order(self):
        """Gets the valuelist_sort_order of this ExtendedAttributeDefinition.  # noqa: E501

        The way value lists are sorted. Values are: 0=Descending, 1=Ascending.  # noqa: E501

        :return: The valuelist_sort_order of this ExtendedAttributeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._valuelist_sort_order

    @valuelist_sort_order.setter
    def valuelist_sort_order(self, valuelist_sort_order):
        """Sets the valuelist_sort_order of this ExtendedAttributeDefinition.

        The way value lists are sorted. Values are: 0=Descending, 1=Ascending.  # noqa: E501

        :param valuelist_sort_order: The valuelist_sort_order of this ExtendedAttributeDefinition.  # noqa: E501
        :type: int
        """
        if valuelist_sort_order is None:
            raise ValueError("Invalid value for `valuelist_sort_order`, must not be `None`")  # noqa: E501
        self._valuelist_sort_order = valuelist_sort_order
    @property
    def append_new_values(self):
        """Gets the append_new_values of this ExtendedAttributeDefinition.  # noqa: E501

        Determines whether new values added to a project are automatically added to the list.  # noqa: E501

        :return: The append_new_values of this ExtendedAttributeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._append_new_values

    @append_new_values.setter
    def append_new_values(self, append_new_values):
        """Sets the append_new_values of this ExtendedAttributeDefinition.

        Determines whether new values added to a project are automatically added to the list.  # noqa: E501

        :param append_new_values: The append_new_values of this ExtendedAttributeDefinition.  # noqa: E501
        :type: bool
        """
        if append_new_values is None:
            raise ValueError("Invalid value for `append_new_values`, must not be `None`")  # noqa: E501
        self._append_new_values = append_new_values
    @property
    def default(self):
        """Gets the default of this ExtendedAttributeDefinition.  # noqa: E501

        The default value in the list.  # noqa: E501

        :return: The default of this ExtendedAttributeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this ExtendedAttributeDefinition.

        The default value in the list.  # noqa: E501

        :param default: The default of this ExtendedAttributeDefinition.  # noqa: E501
        :type: str
        """
        self._default = default
    @property
    def value_list(self):
        """Gets the value_list of this ExtendedAttributeDefinition.  # noqa: E501

        Returns list of Extended Attribute Values.  # noqa: E501

        :return: The value_list of this ExtendedAttributeDefinition.  # noqa: E501
        :rtype: list[Value]
        """
        return self._value_list

    @value_list.setter
    def value_list(self, value_list):
        """Sets the value_list of this ExtendedAttributeDefinition.

        Returns list of Extended Attribute Values.  # noqa: E501

        :param value_list: The value_list of this ExtendedAttributeDefinition.  # noqa: E501
        :type: list[Value]
        """
        self._value_list = value_list
    @property
    def secondary_guid(self):
        """Gets the secondary_guid of this ExtendedAttributeDefinition.  # noqa: E501

        Secondary guid of extended attribute.  # noqa: E501

        :return: The secondary_guid of this ExtendedAttributeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._secondary_guid

    @secondary_guid.setter
    def secondary_guid(self, secondary_guid):
        """Sets the secondary_guid of this ExtendedAttributeDefinition.

        Secondary guid of extended attribute.  # noqa: E501

        :param secondary_guid: The secondary_guid of this ExtendedAttributeDefinition.  # noqa: E501
        :type: str
        """
        self._secondary_guid = secondary_guid
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
        if not isinstance(other, ExtendedAttributeDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
