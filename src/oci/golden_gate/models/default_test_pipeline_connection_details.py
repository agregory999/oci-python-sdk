# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407

from .test_pipeline_connection_details import TestPipelineConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DefaultTestPipelineConnectionDetails(TestPipelineConnectionDetails):
    """
    Additional attribute with which to test the pipeline's connection. The connectionId must be one of the pipeline's assigned connections.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DefaultTestPipelineConnectionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.DefaultTestPipelineConnectionDetails.type` attribute
        of this class is ``DEFAULT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this DefaultTestPipelineConnectionDetails.
            Allowed values for this property are: "DEFAULT"
        :type type: str

        :param connection_id:
            The value to assign to the connection_id property of this DefaultTestPipelineConnectionDetails.
        :type connection_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'connection_id': 'str'
        }
        self.attribute_map = {
            'type': 'type',
            'connection_id': 'connectionId'
        }
        self._type = None
        self._connection_id = None
        self._type = 'DEFAULT'

    @property
    def connection_id(self):
        """
        **[Required]** Gets the connection_id of this DefaultTestPipelineConnectionDetails.
        The `OCID`__ of the connection being
        referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The connection_id of this DefaultTestPipelineConnectionDetails.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """
        Sets the connection_id of this DefaultTestPipelineConnectionDetails.
        The `OCID`__ of the connection being
        referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param connection_id: The connection_id of this DefaultTestPipelineConnectionDetails.
        :type: str
        """
        self._connection_id = connection_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
