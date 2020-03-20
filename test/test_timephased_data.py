#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_timephased_data.py">
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
from asposetaskscloud import GetTaskTimephasedDataRequest, TimephasedDataType, TimephasedDataResponse, \
    GetResourceTimephasedDataRequest, GetAssignmentTimephasedDataRequest
from test.base_test_context import BaseTestContext


class TestTimephasedData(BaseTestContext):

    def test_get_task_timephased_data(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        get_request = GetTaskTimephasedDataRequest(filename, 27, TimephasedDataType.TASKWORK)
        get_result = self.tasks_api.get_task_timephased_data(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TimephasedDataResponse)
        self.assertIsNotNone(get_result.items)
        self.assertLessEqual(1, len(get_result.items))
        for item in get_result.items:
            self.assertEqual(TimephasedDataType.TASKWORK, item.timephased_data_type)
            self.assertEqual(27, item.uid)

    def test_get_resource_timephased_data(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        get_request = GetResourceTimephasedDataRequest(filename, 1, TimephasedDataType.RESOURCEWORK)
        get_result = self.tasks_api.get_resource_timephased_data(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TimephasedDataResponse)
        self.assertIsNotNone(get_result.items)
        self.assertLessEqual(1, len(get_result.items))
        for item in get_result.items:
            self.assertEqual(TimephasedDataType.RESOURCEWORK, item.timephased_data_type)
            self.assertEqual(1, item.uid)

    def test_get_assignment_timephased_data(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        get_request = GetAssignmentTimephasedDataRequest(filename, 66, TimephasedDataType.ASSIGNMENTWORK)
        get_result = self.tasks_api.get_assignment_timephased_data(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TimephasedDataResponse)
        self.assertIsNotNone(get_result.items)
        self.assertLessEqual(1, len(get_result.items))
        for item in get_result.items:
            self.assertEqual(TimephasedDataType.ASSIGNMENTWORK, item.timephased_data_type)
            self.assertEqual(66, item.uid)
