# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190531

from .level_type_details import LevelTypeDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NodeLevelDetails(LevelTypeDetails):
    """
    Details of node level used to trigger the creation of a new node backup configuration and node replacement configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NodeLevelDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.bds.models.NodeLevelDetails.level_type` attribute
        of this class is ``NODE_LEVEL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param level_type:
            The value to assign to the level_type property of this NodeLevelDetails.
            Allowed values for this property are: "NODE_LEVEL", "NODE_TYPE_LEVEL"
        :type level_type: str

        :param node_host_name:
            The value to assign to the node_host_name property of this NodeLevelDetails.
        :type node_host_name: str

        """
        self.swagger_types = {
            'level_type': 'str',
            'node_host_name': 'str'
        }
        self.attribute_map = {
            'level_type': 'levelType',
            'node_host_name': 'nodeHostName'
        }
        self._level_type = None
        self._node_host_name = None
        self._level_type = 'NODE_LEVEL'

    @property
    def node_host_name(self):
        """
        **[Required]** Gets the node_host_name of this NodeLevelDetails.
        Host name of the node to create backup configuration.


        :return: The node_host_name of this NodeLevelDetails.
        :rtype: str
        """
        return self._node_host_name

    @node_host_name.setter
    def node_host_name(self, node_host_name):
        """
        Sets the node_host_name of this NodeLevelDetails.
        Host name of the node to create backup configuration.


        :param node_host_name: The node_host_name of this NodeLevelDetails.
        :type: str
        """
        self._node_host_name = node_host_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
