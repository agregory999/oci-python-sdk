# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220315


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateRedisClusterDetails(object):
    """
    The configuration to update for an existing cluster.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateRedisClusterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param shard_count:
            The value to assign to the shard_count property of this UpdateRedisClusterDetails.
        :type shard_count: int

        :param display_name:
            The value to assign to the display_name property of this UpdateRedisClusterDetails.
        :type display_name: str

        :param node_count:
            The value to assign to the node_count property of this UpdateRedisClusterDetails.
        :type node_count: int

        :param node_memory_in_gbs:
            The value to assign to the node_memory_in_gbs property of this UpdateRedisClusterDetails.
        :type node_memory_in_gbs: float

        :param software_version:
            The value to assign to the software_version property of this UpdateRedisClusterDetails.
        :type software_version: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateRedisClusterDetails.
        :type nsg_ids: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateRedisClusterDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateRedisClusterDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'shard_count': 'int',
            'display_name': 'str',
            'node_count': 'int',
            'node_memory_in_gbs': 'float',
            'software_version': 'str',
            'nsg_ids': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'shard_count': 'shardCount',
            'display_name': 'displayName',
            'node_count': 'nodeCount',
            'node_memory_in_gbs': 'nodeMemoryInGBs',
            'software_version': 'softwareVersion',
            'nsg_ids': 'nsgIds',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._shard_count = None
        self._display_name = None
        self._node_count = None
        self._node_memory_in_gbs = None
        self._software_version = None
        self._nsg_ids = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def shard_count(self):
        """
        Gets the shard_count of this UpdateRedisClusterDetails.
        The number of shards in sharded cluster. Only applicable when clusterMode is SHARDED.


        :return: The shard_count of this UpdateRedisClusterDetails.
        :rtype: int
        """
        return self._shard_count

    @shard_count.setter
    def shard_count(self, shard_count):
        """
        Sets the shard_count of this UpdateRedisClusterDetails.
        The number of shards in sharded cluster. Only applicable when clusterMode is SHARDED.


        :param shard_count: The shard_count of this UpdateRedisClusterDetails.
        :type: int
        """
        self._shard_count = shard_count

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateRedisClusterDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this UpdateRedisClusterDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateRedisClusterDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this UpdateRedisClusterDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def node_count(self):
        """
        Gets the node_count of this UpdateRedisClusterDetails.
        The number of nodes per shard in the cluster when clusterMode is SHARDED. This is the total number of nodes when clusterMode is NONSHARDED.


        :return: The node_count of this UpdateRedisClusterDetails.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        """
        Sets the node_count of this UpdateRedisClusterDetails.
        The number of nodes per shard in the cluster when clusterMode is SHARDED. This is the total number of nodes when clusterMode is NONSHARDED.


        :param node_count: The node_count of this UpdateRedisClusterDetails.
        :type: int
        """
        self._node_count = node_count

    @property
    def node_memory_in_gbs(self):
        """
        Gets the node_memory_in_gbs of this UpdateRedisClusterDetails.
        The amount of memory allocated to the cluster's nodes, in gigabytes.


        :return: The node_memory_in_gbs of this UpdateRedisClusterDetails.
        :rtype: float
        """
        return self._node_memory_in_gbs

    @node_memory_in_gbs.setter
    def node_memory_in_gbs(self, node_memory_in_gbs):
        """
        Sets the node_memory_in_gbs of this UpdateRedisClusterDetails.
        The amount of memory allocated to the cluster's nodes, in gigabytes.


        :param node_memory_in_gbs: The node_memory_in_gbs of this UpdateRedisClusterDetails.
        :type: float
        """
        self._node_memory_in_gbs = node_memory_in_gbs

    @property
    def software_version(self):
        """
        Gets the software_version of this UpdateRedisClusterDetails.
        The OCI Cache engine version that the cluster is running.


        :return: The software_version of this UpdateRedisClusterDetails.
        :rtype: str
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version):
        """
        Sets the software_version of this UpdateRedisClusterDetails.
        The OCI Cache engine version that the cluster is running.


        :param software_version: The software_version of this UpdateRedisClusterDetails.
        :type: str
        """
        self._software_version = software_version

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this UpdateRedisClusterDetails.
        A list of Network Security Group (NSG) `OCIDs`__
        associated with this cluster. For more information,
        see `Using an NSG for Clusters`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/iaas/Content/ocicache/connecttocluster.htm#connecttocluster__networksecuritygroup


        :return: The nsg_ids of this UpdateRedisClusterDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this UpdateRedisClusterDetails.
        A list of Network Security Group (NSG) `OCIDs`__
        associated with this cluster. For more information,
        see `Using an NSG for Clusters`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/iaas/Content/ocicache/connecttocluster.htm#connecttocluster__networksecuritygroup


        :param nsg_ids: The nsg_ids of this UpdateRedisClusterDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateRedisClusterDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateRedisClusterDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateRedisClusterDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateRedisClusterDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateRedisClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateRedisClusterDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateRedisClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateRedisClusterDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
