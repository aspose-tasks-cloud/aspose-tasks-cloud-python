# coding: utf-8
# --------------------------------------------------------------------------------
# <copyright company="Aspose" file="put_move_task_request.py">
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


class PutMoveTaskRequest(object):
    """
    Request model for put_move_task operation.
    Initializes a new instance.
    :param name The name of the file.
    :param task_uid Unique id of the task to be moved.
    :param parent_task_uid Unique id of the new parent task.
    :param file_name The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document. 
    :param storage The document storage.
    :param folder The document folder.
    """

    def __init__(self, name, task_uid, parent_task_uid, file_name=None, storage=None, folder=None):
        self.name = name
        self.task_uid = task_uid
        self.parent_task_uid = parent_task_uid
        self.file_name = file_name
        self.storage = storage
        self.folder = folder


