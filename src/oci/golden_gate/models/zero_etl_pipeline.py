# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407

from .pipeline import Pipeline
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ZeroEtlPipeline(Pipeline):
    """
    The details of a ZeroETL pipeline.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ZeroEtlPipeline object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.ZeroEtlPipeline.recipe_type` attribute
        of this class is ``ZERO_ETL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param recipe_type:
            The value to assign to the recipe_type property of this ZeroEtlPipeline.
            Allowed values for this property are: "ZERO_ETL"
        :type recipe_type: str

        :param id:
            The value to assign to the id property of this ZeroEtlPipeline.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ZeroEtlPipeline.
        :type display_name: str

        :param description:
            The value to assign to the description property of this ZeroEtlPipeline.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ZeroEtlPipeline.
        :type compartment_id: str

        :param license_model:
            The value to assign to the license_model property of this ZeroEtlPipeline.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this ZeroEtlPipeline.
        :type cpu_core_count: int

        :param is_auto_scaling_enabled:
            The value to assign to the is_auto_scaling_enabled property of this ZeroEtlPipeline.
        :type is_auto_scaling_enabled: bool

        :param source_connection_details:
            The value to assign to the source_connection_details property of this ZeroEtlPipeline.
        :type source_connection_details: oci.golden_gate.models.SourcePipelineConnectionDetails

        :param target_connection_details:
            The value to assign to the target_connection_details property of this ZeroEtlPipeline.
        :type target_connection_details: oci.golden_gate.models.TargetPipelineConnectionDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ZeroEtlPipeline.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ZeroEtlPipeline.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ZeroEtlPipeline.
        :type system_tags: dict(str, dict(str, object))

        :param locks:
            The value to assign to the locks property of this ZeroEtlPipeline.
        :type locks: list[oci.golden_gate.models.ResourceLock]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ZeroEtlPipeline.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "NEEDS_ATTENTION", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param lifecycle_sub_state:
            The value to assign to the lifecycle_sub_state property of this ZeroEtlPipeline.
            Allowed values for this property are: "STARTING", "STOPPING", "STOPPED", "MOVING", "RUNNING"
        :type lifecycle_sub_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ZeroEtlPipeline.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this ZeroEtlPipeline.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ZeroEtlPipeline.
        :type time_updated: datetime

        :param mapping_rules:
            The value to assign to the mapping_rules property of this ZeroEtlPipeline.
        :type mapping_rules: list[oci.golden_gate.models.MappingRule]

        :param process_options:
            The value to assign to the process_options property of this ZeroEtlPipeline.
        :type process_options: oci.golden_gate.models.ProcessOptions

        :param time_last_recorded:
            The value to assign to the time_last_recorded property of this ZeroEtlPipeline.
        :type time_last_recorded: datetime

        """
        self.swagger_types = {
            'recipe_type': 'str',
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'license_model': 'str',
            'cpu_core_count': 'int',
            'is_auto_scaling_enabled': 'bool',
            'source_connection_details': 'SourcePipelineConnectionDetails',
            'target_connection_details': 'TargetPipelineConnectionDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'locks': 'list[ResourceLock]',
            'lifecycle_state': 'str',
            'lifecycle_sub_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'mapping_rules': 'list[MappingRule]',
            'process_options': 'ProcessOptions',
            'time_last_recorded': 'datetime'
        }
        self.attribute_map = {
            'recipe_type': 'recipeType',
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'license_model': 'licenseModel',
            'cpu_core_count': 'cpuCoreCount',
            'is_auto_scaling_enabled': 'isAutoScalingEnabled',
            'source_connection_details': 'sourceConnectionDetails',
            'target_connection_details': 'targetConnectionDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'locks': 'locks',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_sub_state': 'lifecycleSubState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'mapping_rules': 'mappingRules',
            'process_options': 'processOptions',
            'time_last_recorded': 'timeLastRecorded'
        }
        self._recipe_type = None
        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._license_model = None
        self._cpu_core_count = None
        self._is_auto_scaling_enabled = None
        self._source_connection_details = None
        self._target_connection_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._locks = None
        self._lifecycle_state = None
        self._lifecycle_sub_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._mapping_rules = None
        self._process_options = None
        self._time_last_recorded = None
        self._recipe_type = 'ZERO_ETL'

    @property
    def mapping_rules(self):
        """
        Gets the mapping_rules of this ZeroEtlPipeline.
        Mapping for source/target schema/tables for the pipeline data replication.


        :return: The mapping_rules of this ZeroEtlPipeline.
        :rtype: list[oci.golden_gate.models.MappingRule]
        """
        return self._mapping_rules

    @mapping_rules.setter
    def mapping_rules(self, mapping_rules):
        """
        Sets the mapping_rules of this ZeroEtlPipeline.
        Mapping for source/target schema/tables for the pipeline data replication.


        :param mapping_rules: The mapping_rules of this ZeroEtlPipeline.
        :type: list[oci.golden_gate.models.MappingRule]
        """
        self._mapping_rules = mapping_rules

    @property
    def process_options(self):
        """
        Gets the process_options of this ZeroEtlPipeline.

        :return: The process_options of this ZeroEtlPipeline.
        :rtype: oci.golden_gate.models.ProcessOptions
        """
        return self._process_options

    @process_options.setter
    def process_options(self, process_options):
        """
        Sets the process_options of this ZeroEtlPipeline.

        :param process_options: The process_options of this ZeroEtlPipeline.
        :type: oci.golden_gate.models.ProcessOptions
        """
        self._process_options = process_options

    @property
    def time_last_recorded(self):
        """
        Gets the time_last_recorded of this ZeroEtlPipeline.
        When the resource was last updated. This option applies when retrieving a pipeline. The format is defined by
        `RFC3339`__, such as `2024-07-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_last_recorded of this ZeroEtlPipeline.
        :rtype: datetime
        """
        return self._time_last_recorded

    @time_last_recorded.setter
    def time_last_recorded(self, time_last_recorded):
        """
        Sets the time_last_recorded of this ZeroEtlPipeline.
        When the resource was last updated. This option applies when retrieving a pipeline. The format is defined by
        `RFC3339`__, such as `2024-07-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_last_recorded: The time_last_recorded of this ZeroEtlPipeline.
        :type: datetime
        """
        self._time_last_recorded = time_last_recorded

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
