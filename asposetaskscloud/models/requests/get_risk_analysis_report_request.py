# coding: utf-8
# --------------------------------------------------------------------------------
# <copyright company="Aspose" file="get_risk_analysis_report_request.py">
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


class GetRiskAnalysisReportRequest(object):
    """
    Request model for get_risk_analysis_report operation.
    Initializes a new instance.
    :param name The name of the file.
    :param task_uid The uid of the task for which this risk will be applied in Monte Carlo simulation.
    :param distribution_type Gets or sets the probability distribution used in Monte Carlo simulation. The default value is ProbabilityDistributionType.Normal.
    :param optimistic The percentage of the most likely task duration which can happen in the best possible project scenario. The default value is 75, which means that if the estimated specified task duration is 4 days then the optimistic duration will be 3 days.
    :param pessimistic The percentage of the most likely task duration which can happen in the worst possible project scenario. The default value is 125, which means that if the estimated specified task duration is 4 days then the pessimistic duration will be 5 days.
    :param confidence_level Gets or sets the confidence level that correspond to the percentage of the time the actual generated values will be within optimistic and pessimistic estimates. The default value is CL99.
    :param iterations The number of iterations to use in Monte Carlo simulation. The default value is 100.
    :param storage The document storage.
    :param folder The folder storage.
    :param file_name The resulting report fileName.
    """

    def __init__(self, name, task_uid, distribution_type=None, optimistic=None, pessimistic=None, confidence_level=None, iterations=None, storage=None, folder=None, file_name=None):
        self.name = name
        self.task_uid = task_uid
        self.distribution_type = distribution_type
        self.optimistic = optimistic
        self.pessimistic = pessimistic
        self.confidence_level = confidence_level
        self.iterations = iterations
        self.storage = storage
        self.folder = folder
        self.file_name = file_name



