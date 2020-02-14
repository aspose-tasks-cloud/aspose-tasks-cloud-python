# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="Resource.py">
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


class Resource(object):
    """Represents a project resource.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'uid': 'int',
        'id': 'int',
        'guid': 'str',
        'type': 'ResourceType',
        'is_null': 'bool',
        'initials': 'str',
        'phonetics': 'str',
        'nt_account': 'str',
        'windows_user_account': 'str',
        'workgroup': 'WorkGroupType',
        'material_label': 'str',
        'code': 'str',
        'group': 'str',
        'email_address': 'str',
        'hyperlink': 'str',
        'hyperlink_address': 'str',
        'hyperlink_sub_address': 'str',
        'max_units': 'float',
        'peak_units': 'float',
        'over_allocated': 'bool',
        'available_from': 'datetime',
        'available_to': 'datetime',
        'start': 'datetime',
        'finish': 'datetime',
        'can_level': 'bool',
        'accrue_at': 'CostAccrualType',
        'work': 'str',
        'regular_work': 'str',
        'overtime_work': 'str',
        'actual_work': 'str',
        'remaining_work': 'str',
        'actual_overtime_work': 'str',
        'remaining_overtime_work': 'str',
        'percent_work_complete': 'int',
        'standard_rate': 'float',
        'standard_rate_format': 'RateFormatType',
        'cost': 'float',
        'overtime_rate_format': 'RateFormatType',
        'overtime_cost': 'float',
        'cost_per_use': 'float',
        'actual_cost': 'float',
        'actual_overtime_cost': 'float',
        'remaining_cost': 'float',
        'remaining_overtime_cost': 'float',
        'work_variance': 'float',
        'cost_variance': 'float',
        'sv': 'float',
        'cv': 'float',
        'acwp': 'float',
        'calendar_uid': 'int',
        'notes_text': 'str',
        'notes': 'str',
        'notes_rtf': 'str',
        'bcws': 'float',
        'bcwp': 'float',
        'is_generic': 'bool',
        'is_inactive': 'bool',
        'is_enterprise': 'bool',
        'booking_type': 'BookingType',
        'actual_work_protected': 'str',
        'actual_overtime_work_protected': 'str',
        'active_directory_guid': 'str',
        'creation_date': 'datetime',
        'cost_center': 'str',
        'is_cost_resource': 'bool',
        'team_assignment_pool': 'bool',
        'assignment_owner': 'str',
        'assignment_owner_guid': 'str',
        'is_budget': 'bool',
        'budget_work': 'str',
        'budget_cost': 'float',
        'overtime_rate': 'float',
        'baselines': 'list[Baseline]',
        'extended_attributes': 'list[ExtendedAttribute]',
        'outline_codes': 'list[OutlineCode]'
    }

    attribute_map = {
        'name': 'name',
        'uid': 'uid',
        'id': 'id',
        'guid': 'guid',
        'type': 'type',
        'is_null': 'isNull',
        'initials': 'initials',
        'phonetics': 'phonetics',
        'nt_account': 'ntAccount',
        'windows_user_account': 'windowsUserAccount',
        'workgroup': 'workgroup',
        'material_label': 'materialLabel',
        'code': 'code',
        'group': 'group',
        'email_address': 'emailAddress',
        'hyperlink': 'hyperlink',
        'hyperlink_address': 'hyperlinkAddress',
        'hyperlink_sub_address': 'hyperlinkSubAddress',
        'max_units': 'maxUnits',
        'peak_units': 'peakUnits',
        'over_allocated': 'overAllocated',
        'available_from': 'availableFrom',
        'available_to': 'availableTo',
        'start': 'start',
        'finish': 'finish',
        'can_level': 'canLevel',
        'accrue_at': 'accrueAt',
        'work': 'work',
        'regular_work': 'regularWork',
        'overtime_work': 'overtimeWork',
        'actual_work': 'actualWork',
        'remaining_work': 'remainingWork',
        'actual_overtime_work': 'actualOvertimeWork',
        'remaining_overtime_work': 'remainingOvertimeWork',
        'percent_work_complete': 'percentWorkComplete',
        'standard_rate': 'standardRate',
        'standard_rate_format': 'standardRateFormat',
        'cost': 'cost',
        'overtime_rate_format': 'overtimeRateFormat',
        'overtime_cost': 'overtimeCost',
        'cost_per_use': 'costPerUse',
        'actual_cost': 'actualCost',
        'actual_overtime_cost': 'actualOvertimeCost',
        'remaining_cost': 'remainingCost',
        'remaining_overtime_cost': 'remainingOvertimeCost',
        'work_variance': 'workVariance',
        'cost_variance': 'costVariance',
        'sv': 'sv',
        'cv': 'cv',
        'acwp': 'acwp',
        'calendar_uid': 'calendarUid',
        'notes_text': 'notesText',
        'notes': 'notes',
        'notes_rtf': 'notesRTF',
        'bcws': 'bcws',
        'bcwp': 'bcwp',
        'is_generic': 'isGeneric',
        'is_inactive': 'isInactive',
        'is_enterprise': 'isEnterprise',
        'booking_type': 'bookingType',
        'actual_work_protected': 'actualWorkProtected',
        'actual_overtime_work_protected': 'actualOvertimeWorkProtected',
        'active_directory_guid': 'activeDirectoryGuid',
        'creation_date': 'creationDate',
        'cost_center': 'costCenter',
        'is_cost_resource': 'isCostResource',
        'team_assignment_pool': 'teamAssignmentPool',
        'assignment_owner': 'assignmentOwner',
        'assignment_owner_guid': 'assignmentOwnerGuid',
        'is_budget': 'isBudget',
        'budget_work': 'budgetWork',
        'budget_cost': 'budgetCost',
        'overtime_rate': 'overtimeRate',
        'baselines': 'baselines',
        'extended_attributes': 'extendedAttributes',
        'outline_codes': 'outlineCodes'
    }

    def __init__(self, name=None, uid=None, id=None, guid=None, type=None, is_null=None, initials=None, phonetics=None, nt_account=None, windows_user_account=None, workgroup=None, material_label=None, code=None, group=None, email_address=None, hyperlink=None, hyperlink_address=None, hyperlink_sub_address=None, max_units=1.0, peak_units=None, over_allocated=None, available_from=None, available_to=None, start=None, finish=None, can_level=True, accrue_at=None, work=None, regular_work=None, overtime_work=None, actual_work=None, remaining_work=None, actual_overtime_work=None, remaining_overtime_work=None, percent_work_complete=None, standard_rate=None, standard_rate_format=None, cost=None, overtime_rate_format=None, overtime_cost=None, cost_per_use=None, actual_cost=None, actual_overtime_cost=None, remaining_cost=None, remaining_overtime_cost=None, work_variance=None, cost_variance=None, sv=None, cv=None, acwp=None, calendar_uid=None, notes_text=None, notes=None, notes_rtf=None, bcws=None, bcwp=None, is_generic=None, is_inactive=None, is_enterprise=None, booking_type=None, actual_work_protected=None, actual_overtime_work_protected=None, active_directory_guid=None, creation_date=None, cost_center=None, is_cost_resource=None, team_assignment_pool=None, assignment_owner=None, assignment_owner_guid=None, is_budget=None, budget_work=None, budget_cost=None, overtime_rate=None, baselines=None, extended_attributes=None, outline_codes=None):  # noqa: E501
        """Resource - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._uid = None
        self._id = None
        self._guid = None
        self._type = None
        self._is_null = None
        self._initials = None
        self._phonetics = None
        self._nt_account = None
        self._windows_user_account = None
        self._workgroup = None
        self._material_label = None
        self._code = None
        self._group = None
        self._email_address = None
        self._hyperlink = None
        self._hyperlink_address = None
        self._hyperlink_sub_address = None
        self._max_units = None
        self._peak_units = None
        self._over_allocated = None
        self._available_from = None
        self._available_to = None
        self._start = None
        self._finish = None
        self._can_level = None
        self._accrue_at = None
        self._work = None
        self._regular_work = None
        self._overtime_work = None
        self._actual_work = None
        self._remaining_work = None
        self._actual_overtime_work = None
        self._remaining_overtime_work = None
        self._percent_work_complete = None
        self._standard_rate = None
        self._standard_rate_format = None
        self._cost = None
        self._overtime_rate_format = None
        self._overtime_cost = None
        self._cost_per_use = None
        self._actual_cost = None
        self._actual_overtime_cost = None
        self._remaining_cost = None
        self._remaining_overtime_cost = None
        self._work_variance = None
        self._cost_variance = None
        self._sv = None
        self._cv = None
        self._acwp = None
        self._calendar_uid = None
        self._notes_text = None
        self._notes = None
        self._notes_rtf = None
        self._bcws = None
        self._bcwp = None
        self._is_generic = None
        self._is_inactive = None
        self._is_enterprise = None
        self._booking_type = None
        self._actual_work_protected = None
        self._actual_overtime_work_protected = None
        self._active_directory_guid = None
        self._creation_date = None
        self._cost_center = None
        self._is_cost_resource = None
        self._team_assignment_pool = None
        self._assignment_owner = None
        self._assignment_owner_guid = None
        self._is_budget = None
        self._budget_work = None
        self._budget_cost = None
        self._overtime_rate = None
        self._baselines = None
        self._extended_attributes = None
        self._outline_codes = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if uid is not None:
            self.uid = uid
        if id is not None:
            self.id = id
        if guid is not None:
            self.guid = guid
        if type is not None:
            self.type = type
        if is_null is not None:
            self.is_null = is_null
        if initials is not None:
            self.initials = initials
        if phonetics is not None:
            self.phonetics = phonetics
        if nt_account is not None:
            self.nt_account = nt_account
        if windows_user_account is not None:
            self.windows_user_account = windows_user_account
        if workgroup is not None:
            self.workgroup = workgroup
        if material_label is not None:
            self.material_label = material_label
        if code is not None:
            self.code = code
        if group is not None:
            self.group = group
        if email_address is not None:
            self.email_address = email_address
        if hyperlink is not None:
            self.hyperlink = hyperlink
        if hyperlink_address is not None:
            self.hyperlink_address = hyperlink_address
        if hyperlink_sub_address is not None:
            self.hyperlink_sub_address = hyperlink_sub_address
        if max_units is not None:
            self.max_units = max_units
        if peak_units is not None:
            self.peak_units = peak_units
        if over_allocated is not None:
            self.over_allocated = over_allocated
        if available_from is not None:
            self.available_from = available_from
        if available_to is not None:
            self.available_to = available_to
        if start is not None:
            self.start = start
        if finish is not None:
            self.finish = finish
        if can_level is not None:
            self.can_level = can_level
        if accrue_at is not None:
            self.accrue_at = accrue_at
        if work is not None:
            self.work = work
        if regular_work is not None:
            self.regular_work = regular_work
        if overtime_work is not None:
            self.overtime_work = overtime_work
        if actual_work is not None:
            self.actual_work = actual_work
        if remaining_work is not None:
            self.remaining_work = remaining_work
        if actual_overtime_work is not None:
            self.actual_overtime_work = actual_overtime_work
        if remaining_overtime_work is not None:
            self.remaining_overtime_work = remaining_overtime_work
        if percent_work_complete is not None:
            self.percent_work_complete = percent_work_complete
        if standard_rate is not None:
            self.standard_rate = standard_rate
        if standard_rate_format is not None:
            self.standard_rate_format = standard_rate_format
        if cost is not None:
            self.cost = cost
        if overtime_rate_format is not None:
            self.overtime_rate_format = overtime_rate_format
        if overtime_cost is not None:
            self.overtime_cost = overtime_cost
        if cost_per_use is not None:
            self.cost_per_use = cost_per_use
        if actual_cost is not None:
            self.actual_cost = actual_cost
        if actual_overtime_cost is not None:
            self.actual_overtime_cost = actual_overtime_cost
        if remaining_cost is not None:
            self.remaining_cost = remaining_cost
        if remaining_overtime_cost is not None:
            self.remaining_overtime_cost = remaining_overtime_cost
        if work_variance is not None:
            self.work_variance = work_variance
        if cost_variance is not None:
            self.cost_variance = cost_variance
        if sv is not None:
            self.sv = sv
        if cv is not None:
            self.cv = cv
        if acwp is not None:
            self.acwp = acwp
        if calendar_uid is not None:
            self.calendar_uid = calendar_uid
        if notes_text is not None:
            self.notes_text = notes_text
        if notes is not None:
            self.notes = notes
        if notes_rtf is not None:
            self.notes_rtf = notes_rtf
        if bcws is not None:
            self.bcws = bcws
        if bcwp is not None:
            self.bcwp = bcwp
        if is_generic is not None:
            self.is_generic = is_generic
        if is_inactive is not None:
            self.is_inactive = is_inactive
        if is_enterprise is not None:
            self.is_enterprise = is_enterprise
        if booking_type is not None:
            self.booking_type = booking_type
        if actual_work_protected is not None:
            self.actual_work_protected = actual_work_protected
        if actual_overtime_work_protected is not None:
            self.actual_overtime_work_protected = actual_overtime_work_protected
        if active_directory_guid is not None:
            self.active_directory_guid = active_directory_guid
        if creation_date is not None:
            self.creation_date = creation_date
        if cost_center is not None:
            self.cost_center = cost_center
        if is_cost_resource is not None:
            self.is_cost_resource = is_cost_resource
        if team_assignment_pool is not None:
            self.team_assignment_pool = team_assignment_pool
        if assignment_owner is not None:
            self.assignment_owner = assignment_owner
        if assignment_owner_guid is not None:
            self.assignment_owner_guid = assignment_owner_guid
        if is_budget is not None:
            self.is_budget = is_budget
        if budget_work is not None:
            self.budget_work = budget_work
        if budget_cost is not None:
            self.budget_cost = budget_cost
        if overtime_rate is not None:
            self.overtime_rate = overtime_rate
        if baselines is not None:
            self.baselines = baselines
        if extended_attributes is not None:
            self.extended_attributes = extended_attributes
        if outline_codes is not None:
            self.outline_codes = outline_codes

    @property
    def name(self):
        """Gets the name of this Resource.  # noqa: E501

        The name of a resource.  # noqa: E501

        :return: The name of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Resource.

        The name of a resource.  # noqa: E501

        :param name: The name of this Resource.  # noqa: E501
        :type: str
        """
        self._name = name
    @property
    def uid(self):
        """Gets the uid of this Resource.  # noqa: E501

        The unique identifier of a resource.  # noqa: E501

        :return: The uid of this Resource.  # noqa: E501
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this Resource.

        The unique identifier of a resource.  # noqa: E501

        :param uid: The uid of this Resource.  # noqa: E501
        :type: int
        """
        if uid is None:
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501
        self._uid = uid
    @property
    def id(self):
        """Gets the id of this Resource.  # noqa: E501

        The position identifier of a resource within the list of resources.  # noqa: E501

        :return: The id of this Resource.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Resource.

        The position identifier of a resource within the list of resources.  # noqa: E501

        :param id: The id of this Resource.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        self._id = id
    @property
    def guid(self):
        """Gets the guid of this Resource.  # noqa: E501

        Contains the generated unique identification code for the resource.               # noqa: E501

        :return: The guid of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this Resource.

        Contains the generated unique identification code for the resource.               # noqa: E501

        :param guid: The guid of this Resource.  # noqa: E501
        :type: str
        """
        self._guid = guid
    @property
    def type(self):
        """Gets the type of this Resource.  # noqa: E501

        The type of a resource.  # noqa: E501

        :return: The type of this Resource.  # noqa: E501
        :rtype: ResourceType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Resource.

        The type of a resource.  # noqa: E501

        :param type: The type of this Resource.  # noqa: E501
        :type: ResourceType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type
    @property
    def is_null(self):
        """Gets the is_null of this Resource.  # noqa: E501

        Determines whether a resource is null.  # noqa: E501

        :return: The is_null of this Resource.  # noqa: E501
        :rtype: bool
        """
        return self._is_null

    @is_null.setter
    def is_null(self, is_null):
        """Sets the is_null of this Resource.

        Determines whether a resource is null.  # noqa: E501

        :param is_null: The is_null of this Resource.  # noqa: E501
        :type: bool
        """
        if is_null is None:
            raise ValueError("Invalid value for `is_null`, must not be `None`")  # noqa: E501
        self._is_null = is_null
    @property
    def initials(self):
        """Gets the initials of this Resource.  # noqa: E501

        The initials of a resource.  # noqa: E501

        :return: The initials of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._initials

    @initials.setter
    def initials(self, initials):
        """Sets the initials of this Resource.

        The initials of a resource.  # noqa: E501

        :param initials: The initials of this Resource.  # noqa: E501
        :type: str
        """
        self._initials = initials
    @property
    def phonetics(self):
        """Gets the phonetics of this Resource.  # noqa: E501

        The phonetic spelling of the resource name. For use with Japanese only.  # noqa: E501

        :return: The phonetics of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._phonetics

    @phonetics.setter
    def phonetics(self, phonetics):
        """Sets the phonetics of this Resource.

        The phonetic spelling of the resource name. For use with Japanese only.  # noqa: E501

        :param phonetics: The phonetics of this Resource.  # noqa: E501
        :type: str
        """
        self._phonetics = phonetics
    @property
    def nt_account(self):
        """Gets the nt_account of this Resource.  # noqa: E501

        The NT account associated with a resource.  # noqa: E501

        :return: The nt_account of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._nt_account

    @nt_account.setter
    def nt_account(self, nt_account):
        """Sets the nt_account of this Resource.

        The NT account associated with a resource.  # noqa: E501

        :param nt_account: The nt_account of this Resource.  # noqa: E501
        :type: str
        """
        self._nt_account = nt_account
    @property
    def windows_user_account(self):
        """Gets the windows_user_account of this Resource.  # noqa: E501

        The NT account associated with a resource.  # noqa: E501

        :return: The windows_user_account of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._windows_user_account

    @windows_user_account.setter
    def windows_user_account(self, windows_user_account):
        """Sets the windows_user_account of this Resource.

        The NT account associated with a resource.  # noqa: E501

        :param windows_user_account: The windows_user_account of this Resource.  # noqa: E501
        :type: str
        """
        self._windows_user_account = windows_user_account
    @property
    def workgroup(self):
        """Gets the workgroup of this Resource.  # noqa: E501

        The type of a workgroup to which a resource belongs.  type.  # noqa: E501

        :return: The workgroup of this Resource.  # noqa: E501
        :rtype: WorkGroupType
        """
        return self._workgroup

    @workgroup.setter
    def workgroup(self, workgroup):
        """Sets the workgroup of this Resource.

        The type of a workgroup to which a resource belongs.  type.  # noqa: E501

        :param workgroup: The workgroup of this Resource.  # noqa: E501
        :type: WorkGroupType
        """
        if workgroup is None:
            raise ValueError("Invalid value for `workgroup`, must not be `None`")  # noqa: E501
        self._workgroup = workgroup
    @property
    def material_label(self):
        """Gets the material_label of this Resource.  # noqa: E501

        The unit of measure for the material resource. Read/write String.  # noqa: E501

        :return: The material_label of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._material_label

    @material_label.setter
    def material_label(self, material_label):
        """Sets the material_label of this Resource.

        The unit of measure for the material resource. Read/write String.  # noqa: E501

        :param material_label: The material_label of this Resource.  # noqa: E501
        :type: str
        """
        self._material_label = material_label
    @property
    def code(self):
        """Gets the code of this Resource.  # noqa: E501

        The code or other information about a resource.  # noqa: E501

        :return: The code of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Resource.

        The code or other information about a resource.  # noqa: E501

        :param code: The code of this Resource.  # noqa: E501
        :type: str
        """
        self._code = code
    @property
    def group(self):
        """Gets the group of this Resource.  # noqa: E501

        The group to which a resource belongs.  # noqa: E501

        :return: The group of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this Resource.

        The group to which a resource belongs.  # noqa: E501

        :param group: The group of this Resource.  # noqa: E501
        :type: str
        """
        self._group = group
    @property
    def email_address(self):
        """Gets the email_address of this Resource.  # noqa: E501


        :return: The email_address of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this Resource.


        :param email_address: The email_address of this Resource.  # noqa: E501
        :type: str
        """
        self._email_address = email_address
    @property
    def hyperlink(self):
        """Gets the hyperlink of this Resource.  # noqa: E501

        The title of a hyperlink associated with a resource.  # noqa: E501

        :return: The hyperlink of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._hyperlink

    @hyperlink.setter
    def hyperlink(self, hyperlink):
        """Sets the hyperlink of this Resource.

        The title of a hyperlink associated with a resource.  # noqa: E501

        :param hyperlink: The hyperlink of this Resource.  # noqa: E501
        :type: str
        """
        self._hyperlink = hyperlink
    @property
    def hyperlink_address(self):
        """Gets the hyperlink_address of this Resource.  # noqa: E501

        The hyperlink associated with a resource.  # noqa: E501

        :return: The hyperlink_address of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._hyperlink_address

    @hyperlink_address.setter
    def hyperlink_address(self, hyperlink_address):
        """Sets the hyperlink_address of this Resource.

        The hyperlink associated with a resource.  # noqa: E501

        :param hyperlink_address: The hyperlink_address of this Resource.  # noqa: E501
        :type: str
        """
        self._hyperlink_address = hyperlink_address
    @property
    def hyperlink_sub_address(self):
        """Gets the hyperlink_sub_address of this Resource.  # noqa: E501

        The document bookmark of a hyperlink associated with a resource. Read/write String.  # noqa: E501

        :return: The hyperlink_sub_address of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._hyperlink_sub_address

    @hyperlink_sub_address.setter
    def hyperlink_sub_address(self, hyperlink_sub_address):
        """Sets the hyperlink_sub_address of this Resource.

        The document bookmark of a hyperlink associated with a resource. Read/write String.  # noqa: E501

        :param hyperlink_sub_address: The hyperlink_sub_address of this Resource.  # noqa: E501
        :type: str
        """
        self._hyperlink_sub_address = hyperlink_sub_address
    @property
    def max_units(self):
        """Gets the max_units of this Resource.  # noqa: E501

        The maximum number of units of a resource is available.  # noqa: E501

        :return: The max_units of this Resource.  # noqa: E501
        :rtype: float
        """
        return self._max_units

    @max_units.setter
    def max_units(self, max_units):
        """Sets the max_units of this Resource.

        The maximum number of units of a resource is available.  # noqa: E501

        :param max_units: The max_units of this Resource.  # noqa: E501
        :type: float
        """
        if max_units is None:
            raise ValueError("Invalid value for `max_units`, must not be `None`")  # noqa: E501
        self._max_units = max_units
    @property
    def peak_units(self):
        """Gets the peak_units of this Resource.  # noqa: E501

        The largest number of units assigned to a resource at any time.  # noqa: E501

        :return: The peak_units of this Resource.  # noqa: E501
        :rtype: float
        """
        return self._peak_units

    @peak_units.setter
    def peak_units(self, peak_units):
        """Sets the peak_units of this Resource.

        The largest number of units assigned to a resource at any time.  # noqa: E501

        :param peak_units: The peak_units of this Resource.  # noqa: E501
        :type: float
        """
        if peak_units is None:
            raise ValueError("Invalid value for `peak_units`, must not be `None`")  # noqa: E501
        self._peak_units = peak_units
    @property
    def over_allocated(self):
        """Gets the over_allocated of this Resource.  # noqa: E501


        :return: The over_allocated of this Resource.  # noqa: E501
        :rtype: bool
        """
        return self._over_allocated

    @over_allocated.setter
    def over_allocated(self, over_allocated):
        """Sets the over_allocated of this Resource.


        :param over_allocated: The over_allocated of this Resource.  # noqa: E501
        :type: bool
        """
        if over_allocated is None:
            raise ValueError("Invalid value for `over_allocated`, must not be `None`")  # noqa: E501
        self._over_allocated = over_allocated
    @property
    def available_from(self):
        """Gets the available_from of this Resource.  # noqa: E501

        The first date when a resource is available.  # noqa: E501

        :return: The available_from of this Resource.  # noqa: E501
        :rtype: datetime
        """
        return self._available_from

    @available_from.setter
    def available_from(self, available_from):
        """Sets the available_from of this Resource.

        The first date when a resource is available.  # noqa: E501

        :param available_from: The available_from of this Resource.  # noqa: E501
        :type: datetime
        """
        if available_from is None:
            raise ValueError("Invalid value for `available_from`, must not be `None`")  # noqa: E501
        self._available_from = available_from
    @property
    def available_to(self):
        """Gets the available_to of this Resource.  # noqa: E501

        The last date when a resource is available.  # noqa: E501

        :return: The available_to of this Resource.  # noqa: E501
        :rtype: datetime
        """
        return self._available_to

    @available_to.setter
    def available_to(self, available_to):
        """Sets the available_to of this Resource.

        The last date when a resource is available.  # noqa: E501

        :param available_to: The available_to of this Resource.  # noqa: E501
        :type: datetime
        """
        if available_to is None:
            raise ValueError("Invalid value for `available_to`, must not be `None`")  # noqa: E501
        self._available_to = available_to
    @property
    def start(self):
        """Gets the start of this Resource.  # noqa: E501

        The scheduled start date of a resource.  # noqa: E501

        :return: The start of this Resource.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this Resource.

        The scheduled start date of a resource.  # noqa: E501

        :param start: The start of this Resource.  # noqa: E501
        :type: datetime
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501
        self._start = start
    @property
    def finish(self):
        """Gets the finish of this Resource.  # noqa: E501

        The scheduled finish date of a resource.  # noqa: E501

        :return: The finish of this Resource.  # noqa: E501
        :rtype: datetime
        """
        return self._finish

    @finish.setter
    def finish(self, finish):
        """Sets the finish of this Resource.

        The scheduled finish date of a resource.  # noqa: E501

        :param finish: The finish of this Resource.  # noqa: E501
        :type: datetime
        """
        if finish is None:
            raise ValueError("Invalid value for `finish`, must not be `None`")  # noqa: E501
        self._finish = finish
    @property
    def can_level(self):
        """Gets the can_level of this Resource.  # noqa: E501

        Determines whether a resource can be leveled.  # noqa: E501

        :return: The can_level of this Resource.  # noqa: E501
        :rtype: bool
        """
        return self._can_level

    @can_level.setter
    def can_level(self, can_level):
        """Sets the can_level of this Resource.

        Determines whether a resource can be leveled.  # noqa: E501

        :param can_level: The can_level of this Resource.  # noqa: E501
        :type: bool
        """
        if can_level is None:
            raise ValueError("Invalid value for `can_level`, must not be `None`")  # noqa: E501
        self._can_level = can_level
    @property
    def accrue_at(self):
        """Gets the accrue_at of this Resource.  # noqa: E501

        Determines how cost is accrued against the resource.  # noqa: E501

        :return: The accrue_at of this Resource.  # noqa: E501
        :rtype: CostAccrualType
        """
        return self._accrue_at

    @accrue_at.setter
    def accrue_at(self, accrue_at):
        """Sets the accrue_at of this Resource.

        Determines how cost is accrued against the resource.  # noqa: E501

        :param accrue_at: The accrue_at of this Resource.  # noqa: E501
        :type: CostAccrualType
        """
        if accrue_at is None:
            raise ValueError("Invalid value for `accrue_at`, must not be `None`")  # noqa: E501
        self._accrue_at = accrue_at
    @property
    def work(self):
        """Gets the work of this Resource.  # noqa: E501

        The total work assigned to a resource across all assigned tasks.  # noqa: E501

        :return: The work of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._work

    @work.setter
    def work(self, work):
        """Sets the work of this Resource.

        The total work assigned to a resource across all assigned tasks.  # noqa: E501

        :param work: The work of this Resource.  # noqa: E501
        :type: str
        """
        if work is None:
            raise ValueError("Invalid value for `work`, must not be `None`")  # noqa: E501
        self._work = work
    @property
    def regular_work(self):
        """Gets the regular_work of this Resource.  # noqa: E501

        The amount of non-overtime work assigned to a resource.  # noqa: E501

        :return: The regular_work of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._regular_work

    @regular_work.setter
    def regular_work(self, regular_work):
        """Sets the regular_work of this Resource.

        The amount of non-overtime work assigned to a resource.  # noqa: E501

        :param regular_work: The regular_work of this Resource.  # noqa: E501
        :type: str
        """
        if regular_work is None:
            raise ValueError("Invalid value for `regular_work`, must not be `None`")  # noqa: E501
        self._regular_work = regular_work
    @property
    def overtime_work(self):
        """Gets the overtime_work of this Resource.  # noqa: E501

        The amount of overtime work assigned to a resource.  # noqa: E501

        :return: The overtime_work of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._overtime_work

    @overtime_work.setter
    def overtime_work(self, overtime_work):
        """Sets the overtime_work of this Resource.

        The amount of overtime work assigned to a resource.  # noqa: E501

        :param overtime_work: The overtime_work of this Resource.  # noqa: E501
        :type: str
        """
        if overtime_work is None:
            raise ValueError("Invalid value for `overtime_work`, must not be `None`")  # noqa: E501
        self._overtime_work = overtime_work
    @property
    def actual_work(self):
        """Gets the actual_work of this Resource.  # noqa: E501

        The amount of actual work performed by a resource.  # noqa: E501

        :return: The actual_work of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._actual_work

    @actual_work.setter
    def actual_work(self, actual_work):
        """Sets the actual_work of this Resource.

        The amount of actual work performed by a resource.  # noqa: E501

        :param actual_work: The actual_work of this Resource.  # noqa: E501
        :type: str
        """
        if actual_work is None:
            raise ValueError("Invalid value for `actual_work`, must not be `None`")  # noqa: E501
        self._actual_work = actual_work
    @property
    def remaining_work(self):
        """Gets the remaining_work of this Resource.  # noqa: E501

        The amount of remaining work required to complete all assigned tasks.  # noqa: E501

        :return: The remaining_work of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._remaining_work

    @remaining_work.setter
    def remaining_work(self, remaining_work):
        """Sets the remaining_work of this Resource.

        The amount of remaining work required to complete all assigned tasks.  # noqa: E501

        :param remaining_work: The remaining_work of this Resource.  # noqa: E501
        :type: str
        """
        if remaining_work is None:
            raise ValueError("Invalid value for `remaining_work`, must not be `None`")  # noqa: E501
        self._remaining_work = remaining_work
    @property
    def actual_overtime_work(self):
        """Gets the actual_overtime_work of this Resource.  # noqa: E501

        The amount of actual overtime work performed by a resource.  # noqa: E501

        :return: The actual_overtime_work of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._actual_overtime_work

    @actual_overtime_work.setter
    def actual_overtime_work(self, actual_overtime_work):
        """Sets the actual_overtime_work of this Resource.

        The amount of actual overtime work performed by a resource.  # noqa: E501

        :param actual_overtime_work: The actual_overtime_work of this Resource.  # noqa: E501
        :type: str
        """
        if actual_overtime_work is None:
            raise ValueError("Invalid value for `actual_overtime_work`, must not be `None`")  # noqa: E501
        self._actual_overtime_work = actual_overtime_work
    @property
    def remaining_overtime_work(self):
        """Gets the remaining_overtime_work of this Resource.  # noqa: E501

        The amount of remaining overtime work required to complete all tasks.  # noqa: E501

        :return: The remaining_overtime_work of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._remaining_overtime_work

    @remaining_overtime_work.setter
    def remaining_overtime_work(self, remaining_overtime_work):
        """Sets the remaining_overtime_work of this Resource.

        The amount of remaining overtime work required to complete all tasks.  # noqa: E501

        :param remaining_overtime_work: The remaining_overtime_work of this Resource.  # noqa: E501
        :type: str
        """
        if remaining_overtime_work is None:
            raise ValueError("Invalid value for `remaining_overtime_work`, must not be `None`")  # noqa: E501
        self._remaining_overtime_work = remaining_overtime_work
    @property
    def percent_work_complete(self):
        """Gets the percent_work_complete of this Resource.  # noqa: E501

        The percentage of work completed across all tasks.  # noqa: E501

        :return: The percent_work_complete of this Resource.  # noqa: E501
        :rtype: int
        """
        return self._percent_work_complete

    @percent_work_complete.setter
    def percent_work_complete(self, percent_work_complete):
        """Sets the percent_work_complete of this Resource.

        The percentage of work completed across all tasks.  # noqa: E501

        :param percent_work_complete: The percent_work_complete of this Resource.  # noqa: E501
        :type: int
        """
        if percent_work_complete is None:
            raise ValueError("Invalid value for `percent_work_complete`, must not be `None`")  # noqa: E501
        self._percent_work_complete = percent_work_complete
    @property
    def standard_rate(self):
        """Gets the standard_rate of this Resource.  # noqa: E501

        The standard rate of a resource. This value retrieved from the current date if a rate table exists for a resource.  # noqa: E501

        :return: The standard_rate of this Resource.  # noqa: E501
        :rtype: float
        """
        return self._standard_rate

    @standard_rate.setter
    def standard_rate(self, standard_rate):
        """Sets the standard_rate of this Resource.

        The standard rate of a resource. This value retrieved from the current date if a rate table exists for a resource.  # noqa: E501

        :param standard_rate: The standard_rate of this Resource.  # noqa: E501
        :type: float
        """
        if standard_rate is None:
            raise ValueError("Invalid value for `standard_rate`, must not be `None`")  # noqa: E501
        self._standard_rate = standard_rate
    @property
    def standard_rate_format(self):
        """Gets the standard_rate_format of this Resource.  # noqa: E501

        The units used by Microsoft Project to display the standard rate.  # noqa: E501

        :return: The standard_rate_format of this Resource.  # noqa: E501
        :rtype: RateFormatType
        """
        return self._standard_rate_format

    @standard_rate_format.setter
    def standard_rate_format(self, standard_rate_format):
        """Sets the standard_rate_format of this Resource.

        The units used by Microsoft Project to display the standard rate.  # noqa: E501

        :param standard_rate_format: The standard_rate_format of this Resource.  # noqa: E501
        :type: RateFormatType
        """
        if standard_rate_format is None:
            raise ValueError("Invalid value for `standard_rate_format`, must not be `None`")  # noqa: E501
        self._standard_rate_format = standard_rate_format
    @property
    def cost(self):
        """Gets the cost of this Resource.  # noqa: E501

        The total project cost for a resource across all assigned tasks.  # noqa: E501

        :return: The cost of this Resource.  # noqa: E501
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this Resource.

        The total project cost for a resource across all assigned tasks.  # noqa: E501

        :param cost: The cost of this Resource.  # noqa: E501
        :type: float
        """
        if cost is None:
            raise ValueError("Invalid value for `cost`, must not be `None`")  # noqa: E501
        self._cost = cost
    @property
    def overtime_rate_format(self):
        """Gets the overtime_rate_format of this Resource.  # noqa: E501

        The units used by Microsoft Project to display the overtime rate.  # noqa: E501

        :return: The overtime_rate_format of this Resource.  # noqa: E501
        :rtype: RateFormatType
        """
        return self._overtime_rate_format

    @overtime_rate_format.setter
    def overtime_rate_format(self, overtime_rate_format):
        """Sets the overtime_rate_format of this Resource.

        The units used by Microsoft Project to display the overtime rate.  # noqa: E501

        :param overtime_rate_format: The overtime_rate_format of this Resource.  # noqa: E501
        :type: RateFormatType
        """
        if overtime_rate_format is None:
            raise ValueError("Invalid value for `overtime_rate_format`, must not be `None`")  # noqa: E501
        self._overtime_rate_format = overtime_rate_format
    @property
    def overtime_cost(self):
        """Gets the overtime_cost of this Resource.  # noqa: E501

        The total overtime cost of a resource including actual and remaining overtime costs.  # noqa: E501

        :return: The overtime_cost of this Resource.  # noqa: E501
        :rtype: float
        """
        return self._overtime_cost

    @overtime_cost.setter
    def overtime_cost(self, overtime_cost):
        """Sets the overtime_cost of this Resource.

        The total overtime cost of a resource including actual and remaining overtime costs.  # noqa: E501

        :param overtime_cost: The overtime_cost of this Resource.  # noqa: E501
        :type: float
        """
        if overtime_cost is None:
            raise ValueError("Invalid value for `overtime_cost`, must not be `None`")  # noqa: E501
        self._overtime_cost = overtime_cost
    @property
    def cost_per_use(self):
        """Gets the cost_per_use of this Resource.  # noqa: E501

        The cost per use of a resource. This value retrieved from the current date if a rate table exists for the resource.  # noqa: E501

        :return: The cost_per_use of this Resource.  # noqa: E501
        :rtype: float
        """
        return self._cost_per_use

    @cost_per_use.setter
    def cost_per_use(self, cost_per_use):
        """Sets the cost_per_use of this Resource.

        The cost per use of a resource. This value retrieved from the current date if a rate table exists for the resource.  # noqa: E501

        :param cost_per_use: The cost_per_use of this Resource.  # noqa: E501
        :type: float
        """
        if cost_per_use is None:
            raise ValueError("Invalid value for `cost_per_use`, must not be `None`")  # noqa: E501
        self._cost_per_use = cost_per_use
    @property
    def actual_cost(self):
        """Gets the actual_cost of this Resource.  # noqa: E501

        The actual cost incurred by the resource across all assigned tasks.  # noqa: E501

        :return: The actual_cost of this Resource.  # noqa: E501
        :rtype: float
        """
        return self._actual_cost

    @actual_cost.setter
    def actual_cost(self, actual_cost):
        """Sets the actual_cost of this Resource.

        The actual cost incurred by the resource across all assigned tasks.  # noqa: E501

        :param actual_cost: The actual_cost of this Resource.  # noqa: E501
        :type: float
        """
        if actual_cost is None:
            raise ValueError("Invalid value for `actual_cost`, must not be `None`")  # noqa: E501
        self._actual_cost = actual_cost
    @property
    def actual_overtime_cost(self):
        """Gets the actual_overtime_cost of this Resource.  # noqa: E501

        The actual overtime cost incurred by the resource across all assigned tasks.  # noqa: E501

        :return: The actual_overtime_cost of this Resource.  # noqa: E501
        :rtype: float
        """
        return self._actual_overtime_cost

    @actual_overtime_cost.setter
    def actual_overtime_cost(self, actual_overtime_cost):
        """Sets the actual_overtime_cost of this Resource.

        The actual overtime cost incurred by the resource across all assigned tasks.  # noqa: E501

        :param actual_overtime_cost: The actual_overtime_cost of this Resource.  # noqa: E501
        :type: float
        """
        if actual_overtime_cost is None:
            raise ValueError("Invalid value for `actual_overtime_cost`, must not be `None`")  # noqa: E501
        self._actual_overtime_cost = actual_overtime_cost
    @property
    def remaining_cost(self):
        """Gets the remaining_cost of this Resource.  # noqa: E501

        The remaining projected cost of a resource to complete all assigned tasks.  # noqa: E501

        :return: The remaining_cost of this Resource.  # noqa: E501
        :rtype: float
        """
        return self._remaining_cost

    @remaining_cost.setter
    def remaining_cost(self, remaining_cost):
        """Sets the remaining_cost of this Resource.

        The remaining projected cost of a resource to complete all assigned tasks.  # noqa: E501

        :param remaining_cost: The remaining_cost of this Resource.  # noqa: E501
        :type: float
        """
        if remaining_cost is None:
            raise ValueError("Invalid value for `remaining_cost`, must not be `None`")  # noqa: E501
        self._remaining_cost = remaining_cost
    @property
    def remaining_overtime_cost(self):
        """Gets the remaining_overtime_cost of this Resource.  # noqa: E501

        The remaining projected overtime cost of a resource to complete all assigned tasks.  # noqa: E501

        :return: The remaining_overtime_cost of this Resource.  # noqa: E501
        :rtype: float
        """
        return self._remaining_overtime_cost

    @remaining_overtime_cost.setter
    def remaining_overtime_cost(self, remaining_overtime_cost):
        """Sets the remaining_overtime_cost of this Resource.

        The remaining projected overtime cost of a resource to complete all assigned tasks.  # noqa: E501

        :param remaining_overtime_cost: The remaining_overtime_cost of this Resource.  # noqa: E501
        :type: float
        """
        if remaining_overtime_cost is None:
            raise ValueError("Invalid value for `remaining_overtime_cost`, must not be `None`")  # noqa: E501
        self._remaining_overtime_cost = remaining_overtime_cost
    @property
    def work_variance(self):
        """Gets the work_variance of this Resource.  # noqa: E501

        The difference between a baseline work and a work  # noqa: E501

        :return: The work_variance of this Resource.  # noqa: E501
        :rtype: float
        """
        return self._work_variance

    @work_variance.setter
    def work_variance(self, work_variance):
        """Sets the work_variance of this Resource.

        The difference between a baseline work and a work  # noqa: E501

        :param work_variance: The work_variance of this Resource.  # noqa: E501
        :type: float
        """
        if work_variance is None:
            raise ValueError("Invalid value for `work_variance`, must not be `None`")  # noqa: E501
        self._work_variance = work_variance
    @property
    def cost_variance(self):
        """Gets the cost_variance of this Resource.  # noqa: E501

        The difference between a baseline cost and a cost.  # noqa: E501

        :return: The cost_variance of this Resource.  # noqa: E501
        :rtype: float
        """
        return self._cost_variance

    @cost_variance.setter
    def cost_variance(self, cost_variance):
        """Sets the cost_variance of this Resource.

        The difference between a baseline cost and a cost.  # noqa: E501

        :param cost_variance: The cost_variance of this Resource.  # noqa: E501
        :type: float
        """
        if cost_variance is None:
            raise ValueError("Invalid value for `cost_variance`, must not be `None`")  # noqa: E501
        self._cost_variance = cost_variance
    @property
    def sv(self):
        """Gets the sv of this Resource.  # noqa: E501

        The earned value schedule variance, through the project status date.  # noqa: E501

        :return: The sv of this Resource.  # noqa: E501
        :rtype: float
        """
        return self._sv

    @sv.setter
    def sv(self, sv):
        """Sets the sv of this Resource.

        The earned value schedule variance, through the project status date.  # noqa: E501

        :param sv: The sv of this Resource.  # noqa: E501
        :type: float
        """
        if sv is None:
            raise ValueError("Invalid value for `sv`, must not be `None`")  # noqa: E501
        self._sv = sv
    @property
    def cv(self):
        """Gets the cv of this Resource.  # noqa: E501

        The earned value cost variance, through the project status date.  # noqa: E501

        :return: The cv of this Resource.  # noqa: E501
        :rtype: float
        """
        return self._cv

    @cv.setter
    def cv(self, cv):
        """Sets the cv of this Resource.

        The earned value cost variance, through the project status date.  # noqa: E501

        :param cv: The cv of this Resource.  # noqa: E501
        :type: float
        """
        if cv is None:
            raise ValueError("Invalid value for `cv`, must not be `None`")  # noqa: E501
        self._cv = cv
    @property
    def acwp(self):
        """Gets the acwp of this Resource.  # noqa: E501

        The actual cost of a work performed by a resource for the project to-date.  # noqa: E501

        :return: The acwp of this Resource.  # noqa: E501
        :rtype: float
        """
        return self._acwp

    @acwp.setter
    def acwp(self, acwp):
        """Sets the acwp of this Resource.

        The actual cost of a work performed by a resource for the project to-date.  # noqa: E501

        :param acwp: The acwp of this Resource.  # noqa: E501
        :type: float
        """
        if acwp is None:
            raise ValueError("Invalid value for `acwp`, must not be `None`")  # noqa: E501
        self._acwp = acwp
    @property
    def calendar_uid(self):
        """Gets the calendar_uid of this Resource.  # noqa: E501

        The calendar of a resource.  # noqa: E501

        :return: The calendar_uid of this Resource.  # noqa: E501
        :rtype: int
        """
        return self._calendar_uid

    @calendar_uid.setter
    def calendar_uid(self, calendar_uid):
        """Sets the calendar_uid of this Resource.

        The calendar of a resource.  # noqa: E501

        :param calendar_uid: The calendar_uid of this Resource.  # noqa: E501
        :type: int
        """
        if calendar_uid is None:
            raise ValueError("Invalid value for `calendar_uid`, must not be `None`")  # noqa: E501
        self._calendar_uid = calendar_uid
    @property
    def notes_text(self):
        """Gets the notes_text of this Resource.  # noqa: E501

        Notes' plain text extracted from RTF data.  # noqa: E501

        :return: The notes_text of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._notes_text

    @notes_text.setter
    def notes_text(self, notes_text):
        """Sets the notes_text of this Resource.

        Notes' plain text extracted from RTF data.  # noqa: E501

        :param notes_text: The notes_text of this Resource.  # noqa: E501
        :type: str
        """
        self._notes_text = notes_text
    @property
    def notes(self):
        """Gets the notes of this Resource.  # noqa: E501

        The text notes associated with a resource.  # noqa: E501

        :return: The notes of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Resource.

        The text notes associated with a resource.  # noqa: E501

        :param notes: The notes of this Resource.  # noqa: E501
        :type: str
        """
        self._notes = notes
    @property
    def notes_rtf(self):
        """Gets the notes_rtf of this Resource.  # noqa: E501

        The text notes in RTF format. Supported for MPP formats only.  # noqa: E501

        :return: The notes_rtf of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._notes_rtf

    @notes_rtf.setter
    def notes_rtf(self, notes_rtf):
        """Sets the notes_rtf of this Resource.

        The text notes in RTF format. Supported for MPP formats only.  # noqa: E501

        :param notes_rtf: The notes_rtf of this Resource.  # noqa: E501
        :type: str
        """
        self._notes_rtf = notes_rtf
    @property
    def bcws(self):
        """Gets the bcws of this Resource.  # noqa: E501

        The budget cost of a work scheduled for a resource.  # noqa: E501

        :return: The bcws of this Resource.  # noqa: E501
        :rtype: float
        """
        return self._bcws

    @bcws.setter
    def bcws(self, bcws):
        """Sets the bcws of this Resource.

        The budget cost of a work scheduled for a resource.  # noqa: E501

        :param bcws: The bcws of this Resource.  # noqa: E501
        :type: float
        """
        if bcws is None:
            raise ValueError("Invalid value for `bcws`, must not be `None`")  # noqa: E501
        self._bcws = bcws
    @property
    def bcwp(self):
        """Gets the bcwp of this Resource.  # noqa: E501

        The budgeted cost of a work performed by a resource for the project to-date.  # noqa: E501

        :return: The bcwp of this Resource.  # noqa: E501
        :rtype: float
        """
        return self._bcwp

    @bcwp.setter
    def bcwp(self, bcwp):
        """Sets the bcwp of this Resource.

        The budgeted cost of a work performed by a resource for the project to-date.  # noqa: E501

        :param bcwp: The bcwp of this Resource.  # noqa: E501
        :type: float
        """
        if bcwp is None:
            raise ValueError("Invalid value for `bcwp`, must not be `None`")  # noqa: E501
        self._bcwp = bcwp
    @property
    def is_generic(self):
        """Gets the is_generic of this Resource.  # noqa: E501

        Determines whether a resource is generic.  # noqa: E501

        :return: The is_generic of this Resource.  # noqa: E501
        :rtype: bool
        """
        return self._is_generic

    @is_generic.setter
    def is_generic(self, is_generic):
        """Sets the is_generic of this Resource.

        Determines whether a resource is generic.  # noqa: E501

        :param is_generic: The is_generic of this Resource.  # noqa: E501
        :type: bool
        """
        if is_generic is None:
            raise ValueError("Invalid value for `is_generic`, must not be `None`")  # noqa: E501
        self._is_generic = is_generic
    @property
    def is_inactive(self):
        """Gets the is_inactive of this Resource.  # noqa: E501

        Determines whether a resource is inactive.  # noqa: E501

        :return: The is_inactive of this Resource.  # noqa: E501
        :rtype: bool
        """
        return self._is_inactive

    @is_inactive.setter
    def is_inactive(self, is_inactive):
        """Sets the is_inactive of this Resource.

        Determines whether a resource is inactive.  # noqa: E501

        :param is_inactive: The is_inactive of this Resource.  # noqa: E501
        :type: bool
        """
        if is_inactive is None:
            raise ValueError("Invalid value for `is_inactive`, must not be `None`")  # noqa: E501
        self._is_inactive = is_inactive
    @property
    def is_enterprise(self):
        """Gets the is_enterprise of this Resource.  # noqa: E501

        Determines whether a resource is an Enterprise resource.  # noqa: E501

        :return: The is_enterprise of this Resource.  # noqa: E501
        :rtype: bool
        """
        return self._is_enterprise

    @is_enterprise.setter
    def is_enterprise(self, is_enterprise):
        """Sets the is_enterprise of this Resource.

        Determines whether a resource is an Enterprise resource.  # noqa: E501

        :param is_enterprise: The is_enterprise of this Resource.  # noqa: E501
        :type: bool
        """
        if is_enterprise is None:
            raise ValueError("Invalid value for `is_enterprise`, must not be `None`")  # noqa: E501
        self._is_enterprise = is_enterprise
    @property
    def booking_type(self):
        """Gets the booking_type of this Resource.  # noqa: E501

        The booking type of a resource.  # noqa: E501

        :return: The booking_type of this Resource.  # noqa: E501
        :rtype: BookingType
        """
        return self._booking_type

    @booking_type.setter
    def booking_type(self, booking_type):
        """Sets the booking_type of this Resource.

        The booking type of a resource.  # noqa: E501

        :param booking_type: The booking_type of this Resource.  # noqa: E501
        :type: BookingType
        """
        if booking_type is None:
            raise ValueError("Invalid value for `booking_type`, must not be `None`")  # noqa: E501
        self._booking_type = booking_type
    @property
    def actual_work_protected(self):
        """Gets the actual_work_protected of this Resource.  # noqa: E501

        The duration through which actual work is protected.  # noqa: E501

        :return: The actual_work_protected of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._actual_work_protected

    @actual_work_protected.setter
    def actual_work_protected(self, actual_work_protected):
        """Sets the actual_work_protected of this Resource.

        The duration through which actual work is protected.  # noqa: E501

        :param actual_work_protected: The actual_work_protected of this Resource.  # noqa: E501
        :type: str
        """
        if actual_work_protected is None:
            raise ValueError("Invalid value for `actual_work_protected`, must not be `None`")  # noqa: E501
        self._actual_work_protected = actual_work_protected
    @property
    def actual_overtime_work_protected(self):
        """Gets the actual_overtime_work_protected of this Resource.  # noqa: E501

        The duration through which actual overtime work is protected.  # noqa: E501

        :return: The actual_overtime_work_protected of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._actual_overtime_work_protected

    @actual_overtime_work_protected.setter
    def actual_overtime_work_protected(self, actual_overtime_work_protected):
        """Sets the actual_overtime_work_protected of this Resource.

        The duration through which actual overtime work is protected.  # noqa: E501

        :param actual_overtime_work_protected: The actual_overtime_work_protected of this Resource.  # noqa: E501
        :type: str
        """
        if actual_overtime_work_protected is None:
            raise ValueError("Invalid value for `actual_overtime_work_protected`, must not be `None`")  # noqa: E501
        self._actual_overtime_work_protected = actual_overtime_work_protected
    @property
    def active_directory_guid(self):
        """Gets the active_directory_guid of this Resource.  # noqa: E501

        The Active Directory Guid for a resource.  # noqa: E501

        :return: The active_directory_guid of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._active_directory_guid

    @active_directory_guid.setter
    def active_directory_guid(self, active_directory_guid):
        """Sets the active_directory_guid of this Resource.

        The Active Directory Guid for a resource.  # noqa: E501

        :param active_directory_guid: The active_directory_guid of this Resource.  # noqa: E501
        :type: str
        """
        self._active_directory_guid = active_directory_guid
    @property
    def creation_date(self):
        """Gets the creation_date of this Resource.  # noqa: E501

        The date when a resource was created.  # noqa: E501

        :return: The creation_date of this Resource.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this Resource.

        The date when a resource was created.  # noqa: E501

        :param creation_date: The creation_date of this Resource.  # noqa: E501
        :type: datetime
        """
        if creation_date is None:
            raise ValueError("Invalid value for `creation_date`, must not be `None`")  # noqa: E501
        self._creation_date = creation_date
    @property
    def cost_center(self):
        """Gets the cost_center of this Resource.  # noqa: E501

        Indicates which cost center the costs accrued by the resource should be charged to.  # noqa: E501

        :return: The cost_center of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._cost_center

    @cost_center.setter
    def cost_center(self, cost_center):
        """Sets the cost_center of this Resource.

        Indicates which cost center the costs accrued by the resource should be charged to.  # noqa: E501

        :param cost_center: The cost_center of this Resource.  # noqa: E501
        :type: str
        """
        self._cost_center = cost_center
    @property
    def is_cost_resource(self):
        """Gets the is_cost_resource of this Resource.  # noqa: E501

        Determines whether a resource is a cost resource.  # noqa: E501

        :return: The is_cost_resource of this Resource.  # noqa: E501
        :rtype: bool
        """
        return self._is_cost_resource

    @is_cost_resource.setter
    def is_cost_resource(self, is_cost_resource):
        """Sets the is_cost_resource of this Resource.

        Determines whether a resource is a cost resource.  # noqa: E501

        :param is_cost_resource: The is_cost_resource of this Resource.  # noqa: E501
        :type: bool
        """
        if is_cost_resource is None:
            raise ValueError("Invalid value for `is_cost_resource`, must not be `None`")  # noqa: E501
        self._is_cost_resource = is_cost_resource
    @property
    def team_assignment_pool(self):
        """Gets the team_assignment_pool of this Resource.  # noqa: E501

        Determines whether the current resource is a team resource.               # noqa: E501

        :return: The team_assignment_pool of this Resource.  # noqa: E501
        :rtype: bool
        """
        return self._team_assignment_pool

    @team_assignment_pool.setter
    def team_assignment_pool(self, team_assignment_pool):
        """Sets the team_assignment_pool of this Resource.

        Determines whether the current resource is a team resource.               # noqa: E501

        :param team_assignment_pool: The team_assignment_pool of this Resource.  # noqa: E501
        :type: bool
        """
        if team_assignment_pool is None:
            raise ValueError("Invalid value for `team_assignment_pool`, must not be `None`")  # noqa: E501
        self._team_assignment_pool = team_assignment_pool
    @property
    def assignment_owner(self):
        """Gets the assignment_owner of this Resource.  # noqa: E501

        The name of an assignment owner.  # noqa: E501

        :return: The assignment_owner of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._assignment_owner

    @assignment_owner.setter
    def assignment_owner(self, assignment_owner):
        """Sets the assignment_owner of this Resource.

        The name of an assignment owner.  # noqa: E501

        :param assignment_owner: The assignment_owner of this Resource.  # noqa: E501
        :type: str
        """
        self._assignment_owner = assignment_owner
    @property
    def assignment_owner_guid(self):
        """Gets the assignment_owner_guid of this Resource.  # noqa: E501

        The GUID of an assignment owner.  # noqa: E501

        :return: The assignment_owner_guid of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._assignment_owner_guid

    @assignment_owner_guid.setter
    def assignment_owner_guid(self, assignment_owner_guid):
        """Sets the assignment_owner_guid of this Resource.

        The GUID of an assignment owner.  # noqa: E501

        :param assignment_owner_guid: The assignment_owner_guid of this Resource.  # noqa: E501
        :type: str
        """
        self._assignment_owner_guid = assignment_owner_guid
    @property
    def is_budget(self):
        """Gets the is_budget of this Resource.  # noqa: E501

        Determines whether a resource is a budget resource.  # noqa: E501

        :return: The is_budget of this Resource.  # noqa: E501
        :rtype: bool
        """
        return self._is_budget

    @is_budget.setter
    def is_budget(self, is_budget):
        """Sets the is_budget of this Resource.

        Determines whether a resource is a budget resource.  # noqa: E501

        :param is_budget: The is_budget of this Resource.  # noqa: E501
        :type: bool
        """
        if is_budget is None:
            raise ValueError("Invalid value for `is_budget`, must not be `None`")  # noqa: E501
        self._is_budget = is_budget
    @property
    def budget_work(self):
        """Gets the budget_work of this Resource.  # noqa: E501

        The budget work for a budget work or material resource.  # noqa: E501

        :return: The budget_work of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._budget_work

    @budget_work.setter
    def budget_work(self, budget_work):
        """Sets the budget_work of this Resource.

        The budget work for a budget work or material resource.  # noqa: E501

        :param budget_work: The budget_work of this Resource.  # noqa: E501
        :type: str
        """
        if budget_work is None:
            raise ValueError("Invalid value for `budget_work`, must not be `None`")  # noqa: E501
        self._budget_work = budget_work
    @property
    def budget_cost(self):
        """Gets the budget_cost of this Resource.  # noqa: E501

        The budget cost for a budget cost resource.  # noqa: E501

        :return: The budget_cost of this Resource.  # noqa: E501
        :rtype: float
        """
        return self._budget_cost

    @budget_cost.setter
    def budget_cost(self, budget_cost):
        """Sets the budget_cost of this Resource.

        The budget cost for a budget cost resource.  # noqa: E501

        :param budget_cost: The budget_cost of this Resource.  # noqa: E501
        :type: float
        """
        if budget_cost is None:
            raise ValueError("Invalid value for `budget_cost`, must not be `None`")  # noqa: E501
        self._budget_cost = budget_cost
    @property
    def overtime_rate(self):
        """Gets the overtime_rate of this Resource.  # noqa: E501

        The overtime rate of a resource. This value retrieved from the current date if a rate table exists for a resource.  # noqa: E501

        :return: The overtime_rate of this Resource.  # noqa: E501
        :rtype: float
        """
        return self._overtime_rate

    @overtime_rate.setter
    def overtime_rate(self, overtime_rate):
        """Sets the overtime_rate of this Resource.

        The overtime rate of a resource. This value retrieved from the current date if a rate table exists for a resource.  # noqa: E501

        :param overtime_rate: The overtime_rate of this Resource.  # noqa: E501
        :type: float
        """
        if overtime_rate is None:
            raise ValueError("Invalid value for `overtime_rate`, must not be `None`")  # noqa: E501
        self._overtime_rate = overtime_rate
    @property
    def baselines(self):
        """Gets the baselines of this Resource.  # noqa: E501

        Gets or sets the collection of baseline values of the resource.  # noqa: E501

        :return: The baselines of this Resource.  # noqa: E501
        :rtype: list[Baseline]
        """
        return self._baselines

    @baselines.setter
    def baselines(self, baselines):
        """Sets the baselines of this Resource.

        Gets or sets the collection of baseline values of the resource.  # noqa: E501

        :param baselines: The baselines of this Resource.  # noqa: E501
        :type: list[Baseline]
        """
        self._baselines = baselines
    @property
    def extended_attributes(self):
        """Gets the extended_attributes of this Resource.  # noqa: E501

        Resource extended attributes.  # noqa: E501

        :return: The extended_attributes of this Resource.  # noqa: E501
        :rtype: list[ExtendedAttribute]
        """
        return self._extended_attributes

    @extended_attributes.setter
    def extended_attributes(self, extended_attributes):
        """Sets the extended_attributes of this Resource.

        Resource extended attributes.  # noqa: E501

        :param extended_attributes: The extended_attributes of this Resource.  # noqa: E501
        :type: list[ExtendedAttribute]
        """
        self._extended_attributes = extended_attributes
    @property
    def outline_codes(self):
        """Gets the outline_codes of this Resource.  # noqa: E501

        Resource outline codes.  # noqa: E501

        :return: The outline_codes of this Resource.  # noqa: E501
        :rtype: list[OutlineCode]
        """
        return self._outline_codes

    @outline_codes.setter
    def outline_codes(self, outline_codes):
        """Sets the outline_codes of this Resource.

        Resource outline codes.  # noqa: E501

        :param outline_codes: The outline_codes of this Resource.  # noqa: E501
        :type: list[OutlineCode]
        """
        self._outline_codes = outline_codes
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
        if not isinstance(other, Resource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
