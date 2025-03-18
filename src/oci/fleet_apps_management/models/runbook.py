# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Runbook(object):
    """
    Runbook definition.
    Runbooks allow you to capture procedural tasks for handling a workflow.
    """

    #: A constant which can be used with the type property of a Runbook.
    #: This constant has a value of "USER_DEFINED"
    TYPE_USER_DEFINED = "USER_DEFINED"

    #: A constant which can be used with the type property of a Runbook.
    #: This constant has a value of "ORACLE_DEFINED"
    TYPE_ORACLE_DEFINED = "ORACLE_DEFINED"

    #: A constant which can be used with the type property of a Runbook.
    #: This constant has a value of "SYSTEM_DEFINED"
    TYPE_SYSTEM_DEFINED = "SYSTEM_DEFINED"

    #: A constant which can be used with the runbook_relevance property of a Runbook.
    #: This constant has a value of "PRODUCT_GROUP"
    RUNBOOK_RELEVANCE_PRODUCT_GROUP = "PRODUCT_GROUP"

    #: A constant which can be used with the runbook_relevance property of a Runbook.
    #: This constant has a value of "PRODUCT"
    RUNBOOK_RELEVANCE_PRODUCT = "PRODUCT"

    #: A constant which can be used with the os_type property of a Runbook.
    #: This constant has a value of "WINDOWS"
    OS_TYPE_WINDOWS = "WINDOWS"

    #: A constant which can be used with the os_type property of a Runbook.
    #: This constant has a value of "LINUX"
    OS_TYPE_LINUX = "LINUX"

    #: A constant which can be used with the os_type property of a Runbook.
    #: This constant has a value of "GENERIC"
    OS_TYPE_GENERIC = "GENERIC"

    #: A constant which can be used with the lifecycle_state property of a Runbook.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Runbook.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Runbook.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a Runbook.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Runbook.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Runbook.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Runbook.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    def __init__(self, **kwargs):
        """
        Initializes a new Runbook object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Runbook.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this Runbook.
        :type display_name: str

        :param description:
            The value to assign to the description property of this Runbook.
        :type description: str

        :param type:
            The value to assign to the type property of this Runbook.
            Allowed values for this property are: "USER_DEFINED", "ORACLE_DEFINED", "SYSTEM_DEFINED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param runbook_relevance:
            The value to assign to the runbook_relevance property of this Runbook.
            Allowed values for this property are: "PRODUCT_GROUP", "PRODUCT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type runbook_relevance: str

        :param operation:
            The value to assign to the operation property of this Runbook.
        :type operation: str

        :param os_type:
            The value to assign to the os_type property of this Runbook.
            Allowed values for this property are: "WINDOWS", "LINUX", "GENERIC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type os_type: str

        :param platform:
            The value to assign to the platform property of this Runbook.
        :type platform: str

        :param is_default:
            The value to assign to the is_default property of this Runbook.
        :type is_default: bool

        :param estimated_time:
            The value to assign to the estimated_time property of this Runbook.
        :type estimated_time: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Runbook.
            Allowed values for this property are: "ACTIVE", "DELETED", "FAILED", "INACTIVE", "CREATING", "DELETING", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Runbook.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this Runbook.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Runbook.
        :type time_updated: datetime

        :param associations:
            The value to assign to the associations property of this Runbook.
        :type associations: oci.fleet_apps_management.models.Associations

        :param compartment_id:
            The value to assign to the compartment_id property of this Runbook.
        :type compartment_id: str

        :param resource_region:
            The value to assign to the resource_region property of this Runbook.
        :type resource_region: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Runbook.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Runbook.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Runbook.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'type': 'str',
            'runbook_relevance': 'str',
            'operation': 'str',
            'os_type': 'str',
            'platform': 'str',
            'is_default': 'bool',
            'estimated_time': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'associations': 'Associations',
            'compartment_id': 'str',
            'resource_region': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'type': 'type',
            'runbook_relevance': 'runbookRelevance',
            'operation': 'operation',
            'os_type': 'osType',
            'platform': 'platform',
            'is_default': 'isDefault',
            'estimated_time': 'estimatedTime',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'associations': 'associations',
            'compartment_id': 'compartmentId',
            'resource_region': 'resourceRegion',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._display_name = None
        self._description = None
        self._type = None
        self._runbook_relevance = None
        self._operation = None
        self._os_type = None
        self._platform = None
        self._is_default = None
        self._estimated_time = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._associations = None
        self._compartment_id = None
        self._resource_region = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Runbook.
        The OCID of the resource.


        :return: The id of this Runbook.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Runbook.
        The OCID of the resource.


        :param id: The id of this Runbook.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Runbook.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this Runbook.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Runbook.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this Runbook.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this Runbook.
        A user-friendly description. To provide some insight about the resource.
        Avoid entering confidential information.


        :return: The description of this Runbook.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Runbook.
        A user-friendly description. To provide some insight about the resource.
        Avoid entering confidential information.


        :param description: The description of this Runbook.
        :type: str
        """
        self._description = description

    @property
    def type(self):
        """
        **[Required]** Gets the type of this Runbook.
        The type of the runbook.

        Allowed values for this property are: "USER_DEFINED", "ORACLE_DEFINED", "SYSTEM_DEFINED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this Runbook.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Runbook.
        The type of the runbook.


        :param type: The type of this Runbook.
        :type: str
        """
        allowed_values = ["USER_DEFINED", "ORACLE_DEFINED", "SYSTEM_DEFINED"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def runbook_relevance(self):
        """
        **[Required]** Gets the runbook_relevance of this Runbook.
        Relevance of the runbook.

        Allowed values for this property are: "PRODUCT_GROUP", "PRODUCT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The runbook_relevance of this Runbook.
        :rtype: str
        """
        return self._runbook_relevance

    @runbook_relevance.setter
    def runbook_relevance(self, runbook_relevance):
        """
        Sets the runbook_relevance of this Runbook.
        Relevance of the runbook.


        :param runbook_relevance: The runbook_relevance of this Runbook.
        :type: str
        """
        allowed_values = ["PRODUCT_GROUP", "PRODUCT"]
        if not value_allowed_none_or_none_sentinel(runbook_relevance, allowed_values):
            runbook_relevance = 'UNKNOWN_ENUM_VALUE'
        self._runbook_relevance = runbook_relevance

    @property
    def operation(self):
        """
        **[Required]** Gets the operation of this Runbook.
        The lifecycle operation performed by the runbook.


        :return: The operation of this Runbook.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this Runbook.
        The lifecycle operation performed by the runbook.


        :param operation: The operation of this Runbook.
        :type: str
        """
        self._operation = operation

    @property
    def os_type(self):
        """
        **[Required]** Gets the os_type of this Runbook.
        The OS type for the runbook.

        Allowed values for this property are: "WINDOWS", "LINUX", "GENERIC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The os_type of this Runbook.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """
        Sets the os_type of this Runbook.
        The OS type for the runbook.


        :param os_type: The os_type of this Runbook.
        :type: str
        """
        allowed_values = ["WINDOWS", "LINUX", "GENERIC"]
        if not value_allowed_none_or_none_sentinel(os_type, allowed_values):
            os_type = 'UNKNOWN_ENUM_VALUE'
        self._os_type = os_type

    @property
    def platform(self):
        """
        **[Required]** Gets the platform of this Runbook.
        The platform of the runbook.


        :return: The platform of this Runbook.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """
        Sets the platform of this Runbook.
        The platform of the runbook.


        :param platform: The platform of this Runbook.
        :type: str
        """
        self._platform = platform

    @property
    def is_default(self):
        """
        **[Required]** Gets the is_default of this Runbook.
        Is the runbook default?
        Sets this runbook as the default for the chosen product/product stack for the specified lifecycle operation.


        :return: The is_default of this Runbook.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this Runbook.
        Is the runbook default?
        Sets this runbook as the default for the chosen product/product stack for the specified lifecycle operation.


        :param is_default: The is_default of this Runbook.
        :type: bool
        """
        self._is_default = is_default

    @property
    def estimated_time(self):
        """
        Gets the estimated_time of this Runbook.
        Estimated time to successfully complete the runbook execution.


        :return: The estimated_time of this Runbook.
        :rtype: str
        """
        return self._estimated_time

    @estimated_time.setter
    def estimated_time(self, estimated_time):
        """
        Sets the estimated_time of this Runbook.
        Estimated time to successfully complete the runbook execution.


        :param estimated_time: The estimated_time of this Runbook.
        :type: str
        """
        self._estimated_time = estimated_time

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Runbook.
        The current state of the Runbook.

        Allowed values for this property are: "ACTIVE", "DELETED", "FAILED", "INACTIVE", "CREATING", "DELETING", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Runbook.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Runbook.
        The current state of the Runbook.


        :param lifecycle_state: The lifecycle_state of this Runbook.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED", "FAILED", "INACTIVE", "CREATING", "DELETING", "UPDATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Runbook.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this Runbook.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Runbook.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this Runbook.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Runbook.
        The time this resource was created. An RFC3339 formatted datetime string.


        :return: The time_created of this Runbook.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Runbook.
        The time this resource was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this Runbook.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this Runbook.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this Runbook.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Runbook.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this Runbook.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def associations(self):
        """
        Gets the associations of this Runbook.

        :return: The associations of this Runbook.
        :rtype: oci.fleet_apps_management.models.Associations
        """
        return self._associations

    @associations.setter
    def associations(self, associations):
        """
        Sets the associations of this Runbook.

        :param associations: The associations of this Runbook.
        :type: oci.fleet_apps_management.models.Associations
        """
        self._associations = associations

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Runbook.
        OCID of the compartment to which the resource belongs to.


        :return: The compartment_id of this Runbook.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Runbook.
        OCID of the compartment to which the resource belongs to.


        :param compartment_id: The compartment_id of this Runbook.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def resource_region(self):
        """
        Gets the resource_region of this Runbook.
        Associated region


        :return: The resource_region of this Runbook.
        :rtype: str
        """
        return self._resource_region

    @resource_region.setter
    def resource_region(self, resource_region):
        """
        Sets the resource_region of this Runbook.
        Associated region


        :param resource_region: The resource_region of this Runbook.
        :type: str
        """
        self._resource_region = resource_region

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Runbook.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Runbook.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Runbook.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Runbook.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Runbook.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Runbook.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Runbook.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Runbook.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Runbook.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this Runbook.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Runbook.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this Runbook.
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
