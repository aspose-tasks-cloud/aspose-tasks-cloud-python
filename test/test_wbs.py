#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_wbs.py">
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
from asposetaskscloud import GetWbsDefinitionRequest, WBSDefinitionResponse, PutRenumberWbsCodeRequest, AsposeResponse
from test.base_test_context import BaseTestContext


class TestWbs(BaseTestContext):

    def test_get_wbs_definition(self):
        filename = 'WBSDefinition.mpp'
        self.upload_file(filename)
        get_request = GetWbsDefinitionRequest(filename)
        get_result = self.tasks_api.get_wbs_definition(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, WBSDefinitionResponse)
        self.assertIsNotNone(get_result.wbs_definition)
        self.assertTrue(get_result.wbs_definition.generate_wbs_code)
        self.assertTrue(get_result.wbs_definition.verify_uniqueness)

    def test_put_renumber_wbs_code(self):
        filename = 'WBSDefinition.mpp'
        self.upload_file(filename)
        get_request = PutRenumberWbsCodeRequest(filename, [])
        get_result = self.tasks_api.put_renumber_wbs_code(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, AsposeResponse)
