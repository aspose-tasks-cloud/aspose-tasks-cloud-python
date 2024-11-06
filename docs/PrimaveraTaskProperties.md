# PrimaveraTaskProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sequence_number** | **int** | The sequence number of the WBS item (summary tasks). It is used to sort summary tasks in Primavera. | 
**activity_id** | **str** | Activity id field - a task&#39;s unique identifier used by Primavera. | [optional] 
**remaining_early_finish** | **datetime** | Remaining early finish date - the date when the remaining work for the activity is scheduled to be finished. | 
**remaining_early_start** | **datetime** | Remaining early start date - the date when the remaining work for the activity is scheduled to begin. | 
**remaining_late_start** | **datetime** | Remaining late start date. | 
**remaining_late_finish** | **datetime** | Remaining late finish date. | 
**raw_duration_type** | **str** | Raw text representation (as in source file) of &#39;Duration Type&#39; field of the activity. | [optional] 
**raw_activity_type** | **str** | Raw text representation (as in source file) of &#39;Activity Type&#39; field of the activity. | [optional] 
**raw_complete_percent_type** | **str** | Raw text representation (as in source file) of &#39;% Complete Type&#39; field of the activity. | [optional] 
**raw_status** | **str** | Raw text representation (as in source file) of &#39;Status&#39; field of the activity. | [optional] 
**duration_percent_complete** | **float** | Gets the value of duration percent complete. | 
**physical_percent_complete** | **float** | Gets the value of Physical Percent Complete. | 
**actual_non_labor_units** | **float** | Gets the value of actual non labor units. | 
**actual_labor_units** | **float** | Gets the value of actual labor units. | 
**units_percent_complete** | **float** | Gets the value of units percent complete. | 
**remaining_labor_units** | **float** | Gets the value of remaining labor units. | 
**remaining_non_labor_units** | **float** | Gets the value of remaining non labor units. | 
**duration_type** | [**PrimaveraDurationType**](PrimaveraDurationType.md) | Gets the value of &#39;Duration Type&#39; field of the activity. | 
**activity_type** | [**PrimaveraActivityType**](PrimaveraActivityType.md) | Gets the value of &#39;Activity Type&#39; field. | 
**percent_complete_type** | [**PrimaveraPercentCompleteType**](PrimaveraPercentCompleteType.md) | Gets the value of &#39;% Complete Type&#39; field of the activity. | 
**actual_labor_cost** | **float** | Gets the value of actual labor cost. | 
**actual_nonlabor_cost** | **float** | Gets the value of actual non labor cost. | 
**actual_material_cost** | **float** | Gets the value of actual material cost.              | 
**actual_expense_cost** | **float** | Gets the value of actual expense cost. | 
**remaining_expense_cost** | **float** | Gets the value of remaining expense cost. | 
**actual_total_cost** | **float** | Gets the total value of actual costs. | 
**budgeted_total_cost** | **float** | Gets the total value of budgeted (or planned) costs. | 
**budgeted_labor_cost** | **float** | Gets the value of budgeted (or planned) labor cost. | 
**budgeted_nonlabor_cost** | **float** | Gets the value of budgeted (or planned) non labor cost. | 
**budgeted_material_cost** | **float** | Gets the value of of budgeted (or planned) material cost. | 
**budgeted_expense_cost** | **float** | Gets the value of budgeted (or planned) expense cost. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


