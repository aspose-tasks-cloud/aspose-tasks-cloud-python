# coding: utf-8
# --------------------------------------------------------------------------------
# <copyright company="Aspose" file="put_task_recurring_info_request.py">
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


class PutTaskRecurringInfoRequest(object):
    """
    Request model for put_task_recurring_info operation.
    Initializes a new instance.
    :param name The name of the file.
    :param task_uid Task Uid.
    :param recurring_info A modified DTO of task's recurring info.
    :param file_name File name to save changes to.
    :param storage The document storage.
    :param folder The document folder.
    """

    def __init__(self, name, task_uid, recurring_info, file_name=None, storage=None, folder=None):
        self.name = name
        self.task_uid = task_uid
        self.recurring_info = recurring_info
        self.file_name = file_name
        self.storage = storage
        self.folder = folder



