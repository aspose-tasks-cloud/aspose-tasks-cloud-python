#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_project_online.py">
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
import unittest
from asposetaskscloud import GetProjectListRequest, ProjectListResponse, CreateNewProjectRequest, AsposeResponse, \
    UpdateProjectRequest
from test.base_test_context import BaseTestContext


class TestProjectOnline(BaseTestContext):

    @unittest.skip('Ignored because real credentials is required')
    def test_get_project_list(self):
        get_request = GetProjectListRequest('https://your_company_name.sharepoint.com')
        get_request.x_project_online_token = 'SOMESECRETTOKEN'
        get_result = self.tasks_api.get_project_list(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, ProjectListResponse)
        self.assertLessEqual(1, len(get_result.projects.project_info))

    @unittest.skip('Ignored because real credentials is required')
    def test_get_project_list_by_login_with_password(self):
        get_request = GetProjectListRequest('https://your_company_name.sharepoint.com')
        get_request.user_name = 'SomeUserName'
        get_request.x_sharepoint_password = 'SomePassword'
        get_result = self.tasks_api.get_project_list(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, ProjectListResponse)
        self.assertLessEqual(1, len(get_result.projects.project_info))

    @unittest.skip('Ignored because real credentials is required')
    def test_create_new_project(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        post_request = CreateNewProjectRequest(filename, 'https://your_company_name.sharepoint.com')
        post_request.x_project_online_token = 'SOMESECRETTOKEN'
        post_result = self.tasks_api.create_new_project(post_request)
        self.assertIsNotNone(post_result)
        self.assertIsInstance(post_result, AsposeResponse)

    @unittest.skip('Ignored because real credentials is required')
    def test_create_new_project_by_login_with_password(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        post_request = CreateNewProjectRequest(filename, 'https://your_company_name.sharepoint.com')
        post_request.user_name = 'SomeUserName'
        post_request.x_sharepoint_password = 'SomePassword'
        post_result = self.tasks_api.create_new_project(post_request)
        self.assertIsNotNone(post_result)
        self.assertIsInstance(post_result, AsposeResponse)

    @unittest.skip('Ignored because real credentials is required')
    def test_update_project(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        put_request = UpdateProjectRequest(filename, 'https://your_company_name.sharepoint.com')
        put_request.x_project_online_token = 'SOMESECRETTOKEN'
        put_result = self.tasks_api.update_project(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, AsposeResponse)

    @unittest.skip('Ignored because real credentials is required')
    def test_update_project_by_login_with_password(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        put_request = UpdateProjectRequest(filename, 'https://your_company_name.sharepoint.com')
        put_request.user_name = 'SomeUserName'
        put_request.x_sharepoint_password = 'SomePassword'
        put_result = self.tasks_api.update_project(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, AsposeResponse)
