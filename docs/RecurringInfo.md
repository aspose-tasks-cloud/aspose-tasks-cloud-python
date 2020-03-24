# RecurringInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recurrence_pattern** | [**RecurrencePattern**](RecurrencePattern.md) | Represents a recurrence pattern of the recurring task. Can be one of the values of  enum. | 
**start_date** | **datetime** | Specifies the date for the occurrences to begin. | 
**end_date** | **datetime** | Specifies the date for the occurrences to end. | 
**duration** | **str** | Specifies the duration for one occurrence of the recurring task. the instance of  class. | 
**occurrences** | **int** | Specifies a number of occurrences of the recurring task. | 
**use_end_date** | **bool** | Determines whether to use the end date or a number of occurrences for the recurring task. | 
**daily_repetitions** | **int** | Specifies an interval between repetitions for the daily recurrence pattern. | 
**daily_use_workdays** | **bool** | Determines whether to use workdays for the daily recurrence pattern. | 
**weekly_repetitions** | **int** | Specifies an interval between repetitions for the weekly recurrence pattern. | 
**weekly_days** | [**WeekDayType**](WeekDayType.md) | Specifies a collection of days used in the weekly recurrence pattern. | 
**monthly_use_ordinal_day** | **bool** | Determines whether to use ordinal day for the monthly recurrence pattern. | 
**monthly_ordinal_number** | [**OrdinalNumber**](OrdinalNumber.md) | Specifies an ordinal number of the monthly recurrence pattern. Can be one of the values of  enum. | 
**monthly_ordinal_day** | [**DayOfWeek**](DayOfWeek.md) | Specifies a day of the monthly recurrence pattern when using ordinal day. Can be one of the values of  enum. | 
**monthly_ordinal_repetitions** | **int** | Specifies a number of repetitions for the monthly recurrence pattern when using ordinal day. | 
**monthly_day** | **int** | Specifies a number of day of the monthly recurrence pattern. | 
**monthly_repetitions** | **int** | Specifies a number of repetitions for the monthly recurrence pattern. | 
**yearly_use_ordinal_day** | **bool** | Determines whether to use ordinal day for the yearly recurrence pattern. | 
**yearly_date** | **datetime** | Specifies a date for the yearly recurrence pattern. | 
**yearly_ordinal_number** | [**OrdinalNumber**](OrdinalNumber.md) | Specifies an ordinal number of the yearly recurrence pattern. Can be one of the values of  enum. | 
**yearly_ordinal_day** | [**DayOfWeek**](DayOfWeek.md) | Specifies a weekday of the yearly recurrence pattern when using ordinal day. Can be one of the values of  enum. | 
**yearly_ordinal_month** | [**Month**](Month.md) | Specifies a month of the yearly recurrence pattern when using ordinal day. Can be one of the values of  enum. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


