# coding: utf-8
# --------------------------------------------------------------------------------
# <copyright company="Aspose" file="put_document_property_request.py">
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


class PutDocumentPropertyRequest(object):
    """
    Request model for put_document_property operation.
    Initializes a new instance.
    :param name The document name.
    :param property_name The property name.
    :param _property DocumentProperty with new property value.
    :param storage The document storage.
    :param folder The document folder.
    :param filename Name of the project document to save changes to. If this parameter is omitted then the changes will be saved to the source project document.
    """

    def __init__(self, name, property_name, _property, storage=None, folder=None, filename=None):
        self.name = name
        self.property_name = property_name
        self._property = _property
        self.storage = storage
        self.folder = folder
        self.filename = filename



