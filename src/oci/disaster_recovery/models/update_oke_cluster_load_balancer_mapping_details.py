# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateOkeClusterLoadBalancerMappingDetails(object):
    """
    Update source-to-destination mapping for a load balancer.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateOkeClusterLoadBalancerMappingDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_load_balancer_id:
            The value to assign to the source_load_balancer_id property of this UpdateOkeClusterLoadBalancerMappingDetails.
        :type source_load_balancer_id: str

        :param destination_load_balancer_id:
            The value to assign to the destination_load_balancer_id property of this UpdateOkeClusterLoadBalancerMappingDetails.
        :type destination_load_balancer_id: str

        """
        self.swagger_types = {
            'source_load_balancer_id': 'str',
            'destination_load_balancer_id': 'str'
        }
        self.attribute_map = {
            'source_load_balancer_id': 'sourceLoadBalancerId',
            'destination_load_balancer_id': 'destinationLoadBalancerId'
        }
        self._source_load_balancer_id = None
        self._destination_load_balancer_id = None

    @property
    def source_load_balancer_id(self):
        """
        **[Required]** Gets the source_load_balancer_id of this UpdateOkeClusterLoadBalancerMappingDetails.
        The OCID of the source Load Balancer .

         Example: `ocid1.loadbalancer.oc1..uniqueID`


        :return: The source_load_balancer_id of this UpdateOkeClusterLoadBalancerMappingDetails.
        :rtype: str
        """
        return self._source_load_balancer_id

    @source_load_balancer_id.setter
    def source_load_balancer_id(self, source_load_balancer_id):
        """
        Sets the source_load_balancer_id of this UpdateOkeClusterLoadBalancerMappingDetails.
        The OCID of the source Load Balancer .

         Example: `ocid1.loadbalancer.oc1..uniqueID`


        :param source_load_balancer_id: The source_load_balancer_id of this UpdateOkeClusterLoadBalancerMappingDetails.
        :type: str
        """
        self._source_load_balancer_id = source_load_balancer_id

    @property
    def destination_load_balancer_id(self):
        """
        **[Required]** Gets the destination_load_balancer_id of this UpdateOkeClusterLoadBalancerMappingDetails.
        The OCID of the destination Load Balancer.

        Example: `ocid1.loadbalancer.oc1..uniqueID`


        :return: The destination_load_balancer_id of this UpdateOkeClusterLoadBalancerMappingDetails.
        :rtype: str
        """
        return self._destination_load_balancer_id

    @destination_load_balancer_id.setter
    def destination_load_balancer_id(self, destination_load_balancer_id):
        """
        Sets the destination_load_balancer_id of this UpdateOkeClusterLoadBalancerMappingDetails.
        The OCID of the destination Load Balancer.

        Example: `ocid1.loadbalancer.oc1..uniqueID`


        :param destination_load_balancer_id: The destination_load_balancer_id of this UpdateOkeClusterLoadBalancerMappingDetails.
        :type: str
        """
        self._destination_load_balancer_id = destination_load_balancer_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
