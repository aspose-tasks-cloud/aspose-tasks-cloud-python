# Calendar

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Gets calendar&#39;s Guid. | [optional] 
**name** | **str** | The name of the calendar. | [optional] 
**uid** | **int** | The unique identifier of the calendar. | 
**days** | [**list[WeekDay]**](WeekDay.md) | The collection of weekdays that defines the calendar. | [optional] 
**is_base_calendar** | **bool** | Determines whether the calendar is a base calendar. | 
**base_calendar** | [**Calendar**](Calendar.md) | The base calendar on which this calendar depends. Only applicable if the calendar is not a base calendar. | [optional] 
**is_baseline_calendar** | **bool** | Specifies whether the calendar is a baseline calendar. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


