# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="ProjectServerSaveOptionsDTO.py">
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


class ProjectServerSaveOptionsDTO(object):
    """Allows to specify additional options when project is saved to Project Server or Project Online.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'project_name': 'str',
        'project_guid': 'str',
        'timeout': 'str',
        'polling_interval': 'str'
    }

    attribute_map = {
        'project_name': 'projectName',
        'project_guid': 'projectGuid',
        'timeout': 'timeout',
        'polling_interval': 'pollingInterval'
    }

    def __init__(self, project_name=None, project_guid=None, timeout=None, polling_interval=None):  # noqa: E501
        """ProjectServerSaveOptionsDTO - a model defined in Swagger"""  # noqa: E501

        self._project_name = None
        self._project_guid = None
        self._timeout = None
        self._polling_interval = None
        self.discriminator = None

        if project_name is not None:
            self.project_name = project_name
        if project_guid is not None:
            self.project_guid = project_guid
        if timeout is not None:
            self.timeout = timeout
        if polling_interval is not None:
            self.polling_interval = polling_interval

    @property
    def project_name(self):
        """Gets the project_name of this ProjectServerSaveOptionsDTO.  # noqa: E501

        Gets or sets name of a project which is displayed in Project Server \\ Project     Online projects list. Should be unique within Project Server \\ Project Online     instance. Is the value is omitted, the value of Prj.Name property will be used     instead.  # noqa: E501

        :return: The project_name of this ProjectServerSaveOptionsDTO.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ProjectServerSaveOptionsDTO.

        Gets or sets name of a project which is displayed in Project Server \\ Project     Online projects list. Should be unique within Project Server \\ Project Online     instance. Is the value is omitted, the value of Prj.Name property will be used     instead.  # noqa: E501

        :param project_name: The project_name of this ProjectServerSaveOptionsDTO.  # noqa: E501
        :type: str
        """
        self._project_name = project_name
    @property
    def project_guid(self):
        """Gets the project_guid of this ProjectServerSaveOptionsDTO.  # noqa: E501

        Gets or sets unique identifier of a project. Should be unique within Project     Server \\ Project Online instance.  # noqa: E501

        :return: The project_guid of this ProjectServerSaveOptionsDTO.  # noqa: E501
        :rtype: str
        """
        return self._project_guid

    @project_guid.setter
    def project_guid(self, project_guid):
        """Sets the project_guid of this ProjectServerSaveOptionsDTO.

        Gets or sets unique identifier of a project. Should be unique within Project     Server \\ Project Online instance.  # noqa: E501

        :param project_guid: The project_guid of this ProjectServerSaveOptionsDTO.  # noqa: E501
        :type: str
        """
        self._project_guid = project_guid
    @property
    def timeout(self):
        """Gets the timeout of this ProjectServerSaveOptionsDTO.  # noqa: E501

        Gets or sets timeout used when waiting for processing of save project request     by a Project Server's queue processing service. The default value for this property     is 1 minute. The processing time may be longer for large projects or in case when Project     Server instance is too busy responding to other requests.  # noqa: E501

        :return: The timeout of this ProjectServerSaveOptionsDTO.  # noqa: E501
        :rtype: str
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this ProjectServerSaveOptionsDTO.

        Gets or sets timeout used when waiting for processing of save project request     by a Project Server's queue processing service. The default value for this property     is 1 minute. The processing time may be longer for large projects or in case when Project     Server instance is too busy responding to other requests.  # noqa: E501

        :param timeout: The timeout of this ProjectServerSaveOptionsDTO.  # noqa: E501
        :type: str
        """
        if timeout is None:
            raise ValueError("Invalid value for `timeout`, must not be `None`")  # noqa: E501
        self._timeout = timeout
    @property
    def polling_interval(self):
        """Gets the polling_interval of this ProjectServerSaveOptionsDTO.  # noqa: E501

        Gets or sets interval between queue job status requests. The default value is     2 seconds.  # noqa: E501

        :return: The polling_interval of this ProjectServerSaveOptionsDTO.  # noqa: E501
        :rtype: str
        """
        return self._polling_interval

    @polling_interval.setter
    def polling_interval(self, polling_interval):
        """Sets the polling_interval of this ProjectServerSaveOptionsDTO.

        Gets or sets interval between queue job status requests. The default value is     2 seconds.  # noqa: E501

        :param polling_interval: The polling_interval of this ProjectServerSaveOptionsDTO.  # noqa: E501
        :type: str
        """
        if polling_interval is None:
            raise ValueError("Invalid value for `polling_interval`, must not be `None`")  # noqa: E501
        self._polling_interval = polling_interval
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
        if not isinstance(other, ProjectServerSaveOptionsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
