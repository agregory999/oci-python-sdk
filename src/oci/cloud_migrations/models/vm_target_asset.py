# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .target_asset import TargetAsset
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VmTargetAsset(TargetAsset):
    """
    Description of the VM target asset.
    """

    #: A constant which can be used with the preferred_shape_type property of a VmTargetAsset.
    #: This constant has a value of "VM"
    PREFERRED_SHAPE_TYPE_VM = "VM"

    #: A constant which can be used with the preferred_shape_type property of a VmTargetAsset.
    #: This constant has a value of "VM_INTEL"
    PREFERRED_SHAPE_TYPE_VM_INTEL = "VM_INTEL"

    #: A constant which can be used with the preferred_shape_type property of a VmTargetAsset.
    #: This constant has a value of "VM_INTEL_Standard"
    PREFERRED_SHAPE_TYPE_VM_INTEL_STANDARD = "VM_INTEL_Standard"

    #: A constant which can be used with the preferred_shape_type property of a VmTargetAsset.
    #: This constant has a value of "VM_INTEL_DensIO"
    PREFERRED_SHAPE_TYPE_VM_INTEL_DENS_IO = "VM_INTEL_DensIO"

    #: A constant which can be used with the preferred_shape_type property of a VmTargetAsset.
    #: This constant has a value of "VM_INTEL_GPU"
    PREFERRED_SHAPE_TYPE_VM_INTEL_GPU = "VM_INTEL_GPU"

    #: A constant which can be used with the preferred_shape_type property of a VmTargetAsset.
    #: This constant has a value of "VM_INTEL_Optimized"
    PREFERRED_SHAPE_TYPE_VM_INTEL_OPTIMIZED = "VM_INTEL_Optimized"

    #: A constant which can be used with the preferred_shape_type property of a VmTargetAsset.
    #: This constant has a value of "VM_AMD"
    PREFERRED_SHAPE_TYPE_VM_AMD = "VM_AMD"

    #: A constant which can be used with the preferred_shape_type property of a VmTargetAsset.
    #: This constant has a value of "VM_AMD_Standard"
    PREFERRED_SHAPE_TYPE_VM_AMD_STANDARD = "VM_AMD_Standard"

    def __init__(self, **kwargs):
        """
        Initializes a new VmTargetAsset object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_migrations.models.VmTargetAsset.type` attribute
        of this class is ``INSTANCE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this VmTargetAsset.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this VmTargetAsset.
        :type display_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this VmTargetAsset.
            Allowed values for this property are: "CREATING", "UPDATING", "NEEDS_ATTENTION", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this VmTargetAsset.
        :type lifecycle_details: str

        :param migration_plan_id:
            The value to assign to the migration_plan_id property of this VmTargetAsset.
        :type migration_plan_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this VmTargetAsset.
        :type compartment_id: str

        :param created_resource_id:
            The value to assign to the created_resource_id property of this VmTargetAsset.
        :type created_resource_id: str

        :param type:
            The value to assign to the type property of this VmTargetAsset.
            Allowed values for this property are: "INSTANCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param is_excluded_from_execution:
            The value to assign to the is_excluded_from_execution property of this VmTargetAsset.
        :type is_excluded_from_execution: bool

        :param compatibility_messages:
            The value to assign to the compatibility_messages property of this VmTargetAsset.
        :type compatibility_messages: list[oci.cloud_migrations.models.CompatibilityMessage]

        :param estimated_cost:
            The value to assign to the estimated_cost property of this VmTargetAsset.
        :type estimated_cost: oci.cloud_migrations.models.CostEstimation

        :param time_created:
            The value to assign to the time_created property of this VmTargetAsset.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this VmTargetAsset.
        :type time_updated: datetime

        :param time_assessed:
            The value to assign to the time_assessed property of this VmTargetAsset.
        :type time_assessed: datetime

        :param migration_asset:
            The value to assign to the migration_asset property of this VmTargetAsset.
        :type migration_asset: oci.cloud_migrations.models.MigrationAsset

        :param preferred_shape_type:
            The value to assign to the preferred_shape_type property of this VmTargetAsset.
            Allowed values for this property are: "VM", "VM_INTEL", "VM_INTEL_Standard", "VM_INTEL_DensIO", "VM_INTEL_GPU", "VM_INTEL_Optimized", "VM_AMD", "VM_AMD_Standard", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type preferred_shape_type: str

        :param test_spec:
            The value to assign to the test_spec property of this VmTargetAsset.
        :type test_spec: oci.cloud_migrations.models.LaunchInstanceDetails

        :param block_volumes_performance:
            The value to assign to the block_volumes_performance property of this VmTargetAsset.
        :type block_volumes_performance: int

        :param ms_license:
            The value to assign to the ms_license property of this VmTargetAsset.
        :type ms_license: str

        :param user_spec:
            The value to assign to the user_spec property of this VmTargetAsset.
        :type user_spec: oci.cloud_migrations.models.LaunchInstanceDetails

        :param recommended_spec:
            The value to assign to the recommended_spec property of this VmTargetAsset.
        :type recommended_spec: oci.cloud_migrations.models.LaunchInstanceDetails

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'migration_plan_id': 'str',
            'compartment_id': 'str',
            'created_resource_id': 'str',
            'type': 'str',
            'is_excluded_from_execution': 'bool',
            'compatibility_messages': 'list[CompatibilityMessage]',
            'estimated_cost': 'CostEstimation',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_assessed': 'datetime',
            'migration_asset': 'MigrationAsset',
            'preferred_shape_type': 'str',
            'test_spec': 'LaunchInstanceDetails',
            'block_volumes_performance': 'int',
            'ms_license': 'str',
            'user_spec': 'LaunchInstanceDetails',
            'recommended_spec': 'LaunchInstanceDetails'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'migration_plan_id': 'migrationPlanId',
            'compartment_id': 'compartmentId',
            'created_resource_id': 'createdResourceId',
            'type': 'type',
            'is_excluded_from_execution': 'isExcludedFromExecution',
            'compatibility_messages': 'compatibilityMessages',
            'estimated_cost': 'estimatedCost',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_assessed': 'timeAssessed',
            'migration_asset': 'migrationAsset',
            'preferred_shape_type': 'preferredShapeType',
            'test_spec': 'testSpec',
            'block_volumes_performance': 'blockVolumesPerformance',
            'ms_license': 'msLicense',
            'user_spec': 'userSpec',
            'recommended_spec': 'recommendedSpec'
        }

        self._id = None
        self._display_name = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._migration_plan_id = None
        self._compartment_id = None
        self._created_resource_id = None
        self._type = None
        self._is_excluded_from_execution = None
        self._compatibility_messages = None
        self._estimated_cost = None
        self._time_created = None
        self._time_updated = None
        self._time_assessed = None
        self._migration_asset = None
        self._preferred_shape_type = None
        self._test_spec = None
        self._block_volumes_performance = None
        self._ms_license = None
        self._user_spec = None
        self._recommended_spec = None
        self._type = 'INSTANCE'

    @property
    def preferred_shape_type(self):
        """
        **[Required]** Gets the preferred_shape_type of this VmTargetAsset.
        Preferred VM shape type that you provide.

        Allowed values for this property are: "VM", "VM_INTEL", "VM_INTEL_Standard", "VM_INTEL_DensIO", "VM_INTEL_GPU", "VM_INTEL_Optimized", "VM_AMD", "VM_AMD_Standard", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The preferred_shape_type of this VmTargetAsset.
        :rtype: str
        """
        return self._preferred_shape_type

    @preferred_shape_type.setter
    def preferred_shape_type(self, preferred_shape_type):
        """
        Sets the preferred_shape_type of this VmTargetAsset.
        Preferred VM shape type that you provide.


        :param preferred_shape_type: The preferred_shape_type of this VmTargetAsset.
        :type: str
        """
        allowed_values = ["VM", "VM_INTEL", "VM_INTEL_Standard", "VM_INTEL_DensIO", "VM_INTEL_GPU", "VM_INTEL_Optimized", "VM_AMD", "VM_AMD_Standard"]
        if not value_allowed_none_or_none_sentinel(preferred_shape_type, allowed_values):
            preferred_shape_type = 'UNKNOWN_ENUM_VALUE'
        self._preferred_shape_type = preferred_shape_type

    @property
    def test_spec(self):
        """
        Gets the test_spec of this VmTargetAsset.

        :return: The test_spec of this VmTargetAsset.
        :rtype: oci.cloud_migrations.models.LaunchInstanceDetails
        """
        return self._test_spec

    @test_spec.setter
    def test_spec(self, test_spec):
        """
        Sets the test_spec of this VmTargetAsset.

        :param test_spec: The test_spec of this VmTargetAsset.
        :type: oci.cloud_migrations.models.LaunchInstanceDetails
        """
        self._test_spec = test_spec

    @property
    def block_volumes_performance(self):
        """
        Gets the block_volumes_performance of this VmTargetAsset.
        Performance of the block volumes.


        :return: The block_volumes_performance of this VmTargetAsset.
        :rtype: int
        """
        return self._block_volumes_performance

    @block_volumes_performance.setter
    def block_volumes_performance(self, block_volumes_performance):
        """
        Sets the block_volumes_performance of this VmTargetAsset.
        Performance of the block volumes.


        :param block_volumes_performance: The block_volumes_performance of this VmTargetAsset.
        :type: int
        """
        self._block_volumes_performance = block_volumes_performance

    @property
    def ms_license(self):
        """
        Gets the ms_license of this VmTargetAsset.
        Microsoft license for VM configuration.


        :return: The ms_license of this VmTargetAsset.
        :rtype: str
        """
        return self._ms_license

    @ms_license.setter
    def ms_license(self, ms_license):
        """
        Sets the ms_license of this VmTargetAsset.
        Microsoft license for VM configuration.


        :param ms_license: The ms_license of this VmTargetAsset.
        :type: str
        """
        self._ms_license = ms_license

    @property
    def user_spec(self):
        """
        Gets the user_spec of this VmTargetAsset.

        :return: The user_spec of this VmTargetAsset.
        :rtype: oci.cloud_migrations.models.LaunchInstanceDetails
        """
        return self._user_spec

    @user_spec.setter
    def user_spec(self, user_spec):
        """
        Sets the user_spec of this VmTargetAsset.

        :param user_spec: The user_spec of this VmTargetAsset.
        :type: oci.cloud_migrations.models.LaunchInstanceDetails
        """
        self._user_spec = user_spec

    @property
    def recommended_spec(self):
        """
        Gets the recommended_spec of this VmTargetAsset.

        :return: The recommended_spec of this VmTargetAsset.
        :rtype: oci.cloud_migrations.models.LaunchInstanceDetails
        """
        return self._recommended_spec

    @recommended_spec.setter
    def recommended_spec(self, recommended_spec):
        """
        Sets the recommended_spec of this VmTargetAsset.

        :param recommended_spec: The recommended_spec of this VmTargetAsset.
        :type: oci.cloud_migrations.models.LaunchInstanceDetails
        """
        self._recommended_spec = recommended_spec

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other