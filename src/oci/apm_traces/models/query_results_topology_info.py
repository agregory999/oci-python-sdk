# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class QueryResultsTopologyInfo(object):
    """
    The structure that provides the metadata of a topology query.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new QueryResultsTopologyInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param nodes:
            The value to assign to the nodes property of this QueryResultsTopologyInfo.
        :type nodes: list[oci.apm_traces.models.QueryResultsTopologyNodeInfo]

        """
        self.swagger_types = {
            'nodes': 'list[QueryResultsTopologyNodeInfo]'
        }
        self.attribute_map = {
            'nodes': 'nodes'
        }
        self._nodes = None

    @property
    def nodes(self):
        """
        Gets the nodes of this QueryResultsTopologyInfo.
        The information about the attributes of the topology nodes.


        :return: The nodes of this QueryResultsTopologyInfo.
        :rtype: list[oci.apm_traces.models.QueryResultsTopologyNodeInfo]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """
        Sets the nodes of this QueryResultsTopologyInfo.
        The information about the attributes of the topology nodes.


        :param nodes: The nodes of this QueryResultsTopologyInfo.
        :type: list[oci.apm_traces.models.QueryResultsTopologyNodeInfo]
        """
        self._nodes = nodes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
