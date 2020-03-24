# Resource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of a resource. | [optional] 
**uid** | **int** | The unique identifier of a resource. | 
**id** | **int** | The position identifier of a resource within the list of resources. | 
**guid** | **str** | Contains the generated unique identification code for the resource.              | [optional] 
**type** | [**ResourceType**](ResourceType.md) | The type of a resource. | 
**is_null** | **bool** | Determines whether a resource is null. | 
**initials** | **str** | The initials of a resource. | [optional] 
**phonetics** | **str** | The phonetic spelling of the resource name. For use with Japanese only. | [optional] 
**nt_account** | **str** | The NT account associated with a resource. | [optional] 
**windows_user_account** | **str** | The NT account associated with a resource. | [optional] 
**workgroup** | [**WorkGroupType**](WorkGroupType.md) | The type of a workgroup to which a resource belongs.  type. | 
**material_label** | **str** | The unit of measure for the material resource. Read/write String. | [optional] 
**code** | **str** | The code or other information about a resource. | [optional] 
**group** | **str** | The group to which a resource belongs. | [optional] 
**email_address** | **str** |  | [optional] 
**hyperlink** | **str** | The title of a hyperlink associated with a resource. | [optional] 
**hyperlink_address** | **str** | The hyperlink associated with a resource. | [optional] 
**hyperlink_sub_address** | **str** | The document bookmark of a hyperlink associated with a resource. Read/write String. | [optional] 
**max_units** | **float** | The maximum number of units of a resource is available. | [default to 1.0]
**peak_units** | **float** | The largest number of units assigned to a resource at any time. | 
**over_allocated** | **bool** |  | 
**available_from** | **datetime** | The first date when a resource is available. | 
**available_to** | **datetime** | The last date when a resource is available. | 
**start** | **datetime** | The scheduled start date of a resource. | 
**finish** | **datetime** | The scheduled finish date of a resource. | 
**can_level** | **bool** | Determines whether a resource can be leveled. | [default to True]
**accrue_at** | [**CostAccrualType**](CostAccrualType.md) | Determines how cost is accrued against the resource. | 
**work** | **str** | The total work assigned to a resource across all assigned tasks. | 
**regular_work** | **str** | The amount of non-overtime work assigned to a resource. | 
**overtime_work** | **str** | The amount of overtime work assigned to a resource. | 
**actual_work** | **str** | The amount of actual work performed by a resource. | 
**remaining_work** | **str** | The amount of remaining work required to complete all assigned tasks. | 
**actual_overtime_work** | **str** | The amount of actual overtime work performed by a resource. | 
**remaining_overtime_work** | **str** | The amount of remaining overtime work required to complete all tasks. | 
**percent_work_complete** | **int** | The percentage of work completed across all tasks. | 
**standard_rate** | **float** | The standard rate of a resource. This value retrieved from the current date if a rate table exists for a resource. | 
**standard_rate_format** | [**RateFormatType**](RateFormatType.md) | The units used by Microsoft Project to display the standard rate. | 
**cost** | **float** | The total project cost for a resource across all assigned tasks. | 
**overtime_rate_format** | [**RateFormatType**](RateFormatType.md) | The units used by Microsoft Project to display the overtime rate. | 
**overtime_cost** | **float** | The total overtime cost of a resource including actual and remaining overtime costs. | 
**cost_per_use** | **float** | The cost per use of a resource. This value retrieved from the current date if a rate table exists for the resource. | 
**actual_cost** | **float** | The actual cost incurred by the resource across all assigned tasks. | 
**actual_overtime_cost** | **float** | The actual overtime cost incurred by the resource across all assigned tasks. | 
**remaining_cost** | **float** | The remaining projected cost of a resource to complete all assigned tasks. | 
**remaining_overtime_cost** | **float** | The remaining projected overtime cost of a resource to complete all assigned tasks. | 
**work_variance** | **float** | The difference between a baseline work and a work | 
**cost_variance** | **float** | The difference between a baseline cost and a cost. | 
**sv** | **float** | The earned value schedule variance, through the project status date. | 
**cv** | **float** | The earned value cost variance, through the project status date. | 
**acwp** | **float** | The actual cost of a work performed by a resource for the project to-date. | 
**calendar_uid** | **int** | The calendar of a resource. | 
**notes_text** | **str** | Notes&#39; plain text extracted from RTF data. | [optional] 
**notes** | **str** | The text notes associated with a resource. | [optional] 
**notes_rtf** | **str** | The text notes in RTF format. Supported for MPP formats only. | [optional] 
**bcws** | **float** | The budget cost of a work scheduled for a resource. | 
**bcwp** | **float** | The budgeted cost of a work performed by a resource for the project to-date. | 
**is_generic** | **bool** | Determines whether a resource is generic. | 
**is_inactive** | **bool** | Determines whether a resource is inactive. | 
**is_enterprise** | **bool** | Determines whether a resource is an Enterprise resource. | 
**booking_type** | [**BookingType**](BookingType.md) | The booking type of a resource. | 
**actual_work_protected** | **str** | The duration through which actual work is protected. | 
**actual_overtime_work_protected** | **str** | The duration through which actual overtime work is protected. | 
**active_directory_guid** | **str** | The Active Directory Guid for a resource. | [optional] 
**creation_date** | **datetime** | The date when a resource was created. | 
**cost_center** | **str** | Indicates which cost center the costs accrued by the resource should be charged to. | [optional] 
**is_cost_resource** | **bool** | Determines whether a resource is a cost resource. | 
**team_assignment_pool** | **bool** | Determines whether the current resource is a team resource.              | 
**assignment_owner** | **str** | The name of an assignment owner. | [optional] 
**assignment_owner_guid** | **str** | The GUID of an assignment owner. | [optional] 
**is_budget** | **bool** | Determines whether a resource is a budget resource. | 
**budget_work** | **str** | The budget work for a budget work or material resource. | 
**budget_cost** | **float** | The budget cost for a budget cost resource. | 
**overtime_rate** | **float** | The overtime rate of a resource. This value retrieved from the current date if a rate table exists for a resource. | 
**baselines** | [**list[Baseline]**](Baseline.md) | Gets or sets the collection of baseline values of the resource. | [optional] 
**extended_attributes** | [**list[ExtendedAttribute]**](ExtendedAttribute.md) | Resource extended attributes. | [optional] 
**outline_codes** | [**list[OutlineCode]**](OutlineCode.md) | Resource outline codes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


