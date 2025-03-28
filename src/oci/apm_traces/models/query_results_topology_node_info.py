# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class QueryResultsTopologyNodeInfo(object):
    """
    The information about a node attribute.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new QueryResultsTopologyNodeInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param node_name:
            The value to assign to the node_name property of this QueryResultsTopologyNodeInfo.
        :type node_name: str

        """
        self.swagger_types = {
            'node_name': 'str'
        }
        self.attribute_map = {
            'node_name': 'nodeName'
        }
        self._node_name = None

    @property
    def node_name(self):
        """
        Gets the node_name of this QueryResultsTopologyNodeInfo.
        The name of the node attribute.


        :return: The node_name of this QueryResultsTopologyNodeInfo.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """
        Sets the node_name of this QueryResultsTopologyNodeInfo.
        The name of the node attribute.


        :param node_name: The node_name of this QueryResultsTopologyNodeInfo.
        :type: str
        """
        self._node_name = node_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
