# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="PrimaveraTaskProperties.py">
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


class PrimaveraTaskProperties(object):
    """Represents Primavera-specific properties for a task read from Primavera format (XER of P6XML).
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'sequence_number': 'int',
        'activity_id': 'str',
        'remaining_early_finish': 'datetime',
        'remaining_early_start': 'datetime',
        'remaining_late_start': 'datetime',
        'remaining_late_finish': 'datetime',
        'raw_duration_type': 'str',
        'raw_activity_type': 'str',
        'raw_complete_percent_type': 'str',
        'raw_status': 'str',
        'duration_percent_complete': 'float',
        'physical_percent_complete': 'float',
        'actual_non_labor_units': 'float',
        'actual_labor_units': 'float',
        'units_percent_complete': 'float',
        'remaining_labor_units': 'float',
        'remaining_non_labor_units': 'float',
        'duration_type': 'PrimaveraDurationType',
        'activity_type': 'PrimaveraActivityType',
        'percent_complete_type': 'PrimaveraPercentCompleteType',
        'actual_labor_cost': 'float',
        'actual_nonlabor_cost': 'float',
        'actual_material_cost': 'float',
        'actual_expense_cost': 'float',
        'remaining_expense_cost': 'float',
        'actual_total_cost': 'float',
        'budgeted_total_cost': 'float',
        'budgeted_labor_cost': 'float',
        'budgeted_nonlabor_cost': 'float',
        'budgeted_material_cost': 'float',
        'budgeted_expense_cost': 'float'
    }

    attribute_map = {
        'sequence_number': 'sequenceNumber',
        'activity_id': 'activityId',
        'remaining_early_finish': 'remainingEarlyFinish',
        'remaining_early_start': 'remainingEarlyStart',
        'remaining_late_start': 'remainingLateStart',
        'remaining_late_finish': 'remainingLateFinish',
        'raw_duration_type': 'rawDurationType',
        'raw_activity_type': 'rawActivityType',
        'raw_complete_percent_type': 'rawCompletePercentType',
        'raw_status': 'rawStatus',
        'duration_percent_complete': 'durationPercentComplete',
        'physical_percent_complete': 'physicalPercentComplete',
        'actual_non_labor_units': 'actualNonLaborUnits',
        'actual_labor_units': 'actualLaborUnits',
        'units_percent_complete': 'unitsPercentComplete',
        'remaining_labor_units': 'remainingLaborUnits',
        'remaining_non_labor_units': 'remainingNonLaborUnits',
        'duration_type': 'durationType',
        'activity_type': 'activityType',
        'percent_complete_type': 'percentCompleteType',
        'actual_labor_cost': 'actualLaborCost',
        'actual_nonlabor_cost': 'actualNonlaborCost',
        'actual_material_cost': 'actualMaterialCost',
        'actual_expense_cost': 'actualExpenseCost',
        'remaining_expense_cost': 'remainingExpenseCost',
        'actual_total_cost': 'actualTotalCost',
        'budgeted_total_cost': 'budgetedTotalCost',
        'budgeted_labor_cost': 'budgetedLaborCost',
        'budgeted_nonlabor_cost': 'budgetedNonlaborCost',
        'budgeted_material_cost': 'budgetedMaterialCost',
        'budgeted_expense_cost': 'budgetedExpenseCost'
    }

    def __init__(self, sequence_number=None, activity_id=None, remaining_early_finish=None, remaining_early_start=None, remaining_late_start=None, remaining_late_finish=None, raw_duration_type=None, raw_activity_type=None, raw_complete_percent_type=None, raw_status=None, duration_percent_complete=None, physical_percent_complete=None, actual_non_labor_units=None, actual_labor_units=None, units_percent_complete=None, remaining_labor_units=None, remaining_non_labor_units=None, duration_type=None, activity_type=None, percent_complete_type=None, actual_labor_cost=None, actual_nonlabor_cost=None, actual_material_cost=None, actual_expense_cost=None, remaining_expense_cost=None, actual_total_cost=None, budgeted_total_cost=None, budgeted_labor_cost=None, budgeted_nonlabor_cost=None, budgeted_material_cost=None, budgeted_expense_cost=None):  # noqa: E501
        """PrimaveraTaskProperties - a model defined in Swagger"""  # noqa: E501

        self._sequence_number = None
        self._activity_id = None
        self._remaining_early_finish = None
        self._remaining_early_start = None
        self._remaining_late_start = None
        self._remaining_late_finish = None
        self._raw_duration_type = None
        self._raw_activity_type = None
        self._raw_complete_percent_type = None
        self._raw_status = None
        self._duration_percent_complete = None
        self._physical_percent_complete = None
        self._actual_non_labor_units = None
        self._actual_labor_units = None
        self._units_percent_complete = None
        self._remaining_labor_units = None
        self._remaining_non_labor_units = None
        self._duration_type = None
        self._activity_type = None
        self._percent_complete_type = None
        self._actual_labor_cost = None
        self._actual_nonlabor_cost = None
        self._actual_material_cost = None
        self._actual_expense_cost = None
        self._remaining_expense_cost = None
        self._actual_total_cost = None
        self._budgeted_total_cost = None
        self._budgeted_labor_cost = None
        self._budgeted_nonlabor_cost = None
        self._budgeted_material_cost = None
        self._budgeted_expense_cost = None
        self.discriminator = None

        if sequence_number is not None:
            self.sequence_number = sequence_number
        if activity_id is not None:
            self.activity_id = activity_id
        if remaining_early_finish is not None:
            self.remaining_early_finish = remaining_early_finish
        if remaining_early_start is not None:
            self.remaining_early_start = remaining_early_start
        if remaining_late_start is not None:
            self.remaining_late_start = remaining_late_start
        if remaining_late_finish is not None:
            self.remaining_late_finish = remaining_late_finish
        if raw_duration_type is not None:
            self.raw_duration_type = raw_duration_type
        if raw_activity_type is not None:
            self.raw_activity_type = raw_activity_type
        if raw_complete_percent_type is not None:
            self.raw_complete_percent_type = raw_complete_percent_type
        if raw_status is not None:
            self.raw_status = raw_status
        if duration_percent_complete is not None:
            self.duration_percent_complete = duration_percent_complete
        if physical_percent_complete is not None:
            self.physical_percent_complete = physical_percent_complete
        if actual_non_labor_units is not None:
            self.actual_non_labor_units = actual_non_labor_units
        if actual_labor_units is not None:
            self.actual_labor_units = actual_labor_units
        if units_percent_complete is not None:
            self.units_percent_complete = units_percent_complete
        if remaining_labor_units is not None:
            self.remaining_labor_units = remaining_labor_units
        if remaining_non_labor_units is not None:
            self.remaining_non_labor_units = remaining_non_labor_units
        if duration_type is not None:
            self.duration_type = duration_type
        if activity_type is not None:
            self.activity_type = activity_type
        if percent_complete_type is not None:
            self.percent_complete_type = percent_complete_type
        if actual_labor_cost is not None:
            self.actual_labor_cost = actual_labor_cost
        if actual_nonlabor_cost is not None:
            self.actual_nonlabor_cost = actual_nonlabor_cost
        if actual_material_cost is not None:
            self.actual_material_cost = actual_material_cost
        if actual_expense_cost is not None:
            self.actual_expense_cost = actual_expense_cost
        if remaining_expense_cost is not None:
            self.remaining_expense_cost = remaining_expense_cost
        if actual_total_cost is not None:
            self.actual_total_cost = actual_total_cost
        if budgeted_total_cost is not None:
            self.budgeted_total_cost = budgeted_total_cost
        if budgeted_labor_cost is not None:
            self.budgeted_labor_cost = budgeted_labor_cost
        if budgeted_nonlabor_cost is not None:
            self.budgeted_nonlabor_cost = budgeted_nonlabor_cost
        if budgeted_material_cost is not None:
            self.budgeted_material_cost = budgeted_material_cost
        if budgeted_expense_cost is not None:
            self.budgeted_expense_cost = budgeted_expense_cost

    @property
    def sequence_number(self):
        """Gets the sequence_number of this PrimaveraTaskProperties.  # noqa: E501

        The sequence number of the WBS item (summary tasks). It is used to sort summary tasks in Primavera.  # noqa: E501

        :return: The sequence_number of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: int
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """Sets the sequence_number of this PrimaveraTaskProperties.

        The sequence number of the WBS item (summary tasks). It is used to sort summary tasks in Primavera.  # noqa: E501

        :param sequence_number: The sequence_number of this PrimaveraTaskProperties.  # noqa: E501
        :type: int
        """
        if sequence_number is None:
            raise ValueError("Invalid value for `sequence_number`, must not be `None`")  # noqa: E501
        self._sequence_number = sequence_number
    @property
    def activity_id(self):
        """Gets the activity_id of this PrimaveraTaskProperties.  # noqa: E501

        Activity id field - a task's unique identifier used by Primavera.  # noqa: E501

        :return: The activity_id of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: str
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """Sets the activity_id of this PrimaveraTaskProperties.

        Activity id field - a task's unique identifier used by Primavera.  # noqa: E501

        :param activity_id: The activity_id of this PrimaveraTaskProperties.  # noqa: E501
        :type: str
        """
        self._activity_id = activity_id
    @property
    def remaining_early_finish(self):
        """Gets the remaining_early_finish of this PrimaveraTaskProperties.  # noqa: E501

        Remaining early finish date - the date when the remaining work for the activity is scheduled to be finished.  # noqa: E501

        :return: The remaining_early_finish of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: datetime
        """
        return self._remaining_early_finish

    @remaining_early_finish.setter
    def remaining_early_finish(self, remaining_early_finish):
        """Sets the remaining_early_finish of this PrimaveraTaskProperties.

        Remaining early finish date - the date when the remaining work for the activity is scheduled to be finished.  # noqa: E501

        :param remaining_early_finish: The remaining_early_finish of this PrimaveraTaskProperties.  # noqa: E501
        :type: datetime
        """
        if remaining_early_finish is None:
            raise ValueError("Invalid value for `remaining_early_finish`, must not be `None`")  # noqa: E501
        self._remaining_early_finish = remaining_early_finish
    @property
    def remaining_early_start(self):
        """Gets the remaining_early_start of this PrimaveraTaskProperties.  # noqa: E501

        Remaining early start date - the date when the remaining work for the activity is scheduled to begin.  # noqa: E501

        :return: The remaining_early_start of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: datetime
        """
        return self._remaining_early_start

    @remaining_early_start.setter
    def remaining_early_start(self, remaining_early_start):
        """Sets the remaining_early_start of this PrimaveraTaskProperties.

        Remaining early start date - the date when the remaining work for the activity is scheduled to begin.  # noqa: E501

        :param remaining_early_start: The remaining_early_start of this PrimaveraTaskProperties.  # noqa: E501
        :type: datetime
        """
        if remaining_early_start is None:
            raise ValueError("Invalid value for `remaining_early_start`, must not be `None`")  # noqa: E501
        self._remaining_early_start = remaining_early_start
    @property
    def remaining_late_start(self):
        """Gets the remaining_late_start of this PrimaveraTaskProperties.  # noqa: E501

        Remaining late start date.  # noqa: E501

        :return: The remaining_late_start of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: datetime
        """
        return self._remaining_late_start

    @remaining_late_start.setter
    def remaining_late_start(self, remaining_late_start):
        """Sets the remaining_late_start of this PrimaveraTaskProperties.

        Remaining late start date.  # noqa: E501

        :param remaining_late_start: The remaining_late_start of this PrimaveraTaskProperties.  # noqa: E501
        :type: datetime
        """
        if remaining_late_start is None:
            raise ValueError("Invalid value for `remaining_late_start`, must not be `None`")  # noqa: E501
        self._remaining_late_start = remaining_late_start
    @property
    def remaining_late_finish(self):
        """Gets the remaining_late_finish of this PrimaveraTaskProperties.  # noqa: E501

        Remaining late finish date.  # noqa: E501

        :return: The remaining_late_finish of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: datetime
        """
        return self._remaining_late_finish

    @remaining_late_finish.setter
    def remaining_late_finish(self, remaining_late_finish):
        """Sets the remaining_late_finish of this PrimaveraTaskProperties.

        Remaining late finish date.  # noqa: E501

        :param remaining_late_finish: The remaining_late_finish of this PrimaveraTaskProperties.  # noqa: E501
        :type: datetime
        """
        if remaining_late_finish is None:
            raise ValueError("Invalid value for `remaining_late_finish`, must not be `None`")  # noqa: E501
        self._remaining_late_finish = remaining_late_finish
    @property
    def raw_duration_type(self):
        """Gets the raw_duration_type of this PrimaveraTaskProperties.  # noqa: E501

        Raw text representation (as in source file) of 'Duration Type' field of the activity.  # noqa: E501

        :return: The raw_duration_type of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: str
        """
        return self._raw_duration_type

    @raw_duration_type.setter
    def raw_duration_type(self, raw_duration_type):
        """Sets the raw_duration_type of this PrimaveraTaskProperties.

        Raw text representation (as in source file) of 'Duration Type' field of the activity.  # noqa: E501

        :param raw_duration_type: The raw_duration_type of this PrimaveraTaskProperties.  # noqa: E501
        :type: str
        """
        self._raw_duration_type = raw_duration_type
    @property
    def raw_activity_type(self):
        """Gets the raw_activity_type of this PrimaveraTaskProperties.  # noqa: E501

        Raw text representation (as in source file) of 'Activity Type' field of the activity.  # noqa: E501

        :return: The raw_activity_type of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: str
        """
        return self._raw_activity_type

    @raw_activity_type.setter
    def raw_activity_type(self, raw_activity_type):
        """Sets the raw_activity_type of this PrimaveraTaskProperties.

        Raw text representation (as in source file) of 'Activity Type' field of the activity.  # noqa: E501

        :param raw_activity_type: The raw_activity_type of this PrimaveraTaskProperties.  # noqa: E501
        :type: str
        """
        self._raw_activity_type = raw_activity_type
    @property
    def raw_complete_percent_type(self):
        """Gets the raw_complete_percent_type of this PrimaveraTaskProperties.  # noqa: E501

        Raw text representation (as in source file) of '% Complete Type' field of the activity.  # noqa: E501

        :return: The raw_complete_percent_type of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: str
        """
        return self._raw_complete_percent_type

    @raw_complete_percent_type.setter
    def raw_complete_percent_type(self, raw_complete_percent_type):
        """Sets the raw_complete_percent_type of this PrimaveraTaskProperties.

        Raw text representation (as in source file) of '% Complete Type' field of the activity.  # noqa: E501

        :param raw_complete_percent_type: The raw_complete_percent_type of this PrimaveraTaskProperties.  # noqa: E501
        :type: str
        """
        self._raw_complete_percent_type = raw_complete_percent_type
    @property
    def raw_status(self):
        """Gets the raw_status of this PrimaveraTaskProperties.  # noqa: E501

        Raw text representation (as in source file) of 'Status' field of the activity.  # noqa: E501

        :return: The raw_status of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: str
        """
        return self._raw_status

    @raw_status.setter
    def raw_status(self, raw_status):
        """Sets the raw_status of this PrimaveraTaskProperties.

        Raw text representation (as in source file) of 'Status' field of the activity.  # noqa: E501

        :param raw_status: The raw_status of this PrimaveraTaskProperties.  # noqa: E501
        :type: str
        """
        self._raw_status = raw_status
    @property
    def duration_percent_complete(self):
        """Gets the duration_percent_complete of this PrimaveraTaskProperties.  # noqa: E501

        Gets the value of duration percent complete.  # noqa: E501

        :return: The duration_percent_complete of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: float
        """
        return self._duration_percent_complete

    @duration_percent_complete.setter
    def duration_percent_complete(self, duration_percent_complete):
        """Sets the duration_percent_complete of this PrimaveraTaskProperties.

        Gets the value of duration percent complete.  # noqa: E501

        :param duration_percent_complete: The duration_percent_complete of this PrimaveraTaskProperties.  # noqa: E501
        :type: float
        """
        if duration_percent_complete is None:
            raise ValueError("Invalid value for `duration_percent_complete`, must not be `None`")  # noqa: E501
        self._duration_percent_complete = duration_percent_complete
    @property
    def physical_percent_complete(self):
        """Gets the physical_percent_complete of this PrimaveraTaskProperties.  # noqa: E501

        Gets the value of Physical Percent Complete.  # noqa: E501

        :return: The physical_percent_complete of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: float
        """
        return self._physical_percent_complete

    @physical_percent_complete.setter
    def physical_percent_complete(self, physical_percent_complete):
        """Sets the physical_percent_complete of this PrimaveraTaskProperties.

        Gets the value of Physical Percent Complete.  # noqa: E501

        :param physical_percent_complete: The physical_percent_complete of this PrimaveraTaskProperties.  # noqa: E501
        :type: float
        """
        if physical_percent_complete is None:
            raise ValueError("Invalid value for `physical_percent_complete`, must not be `None`")  # noqa: E501
        self._physical_percent_complete = physical_percent_complete
    @property
    def actual_non_labor_units(self):
        """Gets the actual_non_labor_units of this PrimaveraTaskProperties.  # noqa: E501

        Gets the value of actual non labor units.  # noqa: E501

        :return: The actual_non_labor_units of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: float
        """
        return self._actual_non_labor_units

    @actual_non_labor_units.setter
    def actual_non_labor_units(self, actual_non_labor_units):
        """Sets the actual_non_labor_units of this PrimaveraTaskProperties.

        Gets the value of actual non labor units.  # noqa: E501

        :param actual_non_labor_units: The actual_non_labor_units of this PrimaveraTaskProperties.  # noqa: E501
        :type: float
        """
        if actual_non_labor_units is None:
            raise ValueError("Invalid value for `actual_non_labor_units`, must not be `None`")  # noqa: E501
        self._actual_non_labor_units = actual_non_labor_units
    @property
    def actual_labor_units(self):
        """Gets the actual_labor_units of this PrimaveraTaskProperties.  # noqa: E501

        Gets the value of actual labor units.  # noqa: E501

        :return: The actual_labor_units of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: float
        """
        return self._actual_labor_units

    @actual_labor_units.setter
    def actual_labor_units(self, actual_labor_units):
        """Sets the actual_labor_units of this PrimaveraTaskProperties.

        Gets the value of actual labor units.  # noqa: E501

        :param actual_labor_units: The actual_labor_units of this PrimaveraTaskProperties.  # noqa: E501
        :type: float
        """
        if actual_labor_units is None:
            raise ValueError("Invalid value for `actual_labor_units`, must not be `None`")  # noqa: E501
        self._actual_labor_units = actual_labor_units
    @property
    def units_percent_complete(self):
        """Gets the units_percent_complete of this PrimaveraTaskProperties.  # noqa: E501

        Gets the value of units percent complete.  # noqa: E501

        :return: The units_percent_complete of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: float
        """
        return self._units_percent_complete

    @units_percent_complete.setter
    def units_percent_complete(self, units_percent_complete):
        """Sets the units_percent_complete of this PrimaveraTaskProperties.

        Gets the value of units percent complete.  # noqa: E501

        :param units_percent_complete: The units_percent_complete of this PrimaveraTaskProperties.  # noqa: E501
        :type: float
        """
        if units_percent_complete is None:
            raise ValueError("Invalid value for `units_percent_complete`, must not be `None`")  # noqa: E501
        self._units_percent_complete = units_percent_complete
    @property
    def remaining_labor_units(self):
        """Gets the remaining_labor_units of this PrimaveraTaskProperties.  # noqa: E501

        Gets the value of remaining labor units.  # noqa: E501

        :return: The remaining_labor_units of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: float
        """
        return self._remaining_labor_units

    @remaining_labor_units.setter
    def remaining_labor_units(self, remaining_labor_units):
        """Sets the remaining_labor_units of this PrimaveraTaskProperties.

        Gets the value of remaining labor units.  # noqa: E501

        :param remaining_labor_units: The remaining_labor_units of this PrimaveraTaskProperties.  # noqa: E501
        :type: float
        """
        if remaining_labor_units is None:
            raise ValueError("Invalid value for `remaining_labor_units`, must not be `None`")  # noqa: E501
        self._remaining_labor_units = remaining_labor_units
    @property
    def remaining_non_labor_units(self):
        """Gets the remaining_non_labor_units of this PrimaveraTaskProperties.  # noqa: E501

        Gets the value of remaining non labor units.  # noqa: E501

        :return: The remaining_non_labor_units of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: float
        """
        return self._remaining_non_labor_units

    @remaining_non_labor_units.setter
    def remaining_non_labor_units(self, remaining_non_labor_units):
        """Sets the remaining_non_labor_units of this PrimaveraTaskProperties.

        Gets the value of remaining non labor units.  # noqa: E501

        :param remaining_non_labor_units: The remaining_non_labor_units of this PrimaveraTaskProperties.  # noqa: E501
        :type: float
        """
        if remaining_non_labor_units is None:
            raise ValueError("Invalid value for `remaining_non_labor_units`, must not be `None`")  # noqa: E501
        self._remaining_non_labor_units = remaining_non_labor_units
    @property
    def duration_type(self):
        """Gets the duration_type of this PrimaveraTaskProperties.  # noqa: E501

        Gets the value of 'Duration Type' field of the activity.  # noqa: E501

        :return: The duration_type of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: PrimaveraDurationType
        """
        return self._duration_type

    @duration_type.setter
    def duration_type(self, duration_type):
        """Sets the duration_type of this PrimaveraTaskProperties.

        Gets the value of 'Duration Type' field of the activity.  # noqa: E501

        :param duration_type: The duration_type of this PrimaveraTaskProperties.  # noqa: E501
        :type: PrimaveraDurationType
        """
        if duration_type is None:
            raise ValueError("Invalid value for `duration_type`, must not be `None`")  # noqa: E501
        self._duration_type = duration_type
    @property
    def activity_type(self):
        """Gets the activity_type of this PrimaveraTaskProperties.  # noqa: E501

        Gets the value of 'Activity Type' field.  # noqa: E501

        :return: The activity_type of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: PrimaveraActivityType
        """
        return self._activity_type

    @activity_type.setter
    def activity_type(self, activity_type):
        """Sets the activity_type of this PrimaveraTaskProperties.

        Gets the value of 'Activity Type' field.  # noqa: E501

        :param activity_type: The activity_type of this PrimaveraTaskProperties.  # noqa: E501
        :type: PrimaveraActivityType
        """
        if activity_type is None:
            raise ValueError("Invalid value for `activity_type`, must not be `None`")  # noqa: E501
        self._activity_type = activity_type
    @property
    def percent_complete_type(self):
        """Gets the percent_complete_type of this PrimaveraTaskProperties.  # noqa: E501

        Gets the value of '% Complete Type' field of the activity.  # noqa: E501

        :return: The percent_complete_type of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: PrimaveraPercentCompleteType
        """
        return self._percent_complete_type

    @percent_complete_type.setter
    def percent_complete_type(self, percent_complete_type):
        """Sets the percent_complete_type of this PrimaveraTaskProperties.

        Gets the value of '% Complete Type' field of the activity.  # noqa: E501

        :param percent_complete_type: The percent_complete_type of this PrimaveraTaskProperties.  # noqa: E501
        :type: PrimaveraPercentCompleteType
        """
        if percent_complete_type is None:
            raise ValueError("Invalid value for `percent_complete_type`, must not be `None`")  # noqa: E501
        self._percent_complete_type = percent_complete_type
    @property
    def actual_labor_cost(self):
        """Gets the actual_labor_cost of this PrimaveraTaskProperties.  # noqa: E501

        Gets the value of actual labor cost.  # noqa: E501

        :return: The actual_labor_cost of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: float
        """
        return self._actual_labor_cost

    @actual_labor_cost.setter
    def actual_labor_cost(self, actual_labor_cost):
        """Sets the actual_labor_cost of this PrimaveraTaskProperties.

        Gets the value of actual labor cost.  # noqa: E501

        :param actual_labor_cost: The actual_labor_cost of this PrimaveraTaskProperties.  # noqa: E501
        :type: float
        """
        if actual_labor_cost is None:
            raise ValueError("Invalid value for `actual_labor_cost`, must not be `None`")  # noqa: E501
        self._actual_labor_cost = actual_labor_cost
    @property
    def actual_nonlabor_cost(self):
        """Gets the actual_nonlabor_cost of this PrimaveraTaskProperties.  # noqa: E501

        Gets the value of actual non labor cost.  # noqa: E501

        :return: The actual_nonlabor_cost of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: float
        """
        return self._actual_nonlabor_cost

    @actual_nonlabor_cost.setter
    def actual_nonlabor_cost(self, actual_nonlabor_cost):
        """Sets the actual_nonlabor_cost of this PrimaveraTaskProperties.

        Gets the value of actual non labor cost.  # noqa: E501

        :param actual_nonlabor_cost: The actual_nonlabor_cost of this PrimaveraTaskProperties.  # noqa: E501
        :type: float
        """
        if actual_nonlabor_cost is None:
            raise ValueError("Invalid value for `actual_nonlabor_cost`, must not be `None`")  # noqa: E501
        self._actual_nonlabor_cost = actual_nonlabor_cost
    @property
    def actual_material_cost(self):
        """Gets the actual_material_cost of this PrimaveraTaskProperties.  # noqa: E501

        Gets the value of actual material cost.               # noqa: E501

        :return: The actual_material_cost of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: float
        """
        return self._actual_material_cost

    @actual_material_cost.setter
    def actual_material_cost(self, actual_material_cost):
        """Sets the actual_material_cost of this PrimaveraTaskProperties.

        Gets the value of actual material cost.               # noqa: E501

        :param actual_material_cost: The actual_material_cost of this PrimaveraTaskProperties.  # noqa: E501
        :type: float
        """
        if actual_material_cost is None:
            raise ValueError("Invalid value for `actual_material_cost`, must not be `None`")  # noqa: E501
        self._actual_material_cost = actual_material_cost
    @property
    def actual_expense_cost(self):
        """Gets the actual_expense_cost of this PrimaveraTaskProperties.  # noqa: E501

        Gets the value of actual expense cost.  # noqa: E501

        :return: The actual_expense_cost of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: float
        """
        return self._actual_expense_cost

    @actual_expense_cost.setter
    def actual_expense_cost(self, actual_expense_cost):
        """Sets the actual_expense_cost of this PrimaveraTaskProperties.

        Gets the value of actual expense cost.  # noqa: E501

        :param actual_expense_cost: The actual_expense_cost of this PrimaveraTaskProperties.  # noqa: E501
        :type: float
        """
        if actual_expense_cost is None:
            raise ValueError("Invalid value for `actual_expense_cost`, must not be `None`")  # noqa: E501
        self._actual_expense_cost = actual_expense_cost
    @property
    def remaining_expense_cost(self):
        """Gets the remaining_expense_cost of this PrimaveraTaskProperties.  # noqa: E501

        Gets the value of remaining expense cost.  # noqa: E501

        :return: The remaining_expense_cost of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: float
        """
        return self._remaining_expense_cost

    @remaining_expense_cost.setter
    def remaining_expense_cost(self, remaining_expense_cost):
        """Sets the remaining_expense_cost of this PrimaveraTaskProperties.

        Gets the value of remaining expense cost.  # noqa: E501

        :param remaining_expense_cost: The remaining_expense_cost of this PrimaveraTaskProperties.  # noqa: E501
        :type: float
        """
        if remaining_expense_cost is None:
            raise ValueError("Invalid value for `remaining_expense_cost`, must not be `None`")  # noqa: E501
        self._remaining_expense_cost = remaining_expense_cost
    @property
    def actual_total_cost(self):
        """Gets the actual_total_cost of this PrimaveraTaskProperties.  # noqa: E501

        Gets the total value of actual costs.  # noqa: E501

        :return: The actual_total_cost of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: float
        """
        return self._actual_total_cost

    @actual_total_cost.setter
    def actual_total_cost(self, actual_total_cost):
        """Sets the actual_total_cost of this PrimaveraTaskProperties.

        Gets the total value of actual costs.  # noqa: E501

        :param actual_total_cost: The actual_total_cost of this PrimaveraTaskProperties.  # noqa: E501
        :type: float
        """
        if actual_total_cost is None:
            raise ValueError("Invalid value for `actual_total_cost`, must not be `None`")  # noqa: E501
        self._actual_total_cost = actual_total_cost
    @property
    def budgeted_total_cost(self):
        """Gets the budgeted_total_cost of this PrimaveraTaskProperties.  # noqa: E501

        Gets the total value of budgeted (or planned) costs.  # noqa: E501

        :return: The budgeted_total_cost of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: float
        """
        return self._budgeted_total_cost

    @budgeted_total_cost.setter
    def budgeted_total_cost(self, budgeted_total_cost):
        """Sets the budgeted_total_cost of this PrimaveraTaskProperties.

        Gets the total value of budgeted (or planned) costs.  # noqa: E501

        :param budgeted_total_cost: The budgeted_total_cost of this PrimaveraTaskProperties.  # noqa: E501
        :type: float
        """
        if budgeted_total_cost is None:
            raise ValueError("Invalid value for `budgeted_total_cost`, must not be `None`")  # noqa: E501
        self._budgeted_total_cost = budgeted_total_cost
    @property
    def budgeted_labor_cost(self):
        """Gets the budgeted_labor_cost of this PrimaveraTaskProperties.  # noqa: E501

        Gets the value of budgeted (or planned) labor cost.  # noqa: E501

        :return: The budgeted_labor_cost of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: float
        """
        return self._budgeted_labor_cost

    @budgeted_labor_cost.setter
    def budgeted_labor_cost(self, budgeted_labor_cost):
        """Sets the budgeted_labor_cost of this PrimaveraTaskProperties.

        Gets the value of budgeted (or planned) labor cost.  # noqa: E501

        :param budgeted_labor_cost: The budgeted_labor_cost of this PrimaveraTaskProperties.  # noqa: E501
        :type: float
        """
        if budgeted_labor_cost is None:
            raise ValueError("Invalid value for `budgeted_labor_cost`, must not be `None`")  # noqa: E501
        self._budgeted_labor_cost = budgeted_labor_cost
    @property
    def budgeted_nonlabor_cost(self):
        """Gets the budgeted_nonlabor_cost of this PrimaveraTaskProperties.  # noqa: E501

        Gets the value of budgeted (or planned) non labor cost.  # noqa: E501

        :return: The budgeted_nonlabor_cost of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: float
        """
        return self._budgeted_nonlabor_cost

    @budgeted_nonlabor_cost.setter
    def budgeted_nonlabor_cost(self, budgeted_nonlabor_cost):
        """Sets the budgeted_nonlabor_cost of this PrimaveraTaskProperties.

        Gets the value of budgeted (or planned) non labor cost.  # noqa: E501

        :param budgeted_nonlabor_cost: The budgeted_nonlabor_cost of this PrimaveraTaskProperties.  # noqa: E501
        :type: float
        """
        if budgeted_nonlabor_cost is None:
            raise ValueError("Invalid value for `budgeted_nonlabor_cost`, must not be `None`")  # noqa: E501
        self._budgeted_nonlabor_cost = budgeted_nonlabor_cost
    @property
    def budgeted_material_cost(self):
        """Gets the budgeted_material_cost of this PrimaveraTaskProperties.  # noqa: E501

        Gets the value of of budgeted (or planned) material cost.  # noqa: E501

        :return: The budgeted_material_cost of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: float
        """
        return self._budgeted_material_cost

    @budgeted_material_cost.setter
    def budgeted_material_cost(self, budgeted_material_cost):
        """Sets the budgeted_material_cost of this PrimaveraTaskProperties.

        Gets the value of of budgeted (or planned) material cost.  # noqa: E501

        :param budgeted_material_cost: The budgeted_material_cost of this PrimaveraTaskProperties.  # noqa: E501
        :type: float
        """
        if budgeted_material_cost is None:
            raise ValueError("Invalid value for `budgeted_material_cost`, must not be `None`")  # noqa: E501
        self._budgeted_material_cost = budgeted_material_cost
    @property
    def budgeted_expense_cost(self):
        """Gets the budgeted_expense_cost of this PrimaveraTaskProperties.  # noqa: E501

        Gets the value of budgeted (or planned) expense cost.  # noqa: E501

        :return: The budgeted_expense_cost of this PrimaveraTaskProperties.  # noqa: E501
        :rtype: float
        """
        return self._budgeted_expense_cost

    @budgeted_expense_cost.setter
    def budgeted_expense_cost(self, budgeted_expense_cost):
        """Sets the budgeted_expense_cost of this PrimaveraTaskProperties.

        Gets the value of budgeted (or planned) expense cost.  # noqa: E501

        :param budgeted_expense_cost: The budgeted_expense_cost of this PrimaveraTaskProperties.  # noqa: E501
        :type: float
        """
        if budgeted_expense_cost is None:
            raise ValueError("Invalid value for `budgeted_expense_cost`, must not be `None`")  # noqa: E501
        self._budgeted_expense_cost = budgeted_expense_cost
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
        if not isinstance(other, PrimaveraTaskProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
