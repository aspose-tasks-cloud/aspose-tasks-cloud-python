# ResourceAssignment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_uid** | **int** | Returns or sets a task unique id to which a resource is assigned. | [default to -1]
**resource_uid** | **int** | Returns or sets a resource unique id assigned to a task. | [default to -1]
**guid** | **str** | Returns or sets the global unique identifier of an assignment. | [optional] 
**uid** | **int** | Returns or sets the unique identifier of an assignment. | 
**percent_work_complete** | **int** | Returns or sets the amount of a work completed on an assignment. | 
**actual_cost** | **float** | Returns or sets the actual cost incurred on an assignment. | 
**actual_finish** | **datetime** | Returns or sets the actual finish date of an assignment. | 
**actual_overtime_cost** | **float** | Returns or sets the actual overtime cost incurred on an assignment. | 
**actual_overtime_work** | **str** | Returns or sets the actual amount of an overtime work incurred on an assignment. | 
**actual_start** | **datetime** | Returns or sets the actual start date of an assignment. | 
**actual_work** | **str** | Returns or sets the actual amount of a work incurred on an assignment. | 
**acwp** | **float** | Returns or sets the actual cost of a work performed on an assignment to-date. | 
**confirmed** | **bool** | Determines whether a resource has accepted all of its assignments. | 
**cost** | **float** | Returns or sets the projected or scheduled cost of an assignment. | 
**cost_rate_table_type** | [**RateType**](RateType.md) | Returns or sets the cost rate table used for this assignment. | 
**cost_variance** | **float** | Returns or sets the difference between the cost and baseline cost of a resource. | 
**cv** | **float** | Returns or sets the earned value cost variance. | 
**delay** | **int** | Returns or sets the delay of an assignment. | 
**finish** | **datetime** | Returns or sets the scheduled finish date of an assignment. | 
**finish_variance** | **int** | Returns or sets the variance of an assignment finish date from a baseline finish date. | 
**hyperlink** | **str** | Returns or sets the title of the hyperlink associated with an assignment. | [optional] 
**hyperlink_address** | **str** | Returns or sets the hyperlink associated with an assignment. | [optional] 
**hyperlink_sub_address** | **str** | Returns or sets the document bookmark of the hyperlink associated with an assignment. | [optional] 
**work_variance** | **float** | Returns or sets the variance of an assignment work from the baseline work as minutes. | 
**has_fixed_rate_units** | **bool** | Determines whether the Units have Fixed Rate. | 
**fixed_material** | **bool** | Determines whether the consumption of an assigned material resource occurs in a single, fixed amount. | 
**leveling_delay** | **int** | Returns or sets the delay caused by leveling. | 
**leveling_delay_format** | [**TimeUnitType**](TimeUnitType.md) | Returns or sets the duration format of a delay. | 
**linked_fields** | **bool** | Determines whether the Project is linked to another OLE object. | 
**milestone** | **bool** | Determines whether the assignment is a milestone. | 
**notes** | **str** | Returns or sets the text notes associated with an assignment. | [optional] 
**overallocated** | **bool** | Determines whether the assignment is overallocated. | 
**overtime_cost** | **float** | Returns or sets the sum of the actual and remaining overtime cost of an assignment. | 
**overtime_work** | **str** | Returns or sets the scheduled overtime work of an assignment. | 
**peak_units** | **float** | Returns or sets the largest number of a resource&#39;s units assigned to a task. | 
**regular_work** | **str** | Returns or sets the amount of a non-overtime work scheduled for an assignment. | 
**remaining_cost** | **float** | Returns or sets the remaining projected cost of completing an assignment. | 
**remaining_overtime_cost** | **float** | Returns or sets the remaining projected overtime cost of completing an assignment. | 
**remaining_overtime_work** | **str** | Returns or sets the remaining overtime work scheduled to complete an assignment. | 
**remaining_work** | **str** | Returns or sets the remaining work scheduled to complete an assignment. | 
**response_pending** | **bool** | Determines whether the response has been received for a TeamAssign message. | 
**start** | **datetime** | Returns or sets the scheduled start date of an assignment. | 
**stop** | **datetime** | Returns or sets the date when assignment is stopped. | 
**resume** | **datetime** | Returns or sets the date when assignment is resumed. | 
**start_variance** | **int** | Returns or sets the variance of an assignment start date from a baseline start date. | 
**summary** | **bool** | Determines whether the task is a summary task. | 
**sv** | **float** | Returns or sets the earned value schedule variance, through the project status date. | 
**units** | **float** | Returns or sets the number of units for an assignment. | [default to 1.0]
**update_needed** | **bool** | Determines whether the resource assigned to a task needs to be updated as to the status of the task. | 
**vac** | **float** | Returns or sets the difference between basline cost and total cost. Read/write Double. | 
**work** | **str** | Returns or sets the amount of scheduled work for an assignment. Read/write TimeSpan. | 
**work_contour** | [**WorkContourType**](WorkContourType.md) | Returns or sets the work contour of an assignment. | 
**bcws** | **float** | Returns or sets the budgeted cost of a work on assignment. | 
**bcwp** | **float** | Returns or sets the budgeted cost of a work performed on assignment to-date. | 
**booking_type** | [**BookingType**](BookingType.md) | Returns or sets the booking type of an assignment. | 
**actual_work_protected** | **str** | Returns or sets the duration through which actual work is protected. | 
**actual_overtime_work_protected** | **str** | Returns or sets the duration through which actual overtime work is protected. | 
**creation_date** | **datetime** | Returns or sets the date that the assignment was created. | 
**assn_owner** | **str** | Returns or sets the name of an assignment owner. | [optional] 
**assn_owner_guid** | **str** | Returns or sets the Guid of an assignment owner. | [optional] 
**budget_cost** | **float** | Returns or sets the budgeted cost of resources on an assignment. | 
**budget_work** | **str** | Returns or sets the budgeted work amount for a work or material resources on an assignment. | 
**rate_scale** | [**RateScaleType**](RateScaleType.md) | Returns the time unit for the usage rate of the material resource assignment. | 
**baselines** | [**list[AssignmentBaseline]**](AssignmentBaseline.md) | List of ResourceAssignment&#39;s Baseline values. | [optional] 
**extended_attributes** | [**list[ExtendedAttribute]**](ExtendedAttribute.md) | ResourceAssignment extended attributes. | [optional] 
**timephased_data** | [**list[TimephasedData]**](TimephasedData.md) | Represents a collection of TimephasedData objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


