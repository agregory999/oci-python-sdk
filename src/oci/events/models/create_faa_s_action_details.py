# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201

from .action_details import ActionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateFaaSActionDetails(ActionDetails):
    """
    Create an action that delivers to an Oracle Functions Service endpoint.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateFaaSActionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.events.models.CreateFaaSActionDetails.action_type` attribute
        of this class is ``FAAS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action_type:
            The value to assign to the action_type property of this CreateFaaSActionDetails.
            Allowed values for this property are: "ONS", "OSS", "FAAS"
        :type action_type: str

        :param is_enabled:
            The value to assign to the is_enabled property of this CreateFaaSActionDetails.
        :type is_enabled: bool

        :param description:
            The value to assign to the description property of this CreateFaaSActionDetails.
        :type description: str

        :param function_id:
            The value to assign to the function_id property of this CreateFaaSActionDetails.
        :type function_id: str

        """
        self.swagger_types = {
            'action_type': 'str',
            'is_enabled': 'bool',
            'description': 'str',
            'function_id': 'str'
        }
        self.attribute_map = {
            'action_type': 'actionType',
            'is_enabled': 'isEnabled',
            'description': 'description',
            'function_id': 'functionId'
        }
        self._action_type = None
        self._is_enabled = None
        self._description = None
        self._function_id = None
        self._action_type = 'FAAS'

    @property
    def function_id(self):
        """
        Gets the function_id of this CreateFaaSActionDetails.
        The `OCID`__ of a Function hosted by Oracle Functions Service.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The function_id of this CreateFaaSActionDetails.
        :rtype: str
        """
        return self._function_id

    @function_id.setter
    def function_id(self, function_id):
        """
        Sets the function_id of this CreateFaaSActionDetails.
        The `OCID`__ of a Function hosted by Oracle Functions Service.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param function_id: The function_id of this CreateFaaSActionDetails.
        :type: str
        """
        self._function_id = function_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
