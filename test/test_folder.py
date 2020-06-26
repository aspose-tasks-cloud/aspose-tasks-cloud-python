#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_folder.py">
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

import uuid
import asposetaskscloud.models.requests
from test.base_test_context import BaseTestContext
from asposetaskscloud.rest import ApiException

class TestFolder(BaseTestContext):
    test_folder = 'Temp/SdkTests/TestData/Storage'

    def test_create_folder(self):
        folder_uuid = str(uuid.uuid4())
        folder_path = self.test_folder + '/TestCreateFolder' + folder_uuid
        request = asposetaskscloud.models.requests.CreateFolderRequest(folder_path)
        response = self.tasks_api.create_folder(request)
        self.assertIsNotNone(response, "Folder has not been created")
        self.tasks_api.delete_folder(asposetaskscloud.models.requests.DeleteFolderRequest(folder_path))

    def test_delete_folder(self):
        folder_uuid = str(uuid.uuid4())
        folder_path = self.test_folder + '/TestCreateFolder' + folder_uuid
        request = asposetaskscloud.models.requests.CreateFolderRequest(folder_path)
        self.tasks_api.create_folder(request)
        request = asposetaskscloud.models.requests.DeleteFolderRequest(folder_path)
        response = self.tasks_api.delete_folder(request)
        self.assertIsNotNone(response, "Folder has not been deleted")

    def test_get_files_list(self):
        request = asposetaskscloud.models.requests.GetFilesListRequest(self.test_folder)
        response = self.tasks_api.get_files_list(request)
        self.assertTrue(True)

    def test_copy_folder(self):
        folder_uuid = str(uuid.uuid4())
        folder_path_src = self.test_folder + '/TestCopyFolderSrc' + folder_uuid
        folder_path_dst = self.test_folder + '/TestCopyFolderDst' + folder_uuid
        self.tasks_api.create_folder(asposetaskscloud.models.requests.CreateFolderRequest(folder_path_src))

        request = asposetaskscloud.models.requests.CopyFolderRequest(folder_path_dst, folder_path_src)
        self.tasks_api.copy_folder(request)

        response = self.tasks_api.get_files_list(asposetaskscloud.models.requests.GetFilesListRequest(self.test_folder))
        self.assertIsNotNone(response)
        self.tasks_api.delete_folder(asposetaskscloud.models.requests.DeleteFolderRequest(folder_path_src))
        self.tasks_api.delete_folder(asposetaskscloud.models.requests.DeleteFolderRequest(folder_path_dst))

    def test_move_folder(self):
        folder_uuid = str(uuid.uuid4())
        folder_path_src = self.test_folder + '/TestCopyFolderSrc' + folder_uuid
        folder_path_dst = self.test_folder + '/TestCopyFolderDst' + folder_uuid
        self.tasks_api.create_folder(asposetaskscloud.models.requests.CreateFolderRequest(folder_path_src))

        request = asposetaskscloud.models.requests.MoveFolderRequest(folder_path_dst, folder_path_src)
        self.tasks_api.move_folder(request)

        response = self.tasks_api.get_files_list(asposetaskscloud.models.requests.GetFilesListRequest(self.test_folder))
        self.tasks_api.delete_folder(asposetaskscloud.models.requests.DeleteFolderRequest(folder_path_dst))