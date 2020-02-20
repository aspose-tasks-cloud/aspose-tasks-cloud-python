#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_calendar_exceptions.py">
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

from asposetaskscloud import GetCalendarExceptionsRequest, CalendarExceptionsResponse, DayType, Month, MonthItemType, \
    MonthPosition, CalendarExceptionType, CalendarException, PostCalendarExceptionRequest, AsposeResponse, WorkingTime, \
    PutCalendarExceptionRequest, DeleteCalendarExceptionRequest
from test.base_test_context import BaseTestContext


class TestCalendarExceptions(BaseTestContext):

    def test_get_calendar_exceptions(self):
        filename = 'Calenar_with_exception.mpp'
        self.upload_file(filename)
        request = GetCalendarExceptionsRequest(filename, 1)
        result = self.tasks_api.get_calendar_exceptions(request)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, CalendarExceptionsResponse)
        self.assertIsNotNone(result.calendar_exceptions)
        self.assertEqual(1, len(result.calendar_exceptions))

        calendar_exception = result.calendar_exceptions[0]
        self.assertTrue(calendar_exception.day_working)
        self.assertEqual([DayType.MONDAY], calendar_exception.days_of_week)
        self.assertEqual("2018-02-13", calendar_exception.from_date.strftime("%Y-%m-%d"))
        self.assertEqual("2018-04-09", calendar_exception.to_date.strftime("%Y-%m-%d"))
        self.assertEqual(Month.UNDEFINED, calendar_exception.month)
        self.assertEqual(MonthItemType.UNDEFINED, calendar_exception.month_item)
        self.assertEqual(MonthPosition.UNDEFINED, calendar_exception.month_position)
        self.assertEqual(CalendarExceptionType.WEEKLY, calendar_exception.type)
        self.assertEqual(8, calendar_exception.occurrences)
        self.assertEqual(1, calendar_exception.period)
        self.assertEqual(2, len(calendar_exception.working_times))
        self.assertEqual("09:00:00", calendar_exception.working_times[0].from_time.strftime("%H:%M:%S"))
        self.assertEqual("12:34:00", calendar_exception.working_times[0].to_time.strftime("%H:%M:%S"))
        self.assertEqual("15:11:00", calendar_exception.working_times[1].from_time.strftime("%H:%M:%S"))
        self.assertEqual("17:30:00", calendar_exception.working_times[1].to_time.strftime("%H:%M:%S"))

    def test_post_calendar_exception(self):
        filename = 'New_project_2013.mpp'
        self.upload_file(filename)

        exception = CalendarException()
        exception.working_times = []
        exception.days_of_week = []
        exception.name = "Non-working day exception"
        exception.day_working = False
        exception.from_date = datetime(2014, 9, 27, 8)
        exception.to_date = datetime(2015, 7, 5, 8)
        exception.occurrences = 10
        exception.type = CalendarExceptionType.MONTHLYBYDAY
        exception.entered_by_occurrences = True
        exception.month_day = 5
        exception.period = 1
        post_request = PostCalendarExceptionRequest(filename, 1, exception)
        post_result = self.tasks_api.post_calendar_exception(post_request)
        self.assertIsNotNone(post_result)
        self.assertIsInstance(post_result, AsposeResponse)

        get_request = GetCalendarExceptionsRequest(filename, 1)
        get_result = self.tasks_api.get_calendar_exceptions(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, CalendarExceptionsResponse)
        self.assertEqual(1, len(get_result.calendar_exceptions))
        self.__assert_calendar_exceptions_are_equal(exception, get_result.calendar_exceptions[0])

    def test_put_calendar_exception(self):
        filename = 'Calenar_with_exception.mpp'
        self.upload_file(filename)

        get_request = GetCalendarExceptionsRequest(filename, 1)
        get_result = self.tasks_api.get_calendar_exceptions(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, CalendarExceptionsResponse)
        exception = get_result.calendar_exceptions[0]
        exception.working_times = [WorkingTime(datetime(2000, 1, 1, 9), datetime(2000, 1, 1, 17))]
        exception.days_of_week = [DayType.THURSDAY, DayType.FRIDAY]
        exception.occurrences = 10
        exception.entered_by_occurrences = True
        exception.period = 1
        exception.name = "Non-working day exception"
        exception.day_working = True
        exception.from_date = datetime(2014, 10, 28)
        exception.to_date = datetime(2015, 8, 5)

        put_request = PutCalendarExceptionRequest(filename, 1, exception.index, exception)
        put_result = self.tasks_api.put_calendar_exception(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, AsposeResponse)

        get_request = GetCalendarExceptionsRequest(filename, 1)
        get_result = self.tasks_api.get_calendar_exceptions(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, CalendarExceptionsResponse)

        self.__assert_calendar_exceptions_are_equal(exception, get_result.calendar_exceptions[0])

    def test_delete_calendar_exception(self):
        filename = 'Calenar_with_exception.mpp'
        self.upload_file(filename)
        delete_request = DeleteCalendarExceptionRequest(filename, 1, 1)
        delete_result = self.tasks_api.delete_calendar_exception(delete_request)
        self.assertIsNotNone(delete_result)
        self.assertIsInstance(delete_result, AsposeResponse)

        get_request = GetCalendarExceptionsRequest(filename, 1)
        get_result = self.tasks_api.get_calendar_exceptions(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, CalendarExceptionsResponse)
        self.assertEqual(0, len(get_result.calendar_exceptions))

    def __assert_calendar_exceptions_are_equal(self, first, second):
        self.assertIsInstance(first, CalendarException)
        self.assertIsInstance(second, CalendarException)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.day_working, second.day_working)
        self.assertEqual(first.entered_by_occurrences, second.entered_by_occurrences)
        self.assertEqual(first.from_date.strftime("%Y-%m-%d"), second.from_date.strftime("%Y-%m-%d"))
        self.assertEqual(first.month_day, second.month_day)
        self.assertEqual(first.occurrences, second.occurrences)
        self.assertEqual(first.period, second.period)
        self.assertEqual(first.to_date.strftime("%Y-%m-%d"), second.to_date.strftime("%Y-%m-%d"))
        self.assertEqual(first.type, second.type)
        self.assertEqual(len(first.working_times), len(second.working_times))
        for i, first_wt in enumerate(first.working_times):
            second_wt = second.working_times[i]
            self.assertEqual(first_wt.from_time.strftime("%H:%M:%S"), second_wt.from_time.strftime("%H:%M:%S"))
            self.assertEqual(first_wt.to_time.strftime("%H:%M:%S"), second_wt.to_time.strftime("%H:%M:%S"))
        self.assertEqual(len(first.days_of_week), len(second.days_of_week))
        for i, first_dw in enumerate(first.days_of_week):
            second_dw = second.days_of_week[i]
            self.assertEqual(first_dw, second_dw)




