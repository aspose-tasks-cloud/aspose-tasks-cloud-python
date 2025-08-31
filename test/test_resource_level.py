#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_resource_level.py">
#   Copyright (c) 2025 Aspose.Tasks Cloud
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
from asposetaskscloud import LevelTasksRequest, LevelingResponse, LevelingOptions, LevelingOrder, ClearLevelingRequest, \
    AsposeResponse
from test.base_test_context import BaseTestContext


class TestResourceLevel(BaseTestContext):

    def test_level_tasks(self):
        filename = 'sample.mpp'
        self.upload_file(filename)
        level_request = LevelTasksRequest(filename)
        level_result = self.tasks_api.level_tasks(level_request)
        self.assertIsNotNone(level_result)
        self.assertIsInstance(level_result, LevelingResponse)
        self.assertIsNotNone(level_result.affected_task_uids)
        self.assertEqual(2, len(level_result.affected_task_uids))

    def test_level_tasks_with_specified_body(self):
        filename = 'sample.mpp'
        self.upload_file(filename)
        options = LevelingOptions()
        options.leveling_order = LevelingOrder.STANDARD
        options.resource_uids = [2, 999]
        level_request = LevelTasksRequest(filename, options)
        level_result = self.tasks_api.level_tasks(level_request)
        self.assertIsNotNone(level_result)
        self.assertIsInstance(level_result, LevelingResponse)
        self.assertIsNotNone(level_result.affected_task_uids)
        self.assertEqual(1, len(level_result.affected_task_uids))

    def test_clear_leveling(self):
        filename = 'sample.mpp'
        self.upload_file(filename)
        clear_request = ClearLevelingRequest(filename)
        clear_result = self.tasks_api.clear_leveling(clear_request)
        self.assertIsNotNone(clear_result)
        self.assertIsInstance(clear_result, AsposeResponse)
        self.assertEqual(200, clear_result.code)

    def test_clear_leveling_with_body(self):
        filename = 'sample.mpp'
        self.upload_file(filename)
        clear_request = ClearLevelingRequest(filename)
        clear_request.task_uids = [24, 9999]
        clear_result = self.tasks_api.clear_leveling(clear_request)
        self.assertIsNotNone(clear_result)
        self.assertIsInstance(clear_result, AsposeResponse)
        self.assertEqual(200, clear_result.code)
