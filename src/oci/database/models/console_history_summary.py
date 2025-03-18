# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConsoleHistorySummary(object):
    """
    The details of the Db Node console history.
    """

    #: A constant which can be used with the lifecycle_state property of a ConsoleHistorySummary.
    #: This constant has a value of "REQUESTED"
    LIFECYCLE_STATE_REQUESTED = "REQUESTED"

    #: A constant which can be used with the lifecycle_state property of a ConsoleHistorySummary.
    #: This constant has a value of "GETTING_HISTORY"
    LIFECYCLE_STATE_GETTING_HISTORY = "GETTING_HISTORY"

    #: A constant which can be used with the lifecycle_state property of a ConsoleHistorySummary.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a ConsoleHistorySummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a ConsoleHistorySummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ConsoleHistorySummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    def __init__(self, **kwargs):
        """
        Initializes a new ConsoleHistorySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ConsoleHistorySummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ConsoleHistorySummary.
        :type compartment_id: str

        :param db_node_id:
            The value to assign to the db_node_id property of this ConsoleHistorySummary.
        :type db_node_id: str

        :param display_name:
            The value to assign to the display_name property of this ConsoleHistorySummary.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ConsoleHistorySummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ConsoleHistorySummary.
        :type defined_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ConsoleHistorySummary.
            Allowed values for this property are: "REQUESTED", "GETTING_HISTORY", "SUCCEEDED", "FAILED", "DELETED", "DELETING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ConsoleHistorySummary.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this ConsoleHistorySummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'db_node_id': 'str',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime'
        }
        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'db_node_id': 'dbNodeId',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated'
        }
        self._id = None
        self._compartment_id = None
        self._db_node_id = None
        self._display_name = None
        self._freeform_tags = None
        self._defined_tags = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ConsoleHistorySummary.
        The OCID of the console history.


        :return: The id of this ConsoleHistorySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConsoleHistorySummary.
        The OCID of the console history.


        :param id: The id of this ConsoleHistorySummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ConsoleHistorySummary.
        The OCID of the compartment containing the console history.


        :return: The compartment_id of this ConsoleHistorySummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ConsoleHistorySummary.
        The OCID of the compartment containing the console history.


        :param compartment_id: The compartment_id of this ConsoleHistorySummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def db_node_id(self):
        """
        **[Required]** Gets the db_node_id of this ConsoleHistorySummary.
        The OCID of the database node.


        :return: The db_node_id of this ConsoleHistorySummary.
        :rtype: str
        """
        return self._db_node_id

    @db_node_id.setter
    def db_node_id(self, db_node_id):
        """
        Sets the db_node_id of this ConsoleHistorySummary.
        The OCID of the database node.


        :param db_node_id: The db_node_id of this ConsoleHistorySummary.
        :type: str
        """
        self._db_node_id = db_node_id

    @property
    def display_name(self):
        """
        Gets the display_name of this ConsoleHistorySummary.
        The user-friendly name for the console history. The name does not need to be unique.


        :return: The display_name of this ConsoleHistorySummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ConsoleHistorySummary.
        The user-friendly name for the console history. The name does not need to be unique.


        :param display_name: The display_name of this ConsoleHistorySummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ConsoleHistorySummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ConsoleHistorySummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ConsoleHistorySummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ConsoleHistorySummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ConsoleHistorySummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ConsoleHistorySummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ConsoleHistorySummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ConsoleHistorySummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ConsoleHistorySummary.
        The current state of the console history.

        Allowed values for this property are: "REQUESTED", "GETTING_HISTORY", "SUCCEEDED", "FAILED", "DELETED", "DELETING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ConsoleHistorySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ConsoleHistorySummary.
        The current state of the console history.


        :param lifecycle_state: The lifecycle_state of this ConsoleHistorySummary.
        :type: str
        """
        allowed_values = ["REQUESTED", "GETTING_HISTORY", "SUCCEEDED", "FAILED", "DELETED", "DELETING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ConsoleHistorySummary.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this ConsoleHistorySummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ConsoleHistorySummary.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this ConsoleHistorySummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ConsoleHistorySummary.
        The date and time the console history was created.


        :return: The time_created of this ConsoleHistorySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ConsoleHistorySummary.
        The date and time the console history was created.


        :param time_created: The time_created of this ConsoleHistorySummary.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
