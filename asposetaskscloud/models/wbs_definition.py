# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="WBSDefinition.py">
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


class WBSDefinition(object):
    """
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code_prefix': 'str',
        'generate_wbs_code': 'bool',
        'verify_uniqueness': 'bool',
        'code_mask_collection': 'list[WBSCodeMask]'
    }

    attribute_map = {
        'code_prefix': 'codePrefix',
        'generate_wbs_code': 'generateWBSCode',
        'verify_uniqueness': 'verifyUniqueness',
        'code_mask_collection': 'codeMaskCollection'
    }

    def __init__(self, code_prefix=None, generate_wbs_code=None, verify_uniqueness=None, code_mask_collection=None):  # noqa: E501
        """WBSDefinition - a model defined in Swagger"""  # noqa: E501

        self._code_prefix = None
        self._generate_wbs_code = None
        self._verify_uniqueness = None
        self._code_mask_collection = None
        self.discriminator = None

        if code_prefix is not None:
            self.code_prefix = code_prefix
        if generate_wbs_code is not None:
            self.generate_wbs_code = generate_wbs_code
        if verify_uniqueness is not None:
            self.verify_uniqueness = verify_uniqueness
        if code_mask_collection is not None:
            self.code_mask_collection = code_mask_collection

    @property
    def code_prefix(self):
        """Gets the code_prefix of this WBSDefinition.  # noqa: E501

        Project Code Prefix.  # noqa: E501

        :return: The code_prefix of this WBSDefinition.  # noqa: E501
        :rtype: str
        """
        return self._code_prefix

    @code_prefix.setter
    def code_prefix(self, code_prefix):
        """Sets the code_prefix of this WBSDefinition.

        Project Code Prefix.  # noqa: E501

        :param code_prefix: The code_prefix of this WBSDefinition.  # noqa: E501
        :type: str
        """
        self._code_prefix = code_prefix
    @property
    def generate_wbs_code(self):
        """Gets the generate_wbs_code of this WBSDefinition.  # noqa: E501

        Determines whether to generate WBS code for new task.  # noqa: E501

        :return: The generate_wbs_code of this WBSDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._generate_wbs_code

    @generate_wbs_code.setter
    def generate_wbs_code(self, generate_wbs_code):
        """Sets the generate_wbs_code of this WBSDefinition.

        Determines whether to generate WBS code for new task.  # noqa: E501

        :param generate_wbs_code: The generate_wbs_code of this WBSDefinition.  # noqa: E501
        :type: bool
        """
        if generate_wbs_code is None:
            raise ValueError("Invalid value for `generate_wbs_code`, must not be `None`")  # noqa: E501
        self._generate_wbs_code = generate_wbs_code
    @property
    def verify_uniqueness(self):
        """Gets the verify_uniqueness of this WBSDefinition.  # noqa: E501

        Determines whether to verify uniqueness of new WBS codes.  # noqa: E501

        :return: The verify_uniqueness of this WBSDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._verify_uniqueness

    @verify_uniqueness.setter
    def verify_uniqueness(self, verify_uniqueness):
        """Sets the verify_uniqueness of this WBSDefinition.

        Determines whether to verify uniqueness of new WBS codes.  # noqa: E501

        :param verify_uniqueness: The verify_uniqueness of this WBSDefinition.  # noqa: E501
        :type: bool
        """
        if verify_uniqueness is None:
            raise ValueError("Invalid value for `verify_uniqueness`, must not be `None`")  # noqa: E501
        self._verify_uniqueness = verify_uniqueness
    @property
    def code_mask_collection(self):
        """Gets the code_mask_collection of this WBSDefinition.  # noqa: E501

        Collection of WBSCodeMask objects.  # noqa: E501

        :return: The code_mask_collection of this WBSDefinition.  # noqa: E501
        :rtype: list[WBSCodeMask]
        """
        return self._code_mask_collection

    @code_mask_collection.setter
    def code_mask_collection(self, code_mask_collection):
        """Sets the code_mask_collection of this WBSDefinition.

        Collection of WBSCodeMask objects.  # noqa: E501

        :param code_mask_collection: The code_mask_collection of this WBSDefinition.  # noqa: E501
        :type: list[WBSCodeMask]
        """
        self._code_mask_collection = code_mask_collection
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
        if not isinstance(other, WBSDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
