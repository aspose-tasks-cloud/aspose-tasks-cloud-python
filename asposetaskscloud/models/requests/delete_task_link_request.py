# coding: utf-8
# --------------------------------------------------------------------------------
# <copyright company="Aspose" file="delete_task_link_request.py">
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
# --------------------------------------------------------------------------------


class DeleteTaskLinkRequest(object):
    """
    Request model for delete_task_link operation.
    Initializes a new instance.
    :param name The name of the file.
    :param index Index of the task link object. See TaskLink.Index property.
    :param storage The document storage.
    :param folder The document folder.
    :param file_name The name of the project document to save changes to.  If this parameter is omitted then the changes will be saved to the source project document.
    """

    def __init__(self, name, index, storage=None, folder=None, file_name=None):
        self.name = name
        self.index = index
        self.storage = storage
        self.folder = folder
        self.file_name = file_name


