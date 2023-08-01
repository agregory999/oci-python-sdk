# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528

from .create_fsu_action_details import CreateFsuActionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePrecheckActionDetails(CreateFsuActionDetails):
    """
    Precheck Exadata Fleet Update Action creation details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePrecheckActionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_software_update.models.CreatePrecheckActionDetails.type` attribute
        of this class is ``PRECHECK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreatePrecheckActionDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreatePrecheckActionDetails.
        :type compartment_id: str

        :param type:
            The value to assign to the type property of this CreatePrecheckActionDetails.
            Allowed values for this property are: "STAGE", "PRECHECK", "APPLY", "ROLLBACK_AND_REMOVE_TARGET", "CLEANUP"
        :type type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreatePrecheckActionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreatePrecheckActionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param fsu_cycle_id:
            The value to assign to the fsu_cycle_id property of this CreatePrecheckActionDetails.
        :type fsu_cycle_id: str

        :param schedule_details:
            The value to assign to the schedule_details property of this CreatePrecheckActionDetails.
        :type schedule_details: oci.fleet_software_update.models.CreateScheduleDetails

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'fsu_cycle_id': 'str',
            'schedule_details': 'CreateScheduleDetails'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'type': 'type',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'fsu_cycle_id': 'fsuCycleId',
            'schedule_details': 'scheduleDetails'
        }

        self._display_name = None
        self._compartment_id = None
        self._type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._fsu_cycle_id = None
        self._schedule_details = None
        self._type = 'PRECHECK'

    @property
    def fsu_cycle_id(self):
        """
        **[Required]** Gets the fsu_cycle_id of this CreatePrecheckActionDetails.
        OCID identifier for the Exadata Fleet Update Cycle the Action will be part of.


        :return: The fsu_cycle_id of this CreatePrecheckActionDetails.
        :rtype: str
        """
        return self._fsu_cycle_id

    @fsu_cycle_id.setter
    def fsu_cycle_id(self, fsu_cycle_id):
        """
        Sets the fsu_cycle_id of this CreatePrecheckActionDetails.
        OCID identifier for the Exadata Fleet Update Cycle the Action will be part of.


        :param fsu_cycle_id: The fsu_cycle_id of this CreatePrecheckActionDetails.
        :type: str
        """
        self._fsu_cycle_id = fsu_cycle_id

    @property
    def schedule_details(self):
        """
        Gets the schedule_details of this CreatePrecheckActionDetails.

        :return: The schedule_details of this CreatePrecheckActionDetails.
        :rtype: oci.fleet_software_update.models.CreateScheduleDetails
        """
        return self._schedule_details

    @schedule_details.setter
    def schedule_details(self, schedule_details):
        """
        Sets the schedule_details of this CreatePrecheckActionDetails.

        :param schedule_details: The schedule_details of this CreatePrecheckActionDetails.
        :type: oci.fleet_software_update.models.CreateScheduleDetails
        """
        self._schedule_details = schedule_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
