# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateComputeGpuMemoryClusterDetails(object):
    """
    The customer facing object includes GPU memory cluster details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateComputeGpuMemoryClusterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this CreateComputeGpuMemoryClusterDetails.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateComputeGpuMemoryClusterDetails.
        :type compartment_id: str

        :param gpu_memory_fabric_id:
            The value to assign to the gpu_memory_fabric_id property of this CreateComputeGpuMemoryClusterDetails.
        :type gpu_memory_fabric_id: str

        :param compute_cluster_id:
            The value to assign to the compute_cluster_id property of this CreateComputeGpuMemoryClusterDetails.
        :type compute_cluster_id: str

        :param instance_configuration_id:
            The value to assign to the instance_configuration_id property of this CreateComputeGpuMemoryClusterDetails.
        :type instance_configuration_id: str

        :param size:
            The value to assign to the size property of this CreateComputeGpuMemoryClusterDetails.
        :type size: int

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateComputeGpuMemoryClusterDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateComputeGpuMemoryClusterDetails.
        :type freeform_tags: dict(str, str)

        :param display_name:
            The value to assign to the display_name property of this CreateComputeGpuMemoryClusterDetails.
        :type display_name: str

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'gpu_memory_fabric_id': 'str',
            'compute_cluster_id': 'str',
            'instance_configuration_id': 'str',
            'size': 'int',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'display_name': 'str'
        }
        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'gpu_memory_fabric_id': 'gpuMemoryFabricId',
            'compute_cluster_id': 'computeClusterId',
            'instance_configuration_id': 'instanceConfigurationId',
            'size': 'size',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'display_name': 'displayName'
        }
        self._availability_domain = None
        self._compartment_id = None
        self._gpu_memory_fabric_id = None
        self._compute_cluster_id = None
        self._instance_configuration_id = None
        self._size = None
        self._defined_tags = None
        self._freeform_tags = None
        self._display_name = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this CreateComputeGpuMemoryClusterDetails.
        The availability domain of the GPU memory cluster.


        :return: The availability_domain of this CreateComputeGpuMemoryClusterDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CreateComputeGpuMemoryClusterDetails.
        The availability domain of the GPU memory cluster.


        :param availability_domain: The availability_domain of this CreateComputeGpuMemoryClusterDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateComputeGpuMemoryClusterDetails.
        The `OCID`__ of the compartment that contains the compute GPU memory cluster.
        compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateComputeGpuMemoryClusterDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateComputeGpuMemoryClusterDetails.
        The `OCID`__ of the compartment that contains the compute GPU memory cluster.
        compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateComputeGpuMemoryClusterDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def gpu_memory_fabric_id(self):
        """
        Gets the gpu_memory_fabric_id of this CreateComputeGpuMemoryClusterDetails.
        The `OCID`__ of the GPU memory fabric.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The gpu_memory_fabric_id of this CreateComputeGpuMemoryClusterDetails.
        :rtype: str
        """
        return self._gpu_memory_fabric_id

    @gpu_memory_fabric_id.setter
    def gpu_memory_fabric_id(self, gpu_memory_fabric_id):
        """
        Sets the gpu_memory_fabric_id of this CreateComputeGpuMemoryClusterDetails.
        The `OCID`__ of the GPU memory fabric.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param gpu_memory_fabric_id: The gpu_memory_fabric_id of this CreateComputeGpuMemoryClusterDetails.
        :type: str
        """
        self._gpu_memory_fabric_id = gpu_memory_fabric_id

    @property
    def compute_cluster_id(self):
        """
        **[Required]** Gets the compute_cluster_id of this CreateComputeGpuMemoryClusterDetails.
        The `OCID`__ of the compute cluster.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compute_cluster_id of this CreateComputeGpuMemoryClusterDetails.
        :rtype: str
        """
        return self._compute_cluster_id

    @compute_cluster_id.setter
    def compute_cluster_id(self, compute_cluster_id):
        """
        Sets the compute_cluster_id of this CreateComputeGpuMemoryClusterDetails.
        The `OCID`__ of the compute cluster.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compute_cluster_id: The compute_cluster_id of this CreateComputeGpuMemoryClusterDetails.
        :type: str
        """
        self._compute_cluster_id = compute_cluster_id

    @property
    def instance_configuration_id(self):
        """
        **[Required]** Gets the instance_configuration_id of this CreateComputeGpuMemoryClusterDetails.
        Instance Configuration to be used for this GPU Memory Cluster


        :return: The instance_configuration_id of this CreateComputeGpuMemoryClusterDetails.
        :rtype: str
        """
        return self._instance_configuration_id

    @instance_configuration_id.setter
    def instance_configuration_id(self, instance_configuration_id):
        """
        Sets the instance_configuration_id of this CreateComputeGpuMemoryClusterDetails.
        Instance Configuration to be used for this GPU Memory Cluster


        :param instance_configuration_id: The instance_configuration_id of this CreateComputeGpuMemoryClusterDetails.
        :type: str
        """
        self._instance_configuration_id = instance_configuration_id

    @property
    def size(self):
        """
        Gets the size of this CreateComputeGpuMemoryClusterDetails.
        The number of instances currently running in the GpuMemoryCluster


        :return: The size of this CreateComputeGpuMemoryClusterDetails.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this CreateComputeGpuMemoryClusterDetails.
        The number of instances currently running in the GpuMemoryCluster


        :param size: The size of this CreateComputeGpuMemoryClusterDetails.
        :type: int
        """
        self._size = size

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateComputeGpuMemoryClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateComputeGpuMemoryClusterDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateComputeGpuMemoryClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateComputeGpuMemoryClusterDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateComputeGpuMemoryClusterDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateComputeGpuMemoryClusterDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateComputeGpuMemoryClusterDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateComputeGpuMemoryClusterDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateComputeGpuMemoryClusterDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateComputeGpuMemoryClusterDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateComputeGpuMemoryClusterDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateComputeGpuMemoryClusterDetails.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
