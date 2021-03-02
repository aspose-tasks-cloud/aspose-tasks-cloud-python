#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_resources.py">
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

from dateutil.tz import tzutc

from asposetaskscloud import GetResourcesRequest, ResourceItemsResponse, PostResourceRequest, ResourceItemResponse, \
    GetResourceRequest, ResourceResponse, Baseline, BaselineType, PutResourceRequest, CalculationMode, AsposeResponse, \
    DeleteResourceRequest
from test.base_test_context import BaseTestContext


class TestResources(BaseTestContext):

    def test_get_resources(self):
        filename = 'NewProductDev.mpp'
        self.upload_file(filename)
        get_request = GetResourcesRequest(filename)
        get_result = self.tasks_api.get_resources(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, ResourceItemsResponse)
        self.assertEqual(2, len(get_result.resources.resource_item))
        self.assertEqual(1, get_result.resources.resource_item[1].uid)
        self.assertEqual(1, get_result.resources.resource_item[1].id)
        self.assertEqual('Project manager', get_result.resources.resource_item[1].name)

    def test_get_resource(self):
        filename = 'sample.mpp'
        self.upload_file(filename)
        get_request = GetResourceRequest(filename, 1)
        get_result = self.tasks_api.get_resource(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, ResourceResponse)
        self.assertEqual(10, get_result.resource.standard_rate)
        self.assertEqual(datetime(2003, 1, 7, 8, tzinfo=tzutc()), get_result.resource.start)
        self.assertEqual('10.00:00:00', get_result.resource.work)
        self.assertEqual(datetime(2003, 3, 17, 17, tzinfo=tzutc()), get_result.resource.finish)
        self.assertIsNone(get_result.resource.overtime_work)
        self.assertEqual(2015, get_result.resource.cost)

    def test_post_resource(self):
        filename = 'Home_move_plan.mpp'
        self.upload_file(filename)
        get_request = GetResourcesRequest(filename)
        get_result = self.tasks_api.get_resources(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, ResourceItemsResponse)
        count = len(get_result.resources.resource_item)
        post_request = PostResourceRequest(filename, 'new resource')
        post_result = self.tasks_api.post_resource(post_request)
        self.assertIsNotNone(post_result)
        self.assertIsInstance(post_result, ResourceItemResponse)
        get_result = self.tasks_api.get_resources(get_request)
        self.assertEqual(count + 1, len(get_result.resources.resource_item))
        added_resource = next(r for r in get_result.resources.resource_item if r.uid == post_result.resource_item.uid)
        self.assertEqual('new resource', added_resource.name)

    def test_put_resource(self):
        filename = 'sample.mpp'
        self.upload_file(filename)
        get_request = GetResourceRequest(filename, 1)
        get_result = self.tasks_api.get_resource(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, ResourceResponse)
        baseline = Baseline(BaselineType.BASELINE1, cost=44)
        resource = get_result.resource
        resource.name = 'Modified Resource1'
        resource.cost = 200
        resource.start = datetime(2000, 10, 10)
        resource.work = '4.04:10:00'
        resource.finish = datetime(2000, 10, 10)
        resource.overtime_work = '4.04:00:00'
        resource.standard_rate = 101
        resource.baselines = [baseline]
        put_request = PutResourceRequest(filename, 1, resource, CalculationMode.NONE, False)
        put_result = self.tasks_api.put_resource(put_request)
        self.assertIsNotNone(put_result)
        self.assertIsInstance(put_result, ResourceResponse)
        self.assertEqual(1, len(put_result.resource.baselines))
        self.assertEqual(BaselineType.BASELINE1, put_result.resource.baselines[0].baseline_number)
        self.assertEqual(44, put_result.resource.baselines[0].cost)
        self.assertEqual(resource.standard_rate, put_result.resource.standard_rate)
        self.assertEqual(resource.start.date(), put_result.resource.start.date())
        self.assertEqual(resource.work, put_result.resource.work)
        self.assertEqual(resource.finish.date(), put_result.resource.finish.date())
        self.assertEqual(resource.overtime_work, put_result.resource.overtime_work)
        self.assertEqual(resource.cost, put_result.resource.cost)

    def test_delete_resource(self):
        filename = 'Plan_with_resource.mpp'
        self.upload_file(filename)
        get_request = GetResourcesRequest(filename)
        get_result = self.tasks_api.get_resources(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, ResourceItemsResponse)
        resource_count_before_delete = len(get_result.resources.resource_item)
        delete_request = DeleteResourceRequest(filename, 1)
        delete_result = self.tasks_api.delete_resource(delete_request)
        self.assertIsNotNone(delete_result)
        self.assertIsInstance(delete_result, AsposeResponse)
        get_result = self.tasks_api.get_resources(get_request)
        self.assertGreater(resource_count_before_delete, len(get_result.resources.resource_item))
