# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230301

from .prevalidate_payload import PrevalidatePayload
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrevalidateCreatePayload(PrevalidatePayload):
    """
    Payload to prevalidate create sharded database operation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PrevalidateCreatePayload object with values from keyword arguments. The default value of the :py:attr:`~oci.globally_distributed_database.models.PrevalidateCreatePayload.operation` attribute
        of this class is ``CREATE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation:
            The value to assign to the operation property of this PrevalidateCreatePayload.
            Allowed values for this property are: "CREATE", "PATCH"
        :type operation: str

        :param prevalidate_payload:
            The value to assign to the prevalidate_payload property of this PrevalidateCreatePayload.
        :type prevalidate_payload: oci.globally_distributed_database.models.CreateShardedDatabaseDetails

        """
        self.swagger_types = {
            'operation': 'str',
            'prevalidate_payload': 'CreateShardedDatabaseDetails'
        }
        self.attribute_map = {
            'operation': 'operation',
            'prevalidate_payload': 'prevalidatePayload'
        }
        self._operation = None
        self._prevalidate_payload = None
        self._operation = 'CREATE'

    @property
    def prevalidate_payload(self):
        """
        **[Required]** Gets the prevalidate_payload of this PrevalidateCreatePayload.

        :return: The prevalidate_payload of this PrevalidateCreatePayload.
        :rtype: oci.globally_distributed_database.models.CreateShardedDatabaseDetails
        """
        return self._prevalidate_payload

    @prevalidate_payload.setter
    def prevalidate_payload(self, prevalidate_payload):
        """
        Sets the prevalidate_payload of this PrevalidateCreatePayload.

        :param prevalidate_payload: The prevalidate_payload of this PrevalidateCreatePayload.
        :type: oci.globally_distributed_database.models.CreateShardedDatabaseDetails
        """
        self._prevalidate_payload = prevalidate_payload

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
