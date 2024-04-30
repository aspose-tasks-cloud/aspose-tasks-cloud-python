#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_views.py">
#   Copyright (c) 2024 Aspose.Tasks Cloud
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
from asposetaskscloud import GetViewsRequest, TableTextStyleResponse, ViewsResponse, View, ItemType, ViewScreen, \
    GetAllTableTextStylesRequest, GetTableTextStyleRequest, Field, TextItemType, Colors, BackgroundPattern, \
    TableTextStyle, CreateTableTextStyleRequest, UpdateTableTextStyleRequest, DeleteTableTextStyleRequest, \
    AsposeResponse
from test.base_test_context import BaseTestContext


class TestViews(BaseTestContext):

    def test_get_views(self):
        filename = 'Home_move_plan.mpp'
        self.upload_file(filename)
        get_request = GetViewsRequest(filename)
        get_result = self.tasks_api.get_views(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, ViewsResponse)
        first_view = get_result.views[0]
        self.assertIsNotNone(first_view)
        self.assertTrue(first_view.show_in_menu)
        self.assertEqual(ItemType.TASKITEM, first_view.type)
        self.assertEqual(ViewScreen.GANTT, first_view.screen)
        self.assertEqual('&Gantt Chart', first_view.name)
        self.assertEqual(1, first_view.uid)

    def test_get_all_table_text_styles(self):
        filename = "NewProductDev.mpp"
        self.upload_file(filename)
        request = GetAllTableTextStylesRequest(filename, 2)
        result = self.tasks_api.get_all_table_text_styles(request)
        self.assertIsNotNone(result)
        self.assertEqual(8, len(result.items))

    def test_get_table_text_style(self):
        filename = "NewProductDev.mpp"
        self.upload_file(filename)
        request = GetTableTextStyleRequest(filename, view_uid=2, row_uid=29)
        result = self.tasks_api.get_table_text_style(request)
        self.assertIsNotNone(result)
        self.assertEqual(29, result.table_text_style.row_uid)
        self.assertEqual(Field.UNDEFINED, result.table_text_style.field)
        self.assertEqual(TextItemType.ALLOCATED, result.table_text_style.item_type)
        self.assertEqual(Colors.TRANSPARENT, result.table_text_style.color)
        self.assertEqual(BackgroundPattern.HOLLOW, result.table_text_style.background_pattern)
        self.assertEqual(Colors.TRANSPARENT, result.table_text_style.background_color)

    def test_create_table_text_style(self):
        filename = "Home_move_plan.mpp"
        self.upload_file(filename)
        new_style = TableTextStyle(3, Field.TASKNAME, TextItemType.ALLOCATED, Colors.RED, BackgroundPattern.HOLLOW,
                                   Colors.GREENYELLOW)
        create_request = CreateTableTextStyleRequest(filename, 1, new_style)
        create_result = self.tasks_api.create_table_text_style(create_request)
        self.assertIsNotNone(create_result)
        self.assertIsInstance(create_result, AsposeResponse)

        get_request = GetTableTextStyleRequest(filename, create_request.view_uid,
                                               new_style.row_uid)
        get_result = self.tasks_api.get_table_text_style(get_request)
        self.assertEqual(new_style.row_uid, get_result.table_text_style.row_uid)
        self.assertEqual(new_style.field, get_result.table_text_style.field)
        self.assertEqual(new_style.item_type, get_result.table_text_style.item_type)
        self.assertEqual(new_style.color, get_result.table_text_style.color)
        self.assertEqual(new_style.background_pattern, get_result.table_text_style.background_pattern)
        self.assertEqual(new_style.background_color, get_result.table_text_style.background_color)

    def test_update_table_text_style(self):
        filename = "NewProductDev.mpp"
        self.upload_file(filename)
        get_request = GetTableTextStyleRequest(filename, 2, 29)
        get_result = self.tasks_api.get_table_text_style(get_request)
        self.assertEqual(Colors.TRANSPARENT, get_result.table_text_style.color)
        self.assertEqual(Colors.TRANSPARENT, get_result.table_text_style.background_color)

        update_request = UpdateTableTextStyleRequest(filename, get_request.view_uid,
                                                     get_result.table_text_style)
        update_request.table_text_style.background_color = Colors.DODGERBLUE
        update_request.table_text_style.color = Colors.ORANGERED
        update_result = self.tasks_api.update_table_text_style(update_request)
        self.assertIsNotNone(update_result)
        self.assertIsInstance(update_result, AsposeResponse)

        get_result = self.tasks_api.get_table_text_style(get_request)
        self.assertEqual(update_request.table_text_style.color, get_result.table_text_style.color)
        self.assertEqual(update_request.table_text_style.background_color,
                         get_result.table_text_style.background_color)

    def test_delete_table_text_style(self):
        filename = "NewProductDev.mpp"
        self.upload_file(filename)
        get_request = GetAllTableTextStylesRequest(filename, 2)
        get_result = self.tasks_api.get_all_table_text_styles(get_request)
        self.assertEqual(8, len(get_result.items))

        delete_request = DeleteTableTextStyleRequest(filename, get_request.view_uid, 29)
        delete_result = self.tasks_api.delete_table_text_style(delete_request)
        self.assertIsNotNone(delete_result)
        self.assertIsInstance(delete_result, AsposeResponse)

        get_result = self.tasks_api.get_all_table_text_styles(get_request)
        self.assertEqual(7, len(get_result.items))
