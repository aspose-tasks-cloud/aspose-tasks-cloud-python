# coding: utf-8
# --------------------------------------------------------------------------------
# <copyright company="Aspose" file="put_import_project_from_db_request.py">
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


class PutImportProjectFromDbRequest(object):
    """
    Request model for put_import_project_from_db operation.
    Initializes a new instance.
    :param database_type The type of source database. The supported values are (Msp, Mpd, Primavera).
    :param connection_string The connection string to the source database.
    :param project_uid Uid of the project to import.
    :param filename The name of the resulting file.
    :param format Format of the resulting file. The import to Mpp format is not supported.
    :param folder The document folder.
    :param storage The document storage.
    :param database_schema Schema of Microsoft project database (if applicable)
    """

    def __init__(self, database_type, connection_string, project_uid, filename, format=None, folder=None, storage=None, database_schema=None):
        self.database_type = database_type
        self.connection_string = connection_string
        self.project_uid = project_uid
        self.filename = filename
        self.format = format
        self.folder = folder
        self.storage = storage
        self.database_schema = database_schema


