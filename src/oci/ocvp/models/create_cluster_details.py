# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230701


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateClusterDetails(object):
    """
    Details of the Cluster.
    """

    #: A constant which can be used with the initial_commitment property of a CreateClusterDetails.
    #: This constant has a value of "HOUR"
    INITIAL_COMMITMENT_HOUR = "HOUR"

    #: A constant which can be used with the initial_commitment property of a CreateClusterDetails.
    #: This constant has a value of "MONTH"
    INITIAL_COMMITMENT_MONTH = "MONTH"

    #: A constant which can be used with the initial_commitment property of a CreateClusterDetails.
    #: This constant has a value of "ONE_YEAR"
    INITIAL_COMMITMENT_ONE_YEAR = "ONE_YEAR"

    #: A constant which can be used with the initial_commitment property of a CreateClusterDetails.
    #: This constant has a value of "THREE_YEARS"
    INITIAL_COMMITMENT_THREE_YEARS = "THREE_YEARS"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateClusterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sddc_id:
            The value to assign to the sddc_id property of this CreateClusterDetails.
        :type sddc_id: str

        :param compute_availability_domain:
            The value to assign to the compute_availability_domain property of this CreateClusterDetails.
        :type compute_availability_domain: str

        :param display_name:
            The value to assign to the display_name property of this CreateClusterDetails.
        :type display_name: str

        :param instance_display_name_prefix:
            The value to assign to the instance_display_name_prefix property of this CreateClusterDetails.
        :type instance_display_name_prefix: str

        :param esxi_hosts_count:
            The value to assign to the esxi_hosts_count property of this CreateClusterDetails.
        :type esxi_hosts_count: int

        :param network_configuration:
            The value to assign to the network_configuration property of this CreateClusterDetails.
        :type network_configuration: oci.ocvp.models.NetworkConfiguration

        :param initial_commitment:
            The value to assign to the initial_commitment property of this CreateClusterDetails.
            Allowed values for this property are: "HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS"
        :type initial_commitment: str

        :param workload_network_cidr:
            The value to assign to the workload_network_cidr property of this CreateClusterDetails.
        :type workload_network_cidr: str

        :param initial_host_shape_name:
            The value to assign to the initial_host_shape_name property of this CreateClusterDetails.
        :type initial_host_shape_name: str

        :param initial_host_ocpu_count:
            The value to assign to the initial_host_ocpu_count property of this CreateClusterDetails.
        :type initial_host_ocpu_count: float

        :param is_shielded_instance_enabled:
            The value to assign to the is_shielded_instance_enabled property of this CreateClusterDetails.
        :type is_shielded_instance_enabled: bool

        :param capacity_reservation_id:
            The value to assign to the capacity_reservation_id property of this CreateClusterDetails.
        :type capacity_reservation_id: str

        :param datastores:
            The value to assign to the datastores property of this CreateClusterDetails.
        :type datastores: list[oci.ocvp.models.DatastoreInfo]

        :param vmware_software_version:
            The value to assign to the vmware_software_version property of this CreateClusterDetails.
        :type vmware_software_version: str

        :param esxi_software_version:
            The value to assign to the esxi_software_version property of this CreateClusterDetails.
        :type esxi_software_version: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateClusterDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateClusterDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'sddc_id': 'str',
            'compute_availability_domain': 'str',
            'display_name': 'str',
            'instance_display_name_prefix': 'str',
            'esxi_hosts_count': 'int',
            'network_configuration': 'NetworkConfiguration',
            'initial_commitment': 'str',
            'workload_network_cidr': 'str',
            'initial_host_shape_name': 'str',
            'initial_host_ocpu_count': 'float',
            'is_shielded_instance_enabled': 'bool',
            'capacity_reservation_id': 'str',
            'datastores': 'list[DatastoreInfo]',
            'vmware_software_version': 'str',
            'esxi_software_version': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'sddc_id': 'sddcId',
            'compute_availability_domain': 'computeAvailabilityDomain',
            'display_name': 'displayName',
            'instance_display_name_prefix': 'instanceDisplayNamePrefix',
            'esxi_hosts_count': 'esxiHostsCount',
            'network_configuration': 'networkConfiguration',
            'initial_commitment': 'initialCommitment',
            'workload_network_cidr': 'workloadNetworkCidr',
            'initial_host_shape_name': 'initialHostShapeName',
            'initial_host_ocpu_count': 'initialHostOcpuCount',
            'is_shielded_instance_enabled': 'isShieldedInstanceEnabled',
            'capacity_reservation_id': 'capacityReservationId',
            'datastores': 'datastores',
            'vmware_software_version': 'vmwareSoftwareVersion',
            'esxi_software_version': 'esxiSoftwareVersion',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._sddc_id = None
        self._compute_availability_domain = None
        self._display_name = None
        self._instance_display_name_prefix = None
        self._esxi_hosts_count = None
        self._network_configuration = None
        self._initial_commitment = None
        self._workload_network_cidr = None
        self._initial_host_shape_name = None
        self._initial_host_ocpu_count = None
        self._is_shielded_instance_enabled = None
        self._capacity_reservation_id = None
        self._datastores = None
        self._vmware_software_version = None
        self._esxi_software_version = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def sddc_id(self):
        """
        **[Required]** Gets the sddc_id of this CreateClusterDetails.
        The `OCID`__ of the SDDC that the
        Cluster belongs to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The sddc_id of this CreateClusterDetails.
        :rtype: str
        """
        return self._sddc_id

    @sddc_id.setter
    def sddc_id(self, sddc_id):
        """
        Sets the sddc_id of this CreateClusterDetails.
        The `OCID`__ of the SDDC that the
        Cluster belongs to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param sddc_id: The sddc_id of this CreateClusterDetails.
        :type: str
        """
        self._sddc_id = sddc_id

    @property
    def compute_availability_domain(self):
        """
        **[Required]** Gets the compute_availability_domain of this CreateClusterDetails.
        The availability domain to create the Cluster's ESXi hosts in. For multi-AD Cluster deployment, set to `multi-AD`.


        :return: The compute_availability_domain of this CreateClusterDetails.
        :rtype: str
        """
        return self._compute_availability_domain

    @compute_availability_domain.setter
    def compute_availability_domain(self, compute_availability_domain):
        """
        Sets the compute_availability_domain of this CreateClusterDetails.
        The availability domain to create the Cluster's ESXi hosts in. For multi-AD Cluster deployment, set to `multi-AD`.


        :param compute_availability_domain: The compute_availability_domain of this CreateClusterDetails.
        :type: str
        """
        self._compute_availability_domain = compute_availability_domain

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateClusterDetails.
        A descriptive name for the Cluster.
        Cluster name requirements are 1-16 character length limit, Must start with a letter, Must be English letters, numbers, - only, No repeating hyphens, Must be unique within the region.
        Avoid entering confidential information.


        :return: The display_name of this CreateClusterDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateClusterDetails.
        A descriptive name for the Cluster.
        Cluster name requirements are 1-16 character length limit, Must start with a letter, Must be English letters, numbers, - only, No repeating hyphens, Must be unique within the region.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateClusterDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def instance_display_name_prefix(self):
        """
        Gets the instance_display_name_prefix of this CreateClusterDetails.
        A prefix used in the name of each ESXi host and Compute instance in the Cluster.
        If this isn't set, the Cluster's `displayName` is used as the prefix.

        For example, if the value is `myCluster`, the ESXi hosts are named `myCluster-1`,
        `myCluster-2`, and so on.


        :return: The instance_display_name_prefix of this CreateClusterDetails.
        :rtype: str
        """
        return self._instance_display_name_prefix

    @instance_display_name_prefix.setter
    def instance_display_name_prefix(self, instance_display_name_prefix):
        """
        Sets the instance_display_name_prefix of this CreateClusterDetails.
        A prefix used in the name of each ESXi host and Compute instance in the Cluster.
        If this isn't set, the Cluster's `displayName` is used as the prefix.

        For example, if the value is `myCluster`, the ESXi hosts are named `myCluster-1`,
        `myCluster-2`, and so on.


        :param instance_display_name_prefix: The instance_display_name_prefix of this CreateClusterDetails.
        :type: str
        """
        self._instance_display_name_prefix = instance_display_name_prefix

    @property
    def esxi_hosts_count(self):
        """
        **[Required]** Gets the esxi_hosts_count of this CreateClusterDetails.
        The number of ESXi hosts to create in the Cluster. You can add more hosts later
        (see :func:`create_esxi_host`).

        **Note:** If you later delete EXSi hosts from a production Cluster to make SDDC
        total host count less than 3, you are still billed for the 3 minimum recommended
        ESXi hosts. Also, you cannot add more VMware workloads to the Cluster until the
        SDDC again has at least 3 ESXi hosts.


        :return: The esxi_hosts_count of this CreateClusterDetails.
        :rtype: int
        """
        return self._esxi_hosts_count

    @esxi_hosts_count.setter
    def esxi_hosts_count(self, esxi_hosts_count):
        """
        Sets the esxi_hosts_count of this CreateClusterDetails.
        The number of ESXi hosts to create in the Cluster. You can add more hosts later
        (see :func:`create_esxi_host`).

        **Note:** If you later delete EXSi hosts from a production Cluster to make SDDC
        total host count less than 3, you are still billed for the 3 minimum recommended
        ESXi hosts. Also, you cannot add more VMware workloads to the Cluster until the
        SDDC again has at least 3 ESXi hosts.


        :param esxi_hosts_count: The esxi_hosts_count of this CreateClusterDetails.
        :type: int
        """
        self._esxi_hosts_count = esxi_hosts_count

    @property
    def network_configuration(self):
        """
        **[Required]** Gets the network_configuration of this CreateClusterDetails.

        :return: The network_configuration of this CreateClusterDetails.
        :rtype: oci.ocvp.models.NetworkConfiguration
        """
        return self._network_configuration

    @network_configuration.setter
    def network_configuration(self, network_configuration):
        """
        Sets the network_configuration of this CreateClusterDetails.

        :param network_configuration: The network_configuration of this CreateClusterDetails.
        :type: oci.ocvp.models.NetworkConfiguration
        """
        self._network_configuration = network_configuration

    @property
    def initial_commitment(self):
        """
        Gets the initial_commitment of this CreateClusterDetails.
        The billing option selected during Cluster creation.
        :func:`list_supported_commitments`.

        Allowed values for this property are: "HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS"


        :return: The initial_commitment of this CreateClusterDetails.
        :rtype: str
        """
        return self._initial_commitment

    @initial_commitment.setter
    def initial_commitment(self, initial_commitment):
        """
        Sets the initial_commitment of this CreateClusterDetails.
        The billing option selected during Cluster creation.
        :func:`list_supported_commitments`.


        :param initial_commitment: The initial_commitment of this CreateClusterDetails.
        :type: str
        """
        allowed_values = ["HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS"]
        if not value_allowed_none_or_none_sentinel(initial_commitment, allowed_values):
            raise ValueError(
                f"Invalid value for `initial_commitment`, must be None or one of {allowed_values}"
            )
        self._initial_commitment = initial_commitment

    @property
    def workload_network_cidr(self):
        """
        Gets the workload_network_cidr of this CreateClusterDetails.
        The CIDR block for the IP addresses that VMware VMs in the Cluster use to run application
        workloads.


        :return: The workload_network_cidr of this CreateClusterDetails.
        :rtype: str
        """
        return self._workload_network_cidr

    @workload_network_cidr.setter
    def workload_network_cidr(self, workload_network_cidr):
        """
        Sets the workload_network_cidr of this CreateClusterDetails.
        The CIDR block for the IP addresses that VMware VMs in the Cluster use to run application
        workloads.


        :param workload_network_cidr: The workload_network_cidr of this CreateClusterDetails.
        :type: str
        """
        self._workload_network_cidr = workload_network_cidr

    @property
    def initial_host_shape_name(self):
        """
        Gets the initial_host_shape_name of this CreateClusterDetails.
        The initial compute shape of the Cluster's ESXi hosts.
        :func:`list_supported_host_shapes`.


        :return: The initial_host_shape_name of this CreateClusterDetails.
        :rtype: str
        """
        return self._initial_host_shape_name

    @initial_host_shape_name.setter
    def initial_host_shape_name(self, initial_host_shape_name):
        """
        Sets the initial_host_shape_name of this CreateClusterDetails.
        The initial compute shape of the Cluster's ESXi hosts.
        :func:`list_supported_host_shapes`.


        :param initial_host_shape_name: The initial_host_shape_name of this CreateClusterDetails.
        :type: str
        """
        self._initial_host_shape_name = initial_host_shape_name

    @property
    def initial_host_ocpu_count(self):
        """
        Gets the initial_host_ocpu_count of this CreateClusterDetails.
        The initial OCPU count of the Cluster's ESXi hosts.


        :return: The initial_host_ocpu_count of this CreateClusterDetails.
        :rtype: float
        """
        return self._initial_host_ocpu_count

    @initial_host_ocpu_count.setter
    def initial_host_ocpu_count(self, initial_host_ocpu_count):
        """
        Sets the initial_host_ocpu_count of this CreateClusterDetails.
        The initial OCPU count of the Cluster's ESXi hosts.


        :param initial_host_ocpu_count: The initial_host_ocpu_count of this CreateClusterDetails.
        :type: float
        """
        self._initial_host_ocpu_count = initial_host_ocpu_count

    @property
    def is_shielded_instance_enabled(self):
        """
        Gets the is_shielded_instance_enabled of this CreateClusterDetails.
        Indicates whether shielded instance is enabled for this Cluster.


        :return: The is_shielded_instance_enabled of this CreateClusterDetails.
        :rtype: bool
        """
        return self._is_shielded_instance_enabled

    @is_shielded_instance_enabled.setter
    def is_shielded_instance_enabled(self, is_shielded_instance_enabled):
        """
        Sets the is_shielded_instance_enabled of this CreateClusterDetails.
        Indicates whether shielded instance is enabled for this Cluster.


        :param is_shielded_instance_enabled: The is_shielded_instance_enabled of this CreateClusterDetails.
        :type: bool
        """
        self._is_shielded_instance_enabled = is_shielded_instance_enabled

    @property
    def capacity_reservation_id(self):
        """
        Gets the capacity_reservation_id of this CreateClusterDetails.
        The `OCID`__ of the Capacity Reservation.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The capacity_reservation_id of this CreateClusterDetails.
        :rtype: str
        """
        return self._capacity_reservation_id

    @capacity_reservation_id.setter
    def capacity_reservation_id(self, capacity_reservation_id):
        """
        Sets the capacity_reservation_id of this CreateClusterDetails.
        The `OCID`__ of the Capacity Reservation.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param capacity_reservation_id: The capacity_reservation_id of this CreateClusterDetails.
        :type: str
        """
        self._capacity_reservation_id = capacity_reservation_id

    @property
    def datastores(self):
        """
        Gets the datastores of this CreateClusterDetails.
        A list of datastore info for the Cluster.
        This value is required only when `initialHostShapeName` is a standard shape.


        :return: The datastores of this CreateClusterDetails.
        :rtype: list[oci.ocvp.models.DatastoreInfo]
        """
        return self._datastores

    @datastores.setter
    def datastores(self, datastores):
        """
        Sets the datastores of this CreateClusterDetails.
        A list of datastore info for the Cluster.
        This value is required only when `initialHostShapeName` is a standard shape.


        :param datastores: The datastores of this CreateClusterDetails.
        :type: list[oci.ocvp.models.DatastoreInfo]
        """
        self._datastores = datastores

    @property
    def vmware_software_version(self):
        """
        Gets the vmware_software_version of this CreateClusterDetails.
        The VMware software bundle to install on the ESXi hosts in the Cluster. To get a list of the available versions, use
        :func:`list_supported_vmware_software_versions`.


        :return: The vmware_software_version of this CreateClusterDetails.
        :rtype: str
        """
        return self._vmware_software_version

    @vmware_software_version.setter
    def vmware_software_version(self, vmware_software_version):
        """
        Sets the vmware_software_version of this CreateClusterDetails.
        The VMware software bundle to install on the ESXi hosts in the Cluster. To get a list of the available versions, use
        :func:`list_supported_vmware_software_versions`.


        :param vmware_software_version: The vmware_software_version of this CreateClusterDetails.
        :type: str
        """
        self._vmware_software_version = vmware_software_version

    @property
    def esxi_software_version(self):
        """
        Gets the esxi_software_version of this CreateClusterDetails.
        The ESXi software bundle to install on the ESXi hosts in the Cluster.
        Only versions under the same vmwareSoftwareVersion and have been validate by Oracle Cloud VMware Solution will be accepted.
        To get a list of the available versions, use
        :func:`list_supported_vmware_software_versions`.


        :return: The esxi_software_version of this CreateClusterDetails.
        :rtype: str
        """
        return self._esxi_software_version

    @esxi_software_version.setter
    def esxi_software_version(self, esxi_software_version):
        """
        Sets the esxi_software_version of this CreateClusterDetails.
        The ESXi software bundle to install on the ESXi hosts in the Cluster.
        Only versions under the same vmwareSoftwareVersion and have been validate by Oracle Cloud VMware Solution will be accepted.
        To get a list of the available versions, use
        :func:`list_supported_vmware_software_versions`.


        :param esxi_software_version: The esxi_software_version of this CreateClusterDetails.
        :type: str
        """
        self._esxi_software_version = esxi_software_version

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateClusterDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateClusterDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateClusterDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateClusterDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateClusterDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateClusterDetails.
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
