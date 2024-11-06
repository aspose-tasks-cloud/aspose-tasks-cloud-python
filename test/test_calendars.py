#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_calendars.py">
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
from asposetaskscloud import GetCalendarsRequest, CalendarItemsResponse, GetCalendarRequest, CalendarResponse, \
    PostCalendarRequest, Calendar, WeekDay, DayType, WorkingTime, CalendarItemResponse, PutCalendarRequest, \
    AsposeResponse, DeleteCalendarRequest
from test.base_test_context import BaseTestContext


class TestCalendars(BaseTestContext):

    def test_get_calendars(self):
        filename = 'Home_move_plan.mpp'
        self.upload_file(filename)
        request = GetCalendarsRequest(filename)
        result = self.tasks_api.get_calendars(request)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, CalendarItemsResponse)
        self.assertIsNotNone(result.calendars)
        self.assertEqual(1, len(result.calendars.list))
        self.assertEqual('Standard', result.calendars.list[0].name)
        self.assertEqual(1, result.calendars.list[0].uid)

    def test_get_calendar(self):
        filename = 'Home_move_plan.mpp'
        self.upload_file(filename)
        request = GetCalendarRequest(filename, 1)
        result = self.tasks_api.get_calendar(request)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, CalendarResponse)
        self.assertIsNotNone(result.calendar)
        self.assertEqual('3F979F74-B9D3-4E5F-98DC-5E08060A0C30', result.calendar.guid)
        self.assertEqual('Standard', result.calendar.name)
        self.assertEqual(1, result.calendar.uid)
        self.assertTrue(result.calendar.is_base_calendar)
        self.assertFalse(result.calendar.is_baseline_calendar)
        self.assertEqual(7, len(result.calendar.days))

    def test_post_calendar(self):
        filename = 'Home_move_plan.mpp'
        self.upload_file(filename)
        first_day = WeekDay()
        first_day.day_type = DayType.SUNDAY
        first_day.day_working = False
        second_day = WeekDay()
        second_day.day_type = DayType.MONDAY
        second_day.day_working = True
        second_day.from_date = datetime(2000, 1, 1, 8)
        second_day.to_date = datetime(2000, 1, 1, 17)
        first_working_time = WorkingTime()
        first_working_time.from_time = datetime(2000, 1, 1, 8)
        first_working_time.to_time = datetime(2000, 1, 1, 13)
        second_working_time = WorkingTime()
        second_working_time.from_time = datetime(2000, 1, 1, 14)
        second_working_time.to_time = datetime(2000, 1, 1, 17)
        second_day.working_times = [first_working_time, second_working_time]
        calendar = Calendar()
        calendar.name = 'My new calendar'
        calendar.days = [first_day, second_day]
        calendar.is_base_calendar = False
        calendar.is_baseline_calendar = False
        request = PostCalendarRequest(filename, calendar)
        post_result = self.tasks_api.post_calendar(request)
        self.assertIsNotNone(post_result)
        self.assertIsInstance(post_result, CalendarItemResponse)
        get_result = self.tasks_api.get_calendar(GetCalendarRequest(filename, post_result.calendar_item.uid))
        self.assertEqual('My new calendar', get_result.calendar.name)
        self.assertEqual(7, len(get_result.calendar.days))
        monday = next(d for d in get_result.calendar.days if d.day_type == DayType.MONDAY)
        self.assertEqual(2, len(monday.working_times))
        self.assertEqual(first_working_time.from_time.strftime("%H:%M:%S"), monday.working_times[0].from_time.strftime("%H:%M:%S"))
        self.assertEqual(first_working_time.to_time.strftime("%H:%M:%S"), monday.working_times[0].to_time.strftime("%H:%M:%S"))
        self.assertEqual(second_working_time.from_time.strftime("%H:%M:%S"), monday.working_times[1].from_time.strftime("%H:%M:%S"))
        self.assertEqual(second_working_time.to_time.strftime("%H:%M:%S"), monday.working_times[1].to_time.strftime("%H:%M:%S"))

    def test_put_calendar(self):
        filename = 'Home_move_plan.mpp'
        self.upload_file(filename)
        first_day = WeekDay()
        first_day.day_type = DayType.SUNDAY
        first_day.day_working = False
        second_day = WeekDay()
        second_day.day_type = DayType.MONDAY
        second_day.day_working = True
        second_day.from_date = datetime(2000, 1, 1, 8)
        second_day.to_date = datetime(2000, 1, 1, 17)
        first_working_time = WorkingTime()
        first_working_time.from_time = datetime(2000, 1, 1, 8)
        first_working_time.to_time = datetime(2000, 1, 1, 13)
        second_working_time = WorkingTime()
        second_working_time.from_time = datetime(2000, 1, 1, 14)
        second_working_time.to_time = datetime(2000, 1, 1, 17)
        second_day.working_times = [first_working_time, second_working_time]
        calendar = Calendar()
        calendar.name = 'Modified calendar'
        calendar.days = [first_day, second_day]
        calendar.is_base_calendar = False
        calendar.is_baseline_calendar = False
        request = PutCalendarRequest(filename, 1, calendar)
        put_result = self.tasks_api.put_calendar(request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, AsposeResponse)
        get_result = self.tasks_api.get_calendar(GetCalendarRequest(filename, 1))
        self.assertEqual('Modified calendar', get_result.calendar.name)
        self.assertEqual(7, len(get_result.calendar.days))
        monday = next(d for d in get_result.calendar.days if d.day_type == DayType.MONDAY)
        self.assertEqual(2, len(monday.working_times))
        self.assertEqual(first_working_time.from_time.strftime("%H:%M:%S"), monday.working_times[0].from_time.strftime("%H:%M:%S"))
        self.assertEqual(first_working_time.to_time.strftime("%H:%M:%S"), monday.working_times[0].to_time.strftime("%H:%M:%S"))
        self.assertEqual(second_working_time.from_time.strftime("%H:%M:%S"), monday.working_times[1].from_time.strftime("%H:%M:%S"))
        self.assertEqual(second_working_time.to_time.strftime("%H:%M:%S"), monday.working_times[1].to_time.strftime("%H:%M:%S"))

    def test_delete_calendar(self):
        filename = 'CalendarWorkWeeks.mpp'
        self.upload_file(filename)
        calendar_uid_to_delete = 3
        request = DeleteCalendarRequest(filename, calendar_uid_to_delete)
        delete_result = self.tasks_api.delete_calendar(request)
        self.assertIsNotNone(delete_result)
        self.assertIsInstance(delete_result, AsposeResponse)
        get_result = self.tasks_api.get_calendars(GetCalendarsRequest(filename))
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, CalendarItemsResponse)
        for calendar in get_result.calendars.list:
            self.assertNotEqual(calendar_uid_to_delete, calendar.uid)




