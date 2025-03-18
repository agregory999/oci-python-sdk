# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528

from .gi_fleet_discovery_filter import GiFleetDiscoveryFilter
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GiCompartmentIdFilter(GiFleetDiscoveryFilter):
    """
    List of Compartments to include in the discovery.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GiCompartmentIdFilter object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_software_update.models.GiCompartmentIdFilter.type` attribute
        of this class is ``COMPARTMENT_ID`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this GiCompartmentIdFilter.
            Allowed values for this property are: "COMPARTMENT_ID", "VERSION", "FREEFORM_TAG", "DEFINED_TAG", "RESOURCE_ID"
        :type type: str

        :param mode:
            The value to assign to the mode property of this GiCompartmentIdFilter.
            Allowed values for this property are: "INCLUDE", "EXCLUDE"
        :type mode: str

        :param identifiers:
            The value to assign to the identifiers property of this GiCompartmentIdFilter.
        :type identifiers: list[str]

        """
        self.swagger_types = {
            'type': 'str',
            'mode': 'str',
            'identifiers': 'list[str]'
        }
        self.attribute_map = {
            'type': 'type',
            'mode': 'mode',
            'identifiers': 'identifiers'
        }
        self._type = None
        self._mode = None
        self._identifiers = None
        self._type = 'COMPARTMENT_ID'

    @property
    def identifiers(self):
        """
        **[Required]** Gets the identifiers of this GiCompartmentIdFilter.
        List of Compartments OCIDs to include in the discovery.


        :return: The identifiers of this GiCompartmentIdFilter.
        :rtype: list[str]
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """
        Sets the identifiers of this GiCompartmentIdFilter.
        List of Compartments OCIDs to include in the discovery.


        :param identifiers: The identifiers of this GiCompartmentIdFilter.
        :type: list[str]
        """
        self._identifiers = identifiers

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
