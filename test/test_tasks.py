#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_tasks.py">
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
import json
from datetime import datetime

from asposetaskscloud import GetTasksRequest, TaskItemsResponse, GetTaskRequest, TaskResponse, DeleteTaskRequest, \
    AsposeResponse, PostTaskRequest, TaskItemResponse, PutTaskRequest, CalculationMode, GetTaskAssignmentsRequest, \
    AssignmentsResponse, PutMoveTaskRequest, PutMoveTaskToSiblingRequest, PostTasksRequest, TaskCreationRequest
from asposetaskscloud.rest import ApiException
from test.base_test_context import BaseTestContext


class TestTasks(BaseTestContext):

    def test_get_tasks(self):
        filename = 'Project2016.mpp'
        self.upload_file(filename)
        get_request = GetTasksRequest(filename)
        get_result = self.tasks_api.get_tasks(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskItemsResponse)
        self.assertIsNotNone(get_result.tasks)
        self.assertEqual(6, len(get_result.tasks.task_item))
        first_task = next(t for t in get_result.tasks.task_item if t.uid == 5)
        self.assertEqual('Summary Task 1', first_task.name)
        self.assertEqual(datetime(2015, 8, 3, 8, 0, 0), first_task.start)
        self.assertEqual(datetime(2015, 8, 6, 17, 0, 0), first_task.finish)
        self.assertEqual('/5', first_task.link.href)

    def test_get_task(self):
        filename = 'Project2016.mpp'
        self.upload_file(filename)
        get_request = GetTaskRequest(filename, 5)
        get_result = self.tasks_api.get_task(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskResponse)
        self.assertIsNotNone(get_result.task)
        self.assertEqual(5, get_result.task.uid)
        self.assertEqual([1, 2, 3, 4], get_result.task.subtasks_uids)
        self.assertEqual('Summary Task 1', get_result.task.name)
        self.assertEqual(datetime(2015, 8, 3, 8, 0, 0), get_result.task.start)
        self.assertEqual(datetime(2015, 8, 6, 17, 0, 0), get_result.task.finish)
        self.assertEqual('1.08:00:00', get_result.task.remaining_work)
        self.assertEqual(1920, get_result.task.work_variance)

    def test_delete_task(self):
        filename = 'Project2016.mpp'
        self.upload_file(filename)
        delete_request = DeleteTaskRequest(filename, 4)
        delete_result = self.tasks_api.delete_task(delete_request)
        self.assertIsNotNone(delete_result)
        self.assertIsInstance(delete_result, AsposeResponse)

        get_request = GetTasksRequest(filename)
        get_result = self.tasks_api.get_tasks(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskItemsResponse)
        self.assertIsNotNone(get_result.tasks)
        self.assertEqual(5, len(get_result.tasks.task_item))
        deleted_task = next((t for t in get_result.tasks.task_item if t.uid == 4), None)
        self.assertIsNone(deleted_task)

    def test_post_task(self):
        filename = 'Project2016.mpp'
        self.upload_file(filename)
        post_request = PostTaskRequest(filename, 'New task name', 4)
        post_result = self.tasks_api.post_task(post_request)
        self.assertIsNotNone(post_result)
        self.assertIsInstance(post_result, TaskItemResponse)
        self.assertIsNotNone(post_result.task_item)

        get_request = GetTaskRequest(filename, post_result.task_item.uid)
        get_result = self.tasks_api.get_task(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskResponse)
        self.assertIsNotNone(get_result.task)

    def test_post_tasks(self):
        filename = 'Home_move_plan.mpp'
        self.upload_file(filename)
        first_task_create_request = TaskCreationRequest(task_name="SomeFirstTaskName")
        second_task_create_request = TaskCreationRequest(task_name="SomeSecondTaskNameWithParent", parent_task_uid=2)
        post_request = PostTasksRequest(filename, [first_task_create_request, second_task_create_request])
        post_result = self.tasks_api.post_tasks(post_request)
        self.assertIsNotNone(post_result)
        self.assertIsInstance(post_result, TaskItemsResponse)
        self.assertIsNotNone(post_result.tasks)
        self.assertEqual(len(post_request.requests), len(post_result.tasks.task_item))
        newSubtaskUid = [t.uid for t in post_result.tasks.task_item if t.name == second_task_create_request.task_name][0]

        get_request = GetTaskRequest(filename, second_task_create_request.parent_task_uid)
        get_result = self.tasks_api.get_task(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskResponse)
        self.assertIsNotNone(get_result.task)
        self.assertIn(newSubtaskUid, get_result.task.subtasks_uids)

    def test_put_task(self):
        filename = 'Project2016.mpp'
        self.upload_file(filename)
        get_request = GetTaskRequest(filename, 4)
        get_result = self.tasks_api.get_task(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskResponse)

        get_result.task.name = "Modified task name"
        get_result.task.is_manual = True
        get_result.task.manual_start = datetime(2015, 10, 1, 9, 15, 0)
        get_result.task.manual_finish = datetime(2015, 10, 1, 17, 15, 0)
        put_request = PutTaskRequest(filename, 4, get_result.task, CalculationMode.NONE, False)
        put_result = self.tasks_api.put_task(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, TaskResponse)

        get_result = self.tasks_api.get_task(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskResponse)
        self.assertIsNotNone(get_result.task)
        self.assertEqual('Modified task name', get_result.task.name)
        self.assertTrue(get_result.task.is_manual)
        self.assertEqual(datetime(2015, 10, 1, 9, 15, 0), get_result.task.manual_start)
        self.assertEqual(datetime(2015, 10, 1, 17, 15, 0), get_result.task.manual_finish)

    def test_get_task_assignments(self):
        filename = 'Home_move_plan.mpp'
        self.upload_file(filename)
        get_request = GetTaskAssignmentsRequest(filename, 1)
        get_result = self.tasks_api.get_task_assignments(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, AssignmentsResponse)
        self.assertIsNotNone(get_result.assignments)

    def test_put_move_task(self):
        filename = 'sample.mpp'
        self.upload_file(filename)
        get_request = GetTaskRequest(filename, 6)
        get_result = self.tasks_api.get_task(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskResponse)
        self.assertIsNone(next((s for s in get_result.task.subtasks_uids if s == 10), None))

        put_request = PutMoveTaskRequest(filename, 10, 6)
        put_result = self.tasks_api.put_move_task(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, AsposeResponse)

        get_result = self.tasks_api.get_task(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskResponse)
        self.assertIsNotNone(next((s for s in get_result.task.subtasks_uids if s == 10), None))

    def test_put_move_task_to_sibling(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        put_request = PutMoveTaskToSiblingRequest(filename, 40, 41)
        put_result = self.tasks_api.put_move_task_to_sibling(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, AsposeResponse)

        get_request = GetTaskRequest(filename, 38)
        get_result = self.tasks_api.get_task(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskResponse)
        self.assertEqual([39, 40, 41], get_result.task.subtasks_uids)

    def test_put_move_task_to_sibling_negative(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        put_request = PutMoveTaskToSiblingRequest(filename, 99999, -1)
        put_result = None
        try:
            put_result = self.tasks_api.put_move_task_to_sibling(put_request)
        except ApiException as e:
            self.assertEqual("Not Found", e.reason)
            error_body = json.loads(e.body)
            self.assertEqual("TaskDoesntExist", error_body['Error']['Code'])
            self.assertEqual("Task with 99999 Uid doesn't exist", error_body['Error']['Message'])
        self.assertIsNone(put_result, 'the result of operation should not be obtained')
