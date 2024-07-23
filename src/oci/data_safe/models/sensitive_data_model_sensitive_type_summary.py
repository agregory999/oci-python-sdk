# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SensitiveDataModelSensitiveTypeSummary(object):
    """
    Summary of sensitive types present in a sensitive data model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SensitiveDataModelSensitiveTypeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sensitive_type_id:
            The value to assign to the sensitive_type_id property of this SensitiveDataModelSensitiveTypeSummary.
        :type sensitive_type_id: str

        :param count:
            The value to assign to the count property of this SensitiveDataModelSensitiveTypeSummary.
        :type count: int

        """
        self.swagger_types = {
            'sensitive_type_id': 'str',
            'count': 'int'
        }

        self.attribute_map = {
            'sensitive_type_id': 'sensitiveTypeId',
            'count': 'count'
        }

        self._sensitive_type_id = None
        self._count = None

    @property
    def sensitive_type_id(self):
        """
        **[Required]** Gets the sensitive_type_id of this SensitiveDataModelSensitiveTypeSummary.
        The OCID of the sensitive type.


        :return: The sensitive_type_id of this SensitiveDataModelSensitiveTypeSummary.
        :rtype: str
        """
        return self._sensitive_type_id

    @sensitive_type_id.setter
    def sensitive_type_id(self, sensitive_type_id):
        """
        Sets the sensitive_type_id of this SensitiveDataModelSensitiveTypeSummary.
        The OCID of the sensitive type.


        :param sensitive_type_id: The sensitive_type_id of this SensitiveDataModelSensitiveTypeSummary.
        :type: str
        """
        self._sensitive_type_id = sensitive_type_id

    @property
    def count(self):
        """
        **[Required]** Gets the count of this SensitiveDataModelSensitiveTypeSummary.
        The total number of sensitive columns linked to this specific sensitive type .


        :return: The count of this SensitiveDataModelSensitiveTypeSummary.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this SensitiveDataModelSensitiveTypeSummary.
        The total number of sensitive columns linked to this specific sensitive type .


        :param count: The count of this SensitiveDataModelSensitiveTypeSummary.
        :type: int
        """
        self._count = count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other