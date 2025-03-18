# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220126


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AccessRequestSummary(object):
    """
    Summary information for an access request.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AccessRequestSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AccessRequestSummary.
        :type id: str

        :param lockbox_id:
            The value to assign to the lockbox_id property of this AccessRequestSummary.
        :type lockbox_id: str

        :param display_name:
            The value to assign to the display_name property of this AccessRequestSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this AccessRequestSummary.
        :type description: str

        :param requestor_id:
            The value to assign to the requestor_id property of this AccessRequestSummary.
        :type requestor_id: str

        :param requestor_location:
            The value to assign to the requestor_location property of this AccessRequestSummary.
        :type requestor_location: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AccessRequestSummary.
        :type lifecycle_state: str

        :param access_duration:
            The value to assign to the access_duration property of this AccessRequestSummary.
        :type access_duration: str

        :param time_created:
            The value to assign to the time_created property of this AccessRequestSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AccessRequestSummary.
        :type time_updated: datetime

        :param time_expired:
            The value to assign to the time_expired property of this AccessRequestSummary.
        :type time_expired: datetime

        :param ticket_number:
            The value to assign to the ticket_number property of this AccessRequestSummary.
        :type ticket_number: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AccessRequestSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AccessRequestSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this AccessRequestSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'lockbox_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'requestor_id': 'str',
            'requestor_location': 'str',
            'lifecycle_state': 'str',
            'access_duration': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_expired': 'datetime',
            'ticket_number': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'lockbox_id': 'lockboxId',
            'display_name': 'displayName',
            'description': 'description',
            'requestor_id': 'requestorId',
            'requestor_location': 'requestorLocation',
            'lifecycle_state': 'lifecycleState',
            'access_duration': 'accessDuration',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_expired': 'timeExpired',
            'ticket_number': 'ticketNumber',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._lockbox_id = None
        self._display_name = None
        self._description = None
        self._requestor_id = None
        self._requestor_location = None
        self._lifecycle_state = None
        self._access_duration = None
        self._time_created = None
        self._time_updated = None
        self._time_expired = None
        self._ticket_number = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AccessRequestSummary.
        The unique identifier (OCID) of the access request, which can't be changed after creation.


        :return: The id of this AccessRequestSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AccessRequestSummary.
        The unique identifier (OCID) of the access request, which can't be changed after creation.


        :param id: The id of this AccessRequestSummary.
        :type: str
        """
        self._id = id

    @property
    def lockbox_id(self):
        """
        **[Required]** Gets the lockbox_id of this AccessRequestSummary.
        The unique identifier (OCID) of the lockbox box that the access request is associated with, which can't be changed after creation.


        :return: The lockbox_id of this AccessRequestSummary.
        :rtype: str
        """
        return self._lockbox_id

    @lockbox_id.setter
    def lockbox_id(self, lockbox_id):
        """
        Sets the lockbox_id of this AccessRequestSummary.
        The unique identifier (OCID) of the lockbox box that the access request is associated with, which can't be changed after creation.


        :param lockbox_id: The lockbox_id of this AccessRequestSummary.
        :type: str
        """
        self._lockbox_id = lockbox_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AccessRequestSummary.
        The name of the access request.


        :return: The display_name of this AccessRequestSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AccessRequestSummary.
        The name of the access request.


        :param display_name: The display_name of this AccessRequestSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this AccessRequestSummary.
        The rationale for requesting the access request.


        :return: The description of this AccessRequestSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AccessRequestSummary.
        The rationale for requesting the access request.


        :param description: The description of this AccessRequestSummary.
        :type: str
        """
        self._description = description

    @property
    def requestor_id(self):
        """
        **[Required]** Gets the requestor_id of this AccessRequestSummary.
        The unique identifier of the requestor.


        :return: The requestor_id of this AccessRequestSummary.
        :rtype: str
        """
        return self._requestor_id

    @requestor_id.setter
    def requestor_id(self, requestor_id):
        """
        Sets the requestor_id of this AccessRequestSummary.
        The unique identifier of the requestor.


        :param requestor_id: The requestor_id of this AccessRequestSummary.
        :type: str
        """
        self._requestor_id = requestor_id

    @property
    def requestor_location(self):
        """
        Gets the requestor_location of this AccessRequestSummary.
        The two-char country code of the requestor while creating the access request
        Example: `US`


        :return: The requestor_location of this AccessRequestSummary.
        :rtype: str
        """
        return self._requestor_location

    @requestor_location.setter
    def requestor_location(self, requestor_location):
        """
        Sets the requestor_location of this AccessRequestSummary.
        The two-char country code of the requestor while creating the access request
        Example: `US`


        :param requestor_location: The requestor_location of this AccessRequestSummary.
        :type: str
        """
        self._requestor_location = requestor_location

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AccessRequestSummary.
        The current state of the access request.


        :return: The lifecycle_state of this AccessRequestSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AccessRequestSummary.
        The current state of the access request.


        :param lifecycle_state: The lifecycle_state of this AccessRequestSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def access_duration(self):
        """
        Gets the access_duration of this AccessRequestSummary.
        The maximum amount of time operator has access to associated resources.


        :return: The access_duration of this AccessRequestSummary.
        :rtype: str
        """
        return self._access_duration

    @access_duration.setter
    def access_duration(self, access_duration):
        """
        Sets the access_duration of this AccessRequestSummary.
        The maximum amount of time operator has access to associated resources.


        :param access_duration: The access_duration of this AccessRequestSummary.
        :type: str
        """
        self._access_duration = access_duration

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this AccessRequestSummary.
        The time the access request was created. Format is defined by `RFC3339`__.
        Example: `2020-01-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this AccessRequestSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AccessRequestSummary.
        The time the access request was created. Format is defined by `RFC3339`__.
        Example: `2020-01-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this AccessRequestSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this AccessRequestSummary.
        The time the access request was last updated. Format is defined by `RFC3339`__.
        Example: `2020-01-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this AccessRequestSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AccessRequestSummary.
        The time the access request was last updated. Format is defined by `RFC3339`__.
        Example: `2020-01-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this AccessRequestSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_expired(self):
        """
        **[Required]** Gets the time_expired of this AccessRequestSummary.
        The time the access request expired. Format is defined by `RFC3339`__.
        Example: `2020-01-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_expired of this AccessRequestSummary.
        :rtype: datetime
        """
        return self._time_expired

    @time_expired.setter
    def time_expired(self, time_expired):
        """
        Sets the time_expired of this AccessRequestSummary.
        The time the access request expired. Format is defined by `RFC3339`__.
        Example: `2020-01-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_expired: The time_expired of this AccessRequestSummary.
        :type: datetime
        """
        self._time_expired = time_expired

    @property
    def ticket_number(self):
        """
        Gets the ticket_number of this AccessRequestSummary.
        The ticket number raised by external customers
        Example: `3-37509643121`


        :return: The ticket_number of this AccessRequestSummary.
        :rtype: str
        """
        return self._ticket_number

    @ticket_number.setter
    def ticket_number(self, ticket_number):
        """
        Sets the ticket_number of this AccessRequestSummary.
        The ticket number raised by external customers
        Example: `3-37509643121`


        :param ticket_number: The ticket_number of this AccessRequestSummary.
        :type: str
        """
        self._ticket_number = ticket_number

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AccessRequestSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this AccessRequestSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AccessRequestSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this AccessRequestSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AccessRequestSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this AccessRequestSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AccessRequestSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this AccessRequestSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this AccessRequestSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this AccessRequestSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this AccessRequestSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this AccessRequestSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
