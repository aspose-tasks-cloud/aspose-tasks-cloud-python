# ExtendedAttributeDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_id** | **str** | Corresponds to the Pid of a custom field. | [optional] 
**field_name** | **str** | The name of a custom field. | [optional] 
**cf_type** | [**CustomFieldType**](CustomFieldType.md) | The type of a custom field. | 
**guid** | **str** | The Guid of a custom field. | [optional] 
**element_type** | [**ElementType**](ElementType.md) | Determines whether the extended attribute is associated with a task or a resource | 
**max_multi_values** | **int** | The maximum number of values you can set in a picklist. | 
**user_def** | **bool** | Determines whether a custom field is user defined. | 
**alias** | **str** | The alias of a custom field. | [optional] 
**secondary_pid** | **str** | The secondary Pid of a custom field. | [optional] 
**auto_roll_down** | **bool** | Determines whether an automatic rolldown to assignments is enabled. | 
**default_guid** | **str** | The Guid of the default lookup table entry. | [optional] 
**lookup_uid** | **str** | The Guid of the lookup table associated with a custom field. | [optional] 
**phonetics_alias** | **str** | The phonetic pronunciation of the alias of a custom field. | [optional] 
**rollup_type** | [**RollupType**](RollupType.md) | The way rollups are calculated. | 
**calculation_type** | [**CalculationType**](CalculationType.md) | Determines whether rollups are calculated for a task and group summary rows. | 
**formula** | **str** | The formula that Microsoft Project uses to populate a custom task field. | [optional] 
**restrict_values** | **bool** | Determines whether only values in the list are allowed in a file. | 
**valuelist_sort_order** | **int** | The way value lists are sorted. Values are: 0&#x3D;Descending, 1&#x3D;Ascending. | 
**append_new_values** | **bool** | Determines whether new values added to a project are automatically added to the list. | 
**default** | **str** | The default value in the list. | [optional] 
**value_list** | [**list[Value]**](Value.md) | Returns list of Extended Attribute Values. | [optional] 
**secondary_guid** | **str** | Secondary guid of extended attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


