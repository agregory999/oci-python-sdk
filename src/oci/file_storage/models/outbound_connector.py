# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20171215


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OutboundConnector(object):
    """
    Outbound connectors are used to help File Storage communicate with an external server, such as an LDAP server.
    An outbound connector contains all the information needed to connect, authenticate, and gain authorization to perform the account's required functions.
    """

    #: A constant which can be used with the lifecycle_state property of a OutboundConnector.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a OutboundConnector.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OutboundConnector.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a OutboundConnector.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the connector_type property of a OutboundConnector.
    #: This constant has a value of "LDAPBIND"
    CONNECTOR_TYPE_LDAPBIND = "LDAPBIND"

    def __init__(self, **kwargs):
        """
        Initializes a new OutboundConnector object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.file_storage.models.LdapBindAccount`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this OutboundConnector.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OutboundConnector.
        :type compartment_id: str

        :param id:
            The value to assign to the id property of this OutboundConnector.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OutboundConnector.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param display_name:
            The value to assign to the display_name property of this OutboundConnector.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this OutboundConnector.
        :type time_created: datetime

        :param connector_type:
            The value to assign to the connector_type property of this OutboundConnector.
            Allowed values for this property are: "LDAPBIND", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type connector_type: str

        :param locks:
            The value to assign to the locks property of this OutboundConnector.
        :type locks: list[oci.file_storage.models.ResourceLock]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OutboundConnector.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OutboundConnector.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this OutboundConnector.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'connector_type': 'str',
            'locks': 'list[ResourceLock]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'connector_type': 'connectorType',
            'locks': 'locks',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._availability_domain = None
        self._compartment_id = None
        self._id = None
        self._lifecycle_state = None
        self._display_name = None
        self._time_created = None
        self._connector_type = None
        self._locks = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['connectorType']

        if type == 'LDAPBIND':
            return 'LdapBindAccount'
        else:
            return 'OutboundConnector'

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this OutboundConnector.
        The availability domain the outbound connector is in. May be unset
        as a blank or NULL value.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this OutboundConnector.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this OutboundConnector.
        The availability domain the outbound connector is in. May be unset
        as a blank or NULL value.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this OutboundConnector.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this OutboundConnector.
        The `OCID`__ of the compartment that contains the outbound connector.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this OutboundConnector.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OutboundConnector.
        The `OCID`__ of the compartment that contains the outbound connector.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this OutboundConnector.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OutboundConnector.
        The `OCID`__ of the outbound connector.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this OutboundConnector.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OutboundConnector.
        The `OCID`__ of the outbound connector.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this OutboundConnector.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this OutboundConnector.
        The current state of this outbound connector.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this OutboundConnector.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OutboundConnector.
        The current state of this outbound connector.


        :param lifecycle_state: The lifecycle_state of this OutboundConnector.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this OutboundConnector.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My outbound connector`


        :return: The display_name of this OutboundConnector.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this OutboundConnector.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My outbound connector`


        :param display_name: The display_name of this OutboundConnector.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this OutboundConnector.
        The date and time the outbound connector was created
        in `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this OutboundConnector.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OutboundConnector.
        The date and time the outbound connector was created
        in `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this OutboundConnector.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def connector_type(self):
        """
        **[Required]** Gets the connector_type of this OutboundConnector.
        The account type of this outbound connector.

        Allowed values for this property are: "LDAPBIND", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The connector_type of this OutboundConnector.
        :rtype: str
        """
        return self._connector_type

    @connector_type.setter
    def connector_type(self, connector_type):
        """
        Sets the connector_type of this OutboundConnector.
        The account type of this outbound connector.


        :param connector_type: The connector_type of this OutboundConnector.
        :type: str
        """
        allowed_values = ["LDAPBIND"]
        if not value_allowed_none_or_none_sentinel(connector_type, allowed_values):
            connector_type = 'UNKNOWN_ENUM_VALUE'
        self._connector_type = connector_type

    @property
    def locks(self):
        """
        Gets the locks of this OutboundConnector.
        Locks associated with this resource.


        :return: The locks of this OutboundConnector.
        :rtype: list[oci.file_storage.models.ResourceLock]
        """
        return self._locks

    @locks.setter
    def locks(self, locks):
        """
        Sets the locks of this OutboundConnector.
        Locks associated with this resource.


        :param locks: The locks of this OutboundConnector.
        :type: list[oci.file_storage.models.ResourceLock]
        """
        self._locks = locks

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this OutboundConnector.
        Free-form tags for this resource. Each tag is a simple key-value pair
         with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this OutboundConnector.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OutboundConnector.
        Free-form tags for this resource. Each tag is a simple key-value pair
         with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this OutboundConnector.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this OutboundConnector.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this OutboundConnector.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OutboundConnector.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this OutboundConnector.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this OutboundConnector.
        System tags for this resource.
        System tags are applied to resources by internal OCI services.


        :return: The system_tags of this OutboundConnector.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this OutboundConnector.
        System tags for this resource.
        System tags are applied to resources by internal OCI services.


        :param system_tags: The system_tags of this OutboundConnector.
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
