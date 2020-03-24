# CalendarException

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Index of the current item in the collection of calendar&#39;s exceptions. | 
**entered_by_occurrences** | **bool** | Determines whether the range of recurrence is defined by entering a number of occurrences. False specifies that the range of recurrence is defined by entering a finish date. | 
**from_date** | **datetime** | The beginning of the exception time. | 
**to_date** | **datetime** | The end of the exception time. | 
**occurrences** | **int** | The number of occurrences for which the calendar exception is valid. | 
**name** | **str** | The name of the exception. | [optional] 
**type** | [**CalendarExceptionType**](CalendarExceptionType.md) | The exception type. | 
**period** | **int** | The period of recurrence for the exception. | 
**days_of_week** | [**list[DayType]**](DayType.md) | The days of the week on which the exception is valid. | [optional] 
**month_item** | [**MonthItemType**](MonthItemType.md) | The month item for which an exception recurrence is scheduled. | 
**month_position** | [**MonthPosition**](MonthPosition.md) | The position of a month item within a month. | 
**month** | [**Month**](Month.md) | The month for which an exception recurrence is scheduled. | 
**month_day** | **int** | The day of a month on which an exception recurrence is scheduled. | 
**day_working** | **bool** | Determines whether the specified date or day type is working. | 
**working_times** | [**list[WorkingTime]**](WorkingTime.md) | The collection of working times that defines the time worked on the weekday.  At least one working time must present, and there can&#39;t be more than five. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


