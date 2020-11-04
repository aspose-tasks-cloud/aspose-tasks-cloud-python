#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_assignments.py">
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

from asposetaskscloud import PostAssignmentRequest, AssignmentItemResponse, GetAssignmentRequest, GetTaskRequest, \
    AssignmentResponse, TaskResponse, GetAssignmentsRequest, AssignmentItemsResponse, GetResourceAssignmentsRequest, \
    AssignmentsResponse, PutAssignmentRequest, CalculationMode, DeleteAssignmentRequest, AsposeResponse, \
    WorkContourType, TimephasedData, TimeUnitType, TimephasedDataType, BaselineType, AssignmentBaseline, Baseline
from test.base_test_context import BaseTestContext


class TestAssignments(BaseTestContext):

    def test_post_assignment(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        request = PostAssignmentRequest(filename, 0, 1, 0.5)
        result = self.tasks_api.post_assignment(request)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, AssignmentItemResponse)
        self.assertIsNotNone(result.assignment_item)

        assignment_uid = result.assignment_item.uid
        get_response = self.tasks_api.get_assignment(GetAssignmentRequest(filename, assignment_uid))
        get_task_response = self.tasks_api.get_task(GetTaskRequest(filename, 0))

        self.assertIsInstance(get_response, AssignmentResponse)
        self.assertIsNotNone(get_response.assignment)
        self.assertEqual(get_response.assignment.task_uid, 0)
        self.assertEqual(1, get_response.assignment.resource_uid)
        self.assertIsInstance(get_task_response, TaskResponse)
        self.assertIsNotNone(get_task_response.task)
        self.assertEqual(get_task_response.task.start, get_response.assignment.start)
        self.assertEqual(get_task_response.task.finish, get_response.assignment.finish)
        self.assertEqual(get_task_response.task.work, get_response.assignment.work)
        self.assertEqual(get_task_response.task.cost, get_response.assignment.cost)

    def test_post_assignment_with_cost_instead_of_units(self):
        filename = 'Cost_Res.mpp'
        self.upload_file(filename)
        request = PostAssignmentRequest(filename, 0, 1, None, 2)
        result = self.tasks_api.post_assignment(request)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, AssignmentItemResponse)
        self.assertIsNotNone(result.assignment_item)

        assignment_uid = result.assignment_item.uid
        get_response = self.tasks_api.get_assignment(GetAssignmentRequest(filename, assignment_uid))

        self.assertIsInstance(get_response, AssignmentResponse)
        self.assertIsNotNone(get_response.assignment)
        self.assertEqual(request.task_uid, get_response.assignment.task_uid)
        self.assertEqual(request.resource_uid, get_response.assignment.resource_uid)
        self.assertEqual(request.cost, get_response.assignment.cost)

    def test_get_assignment(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        result = self.tasks_api.get_assignment(GetAssignmentRequest(filename, 63))

        self.assertIsInstance(result, AssignmentResponse)
        self.assertIsNotNone(result.assignment)
        self.assertEqual("08:00:00", result.assignment.regular_work)
        self.assertEqual("08:00:00", result.assignment.remaining_work)
        self.assertEqual("08:00:00", result.assignment.start.strftime("%H:%M:%S"))

    def test_get_assignments(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        result = self.tasks_api.get_assignments(GetAssignmentsRequest(filename))

        self.assertIsInstance(result, AssignmentItemsResponse)
        self.assertIsNotNone(result.assignments)
        self.assertEqual(6, len(result.assignments.assignment_item))
        self.assertEqual(34, result.assignments.assignment_item[0].task_uid)
        self.assertEqual(63, result.assignments.assignment_item[0].uid)
        self.assertEqual("/63", result.assignments.assignment_item[0].link.href)

    def test_get_resource_assignments(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        result = self.tasks_api.get_resource_assignments(GetResourceAssignmentsRequest(filename, 1))

        self.assertIsInstance(result, AssignmentsResponse)
        self.assertIsNotNone(result.assignments)
        self.assertEqual(6, len(result.assignments.list))
        for assignment in result.assignments.list:
            self.assertEqual(1, assignment.resource_uid)

    def test_put_assignment(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        assignment_response = self.tasks_api.get_assignment(GetAssignmentRequest(filename, 63))
        assignment = assignment_response.assignment
        assignment.task_uid = 0
        put_response = self.tasks_api.put_assignment(
            PutAssignmentRequest(filename, 63, assignment, CalculationMode.AUTOMATIC, True))
        self.assertIsInstance(put_response, AssignmentResponse)
        self.assertIsNotNone(put_response.assignment)

        assignment_response = self.tasks_api.get_assignment(GetAssignmentRequest(filename, 63))
        self.assertIsInstance(assignment_response, AssignmentResponse)
        self.assertIsNotNone(assignment_response.assignment)
        self.assertEqual(0, assignment_response.assignment.task_uid)

    def test_put_assignment_with_timephaseddata_and_baselines(self):
        filename = 'sample.mpp'
        self.upload_file(filename)
        assignment_response = self.tasks_api.get_assignment(GetAssignmentRequest(filename, 1))
        assignment = assignment_response.assignment
        assignment.cost = 100
        assignment.start = datetime(2001, 10, 10)
        assignment.finish = datetime(2002, 10, 10)
        assignment.baselines = [AssignmentBaseline(datetime(2002, 10, 10))]
        assignment.actual_work = "10:10:10"
        assignment.actual_cost = 100
        assignment.actual_start = datetime(2001, 10, 10)
        assignment.actual_finish = datetime(2002, 10, 10)
        assignment.actual_overtime_work = "100:10:10"
        assignment.work = "80:0:0"
        assignment.uid = 1
        assignment.vac = 10
        assignment.work_contour = WorkContourType.CONTOURED
        assignment.timephased_data = [
            TimephasedData(assignment.uid, datetime(2001, 10, 10, 9, 0, 0, 0),
                           datetime(2001, 10, 10, 14, 0, 0, 0), TimeUnitType.HOUR, "4:0:0",
                           TimephasedDataType.ASSIGNMENTREMAININGWORK)
        ]
        put_response = self.tasks_api.put_assignment(
            PutAssignmentRequest(filename, 1, assignment, CalculationMode.NONE, False))

        self.assertIsInstance(put_response, AssignmentResponse)
        self.assertIsNotNone(put_response.assignment)
        self.assertEqual(assignment.uid, put_response.assignment.uid)
        self.assertEqual(assignment.vac, put_response.assignment.vac)
        self.assertNotEqual(assignment.cost, put_response.assignment.cost, "Calculated fields must be overwritten")
        self.assertEqual(assignment.start, put_response.assignment.start)
        self.assertEqual(assignment.finish, put_response.assignment.finish)
        self.assertEqual("80.00:00:00", put_response.assignment.work)
        self.assertEqual(assignment.actual_work, put_response.assignment.actual_work)
        self.assertEqual(assignment.actual_start, put_response.assignment.actual_start)
        self.assertEqual(assignment.actual_finish, put_response.assignment.actual_finish)
        self.assertEqual("100.10:10:00", put_response.assignment.actual_overtime_work)
        self.assertEqual(1, len(put_response.assignment.baselines))
        self.assertEqual(assignment.baselines[0].start, put_response.assignment.baselines[0].start)
        self.assertEqual(1, len(put_response.assignment.timephased_data))
        self.assertEqual(assignment.timephased_data[0].uid, put_response.assignment.timephased_data[0].uid)
        self.assertEqual("PT4H0M0S", put_response.assignment.timephased_data[0].value)
        self.assertEqual(assignment.timephased_data[0].start, put_response.assignment.timephased_data[0].start)
        self.assertEqual(assignment.timephased_data[0].finish, put_response.assignment.timephased_data[0].finish)
        self.assertEqual(assignment.timephased_data[0].timephased_data_type,
                         put_response.assignment.timephased_data[0].timephased_data_type)

    def test_delete_assignment(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        delete_response = self.tasks_api.delete_assignment(DeleteAssignmentRequest(filename, 63))
        self.assertIsInstance(delete_response, AsposeResponse)

        assignment_items_response = self.tasks_api.get_assignments(GetAssignmentsRequest(filename))

        self.assertIsInstance(assignment_items_response, AssignmentItemsResponse)
        self.assertIsNotNone(assignment_items_response.assignments)

        for assignment in assignment_items_response.assignments.assignment_item:
            self.assertFalse(assignment.task_uid == 34 & assignment.resource_uid == 1)
            self.assertNotEqual(63, assignment.uid)
