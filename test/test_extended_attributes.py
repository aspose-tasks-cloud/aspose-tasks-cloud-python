#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_extended_attributes.py">
#   Copyright (c) 2020 Aspose.Tasks Cloud
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# --------------------------------------------------------------------------------------------------------------------
#
from datetime import datetime
from asposetaskscloud import GetExtendedAttributesRequest, ExtendedAttributeItemsResponse, \
    GetExtendedAttributeByIndexRequest, ExtendedAttributeResponse, CalculationType, Value, ExtendedAttributeDefinition, \
    CustomFieldType, ElementType, PutExtendedAttributeRequest, ExtendedAttributeItemResponse, \
    DeleteExtendedAttributeByIndexRequest, AsposeResponse
from test.base_test_context import BaseTestContext


class TestExtendedAttributes(BaseTestContext):

    def test_get_extended_attributes(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        request = GetExtendedAttributesRequest(filename)
        result = self.tasks_api.get_extended_attributes(request)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, ExtendedAttributeItemsResponse)
        self.assertIsNotNone(result.extended_attributes)
        self.assertEqual(2, len(result.extended_attributes.list))

    def test_get_extended_attribute_by_index(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        request = GetExtendedAttributeByIndexRequest(filename, 1)
        result = self.tasks_api.get_extended_attribute_by_index(request)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, ExtendedAttributeResponse)
        self.assertIsNotNone(result.extended_attribute)
        self.assertEqual('Text1', result.extended_attribute.field_name)
        self.assertEqual(CalculationType.LOOKUP, result.extended_attribute.calculation_type)
        self.assertEqual(1, len(result.extended_attribute.value_list))
        self.assertEqual('descr', result.extended_attribute.value_list[0].description)
        self.assertEqual(1, result.extended_attribute.value_list[0].id)

    def test_put_extended_attribute(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        first_value = Value()
        first_value.description = "descr1"
        first_value.val = "Internal"
        first_value.id = 111
        second_value = Value()
        second_value.description = "descr2"
        second_value.val = "External"
        second_value.id = 112
        new_extended_attribute = ExtendedAttributeDefinition()
        new_extended_attribute.calculation_type = CalculationType.LOOKUP
        new_extended_attribute.cf_type = CustomFieldType.TEXT
        new_extended_attribute.field_name = "Text3"
        new_extended_attribute.element_type = ElementType.TASK
        new_extended_attribute.alias = "New Field"
        new_extended_attribute.value_list = [first_value, second_value]
        put_request = PutExtendedAttributeRequest(new_extended_attribute, filename)
        put_result = self.tasks_api.put_extended_attribute(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, ExtendedAttributeItemResponse)
        self.assertIsNotNone(put_result.extended_attribute)
        self.assertEqual('Text3', put_result.extended_attribute.field_name)
        self.assertEqual('New Field', put_result.extended_attribute.alias)
        self.assertEqual('188743737', put_result.extended_attribute.field_id)
        added_attribute_index = put_result.extended_attribute.index
        get_request = GetExtendedAttributeByIndexRequest(filename, added_attribute_index)
        get_result = self.tasks_api.get_extended_attribute_by_index(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, ExtendedAttributeResponse)
        self.assertIsNotNone(get_result.extended_attribute)
        self.assertEqual('Text3', get_result.extended_attribute.field_name)
        self.assertEqual('New Field', get_result.extended_attribute.alias)
        self.assertEqual('188743737', get_result.extended_attribute.field_id)
        self.assertEqual(CustomFieldType.TEXT, get_result.extended_attribute.cf_type)
        self.assertEqual(2, len(get_result.extended_attribute.value_list))
        self.assertEqual(111, get_result.extended_attribute.value_list[0].id)
        self.assertEqual('Internal', get_result.extended_attribute.value_list[0].val)
        self.assertEqual('descr1', get_result.extended_attribute.value_list[0].description)
        self.assertEqual(112, get_result.extended_attribute.value_list[1].id)
        self.assertEqual('External', get_result.extended_attribute.value_list[1].val)
        self.assertEqual('descr2', get_result.extended_attribute.value_list[1].description)

    def test_put_extended_attribute_rewrite(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        get_request = GetExtendedAttributeByIndexRequest(filename, 1)
        get_result = self.tasks_api.get_extended_attribute_by_index(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, ExtendedAttributeResponse)
        self.assertIsNotNone(get_result.extended_attribute)
        extended_attribute_to_edit = get_result.extended_attribute
        extended_attribute_to_edit.calculation_type = CalculationType.NONE
        extended_attribute_to_edit.value_list = []
        extended_attribute_to_edit.cf_type = CustomFieldType.TEXT
        extended_attribute_to_edit.field_name = "Text1"
        extended_attribute_to_edit.element_type = ElementType.TASK
        extended_attribute_to_edit.alias = 'Edited field'
        put_request = PutExtendedAttributeRequest(extended_attribute_to_edit, filename)
        put_result = self.tasks_api.put_extended_attribute(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, ExtendedAttributeItemResponse)
        self.assertIsNotNone(put_result.extended_attribute)
        self.assertEqual('Text1', put_result.extended_attribute.field_name)
        self.assertEqual('Edited field', put_result.extended_attribute.alias)
        self.assertEqual('188743731', put_result.extended_attribute.field_id)
        edited_attribute_index = put_result.extended_attribute.index
        get_request = GetExtendedAttributeByIndexRequest(filename, edited_attribute_index)
        get_result = self.tasks_api.get_extended_attribute_by_index(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, ExtendedAttributeResponse)
        self.assertIsNotNone(get_result.extended_attribute)
        self.assertEqual('Text1', get_result.extended_attribute.field_name)
        self.assertEqual('Edited field', get_result.extended_attribute.alias)
        self.assertEqual('188743731', get_result.extended_attribute.field_id)
        self.assertEqual(CustomFieldType.TEXT, get_result.extended_attribute.cf_type)
        self.assertEqual(0, len(get_result.extended_attribute.value_list))

    def test_delete_extended_attribute_by_index(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        delete_request = DeleteExtendedAttributeByIndexRequest(filename, 1)
        delete_result = self.tasks_api.delete_extended_attribute_by_index(delete_request)
        self.assertIsNotNone(delete_result)
        self.assertIsInstance(delete_result, AsposeResponse)

        get_request = GetExtendedAttributesRequest(filename)
        get_result = self.tasks_api.get_extended_attributes(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, ExtendedAttributeItemsResponse)
        self.assertIsNotNone(get_result.extended_attributes)
        self.assertEqual(1, len(get_result.extended_attributes.list))
