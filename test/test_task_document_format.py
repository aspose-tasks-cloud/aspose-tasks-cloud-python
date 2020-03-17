#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_task_document_format.py">
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
from asposetaskscloud import GetTaskDocumentWithFormatRequest, ProjectFileFormat
from asposetaskscloud.models.requests.post_task_document_with_format_request import PostTaskDocumentWithFormatRequest
from test.base_test_context import BaseTestContext


class TestTaskDocumentFormat(BaseTestContext):

    def test_get_task_document_with_format(self):
        filename = 'Home_move_plan.mpp'
        self.upload_file(filename)
        get_request = GetTaskDocumentWithFormatRequest(filename, ProjectFileFormat.CSV)
        get_result = self.tasks_api.get_task_document_with_format(get_request)
        self.assertIsNotNone(get_result)
        with open(get_result, encoding='utf-8', errors='ignore') as f:
            self.assertTrue(f.readable())
            self.assertIn('ID;Task_Name;Outline_Level;Duration;Start_Date;Finish_Date;Percent_Comp;Cost;Work',
                          f.readline())
            self.assertIn(
                '1;Five to Eight Weeks Before Moving;1;16 days;Thu 01.01.04 08:00;Thu 22.01.04 17:00;0%;$0;0 hrs',
                f.readline())

    def test_get_task_document_with_format_as_zipped_html(self):
        filename = 'Home_move_plan.mpp'
        self.upload_file(filename)
        get_request = GetTaskDocumentWithFormatRequest(filename, ProjectFileFormat.HTML, True)
        get_result = self.tasks_api.get_task_document_with_format(get_request)
        self.assertIsNotNone(get_result)
        self.assertTrue(get_result.endswith('.zip'))
        with open(get_result) as f:
            self.assertTrue(f.readable())

    def test_post_task_document_with_format(self):
        filename = 'Home_move_plan.mpp'
        self.upload_file(filename)

        # SaveOptions parameters is a json-serialized representation of
        # Aspose.Tasks's SaveOptions class or its format-specific inheritors (Like CsvOptions, etc):
        # See Aspose.Tasks reference: https://apireference.aspose.com/net/tasks/aspose.tasks.saving/saveoptions
        save_options_serialized = '{"TextDelimiter":"Comma","IncludeHeaders":false,"NonExistingTestProperty":false,"View":{"Columns":[{"Type":"GanttChartColumn","Name":"TestColumn1","Property":"Name","Width":120},{"Type":"GanttChartColumn","Name":"TestColumn2","Property":"Duration","Width":120}]}}'
        post_request = PostTaskDocumentWithFormatRequest(filename, ProjectFileFormat.CSV, save_options_serialized)
        post_result = self.tasks_api.post_task_document_with_format(post_request)
        self.assertIsNotNone(post_result)
        with open(post_result, encoding='utf-8', errors='ignore') as f:
            self.assertTrue(f.readable())
            self.assertIn('Five to Eight Weeks Before Moving,16 days', f.readline())
            self.assertIn('Planning the Move,3 days', f.readline())
