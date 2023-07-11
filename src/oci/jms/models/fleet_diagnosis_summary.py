# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210610


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FleetDiagnosisSummary(object):
    """
    Diagnosis of a resource needed by the fleet.
    """

    #: A constant which can be used with the resource_type property of a FleetDiagnosisSummary.
    #: This constant has a value of "INVENTORY_LOG"
    RESOURCE_TYPE_INVENTORY_LOG = "INVENTORY_LOG"

    #: A constant which can be used with the resource_type property of a FleetDiagnosisSummary.
    #: This constant has a value of "OPERATION_LOG"
    RESOURCE_TYPE_OPERATION_LOG = "OPERATION_LOG"

    #: A constant which can be used with the resource_type property of a FleetDiagnosisSummary.
    #: This constant has a value of "CRYPTO_SUMMARIZED_LOG"
    RESOURCE_TYPE_CRYPTO_SUMMARIZED_LOG = "CRYPTO_SUMMARIZED_LOG"

    #: A constant which can be used with the resource_type property of a FleetDiagnosisSummary.
    #: This constant has a value of "ANALYSIS_OSS_BUCKET"
    RESOURCE_TYPE_ANALYSIS_OSS_BUCKET = "ANALYSIS_OSS_BUCKET"

    #: A constant which can be used with the resource_state property of a FleetDiagnosisSummary.
    #: This constant has a value of "ACTIVE"
    RESOURCE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the resource_state property of a FleetDiagnosisSummary.
    #: This constant has a value of "INACTIVE"
    RESOURCE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the resource_state property of a FleetDiagnosisSummary.
    #: This constant has a value of "NOT_FOUND"
    RESOURCE_STATE_NOT_FOUND = "NOT_FOUND"

    #: A constant which can be used with the resource_state property of a FleetDiagnosisSummary.
    #: This constant has a value of "OTHER"
    RESOURCE_STATE_OTHER = "OTHER"

    def __init__(self, **kwargs):
        """
        Initializes a new FleetDiagnosisSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_type:
            The value to assign to the resource_type property of this FleetDiagnosisSummary.
            Allowed values for this property are: "INVENTORY_LOG", "OPERATION_LOG", "CRYPTO_SUMMARIZED_LOG", "ANALYSIS_OSS_BUCKET", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_type: str

        :param resource_id:
            The value to assign to the resource_id property of this FleetDiagnosisSummary.
        :type resource_id: str

        :param resource_state:
            The value to assign to the resource_state property of this FleetDiagnosisSummary.
            Allowed values for this property are: "ACTIVE", "INACTIVE", "NOT_FOUND", "OTHER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_state: str

        :param resource_diagnosis:
            The value to assign to the resource_diagnosis property of this FleetDiagnosisSummary.
        :type resource_diagnosis: str

        """
        self.swagger_types = {
            'resource_type': 'str',
            'resource_id': 'str',
            'resource_state': 'str',
            'resource_diagnosis': 'str'
        }

        self.attribute_map = {
            'resource_type': 'resourceType',
            'resource_id': 'resourceId',
            'resource_state': 'resourceState',
            'resource_diagnosis': 'resourceDiagnosis'
        }

        self._resource_type = None
        self._resource_id = None
        self._resource_state = None
        self._resource_diagnosis = None

    @property
    def resource_type(self):
        """
        **[Required]** Gets the resource_type of this FleetDiagnosisSummary.
        The type of the resource needed by the fleet.
        This is the role of a resource in the fleet. Use the OCID to determine the actual OCI
        resource type such as log group or log.

        Allowed values for this property are: "INVENTORY_LOG", "OPERATION_LOG", "CRYPTO_SUMMARIZED_LOG", "ANALYSIS_OSS_BUCKET", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The resource_type of this FleetDiagnosisSummary.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this FleetDiagnosisSummary.
        The type of the resource needed by the fleet.
        This is the role of a resource in the fleet. Use the OCID to determine the actual OCI
        resource type such as log group or log.


        :param resource_type: The resource_type of this FleetDiagnosisSummary.
        :type: str
        """
        allowed_values = ["INVENTORY_LOG", "OPERATION_LOG", "CRYPTO_SUMMARIZED_LOG", "ANALYSIS_OSS_BUCKET"]
        if not value_allowed_none_or_none_sentinel(resource_type, allowed_values):
            resource_type = 'UNKNOWN_ENUM_VALUE'
        self._resource_type = resource_type

    @property
    def resource_id(self):
        """
        Gets the resource_id of this FleetDiagnosisSummary.
        The OCID of the external resouce needed by the fleet.


        :return: The resource_id of this FleetDiagnosisSummary.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this FleetDiagnosisSummary.
        The OCID of the external resouce needed by the fleet.


        :param resource_id: The resource_id of this FleetDiagnosisSummary.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_state(self):
        """
        Gets the resource_state of this FleetDiagnosisSummary.
        The state of the resource. The resource state is ACTIVE when it works properly for the fleet.
        In case it would cause an issue for the fleet function, the state is INACTIVE.
        When JMS can't locate the resource, the state is NOT_FOUND.
        OTHER covers other cases, such as a temporarily network issue that prevents JMS from detecting the
        resource. Check the resourceDiagnosis for details.

        Allowed values for this property are: "ACTIVE", "INACTIVE", "NOT_FOUND", "OTHER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The resource_state of this FleetDiagnosisSummary.
        :rtype: str
        """
        return self._resource_state

    @resource_state.setter
    def resource_state(self, resource_state):
        """
        Sets the resource_state of this FleetDiagnosisSummary.
        The state of the resource. The resource state is ACTIVE when it works properly for the fleet.
        In case it would cause an issue for the fleet function, the state is INACTIVE.
        When JMS can't locate the resource, the state is NOT_FOUND.
        OTHER covers other cases, such as a temporarily network issue that prevents JMS from detecting the
        resource. Check the resourceDiagnosis for details.


        :param resource_state: The resource_state of this FleetDiagnosisSummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE", "NOT_FOUND", "OTHER"]
        if not value_allowed_none_or_none_sentinel(resource_state, allowed_values):
            resource_state = 'UNKNOWN_ENUM_VALUE'
        self._resource_state = resource_state

    @property
    def resource_diagnosis(self):
        """
        Gets the resource_diagnosis of this FleetDiagnosisSummary.
        The diagnosis message.


        :return: The resource_diagnosis of this FleetDiagnosisSummary.
        :rtype: str
        """
        return self._resource_diagnosis

    @resource_diagnosis.setter
    def resource_diagnosis(self, resource_diagnosis):
        """
        Sets the resource_diagnosis of this FleetDiagnosisSummary.
        The diagnosis message.


        :param resource_diagnosis: The resource_diagnosis of this FleetDiagnosisSummary.
        :type: str
        """
        self._resource_diagnosis = resource_diagnosis

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
