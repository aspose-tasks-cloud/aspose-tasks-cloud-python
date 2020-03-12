#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_report.py">
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
from asposetaskscloud import GetReportPdfRequest, ReportType, GetCriticalPathRequest, TaskItemsResponse, \
    GetRiskAnalysisReportRequest, ProbabilityDistributionType, ConfidenceLevel
from test.base_test_context import BaseTestContext


class TestReport(BaseTestContext):

    def test_get_report_pdf(self):
        filename = 'Home_move_plan.mpp'
        self.upload_file(filename)
        get_request = GetReportPdfRequest(filename, ReportType.MILESTONES)
        get_result = self.tasks_api.get_report_pdf(get_request)
        self.assertIsNotNone(get_result)
        with open(get_result, encoding='utf-8', errors='ignore') as f:
            self.assertTrue(f.readable())
            self.assertIn('%PDF-1.5', f.readline())

    def test_get_critical_path(self):
        filename = 'Home_move_plan.mpp'
        self.upload_file(filename)
        get_request = GetCriticalPathRequest(filename)
        get_result = self.tasks_api.get_critical_path(get_request)
        self.assertIsNotNone(get_result)
        self.assertIsInstance(get_result, TaskItemsResponse)
        self.assertEqual(76, len(get_result.tasks.task_item))

    def test_get_risk_analysis_report(self):
        filename = 'Home_move_plan.mpp'
        self.upload_file(filename)
        get_request = GetRiskAnalysisReportRequest(filename, 1, ProbabilityDistributionType.NORMAL, 80, 130)
        get_request.confidence_level = ConfidenceLevel.CL85
        get_request.iterations = 200
        get_result = self.tasks_api.get_risk_analysis_report(get_request)
        self.assertIsNotNone(get_result)
        with open(get_result, encoding='utf-8', errors='ignore') as f:
            self.assertTrue(f.readable())
            self.assertIn('%PDF-1.5', f.readline())
