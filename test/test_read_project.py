#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_read_project.py">
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
from asposetaskscloud import GetProjectIdsRequest, ProjectIdsResponse, GetTaskDocumentRequest
from test.base_test_context import BaseTestContext


class TestReadProject(BaseTestContext):

    def test_get_project_ids(self):
        filename = 'p6_multiproject.xml'
        self.upload_file(filename)
        get_request = GetProjectIdsRequest(filename)
        get_result = self.tasks_api.get_project_ids(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, ProjectIdsResponse)
        self.assertEqual(['1', '111'], get_result.project_ids)

    def test_get_task_document(self):
        filename = 'testXer.xer'
        self.upload_file(filename)
        get_request = GetTaskDocumentRequest(filename)
        get_result = self.tasks_api.get_task_document(get_request)
        self.assertIsNotNone(get_result)
        with open(get_result) as f:
            self.assertTrue(f.readable())
