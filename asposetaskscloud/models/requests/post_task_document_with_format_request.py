# coding: utf-8
# --------------------------------------------------------------------------------
# <copyright company="Aspose" file="post_task_document_with_format_request.py">
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


class PostTaskDocumentWithFormatRequest(object):
    """
    Request model for post_task_document_with_format operation.
    Initializes a new instance.
    :param name The name of the file.
    :param format The format of the resulting file.
    :param save_options Instance of inheritor of SaveOptions class which contains format-specific settings for saving a project.
    :param return_as_zip_archive If parameter is true, HTML resources are included as separate files and returned along with the resulting html file as a zip package.
    :param storage The document storage.
    :param folder The document folder.
    """

    def __init__(self, name, format, save_options, return_as_zip_archive=None, storage=None, folder=None):
        self.name = name
        self.format = format
        self.save_options = save_options
        self.return_as_zip_archive = return_as_zip_archive
        self.storage = storage
        self.folder = folder



