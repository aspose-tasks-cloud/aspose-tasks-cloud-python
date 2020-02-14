# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="TimephasedDataType.py">
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
# -----------------------------------------------------------------------------------
import pprint
import re  # noqa: F401

import six


class TimephasedDataType(object):
    """
    """

    """
    allowed enum values
    """
    ASSIGNMENTREMAININGWORK = "AssignmentRemainingWork"
    ASSIGNMENTACTUALWORK = "AssignmentActualWork"
    ASSIGNMENTACTUALOVERTIMEWORK = "AssignmentActualOvertimeWork"
    ASSIGNMENTBASELINEWORK = "AssignmentBaselineWork"
    ASSIGNMENTBASELINECOST = "AssignmentBaselineCost"
    ASSIGNMENTACTUALCOST = "AssignmentActualCost"
    RESOURCEBASELINEWORK = "ResourceBaselineWork"
    RESOURCEBASELINECOST = "ResourceBaselineCost"
    TASKBASELINEWORK = "TaskBaselineWork"
    TASKBASELINECOST = "TaskBaselineCost"
    TASKPERCENTCOMPLETE = "TaskPercentComplete"
    ASSIGNMENTBASELINE1WORK = "AssignmentBaseline1Work"
    ASSIGNMENTBASELINE1COST = "AssignmentBaseline1Cost"
    TASKBASELINE1WORK = "TaskBaseline1Work"
    TASKBASELINE1COST = "TaskBaseline1Cost"
    RESOURCEBASELINE1WORK = "ResourceBaseline1Work"
    RESOURCEBASELINE1COST = "ResourceBaseline1Cost"
    ASSIGNMENTBASELINE2WORK = "AssignmentBaseline2Work"
    ASSIGNMENTBASELINE2COST = "AssignmentBaseline2Cost"
    TASKBASELINE2WORK = "TaskBaseline2Work"
    TASKBASELINE2COST = "TaskBaseline2Cost"
    RESOURCEBASELINE2WORK = "ResourceBaseline2Work"
    RESOURCEBASELINE2COST = "ResourceBaseline2Cost"
    ASSIGNMENTBASELINE3WORK = "AssignmentBaseline3Work"
    ASSIGNMENTBASELINE3COST = "AssignmentBaseline3Cost"
    TASKBASELINE3WORK = "TaskBaseline3Work"
    TASKBASELINE3COST = "TaskBaseline3Cost"
    RESOURCEBASELINE3WORK = "ResourceBaseline3Work"
    RESOURCEBASELINE3COST = "ResourceBaseline3Cost"
    ASSIGNMENTBASELINE4WORK = "AssignmentBaseline4Work"
    ASSIGNMENTBASELINE4COST = "AssignmentBaseline4Cost"
    TASKBASELINE4WORK = "TaskBaseline4Work"
    TASKBASELINE4COST = "TaskBaseline4Cost"
    RESOURCEBASELINE4WORK = "ResourceBaseline4Work"
    RESOURCEBASELINE4COST = "ResourceBaseline4Cost"
    ASSIGNMENTBASELINE5WORK = "AssignmentBaseline5Work"
    ASSIGNMENTBASELINE5COST = "AssignmentBaseline5Cost"
    TASKBASELINE5WORK = "TaskBaseline5Work"
    TASKBASELINE5COST = "TaskBaseline5Cost"
    RESOURCEBASELINE5WORK = "ResourceBaseline5Work"
    RESOURCEBASELINE5COST = "ResourceBaseline5Cost"
    ASSIGNMENTBASELINE6WORK = "AssignmentBaseline6Work"
    ASSIGNMENTBASELINE6COST = "AssignmentBaseline6Cost"
    TASKBASELINE6WORK = "TaskBaseline6Work"
    TASKBASELINE6COST = "TaskBaseline6Cost"
    RESOURCEBASELINE6WORK = "ResourceBaseline6Work"
    RESOURCEBASELINE6COST = "ResourceBaseline6Cost"
    ASSIGNMENTBASELINE7WORK = "AssignmentBaseline7Work"
    ASSIGNMENTBASELINE7COST = "AssignmentBaseline7Cost"
    TASKBASELINE7WORK = "TaskBaseline7Work"
    TASKBASELINE7COST = "TaskBaseline7Cost"
    RESOURCEBASELINE7WORK = "ResourceBaseline7Work"
    RESOURCEBASELINE7COST = "ResourceBaseline7Cost"
    ASSIGNMENTBASELINE8WORK = "AssignmentBaseline8Work"
    ASSIGNMENTBASELINE8COST = "AssignmentBaseline8Cost"
    TASKBASELINE8WORK = "TaskBaseline8Work"
    TASKBASELINE8COST = "TaskBaseline8Cost"
    RESOURCEBASELINE8WORK = "ResourceBaseline8Work"
    RESOURCEBASELINE8COST = "ResourceBaseline8Cost"
    ASSIGNMENTBASELINE9WORK = "AssignmentBaseline9Work"
    ASSIGNMENTBASELINE9COST = "AssignmentBaseline9Cost"
    TASKBASELINE9WORK = "TaskBaseline9Work"
    TASKBASELINE9COST = "TaskBaseline9Cost"
    RESOURCEBASELINE9WORK = "ResourceBaseline9Work"
    RESOURCEBASELINE9COST = "ResourceBaseline9Cost"
    ASSIGNMENTBASELINE10WORK = "AssignmentBaseline10Work"
    ASSIGNMENTBASELINE10COST = "AssignmentBaseline10Cost"
    TASKBASELINE10WORK = "TaskBaseline10Work"
    TASKBASELINE10COST = "TaskBaseline10Cost"
    RESOURCEBASELINE10WORK = "ResourceBaseline10Work"
    RESOURCEBASELINE10COST = "ResourceBaseline10Cost"
    PHYSICALPERCENTCOMPLETE = "PhysicalPercentComplete"
    TASKWORK = "TaskWork"
    TASKCOST = "TaskCost"
    RESOURCEWORK = "ResourceWork"
    RESOURCECOST = "ResourceCost"
    ASSIGNMENTWORK = "AssignmentWork"
    ASSIGNMENTCOST = "AssignmentCost"
    UNDEFINED = "Undefined"

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """TimephasedDataType - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TimephasedDataType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
