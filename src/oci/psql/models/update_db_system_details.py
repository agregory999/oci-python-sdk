# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220915


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDbSystemDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDbSystemDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateDbSystemDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateDbSystemDetails.
        :type description: str

        :param shape:
            The value to assign to the shape property of this UpdateDbSystemDetails.
        :type shape: str

        :param instance_ocpu_count:
            The value to assign to the instance_ocpu_count property of this UpdateDbSystemDetails.
        :type instance_ocpu_count: int

        :param instance_memory_size_in_gbs:
            The value to assign to the instance_memory_size_in_gbs property of this UpdateDbSystemDetails.
        :type instance_memory_size_in_gbs: int

        :param db_configuration_params:
            The value to assign to the db_configuration_params property of this UpdateDbSystemDetails.
        :type db_configuration_params: oci.psql.models.UpdateDbConfigParams

        :param management_policy:
            The value to assign to the management_policy property of this UpdateDbSystemDetails.
        :type management_policy: oci.psql.models.ManagementPolicyDetails

        :param storage_details:
            The value to assign to the storage_details property of this UpdateDbSystemDetails.
        :type storage_details: oci.psql.models.UpdateStorageDetailsParams

        :param network_details:
            The value to assign to the network_details property of this UpdateDbSystemDetails.
        :type network_details: oci.psql.models.UpdateNetworkDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDbSystemDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDbSystemDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'shape': 'str',
            'instance_ocpu_count': 'int',
            'instance_memory_size_in_gbs': 'int',
            'db_configuration_params': 'UpdateDbConfigParams',
            'management_policy': 'ManagementPolicyDetails',
            'storage_details': 'UpdateStorageDetailsParams',
            'network_details': 'UpdateNetworkDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'shape': 'shape',
            'instance_ocpu_count': 'instanceOcpuCount',
            'instance_memory_size_in_gbs': 'instanceMemorySizeInGBs',
            'db_configuration_params': 'dbConfigurationParams',
            'management_policy': 'managementPolicy',
            'storage_details': 'storageDetails',
            'network_details': 'networkDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._display_name = None
        self._description = None
        self._shape = None
        self._instance_ocpu_count = None
        self._instance_memory_size_in_gbs = None
        self._db_configuration_params = None
        self._management_policy = None
        self._storage_details = None
        self._network_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateDbSystemDetails.
        A user-friendly display name for the database system. Avoid entering confidential information.


        :return: The display_name of this UpdateDbSystemDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateDbSystemDetails.
        A user-friendly display name for the database system. Avoid entering confidential information.


        :param display_name: The display_name of this UpdateDbSystemDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateDbSystemDetails.
        A user-provided description of the database system.


        :return: The description of this UpdateDbSystemDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateDbSystemDetails.
        A user-provided description of the database system.


        :param description: The description of this UpdateDbSystemDetails.
        :type: str
        """
        self._description = description

    @property
    def shape(self):
        """
        Gets the shape of this UpdateDbSystemDetails.
        The name of the shape for the database system nodes.
        Example: `VM.Standard.E4.Flex`


        :return: The shape of this UpdateDbSystemDetails.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this UpdateDbSystemDetails.
        The name of the shape for the database system nodes.
        Example: `VM.Standard.E4.Flex`


        :param shape: The shape of this UpdateDbSystemDetails.
        :type: str
        """
        self._shape = shape

    @property
    def instance_ocpu_count(self):
        """
        Gets the instance_ocpu_count of this UpdateDbSystemDetails.
        The total number of OCPUs available to each database system node.


        :return: The instance_ocpu_count of this UpdateDbSystemDetails.
        :rtype: int
        """
        return self._instance_ocpu_count

    @instance_ocpu_count.setter
    def instance_ocpu_count(self, instance_ocpu_count):
        """
        Sets the instance_ocpu_count of this UpdateDbSystemDetails.
        The total number of OCPUs available to each database system node.


        :param instance_ocpu_count: The instance_ocpu_count of this UpdateDbSystemDetails.
        :type: int
        """
        self._instance_ocpu_count = instance_ocpu_count

    @property
    def instance_memory_size_in_gbs(self):
        """
        Gets the instance_memory_size_in_gbs of this UpdateDbSystemDetails.
        The total amount of memory available to each database system node, in gigabytes.


        :return: The instance_memory_size_in_gbs of this UpdateDbSystemDetails.
        :rtype: int
        """
        return self._instance_memory_size_in_gbs

    @instance_memory_size_in_gbs.setter
    def instance_memory_size_in_gbs(self, instance_memory_size_in_gbs):
        """
        Sets the instance_memory_size_in_gbs of this UpdateDbSystemDetails.
        The total amount of memory available to each database system node, in gigabytes.


        :param instance_memory_size_in_gbs: The instance_memory_size_in_gbs of this UpdateDbSystemDetails.
        :type: int
        """
        self._instance_memory_size_in_gbs = instance_memory_size_in_gbs

    @property
    def db_configuration_params(self):
        """
        Gets the db_configuration_params of this UpdateDbSystemDetails.

        :return: The db_configuration_params of this UpdateDbSystemDetails.
        :rtype: oci.psql.models.UpdateDbConfigParams
        """
        return self._db_configuration_params

    @db_configuration_params.setter
    def db_configuration_params(self, db_configuration_params):
        """
        Sets the db_configuration_params of this UpdateDbSystemDetails.

        :param db_configuration_params: The db_configuration_params of this UpdateDbSystemDetails.
        :type: oci.psql.models.UpdateDbConfigParams
        """
        self._db_configuration_params = db_configuration_params

    @property
    def management_policy(self):
        """
        Gets the management_policy of this UpdateDbSystemDetails.

        :return: The management_policy of this UpdateDbSystemDetails.
        :rtype: oci.psql.models.ManagementPolicyDetails
        """
        return self._management_policy

    @management_policy.setter
    def management_policy(self, management_policy):
        """
        Sets the management_policy of this UpdateDbSystemDetails.

        :param management_policy: The management_policy of this UpdateDbSystemDetails.
        :type: oci.psql.models.ManagementPolicyDetails
        """
        self._management_policy = management_policy

    @property
    def storage_details(self):
        """
        Gets the storage_details of this UpdateDbSystemDetails.

        :return: The storage_details of this UpdateDbSystemDetails.
        :rtype: oci.psql.models.UpdateStorageDetailsParams
        """
        return self._storage_details

    @storage_details.setter
    def storage_details(self, storage_details):
        """
        Sets the storage_details of this UpdateDbSystemDetails.

        :param storage_details: The storage_details of this UpdateDbSystemDetails.
        :type: oci.psql.models.UpdateStorageDetailsParams
        """
        self._storage_details = storage_details

    @property
    def network_details(self):
        """
        Gets the network_details of this UpdateDbSystemDetails.

        :return: The network_details of this UpdateDbSystemDetails.
        :rtype: oci.psql.models.UpdateNetworkDetails
        """
        return self._network_details

    @network_details.setter
    def network_details(self, network_details):
        """
        Sets the network_details of this UpdateDbSystemDetails.

        :param network_details: The network_details of this UpdateDbSystemDetails.
        :type: oci.psql.models.UpdateNetworkDetails
        """
        self._network_details = network_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateDbSystemDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateDbSystemDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateDbSystemDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateDbSystemDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateDbSystemDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateDbSystemDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateDbSystemDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateDbSystemDetails.
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
