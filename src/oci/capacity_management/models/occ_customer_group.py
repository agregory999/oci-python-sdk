# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231107


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OccCustomerGroup(object):
    """
    Details of the customer group resource.
    """

    #: A constant which can be used with the status property of a OccCustomerGroup.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a OccCustomerGroup.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    #: A constant which can be used with the lifecycle_state property of a OccCustomerGroup.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a OccCustomerGroup.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a OccCustomerGroup.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OccCustomerGroup.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a OccCustomerGroup.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a OccCustomerGroup.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new OccCustomerGroup object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OccCustomerGroup.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OccCustomerGroup.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this OccCustomerGroup.
        :type display_name: str

        :param description:
            The value to assign to the description property of this OccCustomerGroup.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this OccCustomerGroup.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OccCustomerGroup.
        :type time_updated: datetime

        :param status:
            The value to assign to the status property of this OccCustomerGroup.
            Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OccCustomerGroup.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this OccCustomerGroup.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OccCustomerGroup.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OccCustomerGroup.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this OccCustomerGroup.
        :type system_tags: dict(str, dict(str, object))

        :param customers_list:
            The value to assign to the customers_list property of this OccCustomerGroup.
        :type customers_list: list[oci.capacity_management.models.OccCustomer]

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'status': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'customers_list': 'list[OccCustomer]'
        }
        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'status': 'status',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'customers_list': 'customersList'
        }
        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._time_created = None
        self._time_updated = None
        self._status = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._customers_list = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OccCustomerGroup.
        The OCID of the customer group.


        :return: The id of this OccCustomerGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OccCustomerGroup.
        The OCID of the customer group.


        :param id: The id of this OccCustomerGroup.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this OccCustomerGroup.
        The OCID of the tenancy containing the customer group.


        :return: The compartment_id of this OccCustomerGroup.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OccCustomerGroup.
        The OCID of the tenancy containing the customer group.


        :param compartment_id: The compartment_id of this OccCustomerGroup.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this OccCustomerGroup.
        The display name of the customer group.


        :return: The display_name of this OccCustomerGroup.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this OccCustomerGroup.
        The display name of the customer group.


        :param display_name: The display_name of this OccCustomerGroup.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this OccCustomerGroup.
        The description about the customer group.


        :return: The description of this OccCustomerGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this OccCustomerGroup.
        The description about the customer group.


        :param description: The description of this OccCustomerGroup.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this OccCustomerGroup.
        The time when the customer group was created.


        :return: The time_created of this OccCustomerGroup.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OccCustomerGroup.
        The time when the customer group was created.


        :param time_created: The time_created of this OccCustomerGroup.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this OccCustomerGroup.
        The time when the customer group was last updated.


        :return: The time_updated of this OccCustomerGroup.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this OccCustomerGroup.
        The time when the customer group was last updated.


        :param time_updated: The time_updated of this OccCustomerGroup.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def status(self):
        """
        **[Required]** Gets the status of this OccCustomerGroup.
        To determine whether the customer group is enabled/disabled.

        Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this OccCustomerGroup.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this OccCustomerGroup.
        To determine whether the customer group is enabled/disabled.


        :param status: The status of this OccCustomerGroup.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this OccCustomerGroup.
        The current lifecycle state of the resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this OccCustomerGroup.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OccCustomerGroup.
        The current lifecycle state of the resource.


        :param lifecycle_state: The lifecycle_state of this OccCustomerGroup.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this OccCustomerGroup.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed State.


        :return: The lifecycle_details of this OccCustomerGroup.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this OccCustomerGroup.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed State.


        :param lifecycle_details: The lifecycle_details of this OccCustomerGroup.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this OccCustomerGroup.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this OccCustomerGroup.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OccCustomerGroup.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this OccCustomerGroup.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this OccCustomerGroup.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this OccCustomerGroup.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OccCustomerGroup.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this OccCustomerGroup.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this OccCustomerGroup.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this OccCustomerGroup.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this OccCustomerGroup.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this OccCustomerGroup.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def customers_list(self):
        """
        **[Required]** Gets the customers_list of this OccCustomerGroup.
        A list containing all the customers that belong to this customer group


        :return: The customers_list of this OccCustomerGroup.
        :rtype: list[oci.capacity_management.models.OccCustomer]
        """
        return self._customers_list

    @customers_list.setter
    def customers_list(self, customers_list):
        """
        Sets the customers_list of this OccCustomerGroup.
        A list containing all the customers that belong to this customer group


        :param customers_list: The customers_list of this OccCustomerGroup.
        :type: list[oci.capacity_management.models.OccCustomer]
        """
        self._customers_list = customers_list

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
