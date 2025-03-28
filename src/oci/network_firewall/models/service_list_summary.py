# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ServiceListSummary(object):
    """
    Summary object for service list in the network firewall policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ServiceListSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ServiceListSummary.
        :type name: str

        :param total_services:
            The value to assign to the total_services property of this ServiceListSummary.
        :type total_services: int

        :param parent_resource_id:
            The value to assign to the parent_resource_id property of this ServiceListSummary.
        :type parent_resource_id: str

        """
        self.swagger_types = {
            'name': 'str',
            'total_services': 'int',
            'parent_resource_id': 'str'
        }
        self.attribute_map = {
            'name': 'name',
            'total_services': 'totalServices',
            'parent_resource_id': 'parentResourceId'
        }
        self._name = None
        self._total_services = None
        self._parent_resource_id = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ServiceListSummary.
        Name of the service groups.


        :return: The name of this ServiceListSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ServiceListSummary.
        Name of the service groups.


        :param name: The name of this ServiceListSummary.
        :type: str
        """
        self._name = name

    @property
    def total_services(self):
        """
        **[Required]** Gets the total_services of this ServiceListSummary.
        Count of total services in the given service List.


        :return: The total_services of this ServiceListSummary.
        :rtype: int
        """
        return self._total_services

    @total_services.setter
    def total_services(self, total_services):
        """
        Sets the total_services of this ServiceListSummary.
        Count of total services in the given service List.


        :param total_services: The total_services of this ServiceListSummary.
        :type: int
        """
        self._total_services = total_services

    @property
    def parent_resource_id(self):
        """
        **[Required]** Gets the parent_resource_id of this ServiceListSummary.
        OCID of the Network Firewall Policy this application belongs to.


        :return: The parent_resource_id of this ServiceListSummary.
        :rtype: str
        """
        return self._parent_resource_id

    @parent_resource_id.setter
    def parent_resource_id(self, parent_resource_id):
        """
        Sets the parent_resource_id of this ServiceListSummary.
        OCID of the Network Firewall Policy this application belongs to.


        :param parent_resource_id: The parent_resource_id of this ServiceListSummary.
        :type: str
        """
        self._parent_resource_id = parent_resource_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
