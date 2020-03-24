# OutlineCodeDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The Guid of an outline code. | [optional] 
**field_id** | **str** | Corresponds to the field number of an outline code. | [optional] 
**field_name** | **str** | The name of a custom outline code. | [optional] 
**alias** | **str** | The alias of a custom outline code. | [optional] 
**phonetic_alias** | **str** | The phonetic pronunciation of the alias of the custom outline code. | [optional] 
**values** | [**list[OutlineValue]**](OutlineValue.md) | Returns List&amp;lt;OutlineValue&amp;gt; Values. The values of the table associated with this outline code. | [optional] 
**enterprise** | **bool** | Determines whether a custom outline code is an enterprise custom outline code. | 
**enterprise_outline_code_alias** | **int** | The reference to another custom field for which this outline code definition is an alias. | 
**resource_substitution_enabled** | **bool** | Determines whether the custom outline code can be used by the Resource Substitution Wizard in Microsoft Project. | 
**leaf_only** | **bool** | Determines whether the values specified in this outline code field must be leaf values. | 
**all_levels_required** | **bool** | Determines whether the new codes must have all levels. Not available for Enterprise Codes. | 
**only_table_values_allowed** | **bool** | Determines whether the values specified must come from values table. | 
**masks** | [**list[OutlineMask]**](OutlineMask.md) | Returns List&amp;lt;OutlineMask&amp;gt; Masks. The table of entries that define the outline code mask. | [optional] 
**show_indent** | **bool** | Determines whether the indents of this outline code must be shown. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


