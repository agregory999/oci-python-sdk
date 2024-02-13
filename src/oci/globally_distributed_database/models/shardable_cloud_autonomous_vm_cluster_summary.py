# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230301


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ShardableCloudAutonomousVmClusterSummary(object):
    """
    Shardable cloud autonomous vm cluster summary.
    """

    #: A constant which can be used with the lifecycle_state property of a ShardableCloudAutonomousVmClusterSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ShardableCloudAutonomousVmClusterSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a ShardableCloudAutonomousVmClusterSummary.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a ShardableCloudAutonomousVmClusterSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ShardableCloudAutonomousVmClusterSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ShardableCloudAutonomousVmClusterSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ShardableCloudAutonomousVmClusterSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ShardableCloudAutonomousVmClusterSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ShardableCloudAutonomousVmClusterSummary.
    #: This constant has a value of "UNAVAILABLE"
    LIFECYCLE_STATE_UNAVAILABLE = "UNAVAILABLE"

    def __init__(self, **kwargs):
        """
        Initializes a new ShardableCloudAutonomousVmClusterSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ShardableCloudAutonomousVmClusterSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ShardableCloudAutonomousVmClusterSummary.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ShardableCloudAutonomousVmClusterSummary.
            Allowed values for this property are: "ACTIVE", "FAILED", "NEEDS_ATTENTION", "INACTIVE", "DELETING", "DELETED", "UPDATING", "CREATING", "UNAVAILABLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_state_details:
            The value to assign to the lifecycle_state_details property of this ShardableCloudAutonomousVmClusterSummary.
        :type lifecycle_state_details: str

        :param display_name:
            The value to assign to the display_name property of this ShardableCloudAutonomousVmClusterSummary.
        :type display_name: str

        :param compute_model:
            The value to assign to the compute_model property of this ShardableCloudAutonomousVmClusterSummary.
        :type compute_model: str

        :param available_container_databases:
            The value to assign to the available_container_databases property of this ShardableCloudAutonomousVmClusterSummary.
        :type available_container_databases: int

        :param available_cpus:
            The value to assign to the available_cpus property of this ShardableCloudAutonomousVmClusterSummary.
        :type available_cpus: float

        :param availability_domain:
            The value to assign to the availability_domain property of this ShardableCloudAutonomousVmClusterSummary.
        :type availability_domain: str

        :param autonomous_data_storage_size_in_tbs:
            The value to assign to the autonomous_data_storage_size_in_tbs property of this ShardableCloudAutonomousVmClusterSummary.
        :type autonomous_data_storage_size_in_tbs: float

        :param available_autonomous_data_storage_size_in_tbs:
            The value to assign to the available_autonomous_data_storage_size_in_tbs property of this ShardableCloudAutonomousVmClusterSummary.
        :type available_autonomous_data_storage_size_in_tbs: float

        :param cloud_exadata_infrastructure_id:
            The value to assign to the cloud_exadata_infrastructure_id property of this ShardableCloudAutonomousVmClusterSummary.
        :type cloud_exadata_infrastructure_id: str

        :param cluster_time_zone:
            The value to assign to the cluster_time_zone property of this ShardableCloudAutonomousVmClusterSummary.
        :type cluster_time_zone: str

        :param total_container_databases:
            The value to assign to the total_container_databases property of this ShardableCloudAutonomousVmClusterSummary.
        :type total_container_databases: int

        :param subnet_id:
            The value to assign to the subnet_id property of this ShardableCloudAutonomousVmClusterSummary.
        :type subnet_id: str

        :param shape:
            The value to assign to the shape property of this ShardableCloudAutonomousVmClusterSummary.
        :type shape: str

        :param node_count:
            The value to assign to the node_count property of this ShardableCloudAutonomousVmClusterSummary.
        :type node_count: int

        :param license_model:
            The value to assign to the license_model property of this ShardableCloudAutonomousVmClusterSummary.
        :type license_model: str

        :param memory_size_in_gbs:
            The value to assign to the memory_size_in_gbs property of this ShardableCloudAutonomousVmClusterSummary.
        :type memory_size_in_gbs: int

        :param memory_per_oracle_compute_unit_in_gbs:
            The value to assign to the memory_per_oracle_compute_unit_in_gbs property of this ShardableCloudAutonomousVmClusterSummary.
        :type memory_per_oracle_compute_unit_in_gbs: int

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this ShardableCloudAutonomousVmClusterSummary.
        :type cpu_core_count: int

        :param cpu_core_count_per_node:
            The value to assign to the cpu_core_count_per_node property of this ShardableCloudAutonomousVmClusterSummary.
        :type cpu_core_count_per_node: int

        :param ocpu_count:
            The value to assign to the ocpu_count property of this ShardableCloudAutonomousVmClusterSummary.
        :type ocpu_count: float

        :param reclaimable_cpus:
            The value to assign to the reclaimable_cpus property of this ShardableCloudAutonomousVmClusterSummary.
        :type reclaimable_cpus: float

        :param provisionable_autonomous_container_databases:
            The value to assign to the provisionable_autonomous_container_databases property of this ShardableCloudAutonomousVmClusterSummary.
        :type provisionable_autonomous_container_databases: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ShardableCloudAutonomousVmClusterSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ShardableCloudAutonomousVmClusterSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_state_details': 'str',
            'display_name': 'str',
            'compute_model': 'str',
            'available_container_databases': 'int',
            'available_cpus': 'float',
            'availability_domain': 'str',
            'autonomous_data_storage_size_in_tbs': 'float',
            'available_autonomous_data_storage_size_in_tbs': 'float',
            'cloud_exadata_infrastructure_id': 'str',
            'cluster_time_zone': 'str',
            'total_container_databases': 'int',
            'subnet_id': 'str',
            'shape': 'str',
            'node_count': 'int',
            'license_model': 'str',
            'memory_size_in_gbs': 'int',
            'memory_per_oracle_compute_unit_in_gbs': 'int',
            'cpu_core_count': 'int',
            'cpu_core_count_per_node': 'int',
            'ocpu_count': 'float',
            'reclaimable_cpus': 'float',
            'provisionable_autonomous_container_databases': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_state_details': 'lifecycleStateDetails',
            'display_name': 'displayName',
            'compute_model': 'computeModel',
            'available_container_databases': 'availableContainerDatabases',
            'available_cpus': 'availableCpus',
            'availability_domain': 'availabilityDomain',
            'autonomous_data_storage_size_in_tbs': 'autonomousDataStorageSizeInTBs',
            'available_autonomous_data_storage_size_in_tbs': 'availableAutonomousDataStorageSizeInTBs',
            'cloud_exadata_infrastructure_id': 'cloudExadataInfrastructureId',
            'cluster_time_zone': 'clusterTimeZone',
            'total_container_databases': 'totalContainerDatabases',
            'subnet_id': 'subnetId',
            'shape': 'shape',
            'node_count': 'nodeCount',
            'license_model': 'licenseModel',
            'memory_size_in_gbs': 'memorySizeInGBs',
            'memory_per_oracle_compute_unit_in_gbs': 'memoryPerOracleComputeUnitInGBs',
            'cpu_core_count': 'cpuCoreCount',
            'cpu_core_count_per_node': 'cpuCoreCountPerNode',
            'ocpu_count': 'ocpuCount',
            'reclaimable_cpus': 'reclaimableCpus',
            'provisionable_autonomous_container_databases': 'provisionableAutonomousContainerDatabases',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._lifecycle_state_details = None
        self._display_name = None
        self._compute_model = None
        self._available_container_databases = None
        self._available_cpus = None
        self._availability_domain = None
        self._autonomous_data_storage_size_in_tbs = None
        self._available_autonomous_data_storage_size_in_tbs = None
        self._cloud_exadata_infrastructure_id = None
        self._cluster_time_zone = None
        self._total_container_databases = None
        self._subnet_id = None
        self._shape = None
        self._node_count = None
        self._license_model = None
        self._memory_size_in_gbs = None
        self._memory_per_oracle_compute_unit_in_gbs = None
        self._cpu_core_count = None
        self._cpu_core_count_per_node = None
        self._ocpu_count = None
        self._reclaimable_cpus = None
        self._provisionable_autonomous_container_databases = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ShardableCloudAutonomousVmClusterSummary.
        Cloud autonomous vmcluster identifier


        :return: The id of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ShardableCloudAutonomousVmClusterSummary.
        Cloud autonomous vmcluster identifier


        :param id: The id of this ShardableCloudAutonomousVmClusterSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ShardableCloudAutonomousVmClusterSummary.
        Cloud autonomous vmcluster compartment id


        :return: The compartment_id of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ShardableCloudAutonomousVmClusterSummary.
        Cloud autonomous vmcluster compartment id


        :param compartment_id: The compartment_id of this ShardableCloudAutonomousVmClusterSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ShardableCloudAutonomousVmClusterSummary.
        Lifecycle states for shardable Cloud autonomous vm cluster.

        Allowed values for this property are: "ACTIVE", "FAILED", "NEEDS_ATTENTION", "INACTIVE", "DELETING", "DELETED", "UPDATING", "CREATING", "UNAVAILABLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ShardableCloudAutonomousVmClusterSummary.
        Lifecycle states for shardable Cloud autonomous vm cluster.


        :param lifecycle_state: The lifecycle_state of this ShardableCloudAutonomousVmClusterSummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "FAILED", "NEEDS_ATTENTION", "INACTIVE", "DELETING", "DELETED", "UPDATING", "CREATING", "UNAVAILABLE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_state_details(self):
        """
        Gets the lifecycle_state_details of this ShardableCloudAutonomousVmClusterSummary.
        Detailed message for the lifecycle state.


        :return: The lifecycle_state_details of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._lifecycle_state_details

    @lifecycle_state_details.setter
    def lifecycle_state_details(self, lifecycle_state_details):
        """
        Sets the lifecycle_state_details of this ShardableCloudAutonomousVmClusterSummary.
        Detailed message for the lifecycle state.


        :param lifecycle_state_details: The lifecycle_state_details of this ShardableCloudAutonomousVmClusterSummary.
        :type: str
        """
        self._lifecycle_state_details = lifecycle_state_details

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ShardableCloudAutonomousVmClusterSummary.
        Cloud autonomous vmcluster displayName


        :return: The display_name of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ShardableCloudAutonomousVmClusterSummary.
        Cloud autonomous vmcluster displayName


        :param display_name: The display_name of this ShardableCloudAutonomousVmClusterSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compute_model(self):
        """
        Gets the compute_model of this ShardableCloudAutonomousVmClusterSummary.
        The compute model of the Cloud Autonomous VM Cluster.


        :return: The compute_model of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._compute_model

    @compute_model.setter
    def compute_model(self, compute_model):
        """
        Sets the compute_model of this ShardableCloudAutonomousVmClusterSummary.
        The compute model of the Cloud Autonomous VM Cluster.


        :param compute_model: The compute_model of this ShardableCloudAutonomousVmClusterSummary.
        :type: str
        """
        self._compute_model = compute_model

    @property
    def available_container_databases(self):
        """
        Gets the available_container_databases of this ShardableCloudAutonomousVmClusterSummary.
        The number of Autonomous Container Databases that can be created with the currently available local storage.


        :return: The available_container_databases of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: int
        """
        return self._available_container_databases

    @available_container_databases.setter
    def available_container_databases(self, available_container_databases):
        """
        Sets the available_container_databases of this ShardableCloudAutonomousVmClusterSummary.
        The number of Autonomous Container Databases that can be created with the currently available local storage.


        :param available_container_databases: The available_container_databases of this ShardableCloudAutonomousVmClusterSummary.
        :type: int
        """
        self._available_container_databases = available_container_databases

    @property
    def available_cpus(self):
        """
        Gets the available_cpus of this ShardableCloudAutonomousVmClusterSummary.
        CPU cores available for allocation to Autonomous Databases.


        :return: The available_cpus of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: float
        """
        return self._available_cpus

    @available_cpus.setter
    def available_cpus(self, available_cpus):
        """
        Sets the available_cpus of this ShardableCloudAutonomousVmClusterSummary.
        CPU cores available for allocation to Autonomous Databases.


        :param available_cpus: The available_cpus of this ShardableCloudAutonomousVmClusterSummary.
        :type: float
        """
        self._available_cpus = available_cpus

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this ShardableCloudAutonomousVmClusterSummary.
        The name of the availability domain that the cloud Autonomous VM cluster is located in.
        The format of the availability domain is the same as returned by Cloud Autonomous VM Cluster API.


        :return: The availability_domain of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this ShardableCloudAutonomousVmClusterSummary.
        The name of the availability domain that the cloud Autonomous VM cluster is located in.
        The format of the availability domain is the same as returned by Cloud Autonomous VM Cluster API.


        :param availability_domain: The availability_domain of this ShardableCloudAutonomousVmClusterSummary.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def autonomous_data_storage_size_in_tbs(self):
        """
        Gets the autonomous_data_storage_size_in_tbs of this ShardableCloudAutonomousVmClusterSummary.
        The data disk group size allocated for Autonomous Databases, in TBs.


        :return: The autonomous_data_storage_size_in_tbs of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: float
        """
        return self._autonomous_data_storage_size_in_tbs

    @autonomous_data_storage_size_in_tbs.setter
    def autonomous_data_storage_size_in_tbs(self, autonomous_data_storage_size_in_tbs):
        """
        Sets the autonomous_data_storage_size_in_tbs of this ShardableCloudAutonomousVmClusterSummary.
        The data disk group size allocated for Autonomous Databases, in TBs.


        :param autonomous_data_storage_size_in_tbs: The autonomous_data_storage_size_in_tbs of this ShardableCloudAutonomousVmClusterSummary.
        :type: float
        """
        self._autonomous_data_storage_size_in_tbs = autonomous_data_storage_size_in_tbs

    @property
    def available_autonomous_data_storage_size_in_tbs(self):
        """
        Gets the available_autonomous_data_storage_size_in_tbs of this ShardableCloudAutonomousVmClusterSummary.
        The data disk group size available for Autonomous Databases, in TBs.


        :return: The available_autonomous_data_storage_size_in_tbs of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: float
        """
        return self._available_autonomous_data_storage_size_in_tbs

    @available_autonomous_data_storage_size_in_tbs.setter
    def available_autonomous_data_storage_size_in_tbs(self, available_autonomous_data_storage_size_in_tbs):
        """
        Sets the available_autonomous_data_storage_size_in_tbs of this ShardableCloudAutonomousVmClusterSummary.
        The data disk group size available for Autonomous Databases, in TBs.


        :param available_autonomous_data_storage_size_in_tbs: The available_autonomous_data_storage_size_in_tbs of this ShardableCloudAutonomousVmClusterSummary.
        :type: float
        """
        self._available_autonomous_data_storage_size_in_tbs = available_autonomous_data_storage_size_in_tbs

    @property
    def cloud_exadata_infrastructure_id(self):
        """
        Gets the cloud_exadata_infrastructure_id of this ShardableCloudAutonomousVmClusterSummary.
        Cloud Exadata Infrastructure Identifier.


        :return: The cloud_exadata_infrastructure_id of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._cloud_exadata_infrastructure_id

    @cloud_exadata_infrastructure_id.setter
    def cloud_exadata_infrastructure_id(self, cloud_exadata_infrastructure_id):
        """
        Sets the cloud_exadata_infrastructure_id of this ShardableCloudAutonomousVmClusterSummary.
        Cloud Exadata Infrastructure Identifier.


        :param cloud_exadata_infrastructure_id: The cloud_exadata_infrastructure_id of this ShardableCloudAutonomousVmClusterSummary.
        :type: str
        """
        self._cloud_exadata_infrastructure_id = cloud_exadata_infrastructure_id

    @property
    def cluster_time_zone(self):
        """
        Gets the cluster_time_zone of this ShardableCloudAutonomousVmClusterSummary.
        The time zone of the Cloud Autonomous VM Cluster.


        :return: The cluster_time_zone of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._cluster_time_zone

    @cluster_time_zone.setter
    def cluster_time_zone(self, cluster_time_zone):
        """
        Sets the cluster_time_zone of this ShardableCloudAutonomousVmClusterSummary.
        The time zone of the Cloud Autonomous VM Cluster.


        :param cluster_time_zone: The cluster_time_zone of this ShardableCloudAutonomousVmClusterSummary.
        :type: str
        """
        self._cluster_time_zone = cluster_time_zone

    @property
    def total_container_databases(self):
        """
        Gets the total_container_databases of this ShardableCloudAutonomousVmClusterSummary.
        The total number of Autonomous Container Databases that can be created with the allocated local storage.


        :return: The total_container_databases of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: int
        """
        return self._total_container_databases

    @total_container_databases.setter
    def total_container_databases(self, total_container_databases):
        """
        Sets the total_container_databases of this ShardableCloudAutonomousVmClusterSummary.
        The total number of Autonomous Container Databases that can be created with the allocated local storage.


        :param total_container_databases: The total_container_databases of this ShardableCloudAutonomousVmClusterSummary.
        :type: int
        """
        self._total_container_databases = total_container_databases

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this ShardableCloudAutonomousVmClusterSummary.
        Cloud autonomous vmcluster subnet id


        :return: The subnet_id of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this ShardableCloudAutonomousVmClusterSummary.
        Cloud autonomous vmcluster subnet id


        :param subnet_id: The subnet_id of this ShardableCloudAutonomousVmClusterSummary.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def shape(self):
        """
        Gets the shape of this ShardableCloudAutonomousVmClusterSummary.
        Cloud autonomous vmcluster shape


        :return: The shape of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this ShardableCloudAutonomousVmClusterSummary.
        Cloud autonomous vmcluster shape


        :param shape: The shape of this ShardableCloudAutonomousVmClusterSummary.
        :type: str
        """
        self._shape = shape

    @property
    def node_count(self):
        """
        Gets the node_count of this ShardableCloudAutonomousVmClusterSummary.
        Cloud autonomous vmcluster node count


        :return: The node_count of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        """
        Sets the node_count of this ShardableCloudAutonomousVmClusterSummary.
        Cloud autonomous vmcluster node count


        :param node_count: The node_count of this ShardableCloudAutonomousVmClusterSummary.
        :type: int
        """
        self._node_count = node_count

    @property
    def license_model(self):
        """
        Gets the license_model of this ShardableCloudAutonomousVmClusterSummary.
        The Oracle license model that applies to the Oracle Autonomous Database.


        :return: The license_model of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this ShardableCloudAutonomousVmClusterSummary.
        The Oracle license model that applies to the Oracle Autonomous Database.


        :param license_model: The license_model of this ShardableCloudAutonomousVmClusterSummary.
        :type: str
        """
        self._license_model = license_model

    @property
    def memory_size_in_gbs(self):
        """
        Gets the memory_size_in_gbs of this ShardableCloudAutonomousVmClusterSummary.
        The memory allocated in GBs.


        :return: The memory_size_in_gbs of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: int
        """
        return self._memory_size_in_gbs

    @memory_size_in_gbs.setter
    def memory_size_in_gbs(self, memory_size_in_gbs):
        """
        Sets the memory_size_in_gbs of this ShardableCloudAutonomousVmClusterSummary.
        The memory allocated in GBs.


        :param memory_size_in_gbs: The memory_size_in_gbs of this ShardableCloudAutonomousVmClusterSummary.
        :type: int
        """
        self._memory_size_in_gbs = memory_size_in_gbs

    @property
    def memory_per_oracle_compute_unit_in_gbs(self):
        """
        Gets the memory_per_oracle_compute_unit_in_gbs of this ShardableCloudAutonomousVmClusterSummary.
        The amount of memory (in GBs) enabled per OCPU or ECPU.


        :return: The memory_per_oracle_compute_unit_in_gbs of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: int
        """
        return self._memory_per_oracle_compute_unit_in_gbs

    @memory_per_oracle_compute_unit_in_gbs.setter
    def memory_per_oracle_compute_unit_in_gbs(self, memory_per_oracle_compute_unit_in_gbs):
        """
        Sets the memory_per_oracle_compute_unit_in_gbs of this ShardableCloudAutonomousVmClusterSummary.
        The amount of memory (in GBs) enabled per OCPU or ECPU.


        :param memory_per_oracle_compute_unit_in_gbs: The memory_per_oracle_compute_unit_in_gbs of this ShardableCloudAutonomousVmClusterSummary.
        :type: int
        """
        self._memory_per_oracle_compute_unit_in_gbs = memory_per_oracle_compute_unit_in_gbs

    @property
    def cpu_core_count(self):
        """
        Gets the cpu_core_count of this ShardableCloudAutonomousVmClusterSummary.
        The number of CPU cores on the cloud Autonomous VM cluster.


        :return: The cpu_core_count of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this ShardableCloudAutonomousVmClusterSummary.
        The number of CPU cores on the cloud Autonomous VM cluster.


        :param cpu_core_count: The cpu_core_count of this ShardableCloudAutonomousVmClusterSummary.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def cpu_core_count_per_node(self):
        """
        Gets the cpu_core_count_per_node of this ShardableCloudAutonomousVmClusterSummary.
        The number of CPU cores enabled per VM cluster node.


        :return: The cpu_core_count_per_node of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: int
        """
        return self._cpu_core_count_per_node

    @cpu_core_count_per_node.setter
    def cpu_core_count_per_node(self, cpu_core_count_per_node):
        """
        Sets the cpu_core_count_per_node of this ShardableCloudAutonomousVmClusterSummary.
        The number of CPU cores enabled per VM cluster node.


        :param cpu_core_count_per_node: The cpu_core_count_per_node of this ShardableCloudAutonomousVmClusterSummary.
        :type: int
        """
        self._cpu_core_count_per_node = cpu_core_count_per_node

    @property
    def ocpu_count(self):
        """
        Gets the ocpu_count of this ShardableCloudAutonomousVmClusterSummary.
        The number of CPU cores on the cloud Autonomous VM cluster.


        :return: The ocpu_count of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: float
        """
        return self._ocpu_count

    @ocpu_count.setter
    def ocpu_count(self, ocpu_count):
        """
        Sets the ocpu_count of this ShardableCloudAutonomousVmClusterSummary.
        The number of CPU cores on the cloud Autonomous VM cluster.


        :param ocpu_count: The ocpu_count of this ShardableCloudAutonomousVmClusterSummary.
        :type: float
        """
        self._ocpu_count = ocpu_count

    @property
    def reclaimable_cpus(self):
        """
        Gets the reclaimable_cpus of this ShardableCloudAutonomousVmClusterSummary.
        The CPUs that continue to be included in the count of CPUs available to the Autonomous Container Database even after one of its Autonomous Database is terminated or scaled down. You can release them to the available CPUs at its parent Autonomous VM Cluster level by restarting the Autonomous Container Database.


        :return: The reclaimable_cpus of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: float
        """
        return self._reclaimable_cpus

    @reclaimable_cpus.setter
    def reclaimable_cpus(self, reclaimable_cpus):
        """
        Sets the reclaimable_cpus of this ShardableCloudAutonomousVmClusterSummary.
        The CPUs that continue to be included in the count of CPUs available to the Autonomous Container Database even after one of its Autonomous Database is terminated or scaled down. You can release them to the available CPUs at its parent Autonomous VM Cluster level by restarting the Autonomous Container Database.


        :param reclaimable_cpus: The reclaimable_cpus of this ShardableCloudAutonomousVmClusterSummary.
        :type: float
        """
        self._reclaimable_cpus = reclaimable_cpus

    @property
    def provisionable_autonomous_container_databases(self):
        """
        Gets the provisionable_autonomous_container_databases of this ShardableCloudAutonomousVmClusterSummary.
        Number of Autonomous Container Databases that can be created in the Autonomous VM Cluster


        :return: The provisionable_autonomous_container_databases of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: int
        """
        return self._provisionable_autonomous_container_databases

    @provisionable_autonomous_container_databases.setter
    def provisionable_autonomous_container_databases(self, provisionable_autonomous_container_databases):
        """
        Sets the provisionable_autonomous_container_databases of this ShardableCloudAutonomousVmClusterSummary.
        Number of Autonomous Container Databases that can be created in the Autonomous VM Cluster


        :param provisionable_autonomous_container_databases: The provisionable_autonomous_container_databases of this ShardableCloudAutonomousVmClusterSummary.
        :type: int
        """
        self._provisionable_autonomous_container_databases = provisionable_autonomous_container_databases

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ShardableCloudAutonomousVmClusterSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ShardableCloudAutonomousVmClusterSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ShardableCloudAutonomousVmClusterSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ShardableCloudAutonomousVmClusterSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ShardableCloudAutonomousVmClusterSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ShardableCloudAutonomousVmClusterSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ShardableCloudAutonomousVmClusterSummary.
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