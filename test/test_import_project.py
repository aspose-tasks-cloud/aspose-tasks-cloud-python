#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_import_project.py">
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

from asposetaskscloud import PutImportProjectFromFileRequest, ImportedProjectType, ProjectFileFormat, AsposeResponse, \
    GetTasksRequest, TaskItemsResponse, PutImportProjectFromDbRequest, ProjectDatabaseType, GetProjectIdsRequest, \
    ProjectIdsResponse, PutImportProjectFromProjectOnlineRequest, DownloadFileRequest
from test.base_test_context import BaseTestContext


class TestImportProject(BaseTestContext):

    def test_put_import_project_from_file(self):
        filename = 'p6_multiproject.xml'
        self.upload_file(filename)
        put_request = PutImportProjectFromFileRequest(filename, "111", 'imported_from_primavera.xml',
                                                      ImportedProjectType.PRIMAVERAXML,
                                                      output_file_format=ProjectFileFormat.P6XML)
        put_result = self.tasks_api.put_import_project_from_file(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, AsposeResponse)
        get_request = GetTasksRequest('imported_from_primavera.xml')
        get_result = self.tasks_api.get_tasks(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskItemsResponse)
        self.assertEqual(12, len(get_result.tasks.task_item))

    @unittest.skip('Ignored because real credentials is required')
    def test_put_import_project_from_db(self):
        put_request = PutImportProjectFromDbRequest()
        put_request.connection_string = "Data Source=db.contoso.com;Initial Catalog=ProjectServer;Persist Security Info=True;User ID=sa;Password=pwd;"
        put_request.database_type = ProjectDatabaseType.MSP
        put_request.filename = "imported_from_db.xml"
        put_request.project_uid = "E6426C44-D6CB-4B9C-AF16-48910ACE0F54"
        put_request.database_schema = "dbo"
        put_request.format = ProjectFileFormat.P6XML
        put_result = self.tasks_api.put_import_project_from_db(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, AsposeResponse)
        get_request = GetProjectIdsRequest("imported_from_db")
        get_result = self.tasks_api.get_project_ids(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, ProjectIdsResponse)
        self.assertEqual(["1"], get_result.project_ids)

    @unittest.skip('Ignored because real credentials is required')
    def test_put_import_project_from_project_online(self):
        put_request = PutImportProjectFromProjectOnlineRequest('NewProductDev.mpp', 'E6426C44-D6CB-4B9C-AF16-48910ACE0F54',
                                                               'https://your_company_name.sharepoint.com')
        put_request.x_project_online_token = 'SOMESECRETTOKEN';
        put_request.format = ProjectFileFormat.P6XML
        put_result = self.tasks_api.put_import_project_from_project_online(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, AsposeResponse)
        get_request = DownloadFileRequest('NewProductDev.mpp')
        get_result = self.tasks_api.download_file(get_request)
        self.assertIsNotNone(get_result)
        with open(get_result) as f:
            self.assertTrue(f.readable())

    @unittest.skip('Ignored because real credentials is required')
    def test_put_import_project_from_project_online_by_login_with_password(self):
        put_request = PutImportProjectFromProjectOnlineRequest('NewProductDev.mpp', 'E6426C44-D6CB-4B9C-AF16-48910ACE0F54',
                                                               'https://your_company_name.sharepoint.com')
        put_request.user_name = 'SomeUserName'
        put_request.x_sharepoint_password = 'SomePassword'
        put_request.format = ProjectFileFormat.P6XML
        put_result = self.tasks_api.put_import_project_from_project_online(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, AsposeResponse)
        get_request = DownloadFileRequest('NewProductDev.mpp')
        get_result = self.tasks_api.download_file(get_request)
        self.assertIsNotNone(get_result)
        with open(get_result) as f:
            self.assertTrue(f.readable())
