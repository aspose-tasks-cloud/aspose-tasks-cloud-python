#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_tasks_primavera_properties.py">
#   Copyright (c) 2022 Aspose.Tasks Cloud
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

from asposetaskscloud import GetPrimaveraTaskPropertiesRequest, PrimaveraTaskPropertiesResponse, PrimaveraDurationType, \
    PrimaveraActivityType, PrimaveraPercentCompleteType
from test.base_test_context import BaseTestContext


class TestTasksPrimaveraProperties(BaseTestContext):

    def test_get_primavera_task_properties(self):
        filename = 'p6_multiproject.xml'
        self.upload_file(filename)
        get_request = GetPrimaveraTaskPropertiesRequest(filename, 1)
        get_result = self.tasks_api.get_primavera_task_properties(get_request)
        self.assertIsInstance(get_result, PrimaveraTaskPropertiesResponse)
        self.assertIsNotNone(get_result.primavera_properties)

        entity = get_result.primavera_properties

        self.assertEqual(0, entity.sequence_number)
        self.assertEqual("A1040", entity.activity_id)
        self.assertEqual(datetime(2000, 10, 12, 8, 0), entity.remaining_early_start)
        self.assertEqual(datetime(2000, 10, 12, 17, 0), entity.remaining_early_finish)
        self.assertEqual(datetime(2000, 10, 12, 8, 0), entity.remaining_late_start)
        self.assertEqual(datetime(2000, 10, 12, 17, 0), entity.remaining_late_finish)
        self.assertEqual("Fixed Units", entity.raw_duration_type)
        self.assertEqual("Task Dependent", entity.raw_activity_type)
        self.assertEqual("Units", entity.raw_complete_percent_type)
        self.assertEqual("Not Started", entity.raw_status)
        self.assertEqual(PrimaveraDurationType.FIXEDUNITS, entity.duration_type)
        self.assertEqual(PrimaveraActivityType.TASKDEPENDENT, entity.activity_type)
        self.assertEqual(PrimaveraPercentCompleteType.UNITS, entity.percent_complete_type)
