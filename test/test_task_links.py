#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_task_links.py">
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
from asposetaskscloud import GetTaskLinksRequest, TaskLinksResponse, TaskLink, TaskLinkType, TimeUnitType, \
    PostTaskLinkRequest, AsposeResponse, PutTaskLinkRequest, TaskLinkResponse, DeleteTaskLinkRequest
from test.base_test_context import BaseTestContext


class TestTaskLinks(BaseTestContext):

    def test_get_task_links(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        get_request = GetTaskLinksRequest(filename)
        get_result = self.tasks_api.get_task_links(get_request)
        self.assertIsInstance(get_result, TaskLinksResponse)
        self.assertIsNotNone(get_result.task_links)
        self.assertEqual(24, len(get_result.task_links))

    def test_post_task_link(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        task_link = TaskLink(predecessor_uid=28, successor_uid=30, link_type=TaskLinkType.STARTTOSTART, lag=9600)
        task_link.lag_format = TimeUnitType.DAY
        post_request = PostTaskLinkRequest(filename, task_link)
        post_result = self.tasks_api.post_task_link(post_request)
        self.assertIsNotNone(post_result)
        self.assertIsInstance(post_result, AsposeResponse)

    def test_put_task_link(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        get_request = GetTaskLinksRequest(filename)
        get_result = self.tasks_api.get_task_links(get_request)
        task_link_to_edit = get_result.task_links[0]

        # Modification of PredecessorUid and SuccessorUid fields is not supported.
        task_link_to_edit.link_type = TaskLinkType.STARTTOFINISH
        task_link_to_edit.lag = 9600
        task_link_to_edit.lag_format = TimeUnitType.DAY
        put_request = PutTaskLinkRequest(filename, 1, task_link_to_edit)
        put_result = self.tasks_api.put_task_link(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, TaskLinkResponse)

        get_result = self.tasks_api.get_task_links(get_request)
        self.assertIsNotNone(get_result.task_links)
        self.assertEqual(TaskLinkType.STARTTOFINISH, get_result.task_links[0].link_type)
        self.assertEqual(9600, get_result.task_links[0].lag)
        self.assertEqual(TimeUnitType.DAY, get_result.task_links[0].lag_format)

    def test_delete_task_link(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        delete_request = DeleteTaskLinkRequest(filename, 1)
        delete_result = self.tasks_api.delete_task_link(delete_request)
        self.assertIsNotNone(delete_result)
        self.assertIsInstance(delete_result, AsposeResponse)

        get_request = GetTaskLinksRequest(filename)
        get_result = self.tasks_api.get_task_links(get_request)
        self.assertIsInstance(get_result, TaskLinksResponse)
        self.assertIsNotNone(get_result.task_links)
        self.assertEqual(23, len(get_result.task_links))
