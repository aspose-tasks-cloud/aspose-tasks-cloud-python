#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_vba.py">
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
from asposetaskscloud import GetVbaProjectRequest, VbaProjectResponse
from test.base_test_context import BaseTestContext


class TestVba(BaseTestContext):

    def test_get_vba_project(self):
        filename = 'VbaProject3.mpp'
        self.upload_file(filename)
        get_request = GetVbaProjectRequest(filename)
        get_result = self.tasks_api.get_vba_project(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, VbaProjectResponse)
        self.assertIsNotNone(get_result.vba_project.modules)
        self.assertEqual(7, len(get_result.vba_project.modules))
        self.assertEqual('Module1', get_result.vba_project.modules[0].name)
        self.assertTrue(get_result.vba_project.modules[0].source_code.startswith('Type MEMORYSTATUS'))
