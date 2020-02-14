# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="ResourceAssignment.py">
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


class ResourceAssignment(object):
    """Represents a resource assignment in a project.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'task_uid': 'int',
        'resource_uid': 'int',
        'uid': 'int',
        'percent_work_complete': 'int',
        'actual_cost': 'float',
        'actual_finish': 'datetime',
        'actual_overtime_cost': 'float',
        'actual_overtime_work': 'str',
        'actual_start': 'datetime',
        'actual_work': 'str',
        'acwp': 'float',
        'confirmed': 'bool',
        'cost': 'float',
        'cost_rate_table_type': 'RateType',
        'cost_variance': 'float',
        'cv': 'float',
        'delay': 'int',
        'finish': 'datetime',
        'finish_variance': 'int',
        'hyperlink': 'str',
        'hyperlink_address': 'str',
        'hyperlink_sub_address': 'str',
        'work_variance': 'float',
        'has_fixed_rate_units': 'bool',
        'fixed_material': 'bool',
        'leveling_delay': 'int',
        'leveling_delay_format': 'TimeUnitType',
        'linked_fields': 'bool',
        'milestone': 'bool',
        'notes': 'str',
        'overallocated': 'bool',
        'overtime_cost': 'float',
        'overtime_work': 'str',
        'peak_units': 'float',
        'regular_work': 'str',
        'remaining_cost': 'float',
        'remaining_overtime_cost': 'float',
        'remaining_overtime_work': 'str',
        'remaining_work': 'str',
        'response_pending': 'bool',
        'start': 'datetime',
        'stop': 'datetime',
        'resume': 'datetime',
        'start_variance': 'int',
        'summary': 'bool',
        'sv': 'float',
        'units': 'float',
        'update_needed': 'bool',
        'vac': 'float',
        'work': 'str',
        'work_contour': 'WorkContourType',
        'bcws': 'float',
        'bcwp': 'float',
        'booking_type': 'BookingType',
        'actual_work_protected': 'str',
        'actual_overtime_work_protected': 'str',
        'creation_date': 'datetime',
        'assn_owner': 'str',
        'assn_owner_guid': 'str',
        'budget_cost': 'float',
        'budget_work': 'str',
        'rate_scale': 'RateScaleType',
        'baselines': 'list[AssignmentBaseline]',
        'extended_attributes': 'list[ExtendedAttribute]'
    }

    attribute_map = {
        'task_uid': 'taskUid',
        'resource_uid': 'resourceUid',
        'uid': 'uid',
        'percent_work_complete': 'percentWorkComplete',
        'actual_cost': 'actualCost',
        'actual_finish': 'actualFinish',
        'actual_overtime_cost': 'actualOvertimeCost',
        'actual_overtime_work': 'actualOvertimeWork',
        'actual_start': 'actualStart',
        'actual_work': 'actualWork',
        'acwp': 'acwp',
        'confirmed': 'confirmed',
        'cost': 'cost',
        'cost_rate_table_type': 'costRateTableType',
        'cost_variance': 'costVariance',
        'cv': 'cv',
        'delay': 'delay',
        'finish': 'finish',
        'finish_variance': 'finishVariance',
        'hyperlink': 'hyperlink',
        'hyperlink_address': 'hyperlinkAddress',
        'hyperlink_sub_address': 'hyperlinkSubAddress',
        'work_variance': 'workVariance',
        'has_fixed_rate_units': 'hasFixedRateUnits',
        'fixed_material': 'fixedMaterial',
        'leveling_delay': 'levelingDelay',
        'leveling_delay_format': 'levelingDelayFormat',
        'linked_fields': 'linkedFields',
        'milestone': 'milestone',
        'notes': 'notes',
        'overallocated': 'overallocated',
        'overtime_cost': 'overtimeCost',
        'overtime_work': 'overtimeWork',
        'peak_units': 'peakUnits',
        'regular_work': 'regularWork',
        'remaining_cost': 'remainingCost',
        'remaining_overtime_cost': 'remainingOvertimeCost',
        'remaining_overtime_work': 'remainingOvertimeWork',
        'remaining_work': 'remainingWork',
        'response_pending': 'responsePending',
        'start': 'start',
        'stop': 'stop',
        'resume': 'resume',
        'start_variance': 'startVariance',
        'summary': 'summary',
        'sv': 'sv',
        'units': 'units',
        'update_needed': 'updateNeeded',
        'vac': 'vac',
        'work': 'work',
        'work_contour': 'workContour',
        'bcws': 'bcws',
        'bcwp': 'bcwp',
        'booking_type': 'bookingType',
        'actual_work_protected': 'actualWorkProtected',
        'actual_overtime_work_protected': 'actualOvertimeWorkProtected',
        'creation_date': 'creationDate',
        'assn_owner': 'assnOwner',
        'assn_owner_guid': 'assnOwnerGuid',
        'budget_cost': 'budgetCost',
        'budget_work': 'budgetWork',
        'rate_scale': 'rateScale',
        'baselines': 'baselines',
        'extended_attributes': 'extendedAttributes'
    }

    def __init__(self, task_uid=-1, resource_uid=-1, uid=None, percent_work_complete=None, actual_cost=None, actual_finish=None, actual_overtime_cost=None, actual_overtime_work=None, actual_start=None, actual_work=None, acwp=None, confirmed=None, cost=None, cost_rate_table_type=None, cost_variance=None, cv=None, delay=None, finish=None, finish_variance=None, hyperlink=None, hyperlink_address=None, hyperlink_sub_address=None, work_variance=None, has_fixed_rate_units=None, fixed_material=None, leveling_delay=None, leveling_delay_format=None, linked_fields=None, milestone=None, notes=None, overallocated=None, overtime_cost=None, overtime_work=None, peak_units=None, regular_work=None, remaining_cost=None, remaining_overtime_cost=None, remaining_overtime_work=None, remaining_work=None, response_pending=None, start=None, stop=None, resume=None, start_variance=None, summary=None, sv=None, units=1.0, update_needed=None, vac=None, work=None, work_contour=None, bcws=None, bcwp=None, booking_type=None, actual_work_protected=None, actual_overtime_work_protected=None, creation_date=None, assn_owner=None, assn_owner_guid=None, budget_cost=None, budget_work=None, rate_scale=None, baselines=None, extended_attributes=None):  # noqa: E501
        """ResourceAssignment - a model defined in Swagger"""  # noqa: E501

        self._task_uid = None
        self._resource_uid = None
        self._uid = None
        self._percent_work_complete = None
        self._actual_cost = None
        self._actual_finish = None
        self._actual_overtime_cost = None
        self._actual_overtime_work = None
        self._actual_start = None
        self._actual_work = None
        self._acwp = None
        self._confirmed = None
        self._cost = None
        self._cost_rate_table_type = None
        self._cost_variance = None
        self._cv = None
        self._delay = None
        self._finish = None
        self._finish_variance = None
        self._hyperlink = None
        self._hyperlink_address = None
        self._hyperlink_sub_address = None
        self._work_variance = None
        self._has_fixed_rate_units = None
        self._fixed_material = None
        self._leveling_delay = None
        self._leveling_delay_format = None
        self._linked_fields = None
        self._milestone = None
        self._notes = None
        self._overallocated = None
        self._overtime_cost = None
        self._overtime_work = None
        self._peak_units = None
        self._regular_work = None
        self._remaining_cost = None
        self._remaining_overtime_cost = None
        self._remaining_overtime_work = None
        self._remaining_work = None
        self._response_pending = None
        self._start = None
        self._stop = None
        self._resume = None
        self._start_variance = None
        self._summary = None
        self._sv = None
        self._units = None
        self._update_needed = None
        self._vac = None
        self._work = None
        self._work_contour = None
        self._bcws = None
        self._bcwp = None
        self._booking_type = None
        self._actual_work_protected = None
        self._actual_overtime_work_protected = None
        self._creation_date = None
        self._assn_owner = None
        self._assn_owner_guid = None
        self._budget_cost = None
        self._budget_work = None
        self._rate_scale = None
        self._baselines = None
        self._extended_attributes = None
        self.discriminator = None

        if task_uid is not None:
            self.task_uid = task_uid
        if resource_uid is not None:
            self.resource_uid = resource_uid
        if uid is not None:
            self.uid = uid
        if percent_work_complete is not None:
            self.percent_work_complete = percent_work_complete
        if actual_cost is not None:
            self.actual_cost = actual_cost
        if actual_finish is not None:
            self.actual_finish = actual_finish
        if actual_overtime_cost is not None:
            self.actual_overtime_cost = actual_overtime_cost
        if actual_overtime_work is not None:
            self.actual_overtime_work = actual_overtime_work
        if actual_start is not None:
            self.actual_start = actual_start
        if actual_work is not None:
            self.actual_work = actual_work
        if acwp is not None:
            self.acwp = acwp
        if confirmed is not None:
            self.confirmed = confirmed
        if cost is not None:
            self.cost = cost
        if cost_rate_table_type is not None:
            self.cost_rate_table_type = cost_rate_table_type
        if cost_variance is not None:
            self.cost_variance = cost_variance
        if cv is not None:
            self.cv = cv
        if delay is not None:
            self.delay = delay
        if finish is not None:
            self.finish = finish
        if finish_variance is not None:
            self.finish_variance = finish_variance
        if hyperlink is not None:
            self.hyperlink = hyperlink
        if hyperlink_address is not None:
            self.hyperlink_address = hyperlink_address
        if hyperlink_sub_address is not None:
            self.hyperlink_sub_address = hyperlink_sub_address
        if work_variance is not None:
            self.work_variance = work_variance
        if has_fixed_rate_units is not None:
            self.has_fixed_rate_units = has_fixed_rate_units
        if fixed_material is not None:
            self.fixed_material = fixed_material
        if leveling_delay is not None:
            self.leveling_delay = leveling_delay
        if leveling_delay_format is not None:
            self.leveling_delay_format = leveling_delay_format
        if linked_fields is not None:
            self.linked_fields = linked_fields
        if milestone is not None:
            self.milestone = milestone
        if notes is not None:
            self.notes = notes
        if overallocated is not None:
            self.overallocated = overallocated
        if overtime_cost is not None:
            self.overtime_cost = overtime_cost
        if overtime_work is not None:
            self.overtime_work = overtime_work
        if peak_units is not None:
            self.peak_units = peak_units
        if regular_work is not None:
            self.regular_work = regular_work
        if remaining_cost is not None:
            self.remaining_cost = remaining_cost
        if remaining_overtime_cost is not None:
            self.remaining_overtime_cost = remaining_overtime_cost
        if remaining_overtime_work is not None:
            self.remaining_overtime_work = remaining_overtime_work
        if remaining_work is not None:
            self.remaining_work = remaining_work
        if response_pending is not None:
            self.response_pending = response_pending
        if start is not None:
            self.start = start
        if stop is not None:
            self.stop = stop
        if resume is not None:
            self.resume = resume
        if start_variance is not None:
            self.start_variance = start_variance
        if summary is not None:
            self.summary = summary
        if sv is not None:
            self.sv = sv
        if units is not None:
            self.units = units
        if update_needed is not None:
            self.update_needed = update_needed
        if vac is not None:
            self.vac = vac
        if work is not None:
            self.work = work
        if work_contour is not None:
            self.work_contour = work_contour
        if bcws is not None:
            self.bcws = bcws
        if bcwp is not None:
            self.bcwp = bcwp
        if booking_type is not None:
            self.booking_type = booking_type
        if actual_work_protected is not None:
            self.actual_work_protected = actual_work_protected
        if actual_overtime_work_protected is not None:
            self.actual_overtime_work_protected = actual_overtime_work_protected
        if creation_date is not None:
            self.creation_date = creation_date
        if assn_owner is not None:
            self.assn_owner = assn_owner
        if assn_owner_guid is not None:
            self.assn_owner_guid = assn_owner_guid
        if budget_cost is not None:
            self.budget_cost = budget_cost
        if budget_work is not None:
            self.budget_work = budget_work
        if rate_scale is not None:
            self.rate_scale = rate_scale
        if baselines is not None:
            self.baselines = baselines
        if extended_attributes is not None:
            self.extended_attributes = extended_attributes

    @property
    def task_uid(self):
        """Gets the task_uid of this ResourceAssignment.  # noqa: E501

        Returns or sets a task unique id to which a resource is assigned.  # noqa: E501

        :return: The task_uid of this ResourceAssignment.  # noqa: E501
        :rtype: int
        """
        return self._task_uid

    @task_uid.setter
    def task_uid(self, task_uid):
        """Sets the task_uid of this ResourceAssignment.

        Returns or sets a task unique id to which a resource is assigned.  # noqa: E501

        :param task_uid: The task_uid of this ResourceAssignment.  # noqa: E501
        :type: int
        """
        if task_uid is None:
            raise ValueError("Invalid value for `task_uid`, must not be `None`")  # noqa: E501
        self._task_uid = task_uid
    @property
    def resource_uid(self):
        """Gets the resource_uid of this ResourceAssignment.  # noqa: E501

        Returns or sets a resource unique id assigned to a task.  # noqa: E501

        :return: The resource_uid of this ResourceAssignment.  # noqa: E501
        :rtype: int
        """
        return self._resource_uid

    @resource_uid.setter
    def resource_uid(self, resource_uid):
        """Sets the resource_uid of this ResourceAssignment.

        Returns or sets a resource unique id assigned to a task.  # noqa: E501

        :param resource_uid: The resource_uid of this ResourceAssignment.  # noqa: E501
        :type: int
        """
        if resource_uid is None:
            raise ValueError("Invalid value for `resource_uid`, must not be `None`")  # noqa: E501
        self._resource_uid = resource_uid
    @property
    def uid(self):
        """Gets the uid of this ResourceAssignment.  # noqa: E501

        Returns or sets the unique identifier of an assignment.  # noqa: E501

        :return: The uid of this ResourceAssignment.  # noqa: E501
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this ResourceAssignment.

        Returns or sets the unique identifier of an assignment.  # noqa: E501

        :param uid: The uid of this ResourceAssignment.  # noqa: E501
        :type: int
        """
        if uid is None:
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501
        self._uid = uid
    @property
    def percent_work_complete(self):
        """Gets the percent_work_complete of this ResourceAssignment.  # noqa: E501

        Returns or sets the amount of a work completed on an assignment.  # noqa: E501

        :return: The percent_work_complete of this ResourceAssignment.  # noqa: E501
        :rtype: int
        """
        return self._percent_work_complete

    @percent_work_complete.setter
    def percent_work_complete(self, percent_work_complete):
        """Sets the percent_work_complete of this ResourceAssignment.

        Returns or sets the amount of a work completed on an assignment.  # noqa: E501

        :param percent_work_complete: The percent_work_complete of this ResourceAssignment.  # noqa: E501
        :type: int
        """
        if percent_work_complete is None:
            raise ValueError("Invalid value for `percent_work_complete`, must not be `None`")  # noqa: E501
        self._percent_work_complete = percent_work_complete
    @property
    def actual_cost(self):
        """Gets the actual_cost of this ResourceAssignment.  # noqa: E501

        Returns or sets the actual cost incurred on an assignment.  # noqa: E501

        :return: The actual_cost of this ResourceAssignment.  # noqa: E501
        :rtype: float
        """
        return self._actual_cost

    @actual_cost.setter
    def actual_cost(self, actual_cost):
        """Sets the actual_cost of this ResourceAssignment.

        Returns or sets the actual cost incurred on an assignment.  # noqa: E501

        :param actual_cost: The actual_cost of this ResourceAssignment.  # noqa: E501
        :type: float
        """
        if actual_cost is None:
            raise ValueError("Invalid value for `actual_cost`, must not be `None`")  # noqa: E501
        self._actual_cost = actual_cost
    @property
    def actual_finish(self):
        """Gets the actual_finish of this ResourceAssignment.  # noqa: E501

        Returns or sets the actual finish date of an assignment.  # noqa: E501

        :return: The actual_finish of this ResourceAssignment.  # noqa: E501
        :rtype: datetime
        """
        return self._actual_finish

    @actual_finish.setter
    def actual_finish(self, actual_finish):
        """Sets the actual_finish of this ResourceAssignment.

        Returns or sets the actual finish date of an assignment.  # noqa: E501

        :param actual_finish: The actual_finish of this ResourceAssignment.  # noqa: E501
        :type: datetime
        """
        if actual_finish is None:
            raise ValueError("Invalid value for `actual_finish`, must not be `None`")  # noqa: E501
        self._actual_finish = actual_finish
    @property
    def actual_overtime_cost(self):
        """Gets the actual_overtime_cost of this ResourceAssignment.  # noqa: E501

        Returns or sets the actual overtime cost incurred on an assignment.  # noqa: E501

        :return: The actual_overtime_cost of this ResourceAssignment.  # noqa: E501
        :rtype: float
        """
        return self._actual_overtime_cost

    @actual_overtime_cost.setter
    def actual_overtime_cost(self, actual_overtime_cost):
        """Sets the actual_overtime_cost of this ResourceAssignment.

        Returns or sets the actual overtime cost incurred on an assignment.  # noqa: E501

        :param actual_overtime_cost: The actual_overtime_cost of this ResourceAssignment.  # noqa: E501
        :type: float
        """
        if actual_overtime_cost is None:
            raise ValueError("Invalid value for `actual_overtime_cost`, must not be `None`")  # noqa: E501
        self._actual_overtime_cost = actual_overtime_cost
    @property
    def actual_overtime_work(self):
        """Gets the actual_overtime_work of this ResourceAssignment.  # noqa: E501

        Returns or sets the actual amount of an overtime work incurred on an assignment.  # noqa: E501

        :return: The actual_overtime_work of this ResourceAssignment.  # noqa: E501
        :rtype: str
        """
        return self._actual_overtime_work

    @actual_overtime_work.setter
    def actual_overtime_work(self, actual_overtime_work):
        """Sets the actual_overtime_work of this ResourceAssignment.

        Returns or sets the actual amount of an overtime work incurred on an assignment.  # noqa: E501

        :param actual_overtime_work: The actual_overtime_work of this ResourceAssignment.  # noqa: E501
        :type: str
        """
        if actual_overtime_work is None:
            raise ValueError("Invalid value for `actual_overtime_work`, must not be `None`")  # noqa: E501
        self._actual_overtime_work = actual_overtime_work
    @property
    def actual_start(self):
        """Gets the actual_start of this ResourceAssignment.  # noqa: E501

        Returns or sets the actual start date of an assignment.  # noqa: E501

        :return: The actual_start of this ResourceAssignment.  # noqa: E501
        :rtype: datetime
        """
        return self._actual_start

    @actual_start.setter
    def actual_start(self, actual_start):
        """Sets the actual_start of this ResourceAssignment.

        Returns or sets the actual start date of an assignment.  # noqa: E501

        :param actual_start: The actual_start of this ResourceAssignment.  # noqa: E501
        :type: datetime
        """
        if actual_start is None:
            raise ValueError("Invalid value for `actual_start`, must not be `None`")  # noqa: E501
        self._actual_start = actual_start
    @property
    def actual_work(self):
        """Gets the actual_work of this ResourceAssignment.  # noqa: E501

        Returns or sets the actual amount of a work incurred on an assignment.  # noqa: E501

        :return: The actual_work of this ResourceAssignment.  # noqa: E501
        :rtype: str
        """
        return self._actual_work

    @actual_work.setter
    def actual_work(self, actual_work):
        """Sets the actual_work of this ResourceAssignment.

        Returns or sets the actual amount of a work incurred on an assignment.  # noqa: E501

        :param actual_work: The actual_work of this ResourceAssignment.  # noqa: E501
        :type: str
        """
        if actual_work is None:
            raise ValueError("Invalid value for `actual_work`, must not be `None`")  # noqa: E501
        self._actual_work = actual_work
    @property
    def acwp(self):
        """Gets the acwp of this ResourceAssignment.  # noqa: E501

        Returns or sets the actual cost of a work performed on an assignment to-date.  # noqa: E501

        :return: The acwp of this ResourceAssignment.  # noqa: E501
        :rtype: float
        """
        return self._acwp

    @acwp.setter
    def acwp(self, acwp):
        """Sets the acwp of this ResourceAssignment.

        Returns or sets the actual cost of a work performed on an assignment to-date.  # noqa: E501

        :param acwp: The acwp of this ResourceAssignment.  # noqa: E501
        :type: float
        """
        if acwp is None:
            raise ValueError("Invalid value for `acwp`, must not be `None`")  # noqa: E501
        self._acwp = acwp
    @property
    def confirmed(self):
        """Gets the confirmed of this ResourceAssignment.  # noqa: E501

        Determines whether a resource has accepted all of its assignments.  # noqa: E501

        :return: The confirmed of this ResourceAssignment.  # noqa: E501
        :rtype: bool
        """
        return self._confirmed

    @confirmed.setter
    def confirmed(self, confirmed):
        """Sets the confirmed of this ResourceAssignment.

        Determines whether a resource has accepted all of its assignments.  # noqa: E501

        :param confirmed: The confirmed of this ResourceAssignment.  # noqa: E501
        :type: bool
        """
        if confirmed is None:
            raise ValueError("Invalid value for `confirmed`, must not be `None`")  # noqa: E501
        self._confirmed = confirmed
    @property
    def cost(self):
        """Gets the cost of this ResourceAssignment.  # noqa: E501

        Returns or sets the projected or scheduled cost of an assignment.  # noqa: E501

        :return: The cost of this ResourceAssignment.  # noqa: E501
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this ResourceAssignment.

        Returns or sets the projected or scheduled cost of an assignment.  # noqa: E501

        :param cost: The cost of this ResourceAssignment.  # noqa: E501
        :type: float
        """
        if cost is None:
            raise ValueError("Invalid value for `cost`, must not be `None`")  # noqa: E501
        self._cost = cost
    @property
    def cost_rate_table_type(self):
        """Gets the cost_rate_table_type of this ResourceAssignment.  # noqa: E501

        Returns or sets the cost rate table used for this assignment.  # noqa: E501

        :return: The cost_rate_table_type of this ResourceAssignment.  # noqa: E501
        :rtype: RateType
        """
        return self._cost_rate_table_type

    @cost_rate_table_type.setter
    def cost_rate_table_type(self, cost_rate_table_type):
        """Sets the cost_rate_table_type of this ResourceAssignment.

        Returns or sets the cost rate table used for this assignment.  # noqa: E501

        :param cost_rate_table_type: The cost_rate_table_type of this ResourceAssignment.  # noqa: E501
        :type: RateType
        """
        if cost_rate_table_type is None:
            raise ValueError("Invalid value for `cost_rate_table_type`, must not be `None`")  # noqa: E501
        self._cost_rate_table_type = cost_rate_table_type
    @property
    def cost_variance(self):
        """Gets the cost_variance of this ResourceAssignment.  # noqa: E501

        Returns or sets the difference between the cost and baseline cost of a resource.  # noqa: E501

        :return: The cost_variance of this ResourceAssignment.  # noqa: E501
        :rtype: float
        """
        return self._cost_variance

    @cost_variance.setter
    def cost_variance(self, cost_variance):
        """Sets the cost_variance of this ResourceAssignment.

        Returns or sets the difference between the cost and baseline cost of a resource.  # noqa: E501

        :param cost_variance: The cost_variance of this ResourceAssignment.  # noqa: E501
        :type: float
        """
        if cost_variance is None:
            raise ValueError("Invalid value for `cost_variance`, must not be `None`")  # noqa: E501
        self._cost_variance = cost_variance
    @property
    def cv(self):
        """Gets the cv of this ResourceAssignment.  # noqa: E501

        Returns or sets the earned value cost variance.  # noqa: E501

        :return: The cv of this ResourceAssignment.  # noqa: E501
        :rtype: float
        """
        return self._cv

    @cv.setter
    def cv(self, cv):
        """Sets the cv of this ResourceAssignment.

        Returns or sets the earned value cost variance.  # noqa: E501

        :param cv: The cv of this ResourceAssignment.  # noqa: E501
        :type: float
        """
        if cv is None:
            raise ValueError("Invalid value for `cv`, must not be `None`")  # noqa: E501
        self._cv = cv
    @property
    def delay(self):
        """Gets the delay of this ResourceAssignment.  # noqa: E501

        Returns or sets the delay of an assignment.  # noqa: E501

        :return: The delay of this ResourceAssignment.  # noqa: E501
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this ResourceAssignment.

        Returns or sets the delay of an assignment.  # noqa: E501

        :param delay: The delay of this ResourceAssignment.  # noqa: E501
        :type: int
        """
        if delay is None:
            raise ValueError("Invalid value for `delay`, must not be `None`")  # noqa: E501
        self._delay = delay
    @property
    def finish(self):
        """Gets the finish of this ResourceAssignment.  # noqa: E501

        Returns or sets the scheduled finish date of an assignment.  # noqa: E501

        :return: The finish of this ResourceAssignment.  # noqa: E501
        :rtype: datetime
        """
        return self._finish

    @finish.setter
    def finish(self, finish):
        """Sets the finish of this ResourceAssignment.

        Returns or sets the scheduled finish date of an assignment.  # noqa: E501

        :param finish: The finish of this ResourceAssignment.  # noqa: E501
        :type: datetime
        """
        if finish is None:
            raise ValueError("Invalid value for `finish`, must not be `None`")  # noqa: E501
        self._finish = finish
    @property
    def finish_variance(self):
        """Gets the finish_variance of this ResourceAssignment.  # noqa: E501

        Returns or sets the variance of an assignment finish date from a baseline finish date.  # noqa: E501

        :return: The finish_variance of this ResourceAssignment.  # noqa: E501
        :rtype: int
        """
        return self._finish_variance

    @finish_variance.setter
    def finish_variance(self, finish_variance):
        """Sets the finish_variance of this ResourceAssignment.

        Returns or sets the variance of an assignment finish date from a baseline finish date.  # noqa: E501

        :param finish_variance: The finish_variance of this ResourceAssignment.  # noqa: E501
        :type: int
        """
        if finish_variance is None:
            raise ValueError("Invalid value for `finish_variance`, must not be `None`")  # noqa: E501
        self._finish_variance = finish_variance
    @property
    def hyperlink(self):
        """Gets the hyperlink of this ResourceAssignment.  # noqa: E501

        Returns or sets the title of the hyperlink associated with an assignment.  # noqa: E501

        :return: The hyperlink of this ResourceAssignment.  # noqa: E501
        :rtype: str
        """
        return self._hyperlink

    @hyperlink.setter
    def hyperlink(self, hyperlink):
        """Sets the hyperlink of this ResourceAssignment.

        Returns or sets the title of the hyperlink associated with an assignment.  # noqa: E501

        :param hyperlink: The hyperlink of this ResourceAssignment.  # noqa: E501
        :type: str
        """
        self._hyperlink = hyperlink
    @property
    def hyperlink_address(self):
        """Gets the hyperlink_address of this ResourceAssignment.  # noqa: E501

        Returns or sets the hyperlink associated with an assignment.  # noqa: E501

        :return: The hyperlink_address of this ResourceAssignment.  # noqa: E501
        :rtype: str
        """
        return self._hyperlink_address

    @hyperlink_address.setter
    def hyperlink_address(self, hyperlink_address):
        """Sets the hyperlink_address of this ResourceAssignment.

        Returns or sets the hyperlink associated with an assignment.  # noqa: E501

        :param hyperlink_address: The hyperlink_address of this ResourceAssignment.  # noqa: E501
        :type: str
        """
        self._hyperlink_address = hyperlink_address
    @property
    def hyperlink_sub_address(self):
        """Gets the hyperlink_sub_address of this ResourceAssignment.  # noqa: E501

        Returns or sets the document bookmark of the hyperlink associated with an assignment.  # noqa: E501

        :return: The hyperlink_sub_address of this ResourceAssignment.  # noqa: E501
        :rtype: str
        """
        return self._hyperlink_sub_address

    @hyperlink_sub_address.setter
    def hyperlink_sub_address(self, hyperlink_sub_address):
        """Sets the hyperlink_sub_address of this ResourceAssignment.

        Returns or sets the document bookmark of the hyperlink associated with an assignment.  # noqa: E501

        :param hyperlink_sub_address: The hyperlink_sub_address of this ResourceAssignment.  # noqa: E501
        :type: str
        """
        self._hyperlink_sub_address = hyperlink_sub_address
    @property
    def work_variance(self):
        """Gets the work_variance of this ResourceAssignment.  # noqa: E501

        Returns or sets the variance of an assignment work from the baseline work as minutes.  # noqa: E501

        :return: The work_variance of this ResourceAssignment.  # noqa: E501
        :rtype: float
        """
        return self._work_variance

    @work_variance.setter
    def work_variance(self, work_variance):
        """Sets the work_variance of this ResourceAssignment.

        Returns or sets the variance of an assignment work from the baseline work as minutes.  # noqa: E501

        :param work_variance: The work_variance of this ResourceAssignment.  # noqa: E501
        :type: float
        """
        if work_variance is None:
            raise ValueError("Invalid value for `work_variance`, must not be `None`")  # noqa: E501
        self._work_variance = work_variance
    @property
    def has_fixed_rate_units(self):
        """Gets the has_fixed_rate_units of this ResourceAssignment.  # noqa: E501

        Determines whether the Units have Fixed Rate.  # noqa: E501

        :return: The has_fixed_rate_units of this ResourceAssignment.  # noqa: E501
        :rtype: bool
        """
        return self._has_fixed_rate_units

    @has_fixed_rate_units.setter
    def has_fixed_rate_units(self, has_fixed_rate_units):
        """Sets the has_fixed_rate_units of this ResourceAssignment.

        Determines whether the Units have Fixed Rate.  # noqa: E501

        :param has_fixed_rate_units: The has_fixed_rate_units of this ResourceAssignment.  # noqa: E501
        :type: bool
        """
        if has_fixed_rate_units is None:
            raise ValueError("Invalid value for `has_fixed_rate_units`, must not be `None`")  # noqa: E501
        self._has_fixed_rate_units = has_fixed_rate_units
    @property
    def fixed_material(self):
        """Gets the fixed_material of this ResourceAssignment.  # noqa: E501

        Determines whether the consumption of an assigned material resource occurs in a single, fixed amount.  # noqa: E501

        :return: The fixed_material of this ResourceAssignment.  # noqa: E501
        :rtype: bool
        """
        return self._fixed_material

    @fixed_material.setter
    def fixed_material(self, fixed_material):
        """Sets the fixed_material of this ResourceAssignment.

        Determines whether the consumption of an assigned material resource occurs in a single, fixed amount.  # noqa: E501

        :param fixed_material: The fixed_material of this ResourceAssignment.  # noqa: E501
        :type: bool
        """
        if fixed_material is None:
            raise ValueError("Invalid value for `fixed_material`, must not be `None`")  # noqa: E501
        self._fixed_material = fixed_material
    @property
    def leveling_delay(self):
        """Gets the leveling_delay of this ResourceAssignment.  # noqa: E501

        Returns or sets the delay caused by leveling.  # noqa: E501

        :return: The leveling_delay of this ResourceAssignment.  # noqa: E501
        :rtype: int
        """
        return self._leveling_delay

    @leveling_delay.setter
    def leveling_delay(self, leveling_delay):
        """Sets the leveling_delay of this ResourceAssignment.

        Returns or sets the delay caused by leveling.  # noqa: E501

        :param leveling_delay: The leveling_delay of this ResourceAssignment.  # noqa: E501
        :type: int
        """
        if leveling_delay is None:
            raise ValueError("Invalid value for `leveling_delay`, must not be `None`")  # noqa: E501
        self._leveling_delay = leveling_delay
    @property
    def leveling_delay_format(self):
        """Gets the leveling_delay_format of this ResourceAssignment.  # noqa: E501

        Returns or sets the duration format of a delay.  # noqa: E501

        :return: The leveling_delay_format of this ResourceAssignment.  # noqa: E501
        :rtype: TimeUnitType
        """
        return self._leveling_delay_format

    @leveling_delay_format.setter
    def leveling_delay_format(self, leveling_delay_format):
        """Sets the leveling_delay_format of this ResourceAssignment.

        Returns or sets the duration format of a delay.  # noqa: E501

        :param leveling_delay_format: The leveling_delay_format of this ResourceAssignment.  # noqa: E501
        :type: TimeUnitType
        """
        if leveling_delay_format is None:
            raise ValueError("Invalid value for `leveling_delay_format`, must not be `None`")  # noqa: E501
        self._leveling_delay_format = leveling_delay_format
    @property
    def linked_fields(self):
        """Gets the linked_fields of this ResourceAssignment.  # noqa: E501

        Determines whether the Project is linked to another OLE object.  # noqa: E501

        :return: The linked_fields of this ResourceAssignment.  # noqa: E501
        :rtype: bool
        """
        return self._linked_fields

    @linked_fields.setter
    def linked_fields(self, linked_fields):
        """Sets the linked_fields of this ResourceAssignment.

        Determines whether the Project is linked to another OLE object.  # noqa: E501

        :param linked_fields: The linked_fields of this ResourceAssignment.  # noqa: E501
        :type: bool
        """
        if linked_fields is None:
            raise ValueError("Invalid value for `linked_fields`, must not be `None`")  # noqa: E501
        self._linked_fields = linked_fields
    @property
    def milestone(self):
        """Gets the milestone of this ResourceAssignment.  # noqa: E501

        Determines whether the assignment is a milestone.  # noqa: E501

        :return: The milestone of this ResourceAssignment.  # noqa: E501
        :rtype: bool
        """
        return self._milestone

    @milestone.setter
    def milestone(self, milestone):
        """Sets the milestone of this ResourceAssignment.

        Determines whether the assignment is a milestone.  # noqa: E501

        :param milestone: The milestone of this ResourceAssignment.  # noqa: E501
        :type: bool
        """
        if milestone is None:
            raise ValueError("Invalid value for `milestone`, must not be `None`")  # noqa: E501
        self._milestone = milestone
    @property
    def notes(self):
        """Gets the notes of this ResourceAssignment.  # noqa: E501

        Returns or sets the text notes associated with an assignment.  # noqa: E501

        :return: The notes of this ResourceAssignment.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this ResourceAssignment.

        Returns or sets the text notes associated with an assignment.  # noqa: E501

        :param notes: The notes of this ResourceAssignment.  # noqa: E501
        :type: str
        """
        self._notes = notes
    @property
    def overallocated(self):
        """Gets the overallocated of this ResourceAssignment.  # noqa: E501

        Determines whether the assignment is overallocated.  # noqa: E501

        :return: The overallocated of this ResourceAssignment.  # noqa: E501
        :rtype: bool
        """
        return self._overallocated

    @overallocated.setter
    def overallocated(self, overallocated):
        """Sets the overallocated of this ResourceAssignment.

        Determines whether the assignment is overallocated.  # noqa: E501

        :param overallocated: The overallocated of this ResourceAssignment.  # noqa: E501
        :type: bool
        """
        if overallocated is None:
            raise ValueError("Invalid value for `overallocated`, must not be `None`")  # noqa: E501
        self._overallocated = overallocated
    @property
    def overtime_cost(self):
        """Gets the overtime_cost of this ResourceAssignment.  # noqa: E501

        Returns or sets the sum of the actual and remaining overtime cost of an assignment.  # noqa: E501

        :return: The overtime_cost of this ResourceAssignment.  # noqa: E501
        :rtype: float
        """
        return self._overtime_cost

    @overtime_cost.setter
    def overtime_cost(self, overtime_cost):
        """Sets the overtime_cost of this ResourceAssignment.

        Returns or sets the sum of the actual and remaining overtime cost of an assignment.  # noqa: E501

        :param overtime_cost: The overtime_cost of this ResourceAssignment.  # noqa: E501
        :type: float
        """
        if overtime_cost is None:
            raise ValueError("Invalid value for `overtime_cost`, must not be `None`")  # noqa: E501
        self._overtime_cost = overtime_cost
    @property
    def overtime_work(self):
        """Gets the overtime_work of this ResourceAssignment.  # noqa: E501

        Returns or sets the scheduled overtime work of an assignment.  # noqa: E501

        :return: The overtime_work of this ResourceAssignment.  # noqa: E501
        :rtype: str
        """
        return self._overtime_work

    @overtime_work.setter
    def overtime_work(self, overtime_work):
        """Sets the overtime_work of this ResourceAssignment.

        Returns or sets the scheduled overtime work of an assignment.  # noqa: E501

        :param overtime_work: The overtime_work of this ResourceAssignment.  # noqa: E501
        :type: str
        """
        if overtime_work is None:
            raise ValueError("Invalid value for `overtime_work`, must not be `None`")  # noqa: E501
        self._overtime_work = overtime_work
    @property
    def peak_units(self):
        """Gets the peak_units of this ResourceAssignment.  # noqa: E501

        Returns or sets the largest number of a resource's units assigned to a task.  # noqa: E501

        :return: The peak_units of this ResourceAssignment.  # noqa: E501
        :rtype: float
        """
        return self._peak_units

    @peak_units.setter
    def peak_units(self, peak_units):
        """Sets the peak_units of this ResourceAssignment.

        Returns or sets the largest number of a resource's units assigned to a task.  # noqa: E501

        :param peak_units: The peak_units of this ResourceAssignment.  # noqa: E501
        :type: float
        """
        if peak_units is None:
            raise ValueError("Invalid value for `peak_units`, must not be `None`")  # noqa: E501
        self._peak_units = peak_units
    @property
    def regular_work(self):
        """Gets the regular_work of this ResourceAssignment.  # noqa: E501

        Returns or sets the amount of a non-overtime work scheduled for an assignment.  # noqa: E501

        :return: The regular_work of this ResourceAssignment.  # noqa: E501
        :rtype: str
        """
        return self._regular_work

    @regular_work.setter
    def regular_work(self, regular_work):
        """Sets the regular_work of this ResourceAssignment.

        Returns or sets the amount of a non-overtime work scheduled for an assignment.  # noqa: E501

        :param regular_work: The regular_work of this ResourceAssignment.  # noqa: E501
        :type: str
        """
        if regular_work is None:
            raise ValueError("Invalid value for `regular_work`, must not be `None`")  # noqa: E501
        self._regular_work = regular_work
    @property
    def remaining_cost(self):
        """Gets the remaining_cost of this ResourceAssignment.  # noqa: E501

        Returns or sets the remaining projected cost of completing an assignment.  # noqa: E501

        :return: The remaining_cost of this ResourceAssignment.  # noqa: E501
        :rtype: float
        """
        return self._remaining_cost

    @remaining_cost.setter
    def remaining_cost(self, remaining_cost):
        """Sets the remaining_cost of this ResourceAssignment.

        Returns or sets the remaining projected cost of completing an assignment.  # noqa: E501

        :param remaining_cost: The remaining_cost of this ResourceAssignment.  # noqa: E501
        :type: float
        """
        if remaining_cost is None:
            raise ValueError("Invalid value for `remaining_cost`, must not be `None`")  # noqa: E501
        self._remaining_cost = remaining_cost
    @property
    def remaining_overtime_cost(self):
        """Gets the remaining_overtime_cost of this ResourceAssignment.  # noqa: E501

        Returns or sets the remaining projected overtime cost of completing an assignment.  # noqa: E501

        :return: The remaining_overtime_cost of this ResourceAssignment.  # noqa: E501
        :rtype: float
        """
        return self._remaining_overtime_cost

    @remaining_overtime_cost.setter
    def remaining_overtime_cost(self, remaining_overtime_cost):
        """Sets the remaining_overtime_cost of this ResourceAssignment.

        Returns or sets the remaining projected overtime cost of completing an assignment.  # noqa: E501

        :param remaining_overtime_cost: The remaining_overtime_cost of this ResourceAssignment.  # noqa: E501
        :type: float
        """
        if remaining_overtime_cost is None:
            raise ValueError("Invalid value for `remaining_overtime_cost`, must not be `None`")  # noqa: E501
        self._remaining_overtime_cost = remaining_overtime_cost
    @property
    def remaining_overtime_work(self):
        """Gets the remaining_overtime_work of this ResourceAssignment.  # noqa: E501

        Returns or sets the remaining overtime work scheduled to complete an assignment.  # noqa: E501

        :return: The remaining_overtime_work of this ResourceAssignment.  # noqa: E501
        :rtype: str
        """
        return self._remaining_overtime_work

    @remaining_overtime_work.setter
    def remaining_overtime_work(self, remaining_overtime_work):
        """Sets the remaining_overtime_work of this ResourceAssignment.

        Returns or sets the remaining overtime work scheduled to complete an assignment.  # noqa: E501

        :param remaining_overtime_work: The remaining_overtime_work of this ResourceAssignment.  # noqa: E501
        :type: str
        """
        if remaining_overtime_work is None:
            raise ValueError("Invalid value for `remaining_overtime_work`, must not be `None`")  # noqa: E501
        self._remaining_overtime_work = remaining_overtime_work
    @property
    def remaining_work(self):
        """Gets the remaining_work of this ResourceAssignment.  # noqa: E501

        Returns or sets the remaining work scheduled to complete an assignment.  # noqa: E501

        :return: The remaining_work of this ResourceAssignment.  # noqa: E501
        :rtype: str
        """
        return self._remaining_work

    @remaining_work.setter
    def remaining_work(self, remaining_work):
        """Sets the remaining_work of this ResourceAssignment.

        Returns or sets the remaining work scheduled to complete an assignment.  # noqa: E501

        :param remaining_work: The remaining_work of this ResourceAssignment.  # noqa: E501
        :type: str
        """
        if remaining_work is None:
            raise ValueError("Invalid value for `remaining_work`, must not be `None`")  # noqa: E501
        self._remaining_work = remaining_work
    @property
    def response_pending(self):
        """Gets the response_pending of this ResourceAssignment.  # noqa: E501

        Determines whether the response has been received for a TeamAssign message.  # noqa: E501

        :return: The response_pending of this ResourceAssignment.  # noqa: E501
        :rtype: bool
        """
        return self._response_pending

    @response_pending.setter
    def response_pending(self, response_pending):
        """Sets the response_pending of this ResourceAssignment.

        Determines whether the response has been received for a TeamAssign message.  # noqa: E501

        :param response_pending: The response_pending of this ResourceAssignment.  # noqa: E501
        :type: bool
        """
        if response_pending is None:
            raise ValueError("Invalid value for `response_pending`, must not be `None`")  # noqa: E501
        self._response_pending = response_pending
    @property
    def start(self):
        """Gets the start of this ResourceAssignment.  # noqa: E501

        Returns or sets the scheduled start date of an assignment.  # noqa: E501

        :return: The start of this ResourceAssignment.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ResourceAssignment.

        Returns or sets the scheduled start date of an assignment.  # noqa: E501

        :param start: The start of this ResourceAssignment.  # noqa: E501
        :type: datetime
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501
        self._start = start
    @property
    def stop(self):
        """Gets the stop of this ResourceAssignment.  # noqa: E501

        Returns or sets the date when assignment is stopped.  # noqa: E501

        :return: The stop of this ResourceAssignment.  # noqa: E501
        :rtype: datetime
        """
        return self._stop

    @stop.setter
    def stop(self, stop):
        """Sets the stop of this ResourceAssignment.

        Returns or sets the date when assignment is stopped.  # noqa: E501

        :param stop: The stop of this ResourceAssignment.  # noqa: E501
        :type: datetime
        """
        if stop is None:
            raise ValueError("Invalid value for `stop`, must not be `None`")  # noqa: E501
        self._stop = stop
    @property
    def resume(self):
        """Gets the resume of this ResourceAssignment.  # noqa: E501

        Returns or sets the date when assignment is resumed.  # noqa: E501

        :return: The resume of this ResourceAssignment.  # noqa: E501
        :rtype: datetime
        """
        return self._resume

    @resume.setter
    def resume(self, resume):
        """Sets the resume of this ResourceAssignment.

        Returns or sets the date when assignment is resumed.  # noqa: E501

        :param resume: The resume of this ResourceAssignment.  # noqa: E501
        :type: datetime
        """
        if resume is None:
            raise ValueError("Invalid value for `resume`, must not be `None`")  # noqa: E501
        self._resume = resume
    @property
    def start_variance(self):
        """Gets the start_variance of this ResourceAssignment.  # noqa: E501

        Returns or sets the variance of an assignment start date from a baseline start date.  # noqa: E501

        :return: The start_variance of this ResourceAssignment.  # noqa: E501
        :rtype: int
        """
        return self._start_variance

    @start_variance.setter
    def start_variance(self, start_variance):
        """Sets the start_variance of this ResourceAssignment.

        Returns or sets the variance of an assignment start date from a baseline start date.  # noqa: E501

        :param start_variance: The start_variance of this ResourceAssignment.  # noqa: E501
        :type: int
        """
        if start_variance is None:
            raise ValueError("Invalid value for `start_variance`, must not be `None`")  # noqa: E501
        self._start_variance = start_variance
    @property
    def summary(self):
        """Gets the summary of this ResourceAssignment.  # noqa: E501

        Determines whether the task is a summary task.  # noqa: E501

        :return: The summary of this ResourceAssignment.  # noqa: E501
        :rtype: bool
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this ResourceAssignment.

        Determines whether the task is a summary task.  # noqa: E501

        :param summary: The summary of this ResourceAssignment.  # noqa: E501
        :type: bool
        """
        if summary is None:
            raise ValueError("Invalid value for `summary`, must not be `None`")  # noqa: E501
        self._summary = summary
    @property
    def sv(self):
        """Gets the sv of this ResourceAssignment.  # noqa: E501

        Returns or sets the earned value schedule variance, through the project status date.  # noqa: E501

        :return: The sv of this ResourceAssignment.  # noqa: E501
        :rtype: float
        """
        return self._sv

    @sv.setter
    def sv(self, sv):
        """Sets the sv of this ResourceAssignment.

        Returns or sets the earned value schedule variance, through the project status date.  # noqa: E501

        :param sv: The sv of this ResourceAssignment.  # noqa: E501
        :type: float
        """
        if sv is None:
            raise ValueError("Invalid value for `sv`, must not be `None`")  # noqa: E501
        self._sv = sv
    @property
    def units(self):
        """Gets the units of this ResourceAssignment.  # noqa: E501

        Returns or sets the number of units for an assignment.  # noqa: E501

        :return: The units of this ResourceAssignment.  # noqa: E501
        :rtype: float
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this ResourceAssignment.

        Returns or sets the number of units for an assignment.  # noqa: E501

        :param units: The units of this ResourceAssignment.  # noqa: E501
        :type: float
        """
        if units is None:
            raise ValueError("Invalid value for `units`, must not be `None`")  # noqa: E501
        self._units = units
    @property
    def update_needed(self):
        """Gets the update_needed of this ResourceAssignment.  # noqa: E501

        Determines whether the resource assigned to a task needs to be updated as to the status of the task.  # noqa: E501

        :return: The update_needed of this ResourceAssignment.  # noqa: E501
        :rtype: bool
        """
        return self._update_needed

    @update_needed.setter
    def update_needed(self, update_needed):
        """Sets the update_needed of this ResourceAssignment.

        Determines whether the resource assigned to a task needs to be updated as to the status of the task.  # noqa: E501

        :param update_needed: The update_needed of this ResourceAssignment.  # noqa: E501
        :type: bool
        """
        if update_needed is None:
            raise ValueError("Invalid value for `update_needed`, must not be `None`")  # noqa: E501
        self._update_needed = update_needed
    @property
    def vac(self):
        """Gets the vac of this ResourceAssignment.  # noqa: E501

        Returns or sets the difference between basline cost and total cost. Read/write Double.  # noqa: E501

        :return: The vac of this ResourceAssignment.  # noqa: E501
        :rtype: float
        """
        return self._vac

    @vac.setter
    def vac(self, vac):
        """Sets the vac of this ResourceAssignment.

        Returns or sets the difference between basline cost and total cost. Read/write Double.  # noqa: E501

        :param vac: The vac of this ResourceAssignment.  # noqa: E501
        :type: float
        """
        if vac is None:
            raise ValueError("Invalid value for `vac`, must not be `None`")  # noqa: E501
        self._vac = vac
    @property
    def work(self):
        """Gets the work of this ResourceAssignment.  # noqa: E501

        Returns or sets the amount of scheduled work for an assignment. Read/write TimeSpan.  # noqa: E501

        :return: The work of this ResourceAssignment.  # noqa: E501
        :rtype: str
        """
        return self._work

    @work.setter
    def work(self, work):
        """Sets the work of this ResourceAssignment.

        Returns or sets the amount of scheduled work for an assignment. Read/write TimeSpan.  # noqa: E501

        :param work: The work of this ResourceAssignment.  # noqa: E501
        :type: str
        """
        if work is None:
            raise ValueError("Invalid value for `work`, must not be `None`")  # noqa: E501
        self._work = work
    @property
    def work_contour(self):
        """Gets the work_contour of this ResourceAssignment.  # noqa: E501

        Returns or sets the work contour of an assignment.  # noqa: E501

        :return: The work_contour of this ResourceAssignment.  # noqa: E501
        :rtype: WorkContourType
        """
        return self._work_contour

    @work_contour.setter
    def work_contour(self, work_contour):
        """Sets the work_contour of this ResourceAssignment.

        Returns or sets the work contour of an assignment.  # noqa: E501

        :param work_contour: The work_contour of this ResourceAssignment.  # noqa: E501
        :type: WorkContourType
        """
        if work_contour is None:
            raise ValueError("Invalid value for `work_contour`, must not be `None`")  # noqa: E501
        self._work_contour = work_contour
    @property
    def bcws(self):
        """Gets the bcws of this ResourceAssignment.  # noqa: E501

        Returns or sets the budgeted cost of a work on assignment.  # noqa: E501

        :return: The bcws of this ResourceAssignment.  # noqa: E501
        :rtype: float
        """
        return self._bcws

    @bcws.setter
    def bcws(self, bcws):
        """Sets the bcws of this ResourceAssignment.

        Returns or sets the budgeted cost of a work on assignment.  # noqa: E501

        :param bcws: The bcws of this ResourceAssignment.  # noqa: E501
        :type: float
        """
        if bcws is None:
            raise ValueError("Invalid value for `bcws`, must not be `None`")  # noqa: E501
        self._bcws = bcws
    @property
    def bcwp(self):
        """Gets the bcwp of this ResourceAssignment.  # noqa: E501

        Returns or sets the budgeted cost of a work performed on assignment to-date.  # noqa: E501

        :return: The bcwp of this ResourceAssignment.  # noqa: E501
        :rtype: float
        """
        return self._bcwp

    @bcwp.setter
    def bcwp(self, bcwp):
        """Sets the bcwp of this ResourceAssignment.

        Returns or sets the budgeted cost of a work performed on assignment to-date.  # noqa: E501

        :param bcwp: The bcwp of this ResourceAssignment.  # noqa: E501
        :type: float
        """
        if bcwp is None:
            raise ValueError("Invalid value for `bcwp`, must not be `None`")  # noqa: E501
        self._bcwp = bcwp
    @property
    def booking_type(self):
        """Gets the booking_type of this ResourceAssignment.  # noqa: E501

        Returns or sets the booking type of an assignment.  # noqa: E501

        :return: The booking_type of this ResourceAssignment.  # noqa: E501
        :rtype: BookingType
        """
        return self._booking_type

    @booking_type.setter
    def booking_type(self, booking_type):
        """Sets the booking_type of this ResourceAssignment.

        Returns or sets the booking type of an assignment.  # noqa: E501

        :param booking_type: The booking_type of this ResourceAssignment.  # noqa: E501
        :type: BookingType
        """
        if booking_type is None:
            raise ValueError("Invalid value for `booking_type`, must not be `None`")  # noqa: E501
        self._booking_type = booking_type
    @property
    def actual_work_protected(self):
        """Gets the actual_work_protected of this ResourceAssignment.  # noqa: E501

        Returns or sets the duration through which actual work is protected.  # noqa: E501

        :return: The actual_work_protected of this ResourceAssignment.  # noqa: E501
        :rtype: str
        """
        return self._actual_work_protected

    @actual_work_protected.setter
    def actual_work_protected(self, actual_work_protected):
        """Sets the actual_work_protected of this ResourceAssignment.

        Returns or sets the duration through which actual work is protected.  # noqa: E501

        :param actual_work_protected: The actual_work_protected of this ResourceAssignment.  # noqa: E501
        :type: str
        """
        if actual_work_protected is None:
            raise ValueError("Invalid value for `actual_work_protected`, must not be `None`")  # noqa: E501
        self._actual_work_protected = actual_work_protected
    @property
    def actual_overtime_work_protected(self):
        """Gets the actual_overtime_work_protected of this ResourceAssignment.  # noqa: E501

        Returns or sets the duration through which actual overtime work is protected.  # noqa: E501

        :return: The actual_overtime_work_protected of this ResourceAssignment.  # noqa: E501
        :rtype: str
        """
        return self._actual_overtime_work_protected

    @actual_overtime_work_protected.setter
    def actual_overtime_work_protected(self, actual_overtime_work_protected):
        """Sets the actual_overtime_work_protected of this ResourceAssignment.

        Returns or sets the duration through which actual overtime work is protected.  # noqa: E501

        :param actual_overtime_work_protected: The actual_overtime_work_protected of this ResourceAssignment.  # noqa: E501
        :type: str
        """
        if actual_overtime_work_protected is None:
            raise ValueError("Invalid value for `actual_overtime_work_protected`, must not be `None`")  # noqa: E501
        self._actual_overtime_work_protected = actual_overtime_work_protected
    @property
    def creation_date(self):
        """Gets the creation_date of this ResourceAssignment.  # noqa: E501

        Returns or sets the date that the assignment was created.  # noqa: E501

        :return: The creation_date of this ResourceAssignment.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ResourceAssignment.

        Returns or sets the date that the assignment was created.  # noqa: E501

        :param creation_date: The creation_date of this ResourceAssignment.  # noqa: E501
        :type: datetime
        """
        if creation_date is None:
            raise ValueError("Invalid value for `creation_date`, must not be `None`")  # noqa: E501
        self._creation_date = creation_date
    @property
    def assn_owner(self):
        """Gets the assn_owner of this ResourceAssignment.  # noqa: E501

        Returns or sets the name of an assignment owner.  # noqa: E501

        :return: The assn_owner of this ResourceAssignment.  # noqa: E501
        :rtype: str
        """
        return self._assn_owner

    @assn_owner.setter
    def assn_owner(self, assn_owner):
        """Sets the assn_owner of this ResourceAssignment.

        Returns or sets the name of an assignment owner.  # noqa: E501

        :param assn_owner: The assn_owner of this ResourceAssignment.  # noqa: E501
        :type: str
        """
        self._assn_owner = assn_owner
    @property
    def assn_owner_guid(self):
        """Gets the assn_owner_guid of this ResourceAssignment.  # noqa: E501

        Returns or sets the Guid of an assignment owner.  # noqa: E501

        :return: The assn_owner_guid of this ResourceAssignment.  # noqa: E501
        :rtype: str
        """
        return self._assn_owner_guid

    @assn_owner_guid.setter
    def assn_owner_guid(self, assn_owner_guid):
        """Sets the assn_owner_guid of this ResourceAssignment.

        Returns or sets the Guid of an assignment owner.  # noqa: E501

        :param assn_owner_guid: The assn_owner_guid of this ResourceAssignment.  # noqa: E501
        :type: str
        """
        self._assn_owner_guid = assn_owner_guid
    @property
    def budget_cost(self):
        """Gets the budget_cost of this ResourceAssignment.  # noqa: E501

        Returns or sets the budgeted cost of resources on an assignment.  # noqa: E501

        :return: The budget_cost of this ResourceAssignment.  # noqa: E501
        :rtype: float
        """
        return self._budget_cost

    @budget_cost.setter
    def budget_cost(self, budget_cost):
        """Sets the budget_cost of this ResourceAssignment.

        Returns or sets the budgeted cost of resources on an assignment.  # noqa: E501

        :param budget_cost: The budget_cost of this ResourceAssignment.  # noqa: E501
        :type: float
        """
        if budget_cost is None:
            raise ValueError("Invalid value for `budget_cost`, must not be `None`")  # noqa: E501
        self._budget_cost = budget_cost
    @property
    def budget_work(self):
        """Gets the budget_work of this ResourceAssignment.  # noqa: E501

        Returns or sets the budgeted work amount for a work or material resources on an assignment.  # noqa: E501

        :return: The budget_work of this ResourceAssignment.  # noqa: E501
        :rtype: str
        """
        return self._budget_work

    @budget_work.setter
    def budget_work(self, budget_work):
        """Sets the budget_work of this ResourceAssignment.

        Returns or sets the budgeted work amount for a work or material resources on an assignment.  # noqa: E501

        :param budget_work: The budget_work of this ResourceAssignment.  # noqa: E501
        :type: str
        """
        if budget_work is None:
            raise ValueError("Invalid value for `budget_work`, must not be `None`")  # noqa: E501
        self._budget_work = budget_work
    @property
    def rate_scale(self):
        """Gets the rate_scale of this ResourceAssignment.  # noqa: E501

        Returns the time unit for the usage rate of the material resource assignment.  # noqa: E501

        :return: The rate_scale of this ResourceAssignment.  # noqa: E501
        :rtype: RateScaleType
        """
        return self._rate_scale

    @rate_scale.setter
    def rate_scale(self, rate_scale):
        """Sets the rate_scale of this ResourceAssignment.

        Returns the time unit for the usage rate of the material resource assignment.  # noqa: E501

        :param rate_scale: The rate_scale of this ResourceAssignment.  # noqa: E501
        :type: RateScaleType
        """
        if rate_scale is None:
            raise ValueError("Invalid value for `rate_scale`, must not be `None`")  # noqa: E501
        self._rate_scale = rate_scale
    @property
    def baselines(self):
        """Gets the baselines of this ResourceAssignment.  # noqa: E501

        List of ResourceAssignment's Baseline values.  # noqa: E501

        :return: The baselines of this ResourceAssignment.  # noqa: E501
        :rtype: list[AssignmentBaseline]
        """
        return self._baselines

    @baselines.setter
    def baselines(self, baselines):
        """Sets the baselines of this ResourceAssignment.

        List of ResourceAssignment's Baseline values.  # noqa: E501

        :param baselines: The baselines of this ResourceAssignment.  # noqa: E501
        :type: list[AssignmentBaseline]
        """
        self._baselines = baselines
    @property
    def extended_attributes(self):
        """Gets the extended_attributes of this ResourceAssignment.  # noqa: E501

        ResourceAssignment extended attributes.  # noqa: E501

        :return: The extended_attributes of this ResourceAssignment.  # noqa: E501
        :rtype: list[ExtendedAttribute]
        """
        return self._extended_attributes

    @extended_attributes.setter
    def extended_attributes(self, extended_attributes):
        """Sets the extended_attributes of this ResourceAssignment.

        ResourceAssignment extended attributes.  # noqa: E501

        :param extended_attributes: The extended_attributes of this ResourceAssignment.  # noqa: E501
        :type: list[ExtendedAttribute]
        """
        self._extended_attributes = extended_attributes
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
        if not isinstance(other, ResourceAssignment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
