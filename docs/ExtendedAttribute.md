# ExtendedAttribute

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_id** | **str** | Gets or sets the id of a field. | [optional] 
**attribute_type** | [**CustomFieldType**](CustomFieldType.md) | Gets the type of a custom field. | 
**value_guid** | **str** | Gets or sets the guid of a value. | [optional] 
**lookup_value_id** | **int** | Gets or sets Id of the lookup value (if value is lookup value) | [optional] 
**duration_value** | [**Duration**](Duration.md) | Gets or sets value for attributes with &#39;Duration&#39; type. | [optional] 
**numeric_value** | **float** | Gets or sets a value for attributes with numeric types (Cost, Number). | 
**date_value** | **datetime** | Gets or sets a value for attributes with date types (Date, Start, Finish). | 
**flag_value** | **bool** | Gets or sets a value indicating whether a flag is set for an attribute with &#39;Flag&#39; type. | 
**text_value** | **str** | Gets or sets a value for attributes with &#39;Text&#39; type. | [optional] 
**is_error_value** | **bool** | Gets whether calculation of extended attribute&#39;s value resulted in an error.              | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


