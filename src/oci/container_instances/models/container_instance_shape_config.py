# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210415


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContainerInstanceShapeConfig(object):
    """
    The shape configuration for a container instance. The shape configuration determines
    the resources thats are available to the container instance and its containers.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ContainerInstanceShapeConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ocpus:
            The value to assign to the ocpus property of this ContainerInstanceShapeConfig.
        :type ocpus: float

        :param memory_in_gbs:
            The value to assign to the memory_in_gbs property of this ContainerInstanceShapeConfig.
        :type memory_in_gbs: float

        :param processor_description:
            The value to assign to the processor_description property of this ContainerInstanceShapeConfig.
        :type processor_description: str

        :param networking_bandwidth_in_gbps:
            The value to assign to the networking_bandwidth_in_gbps property of this ContainerInstanceShapeConfig.
        :type networking_bandwidth_in_gbps: float

        """
        self.swagger_types = {
            'ocpus': 'float',
            'memory_in_gbs': 'float',
            'processor_description': 'str',
            'networking_bandwidth_in_gbps': 'float'
        }
        self.attribute_map = {
            'ocpus': 'ocpus',
            'memory_in_gbs': 'memoryInGBs',
            'processor_description': 'processorDescription',
            'networking_bandwidth_in_gbps': 'networkingBandwidthInGbps'
        }
        self._ocpus = None
        self._memory_in_gbs = None
        self._processor_description = None
        self._networking_bandwidth_in_gbps = None

    @property
    def ocpus(self):
        """
        **[Required]** Gets the ocpus of this ContainerInstanceShapeConfig.
        The total number of OCPUs available to the container instance.


        :return: The ocpus of this ContainerInstanceShapeConfig.
        :rtype: float
        """
        return self._ocpus

    @ocpus.setter
    def ocpus(self, ocpus):
        """
        Sets the ocpus of this ContainerInstanceShapeConfig.
        The total number of OCPUs available to the container instance.


        :param ocpus: The ocpus of this ContainerInstanceShapeConfig.
        :type: float
        """
        self._ocpus = ocpus

    @property
    def memory_in_gbs(self):
        """
        **[Required]** Gets the memory_in_gbs of this ContainerInstanceShapeConfig.
        The total amount of memory available to the container instance, in gigabytes.


        :return: The memory_in_gbs of this ContainerInstanceShapeConfig.
        :rtype: float
        """
        return self._memory_in_gbs

    @memory_in_gbs.setter
    def memory_in_gbs(self, memory_in_gbs):
        """
        Sets the memory_in_gbs of this ContainerInstanceShapeConfig.
        The total amount of memory available to the container instance, in gigabytes.


        :param memory_in_gbs: The memory_in_gbs of this ContainerInstanceShapeConfig.
        :type: float
        """
        self._memory_in_gbs = memory_in_gbs

    @property
    def processor_description(self):
        """
        **[Required]** Gets the processor_description of this ContainerInstanceShapeConfig.
        A short description of the container instance's processor (CPU).


        :return: The processor_description of this ContainerInstanceShapeConfig.
        :rtype: str
        """
        return self._processor_description

    @processor_description.setter
    def processor_description(self, processor_description):
        """
        Sets the processor_description of this ContainerInstanceShapeConfig.
        A short description of the container instance's processor (CPU).


        :param processor_description: The processor_description of this ContainerInstanceShapeConfig.
        :type: str
        """
        self._processor_description = processor_description

    @property
    def networking_bandwidth_in_gbps(self):
        """
        **[Required]** Gets the networking_bandwidth_in_gbps of this ContainerInstanceShapeConfig.
        The networking bandwidth available to the container instance, in gigabits per second.


        :return: The networking_bandwidth_in_gbps of this ContainerInstanceShapeConfig.
        :rtype: float
        """
        return self._networking_bandwidth_in_gbps

    @networking_bandwidth_in_gbps.setter
    def networking_bandwidth_in_gbps(self, networking_bandwidth_in_gbps):
        """
        Sets the networking_bandwidth_in_gbps of this ContainerInstanceShapeConfig.
        The networking bandwidth available to the container instance, in gigabits per second.


        :param networking_bandwidth_in_gbps: The networking_bandwidth_in_gbps of this ContainerInstanceShapeConfig.
        :type: float
        """
        self._networking_bandwidth_in_gbps = networking_bandwidth_in_gbps

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
