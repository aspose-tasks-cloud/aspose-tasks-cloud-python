#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_file.py">
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
import uuid
from asposetaskscloud import UploadFileRequest, CopyFileRequest, MoveFileRequest, DownloadFileRequest, DeleteFileRequest
from asposetaskscloud.rest import ApiException
from test.base_test_context import BaseTestContext


class TestFile(BaseTestContext):

    def test_upload_file(self):
        filename = 'Home_move_plan.mpp'
        request = UploadFileRequest(os.path.join(self.remote_test_folder, filename), os.path.join(self.local_test_folder, filename))
        result = self.tasks_api.upload_file(request)
        self.assertTrue(len(result._uploaded) == 1 , 'Error has occurred while delete document macros')
        self.uploaded_files.append(os.path.join(self.remote_test_folder, filename))

    def test_copy_file(self):
        filename = 'Home_move_plan.mpp'
        filename_dst = 'TestCopyFileDst' + str(uuid.uuid4()) + '.mpp'
        remote_path_src = os.path.join(self.remote_test_folder, filename)
        remote_path_dst = os.path.join(self.remote_test_folder, filename_dst)
       
        request = UploadFileRequest(remote_path_src, os.path.join(self.local_test_folder, filename))
        self.tasks_api.upload_file(request)

        request = CopyFileRequest(remote_path_src, remote_path_dst)
        response = self.tasks_api.copy_file(request)

        self.assertIsNotNone(response, 'Error has occurred while delete document macros')
        self.uploaded_files.append(remote_path_src)
        self.uploaded_files.append(remote_path_dst)
        
    def test_move_file(self):
        filename = 'Home_move_plan.mpp'
        filename_dst = 'TestMoveFileDst' + str(uuid.uuid4()) + '.mpp'
        remote_path_src = os.path.join(self.remote_test_folder, filename)
        remote_path_dst = os.path.join(self.remote_test_folder, filename_dst)

        request = UploadFileRequest(remote_path_src, os.path.join(self.local_test_folder, filename))
        result = self.tasks_api.upload_file(request)

        request = MoveFileRequest(remote_path_src, remote_path_dst)
        result = self.tasks_api.move_file(request)
        download_dst = self.tasks_api.download_file(DownloadFileRequest(request.dest_path))
        self.assertTrue(len(download_dst) > 0)

        try:
            download_src = self.tasks_api.download_file(DownloadFileRequest(remote_path_src))
            self.assertRaises(ApiException)
        except ApiException as e:
            self.assertEqual(404, e.status, "Status has to be 404")

        self.uploaded_files.append(remote_path_dst)

    def test_delete_file(self):
        filename = 'Home_move_plan.mpp'
        path = os.path.join(self.local_test_folder, filename)
        request = UploadFileRequest(os.path.join(self.remote_test_folder, filename), path)
        self.tasks_api.upload_file(request)

        result = self.tasks_api.delete_file(DeleteFileRequest(os.path.join(self.remote_test_folder, filename)))
        self.assertIsNotNone(result, "Error while deleting file")

    def test_download_file(self):
        filename = 'Home_move_plan.mpp'
        self.upload_file(filename)

        request = DownloadFileRequest(filename)
        response = self.tasks_api.download_file(request)
        self.assertTrue(len(response) > 0, 'Error while downloading file')
