#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_recalculation.py">
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

from asposetaskscloud import PostTaskRequest, TaskItemResponse, GetTaskRequest, TaskResponse, PutTaskRequest, \
    PutRecalculateProjectRequest, CalculationMode, ProjectRecalculateResponse, ProjectValidationState, \
    PutRecalculateProjectResourceFieldsRequest, AsposeResponse, PutRecalculateProjectUncompleteWorkToStartAfterRequest, \
    PutRecalculateProjectWorkAsCompleteRequest
from test.base_test_context import BaseTestContext


class TestRecalculation(BaseTestContext):

    def test_put_recalculate_project(self):
        filename = 'sample.mpp'
        self.upload_file(filename)
        post_task_request = PostTaskRequest(filename, 'NewTaskName')
        post_task_result = self.tasks_api.post_task(post_task_request)
        self.assertIsNotNone(post_task_result)
        self.assertIsInstance(post_task_result, TaskItemResponse)
        task_uid = post_task_result.task_item.uid
        get_task_request = GetTaskRequest(filename, task_uid)
        get_task_result = self.tasks_api.get_task(get_task_request)
        self.assertIsNotNone(get_task_result)
        self.assertIsInstance(get_task_result, TaskResponse)
        task = get_task_result.task
        task.name = 'New task Name'
        task.actual_start = datetime(2000, 10, 20, 8)
        task.actual_finish = datetime(2000, 10, 9, 18)
        task.cost = 100
        put_task_request = PutTaskRequest(filename, task_uid, task, recalculate=False)
        put_task_result = self.tasks_api.put_task(put_task_request)
        self.assertIsNotNone(put_task_result)
        self.assertIsInstance(put_task_result, TaskResponse)
        put_recalculate_project_request = PutRecalculateProjectRequest(filename, CalculationMode.NONE, True)
        put_recalculate_project_result = self.tasks_api.put_recalculate_project(put_recalculate_project_request)
        self.assertIsNotNone(put_recalculate_project_result)
        self.assertIsInstance(put_recalculate_project_result, ProjectRecalculateResponse)
        self.assertEqual(ProjectValidationState.VALID, put_recalculate_project_result.result.validation_state)

    def test_put_recalculate_project_resource_fields(self):
        filename = 'Home_move_plan.mpp'
        self.upload_file(filename)
        put_request = PutRecalculateProjectResourceFieldsRequest(filename)
        put_result = self.tasks_api.put_recalculate_project_resource_fields(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, AsposeResponse)

    def test_put_recalculate_project_uncomplete_work_to_start_after(self):
        filename = 'Home_move_plan.mpp'
        self.upload_file(filename)
        put_request = PutRecalculateProjectUncompleteWorkToStartAfterRequest(filename, datetime(2010, 10, 10, 13))
        put_result = self.tasks_api.put_recalculate_project_uncomplete_work_to_start_after(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, AsposeResponse)

    def test_put_recalculate_project_work_as_complete(self):
        filename = 'Home_move_plan.mpp'
        self.upload_file(filename)
        put_request = PutRecalculateProjectWorkAsCompleteRequest(filename, datetime(2010, 10, 10, 13))
        put_result = self.tasks_api.put_recalculate_project_work_as_complete(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, AsposeResponse)
