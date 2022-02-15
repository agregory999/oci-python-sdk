# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_column_source_details import CreateColumnSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateColumnSourceFromSdmDetails(CreateColumnSourceDetails):
    """
    Details of the sensitive data model to be associated as the column source with a masking policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateColumnSourceFromSdmDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.CreateColumnSourceFromSdmDetails.column_source` attribute
        of this class is ``SENSITIVE_DATA_MODEL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param column_source:
            The value to assign to the column_source property of this CreateColumnSourceFromSdmDetails.
            Allowed values for this property are: "TARGET", "SENSITIVE_DATA_MODEL"
        :type column_source: str

        :param sensitive_data_model_id:
            The value to assign to the sensitive_data_model_id property of this CreateColumnSourceFromSdmDetails.
        :type sensitive_data_model_id: str

        """
        self.swagger_types = {
            'column_source': 'str',
            'sensitive_data_model_id': 'str'
        }

        self.attribute_map = {
            'column_source': 'columnSource',
            'sensitive_data_model_id': 'sensitiveDataModelId'
        }

        self._column_source = None
        self._sensitive_data_model_id = None
        self._column_source = 'SENSITIVE_DATA_MODEL'

    @property
    def sensitive_data_model_id(self):
        """
        **[Required]** Gets the sensitive_data_model_id of this CreateColumnSourceFromSdmDetails.
        The OCID of the sensitive data model to be associated as the column source with the masking policy.


        :return: The sensitive_data_model_id of this CreateColumnSourceFromSdmDetails.
        :rtype: str
        """
        return self._sensitive_data_model_id

    @sensitive_data_model_id.setter
    def sensitive_data_model_id(self, sensitive_data_model_id):
        """
        Sets the sensitive_data_model_id of this CreateColumnSourceFromSdmDetails.
        The OCID of the sensitive data model to be associated as the column source with the masking policy.


        :param sensitive_data_model_id: The sensitive_data_model_id of this CreateColumnSourceFromSdmDetails.
        :type: str
        """
        self._sensitive_data_model_id = sensitive_data_model_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
