# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AssociatedFleetResourceDetails(object):
    """
    The information about associated FleetResource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AssociatedFleetResourceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_id:
            The value to assign to the resource_id property of this AssociatedFleetResourceDetails.
        :type resource_id: str

        :param fleet_resource_type:
            The value to assign to the fleet_resource_type property of this AssociatedFleetResourceDetails.
        :type fleet_resource_type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AssociatedFleetResourceDetails.
        :type compartment_id: str

        :param tenancy_id:
            The value to assign to the tenancy_id property of this AssociatedFleetResourceDetails.
        :type tenancy_id: str

        """
        self.swagger_types = {
            'resource_id': 'str',
            'fleet_resource_type': 'str',
            'compartment_id': 'str',
            'tenancy_id': 'str'
        }
        self.attribute_map = {
            'resource_id': 'resourceId',
            'fleet_resource_type': 'fleetResourceType',
            'compartment_id': 'compartmentId',
            'tenancy_id': 'tenancyId'
        }
        self._resource_id = None
        self._fleet_resource_type = None
        self._compartment_id = None
        self._tenancy_id = None

    @property
    def resource_id(self):
        """
        **[Required]** Gets the resource_id of this AssociatedFleetResourceDetails.
        OCID of the resource.


        :return: The resource_id of this AssociatedFleetResourceDetails.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this AssociatedFleetResourceDetails.
        OCID of the resource.


        :param resource_id: The resource_id of this AssociatedFleetResourceDetails.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def fleet_resource_type(self):
        """
        Gets the fleet_resource_type of this AssociatedFleetResourceDetails.
        Type of the FleetResource.


        :return: The fleet_resource_type of this AssociatedFleetResourceDetails.
        :rtype: str
        """
        return self._fleet_resource_type

    @fleet_resource_type.setter
    def fleet_resource_type(self, fleet_resource_type):
        """
        Sets the fleet_resource_type of this AssociatedFleetResourceDetails.
        Type of the FleetResource.


        :param fleet_resource_type: The fleet_resource_type of this AssociatedFleetResourceDetails.
        :type: str
        """
        self._fleet_resource_type = fleet_resource_type

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AssociatedFleetResourceDetails.
        Compartment Identifier[OCID].


        :return: The compartment_id of this AssociatedFleetResourceDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AssociatedFleetResourceDetails.
        Compartment Identifier[OCID].


        :param compartment_id: The compartment_id of this AssociatedFleetResourceDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def tenancy_id(self):
        """
        **[Required]** Gets the tenancy_id of this AssociatedFleetResourceDetails.
        Tenancy Identifier[OCID].


        :return: The tenancy_id of this AssociatedFleetResourceDetails.
        :rtype: str
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        """
        Sets the tenancy_id of this AssociatedFleetResourceDetails.
        Tenancy Identifier[OCID].


        :param tenancy_id: The tenancy_id of this AssociatedFleetResourceDetails.
        :type: str
        """
        self._tenancy_id = tenancy_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
