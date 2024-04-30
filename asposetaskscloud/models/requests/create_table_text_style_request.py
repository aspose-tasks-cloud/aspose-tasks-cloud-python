# coding: utf-8
# --------------------------------------------------------------------------------
# <copyright company="Aspose" file="create_table_text_style_request.py">
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


class CreateTableTextStyleRequest(object):
    """
    Request model for create_table_text_style operation.
    Initializes a new instance.
    :param name The name of the file.
    :param view_uid Uid of the view.
    :param table_text_style A DTO of TableTextStyle to create
    :param file_name File name to save changes to.
    :param storage The document storage.
    :param folder The document folder.
    """

    def __init__(self, name, view_uid, table_text_style, file_name=None, storage=None, folder=None):
        self.name = name
        self.view_uid = view_uid
        self.table_text_style = table_text_style
        self.file_name = file_name
        self.storage = storage
        self.folder = folder


