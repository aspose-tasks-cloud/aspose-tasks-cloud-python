#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_calendar_work_weeks.py">
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
from asposetaskscloud import GetCalendarsRequest, CalendarItemsResponse, GetCalendarWorkWeeksRequest, \
    CalendarWorkWeeksResponse, DayType
from test.base_test_context import BaseTestContext


class TestCalendarWorkWeeks(BaseTestContext):

    def test_get_calendar_work_weeks(self):
        filename = 'CalendarWorkWeeks.mpp'
        self.upload_file(filename)
        calendars_request = GetCalendarsRequest(filename)
        calendars_result = self.tasks_api.get_calendars(calendars_request)
        self.assertIsNotNone(calendars_result)
        self.assertIsInstance(calendars_result, CalendarItemsResponse)
        self.assertIsNotNone(calendars_result.calendars)
        calendar_uid = next(c for c in calendars_result.calendars.list if c.name == 'Test work weeks').uid
        work_weeks_result = self.tasks_api.get_calendar_work_weeks(GetCalendarWorkWeeksRequest(filename, calendar_uid))
        self.assertIsNotNone(work_weeks_result)
        self.assertIsInstance(work_weeks_result, CalendarWorkWeeksResponse)
        self.assertEqual(1, len(work_weeks_result.calendar_work_weeks))
        work_week = work_weeks_result.calendar_work_weeks[0]
        self.assertEqual('Work week 1', work_week.name)
        self.assertEqual("2018-01-01", work_week.from_date.strftime("%Y-%m-%d"))
        self.assertEqual("2018-01-07", work_week.to_date.strftime("%Y-%m-%d"))
        
        self.assertEqual(4, len(work_week.week_days))
        self.assertEqual(True, work_week.week_days[0].day_working)
        self.assertEqual(DayType.MONDAY, work_week.week_days[0].day_type)
        self.assertEqual(1, len(work_week.week_days[0].working_times))
        self.assertEqual("11:30:00", work_week.week_days[0].working_times[0].from_time.strftime("%H:%M:%S"))
        self.assertEqual("12:30:00", work_week.week_days[0].working_times[0].to_time.strftime("%H:%M:%S"))
        
        self.assertEqual(False, work_week.week_days[1].day_working)
        self.assertEqual(DayType.TUESDAY, work_week.week_days[1].day_type)
        self.assertEqual(0, len(work_week.week_days[1].working_times))
        
        self.assertEqual(True, work_week.week_days[2].day_working)
        self.assertEqual(DayType.WEDNESDAY, work_week.week_days[2].day_type)
        self.assertEqual(2, len(work_week.week_days[2].working_times))
        
        self.assertEqual("09:30:00", work_week.week_days[2].working_times[0].from_time.strftime("%H:%M:%S"))
        self.assertEqual("13:23:00", work_week.week_days[2].working_times[0].to_time.strftime("%H:%M:%S"))
        self.assertEqual("14:45:00", work_week.week_days[2].working_times[1].from_time.strftime("%H:%M:%S"))
        self.assertEqual("18:45:00", work_week.week_days[2].working_times[1].to_time.strftime("%H:%M:%S"))
        
        self.assertEqual(True, work_week.week_days[3].day_working)
        self.assertEqual(DayType.SATURDAY, work_week.week_days[3].day_type)
        self.assertEqual(1, len(work_week.week_days[3].working_times))
        
        self.assertEqual("09:00:00", work_week.week_days[3].working_times[0].from_time.strftime("%H:%M:%S"))
        self.assertEqual("10:00:00", work_week.week_days[3].working_times[0].to_time.strftime("%H:%M:%S"))




