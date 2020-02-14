# coding: utf-8
# --------------------------------------------------------------------------------
# <copyright company="Aspose" file="put_import_project_from_file_request.py">
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
# coding: utf-8
# --------------------------------------------------------------------------------


class PutImportProjectFromFileRequest(object):
    """
    Request model for put_import_project_from_file operation.
    Initializes a new instance.
    :param name The name of the file.
    :param project_uid Uid of the project to import.
    :param filename The name of the resulting file.
    :param file_type The type of file to import. The supported values are (PrimaveraSqliteDb, PrimaveraXml).
    :param folder The document folder.
    :param storage The document storage.
    :param output_file_format The format of the resulting file.
    """

    def __init__(self, name, project_uid, filename, file_type=None, folder=None, storage=None, output_file_format=None):
        self.name = name
        self.project_uid = project_uid
        self.filename = filename
        self.file_type = file_type
        self.folder = folder
        self.storage = storage
        self.output_file_format = output_file_format


