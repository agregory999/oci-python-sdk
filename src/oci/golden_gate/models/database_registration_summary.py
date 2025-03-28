# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseRegistrationSummary(object):
    """
    Summary of the DatabaseRegistration.
    """

    #: A constant which can be used with the lifecycle_state property of a DatabaseRegistrationSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DatabaseRegistrationSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DatabaseRegistrationSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DatabaseRegistrationSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DatabaseRegistrationSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DatabaseRegistrationSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DatabaseRegistrationSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a DatabaseRegistrationSummary.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a DatabaseRegistrationSummary.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a DatabaseRegistrationSummary.
    #: This constant has a value of "CANCELING"
    LIFECYCLE_STATE_CANCELING = "CANCELING"

    #: A constant which can be used with the lifecycle_state property of a DatabaseRegistrationSummary.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    #: A constant which can be used with the lifecycle_state property of a DatabaseRegistrationSummary.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a DatabaseRegistrationSummary.
    #: This constant has a value of "WAITING"
    LIFECYCLE_STATE_WAITING = "WAITING"

    #: A constant which can be used with the session_mode property of a DatabaseRegistrationSummary.
    #: This constant has a value of "DIRECT"
    SESSION_MODE_DIRECT = "DIRECT"

    #: A constant which can be used with the session_mode property of a DatabaseRegistrationSummary.
    #: This constant has a value of "REDIRECT"
    SESSION_MODE_REDIRECT = "REDIRECT"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseRegistrationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DatabaseRegistrationSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this DatabaseRegistrationSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this DatabaseRegistrationSummary.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DatabaseRegistrationSummary.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this DatabaseRegistrationSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DatabaseRegistrationSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DatabaseRegistrationSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", "IN_PROGRESS", "CANCELING", "CANCELED", "SUCCEEDED", "WAITING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DatabaseRegistrationSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DatabaseRegistrationSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DatabaseRegistrationSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param fqdn:
            The value to assign to the fqdn property of this DatabaseRegistrationSummary.
        :type fqdn: str

        :param subnet_id:
            The value to assign to the subnet_id property of this DatabaseRegistrationSummary.
        :type subnet_id: str

        :param system_tags:
            The value to assign to the system_tags property of this DatabaseRegistrationSummary.
        :type system_tags: dict(str, dict(str, object))

        :param database_id:
            The value to assign to the database_id property of this DatabaseRegistrationSummary.
        :type database_id: str

        :param username:
            The value to assign to the username property of this DatabaseRegistrationSummary.
        :type username: str

        :param connection_string:
            The value to assign to the connection_string property of this DatabaseRegistrationSummary.
        :type connection_string: str

        :param session_mode:
            The value to assign to the session_mode property of this DatabaseRegistrationSummary.
            Allowed values for this property are: "DIRECT", "REDIRECT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type session_mode: str

        :param alias_name:
            The value to assign to the alias_name property of this DatabaseRegistrationSummary.
        :type alias_name: str

        :param secret_id:
            The value to assign to the secret_id property of this DatabaseRegistrationSummary.
        :type secret_id: str

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'fqdn': 'str',
            'subnet_id': 'str',
            'system_tags': 'dict(str, dict(str, object))',
            'database_id': 'str',
            'username': 'str',
            'connection_string': 'str',
            'session_mode': 'str',
            'alias_name': 'str',
            'secret_id': 'str'
        }
        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'fqdn': 'fqdn',
            'subnet_id': 'subnetId',
            'system_tags': 'systemTags',
            'database_id': 'databaseId',
            'username': 'username',
            'connection_string': 'connectionString',
            'session_mode': 'sessionMode',
            'alias_name': 'aliasName',
            'secret_id': 'secretId'
        }
        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._fqdn = None
        self._subnet_id = None
        self._system_tags = None
        self._database_id = None
        self._username = None
        self._connection_string = None
        self._session_mode = None
        self._alias_name = None
        self._secret_id = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DatabaseRegistrationSummary.
        The `OCID`__ of the databaseRegistration being
        referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this DatabaseRegistrationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DatabaseRegistrationSummary.
        The `OCID`__ of the databaseRegistration being
        referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this DatabaseRegistrationSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DatabaseRegistrationSummary.
        An object's Display Name.


        :return: The display_name of this DatabaseRegistrationSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DatabaseRegistrationSummary.
        An object's Display Name.


        :param display_name: The display_name of this DatabaseRegistrationSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this DatabaseRegistrationSummary.
        Metadata about this specific object.


        :return: The description of this DatabaseRegistrationSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DatabaseRegistrationSummary.
        Metadata about this specific object.


        :param description: The description of this DatabaseRegistrationSummary.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DatabaseRegistrationSummary.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this DatabaseRegistrationSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DatabaseRegistrationSummary.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this DatabaseRegistrationSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        Gets the time_created of this DatabaseRegistrationSummary.
        The time the resource was created. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this DatabaseRegistrationSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DatabaseRegistrationSummary.
        The time the resource was created. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this DatabaseRegistrationSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this DatabaseRegistrationSummary.
        The time the resource was last updated. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this DatabaseRegistrationSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DatabaseRegistrationSummary.
        The time the resource was last updated. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this DatabaseRegistrationSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DatabaseRegistrationSummary.
        Possible lifecycle states.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", "IN_PROGRESS", "CANCELING", "CANCELED", "SUCCEEDED", "WAITING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DatabaseRegistrationSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DatabaseRegistrationSummary.
        Possible lifecycle states.


        :param lifecycle_state: The lifecycle_state of this DatabaseRegistrationSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", "IN_PROGRESS", "CANCELING", "CANCELED", "SUCCEEDED", "WAITING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DatabaseRegistrationSummary.
        Describes the object's current state in detail. For example, it can be used to provide
        actionable information for a resource in a Failed state.


        :return: The lifecycle_details of this DatabaseRegistrationSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DatabaseRegistrationSummary.
        Describes the object's current state in detail. For example, it can be used to provide
        actionable information for a resource in a Failed state.


        :param lifecycle_details: The lifecycle_details of this DatabaseRegistrationSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DatabaseRegistrationSummary.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists
        for cross-compatibility only.

        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this DatabaseRegistrationSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DatabaseRegistrationSummary.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists
        for cross-compatibility only.

        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this DatabaseRegistrationSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DatabaseRegistrationSummary.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this DatabaseRegistrationSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DatabaseRegistrationSummary.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this DatabaseRegistrationSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def fqdn(self):
        """
        **[Required]** Gets the fqdn of this DatabaseRegistrationSummary.
        A three-label Fully Qualified Domain Name (FQDN) for a resource.


        :return: The fqdn of this DatabaseRegistrationSummary.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """
        Sets the fqdn of this DatabaseRegistrationSummary.
        A three-label Fully Qualified Domain Name (FQDN) for a resource.


        :param fqdn: The fqdn of this DatabaseRegistrationSummary.
        :type: str
        """
        self._fqdn = fqdn

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this DatabaseRegistrationSummary.
        The `OCID`__ of the target subnet of the dedicated connection.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this DatabaseRegistrationSummary.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this DatabaseRegistrationSummary.
        The `OCID`__ of the target subnet of the dedicated connection.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this DatabaseRegistrationSummary.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DatabaseRegistrationSummary.
        The system tags associated with this resource, if any. The system tags are set by Oracle
        Cloud Infrastructure services. Each key is predefined and scoped to namespaces.  For more
        information, see `Resource Tags`__.

        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this DatabaseRegistrationSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DatabaseRegistrationSummary.
        The system tags associated with this resource, if any. The system tags are set by Oracle
        Cloud Infrastructure services. Each key is predefined and scoped to namespaces.  For more
        information, see `Resource Tags`__.

        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this DatabaseRegistrationSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def database_id(self):
        """
        Gets the database_id of this DatabaseRegistrationSummary.
        The `OCID`__ of the database being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The database_id of this DatabaseRegistrationSummary.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this DatabaseRegistrationSummary.
        The `OCID`__ of the database being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param database_id: The database_id of this DatabaseRegistrationSummary.
        :type: str
        """
        self._database_id = database_id

    @property
    def username(self):
        """
        Gets the username of this DatabaseRegistrationSummary.
        The username Oracle GoldenGate uses to connect the associated system of the given technology.
        This username must already exist and be available by the system/application to be connected to
        and must conform to the case sensitivty requirments defined in it.


        :return: The username of this DatabaseRegistrationSummary.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this DatabaseRegistrationSummary.
        The username Oracle GoldenGate uses to connect the associated system of the given technology.
        This username must already exist and be available by the system/application to be connected to
        and must conform to the case sensitivty requirments defined in it.


        :param username: The username of this DatabaseRegistrationSummary.
        :type: str
        """
        self._username = username

    @property
    def connection_string(self):
        """
        Gets the connection_string of this DatabaseRegistrationSummary.
        Connect descriptor or Easy Connect Naming method used to connect to a database.


        :return: The connection_string of this DatabaseRegistrationSummary.
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """
        Sets the connection_string of this DatabaseRegistrationSummary.
        Connect descriptor or Easy Connect Naming method used to connect to a database.


        :param connection_string: The connection_string of this DatabaseRegistrationSummary.
        :type: str
        """
        self._connection_string = connection_string

    @property
    def session_mode(self):
        """
        Gets the session_mode of this DatabaseRegistrationSummary.
        The mode of the database connection session to be established by the data client.
        'REDIRECT' - for a RAC database, 'DIRECT' - for a non-RAC database.
        Connection to a RAC database involves a redirection received from the SCAN listeners
        to the database node to connect to. By default the mode would be DIRECT.

        Allowed values for this property are: "DIRECT", "REDIRECT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The session_mode of this DatabaseRegistrationSummary.
        :rtype: str
        """
        return self._session_mode

    @session_mode.setter
    def session_mode(self, session_mode):
        """
        Sets the session_mode of this DatabaseRegistrationSummary.
        The mode of the database connection session to be established by the data client.
        'REDIRECT' - for a RAC database, 'DIRECT' - for a non-RAC database.
        Connection to a RAC database involves a redirection received from the SCAN listeners
        to the database node to connect to. By default the mode would be DIRECT.


        :param session_mode: The session_mode of this DatabaseRegistrationSummary.
        :type: str
        """
        allowed_values = ["DIRECT", "REDIRECT"]
        if not value_allowed_none_or_none_sentinel(session_mode, allowed_values):
            session_mode = 'UNKNOWN_ENUM_VALUE'
        self._session_mode = session_mode

    @property
    def alias_name(self):
        """
        Gets the alias_name of this DatabaseRegistrationSummary.
        Credential store alias.


        :return: The alias_name of this DatabaseRegistrationSummary.
        :rtype: str
        """
        return self._alias_name

    @alias_name.setter
    def alias_name(self, alias_name):
        """
        Sets the alias_name of this DatabaseRegistrationSummary.
        Credential store alias.


        :param alias_name: The alias_name of this DatabaseRegistrationSummary.
        :type: str
        """
        self._alias_name = alias_name

    @property
    def secret_id(self):
        """
        Gets the secret_id of this DatabaseRegistrationSummary.
        The OCID of the customer's GoldenGate Service Secret.
        If provided, it references a key that customers will be required to ensure the policies are established
        to permit GoldenGate to use this Secret.


        :return: The secret_id of this DatabaseRegistrationSummary.
        :rtype: str
        """
        return self._secret_id

    @secret_id.setter
    def secret_id(self, secret_id):
        """
        Sets the secret_id of this DatabaseRegistrationSummary.
        The OCID of the customer's GoldenGate Service Secret.
        If provided, it references a key that customers will be required to ensure the policies are established
        to permit GoldenGate to use this Secret.


        :param secret_id: The secret_id of this DatabaseRegistrationSummary.
        :type: str
        """
        self._secret_id = secret_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
