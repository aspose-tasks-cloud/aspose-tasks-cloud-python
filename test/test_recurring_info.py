#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_recurring_info.py">
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

from asposetaskscloud import GetTaskRecurringInfoRequest, RecurringInfoResponse, RecurrencePattern, WeekDayType, \
    OrdinalNumber, PutTaskRecurringInfoRequest, AsposeResponse, RecurringInfo, PostTaskRecurringInfoRequest, \
    TaskItemResponse, GetTaskRequest, TaskResponse
from test.base_test_context import BaseTestContext


class TestRecurringInfo(BaseTestContext):

    def test_get_task_recurring_info(self):
        filename = 'sample.mpp'
        self.upload_file(filename)
        get_request = GetTaskRecurringInfoRequest(filename, 6)
        get_result = self.tasks_api.get_task_recurring_info(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, RecurringInfoResponse)
        self.assertEqual(2, get_result.recurring_info.occurrences)
        self.assertEqual(RecurrencePattern.MONTHLY, get_result.recurring_info.recurrence_pattern)
        self.assertTrue(get_result.recurring_info.use_end_date)
        self.assertFalse(get_result.recurring_info.monthly_use_ordinal_day)
        self.assertEqual(1, get_result.recurring_info.monthly_day)
        self.assertEqual(WeekDayType.NONE, get_result.recurring_info.weekly_days)
        self.assertEqual(OrdinalNumber.SECOND, get_result.recurring_info.yearly_ordinal_number)

    def test_put_task_recurring_info(self):
        filename = 'sample.mpp'
        self.upload_file(filename)
        get_request = GetTaskRecurringInfoRequest(filename, 6)
        get_result = self.tasks_api.get_task_recurring_info(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, RecurringInfoResponse)
        self.assertEqual(2, get_result.recurring_info.occurrences)
        recurring_info = get_result.recurring_info
        recurring_info.occurrences = 10
        put_request = PutTaskRecurringInfoRequest(filename, 6, recurring_info)
        put_result = self.tasks_api.put_task_recurring_info(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, AsposeResponse)
        get_result = self.tasks_api.get_task_recurring_info(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, RecurringInfoResponse)
        self.assertEqual(10, get_result.recurring_info.occurrences)
        self.assertEqual(RecurrencePattern.MONTHLY, get_result.recurring_info.recurrence_pattern)
        self.assertTrue(get_result.recurring_info.use_end_date)
        self.assertFalse(get_result.recurring_info.monthly_use_ordinal_day)
        self.assertEqual(1, get_result.recurring_info.monthly_day)
        self.assertEqual(WeekDayType.NONE, get_result.recurring_info.weekly_days)
        self.assertEqual(OrdinalNumber.SECOND, get_result.recurring_info.yearly_ordinal_number)

    def test_post_task_recurring_info(self):
        filename = 'sample.mpp'
        self.upload_file(filename)
        recurring_info = RecurringInfo()
        recurring_info.recurrence_pattern = RecurrencePattern.WEEKLY
        recurring_info.occurrences = 4
        recurring_info.weekly_repetitions = 3
        recurring_info.weekly_days = WeekDayType.THURSDAY
        recurring_info.start_date = datetime(2018, 1, 1, 8)
        recurring_info.end_date = datetime(2018, 12, 31)
        recurring_info.use_end_date = True
        post_request = PostTaskRecurringInfoRequest(filename, 0, 'New recurring task', recurring_info, 'Standard')
        post_result = self.tasks_api.post_task_recurring_info(post_request)
        self.assertIsNotNone(post_result)
        self.assertIsInstance(post_result, TaskItemResponse)
        get_request = GetTaskRequest(filename, post_result.task_item.uid)
        get_result = self.tasks_api.get_task(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskResponse)
        self.assertEqual(18, len(get_result.task.subtasks_uids))
        task_uid = max(get_result.task.subtasks_uids)
        get_request = GetTaskRequest(filename, task_uid)
        get_result = self.tasks_api.get_task(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskResponse)
        self.assertEqual(datetime(2018, 12, 27, 8, 0, 0), get_result.task.start)
