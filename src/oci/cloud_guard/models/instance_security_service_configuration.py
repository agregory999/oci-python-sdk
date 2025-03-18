# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200131

from .service_configuration import ServiceConfiguration
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceSecurityServiceConfiguration(ServiceConfiguration):
    """
    Instance Security service configuration.
    """

    #: A constant which can be used with the status property of a InstanceSecurityServiceConfiguration.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a InstanceSecurityServiceConfiguration.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceSecurityServiceConfiguration object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_guard.models.InstanceSecurityServiceConfiguration.service_configuration_type` attribute
        of this class is ``INSTANCE_SECURITY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param service_configuration_type:
            The value to assign to the service_configuration_type property of this InstanceSecurityServiceConfiguration.
            Allowed values for this property are: "INSTANCE_SECURITY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type service_configuration_type: str

        :param status:
            The value to assign to the status property of this InstanceSecurityServiceConfiguration.
            Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        """
        self.swagger_types = {
            'service_configuration_type': 'str',
            'status': 'str'
        }
        self.attribute_map = {
            'service_configuration_type': 'serviceConfigurationType',
            'status': 'status'
        }
        self._service_configuration_type = None
        self._status = None
        self._service_configuration_type = 'INSTANCE_SECURITY'

    @property
    def status(self):
        """
        Gets the status of this InstanceSecurityServiceConfiguration.
        Partner service status

        Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this InstanceSecurityServiceConfiguration.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this InstanceSecurityServiceConfiguration.
        Partner service status


        :param status: The status of this InstanceSecurityServiceConfiguration.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
