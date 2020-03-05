#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_outline_codes.py">
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
from asposetaskscloud import GetOutlineCodesRequest, OutlineCodeItemsResponse, GetOutlineCodeByIndexRequest, \
    OutlineCodeResponse, DeleteOutlineCodeByIndexRequest, AsposeResponse
from test.base_test_context import BaseTestContext


class TestOutlineCodes(BaseTestContext):

    def test_get_outline_codes(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        get_request = GetOutlineCodesRequest(filename)
        get_result = self.tasks_api.get_outline_codes(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, OutlineCodeItemsResponse)
        self.assertEqual(2, len(get_result.outline_codes.list))

    def test_get_outline_code_by_index(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        get_request = GetOutlineCodeByIndexRequest(filename, 1)
        get_result = self.tasks_api.get_outline_code_by_index(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, OutlineCodeResponse)
        self.assertEqual('F45D601B-70C5-E311-A5BA-D43D7E937F92', get_result.outline_code.guid)

    def test_delete_outline_code_by_index(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        delete_request = DeleteOutlineCodeByIndexRequest(filename, 1)
        delete_result = self.tasks_api.delete_outline_code_by_index(delete_request)
        self.assertIsNotNone(delete_result)
        self.assertIsInstance(delete_result, AsposeResponse)

        get_request = GetOutlineCodesRequest(filename)
        get_result = self.tasks_api.get_outline_codes(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, OutlineCodeItemsResponse)
        self.assertEqual(1, len(get_result.outline_codes.list))
        self.assertEqual(1, get_result.outline_codes.list[0].index)
