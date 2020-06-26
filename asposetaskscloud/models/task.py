# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="Task.py">
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


class Task(object):
    """Represents project task.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'uid': 'int',
        'id': 'int',
        'name': 'str',
        'duration_text': 'str',
        'duration': 'str',
        'start': 'datetime',
        'finish': 'datetime',
        'start_text': 'str',
        'finish_text': 'str',
        'percent_complete': 'int',
        'percent_work_complete': 'int',
        'is_active': 'bool',
        'actual_cost': 'float',
        'actual_duration': 'str',
        'actual_finish': 'datetime',
        'actual_overtime_cost': 'float',
        'actual_overtime_work': 'str',
        'actual_work_protected': 'str',
        'actual_overtime_work_protected': 'str',
        'actual_start': 'datetime',
        'budget_work': 'str',
        'budget_cost': 'float',
        'constraint_date': 'datetime',
        'constraint_type': 'ConstraintType',
        'contact': 'str',
        'cost': 'float',
        'cv': 'float',
        'deadline': 'datetime',
        'duration_variance': 'str',
        'early_finish': 'datetime',
        'early_start': 'datetime',
        'is_effort_driven': 'bool',
        'is_external_task': 'bool',
        'external_task_project': 'str',
        'external_id': 'int',
        'finish_slack': 'int',
        'finish_variance': 'int',
        'fixed_cost': 'float',
        'fixed_cost_accrual': 'CostAccrualType',
        'free_slack': 'int',
        'guid': 'str',
        'hide_bar': 'bool',
        'ignore_resource_calendar': 'bool',
        'late_finish': 'datetime',
        'late_start': 'datetime',
        'is_level_assignments': 'bool',
        'can_leveling_split': 'bool',
        'leveling_delay': 'int',
        'is_marked': 'bool',
        'is_milestone': 'bool',
        'is_critical': 'bool',
        'is_subproject': 'bool',
        'is_subproject_read_only': 'bool',
        'subproject_name': 'str',
        'is_summary': 'bool',
        'subtasks_uids': 'list[int]',
        'outline_level': 'int',
        'is_over_allocated': 'bool',
        'is_estimated': 'bool',
        'overtime_cost': 'float',
        'overtime_work': 'str',
        'physical_percent_complete': 'int',
        'pre_leveled_finish': 'datetime',
        'pre_leveled_start': 'datetime',
        'is_recurring': 'bool',
        'regular_work': 'str',
        'remaining_cost': 'float',
        'remaining_duration': 'str',
        'remaining_overtime_cost': 'float',
        'remaining_overtime_work': 'str',
        'remaining_work': 'str',
        'resume': 'datetime',
        'is_resume_valid': 'bool',
        'stop': 'datetime',
        'is_rollup': 'bool',
        'start_slack': 'int',
        'start_variance': 'int',
        'calendar_uid': 'int',
        'is_manual': 'bool',
        'manual_start': 'datetime',
        'manual_finish': 'datetime',
        'manual_duration': 'str',
        'total_slack': 'int',
        'type': 'TaskType',
        'wbs': 'str',
        'priority': 'int',
        'work': 'str',
        'work_variance': 'float',
        'notes_text': 'str',
        'notes_rtf': 'str',
        'acwp': 'float',
        'bcws': 'float',
        'bcwp': 'float',
        'leveling_delay_format': 'TimeUnitType',
        'predecessors': 'str',
        'successors': 'str',
        'ignore_warnings': 'bool',
        'is_expanded': 'bool',
        'display_on_timeline': 'bool',
        'display_as_summary': 'bool',
        'hyperlink': 'str',
        'hyperlink_address': 'str',
        'hyperlink_sub_address': 'str',
        'earned_value_method': 'EarnedValueMethodType',
        'is_published': 'bool',
        'status_manager': 'str',
        'commitment_start': 'datetime',
        'commitment_finish': 'datetime',
        'commitment_type': 'int',
        'baselines': 'list[TaskBaseline]',
        'extended_attributes': 'list[ExtendedAttribute]',
        'outline_codes': 'list[OutlineCode]',
        'warning': 'bool'
    }

    attribute_map = {
        'uid': 'uid',
        'id': 'id',
        'name': 'name',
        'duration_text': 'durationText',
        'duration': 'duration',
        'start': 'start',
        'finish': 'finish',
        'start_text': 'startText',
        'finish_text': 'finishText',
        'percent_complete': 'percentComplete',
        'percent_work_complete': 'percentWorkComplete',
        'is_active': 'isActive',
        'actual_cost': 'actualCost',
        'actual_duration': 'actualDuration',
        'actual_finish': 'actualFinish',
        'actual_overtime_cost': 'actualOvertimeCost',
        'actual_overtime_work': 'actualOvertimeWork',
        'actual_work_protected': 'actualWorkProtected',
        'actual_overtime_work_protected': 'actualOvertimeWorkProtected',
        'actual_start': 'actualStart',
        'budget_work': 'budgetWork',
        'budget_cost': 'budgetCost',
        'constraint_date': 'constraintDate',
        'constraint_type': 'constraintType',
        'contact': 'contact',
        'cost': 'cost',
        'cv': 'cv',
        'deadline': 'deadline',
        'duration_variance': 'durationVariance',
        'early_finish': 'earlyFinish',
        'early_start': 'earlyStart',
        'is_effort_driven': 'isEffortDriven',
        'is_external_task': 'isExternalTask',
        'external_task_project': 'externalTaskProject',
        'external_id': 'externalId',
        'finish_slack': 'finishSlack',
        'finish_variance': 'finishVariance',
        'fixed_cost': 'fixedCost',
        'fixed_cost_accrual': 'fixedCostAccrual',
        'free_slack': 'freeSlack',
        'guid': 'guid',
        'hide_bar': 'hideBar',
        'ignore_resource_calendar': 'ignoreResourceCalendar',
        'late_finish': 'lateFinish',
        'late_start': 'lateStart',
        'is_level_assignments': 'isLevelAssignments',
        'can_leveling_split': 'canLevelingSplit',
        'leveling_delay': 'levelingDelay',
        'is_marked': 'isMarked',
        'is_milestone': 'isMilestone',
        'is_critical': 'isCritical',
        'is_subproject': 'isSubproject',
        'is_subproject_read_only': 'isSubprojectReadOnly',
        'subproject_name': 'subprojectName',
        'is_summary': 'isSummary',
        'subtasks_uids': 'subtasksUids',
        'outline_level': 'outlineLevel',
        'is_over_allocated': 'isOverAllocated',
        'is_estimated': 'isEstimated',
        'overtime_cost': 'overtimeCost',
        'overtime_work': 'overtimeWork',
        'physical_percent_complete': 'physicalPercentComplete',
        'pre_leveled_finish': 'preLeveledFinish',
        'pre_leveled_start': 'preLeveledStart',
        'is_recurring': 'isRecurring',
        'regular_work': 'regularWork',
        'remaining_cost': 'remainingCost',
        'remaining_duration': 'remainingDuration',
        'remaining_overtime_cost': 'remainingOvertimeCost',
        'remaining_overtime_work': 'remainingOvertimeWork',
        'remaining_work': 'remainingWork',
        'resume': 'resume',
        'is_resume_valid': 'isResumeValid',
        'stop': 'stop',
        'is_rollup': 'isRollup',
        'start_slack': 'startSlack',
        'start_variance': 'startVariance',
        'calendar_uid': 'calendarUid',
        'is_manual': 'isManual',
        'manual_start': 'manualStart',
        'manual_finish': 'manualFinish',
        'manual_duration': 'manualDuration',
        'total_slack': 'totalSlack',
        'type': 'type',
        'wbs': 'wbs',
        'priority': 'priority',
        'work': 'work',
        'work_variance': 'workVariance',
        'notes_text': 'notesText',
        'notes_rtf': 'notesRTF',
        'acwp': 'acwp',
        'bcws': 'bcws',
        'bcwp': 'bcwp',
        'leveling_delay_format': 'levelingDelayFormat',
        'predecessors': 'predecessors',
        'successors': 'successors',
        'ignore_warnings': 'ignoreWarnings',
        'is_expanded': 'isExpanded',
        'display_on_timeline': 'displayOnTimeline',
        'display_as_summary': 'displayAsSummary',
        'hyperlink': 'hyperlink',
        'hyperlink_address': 'hyperlinkAddress',
        'hyperlink_sub_address': 'hyperlinkSubAddress',
        'earned_value_method': 'earnedValueMethod',
        'is_published': 'isPublished',
        'status_manager': 'statusManager',
        'commitment_start': 'commitmentStart',
        'commitment_finish': 'commitmentFinish',
        'commitment_type': 'commitmentType',
        'baselines': 'baselines',
        'extended_attributes': 'extendedAttributes',
        'outline_codes': 'outlineCodes',
        'warning': 'warning'
    }

    def __init__(self, uid=None, id=None, name=None, duration_text=None, duration=None, start=None, finish=None, start_text=None, finish_text=None, percent_complete=None, percent_work_complete=None, is_active=True, actual_cost=None, actual_duration=None, actual_finish=None, actual_overtime_cost=None, actual_overtime_work=None, actual_work_protected=None, actual_overtime_work_protected=None, actual_start=None, budget_work=None, budget_cost=None, constraint_date=None, constraint_type=None, contact=None, cost=None, cv=None, deadline=None, duration_variance=None, early_finish=None, early_start=None, is_effort_driven=None, is_external_task=None, external_task_project=None, external_id=None, finish_slack=None, finish_variance=None, fixed_cost=None, fixed_cost_accrual=None, free_slack=None, guid=None, hide_bar=None, ignore_resource_calendar=None, late_finish=None, late_start=None, is_level_assignments=True, can_leveling_split=True, leveling_delay=None, is_marked=None, is_milestone=None, is_critical=None, is_subproject=None, is_subproject_read_only=None, subproject_name=None, is_summary=None, subtasks_uids=None, outline_level=None, is_over_allocated=None, is_estimated=None, overtime_cost=None, overtime_work=None, physical_percent_complete=None, pre_leveled_finish=None, pre_leveled_start=None, is_recurring=None, regular_work=None, remaining_cost=None, remaining_duration=None, remaining_overtime_cost=None, remaining_overtime_work=None, remaining_work=None, resume=None, is_resume_valid=None, stop=None, is_rollup=None, start_slack=None, start_variance=None, calendar_uid=-1, is_manual=None, manual_start=None, manual_finish=None, manual_duration=None, total_slack=None, type=None, wbs=None, priority=None, work=None, work_variance=None, notes_text=None, notes_rtf=None, acwp=None, bcws=None, bcwp=None, leveling_delay_format=None, predecessors=None, successors=None, ignore_warnings=False, is_expanded=None, display_on_timeline=None, display_as_summary=None, hyperlink=None, hyperlink_address=None, hyperlink_sub_address=None, earned_value_method=None, is_published=True, status_manager=None, commitment_start=None, commitment_finish=None, commitment_type=None, baselines=None, extended_attributes=None, outline_codes=None, warning=False):  # noqa: E501
        """Task - a model defined in Swagger"""  # noqa: E501

        self._uid = None
        self._id = None
        self._name = None
        self._duration_text = None
        self._duration = None
        self._start = None
        self._finish = None
        self._start_text = None
        self._finish_text = None
        self._percent_complete = None
        self._percent_work_complete = None
        self._is_active = None
        self._actual_cost = None
        self._actual_duration = None
        self._actual_finish = None
        self._actual_overtime_cost = None
        self._actual_overtime_work = None
        self._actual_work_protected = None
        self._actual_overtime_work_protected = None
        self._actual_start = None
        self._budget_work = None
        self._budget_cost = None
        self._constraint_date = None
        self._constraint_type = None
        self._contact = None
        self._cost = None
        self._cv = None
        self._deadline = None
        self._duration_variance = None
        self._early_finish = None
        self._early_start = None
        self._is_effort_driven = None
        self._is_external_task = None
        self._external_task_project = None
        self._external_id = None
        self._finish_slack = None
        self._finish_variance = None
        self._fixed_cost = None
        self._fixed_cost_accrual = None
        self._free_slack = None
        self._guid = None
        self._hide_bar = None
        self._ignore_resource_calendar = None
        self._late_finish = None
        self._late_start = None
        self._is_level_assignments = None
        self._can_leveling_split = None
        self._leveling_delay = None
        self._is_marked = None
        self._is_milestone = None
        self._is_critical = None
        self._is_subproject = None
        self._is_subproject_read_only = None
        self._subproject_name = None
        self._is_summary = None
        self._subtasks_uids = None
        self._outline_level = None
        self._is_over_allocated = None
        self._is_estimated = None
        self._overtime_cost = None
        self._overtime_work = None
        self._physical_percent_complete = None
        self._pre_leveled_finish = None
        self._pre_leveled_start = None
        self._is_recurring = None
        self._regular_work = None
        self._remaining_cost = None
        self._remaining_duration = None
        self._remaining_overtime_cost = None
        self._remaining_overtime_work = None
        self._remaining_work = None
        self._resume = None
        self._is_resume_valid = None
        self._stop = None
        self._is_rollup = None
        self._start_slack = None
        self._start_variance = None
        self._calendar_uid = None
        self._is_manual = None
        self._manual_start = None
        self._manual_finish = None
        self._manual_duration = None
        self._total_slack = None
        self._type = None
        self._wbs = None
        self._priority = None
        self._work = None
        self._work_variance = None
        self._notes_text = None
        self._notes_rtf = None
        self._acwp = None
        self._bcws = None
        self._bcwp = None
        self._leveling_delay_format = None
        self._predecessors = None
        self._successors = None
        self._ignore_warnings = None
        self._is_expanded = None
        self._display_on_timeline = None
        self._display_as_summary = None
        self._hyperlink = None
        self._hyperlink_address = None
        self._hyperlink_sub_address = None
        self._earned_value_method = None
        self._is_published = None
        self._status_manager = None
        self._commitment_start = None
        self._commitment_finish = None
        self._commitment_type = None
        self._baselines = None
        self._extended_attributes = None
        self._outline_codes = None
        self._warning = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if duration_text is not None:
            self.duration_text = duration_text
        if duration is not None:
            self.duration = duration
        if start is not None:
            self.start = start
        if finish is not None:
            self.finish = finish
        if start_text is not None:
            self.start_text = start_text
        if finish_text is not None:
            self.finish_text = finish_text
        if percent_complete is not None:
            self.percent_complete = percent_complete
        if percent_work_complete is not None:
            self.percent_work_complete = percent_work_complete
        if is_active is not None:
            self.is_active = is_active
        if actual_cost is not None:
            self.actual_cost = actual_cost
        if actual_duration is not None:
            self.actual_duration = actual_duration
        if actual_finish is not None:
            self.actual_finish = actual_finish
        if actual_overtime_cost is not None:
            self.actual_overtime_cost = actual_overtime_cost
        if actual_overtime_work is not None:
            self.actual_overtime_work = actual_overtime_work
        if actual_work_protected is not None:
            self.actual_work_protected = actual_work_protected
        if actual_overtime_work_protected is not None:
            self.actual_overtime_work_protected = actual_overtime_work_protected
        if actual_start is not None:
            self.actual_start = actual_start
        if budget_work is not None:
            self.budget_work = budget_work
        if budget_cost is not None:
            self.budget_cost = budget_cost
        if constraint_date is not None:
            self.constraint_date = constraint_date
        if constraint_type is not None:
            self.constraint_type = constraint_type
        if contact is not None:
            self.contact = contact
        if cost is not None:
            self.cost = cost
        if cv is not None:
            self.cv = cv
        if deadline is not None:
            self.deadline = deadline
        if duration_variance is not None:
            self.duration_variance = duration_variance
        if early_finish is not None:
            self.early_finish = early_finish
        if early_start is not None:
            self.early_start = early_start
        if is_effort_driven is not None:
            self.is_effort_driven = is_effort_driven
        if is_external_task is not None:
            self.is_external_task = is_external_task
        if external_task_project is not None:
            self.external_task_project = external_task_project
        if external_id is not None:
            self.external_id = external_id
        if finish_slack is not None:
            self.finish_slack = finish_slack
        if finish_variance is not None:
            self.finish_variance = finish_variance
        if fixed_cost is not None:
            self.fixed_cost = fixed_cost
        if fixed_cost_accrual is not None:
            self.fixed_cost_accrual = fixed_cost_accrual
        if free_slack is not None:
            self.free_slack = free_slack
        if guid is not None:
            self.guid = guid
        if hide_bar is not None:
            self.hide_bar = hide_bar
        if ignore_resource_calendar is not None:
            self.ignore_resource_calendar = ignore_resource_calendar
        if late_finish is not None:
            self.late_finish = late_finish
        if late_start is not None:
            self.late_start = late_start
        if is_level_assignments is not None:
            self.is_level_assignments = is_level_assignments
        if can_leveling_split is not None:
            self.can_leveling_split = can_leveling_split
        if leveling_delay is not None:
            self.leveling_delay = leveling_delay
        if is_marked is not None:
            self.is_marked = is_marked
        if is_milestone is not None:
            self.is_milestone = is_milestone
        if is_critical is not None:
            self.is_critical = is_critical
        if is_subproject is not None:
            self.is_subproject = is_subproject
        if is_subproject_read_only is not None:
            self.is_subproject_read_only = is_subproject_read_only
        if subproject_name is not None:
            self.subproject_name = subproject_name
        if is_summary is not None:
            self.is_summary = is_summary
        if subtasks_uids is not None:
            self.subtasks_uids = subtasks_uids
        if outline_level is not None:
            self.outline_level = outline_level
        if is_over_allocated is not None:
            self.is_over_allocated = is_over_allocated
        if is_estimated is not None:
            self.is_estimated = is_estimated
        if overtime_cost is not None:
            self.overtime_cost = overtime_cost
        if overtime_work is not None:
            self.overtime_work = overtime_work
        if physical_percent_complete is not None:
            self.physical_percent_complete = physical_percent_complete
        if pre_leveled_finish is not None:
            self.pre_leveled_finish = pre_leveled_finish
        if pre_leveled_start is not None:
            self.pre_leveled_start = pre_leveled_start
        if is_recurring is not None:
            self.is_recurring = is_recurring
        if regular_work is not None:
            self.regular_work = regular_work
        if remaining_cost is not None:
            self.remaining_cost = remaining_cost
        if remaining_duration is not None:
            self.remaining_duration = remaining_duration
        if remaining_overtime_cost is not None:
            self.remaining_overtime_cost = remaining_overtime_cost
        if remaining_overtime_work is not None:
            self.remaining_overtime_work = remaining_overtime_work
        if remaining_work is not None:
            self.remaining_work = remaining_work
        if resume is not None:
            self.resume = resume
        if is_resume_valid is not None:
            self.is_resume_valid = is_resume_valid
        if stop is not None:
            self.stop = stop
        if is_rollup is not None:
            self.is_rollup = is_rollup
        if start_slack is not None:
            self.start_slack = start_slack
        if start_variance is not None:
            self.start_variance = start_variance
        if calendar_uid is not None:
            self.calendar_uid = calendar_uid
        if is_manual is not None:
            self.is_manual = is_manual
        if manual_start is not None:
            self.manual_start = manual_start
        if manual_finish is not None:
            self.manual_finish = manual_finish
        if manual_duration is not None:
            self.manual_duration = manual_duration
        if total_slack is not None:
            self.total_slack = total_slack
        if type is not None:
            self.type = type
        if wbs is not None:
            self.wbs = wbs
        if priority is not None:
            self.priority = priority
        if work is not None:
            self.work = work
        if work_variance is not None:
            self.work_variance = work_variance
        if notes_text is not None:
            self.notes_text = notes_text
        if notes_rtf is not None:
            self.notes_rtf = notes_rtf
        if acwp is not None:
            self.acwp = acwp
        if bcws is not None:
            self.bcws = bcws
        if bcwp is not None:
            self.bcwp = bcwp
        if leveling_delay_format is not None:
            self.leveling_delay_format = leveling_delay_format
        if predecessors is not None:
            self.predecessors = predecessors
        if successors is not None:
            self.successors = successors
        if ignore_warnings is not None:
            self.ignore_warnings = ignore_warnings
        if is_expanded is not None:
            self.is_expanded = is_expanded
        if display_on_timeline is not None:
            self.display_on_timeline = display_on_timeline
        if display_as_summary is not None:
            self.display_as_summary = display_as_summary
        if hyperlink is not None:
            self.hyperlink = hyperlink
        if hyperlink_address is not None:
            self.hyperlink_address = hyperlink_address
        if hyperlink_sub_address is not None:
            self.hyperlink_sub_address = hyperlink_sub_address
        if earned_value_method is not None:
            self.earned_value_method = earned_value_method
        if is_published is not None:
            self.is_published = is_published
        if status_manager is not None:
            self.status_manager = status_manager
        if commitment_start is not None:
            self.commitment_start = commitment_start
        if commitment_finish is not None:
            self.commitment_finish = commitment_finish
        if commitment_type is not None:
            self.commitment_type = commitment_type
        if baselines is not None:
            self.baselines = baselines
        if extended_attributes is not None:
            self.extended_attributes = extended_attributes
        if outline_codes is not None:
            self.outline_codes = outline_codes
        if warning is not None:
            self.warning = warning

    @property
    def uid(self):
        """Gets the uid of this Task.  # noqa: E501

        The unique id of a task.  # noqa: E501

        :return: The uid of this Task.  # noqa: E501
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this Task.

        The unique id of a task.  # noqa: E501

        :param uid: The uid of this Task.  # noqa: E501
        :type: int
        """
        if uid is None:
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501
        self._uid = uid
    @property
    def id(self):
        """Gets the id of this Task.  # noqa: E501

        The position of a task in collection.  # noqa: E501

        :return: The id of this Task.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Task.

        The position of a task in collection.  # noqa: E501

        :param id: The id of this Task.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        self._id = id
    @property
    def name(self):
        """Gets the name of this Task.  # noqa: E501

        The name of a task.  # noqa: E501

        :return: The name of this Task.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Task.

        The name of a task.  # noqa: E501

        :param name: The name of this Task.  # noqa: E501
        :type: str
        """
        self._name = name
    @property
    def duration_text(self):
        """Gets the duration_text of this Task.  # noqa: E501

        The duration of a task entered by the user as a text.  # noqa: E501

        :return: The duration_text of this Task.  # noqa: E501
        :rtype: str
        """
        return self._duration_text

    @duration_text.setter
    def duration_text(self, duration_text):
        """Sets the duration_text of this Task.

        The duration of a task entered by the user as a text.  # noqa: E501

        :param duration_text: The duration_text of this Task.  # noqa: E501
        :type: str
        """
        self._duration_text = duration_text
    @property
    def duration(self):
        """Gets the duration of this Task.  # noqa: E501

        The duration of a task.  # noqa: E501

        :return: The duration of this Task.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Task.

        The duration of a task.  # noqa: E501

        :param duration: The duration of this Task.  # noqa: E501
        :type: str
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501
        self._duration = duration
    @property
    def start(self):
        """Gets the start of this Task.  # noqa: E501

        The start date of a task.  # noqa: E501

        :return: The start of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this Task.

        The start date of a task.  # noqa: E501

        :param start: The start of this Task.  # noqa: E501
        :type: datetime
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501
        self._start = start
    @property
    def finish(self):
        """Gets the finish of this Task.  # noqa: E501

        The finish date of a task.  # noqa: E501

        :return: The finish of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._finish

    @finish.setter
    def finish(self, finish):
        """Sets the finish of this Task.

        The finish date of a task.  # noqa: E501

        :param finish: The finish of this Task.  # noqa: E501
        :type: datetime
        """
        if finish is None:
            raise ValueError("Invalid value for `finish`, must not be `None`")  # noqa: E501
        self._finish = finish
    @property
    def start_text(self):
        """Gets the start_text of this Task.  # noqa: E501

        Returns the task's start text.  # noqa: E501

        :return: The start_text of this Task.  # noqa: E501
        :rtype: str
        """
        return self._start_text

    @start_text.setter
    def start_text(self, start_text):
        """Sets the start_text of this Task.

        Returns the task's start text.  # noqa: E501

        :param start_text: The start_text of this Task.  # noqa: E501
        :type: str
        """
        self._start_text = start_text
    @property
    def finish_text(self):
        """Gets the finish_text of this Task.  # noqa: E501

        Returns the task's finish text.  # noqa: E501

        :return: The finish_text of this Task.  # noqa: E501
        :rtype: str
        """
        return self._finish_text

    @finish_text.setter
    def finish_text(self, finish_text):
        """Sets the finish_text of this Task.

        Returns the task's finish text.  # noqa: E501

        :param finish_text: The finish_text of this Task.  # noqa: E501
        :type: str
        """
        self._finish_text = finish_text
    @property
    def percent_complete(self):
        """Gets the percent_complete of this Task.  # noqa: E501

        The percent complete of a task.  # noqa: E501

        :return: The percent_complete of this Task.  # noqa: E501
        :rtype: int
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """Sets the percent_complete of this Task.

        The percent complete of a task.  # noqa: E501

        :param percent_complete: The percent_complete of this Task.  # noqa: E501
        :type: int
        """
        if percent_complete is None:
            raise ValueError("Invalid value for `percent_complete`, must not be `None`")  # noqa: E501
        self._percent_complete = percent_complete
    @property
    def percent_work_complete(self):
        """Gets the percent_work_complete of this Task.  # noqa: E501

        The percent work complete of a task.  # noqa: E501

        :return: The percent_work_complete of this Task.  # noqa: E501
        :rtype: int
        """
        return self._percent_work_complete

    @percent_work_complete.setter
    def percent_work_complete(self, percent_work_complete):
        """Sets the percent_work_complete of this Task.

        The percent work complete of a task.  # noqa: E501

        :param percent_work_complete: The percent_work_complete of this Task.  # noqa: E501
        :type: int
        """
        if percent_work_complete is None:
            raise ValueError("Invalid value for `percent_work_complete`, must not be `None`")  # noqa: E501
        self._percent_work_complete = percent_work_complete
    @property
    def is_active(self):
        """Gets the is_active of this Task.  # noqa: E501

        Determines if a task is active.  # noqa: E501

        :return: The is_active of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this Task.

        Determines if a task is active.  # noqa: E501

        :param is_active: The is_active of this Task.  # noqa: E501
        :type: bool
        """
        if is_active is None:
            raise ValueError("Invalid value for `is_active`, must not be `None`")  # noqa: E501
        self._is_active = is_active
    @property
    def actual_cost(self):
        """Gets the actual_cost of this Task.  # noqa: E501

        The actual cost of a task.  # noqa: E501

        :return: The actual_cost of this Task.  # noqa: E501
        :rtype: float
        """
        return self._actual_cost

    @actual_cost.setter
    def actual_cost(self, actual_cost):
        """Sets the actual_cost of this Task.

        The actual cost of a task.  # noqa: E501

        :param actual_cost: The actual_cost of this Task.  # noqa: E501
        :type: float
        """
        if actual_cost is None:
            raise ValueError("Invalid value for `actual_cost`, must not be `None`")  # noqa: E501
        self._actual_cost = actual_cost
    @property
    def actual_duration(self):
        """Gets the actual_duration of this Task.  # noqa: E501

        The actual duration of a task.  # noqa: E501

        :return: The actual_duration of this Task.  # noqa: E501
        :rtype: str
        """
        return self._actual_duration

    @actual_duration.setter
    def actual_duration(self, actual_duration):
        """Sets the actual_duration of this Task.

        The actual duration of a task.  # noqa: E501

        :param actual_duration: The actual_duration of this Task.  # noqa: E501
        :type: str
        """
        if actual_duration is None:
            raise ValueError("Invalid value for `actual_duration`, must not be `None`")  # noqa: E501
        self._actual_duration = actual_duration
    @property
    def actual_finish(self):
        """Gets the actual_finish of this Task.  # noqa: E501

        The actual finish date of a task.  # noqa: E501

        :return: The actual_finish of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._actual_finish

    @actual_finish.setter
    def actual_finish(self, actual_finish):
        """Sets the actual_finish of this Task.

        The actual finish date of a task.  # noqa: E501

        :param actual_finish: The actual_finish of this Task.  # noqa: E501
        :type: datetime
        """
        if actual_finish is None:
            raise ValueError("Invalid value for `actual_finish`, must not be `None`")  # noqa: E501
        self._actual_finish = actual_finish
    @property
    def actual_overtime_cost(self):
        """Gets the actual_overtime_cost of this Task.  # noqa: E501

        The actual overtime cost of a task.  # noqa: E501

        :return: The actual_overtime_cost of this Task.  # noqa: E501
        :rtype: float
        """
        return self._actual_overtime_cost

    @actual_overtime_cost.setter
    def actual_overtime_cost(self, actual_overtime_cost):
        """Sets the actual_overtime_cost of this Task.

        The actual overtime cost of a task.  # noqa: E501

        :param actual_overtime_cost: The actual_overtime_cost of this Task.  # noqa: E501
        :type: float
        """
        if actual_overtime_cost is None:
            raise ValueError("Invalid value for `actual_overtime_cost`, must not be `None`")  # noqa: E501
        self._actual_overtime_cost = actual_overtime_cost
    @property
    def actual_overtime_work(self):
        """Gets the actual_overtime_work of this Task.  # noqa: E501

        The actual overtime work of a task.  # noqa: E501

        :return: The actual_overtime_work of this Task.  # noqa: E501
        :rtype: str
        """
        return self._actual_overtime_work

    @actual_overtime_work.setter
    def actual_overtime_work(self, actual_overtime_work):
        """Sets the actual_overtime_work of this Task.

        The actual overtime work of a task.  # noqa: E501

        :param actual_overtime_work: The actual_overtime_work of this Task.  # noqa: E501
        :type: str
        """
        if actual_overtime_work is None:
            raise ValueError("Invalid value for `actual_overtime_work`, must not be `None`")  # noqa: E501
        self._actual_overtime_work = actual_overtime_work
    @property
    def actual_work_protected(self):
        """Gets the actual_work_protected of this Task.  # noqa: E501

        The duration through which actual work is protected. Reading supported for XML format only.  # noqa: E501

        :return: The actual_work_protected of this Task.  # noqa: E501
        :rtype: str
        """
        return self._actual_work_protected

    @actual_work_protected.setter
    def actual_work_protected(self, actual_work_protected):
        """Sets the actual_work_protected of this Task.

        The duration through which actual work is protected. Reading supported for XML format only.  # noqa: E501

        :param actual_work_protected: The actual_work_protected of this Task.  # noqa: E501
        :type: str
        """
        if actual_work_protected is None:
            raise ValueError("Invalid value for `actual_work_protected`, must not be `None`")  # noqa: E501
        self._actual_work_protected = actual_work_protected
    @property
    def actual_overtime_work_protected(self):
        """Gets the actual_overtime_work_protected of this Task.  # noqa: E501

        The duration through which actual overtime work is protected. Reading supported for XML format only.  # noqa: E501

        :return: The actual_overtime_work_protected of this Task.  # noqa: E501
        :rtype: str
        """
        return self._actual_overtime_work_protected

    @actual_overtime_work_protected.setter
    def actual_overtime_work_protected(self, actual_overtime_work_protected):
        """Sets the actual_overtime_work_protected of this Task.

        The duration through which actual overtime work is protected. Reading supported for XML format only.  # noqa: E501

        :param actual_overtime_work_protected: The actual_overtime_work_protected of this Task.  # noqa: E501
        :type: str
        """
        if actual_overtime_work_protected is None:
            raise ValueError("Invalid value for `actual_overtime_work_protected`, must not be `None`")  # noqa: E501
        self._actual_overtime_work_protected = actual_overtime_work_protected
    @property
    def actual_start(self):
        """Gets the actual_start of this Task.  # noqa: E501

        The actual start date of a task.  # noqa: E501

        :return: The actual_start of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._actual_start

    @actual_start.setter
    def actual_start(self, actual_start):
        """Sets the actual_start of this Task.

        The actual start date of a task.  # noqa: E501

        :param actual_start: The actual_start of this Task.  # noqa: E501
        :type: datetime
        """
        if actual_start is None:
            raise ValueError("Invalid value for `actual_start`, must not be `None`")  # noqa: E501
        self._actual_start = actual_start
    @property
    def budget_work(self):
        """Gets the budget_work of this Task.  # noqa: E501

        The amount of budgeted work for a project root task.  # noqa: E501

        :return: The budget_work of this Task.  # noqa: E501
        :rtype: str
        """
        return self._budget_work

    @budget_work.setter
    def budget_work(self, budget_work):
        """Sets the budget_work of this Task.

        The amount of budgeted work for a project root task.  # noqa: E501

        :param budget_work: The budget_work of this Task.  # noqa: E501
        :type: str
        """
        if budget_work is None:
            raise ValueError("Invalid value for `budget_work`, must not be `None`")  # noqa: E501
        self._budget_work = budget_work
    @property
    def budget_cost(self):
        """Gets the budget_cost of this Task.  # noqa: E501

        The amount of budgeted cost for a project root task.  # noqa: E501

        :return: The budget_cost of this Task.  # noqa: E501
        :rtype: float
        """
        return self._budget_cost

    @budget_cost.setter
    def budget_cost(self, budget_cost):
        """Sets the budget_cost of this Task.

        The amount of budgeted cost for a project root task.  # noqa: E501

        :param budget_cost: The budget_cost of this Task.  # noqa: E501
        :type: float
        """
        if budget_cost is None:
            raise ValueError("Invalid value for `budget_cost`, must not be `None`")  # noqa: E501
        self._budget_cost = budget_cost
    @property
    def constraint_date(self):
        """Gets the constraint_date of this Task.  # noqa: E501

        Shows the specific date associated with certain constraint types,  such as Must Start On, Must Finish On, Start No Earlier Than, Start No Later Than, Finish No Earlier Than, and Finish No Later Than.  # noqa: E501

        :return: The constraint_date of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._constraint_date

    @constraint_date.setter
    def constraint_date(self, constraint_date):
        """Sets the constraint_date of this Task.

        Shows the specific date associated with certain constraint types,  such as Must Start On, Must Finish On, Start No Earlier Than, Start No Later Than, Finish No Earlier Than, and Finish No Later Than.  # noqa: E501

        :param constraint_date: The constraint_date of this Task.  # noqa: E501
        :type: datetime
        """
        if constraint_date is None:
            raise ValueError("Invalid value for `constraint_date`, must not be `None`")  # noqa: E501
        self._constraint_date = constraint_date
    @property
    def constraint_type(self):
        """Gets the constraint_type of this Task.  # noqa: E501

        Provides choices for the type of constraint that can be applied for scheduling a task.  # noqa: E501

        :return: The constraint_type of this Task.  # noqa: E501
        :rtype: ConstraintType
        """
        return self._constraint_type

    @constraint_type.setter
    def constraint_type(self, constraint_type):
        """Sets the constraint_type of this Task.

        Provides choices for the type of constraint that can be applied for scheduling a task.  # noqa: E501

        :param constraint_type: The constraint_type of this Task.  # noqa: E501
        :type: ConstraintType
        """
        if constraint_type is None:
            raise ValueError("Invalid value for `constraint_type`, must not be `None`")  # noqa: E501
        self._constraint_type = constraint_type
    @property
    def contact(self):
        """Gets the contact of this Task.  # noqa: E501

        The contact person for a task.  # noqa: E501

        :return: The contact of this Task.  # noqa: E501
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this Task.

        The contact person for a task.  # noqa: E501

        :param contact: The contact of this Task.  # noqa: E501
        :type: str
        """
        self._contact = contact
    @property
    def cost(self):
        """Gets the cost of this Task.  # noqa: E501

        The projected or scheduled cost of a task.  # noqa: E501

        :return: The cost of this Task.  # noqa: E501
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this Task.

        The projected or scheduled cost of a task.  # noqa: E501

        :param cost: The cost of this Task.  # noqa: E501
        :type: float
        """
        if cost is None:
            raise ValueError("Invalid value for `cost`, must not be `None`")  # noqa: E501
        self._cost = cost
    @property
    def cv(self):
        """Gets the cv of this Task.  # noqa: E501

        The difference between the baseline cost and total cost for a task.  # noqa: E501

        :return: The cv of this Task.  # noqa: E501
        :rtype: float
        """
        return self._cv

    @cv.setter
    def cv(self, cv):
        """Sets the cv of this Task.

        The difference between the baseline cost and total cost for a task.  # noqa: E501

        :param cv: The cv of this Task.  # noqa: E501
        :type: float
        """
        if cv is None:
            raise ValueError("Invalid value for `cv`, must not be `None`")  # noqa: E501
        self._cv = cv
    @property
    def deadline(self):
        """Gets the deadline of this Task.  # noqa: E501

        The deadline for a task to be completed.  # noqa: E501

        :return: The deadline of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        """Sets the deadline of this Task.

        The deadline for a task to be completed.  # noqa: E501

        :param deadline: The deadline of this Task.  # noqa: E501
        :type: datetime
        """
        if deadline is None:
            raise ValueError("Invalid value for `deadline`, must not be `None`")  # noqa: E501
        self._deadline = deadline
    @property
    def duration_variance(self):
        """Gets the duration_variance of this Task.  # noqa: E501

        Contains the difference between the total duration of a task and the baseline duration of a task.  # noqa: E501

        :return: The duration_variance of this Task.  # noqa: E501
        :rtype: str
        """
        return self._duration_variance

    @duration_variance.setter
    def duration_variance(self, duration_variance):
        """Sets the duration_variance of this Task.

        Contains the difference between the total duration of a task and the baseline duration of a task.  # noqa: E501

        :param duration_variance: The duration_variance of this Task.  # noqa: E501
        :type: str
        """
        if duration_variance is None:
            raise ValueError("Invalid value for `duration_variance`, must not be `None`")  # noqa: E501
        self._duration_variance = duration_variance
    @property
    def early_finish(self):
        """Gets the early_finish of this Task.  # noqa: E501

        The early finish date of a task.  # noqa: E501

        :return: The early_finish of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._early_finish

    @early_finish.setter
    def early_finish(self, early_finish):
        """Sets the early_finish of this Task.

        The early finish date of a task.  # noqa: E501

        :param early_finish: The early_finish of this Task.  # noqa: E501
        :type: datetime
        """
        if early_finish is None:
            raise ValueError("Invalid value for `early_finish`, must not be `None`")  # noqa: E501
        self._early_finish = early_finish
    @property
    def early_start(self):
        """Gets the early_start of this Task.  # noqa: E501

        The early start date of a task.  # noqa: E501

        :return: The early_start of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._early_start

    @early_start.setter
    def early_start(self, early_start):
        """Sets the early_start of this Task.

        The early start date of a task.  # noqa: E501

        :param early_start: The early_start of this Task.  # noqa: E501
        :type: datetime
        """
        if early_start is None:
            raise ValueError("Invalid value for `early_start`, must not be `None`")  # noqa: E501
        self._early_start = early_start
    @property
    def is_effort_driven(self):
        """Gets the is_effort_driven of this Task.  # noqa: E501

        Determines whether a task is effort-driven.  # noqa: E501

        :return: The is_effort_driven of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._is_effort_driven

    @is_effort_driven.setter
    def is_effort_driven(self, is_effort_driven):
        """Sets the is_effort_driven of this Task.

        Determines whether a task is effort-driven.  # noqa: E501

        :param is_effort_driven: The is_effort_driven of this Task.  # noqa: E501
        :type: bool
        """
        if is_effort_driven is None:
            raise ValueError("Invalid value for `is_effort_driven`, must not be `None`")  # noqa: E501
        self._is_effort_driven = is_effort_driven
    @property
    def is_external_task(self):
        """Gets the is_external_task of this Task.  # noqa: E501

        Determines whether a task is external.  # noqa: E501

        :return: The is_external_task of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._is_external_task

    @is_external_task.setter
    def is_external_task(self, is_external_task):
        """Sets the is_external_task of this Task.

        Determines whether a task is external.  # noqa: E501

        :param is_external_task: The is_external_task of this Task.  # noqa: E501
        :type: bool
        """
        if is_external_task is None:
            raise ValueError("Invalid value for `is_external_task`, must not be `None`")  # noqa: E501
        self._is_external_task = is_external_task
    @property
    def external_task_project(self):
        """Gets the external_task_project of this Task.  # noqa: E501

        The source location and task identifier of an external task.  # noqa: E501

        :return: The external_task_project of this Task.  # noqa: E501
        :rtype: str
        """
        return self._external_task_project

    @external_task_project.setter
    def external_task_project(self, external_task_project):
        """Sets the external_task_project of this Task.

        The source location and task identifier of an external task.  # noqa: E501

        :param external_task_project: The external_task_project of this Task.  # noqa: E501
        :type: str
        """
        self._external_task_project = external_task_project
    @property
    def external_id(self):
        """Gets the external_id of this Task.  # noqa: E501

        If a task is an external task the property contains the task's external Id.  type.  # noqa: E501

        :return: The external_id of this Task.  # noqa: E501
        :rtype: int
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Task.

        If a task is an external task the property contains the task's external Id.  type.  # noqa: E501

        :param external_id: The external_id of this Task.  # noqa: E501
        :type: int
        """
        if external_id is None:
            raise ValueError("Invalid value for `external_id`, must not be `None`")  # noqa: E501
        self._external_id = external_id
    @property
    def finish_slack(self):
        """Gets the finish_slack of this Task.  # noqa: E501

        Contains the duration between the Early Finish and Late Finish dates.  # noqa: E501

        :return: The finish_slack of this Task.  # noqa: E501
        :rtype: int
        """
        return self._finish_slack

    @finish_slack.setter
    def finish_slack(self, finish_slack):
        """Sets the finish_slack of this Task.

        Contains the duration between the Early Finish and Late Finish dates.  # noqa: E501

        :param finish_slack: The finish_slack of this Task.  # noqa: E501
        :type: int
        """
        if finish_slack is None:
            raise ValueError("Invalid value for `finish_slack`, must not be `None`")  # noqa: E501
        self._finish_slack = finish_slack
    @property
    def finish_variance(self):
        """Gets the finish_variance of this Task.  # noqa: E501

        The variance of the task finish date from the baseline finish date as minutes.  # noqa: E501

        :return: The finish_variance of this Task.  # noqa: E501
        :rtype: int
        """
        return self._finish_variance

    @finish_variance.setter
    def finish_variance(self, finish_variance):
        """Sets the finish_variance of this Task.

        The variance of the task finish date from the baseline finish date as minutes.  # noqa: E501

        :param finish_variance: The finish_variance of this Task.  # noqa: E501
        :type: int
        """
        if finish_variance is None:
            raise ValueError("Invalid value for `finish_variance`, must not be `None`")  # noqa: E501
        self._finish_variance = finish_variance
    @property
    def fixed_cost(self):
        """Gets the fixed_cost of this Task.  # noqa: E501

        The fixed cost of a task.  # noqa: E501

        :return: The fixed_cost of this Task.  # noqa: E501
        :rtype: float
        """
        return self._fixed_cost

    @fixed_cost.setter
    def fixed_cost(self, fixed_cost):
        """Sets the fixed_cost of this Task.

        The fixed cost of a task.  # noqa: E501

        :param fixed_cost: The fixed_cost of this Task.  # noqa: E501
        :type: float
        """
        if fixed_cost is None:
            raise ValueError("Invalid value for `fixed_cost`, must not be `None`")  # noqa: E501
        self._fixed_cost = fixed_cost
    @property
    def fixed_cost_accrual(self):
        """Gets the fixed_cost_accrual of this Task.  # noqa: E501

        Determines how the fixed cost is accrued against a task.  # noqa: E501

        :return: The fixed_cost_accrual of this Task.  # noqa: E501
        :rtype: CostAccrualType
        """
        return self._fixed_cost_accrual

    @fixed_cost_accrual.setter
    def fixed_cost_accrual(self, fixed_cost_accrual):
        """Sets the fixed_cost_accrual of this Task.

        Determines how the fixed cost is accrued against a task.  # noqa: E501

        :param fixed_cost_accrual: The fixed_cost_accrual of this Task.  # noqa: E501
        :type: CostAccrualType
        """
        if fixed_cost_accrual is None:
            raise ValueError("Invalid value for `fixed_cost_accrual`, must not be `None`")  # noqa: E501
        self._fixed_cost_accrual = fixed_cost_accrual
    @property
    def free_slack(self):
        """Gets the free_slack of this Task.  # noqa: E501

        The amount of a free slack.  # noqa: E501

        :return: The free_slack of this Task.  # noqa: E501
        :rtype: int
        """
        return self._free_slack

    @free_slack.setter
    def free_slack(self, free_slack):
        """Sets the free_slack of this Task.

        The amount of a free slack.  # noqa: E501

        :param free_slack: The free_slack of this Task.  # noqa: E501
        :type: int
        """
        if free_slack is None:
            raise ValueError("Invalid value for `free_slack`, must not be `None`")  # noqa: E501
        self._free_slack = free_slack
    @property
    def guid(self):
        """Gets the guid of this Task.  # noqa: E501


        :return: The guid of this Task.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this Task.


        :param guid: The guid of this Task.  # noqa: E501
        :type: str
        """
        self._guid = guid
    @property
    def hide_bar(self):
        """Gets the hide_bar of this Task.  # noqa: E501

        Determines whether the GANTT bar of a task is hidden when displayed in Microsoft Project.  # noqa: E501

        :return: The hide_bar of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._hide_bar

    @hide_bar.setter
    def hide_bar(self, hide_bar):
        """Sets the hide_bar of this Task.

        Determines whether the GANTT bar of a task is hidden when displayed in Microsoft Project.  # noqa: E501

        :param hide_bar: The hide_bar of this Task.  # noqa: E501
        :type: bool
        """
        if hide_bar is None:
            raise ValueError("Invalid value for `hide_bar`, must not be `None`")  # noqa: E501
        self._hide_bar = hide_bar
    @property
    def ignore_resource_calendar(self):
        """Gets the ignore_resource_calendar of this Task.  # noqa: E501

        Determines whether a task ignores the resource calendar.  # noqa: E501

        :return: The ignore_resource_calendar of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_resource_calendar

    @ignore_resource_calendar.setter
    def ignore_resource_calendar(self, ignore_resource_calendar):
        """Sets the ignore_resource_calendar of this Task.

        Determines whether a task ignores the resource calendar.  # noqa: E501

        :param ignore_resource_calendar: The ignore_resource_calendar of this Task.  # noqa: E501
        :type: bool
        """
        if ignore_resource_calendar is None:
            raise ValueError("Invalid value for `ignore_resource_calendar`, must not be `None`")  # noqa: E501
        self._ignore_resource_calendar = ignore_resource_calendar
    @property
    def late_finish(self):
        """Gets the late_finish of this Task.  # noqa: E501

        The late finish date of a task.  # noqa: E501

        :return: The late_finish of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._late_finish

    @late_finish.setter
    def late_finish(self, late_finish):
        """Sets the late_finish of this Task.

        The late finish date of a task.  # noqa: E501

        :param late_finish: The late_finish of this Task.  # noqa: E501
        :type: datetime
        """
        if late_finish is None:
            raise ValueError("Invalid value for `late_finish`, must not be `None`")  # noqa: E501
        self._late_finish = late_finish
    @property
    def late_start(self):
        """Gets the late_start of this Task.  # noqa: E501

        The late start date of a task.  # noqa: E501

        :return: The late_start of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._late_start

    @late_start.setter
    def late_start(self, late_start):
        """Sets the late_start of this Task.

        The late start date of a task.  # noqa: E501

        :param late_start: The late_start of this Task.  # noqa: E501
        :type: datetime
        """
        if late_start is None:
            raise ValueError("Invalid value for `late_start`, must not be `None`")  # noqa: E501
        self._late_start = late_start
    @property
    def is_level_assignments(self):
        """Gets the is_level_assignments of this Task.  # noqa: E501


        :return: The is_level_assignments of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._is_level_assignments

    @is_level_assignments.setter
    def is_level_assignments(self, is_level_assignments):
        """Sets the is_level_assignments of this Task.


        :param is_level_assignments: The is_level_assignments of this Task.  # noqa: E501
        :type: bool
        """
        if is_level_assignments is None:
            raise ValueError("Invalid value for `is_level_assignments`, must not be `None`")  # noqa: E501
        self._is_level_assignments = is_level_assignments
    @property
    def can_leveling_split(self):
        """Gets the can_leveling_split of this Task.  # noqa: E501


        :return: The can_leveling_split of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._can_leveling_split

    @can_leveling_split.setter
    def can_leveling_split(self, can_leveling_split):
        """Sets the can_leveling_split of this Task.


        :param can_leveling_split: The can_leveling_split of this Task.  # noqa: E501
        :type: bool
        """
        if can_leveling_split is None:
            raise ValueError("Invalid value for `can_leveling_split`, must not be `None`")  # noqa: E501
        self._can_leveling_split = can_leveling_split
    @property
    def leveling_delay(self):
        """Gets the leveling_delay of this Task.  # noqa: E501

        The delay caused by leveling a task.  # noqa: E501

        :return: The leveling_delay of this Task.  # noqa: E501
        :rtype: int
        """
        return self._leveling_delay

    @leveling_delay.setter
    def leveling_delay(self, leveling_delay):
        """Sets the leveling_delay of this Task.

        The delay caused by leveling a task.  # noqa: E501

        :param leveling_delay: The leveling_delay of this Task.  # noqa: E501
        :type: int
        """
        if leveling_delay is None:
            raise ValueError("Invalid value for `leveling_delay`, must not be `None`")  # noqa: E501
        self._leveling_delay = leveling_delay
    @property
    def is_marked(self):
        """Gets the is_marked of this Task.  # noqa: E501

        Shows whether a task is marked for further action or identification of some kind.               # noqa: E501

        :return: The is_marked of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._is_marked

    @is_marked.setter
    def is_marked(self, is_marked):
        """Sets the is_marked of this Task.

        Shows whether a task is marked for further action or identification of some kind.               # noqa: E501

        :param is_marked: The is_marked of this Task.  # noqa: E501
        :type: bool
        """
        if is_marked is None:
            raise ValueError("Invalid value for `is_marked`, must not be `None`")  # noqa: E501
        self._is_marked = is_marked
    @property
    def is_milestone(self):
        """Gets the is_milestone of this Task.  # noqa: E501

        Determines whether a task is a milestone.  # noqa: E501

        :return: The is_milestone of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._is_milestone

    @is_milestone.setter
    def is_milestone(self, is_milestone):
        """Sets the is_milestone of this Task.

        Determines whether a task is a milestone.  # noqa: E501

        :param is_milestone: The is_milestone of this Task.  # noqa: E501
        :type: bool
        """
        if is_milestone is None:
            raise ValueError("Invalid value for `is_milestone`, must not be `None`")  # noqa: E501
        self._is_milestone = is_milestone
    @property
    def is_critical(self):
        """Gets the is_critical of this Task.  # noqa: E501

        Determines whether a task is in the critical chain.  # noqa: E501

        :return: The is_critical of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._is_critical

    @is_critical.setter
    def is_critical(self, is_critical):
        """Sets the is_critical of this Task.

        Determines whether a task is in the critical chain.  # noqa: E501

        :param is_critical: The is_critical of this Task.  # noqa: E501
        :type: bool
        """
        if is_critical is None:
            raise ValueError("Invalid value for `is_critical`, must not be `None`")  # noqa: E501
        self._is_critical = is_critical
    @property
    def is_subproject(self):
        """Gets the is_subproject of this Task.  # noqa: E501

        Determines whether a task is an inserted project.  # noqa: E501

        :return: The is_subproject of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._is_subproject

    @is_subproject.setter
    def is_subproject(self, is_subproject):
        """Sets the is_subproject of this Task.

        Determines whether a task is an inserted project.  # noqa: E501

        :param is_subproject: The is_subproject of this Task.  # noqa: E501
        :type: bool
        """
        if is_subproject is None:
            raise ValueError("Invalid value for `is_subproject`, must not be `None`")  # noqa: E501
        self._is_subproject = is_subproject
    @property
    def is_subproject_read_only(self):
        """Gets the is_subproject_read_only of this Task.  # noqa: E501

        Determines whether a subproject is read-only.  # noqa: E501

        :return: The is_subproject_read_only of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._is_subproject_read_only

    @is_subproject_read_only.setter
    def is_subproject_read_only(self, is_subproject_read_only):
        """Sets the is_subproject_read_only of this Task.

        Determines whether a subproject is read-only.  # noqa: E501

        :param is_subproject_read_only: The is_subproject_read_only of this Task.  # noqa: E501
        :type: bool
        """
        if is_subproject_read_only is None:
            raise ValueError("Invalid value for `is_subproject_read_only`, must not be `None`")  # noqa: E501
        self._is_subproject_read_only = is_subproject_read_only
    @property
    def subproject_name(self):
        """Gets the subproject_name of this Task.  # noqa: E501

        The source location of a subproject. Read/write String.  # noqa: E501

        :return: The subproject_name of this Task.  # noqa: E501
        :rtype: str
        """
        return self._subproject_name

    @subproject_name.setter
    def subproject_name(self, subproject_name):
        """Sets the subproject_name of this Task.

        The source location of a subproject. Read/write String.  # noqa: E501

        :param subproject_name: The subproject_name of this Task.  # noqa: E501
        :type: str
        """
        self._subproject_name = subproject_name
    @property
    def is_summary(self):
        """Gets the is_summary of this Task.  # noqa: E501

        Determines whether a task is a summary task.  # noqa: E501

        :return: The is_summary of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._is_summary

    @is_summary.setter
    def is_summary(self, is_summary):
        """Sets the is_summary of this Task.

        Determines whether a task is a summary task.  # noqa: E501

        :param is_summary: The is_summary of this Task.  # noqa: E501
        :type: bool
        """
        if is_summary is None:
            raise ValueError("Invalid value for `is_summary`, must not be `None`")  # noqa: E501
        self._is_summary = is_summary
    @property
    def subtasks_uids(self):
        """Gets the subtasks_uids of this Task.  # noqa: E501

        Unique ids of all subtasks.  # noqa: E501

        :return: The subtasks_uids of this Task.  # noqa: E501
        :rtype: list[int]
        """
        return self._subtasks_uids

    @subtasks_uids.setter
    def subtasks_uids(self, subtasks_uids):
        """Sets the subtasks_uids of this Task.

        Unique ids of all subtasks.  # noqa: E501

        :param subtasks_uids: The subtasks_uids of this Task.  # noqa: E501
        :type: list[int]
        """
        self._subtasks_uids = subtasks_uids
    @property
    def outline_level(self):
        """Gets the outline_level of this Task.  # noqa: E501

        The outline level of a task.  # noqa: E501

        :return: The outline_level of this Task.  # noqa: E501
        :rtype: int
        """
        return self._outline_level

    @outline_level.setter
    def outline_level(self, outline_level):
        """Sets the outline_level of this Task.

        The outline level of a task.  # noqa: E501

        :param outline_level: The outline_level of this Task.  # noqa: E501
        :type: int
        """
        if outline_level is None:
            raise ValueError("Invalid value for `outline_level`, must not be `None`")  # noqa: E501
        self._outline_level = outline_level
    @property
    def is_over_allocated(self):
        """Gets the is_over_allocated of this Task.  # noqa: E501


        :return: The is_over_allocated of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._is_over_allocated

    @is_over_allocated.setter
    def is_over_allocated(self, is_over_allocated):
        """Sets the is_over_allocated of this Task.


        :param is_over_allocated: The is_over_allocated of this Task.  # noqa: E501
        :type: bool
        """
        if is_over_allocated is None:
            raise ValueError("Invalid value for `is_over_allocated`, must not be `None`")  # noqa: E501
        self._is_over_allocated = is_over_allocated
    @property
    def is_estimated(self):
        """Gets the is_estimated of this Task.  # noqa: E501

        Determines whether a task is estimated.  # noqa: E501

        :return: The is_estimated of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._is_estimated

    @is_estimated.setter
    def is_estimated(self, is_estimated):
        """Sets the is_estimated of this Task.

        Determines whether a task is estimated.  # noqa: E501

        :param is_estimated: The is_estimated of this Task.  # noqa: E501
        :type: bool
        """
        if is_estimated is None:
            raise ValueError("Invalid value for `is_estimated`, must not be `None`")  # noqa: E501
        self._is_estimated = is_estimated
    @property
    def overtime_cost(self):
        """Gets the overtime_cost of this Task.  # noqa: E501

        The sum of an actual and remaining overtime cost of a task.  # noqa: E501

        :return: The overtime_cost of this Task.  # noqa: E501
        :rtype: float
        """
        return self._overtime_cost

    @overtime_cost.setter
    def overtime_cost(self, overtime_cost):
        """Sets the overtime_cost of this Task.

        The sum of an actual and remaining overtime cost of a task.  # noqa: E501

        :param overtime_cost: The overtime_cost of this Task.  # noqa: E501
        :type: float
        """
        if overtime_cost is None:
            raise ValueError("Invalid value for `overtime_cost`, must not be `None`")  # noqa: E501
        self._overtime_cost = overtime_cost
    @property
    def overtime_work(self):
        """Gets the overtime_work of this Task.  # noqa: E501

        The amount of an overtime work scheduled for a task.  # noqa: E501

        :return: The overtime_work of this Task.  # noqa: E501
        :rtype: str
        """
        return self._overtime_work

    @overtime_work.setter
    def overtime_work(self, overtime_work):
        """Sets the overtime_work of this Task.

        The amount of an overtime work scheduled for a task.  # noqa: E501

        :param overtime_work: The overtime_work of this Task.  # noqa: E501
        :type: str
        """
        if overtime_work is None:
            raise ValueError("Invalid value for `overtime_work`, must not be `None`")  # noqa: E501
        self._overtime_work = overtime_work
    @property
    def physical_percent_complete(self):
        """Gets the physical_percent_complete of this Task.  # noqa: E501

        The percentage complete value entered by the Project Manager.  # noqa: E501

        :return: The physical_percent_complete of this Task.  # noqa: E501
        :rtype: int
        """
        return self._physical_percent_complete

    @physical_percent_complete.setter
    def physical_percent_complete(self, physical_percent_complete):
        """Sets the physical_percent_complete of this Task.

        The percentage complete value entered by the Project Manager.  # noqa: E501

        :param physical_percent_complete: The physical_percent_complete of this Task.  # noqa: E501
        :type: int
        """
        if physical_percent_complete is None:
            raise ValueError("Invalid value for `physical_percent_complete`, must not be `None`")  # noqa: E501
        self._physical_percent_complete = physical_percent_complete
    @property
    def pre_leveled_finish(self):
        """Gets the pre_leveled_finish of this Task.  # noqa: E501


        :return: The pre_leveled_finish of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._pre_leveled_finish

    @pre_leveled_finish.setter
    def pre_leveled_finish(self, pre_leveled_finish):
        """Sets the pre_leveled_finish of this Task.


        :param pre_leveled_finish: The pre_leveled_finish of this Task.  # noqa: E501
        :type: datetime
        """
        if pre_leveled_finish is None:
            raise ValueError("Invalid value for `pre_leveled_finish`, must not be `None`")  # noqa: E501
        self._pre_leveled_finish = pre_leveled_finish
    @property
    def pre_leveled_start(self):
        """Gets the pre_leveled_start of this Task.  # noqa: E501


        :return: The pre_leveled_start of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._pre_leveled_start

    @pre_leveled_start.setter
    def pre_leveled_start(self, pre_leveled_start):
        """Sets the pre_leveled_start of this Task.


        :param pre_leveled_start: The pre_leveled_start of this Task.  # noqa: E501
        :type: datetime
        """
        if pre_leveled_start is None:
            raise ValueError("Invalid value for `pre_leveled_start`, must not be `None`")  # noqa: E501
        self._pre_leveled_start = pre_leveled_start
    @property
    def is_recurring(self):
        """Gets the is_recurring of this Task.  # noqa: E501

        Determines whether a task is a recurring task.  # noqa: E501

        :return: The is_recurring of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._is_recurring

    @is_recurring.setter
    def is_recurring(self, is_recurring):
        """Sets the is_recurring of this Task.

        Determines whether a task is a recurring task.  # noqa: E501

        :param is_recurring: The is_recurring of this Task.  # noqa: E501
        :type: bool
        """
        if is_recurring is None:
            raise ValueError("Invalid value for `is_recurring`, must not be `None`")  # noqa: E501
        self._is_recurring = is_recurring
    @property
    def regular_work(self):
        """Gets the regular_work of this Task.  # noqa: E501

        The amount of non-overtime work scheduled for a task.  # noqa: E501

        :return: The regular_work of this Task.  # noqa: E501
        :rtype: str
        """
        return self._regular_work

    @regular_work.setter
    def regular_work(self, regular_work):
        """Sets the regular_work of this Task.

        The amount of non-overtime work scheduled for a task.  # noqa: E501

        :param regular_work: The regular_work of this Task.  # noqa: E501
        :type: str
        """
        if regular_work is None:
            raise ValueError("Invalid value for `regular_work`, must not be `None`")  # noqa: E501
        self._regular_work = regular_work
    @property
    def remaining_cost(self):
        """Gets the remaining_cost of this Task.  # noqa: E501

        The remaining projected cost of completing a task.  # noqa: E501

        :return: The remaining_cost of this Task.  # noqa: E501
        :rtype: float
        """
        return self._remaining_cost

    @remaining_cost.setter
    def remaining_cost(self, remaining_cost):
        """Sets the remaining_cost of this Task.

        The remaining projected cost of completing a task.  # noqa: E501

        :param remaining_cost: The remaining_cost of this Task.  # noqa: E501
        :type: float
        """
        if remaining_cost is None:
            raise ValueError("Invalid value for `remaining_cost`, must not be `None`")  # noqa: E501
        self._remaining_cost = remaining_cost
    @property
    def remaining_duration(self):
        """Gets the remaining_duration of this Task.  # noqa: E501

        The amount of time required to complete the unfinished portion of a task.  # noqa: E501

        :return: The remaining_duration of this Task.  # noqa: E501
        :rtype: str
        """
        return self._remaining_duration

    @remaining_duration.setter
    def remaining_duration(self, remaining_duration):
        """Sets the remaining_duration of this Task.

        The amount of time required to complete the unfinished portion of a task.  # noqa: E501

        :param remaining_duration: The remaining_duration of this Task.  # noqa: E501
        :type: str
        """
        if remaining_duration is None:
            raise ValueError("Invalid value for `remaining_duration`, must not be `None`")  # noqa: E501
        self._remaining_duration = remaining_duration
    @property
    def remaining_overtime_cost(self):
        """Gets the remaining_overtime_cost of this Task.  # noqa: E501

        The remaining overtime cost projected to finish a task.  # noqa: E501

        :return: The remaining_overtime_cost of this Task.  # noqa: E501
        :rtype: float
        """
        return self._remaining_overtime_cost

    @remaining_overtime_cost.setter
    def remaining_overtime_cost(self, remaining_overtime_cost):
        """Sets the remaining_overtime_cost of this Task.

        The remaining overtime cost projected to finish a task.  # noqa: E501

        :param remaining_overtime_cost: The remaining_overtime_cost of this Task.  # noqa: E501
        :type: float
        """
        if remaining_overtime_cost is None:
            raise ValueError("Invalid value for `remaining_overtime_cost`, must not be `None`")  # noqa: E501
        self._remaining_overtime_cost = remaining_overtime_cost
    @property
    def remaining_overtime_work(self):
        """Gets the remaining_overtime_work of this Task.  # noqa: E501

        The remaining overtime work scheduled to finish a task.  # noqa: E501

        :return: The remaining_overtime_work of this Task.  # noqa: E501
        :rtype: str
        """
        return self._remaining_overtime_work

    @remaining_overtime_work.setter
    def remaining_overtime_work(self, remaining_overtime_work):
        """Sets the remaining_overtime_work of this Task.

        The remaining overtime work scheduled to finish a task.  # noqa: E501

        :param remaining_overtime_work: The remaining_overtime_work of this Task.  # noqa: E501
        :type: str
        """
        if remaining_overtime_work is None:
            raise ValueError("Invalid value for `remaining_overtime_work`, must not be `None`")  # noqa: E501
        self._remaining_overtime_work = remaining_overtime_work
    @property
    def remaining_work(self):
        """Gets the remaining_work of this Task.  # noqa: E501

        The remaining work scheduled to complete a task.  # noqa: E501

        :return: The remaining_work of this Task.  # noqa: E501
        :rtype: str
        """
        return self._remaining_work

    @remaining_work.setter
    def remaining_work(self, remaining_work):
        """Sets the remaining_work of this Task.

        The remaining work scheduled to complete a task.  # noqa: E501

        :param remaining_work: The remaining_work of this Task.  # noqa: E501
        :type: str
        """
        if remaining_work is None:
            raise ValueError("Invalid value for `remaining_work`, must not be `None`")  # noqa: E501
        self._remaining_work = remaining_work
    @property
    def resume(self):
        """Gets the resume of this Task.  # noqa: E501

        The date when a task resumed.  # noqa: E501

        :return: The resume of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._resume

    @resume.setter
    def resume(self, resume):
        """Sets the resume of this Task.

        The date when a task resumed.  # noqa: E501

        :param resume: The resume of this Task.  # noqa: E501
        :type: datetime
        """
        if resume is None:
            raise ValueError("Invalid value for `resume`, must not be `None`")  # noqa: E501
        self._resume = resume
    @property
    def is_resume_valid(self):
        """Gets the is_resume_valid of this Task.  # noqa: E501

        Determines whether a task can be resumed.  # noqa: E501

        :return: The is_resume_valid of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._is_resume_valid

    @is_resume_valid.setter
    def is_resume_valid(self, is_resume_valid):
        """Sets the is_resume_valid of this Task.

        Determines whether a task can be resumed.  # noqa: E501

        :param is_resume_valid: The is_resume_valid of this Task.  # noqa: E501
        :type: bool
        """
        self._is_resume_valid = is_resume_valid
    @property
    def stop(self):
        """Gets the stop of this Task.  # noqa: E501

        The date that represents the end of the actual portion of a task.  # noqa: E501

        :return: The stop of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._stop

    @stop.setter
    def stop(self, stop):
        """Sets the stop of this Task.

        The date that represents the end of the actual portion of a task.  # noqa: E501

        :param stop: The stop of this Task.  # noqa: E501
        :type: datetime
        """
        if stop is None:
            raise ValueError("Invalid value for `stop`, must not be `None`")  # noqa: E501
        self._stop = stop
    @property
    def is_rollup(self):
        """Gets the is_rollup of this Task.  # noqa: E501

        Determines whether a task is rolled up.  # noqa: E501

        :return: The is_rollup of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._is_rollup

    @is_rollup.setter
    def is_rollup(self, is_rollup):
        """Sets the is_rollup of this Task.

        Determines whether a task is rolled up.  # noqa: E501

        :param is_rollup: The is_rollup of this Task.  # noqa: E501
        :type: bool
        """
        if is_rollup is None:
            raise ValueError("Invalid value for `is_rollup`, must not be `None`")  # noqa: E501
        self._is_rollup = is_rollup
    @property
    def start_slack(self):
        """Gets the start_slack of this Task.  # noqa: E501

        Returns the task's start slack.  # noqa: E501

        :return: The start_slack of this Task.  # noqa: E501
        :rtype: int
        """
        return self._start_slack

    @start_slack.setter
    def start_slack(self, start_slack):
        """Sets the start_slack of this Task.

        Returns the task's start slack.  # noqa: E501

        :param start_slack: The start_slack of this Task.  # noqa: E501
        :type: int
        """
        if start_slack is None:
            raise ValueError("Invalid value for `start_slack`, must not be `None`")  # noqa: E501
        self._start_slack = start_slack
    @property
    def start_variance(self):
        """Gets the start_variance of this Task.  # noqa: E501

        The variance of the task start date from the baseline start date as minutes.   # noqa: E501

        :return: The start_variance of this Task.  # noqa: E501
        :rtype: int
        """
        return self._start_variance

    @start_variance.setter
    def start_variance(self, start_variance):
        """Sets the start_variance of this Task.

        The variance of the task start date from the baseline start date as minutes.   # noqa: E501

        :param start_variance: The start_variance of this Task.  # noqa: E501
        :type: int
        """
        if start_variance is None:
            raise ValueError("Invalid value for `start_variance`, must not be `None`")  # noqa: E501
        self._start_variance = start_variance
    @property
    def calendar_uid(self):
        """Gets the calendar_uid of this Task.  # noqa: E501

        The unique id of task calendar.  # noqa: E501

        :return: The calendar_uid of this Task.  # noqa: E501
        :rtype: int
        """
        return self._calendar_uid

    @calendar_uid.setter
    def calendar_uid(self, calendar_uid):
        """Sets the calendar_uid of this Task.

        The unique id of task calendar.  # noqa: E501

        :param calendar_uid: The calendar_uid of this Task.  # noqa: E501
        :type: int
        """
        if calendar_uid is None:
            raise ValueError("Invalid value for `calendar_uid`, must not be `None`")  # noqa: E501
        self._calendar_uid = calendar_uid
    @property
    def is_manual(self):
        """Gets the is_manual of this Task.  # noqa: E501

        Determines whether a task is manually scheduled.  # noqa: E501

        :return: The is_manual of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._is_manual

    @is_manual.setter
    def is_manual(self, is_manual):
        """Sets the is_manual of this Task.

        Determines whether a task is manually scheduled.  # noqa: E501

        :param is_manual: The is_manual of this Task.  # noqa: E501
        :type: bool
        """
        if is_manual is None:
            raise ValueError("Invalid value for `is_manual`, must not be `None`")  # noqa: E501
        self._is_manual = is_manual
    @property
    def manual_start(self):
        """Gets the manual_start of this Task.  # noqa: E501

        Defines manually scheduled start of a task.  # noqa: E501

        :return: The manual_start of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._manual_start

    @manual_start.setter
    def manual_start(self, manual_start):
        """Sets the manual_start of this Task.

        Defines manually scheduled start of a task.  # noqa: E501

        :param manual_start: The manual_start of this Task.  # noqa: E501
        :type: datetime
        """
        if manual_start is None:
            raise ValueError("Invalid value for `manual_start`, must not be `None`")  # noqa: E501
        self._manual_start = manual_start
    @property
    def manual_finish(self):
        """Gets the manual_finish of this Task.  # noqa: E501

        Defines manually scheduled finish of a task.  # noqa: E501

        :return: The manual_finish of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._manual_finish

    @manual_finish.setter
    def manual_finish(self, manual_finish):
        """Sets the manual_finish of this Task.

        Defines manually scheduled finish of a task.  # noqa: E501

        :param manual_finish: The manual_finish of this Task.  # noqa: E501
        :type: datetime
        """
        if manual_finish is None:
            raise ValueError("Invalid value for `manual_finish`, must not be `None`")  # noqa: E501
        self._manual_finish = manual_finish
    @property
    def manual_duration(self):
        """Gets the manual_duration of this Task.  # noqa: E501

        Defines manually scheduled duration of a task.  # noqa: E501

        :return: The manual_duration of this Task.  # noqa: E501
        :rtype: str
        """
        return self._manual_duration

    @manual_duration.setter
    def manual_duration(self, manual_duration):
        """Sets the manual_duration of this Task.

        Defines manually scheduled duration of a task.  # noqa: E501

        :param manual_duration: The manual_duration of this Task.  # noqa: E501
        :type: str
        """
        if manual_duration is None:
            raise ValueError("Invalid value for `manual_duration`, must not be `None`")  # noqa: E501
        self._manual_duration = manual_duration
    @property
    def total_slack(self):
        """Gets the total_slack of this Task.  # noqa: E501

        The amount of a total slack.  # noqa: E501

        :return: The total_slack of this Task.  # noqa: E501
        :rtype: int
        """
        return self._total_slack

    @total_slack.setter
    def total_slack(self, total_slack):
        """Sets the total_slack of this Task.

        The amount of a total slack.  # noqa: E501

        :param total_slack: The total_slack of this Task.  # noqa: E501
        :type: int
        """
        if total_slack is None:
            raise ValueError("Invalid value for `total_slack`, must not be `None`")  # noqa: E501
        self._total_slack = total_slack
    @property
    def type(self):
        """Gets the type of this Task.  # noqa: E501

        The type of a task.  # noqa: E501

        :return: The type of this Task.  # noqa: E501
        :rtype: TaskType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Task.

        The type of a task.  # noqa: E501

        :param type: The type of this Task.  # noqa: E501
        :type: TaskType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type
    @property
    def wbs(self):
        """Gets the wbs of this Task.  # noqa: E501

        The work breakdown structure code of a task.  # noqa: E501

        :return: The wbs of this Task.  # noqa: E501
        :rtype: str
        """
        return self._wbs

    @wbs.setter
    def wbs(self, wbs):
        """Sets the wbs of this Task.

        The work breakdown structure code of a task.  # noqa: E501

        :param wbs: The wbs of this Task.  # noqa: E501
        :type: str
        """
        self._wbs = wbs
    @property
    def priority(self):
        """Gets the priority of this Task.  # noqa: E501

        The priority of a task from 0 to 1000.  # noqa: E501

        :return: The priority of this Task.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this Task.

        The priority of a task from 0 to 1000.  # noqa: E501

        :param priority: The priority of this Task.  # noqa: E501
        :type: int
        """
        if priority is None:
            raise ValueError("Invalid value for `priority`, must not be `None`")  # noqa: E501
        self._priority = priority
    @property
    def work(self):
        """Gets the work of this Task.  # noqa: E501

        The amount of the scheduled work for a task.  # noqa: E501

        :return: The work of this Task.  # noqa: E501
        :rtype: str
        """
        return self._work

    @work.setter
    def work(self, work):
        """Sets the work of this Task.

        The amount of the scheduled work for a task.  # noqa: E501

        :param work: The work of this Task.  # noqa: E501
        :type: str
        """
        if work is None:
            raise ValueError("Invalid value for `work`, must not be `None`")  # noqa: E501
        self._work = work
    @property
    def work_variance(self):
        """Gets the work_variance of this Task.  # noqa: E501

        The variance of the task work from the baseline task work as minutes.  # noqa: E501

        :return: The work_variance of this Task.  # noqa: E501
        :rtype: float
        """
        return self._work_variance

    @work_variance.setter
    def work_variance(self, work_variance):
        """Sets the work_variance of this Task.

        The variance of the task work from the baseline task work as minutes.  # noqa: E501

        :param work_variance: The work_variance of this Task.  # noqa: E501
        :type: float
        """
        if work_variance is None:
            raise ValueError("Invalid value for `work_variance`, must not be `None`")  # noqa: E501
        self._work_variance = work_variance
    @property
    def notes_text(self):
        """Gets the notes_text of this Task.  # noqa: E501

        Notes' plain text extracted from RTF data.  # noqa: E501

        :return: The notes_text of this Task.  # noqa: E501
        :rtype: str
        """
        return self._notes_text

    @notes_text.setter
    def notes_text(self, notes_text):
        """Sets the notes_text of this Task.

        Notes' plain text extracted from RTF data.  # noqa: E501

        :param notes_text: The notes_text of this Task.  # noqa: E501
        :type: str
        """
        self._notes_text = notes_text
    @property
    def notes_rtf(self):
        """Gets the notes_rtf of this Task.  # noqa: E501

        The text notes in RTF format.  # noqa: E501

        :return: The notes_rtf of this Task.  # noqa: E501
        :rtype: str
        """
        return self._notes_rtf

    @notes_rtf.setter
    def notes_rtf(self, notes_rtf):
        """Sets the notes_rtf of this Task.

        The text notes in RTF format.  # noqa: E501

        :param notes_rtf: The notes_rtf of this Task.  # noqa: E501
        :type: str
        """
        self._notes_rtf = notes_rtf
    @property
    def acwp(self):
        """Gets the acwp of this Task.  # noqa: E501


        :return: The acwp of this Task.  # noqa: E501
        :rtype: float
        """
        return self._acwp

    @acwp.setter
    def acwp(self, acwp):
        """Sets the acwp of this Task.


        :param acwp: The acwp of this Task.  # noqa: E501
        :type: float
        """
        if acwp is None:
            raise ValueError("Invalid value for `acwp`, must not be `None`")  # noqa: E501
        self._acwp = acwp
    @property
    def bcws(self):
        """Gets the bcws of this Task.  # noqa: E501


        :return: The bcws of this Task.  # noqa: E501
        :rtype: float
        """
        return self._bcws

    @bcws.setter
    def bcws(self, bcws):
        """Sets the bcws of this Task.


        :param bcws: The bcws of this Task.  # noqa: E501
        :type: float
        """
        if bcws is None:
            raise ValueError("Invalid value for `bcws`, must not be `None`")  # noqa: E501
        self._bcws = bcws
    @property
    def bcwp(self):
        """Gets the bcwp of this Task.  # noqa: E501


        :return: The bcwp of this Task.  # noqa: E501
        :rtype: float
        """
        return self._bcwp

    @bcwp.setter
    def bcwp(self, bcwp):
        """Sets the bcwp of this Task.


        :param bcwp: The bcwp of this Task.  # noqa: E501
        :type: float
        """
        if bcwp is None:
            raise ValueError("Invalid value for `bcwp`, must not be `None`")  # noqa: E501
        self._bcwp = bcwp
    @property
    def leveling_delay_format(self):
        """Gets the leveling_delay_format of this Task.  # noqa: E501

        LevelingDelayFormat  # noqa: E501

        :return: The leveling_delay_format of this Task.  # noqa: E501
        :rtype: TimeUnitType
        """
        return self._leveling_delay_format

    @leveling_delay_format.setter
    def leveling_delay_format(self, leveling_delay_format):
        """Sets the leveling_delay_format of this Task.

        LevelingDelayFormat  # noqa: E501

        :param leveling_delay_format: The leveling_delay_format of this Task.  # noqa: E501
        :type: TimeUnitType
        """
        if leveling_delay_format is None:
            raise ValueError("Invalid value for `leveling_delay_format`, must not be `None`")  # noqa: E501
        self._leveling_delay_format = leveling_delay_format
    @property
    def predecessors(self):
        """Gets the predecessors of this Task.  # noqa: E501

        The task Uid numbers for the predecessor tasks on which the task depends before it can be started or finished.  # noqa: E501

        :return: The predecessors of this Task.  # noqa: E501
        :rtype: str
        """
        return self._predecessors

    @predecessors.setter
    def predecessors(self, predecessors):
        """Sets the predecessors of this Task.

        The task Uid numbers for the predecessor tasks on which the task depends before it can be started or finished.  # noqa: E501

        :param predecessors: The predecessors of this Task.  # noqa: E501
        :type: str
        """
        self._predecessors = predecessors
    @property
    def successors(self):
        """Gets the successors of this Task.  # noqa: E501

        The task Uid numbers for the successor tasks to a task.  # noqa: E501

        :return: The successors of this Task.  # noqa: E501
        :rtype: str
        """
        return self._successors

    @successors.setter
    def successors(self, successors):
        """Sets the successors of this Task.

        The task Uid numbers for the successor tasks to a task.  # noqa: E501

        :param successors: The successors of this Task.  # noqa: E501
        :type: str
        """
        self._successors = successors
    @property
    def ignore_warnings(self):
        """Gets the ignore_warnings of this Task.  # noqa: E501

        Indicates whether to hide the schedule conflict warning indicator in Microsoft Project.               # noqa: E501

        :return: The ignore_warnings of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_warnings

    @ignore_warnings.setter
    def ignore_warnings(self, ignore_warnings):
        """Sets the ignore_warnings of this Task.

        Indicates whether to hide the schedule conflict warning indicator in Microsoft Project.               # noqa: E501

        :param ignore_warnings: The ignore_warnings of this Task.  # noqa: E501
        :type: bool
        """
        if ignore_warnings is None:
            raise ValueError("Invalid value for `ignore_warnings`, must not be `None`")  # noqa: E501
        self._ignore_warnings = ignore_warnings
    @property
    def is_expanded(self):
        """Gets the is_expanded of this Task.  # noqa: E501

        Determines whether a summary task is expanded or not in GanttChart view.  # noqa: E501

        :return: The is_expanded of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._is_expanded

    @is_expanded.setter
    def is_expanded(self, is_expanded):
        """Sets the is_expanded of this Task.

        Determines whether a summary task is expanded or not in GanttChart view.  # noqa: E501

        :param is_expanded: The is_expanded of this Task.  # noqa: E501
        :type: bool
        """
        if is_expanded is None:
            raise ValueError("Invalid value for `is_expanded`, must not be `None`")  # noqa: E501
        self._is_expanded = is_expanded
    @property
    def display_on_timeline(self):
        """Gets the display_on_timeline of this Task.  # noqa: E501

        Specifies whether a task should be displayed on a timeline view.  # noqa: E501

        :return: The display_on_timeline of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._display_on_timeline

    @display_on_timeline.setter
    def display_on_timeline(self, display_on_timeline):
        """Sets the display_on_timeline of this Task.

        Specifies whether a task should be displayed on a timeline view.  # noqa: E501

        :param display_on_timeline: The display_on_timeline of this Task.  # noqa: E501
        :type: bool
        """
        if display_on_timeline is None:
            raise ValueError("Invalid value for `display_on_timeline`, must not be `None`")  # noqa: E501
        self._display_on_timeline = display_on_timeline
    @property
    def display_as_summary(self):
        """Gets the display_as_summary of this Task.  # noqa: E501

        Determines whether the task should be displayed as a summary task. Reading supported for XML format only.  # noqa: E501

        :return: The display_as_summary of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._display_as_summary

    @display_as_summary.setter
    def display_as_summary(self, display_as_summary):
        """Sets the display_as_summary of this Task.

        Determines whether the task should be displayed as a summary task. Reading supported for XML format only.  # noqa: E501

        :param display_as_summary: The display_as_summary of this Task.  # noqa: E501
        :type: bool
        """
        if display_as_summary is None:
            raise ValueError("Invalid value for `display_as_summary`, must not be `None`")  # noqa: E501
        self._display_as_summary = display_as_summary
    @property
    def hyperlink(self):
        """Gets the hyperlink of this Task.  # noqa: E501

        The title or explanatory text for a hyperlink associated with a task.  # noqa: E501

        :return: The hyperlink of this Task.  # noqa: E501
        :rtype: str
        """
        return self._hyperlink

    @hyperlink.setter
    def hyperlink(self, hyperlink):
        """Sets the hyperlink of this Task.

        The title or explanatory text for a hyperlink associated with a task.  # noqa: E501

        :param hyperlink: The hyperlink of this Task.  # noqa: E501
        :type: str
        """
        self._hyperlink = hyperlink
    @property
    def hyperlink_address(self):
        """Gets the hyperlink_address of this Task.  # noqa: E501

        The address for a hyperlink associated with a task.  # noqa: E501

        :return: The hyperlink_address of this Task.  # noqa: E501
        :rtype: str
        """
        return self._hyperlink_address

    @hyperlink_address.setter
    def hyperlink_address(self, hyperlink_address):
        """Sets the hyperlink_address of this Task.

        The address for a hyperlink associated with a task.  # noqa: E501

        :param hyperlink_address: The hyperlink_address of this Task.  # noqa: E501
        :type: str
        """
        self._hyperlink_address = hyperlink_address
    @property
    def hyperlink_sub_address(self):
        """Gets the hyperlink_sub_address of this Task.  # noqa: E501

        The specific location in a document in a hyperlink associated with a task.  type.  # noqa: E501

        :return: The hyperlink_sub_address of this Task.  # noqa: E501
        :rtype: str
        """
        return self._hyperlink_sub_address

    @hyperlink_sub_address.setter
    def hyperlink_sub_address(self, hyperlink_sub_address):
        """Sets the hyperlink_sub_address of this Task.

        The specific location in a document in a hyperlink associated with a task.  type.  # noqa: E501

        :param hyperlink_sub_address: The hyperlink_sub_address of this Task.  # noqa: E501
        :type: str
        """
        self._hyperlink_sub_address = hyperlink_sub_address
    @property
    def earned_value_method(self):
        """Gets the earned_value_method of this Task.  # noqa: E501

        Determines whether the % Complete or Physical % Complete field should be used to calculate budgeted cost of work performed (BCWP).  # noqa: E501

        :return: The earned_value_method of this Task.  # noqa: E501
        :rtype: EarnedValueMethodType
        """
        return self._earned_value_method

    @earned_value_method.setter
    def earned_value_method(self, earned_value_method):
        """Sets the earned_value_method of this Task.

        Determines whether the % Complete or Physical % Complete field should be used to calculate budgeted cost of work performed (BCWP).  # noqa: E501

        :param earned_value_method: The earned_value_method of this Task.  # noqa: E501
        :type: EarnedValueMethodType
        """
        if earned_value_method is None:
            raise ValueError("Invalid value for `earned_value_method`, must not be `None`")  # noqa: E501
        self._earned_value_method = earned_value_method
    @property
    def is_published(self):
        """Gets the is_published of this Task.  # noqa: E501

        Determines whether the current task should be published to Project Server with the rest of the project.  # noqa: E501

        :return: The is_published of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._is_published

    @is_published.setter
    def is_published(self, is_published):
        """Sets the is_published of this Task.

        Determines whether the current task should be published to Project Server with the rest of the project.  # noqa: E501

        :param is_published: The is_published of this Task.  # noqa: E501
        :type: bool
        """
        if is_published is None:
            raise ValueError("Invalid value for `is_published`, must not be `None`")  # noqa: E501
        self._is_published = is_published
    @property
    def status_manager(self):
        """Gets the status_manager of this Task.  # noqa: E501

        The name of the enterprise resource who is to receive status updates for the current task from resources.  # noqa: E501

        :return: The status_manager of this Task.  # noqa: E501
        :rtype: str
        """
        return self._status_manager

    @status_manager.setter
    def status_manager(self, status_manager):
        """Sets the status_manager of this Task.

        The name of the enterprise resource who is to receive status updates for the current task from resources.  # noqa: E501

        :param status_manager: The status_manager of this Task.  # noqa: E501
        :type: str
        """
        self._status_manager = status_manager
    @property
    def commitment_start(self):
        """Gets the commitment_start of this Task.  # noqa: E501

        The start date of a delivery. Reading supported for XML format only.  # noqa: E501

        :return: The commitment_start of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._commitment_start

    @commitment_start.setter
    def commitment_start(self, commitment_start):
        """Sets the commitment_start of this Task.

        The start date of a delivery. Reading supported for XML format only.  # noqa: E501

        :param commitment_start: The commitment_start of this Task.  # noqa: E501
        :type: datetime
        """
        if commitment_start is None:
            raise ValueError("Invalid value for `commitment_start`, must not be `None`")  # noqa: E501
        self._commitment_start = commitment_start
    @property
    def commitment_finish(self):
        """Gets the commitment_finish of this Task.  # noqa: E501

        The finish date of a delivery. Reading supported for XML format only.  # noqa: E501

        :return: The commitment_finish of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._commitment_finish

    @commitment_finish.setter
    def commitment_finish(self, commitment_finish):
        """Sets the commitment_finish of this Task.

        The finish date of a delivery. Reading supported for XML format only.  # noqa: E501

        :param commitment_finish: The commitment_finish of this Task.  # noqa: E501
        :type: datetime
        """
        if commitment_finish is None:
            raise ValueError("Invalid value for `commitment_finish`, must not be `None`")  # noqa: E501
        self._commitment_finish = commitment_finish
    @property
    def commitment_type(self):
        """Gets the commitment_type of this Task.  # noqa: E501

        Determines whether a task has an associated delivery or a dependency on an associated delivery. Reading supported for XML format only.  # noqa: E501

        :return: The commitment_type of this Task.  # noqa: E501
        :rtype: int
        """
        return self._commitment_type

    @commitment_type.setter
    def commitment_type(self, commitment_type):
        """Sets the commitment_type of this Task.

        Determines whether a task has an associated delivery or a dependency on an associated delivery. Reading supported for XML format only.  # noqa: E501

        :param commitment_type: The commitment_type of this Task.  # noqa: E501
        :type: int
        """
        if commitment_type is None:
            raise ValueError("Invalid value for `commitment_type`, must not be `None`")  # noqa: E501
        self._commitment_type = commitment_type
    @property
    def baselines(self):
        """Gets the baselines of this Task.  # noqa: E501

        Gets or sets the collection of baseline values of the task.  # noqa: E501

        :return: The baselines of this Task.  # noqa: E501
        :rtype: list[TaskBaseline]
        """
        return self._baselines

    @baselines.setter
    def baselines(self, baselines):
        """Sets the baselines of this Task.

        Gets or sets the collection of baseline values of the task.  # noqa: E501

        :param baselines: The baselines of this Task.  # noqa: E501
        :type: list[TaskBaseline]
        """
        self._baselines = baselines
    @property
    def extended_attributes(self):
        """Gets the extended_attributes of this Task.  # noqa: E501

        Task extended attributes.  # noqa: E501

        :return: The extended_attributes of this Task.  # noqa: E501
        :rtype: list[ExtendedAttribute]
        """
        return self._extended_attributes

    @extended_attributes.setter
    def extended_attributes(self, extended_attributes):
        """Sets the extended_attributes of this Task.

        Task extended attributes.  # noqa: E501

        :param extended_attributes: The extended_attributes of this Task.  # noqa: E501
        :type: list[ExtendedAttribute]
        """
        self._extended_attributes = extended_attributes
    @property
    def outline_codes(self):
        """Gets the outline_codes of this Task.  # noqa: E501

        Task outline codes.  # noqa: E501

        :return: The outline_codes of this Task.  # noqa: E501
        :rtype: list[OutlineCode]
        """
        return self._outline_codes

    @outline_codes.setter
    def outline_codes(self, outline_codes):
        """Sets the outline_codes of this Task.

        Task outline codes.  # noqa: E501

        :param outline_codes: The outline_codes of this Task.  # noqa: E501
        :type: list[OutlineCode]
        """
        self._outline_codes = outline_codes
    @property
    def warning(self):
        """Gets the warning of this Task.  # noqa: E501

        Represents the flag which indicates that task has schedule discrepancies.  # noqa: E501

        :return: The warning of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._warning

    @warning.setter
    def warning(self, warning):
        """Sets the warning of this Task.

        Represents the flag which indicates that task has schedule discrepancies.  # noqa: E501

        :param warning: The warning of this Task.  # noqa: E501
        :type: bool
        """
        if warning is None:
            raise ValueError("Invalid value for `warning`, must not be `None`")  # noqa: E501
        self._warning = warning
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
        if not isinstance(other, Task):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
