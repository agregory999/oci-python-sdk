# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528

from .fsu_cycle import FsuCycle
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PatchFsuCycle(FsuCycle):
    """
    Patch Exadata Fleet Update Cycle resource details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PatchFsuCycle object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_software_update.models.PatchFsuCycle.type` attribute
        of this class is ``PATCH`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this PatchFsuCycle.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this PatchFsuCycle.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this PatchFsuCycle.
        :type compartment_id: str

        :param type:
            The value to assign to the type property of this PatchFsuCycle.
            Allowed values for this property are: "PATCH"
        :type type: str

        :param fsu_collection_id:
            The value to assign to the fsu_collection_id property of this PatchFsuCycle.
        :type fsu_collection_id: str

        :param collection_type:
            The value to assign to the collection_type property of this PatchFsuCycle.
            Allowed values for this property are: "DB", "GI"
        :type collection_type: str

        :param executing_fsu_action_id:
            The value to assign to the executing_fsu_action_id property of this PatchFsuCycle.
        :type executing_fsu_action_id: str

        :param next_action_to_execute:
            The value to assign to the next_action_to_execute property of this PatchFsuCycle.
        :type next_action_to_execute: list[oci.fleet_software_update.models.NextActionToExecuteDetails]

        :param last_completed_action_id:
            The value to assign to the last_completed_action_id property of this PatchFsuCycle.
        :type last_completed_action_id: str

        :param rollback_cycle_state:
            The value to assign to the rollback_cycle_state property of this PatchFsuCycle.
            Allowed values for this property are: "ABLE_TO_EXECUTE", "IN_PROGRESS", "FAILED", "NEEDS_ATTENTION", "SUCCEEDED"
        :type rollback_cycle_state: str

        :param last_completed_action:
            The value to assign to the last_completed_action property of this PatchFsuCycle.
            Allowed values for this property are: "STAGE", "PRECHECK_STAGE", "PRECHECK_APPLY", "APPLY", "ROLLBACK_AND_REMOVE_TARGET", "CLEANUP", "ROLLBACK_MAINTENANCE_CYCLE"
        :type last_completed_action: str

        :param goal_version_details:
            The value to assign to the goal_version_details property of this PatchFsuCycle.
        :type goal_version_details: oci.fleet_software_update.models.FsuGoalVersionDetails

        :param batching_strategy:
            The value to assign to the batching_strategy property of this PatchFsuCycle.
        :type batching_strategy: oci.fleet_software_update.models.BatchingStrategyDetails

        :param stage_action_schedule:
            The value to assign to the stage_action_schedule property of this PatchFsuCycle.
        :type stage_action_schedule: oci.fleet_software_update.models.ScheduleDetails

        :param apply_action_schedule:
            The value to assign to the apply_action_schedule property of this PatchFsuCycle.
        :type apply_action_schedule: oci.fleet_software_update.models.ScheduleDetails

        :param diagnostics_collection:
            The value to assign to the diagnostics_collection property of this PatchFsuCycle.
        :type diagnostics_collection: oci.fleet_software_update.models.DiagnosticsCollectionDetails

        :param time_created:
            The value to assign to the time_created property of this PatchFsuCycle.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this PatchFsuCycle.
        :type time_updated: datetime

        :param time_finished:
            The value to assign to the time_finished property of this PatchFsuCycle.
        :type time_finished: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this PatchFsuCycle.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "IN_PROGRESS", "FAILED", "NEEDS_ATTENTION", "SUCCEEDED", "DELETING", "DELETED"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this PatchFsuCycle.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this PatchFsuCycle.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this PatchFsuCycle.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this PatchFsuCycle.
        :type system_tags: dict(str, dict(str, object))

        :param is_ignore_patches:
            The value to assign to the is_ignore_patches property of this PatchFsuCycle.
        :type is_ignore_patches: bool

        :param is_ignore_missing_patches:
            The value to assign to the is_ignore_missing_patches property of this PatchFsuCycle.
        :type is_ignore_missing_patches: list[str]

        :param max_drain_timeout_in_seconds:
            The value to assign to the max_drain_timeout_in_seconds property of this PatchFsuCycle.
        :type max_drain_timeout_in_seconds: int

        :param is_keep_placement:
            The value to assign to the is_keep_placement property of this PatchFsuCycle.
        :type is_keep_placement: bool

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'type': 'str',
            'fsu_collection_id': 'str',
            'collection_type': 'str',
            'executing_fsu_action_id': 'str',
            'next_action_to_execute': 'list[NextActionToExecuteDetails]',
            'last_completed_action_id': 'str',
            'rollback_cycle_state': 'str',
            'last_completed_action': 'str',
            'goal_version_details': 'FsuGoalVersionDetails',
            'batching_strategy': 'BatchingStrategyDetails',
            'stage_action_schedule': 'ScheduleDetails',
            'apply_action_schedule': 'ScheduleDetails',
            'diagnostics_collection': 'DiagnosticsCollectionDetails',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_finished': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'is_ignore_patches': 'bool',
            'is_ignore_missing_patches': 'list[str]',
            'max_drain_timeout_in_seconds': 'int',
            'is_keep_placement': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'type': 'type',
            'fsu_collection_id': 'fsuCollectionId',
            'collection_type': 'collectionType',
            'executing_fsu_action_id': 'executingFsuActionId',
            'next_action_to_execute': 'nextActionToExecute',
            'last_completed_action_id': 'lastCompletedActionId',
            'rollback_cycle_state': 'rollbackCycleState',
            'last_completed_action': 'lastCompletedAction',
            'goal_version_details': 'goalVersionDetails',
            'batching_strategy': 'batchingStrategy',
            'stage_action_schedule': 'stageActionSchedule',
            'apply_action_schedule': 'applyActionSchedule',
            'diagnostics_collection': 'diagnosticsCollection',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_finished': 'timeFinished',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'is_ignore_patches': 'isIgnorePatches',
            'is_ignore_missing_patches': 'isIgnoreMissingPatches',
            'max_drain_timeout_in_seconds': 'maxDrainTimeoutInSeconds',
            'is_keep_placement': 'isKeepPlacement'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._type = None
        self._fsu_collection_id = None
        self._collection_type = None
        self._executing_fsu_action_id = None
        self._next_action_to_execute = None
        self._last_completed_action_id = None
        self._rollback_cycle_state = None
        self._last_completed_action = None
        self._goal_version_details = None
        self._batching_strategy = None
        self._stage_action_schedule = None
        self._apply_action_schedule = None
        self._diagnostics_collection = None
        self._time_created = None
        self._time_updated = None
        self._time_finished = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._is_ignore_patches = None
        self._is_ignore_missing_patches = None
        self._max_drain_timeout_in_seconds = None
        self._is_keep_placement = None
        self._type = 'PATCH'

    @property
    def is_ignore_patches(self):
        """
        Gets the is_ignore_patches of this PatchFsuCycle.
        Ignore all patches between the source and target homes during patching.


        :return: The is_ignore_patches of this PatchFsuCycle.
        :rtype: bool
        """
        return self._is_ignore_patches

    @is_ignore_patches.setter
    def is_ignore_patches(self, is_ignore_patches):
        """
        Sets the is_ignore_patches of this PatchFsuCycle.
        Ignore all patches between the source and target homes during patching.


        :param is_ignore_patches: The is_ignore_patches of this PatchFsuCycle.
        :type: bool
        """
        self._is_ignore_patches = is_ignore_patches

    @property
    def is_ignore_missing_patches(self):
        """
        Gets the is_ignore_missing_patches of this PatchFsuCycle.
        List of bug numbers to ignore.


        :return: The is_ignore_missing_patches of this PatchFsuCycle.
        :rtype: list[str]
        """
        return self._is_ignore_missing_patches

    @is_ignore_missing_patches.setter
    def is_ignore_missing_patches(self, is_ignore_missing_patches):
        """
        Sets the is_ignore_missing_patches of this PatchFsuCycle.
        List of bug numbers to ignore.


        :param is_ignore_missing_patches: The is_ignore_missing_patches of this PatchFsuCycle.
        :type: list[str]
        """
        self._is_ignore_missing_patches = is_ignore_missing_patches

    @property
    def max_drain_timeout_in_seconds(self):
        """
        Gets the max_drain_timeout_in_seconds of this PatchFsuCycle.
        Service drain timeout specified in seconds.


        :return: The max_drain_timeout_in_seconds of this PatchFsuCycle.
        :rtype: int
        """
        return self._max_drain_timeout_in_seconds

    @max_drain_timeout_in_seconds.setter
    def max_drain_timeout_in_seconds(self, max_drain_timeout_in_seconds):
        """
        Sets the max_drain_timeout_in_seconds of this PatchFsuCycle.
        Service drain timeout specified in seconds.


        :param max_drain_timeout_in_seconds: The max_drain_timeout_in_seconds of this PatchFsuCycle.
        :type: int
        """
        self._max_drain_timeout_in_seconds = max_drain_timeout_in_seconds

    @property
    def is_keep_placement(self):
        """
        Gets the is_keep_placement of this PatchFsuCycle.
        Ensure that services of administrator-managed Oracle RAC or Oracle RAC One databases are running on the same
        instances before and after the move operation.


        :return: The is_keep_placement of this PatchFsuCycle.
        :rtype: bool
        """
        return self._is_keep_placement

    @is_keep_placement.setter
    def is_keep_placement(self, is_keep_placement):
        """
        Sets the is_keep_placement of this PatchFsuCycle.
        Ensure that services of administrator-managed Oracle RAC or Oracle RAC One databases are running on the same
        instances before and after the move operation.


        :param is_keep_placement: The is_keep_placement of this PatchFsuCycle.
        :type: bool
        """
        self._is_keep_placement = is_keep_placement

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
