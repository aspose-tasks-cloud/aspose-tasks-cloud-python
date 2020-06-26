#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_get_page_count.py">
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
from datetime import date

from asposetaskscloud import GetPageCountRequest, PresentationFormat, Timescale, PageCountResponse
from test.base_test_context import BaseTestContext


class TestGetPageCount(BaseTestContext):

    def test_get_page_count(self):
        filename = 'Home_move_plan.mpp'
        self.upload_file(filename)
        request = GetPageCountRequest(filename, presentation_format=PresentationFormat.TASKUSAGE, timescale=Timescale.MONTHS)
        result = self.tasks_api.get_page_count(request)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, PageCountResponse)
        self.assertEqual(4, result.page_count)

    def test_get_page_count_with_enhanced_data(self):
        filename = 'Home_move_plan.mpp'
        self.upload_file(filename)
        request = GetPageCountRequest(filename, presentation_format=PresentationFormat.TASKUSAGE, timescale=Timescale.MONTHS,
                                      start_date=date(2004, 1, 1), end_date=date(2004, 2, 28))
        result = self.tasks_api.get_page_count(request)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, PageCountResponse)
        self.assertEqual(4, result.page_count)
