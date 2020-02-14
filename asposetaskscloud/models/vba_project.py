# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="VbaProject.py">
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


class VbaProject(object):
    """Represents VbaProject
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'compilation_arguments': 'str',
        'description': 'str',
        'help_context_id': 'int',
        'help_file': 'str',
        'modules': 'list[VbaModule]',
        'name': 'str',
        'references': 'list[VbaReference]'
    }

    attribute_map = {
        'compilation_arguments': 'compilationArguments',
        'description': 'description',
        'help_context_id': 'helpContextId',
        'help_file': 'helpFile',
        'modules': 'modules',
        'name': 'name',
        'references': 'references'
    }

    def __init__(self, compilation_arguments=None, description=None, help_context_id=None, help_file=None, modules=None, name=None, references=None):  # noqa: E501
        """VbaProject - a model defined in Swagger"""  # noqa: E501

        self._compilation_arguments = None
        self._description = None
        self._help_context_id = None
        self._help_file = None
        self._modules = None
        self._name = None
        self._references = None
        self.discriminator = None

        if compilation_arguments is not None:
            self.compilation_arguments = compilation_arguments
        if description is not None:
            self.description = description
        if help_context_id is not None:
            self.help_context_id = help_context_id
        if help_file is not None:
            self.help_file = help_file
        if modules is not None:
            self.modules = modules
        if name is not None:
            self.name = name
        if references is not None:
            self.references = references

    @property
    def compilation_arguments(self):
        """Gets the compilation_arguments of this VbaProject.  # noqa: E501

        Gets conditional Compilation Arguments  # noqa: E501

        :return: The compilation_arguments of this VbaProject.  # noqa: E501
        :rtype: str
        """
        return self._compilation_arguments

    @compilation_arguments.setter
    def compilation_arguments(self, compilation_arguments):
        """Sets the compilation_arguments of this VbaProject.

        Gets conditional Compilation Arguments  # noqa: E501

        :param compilation_arguments: The compilation_arguments of this VbaProject.  # noqa: E501
        :type: str
        """
        self._compilation_arguments = compilation_arguments
    @property
    def description(self):
        """Gets the description of this VbaProject.  # noqa: E501

        Gets a project Description  # noqa: E501

        :return: The description of this VbaProject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VbaProject.

        Gets a project Description  # noqa: E501

        :param description: The description of this VbaProject.  # noqa: E501
        :type: str
        """
        self._description = description
    @property
    def help_context_id(self):
        """Gets the help_context_id of this VbaProject.  # noqa: E501

        Gets a project Help Context Id  # noqa: E501

        :return: The help_context_id of this VbaProject.  # noqa: E501
        :rtype: int
        """
        return self._help_context_id

    @help_context_id.setter
    def help_context_id(self, help_context_id):
        """Sets the help_context_id of this VbaProject.

        Gets a project Help Context Id  # noqa: E501

        :param help_context_id: The help_context_id of this VbaProject.  # noqa: E501
        :type: int
        """
        if help_context_id is None:
            raise ValueError("Invalid value for `help_context_id`, must not be `None`")  # noqa: E501
        self._help_context_id = help_context_id
    @property
    def help_file(self):
        """Gets the help_file of this VbaProject.  # noqa: E501

        Gets a help file name  # noqa: E501

        :return: The help_file of this VbaProject.  # noqa: E501
        :rtype: str
        """
        return self._help_file

    @help_file.setter
    def help_file(self, help_file):
        """Sets the help_file of this VbaProject.

        Gets a help file name  # noqa: E501

        :param help_file: The help_file of this VbaProject.  # noqa: E501
        :type: str
        """
        self._help_file = help_file
    @property
    def modules(self):
        """Gets the modules of this VbaProject.  # noqa: E501

        Gets a collection of VbaModuleCollection  # noqa: E501

        :return: The modules of this VbaProject.  # noqa: E501
        :rtype: list[VbaModule]
        """
        return self._modules

    @modules.setter
    def modules(self, modules):
        """Sets the modules of this VbaProject.

        Gets a collection of VbaModuleCollection  # noqa: E501

        :param modules: The modules of this VbaProject.  # noqa: E501
        :type: list[VbaModule]
        """
        self._modules = modules
    @property
    def name(self):
        """Gets the name of this VbaProject.  # noqa: E501

        Gets project name  # noqa: E501

        :return: The name of this VbaProject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VbaProject.

        Gets project name  # noqa: E501

        :param name: The name of this VbaProject.  # noqa: E501
        :type: str
        """
        self._name = name
    @property
    def references(self):
        """Gets the references of this VbaProject.  # noqa: E501

        Gets a collection of VbaReferenceCollection  # noqa: E501

        :return: The references of this VbaProject.  # noqa: E501
        :rtype: list[VbaReference]
        """
        return self._references

    @references.setter
    def references(self, references):
        """Sets the references of this VbaProject.

        Gets a collection of VbaReferenceCollection  # noqa: E501

        :param references: The references of this VbaProject.  # noqa: E501
        :type: list[VbaReference]
        """
        self._references = references
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
        if not isinstance(other, VbaProject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
