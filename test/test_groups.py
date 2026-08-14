#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_groups.py">
#   Copyright (c) 2026 Aspose.Tasks Cloud
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
from asposetaskscloud import GetResourceGroupsRequest, GroupItemsResponse, GetResourceGroupRequest, \
    GroupResponse, GetGroupedResourcesRequest, GroupedResourcesResponse, GetTaskGroupsRequest, \
    GetTaskGroupRequest, GetGroupedTasksRequest, GroupedTasksResponse
from test.base_test_context import BaseTestContext


class TestGroups(BaseTestContext):

    def test_get_resource_groups(self):
        filename = 'ProjectWithGroups.mpp'
        self.upload_file(filename)
        request = GetResourceGroupsRequest(filename)
        result = self.tasks_api.get_resource_groups(request)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, GroupItemsResponse)
        self.assertIsNotNone(result.groups)
        self.assertIsNotNone(result.groups.list)
        self.assertGreater(len(result.groups.list), 0)

    def test_get_resource_group(self):
        filename = 'ProjectWithGroups.mpp'
        self.upload_file(filename)
        list_request = GetResourceGroupsRequest(filename)
        list_result = self.tasks_api.get_resource_groups(list_request)
        self.assertIsNotNone(list_result)
        self.assertIsInstance(list_result, GroupItemsResponse)
        self.assertGreater(len(list_result.groups.list), 0)

        group_uid = list_result.groups.list[0].uid

        request = GetResourceGroupRequest(filename, group_uid)
        result = self.tasks_api.get_resource_group(request)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, GroupResponse)
        self.assertIsNotNone(result.group)
        self.assertEqual(group_uid, result.group.uid)
        self.assertIsNotNone(result.group.name)

    def test_get_grouped_resources(self):
        filename = 'ProjectWithGroups.mpp'
        self.upload_file(filename)
        list_request = GetResourceGroupsRequest(filename)
        list_result = self.tasks_api.get_resource_groups(list_request)
        self.assertIsNotNone(list_result)
        self.assertIsInstance(list_result, GroupItemsResponse)
        self.assertGreater(len(list_result.groups.list), 1)

        group_uid = list_result.groups.list[1].uid

        request = GetGroupedResourcesRequest(filename, group_uid)
        result = self.tasks_api.get_grouped_resources(request)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, GroupedResourcesResponse)
        self.assertIsNotNone(result.buckets)
        self.assertGreater(len(result.buckets), 0)

        for bucket in result.buckets:
            self.assertIsNotNone(bucket.key)
            self.assertIsNotNone(bucket.resources)

    def test_get_task_groups(self):
        filename = 'ProjectWithGroups.mpp'
        self.upload_file(filename)
        request = GetTaskGroupsRequest(filename)
        result = self.tasks_api.get_task_groups(request)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, GroupItemsResponse)
        self.assertIsNotNone(result.groups)
        self.assertIsNotNone(result.groups.list)
        self.assertGreater(len(result.groups.list), 1)

    def test_get_task_group(self):
        filename = 'ProjectWithGroups.mpp'
        self.upload_file(filename)
        list_request = GetTaskGroupsRequest(filename)
        list_result = self.tasks_api.get_task_groups(list_request)
        self.assertIsNotNone(list_result)
        self.assertIsInstance(list_result, GroupItemsResponse)
        self.assertGreater(len(list_result.groups.list), 1)

        group_uid = list_result.groups.list[0].uid

        request = GetTaskGroupRequest(filename, group_uid)
        result = self.tasks_api.get_task_group(request)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, GroupResponse)
        self.assertIsNotNone(result.group)
        self.assertEqual(group_uid, result.group.uid)
        self.assertEqual("Percent complete", result.group.name)
        self.assertIsNotNone(result.group.group_criteria)
        self.assertGreater(len(result.group.group_criteria), 0)

    def test_get_grouped_tasks(self):
        filename = 'ProjectWithGroups.mpp'
        self.upload_file(filename)
        list_request = GetTaskGroupsRequest(filename)
        list_result = self.tasks_api.get_task_groups(list_request)
        self.assertIsNotNone(list_result)
        self.assertIsInstance(list_result, GroupItemsResponse)
        self.assertGreater(len(list_result.groups.list), 1)

        group_uid = list_result.groups.list[0].uid

        request = GetGroupedTasksRequest(filename, group_uid)
        result = self.tasks_api.get_grouped_tasks(request)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, GroupedTasksResponse)
        self.assertIsNotNone(result.buckets)
        self.assertGreater(len(result.buckets), 0)

        for bucket in result.buckets:
            self.assertIsNotNone(bucket.key)
            self.assertIsNotNone(bucket.tasks)
