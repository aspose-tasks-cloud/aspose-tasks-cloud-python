#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_tasks_extended_attributes.py">
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

from asposetaskscloud import Value, ExtendedAttributeDefinition, CalculationType, CustomFieldType, ElementType, \
    PutExtendedAttributeRequest, ExtendedAttributeItemResponse, GetTaskRequest, TaskResponse, ExtendedAttribute, \
    PutTaskRequest, Duration, TimeUnitType
from test.base_test_context import BaseTestContext


class TestTasksExtendedAttributes(BaseTestContext):

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

        get_request = GetTaskRequest(filename, 27)
        get_result = self.tasks_api.get_task(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskResponse)

        new_extended_attribute = ExtendedAttribute(put_result.extended_attribute.field_id, lookup_value_id=112)
        get_result.task.extended_attributes.append(new_extended_attribute)
        put_request = PutTaskRequest(filename, 27, get_result.task)
        put_result = self.tasks_api.put_task(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, TaskResponse)

        get_result = self.tasks_api.get_task(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskResponse)
        self.assertEqual('188743737', get_result.task.extended_attributes[0].field_id)
        self.assertEqual(112, get_result.task.extended_attributes[0].lookup_value_id)

    def test_put_extended_attribute_second_case_with_uniform_date_value(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        new_extended_attribute = ExtendedAttributeDefinition()
        new_extended_attribute.calculation_type = CalculationType.NONE
        new_extended_attribute.cf_type = CustomFieldType.FINISH
        new_extended_attribute.field_name = "Finish4"
        new_extended_attribute.element_type = ElementType.TASK
        new_extended_attribute.alias = "Custom Finish Field"
        put_request = PutExtendedAttributeRequest(new_extended_attribute, filename)
        put_result = self.tasks_api.put_extended_attribute(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, ExtendedAttributeItemResponse)

        get_request = GetTaskRequest(filename, 27)
        get_result = self.tasks_api.get_task(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskResponse)

        new_extended_attribute = ExtendedAttribute('188743742', date_value=datetime(2018, 3, 4, 12, 30, 0))
        get_result.task.extended_attributes.append(new_extended_attribute)
        put_request = PutTaskRequest(filename, 27, get_result.task)
        put_result = self.tasks_api.put_task(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, TaskResponse)

        get_result = self.tasks_api.get_task(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskResponse)
        self.assertEqual(1, len(get_result.task.extended_attributes))
        self.assertEqual('188743742', get_result.task.extended_attributes[0].field_id)
        self.assertEqual(datetime(2018, 3, 4, 12, 30, 0), get_result.task.extended_attributes[0].date_value)

    def test_put_extended_attribute_third_case_with_uniform_duration_value(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        new_extended_attribute = ExtendedAttributeDefinition()
        new_extended_attribute.calculation_type = CalculationType.NONE
        new_extended_attribute.cf_type = CustomFieldType.DURATION
        new_extended_attribute.field_name = "Duration3"
        new_extended_attribute.element_type = ElementType.TASK
        new_extended_attribute.alias = "Custom Duration Field"
        put_request = PutExtendedAttributeRequest(new_extended_attribute, filename)
        put_result = self.tasks_api.put_extended_attribute(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, ExtendedAttributeItemResponse)

        get_request = GetTaskRequest(filename, 27)
        get_result = self.tasks_api.get_task(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskResponse)

        duration = Duration()
        duration.time_span = '04:00:00'
        duration.time_unit = TimeUnitType.MINUTE
        new_extended_attribute = ExtendedAttribute('188743785', duration_value=duration)
        get_result.task.extended_attributes.append(new_extended_attribute)
        put_request = PutTaskRequest(filename, 27, get_result.task)
        put_result = self.tasks_api.put_task(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, TaskResponse)

        get_result = self.tasks_api.get_task(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskResponse)
        self.assertEqual(1, len(get_result.task.extended_attributes))
        self.assertEqual('188743785', get_result.task.extended_attributes[0].field_id)
        self.assertIsNotNone(get_result.task.extended_attributes[0].duration_value)
        self.assertEqual('04:00:00', get_result.task.extended_attributes[0].duration_value.time_span)

    def test_put_extended_attribute_fourth_case_with_uniform_flag_value(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        new_extended_attribute = ExtendedAttributeDefinition()
        new_extended_attribute.calculation_type = CalculationType.NONE
        new_extended_attribute.cf_type = CustomFieldType.FLAG
        new_extended_attribute.field_name = "Flag12"
        new_extended_attribute.element_type = ElementType.TASK
        new_extended_attribute.alias = "Custom Flag Field"
        put_request = PutExtendedAttributeRequest(new_extended_attribute, filename)
        put_result = self.tasks_api.put_extended_attribute(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, ExtendedAttributeItemResponse)

        get_request = GetTaskRequest(filename, 27)
        get_result = self.tasks_api.get_task(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskResponse)

        new_extended_attribute = ExtendedAttribute('188743973', flag_value=True)
        get_result.task.extended_attributes.append(new_extended_attribute)
        put_request = PutTaskRequest(filename, 27, get_result.task)
        put_result = self.tasks_api.put_task(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, TaskResponse)

        get_result = self.tasks_api.get_task(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskResponse)
        self.assertEqual(1, len(get_result.task.extended_attributes))
        self.assertEqual('188743973', get_result.task.extended_attributes[0].field_id)
        self.assertTrue(get_result.task.extended_attributes[0].flag_value)

    def test_put_extended_attribute_fifth_case_with_uniform_cost_value(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        new_extended_attribute = ExtendedAttributeDefinition()
        new_extended_attribute.calculation_type = CalculationType.NONE
        new_extended_attribute.cf_type = CustomFieldType.COST
        new_extended_attribute.field_name = "Cost10"
        new_extended_attribute.element_type = ElementType.TASK
        new_extended_attribute.alias = "Custom Cost Field"
        put_request = PutExtendedAttributeRequest(new_extended_attribute, filename)
        put_result = self.tasks_api.put_extended_attribute(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, ExtendedAttributeItemResponse)

        get_request = GetTaskRequest(filename, 27)
        get_result = self.tasks_api.get_task(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskResponse)

        new_extended_attribute = ExtendedAttribute('188743944', numeric_value=115.99)
        get_result.task.extended_attributes.append(new_extended_attribute)
        put_request = PutTaskRequest(filename, 27, get_result.task)
        put_result = self.tasks_api.put_task(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, TaskResponse)

        get_result = self.tasks_api.get_task(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskResponse)
        self.assertEqual(1, len(get_result.task.extended_attributes))
        self.assertEqual('188743944', get_result.task.extended_attributes[0].field_id)
        self.assertEqual(115.99, get_result.task.extended_attributes[0].numeric_value)

    def test_put_extended_attribute_sixth_case_with_uniform_number_value(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        new_extended_attribute = ExtendedAttributeDefinition()
        new_extended_attribute.calculation_type = CalculationType.NONE
        new_extended_attribute.cf_type = CustomFieldType.NUMBER
        new_extended_attribute.field_name = "Number9"
        new_extended_attribute.element_type = ElementType.TASK
        new_extended_attribute.alias = "Custom Number Field"
        put_request = PutExtendedAttributeRequest(new_extended_attribute, filename)
        put_result = self.tasks_api.put_extended_attribute(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, ExtendedAttributeItemResponse)

        get_request = GetTaskRequest(filename, 27)
        get_result = self.tasks_api.get_task(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskResponse)

        new_extended_attribute = ExtendedAttribute('188743985', numeric_value=99.99)
        get_result.task.extended_attributes.append(new_extended_attribute)
        put_request = PutTaskRequest(filename, 27, get_result.task)
        put_result = self.tasks_api.put_task(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, TaskResponse)

        get_result = self.tasks_api.get_task(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskResponse)
        self.assertEqual(1, len(get_result.task.extended_attributes))
        self.assertEqual('188743985', get_result.task.extended_attributes[0].field_id)
        self.assertEqual(99.99, get_result.task.extended_attributes[0].numeric_value)

    def test_put_extended_attribute_seventh_case_with_uniform_text_value(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        new_extended_attribute = ExtendedAttributeDefinition()
        new_extended_attribute.calculation_type = CalculationType.NONE
        new_extended_attribute.cf_type = CustomFieldType.TEXT
        new_extended_attribute.field_name = "Text1"
        new_extended_attribute.element_type = ElementType.TASK
        new_extended_attribute.alias = "Custom Text Field"
        put_request = PutExtendedAttributeRequest(new_extended_attribute, filename)
        put_result = self.tasks_api.put_extended_attribute(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, ExtendedAttributeItemResponse)

        get_request = GetTaskRequest(filename, 27)
        get_result = self.tasks_api.get_task(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskResponse)

        new_extended_attribute = ExtendedAttribute('188743731', text_value='Test value')
        get_result.task.extended_attributes.append(new_extended_attribute)
        put_request = PutTaskRequest(filename, 27, get_result.task)
        put_result = self.tasks_api.put_task(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, TaskResponse)

        get_result = self.tasks_api.get_task(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskResponse)
        self.assertEqual(1, len(get_result.task.extended_attributes))
        self.assertEqual('188743731', get_result.task.extended_attributes[0].field_id)
        self.assertEqual('Test value', get_result.task.extended_attributes[0].text_value)
