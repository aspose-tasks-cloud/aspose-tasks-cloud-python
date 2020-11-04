#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="base_test_context.py">
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

import os
import json
import unittest
import warnings
import six
from asposetaskscloud import ApiClient, TasksApi, UploadFileRequest, DeleteFileRequest, DeleteFolderRequest


class BaseTestContext(unittest.TestCase):

    def setUp(self):
        root_path = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
        self.local_test_folder = os.path.join(root_path, 'testData')
        self.remote_test_folder = os.path.join('Temp', 'SdkTests', 'python')
        self.remote_test_out = os.path.join('Temp', 'SdkTests', 'python', 'TestOut')
        creds_path = os.path.join(root_path, '..', 'testConfig.json')
        if not os.path.exists(creds_path):
            raise IOError('Credential file testConfig.json is not found')

        with open(os.path.join(root_path, '..', 'testConfig.json')) as f:
            creds = json.loads(f.read())
        api_client = ApiClient()
        api_client.configuration.host = creds['BaseUrl']
        api_client.configuration.api_key['api_key'] = creds['AppKey']
        api_client.configuration.api_key['app_sid'] = creds['AppSid']
        if 'AuthUrl' in creds:
            api_client.configuration.auth_url = creds['AuthUrl']
        self.tasks_api = TasksApi(api_client)
        self.uploaded_files = []
        if six.PY3:
            warnings.simplefilter("ignore", ResourceWarning)

    def upload_file(self, filename):
        file = os.path.join(self.local_test_folder, filename)
        request = UploadFileRequest(filename, file)
        self.tasks_api.upload_file(request)
        self.uploaded_files.append(filename)

    def tearDown(self):

        request = DeleteFolderRequest('Temp/SdkTests/TestData/Storage', recursive=True)
        self.tasks_api.delete_folder(request)
        for file in self.uploaded_files:
            request = DeleteFileRequest(file)
            self.tasks_api.delete_file(request)

