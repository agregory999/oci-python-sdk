# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GiFleetDiscoveryDetails(object):
    """
    Supported fleet discovery strategies for GI Collections.
    If specified on an Update Collection request, this will re-discover the targets of the Collection.
    """

    #: A constant which can be used with the strategy property of a GiFleetDiscoveryDetails.
    #: This constant has a value of "SEARCH_QUERY"
    STRATEGY_SEARCH_QUERY = "SEARCH_QUERY"

    #: A constant which can be used with the strategy property of a GiFleetDiscoveryDetails.
    #: This constant has a value of "FILTERS"
    STRATEGY_FILTERS = "FILTERS"

    #: A constant which can be used with the strategy property of a GiFleetDiscoveryDetails.
    #: This constant has a value of "TARGET_LIST"
    STRATEGY_TARGET_LIST = "TARGET_LIST"

    #: A constant which can be used with the strategy property of a GiFleetDiscoveryDetails.
    #: This constant has a value of "DISCOVERY_RESULTS"
    STRATEGY_DISCOVERY_RESULTS = "DISCOVERY_RESULTS"

    def __init__(self, **kwargs):
        """
        Initializes a new GiFleetDiscoveryDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.fleet_software_update.models.GiFiltersDiscovery`
        * :class:`~oci.fleet_software_update.models.GiSearchQueryDiscovery`
        * :class:`~oci.fleet_software_update.models.GiDiscoveryResults`
        * :class:`~oci.fleet_software_update.models.GiTargetListDiscovery`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param strategy:
            The value to assign to the strategy property of this GiFleetDiscoveryDetails.
            Allowed values for this property are: "SEARCH_QUERY", "FILTERS", "TARGET_LIST", "DISCOVERY_RESULTS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type strategy: str

        """
        self.swagger_types = {
            'strategy': 'str'
        }
        self.attribute_map = {
            'strategy': 'strategy'
        }
        self._strategy = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['strategy']

        if type == 'FILTERS':
            return 'GiFiltersDiscovery'

        if type == 'SEARCH_QUERY':
            return 'GiSearchQueryDiscovery'

        if type == 'DISCOVERY_RESULTS':
            return 'GiDiscoveryResults'

        if type == 'TARGET_LIST':
            return 'GiTargetListDiscovery'
        else:
            return 'GiFleetDiscoveryDetails'

    @property
    def strategy(self):
        """
        **[Required]** Gets the strategy of this GiFleetDiscoveryDetails.
        Possible fleet discovery strategies.

        Allowed values for this property are: "SEARCH_QUERY", "FILTERS", "TARGET_LIST", "DISCOVERY_RESULTS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The strategy of this GiFleetDiscoveryDetails.
        :rtype: str
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        """
        Sets the strategy of this GiFleetDiscoveryDetails.
        Possible fleet discovery strategies.


        :param strategy: The strategy of this GiFleetDiscoveryDetails.
        :type: str
        """
        allowed_values = ["SEARCH_QUERY", "FILTERS", "TARGET_LIST", "DISCOVERY_RESULTS"]
        if not value_allowed_none_or_none_sentinel(strategy, allowed_values):
            strategy = 'UNKNOWN_ENUM_VALUE'
        self._strategy = strategy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
