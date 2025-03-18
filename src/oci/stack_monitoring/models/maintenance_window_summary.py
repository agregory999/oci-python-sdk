# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MaintenanceWindowSummary(object):
    """
    General information of a Maintenance Window
    """

    #: A constant which can be used with the lifecycle_state property of a MaintenanceWindowSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a MaintenanceWindowSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a MaintenanceWindowSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MaintenanceWindowSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a MaintenanceWindowSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a MaintenanceWindowSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_details property of a MaintenanceWindowSummary.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_DETAILS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_details property of a MaintenanceWindowSummary.
    #: This constant has a value of "SCHEDULED"
    LIFECYCLE_DETAILS_SCHEDULED = "SCHEDULED"

    #: A constant which can be used with the lifecycle_details property of a MaintenanceWindowSummary.
    #: This constant has a value of "COMPLETED"
    LIFECYCLE_DETAILS_COMPLETED = "COMPLETED"

    #: A constant which can be used with the operation_type property of a MaintenanceWindowSummary.
    #: This constant has a value of "UPDATE"
    OPERATION_TYPE_UPDATE = "UPDATE"

    #: A constant which can be used with the operation_type property of a MaintenanceWindowSummary.
    #: This constant has a value of "CREATE"
    OPERATION_TYPE_CREATE = "CREATE"

    #: A constant which can be used with the operation_type property of a MaintenanceWindowSummary.
    #: This constant has a value of "DELETE"
    OPERATION_TYPE_DELETE = "DELETE"

    #: A constant which can be used with the operation_type property of a MaintenanceWindowSummary.
    #: This constant has a value of "STOP"
    OPERATION_TYPE_STOP = "STOP"

    #: A constant which can be used with the operation_status property of a MaintenanceWindowSummary.
    #: This constant has a value of "IN_PROGRESS"
    OPERATION_STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the operation_status property of a MaintenanceWindowSummary.
    #: This constant has a value of "FAILED"
    OPERATION_STATUS_FAILED = "FAILED"

    #: A constant which can be used with the operation_status property of a MaintenanceWindowSummary.
    #: This constant has a value of "SUCCEEDED"
    OPERATION_STATUS_SUCCEEDED = "SUCCEEDED"

    def __init__(self, **kwargs):
        """
        Initializes a new MaintenanceWindowSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MaintenanceWindowSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this MaintenanceWindowSummary.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MaintenanceWindowSummary.
        :type compartment_id: str

        :param number_of_resources:
            The value to assign to the number_of_resources property of this MaintenanceWindowSummary.
        :type number_of_resources: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MaintenanceWindowSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this MaintenanceWindowSummary.
            Allowed values for this property are: "IN_PROGRESS", "SCHEDULED", "COMPLETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_details: str

        :param operation_type:
            The value to assign to the operation_type property of this MaintenanceWindowSummary.
            Allowed values for this property are: "UPDATE", "CREATE", "DELETE", "STOP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param operation_status:
            The value to assign to the operation_status property of this MaintenanceWindowSummary.
            Allowed values for this property are: "IN_PROGRESS", "FAILED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_status: str

        :param schedule:
            The value to assign to the schedule property of this MaintenanceWindowSummary.
        :type schedule: oci.stack_monitoring.models.MaintenanceWindowSchedule

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MaintenanceWindowSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MaintenanceWindowSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this MaintenanceWindowSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'number_of_resources': 'int',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'operation_type': 'str',
            'operation_status': 'str',
            'schedule': 'MaintenanceWindowSchedule',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'number_of_resources': 'numberOfResources',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'operation_type': 'operationType',
            'operation_status': 'operationStatus',
            'schedule': 'schedule',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._name = None
        self._compartment_id = None
        self._number_of_resources = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._operation_type = None
        self._operation_status = None
        self._schedule = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MaintenanceWindowSummary.
        The `OCID`__ of maintenance window.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this MaintenanceWindowSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MaintenanceWindowSummary.
        The `OCID`__ of maintenance window.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this MaintenanceWindowSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this MaintenanceWindowSummary.
        Maintenance Window name.


        :return: The name of this MaintenanceWindowSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MaintenanceWindowSummary.
        Maintenance Window name.


        :param name: The name of this MaintenanceWindowSummary.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this MaintenanceWindowSummary.
        Compartment Identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this MaintenanceWindowSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MaintenanceWindowSummary.
        Compartment Identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this MaintenanceWindowSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def number_of_resources(self):
        """
        Gets the number_of_resources of this MaintenanceWindowSummary.
        Number of resources of the Maintenance window.


        :return: The number_of_resources of this MaintenanceWindowSummary.
        :rtype: int
        """
        return self._number_of_resources

    @number_of_resources.setter
    def number_of_resources(self, number_of_resources):
        """
        Sets the number_of_resources of this MaintenanceWindowSummary.
        Number of resources of the Maintenance window.


        :param number_of_resources: The number_of_resources of this MaintenanceWindowSummary.
        :type: int
        """
        self._number_of_resources = number_of_resources

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this MaintenanceWindowSummary.
        Lifecycle state of the monitored resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this MaintenanceWindowSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MaintenanceWindowSummary.
        Lifecycle state of the monitored resource.


        :param lifecycle_state: The lifecycle_state of this MaintenanceWindowSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this MaintenanceWindowSummary.
        Lifecycle Details of the Maintenance Window.

        Allowed values for this property are: "IN_PROGRESS", "SCHEDULED", "COMPLETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_details of this MaintenanceWindowSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this MaintenanceWindowSummary.
        Lifecycle Details of the Maintenance Window.


        :param lifecycle_details: The lifecycle_details of this MaintenanceWindowSummary.
        :type: str
        """
        allowed_values = ["IN_PROGRESS", "SCHEDULED", "COMPLETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_details, allowed_values):
            lifecycle_details = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_details = lifecycle_details

    @property
    def operation_type(self):
        """
        Gets the operation_type of this MaintenanceWindowSummary.
        The name of the most recent operation of the Maintenance window.

        Allowed values for this property are: "UPDATE", "CREATE", "DELETE", "STOP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this MaintenanceWindowSummary.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this MaintenanceWindowSummary.
        The name of the most recent operation of the Maintenance window.


        :param operation_type: The operation_type of this MaintenanceWindowSummary.
        :type: str
        """
        allowed_values = ["UPDATE", "CREATE", "DELETE", "STOP"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def operation_status(self):
        """
        Gets the operation_status of this MaintenanceWindowSummary.
        Status of the most recent operation of the Maintenance Window.

        Allowed values for this property are: "IN_PROGRESS", "FAILED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_status of this MaintenanceWindowSummary.
        :rtype: str
        """
        return self._operation_status

    @operation_status.setter
    def operation_status(self, operation_status):
        """
        Sets the operation_status of this MaintenanceWindowSummary.
        Status of the most recent operation of the Maintenance Window.


        :param operation_status: The operation_status of this MaintenanceWindowSummary.
        :type: str
        """
        allowed_values = ["IN_PROGRESS", "FAILED", "SUCCEEDED"]
        if not value_allowed_none_or_none_sentinel(operation_status, allowed_values):
            operation_status = 'UNKNOWN_ENUM_VALUE'
        self._operation_status = operation_status

    @property
    def schedule(self):
        """
        Gets the schedule of this MaintenanceWindowSummary.

        :return: The schedule of this MaintenanceWindowSummary.
        :rtype: oci.stack_monitoring.models.MaintenanceWindowSchedule
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """
        Sets the schedule of this MaintenanceWindowSummary.

        :param schedule: The schedule of this MaintenanceWindowSummary.
        :type: oci.stack_monitoring.models.MaintenanceWindowSchedule
        """
        self._schedule = schedule

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this MaintenanceWindowSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this MaintenanceWindowSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this MaintenanceWindowSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this MaintenanceWindowSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this MaintenanceWindowSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this MaintenanceWindowSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this MaintenanceWindowSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this MaintenanceWindowSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this MaintenanceWindowSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this MaintenanceWindowSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this MaintenanceWindowSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this MaintenanceWindowSummary.
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
