#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_document_properties.py">
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
from datetime import datetime
from asposetaskscloud import GetDocumentPropertiesRequest, DocumentPropertiesResponse, GetDocumentPropertyRequest, \
    DocumentPropertyResponse, DocumentProperty, PutDocumentPropertyRequest, PostDocumentPropertyRequest
from test.base_test_context import BaseTestContext


class TestDocumentProperties(BaseTestContext):

    def test_get_document_properties(self):
        filename = 'Home_move_plan.mpp'
        self.upload_file(filename)
        request = GetDocumentPropertiesRequest(filename)
        result = self.tasks_api.get_document_properties(request)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, DocumentPropertiesResponse)
        self.assertIsNotNone(result.properties)
        self.assertEqual(63, len(result.properties.list))
        self.assertEqual('Title', result.properties.list[0].name)
        self.assertEqual('Home Move', result.properties.list[0].value)

    def test_get_document_property(self):
        filename = 'Home_move_plan.mpp'
        self.upload_file(filename)
        request = GetDocumentPropertyRequest(filename, 'Title')
        result = self.tasks_api.get_document_property(request)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, DocumentPropertyResponse)
        self.assertIsNotNone(result._property)
        self.assertEqual('Title', result._property.name)
        self.assertEqual('Home Move', result._property.value)

    def test_put_document_property(self):
        filename = 'Home_move_plan.mpp'
        self.upload_file(filename)
        _property = DocumentProperty('Title', 'New title value')
        put_request = PutDocumentPropertyRequest(filename, 'Title', _property)
        self.tasks_api.put_document_property(put_request)
        get_request = GetDocumentPropertyRequest(filename, 'Title')
        result = self.tasks_api.get_document_property(get_request)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, DocumentPropertyResponse)
        self.assertIsNotNone(result._property)
        self.assertEqual('Title', result._property.name)
        self.assertEqual('New title value', result._property.value)

    def test_post_document_property(self):
        filename = 'Home_move_plan.mpp'
        self.upload_file(filename)
        _property = DocumentProperty('Title', 'New title value')
        post_request = PostDocumentPropertyRequest(filename, 'Title', _property)
        self.tasks_api.post_document_property(post_request)
        get_request = GetDocumentPropertyRequest(filename, 'Title')
        result = self.tasks_api.get_document_property(get_request)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, DocumentPropertyResponse)
        self.assertIsNotNone(result._property)
        self.assertEqual('New title value', result._property.value)

    def test_post_document_property_negative(self):
        filename = 'Home_move_plan.mpp'
        self.upload_file(filename)
        _property = DocumentProperty('new property', 'New property value')
        post_request = PostDocumentPropertyRequest(filename, 'new property', _property)
        self.tasks_api.post_document_property(post_request)
        get_request = GetDocumentPropertyRequest(filename, 'new property')
        result = self.tasks_api.get_document_property(get_request)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, DocumentPropertyResponse)
        self.assertIsNone(result._property)
