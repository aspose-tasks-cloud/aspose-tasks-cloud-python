#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_vba.py">
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
from asposetaskscloud import (
    GetVbaProjectRequest,
    GetVbaModuleRequest,
    PostVbaModuleRequest,
    PutVbaModuleRequest,
    DeleteVbaModuleRequest,
    ClearVbaRequest,
    CreateVbaModuleRequest,
    UpdateVbaModuleRequest,
    VbaModuleResponse,
    VbaProjectResponse,
    VbaModuleType,
)
from test.base_test_context import BaseTestContext


class TestVba(BaseTestContext):

    def test_get_vba_project(self):
        filename = 'VbaProject3.mpp'
        self.upload_file(filename)
        get_request = GetVbaProjectRequest(filename)
        get_result = self.tasks_api.get_vba_project(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, VbaProjectResponse)
        self.assertIsNotNone(get_result.vba_project.modules)
        self.assertEqual(8, len(get_result.vba_project.modules))
        self.assertEqual('Module1', get_result.vba_project.modules[1].name)
        self.assertTrue(get_result.vba_project.modules[1].source_code.startswith('Type MEMORYSTATUS'))

    def test_get_vba_module(self):
        filename = 'VbaProject3.mpp'
        self.upload_file(filename)
        get_request = GetVbaModuleRequest(filename, 'Module1')
        get_result = self.tasks_api.get_vba_module(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, VbaModuleResponse)
        self.assertIsNotNone(get_result.module)
        self.assertEqual('Module1', get_result.module.name)

    def test_get_vba_module_by_index(self):
        filename = 'VbaProject3.mpp'
        self.upload_file(filename)
        get_request = GetVbaModuleRequest(filename, '1')
        get_result = self.tasks_api.get_vba_module(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, VbaModuleResponse)
        self.assertIsNotNone(get_result.module)
        self.assertEqual('Module1', get_result.module.name)
        self.assertIsNotNone(get_result.module.source_code)
        self.assertTrue(get_result.module.source_code.startswith('Type MEMORYSTATUS'))

    def test_post_vba_module(self):
        filename = 'VbaProject3.mpp'
        self.upload_file(filename)
        create_request = CreateVbaModuleRequest(
            name='NewTestModule',
            type=VbaModuleType.PROCEDURALMODULE,
            source_code='Sub TestProc()\n    MsgBox "Hello"\nEnd Sub'
        )
        post_request = PostVbaModuleRequest(filename, create_request)
        post_result = self.tasks_api.post_vba_module(post_request)
        self.assertIsNotNone(post_result)
        self.assertIsInstance(post_result, VbaModuleResponse)
        self.assertIsNotNone(post_result.module)
        self.assertEqual('NewTestModule', post_result.module.name)
        self.assertEqual('Sub TestProc()\n    MsgBox "Hello"\nEnd Sub', post_result.module.source_code)

        get_request = GetVbaModuleRequest(filename, 'NewTestModule')
        get_result = self.tasks_api.get_vba_module(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, VbaModuleResponse)
        self.assertIsNotNone(get_result.module)
        self.assertEqual('NewTestModule', get_result.module.name)
        self.assertEqual('Sub TestProc()\n    MsgBox "Hello"\nEnd Sub', get_result.module.source_code)
        self.assertEqual(VbaModuleType.PROCEDURALMODULE, get_result.module.type)

    def test_put_vba_module(self):
        filename = 'VbaProject3.mpp'
        self.upload_file(filename)
        new_source_code = 'Sub UpdatedProc()\n    MsgBox "Updated"\nEnd Sub'
        update_request = UpdateVbaModuleRequest(source_code=new_source_code)
        put_request = PutVbaModuleRequest(filename, 'Module1', update_request)
        put_result = self.tasks_api.put_vba_module(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, VbaModuleResponse)
        self.assertIsNotNone(put_result.module)
        self.assertEqual('Module1', put_result.module.name)
        self.assertEqual(new_source_code, put_result.module.source_code)

        get_request = GetVbaModuleRequest(filename, 'Module1')
        get_result = self.tasks_api.get_vba_module(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, VbaModuleResponse)
        self.assertIsNotNone(get_result.module)
        self.assertEqual('Module1', get_result.module.name)
        self.assertEqual(new_source_code, get_result.module.source_code)

    def test_delete_vba_module(self):
        filename = 'VbaProject3.mpp'
        self.upload_file(filename)
        get_before_request = GetVbaModuleRequest(filename, 'Module1')
        get_before_result = self.tasks_api.get_vba_module(get_before_request)
        self.assertIsNotNone(get_before_result)
        self.assertEqual('Module1', get_before_result.module.name)

        delete_request = DeleteVbaModuleRequest(filename, 'Module1')
        delete_result = self.tasks_api.delete_vba_module(delete_request)
        self.assertIsNotNone(delete_result)

        get_project_request = GetVbaProjectRequest(filename)
        get_project_result = self.tasks_api.get_vba_project(get_project_request)
        self.assertIsNotNone(get_project_result)
        module_names = [m.name for m in get_project_result.vba_project.modules]
        self.assertNotIn('Module1', module_names)

    def test_clear_vba(self):
        filename = 'VbaProject3.mpp'
        self.upload_file(filename)
        get_before_request = GetVbaProjectRequest(filename)
        get_before_result = self.tasks_api.get_vba_project(get_before_request)
        self.assertIsNotNone(get_before_result)
        self.assertGreater(len(get_before_result.vba_project.modules), 0)

        clear_request = ClearVbaRequest(filename)
        clear_result = self.tasks_api.clear_vba(clear_request)
        self.assertIsNotNone(clear_result)

        get_after_request = GetVbaProjectRequest(filename)
        get_after_result = self.tasks_api.get_vba_project(get_after_request)
        self.assertIsNotNone(get_after_result)
        self.assertEqual(0, len(get_after_result.vba_project.modules))
