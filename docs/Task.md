# Task

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **int** | The unique id of a task. | 
**id** | **int** | The position of a task in collection. | 
**name** | **str** | The name of a task. | [optional] 
**duration_text** | **str** | The duration of a task entered by the user as a text. | [optional] 
**duration** | **str** | The duration of a task. | 
**start** | **datetime** | The start date of a task. | 
**finish** | **datetime** | The finish date of a task. | 
**start_text** | **str** | Returns the task&#39;s start text. | [optional] 
**finish_text** | **str** | Returns the task&#39;s finish text. | [optional] 
**percent_complete** | **int** | The percent complete of a task. | 
**percent_work_complete** | **int** | The percent work complete of a task. | 
**is_active** | **bool** | Determines if a task is active. | [default to True]
**actual_cost** | **float** | The actual cost of a task. | 
**actual_duration** | **str** | The actual duration of a task. | 
**actual_finish** | **datetime** | The actual finish date of a task. | 
**actual_overtime_cost** | **float** | The actual overtime cost of a task. | 
**actual_overtime_work** | **str** | The actual overtime work of a task. | 
**actual_work_protected** | **str** | The duration through which actual work is protected. Reading supported for XML format only. | 
**actual_overtime_work_protected** | **str** | The duration through which actual overtime work is protected. Reading supported for XML format only. | 
**actual_start** | **datetime** | The actual start date of a task. | 
**budget_work** | **str** | The amount of budgeted work for a project root task. | 
**budget_cost** | **float** | The amount of budgeted cost for a project root task. | 
**constraint_date** | **datetime** | Shows the specific date associated with certain constraint types,  such as Must Start On, Must Finish On, Start No Earlier Than, Start No Later Than, Finish No Earlier Than, and Finish No Later Than. | 
**constraint_type** | [**ConstraintType**](ConstraintType.md) | Provides choices for the type of constraint that can be applied for scheduling a task. | 
**contact** | **str** | The contact person for a task. | [optional] 
**cost** | **float** | The projected or scheduled cost of a task. | 
**outline_number** | **str** | Gets or sets a value of OutlineNumber. | [optional] 
**cv** | **float** | The difference between the baseline cost and total cost for a task. | 
**deadline** | **datetime** | The deadline for a task to be completed. | 
**duration_variance** | **str** | Contains the difference between the total duration of a task and the baseline duration of a task. | 
**early_finish** | **datetime** | The early finish date of a task. | 
**early_start** | **datetime** | The early start date of a task. | 
**is_effort_driven** | **bool** | Determines whether a task is effort-driven. | 
**is_external_task** | **bool** | Determines whether a task is external. | 
**external_task_project** | **str** | The source location and task identifier of an external task. | [optional] 
**external_id** | **int** | If a task is an external task the property contains the task&#39;s external Id.  type. | 
**finish_slack** | **int** | Contains the duration between the Early Finish and Late Finish dates. | 
**finish_variance** | **int** | The variance of the task finish date from the baseline finish date as minutes. | 
**fixed_cost** | **float** | The fixed cost of a task. | 
**fixed_cost_accrual** | [**CostAccrualType**](CostAccrualType.md) | Determines how the fixed cost is accrued against a task. | 
**free_slack** | **int** | The amount of a free slack. | 
**guid** | **str** |  | [optional] 
**has_overallocated_resource** | **bool** | Indicates whether the task has an resource assigned which has more work on assigned tasks than can be completed within normal working capacity. | 
**hide_bar** | **bool** | Determines whether the GANTT bar of a task is hidden when displayed in Microsoft Project. | 
**ignore_resource_calendar** | **bool** | Determines whether a task ignores the resource calendar. | 
**late_finish** | **datetime** | The late finish date of a task. | 
**late_start** | **datetime** | The late start date of a task. | 
**is_level_assignments** | **bool** |  | [default to True]
**can_leveling_split** | **bool** |  | [default to True]
**leveling_delay** | **int** | The delay caused by leveling a task. | 
**is_marked** | **bool** | Shows whether a task is marked for further action or identification of some kind.              | 
**is_milestone** | **bool** | Determines whether a task is a milestone. | 
**is_critical** | **bool** | Determines whether a task is in the critical chain. | 
**is_subproject** | **bool** | Determines whether a task is an inserted project. | 
**is_subproject_read_only** | **bool** | Determines whether a subproject is read-only. | 
**subproject_name** | **str** | The source location of a subproject. Read/write String. | [optional] 
**is_summary** | **bool** | Determines whether a task is a summary task. | 
**subtasks_uids** | **list[int]** | Unique ids of all subtasks. | [optional] 
**outline_level** | **int** | The outline level of a task. | 
**is_over_allocated** | **bool** |  | 
**is_estimated** | **bool** | Determines whether a task is estimated. | 
**overtime_cost** | **float** | The sum of an actual and remaining overtime cost of a task. | 
**overtime_work** | **str** | The amount of an overtime work scheduled for a task. | 
**physical_percent_complete** | **int** | The percentage complete value entered by the Project Manager. | 
**pre_leveled_finish** | **datetime** |  | 
**pre_leveled_start** | **datetime** |  | 
**is_recurring** | **bool** | Determines whether a task is a recurring task. | 
**regular_work** | **str** | The amount of non-overtime work scheduled for a task. | 
**remaining_cost** | **float** | The remaining projected cost of completing a task. | 
**remaining_duration** | **str** | The amount of time required to complete the unfinished portion of a task. | 
**remaining_overtime_cost** | **float** | The remaining overtime cost projected to finish a task. | 
**remaining_overtime_work** | **str** | The remaining overtime work scheduled to finish a task. | 
**remaining_work** | **str** | The remaining work scheduled to complete a task. | 
**resume** | **datetime** | The date when a task resumed. | 
**is_resume_valid** | **bool** | Determines whether a task can be resumed. | [optional] 
**stop** | **datetime** | The date that represents the end of the actual portion of a task. | 
**is_rollup** | **bool** | Determines whether a task is rolled up. | 
**start_slack** | **int** | Returns the task&#39;s start slack. | 
**start_variance** | **int** | The variance of the task start date from the baseline start date as minutes.  | 
**calendar_uid** | **int** | The unique id of task calendar. | [default to -1]
**is_manual** | **bool** | Determines whether a task is manually scheduled. | 
**manual_start** | **datetime** | Defines manually scheduled start of a task. | 
**manual_finish** | **datetime** | Defines manually scheduled finish of a task. | 
**manual_duration** | **str** | Defines manually scheduled duration of a task. | 
**total_slack** | **int** | The amount of a total slack. | 
**type** | [**TaskType**](TaskType.md) | The type of a task. | 
**wbs** | **str** | The work breakdown structure code of a task. | [optional] 
**priority** | **int** | The priority of a task from 0 to 1000. | 
**work** | **str** | The amount of the scheduled work for a task. | 
**work_variance** | **float** | The variance of the task work from the baseline task work as minutes. | 
**notes_text** | **str** | Notes&#39; plain text extracted from RTF data. | [optional] 
**notes_rtf** | **str** | The text notes in RTF format. | [optional] 
**acwp** | **float** |  | 
**bcws** | **float** |  | 
**bcwp** | **float** |  | 
**leveling_delay_format** | [**TimeUnitType**](TimeUnitType.md) | LevelingDelayFormat | 
**predecessors** | **str** | The task Uid numbers for the predecessor tasks on which the task depends before it can be started or finished. | [optional] 
**successors** | **str** | The task Uid numbers for the successor tasks to a task. | [optional] 
**ignore_warnings** | **bool** | Indicates whether to hide the schedule conflict warning indicator in Microsoft Project.              | [default to False]
**is_expanded** | **bool** | Determines whether a summary task is expanded or not in GanttChart view. | 
**display_on_timeline** | **bool** | Specifies whether a task should be displayed on a timeline view. | 
**display_as_summary** | **bool** | Determines whether the task should be displayed as a summary task. Reading supported for XML format only. | 
**hyperlink** | **str** | The title or explanatory text for a hyperlink associated with a task. | [optional] 
**hyperlink_address** | **str** | The address for a hyperlink associated with a task. | [optional] 
**hyperlink_sub_address** | **str** | The specific location in a document in a hyperlink associated with a task.  type. | [optional] 
**earned_value_method** | [**EarnedValueMethodType**](EarnedValueMethodType.md) | Determines whether the % Complete or Physical % Complete field should be used to calculate budgeted cost of work performed (BCWP). | 
**is_published** | **bool** | Determines whether the current task should be published to Project Server with the rest of the project. | [default to True]
**status_manager** | **str** | The name of the enterprise resource who is to receive status updates for the current task from resources. | [optional] 
**commitment_start** | **datetime** | The start date of a delivery. Reading supported for XML format only. | 
**commitment_finish** | **datetime** | The finish date of a delivery. Reading supported for XML format only. | 
**commitment_type** | **int** | Determines whether a task has an associated delivery or a dependency on an associated delivery. Reading supported for XML format only. | 
**baselines** | [**list[TaskBaseline]**](TaskBaseline.md) | Gets or sets the collection of baseline values of the task. | [optional] 
**extended_attributes** | [**list[ExtendedAttribute]**](ExtendedAttribute.md) | Task extended attributes. | [optional] 
**outline_codes** | [**list[OutlineCode]**](OutlineCode.md) | Task outline codes. | [optional] 
**warning** | **bool** | Represents the flag which indicates that task has schedule discrepancies. | [default to False]
**activity_id** | **str** | Represents activity id field - a task&#39;s unique identifier used by Primavera (only applicable to Primavera projects). | [optional] 
**external_uid** | **int** | Contains the external task&#39;s Unique identifier when the task is external. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


