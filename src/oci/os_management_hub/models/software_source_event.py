# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901

from .event import Event
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SoftwareSourceEvent(Event):
    """
    Provides information for a software source event.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SoftwareSourceEvent object with values from keyword arguments. The default value of the :py:attr:`~oci.os_management_hub.models.SoftwareSourceEvent.type` attribute
        of this class is ``SOFTWARE_SOURCE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SoftwareSourceEvent.
        :type id: str

        :param type:
            The value to assign to the type property of this SoftwareSourceEvent.
            Allowed values for this property are: "KERNEL_OOPS", "KERNEL_CRASH", "EXPLOIT_ATTEMPT", "SOFTWARE_UPDATE", "KSPLICE_UPDATE", "SOFTWARE_SOURCE", "AGENT", "MANAGEMENT_STATION", "SYSADMIN", "REBOOT"
        :type type: str

        :param event_summary:
            The value to assign to the event_summary property of this SoftwareSourceEvent.
        :type event_summary: str

        :param compartment_id:
            The value to assign to the compartment_id property of this SoftwareSourceEvent.
        :type compartment_id: str

        :param event_details:
            The value to assign to the event_details property of this SoftwareSourceEvent.
        :type event_details: str

        :param resource_id:
            The value to assign to the resource_id property of this SoftwareSourceEvent.
        :type resource_id: str

        :param system_details:
            The value to assign to the system_details property of this SoftwareSourceEvent.
        :type system_details: oci.os_management_hub.models.SystemDetails

        :param time_occurred:
            The value to assign to the time_occurred property of this SoftwareSourceEvent.
        :type time_occurred: datetime

        :param time_created:
            The value to assign to the time_created property of this SoftwareSourceEvent.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this SoftwareSourceEvent.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SoftwareSourceEvent.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this SoftwareSourceEvent.
        :type lifecycle_details: str

        :param is_managed_by_autonomous_linux:
            The value to assign to the is_managed_by_autonomous_linux property of this SoftwareSourceEvent.
        :type is_managed_by_autonomous_linux: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SoftwareSourceEvent.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SoftwareSourceEvent.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this SoftwareSourceEvent.
        :type system_tags: dict(str, dict(str, object))

        :param data:
            The value to assign to the data property of this SoftwareSourceEvent.
        :type data: oci.os_management_hub.models.SoftwareSourceEventData

        """
        self.swagger_types = {
            'id': 'str',
            'type': 'str',
            'event_summary': 'str',
            'compartment_id': 'str',
            'event_details': 'str',
            'resource_id': 'str',
            'system_details': 'SystemDetails',
            'time_occurred': 'datetime',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'is_managed_by_autonomous_linux': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'data': 'SoftwareSourceEventData'
        }
        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'event_summary': 'eventSummary',
            'compartment_id': 'compartmentId',
            'event_details': 'eventDetails',
            'resource_id': 'resourceId',
            'system_details': 'systemDetails',
            'time_occurred': 'timeOccurred',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'is_managed_by_autonomous_linux': 'isManagedByAutonomousLinux',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'data': 'data'
        }
        self._id = None
        self._type = None
        self._event_summary = None
        self._compartment_id = None
        self._event_details = None
        self._resource_id = None
        self._system_details = None
        self._time_occurred = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._is_managed_by_autonomous_linux = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._data = None
        self._type = 'SOFTWARE_SOURCE'

    @property
    def data(self):
        """
        **[Required]** Gets the data of this SoftwareSourceEvent.

        :return: The data of this SoftwareSourceEvent.
        :rtype: oci.os_management_hub.models.SoftwareSourceEventData
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this SoftwareSourceEvent.

        :param data: The data of this SoftwareSourceEvent.
        :type: oci.os_management_hub.models.SoftwareSourceEventData
        """
        self._data = data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
