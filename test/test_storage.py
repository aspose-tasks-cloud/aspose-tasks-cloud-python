#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_storage.py">
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
from asposetaskscloud import GetDiscUsageRequest, DiscUsage, GetFileVersionsRequest, FileVersions, ObjectExistsRequest, \
    ObjectExist, StorageExistsRequest, StorageExist
from test.base_test_context import BaseTestContext


class TestStorage(BaseTestContext):

    def test_get_disc_usage(self):
        get_request = GetDiscUsageRequest()
        get_result = self.tasks_api.get_disc_usage(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, DiscUsage)
        self.assertTrue(get_result.total_size > 0)

    def test_get_file_versions(self):
        filename = 'sample.mpp'
        self.upload_file(filename)
        get_request = GetFileVersionsRequest(filename)
        get_result = self.tasks_api.get_file_versions(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, FileVersions)
        self.assertIsNotNone(get_result.value)
        self.assertTrue(any(f.is_latest for f in get_result.value))

    def test_object_exists(self):
        filename = 'SomeNonexistentFileName'
        get_request = ObjectExistsRequest(filename)
        get_result = self.tasks_api.object_exists(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, ObjectExist)
        self.assertFalse(get_result.exists)

    def test_storage_exists(self):
        filename = 'SomeNonexistentStorageName'
        get_request = StorageExistsRequest(filename)
        get_result = self.tasks_api.storage_exists(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, StorageExist)
        self.assertFalse(get_result.exists)
