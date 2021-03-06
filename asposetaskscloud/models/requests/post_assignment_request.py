# coding: utf-8
# --------------------------------------------------------------------------------
# <copyright company="Aspose" file="post_assignment_request.py">
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


class PostAssignmentRequest(object):
    """
    Request model for post_assignment operation.
    Initializes a new instance.
    :param name The name of the file.
    :param task_uid The unique id of the task to be assigned.
    :param resource_uid The unique id of the resource to be assigned.
    :param units The units for the new assignment. If not specified, 'cost' value is used.
    :param cost The cost for a new assignment. If not specified, default value is used.
    :param file_name The name of the project document to save changes to. If this parameter is omitted then the changes will be saved to the source project document.
    :param storage The document storage.
    :param folder The document folder.
    """

    def __init__(self, name, task_uid, resource_uid, units=None, cost=None, file_name=None, storage=None, folder=None):
        self.name = name
        self.task_uid = task_uid
        self.resource_uid = resource_uid
        self.units = units
        self.cost = cost
        self.file_name = file_name
        self.storage = storage
        self.folder = folder


