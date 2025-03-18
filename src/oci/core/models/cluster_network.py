# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ClusterNetwork(object):
    """
    A cluster network is a group of high performance computing (HPC), GPU, or optimized bare metal
    instances that are connected with an ultra low-latency remote direct memory access (RDMA)
    network. `Cluster networks with instance pools`__
    use instance pools to manage groups of identical instances.

    Use cluster networks with instance pools when you want predictable capacity for a specific number of identical
    instances that are managed as a group.

    If you want to manage instances in the RDMA network independently of each other or use different types of instances
    in the network group, use compute clusters instead. For details, see :class:`ComputeCluster`.

    __ https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/managingclusternetworks.htm
    """

    #: A constant which can be used with the lifecycle_state property of a ClusterNetwork.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a ClusterNetwork.
    #: This constant has a value of "SCALING"
    LIFECYCLE_STATE_SCALING = "SCALING"

    #: A constant which can be used with the lifecycle_state property of a ClusterNetwork.
    #: This constant has a value of "STARTING"
    LIFECYCLE_STATE_STARTING = "STARTING"

    #: A constant which can be used with the lifecycle_state property of a ClusterNetwork.
    #: This constant has a value of "STOPPING"
    LIFECYCLE_STATE_STOPPING = "STOPPING"

    #: A constant which can be used with the lifecycle_state property of a ClusterNetwork.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a ClusterNetwork.
    #: This constant has a value of "STOPPED"
    LIFECYCLE_STATE_STOPPED = "STOPPED"

    #: A constant which can be used with the lifecycle_state property of a ClusterNetwork.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a ClusterNetwork.
    #: This constant has a value of "RUNNING"
    LIFECYCLE_STATE_RUNNING = "RUNNING"

    def __init__(self, **kwargs):
        """
        Initializes a new ClusterNetwork object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ClusterNetwork.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ClusterNetwork.
        :type compartment_id: str

        :param hpc_island_id:
            The value to assign to the hpc_island_id property of this ClusterNetwork.
        :type hpc_island_id: str

        :param network_block_ids:
            The value to assign to the network_block_ids property of this ClusterNetwork.
        :type network_block_ids: list[str]

        :param defined_tags:
            The value to assign to the defined_tags property of this ClusterNetwork.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this ClusterNetwork.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ClusterNetwork.
        :type freeform_tags: dict(str, str)

        :param instance_pools:
            The value to assign to the instance_pools property of this ClusterNetwork.
        :type instance_pools: list[oci.core.models.InstancePool]

        :param placement_configuration:
            The value to assign to the placement_configuration property of this ClusterNetwork.
        :type placement_configuration: oci.core.models.ClusterNetworkPlacementConfigurationDetails

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ClusterNetwork.
            Allowed values for this property are: "PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this ClusterNetwork.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ClusterNetwork.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'hpc_island_id': 'str',
            'network_block_ids': 'list[str]',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'instance_pools': 'list[InstancePool]',
            'placement_configuration': 'ClusterNetworkPlacementConfigurationDetails',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }
        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'hpc_island_id': 'hpcIslandId',
            'network_block_ids': 'networkBlockIds',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'instance_pools': 'instancePools',
            'placement_configuration': 'placementConfiguration',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }
        self._id = None
        self._compartment_id = None
        self._hpc_island_id = None
        self._network_block_ids = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._instance_pools = None
        self._placement_configuration = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ClusterNetwork.
        The `OCID`__ of the cluster network.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this ClusterNetwork.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ClusterNetwork.
        The `OCID`__ of the cluster network.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this ClusterNetwork.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ClusterNetwork.
        The `OCID`__ of the compartment containing the cluster network.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ClusterNetwork.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ClusterNetwork.
        The `OCID`__ of the compartment containing the cluster network.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ClusterNetwork.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def hpc_island_id(self):
        """
        Gets the hpc_island_id of this ClusterNetwork.
        The `OCID`__ of the HPC island used by the cluster network.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The hpc_island_id of this ClusterNetwork.
        :rtype: str
        """
        return self._hpc_island_id

    @hpc_island_id.setter
    def hpc_island_id(self, hpc_island_id):
        """
        Sets the hpc_island_id of this ClusterNetwork.
        The `OCID`__ of the HPC island used by the cluster network.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param hpc_island_id: The hpc_island_id of this ClusterNetwork.
        :type: str
        """
        self._hpc_island_id = hpc_island_id

    @property
    def network_block_ids(self):
        """
        Gets the network_block_ids of this ClusterNetwork.
        The list of network block OCIDs of the HPC island.


        :return: The network_block_ids of this ClusterNetwork.
        :rtype: list[str]
        """
        return self._network_block_ids

    @network_block_ids.setter
    def network_block_ids(self, network_block_ids):
        """
        Sets the network_block_ids of this ClusterNetwork.
        The list of network block OCIDs of the HPC island.


        :param network_block_ids: The network_block_ids of this ClusterNetwork.
        :type: list[str]
        """
        self._network_block_ids = network_block_ids

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ClusterNetwork.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ClusterNetwork.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ClusterNetwork.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ClusterNetwork.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this ClusterNetwork.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this ClusterNetwork.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ClusterNetwork.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this ClusterNetwork.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ClusterNetwork.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ClusterNetwork.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ClusterNetwork.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ClusterNetwork.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def instance_pools(self):
        """
        Gets the instance_pools of this ClusterNetwork.
        The instance pools in the cluster network.

        Each cluster network can have one instance pool.


        :return: The instance_pools of this ClusterNetwork.
        :rtype: list[oci.core.models.InstancePool]
        """
        return self._instance_pools

    @instance_pools.setter
    def instance_pools(self, instance_pools):
        """
        Sets the instance_pools of this ClusterNetwork.
        The instance pools in the cluster network.

        Each cluster network can have one instance pool.


        :param instance_pools: The instance_pools of this ClusterNetwork.
        :type: list[oci.core.models.InstancePool]
        """
        self._instance_pools = instance_pools

    @property
    def placement_configuration(self):
        """
        Gets the placement_configuration of this ClusterNetwork.

        :return: The placement_configuration of this ClusterNetwork.
        :rtype: oci.core.models.ClusterNetworkPlacementConfigurationDetails
        """
        return self._placement_configuration

    @placement_configuration.setter
    def placement_configuration(self, placement_configuration):
        """
        Sets the placement_configuration of this ClusterNetwork.

        :param placement_configuration: The placement_configuration of this ClusterNetwork.
        :type: oci.core.models.ClusterNetworkPlacementConfigurationDetails
        """
        self._placement_configuration = placement_configuration

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ClusterNetwork.
        The current state of the cluster network.

        Allowed values for this property are: "PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ClusterNetwork.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ClusterNetwork.
        The current state of the cluster network.


        :param lifecycle_state: The lifecycle_state of this ClusterNetwork.
        :type: str
        """
        allowed_values = ["PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ClusterNetwork.
        The date and time the resource was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ClusterNetwork.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ClusterNetwork.
        The date and time the resource was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ClusterNetwork.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ClusterNetwork.
        The date and time the resource was updated, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this ClusterNetwork.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ClusterNetwork.
        The date and time the resource was updated, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this ClusterNetwork.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
