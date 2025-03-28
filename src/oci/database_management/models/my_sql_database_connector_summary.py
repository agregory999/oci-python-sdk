# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MySqlDatabaseConnectorSummary(object):
    """
    Details of external database connector.
    """

    #: A constant which can be used with the source_database_type property of a MySqlDatabaseConnectorSummary.
    #: This constant has a value of "EXTERNAL"
    SOURCE_DATABASE_TYPE_EXTERNAL = "EXTERNAL"

    #: A constant which can be used with the source_database_type property of a MySqlDatabaseConnectorSummary.
    #: This constant has a value of "MDS"
    SOURCE_DATABASE_TYPE_MDS = "MDS"

    #: A constant which can be used with the connector_type property of a MySqlDatabaseConnectorSummary.
    #: This constant has a value of "MACS"
    CONNECTOR_TYPE_MACS = "MACS"

    #: A constant which can be used with the network_protocol property of a MySqlDatabaseConnectorSummary.
    #: This constant has a value of "TCP"
    NETWORK_PROTOCOL_TCP = "TCP"

    #: A constant which can be used with the network_protocol property of a MySqlDatabaseConnectorSummary.
    #: This constant has a value of "TCPS"
    NETWORK_PROTOCOL_TCPS = "TCPS"

    #: A constant which can be used with the network_protocol property of a MySqlDatabaseConnectorSummary.
    #: This constant has a value of "SOCKETS"
    NETWORK_PROTOCOL_SOCKETS = "SOCKETS"

    #: A constant which can be used with the credential_type property of a MySqlDatabaseConnectorSummary.
    #: This constant has a value of "MYSQL_EXTERNAL_NON_SSL_CREDENTIALS"
    CREDENTIAL_TYPE_MYSQL_EXTERNAL_NON_SSL_CREDENTIALS = "MYSQL_EXTERNAL_NON_SSL_CREDENTIALS"

    #: A constant which can be used with the credential_type property of a MySqlDatabaseConnectorSummary.
    #: This constant has a value of "MYSQL_EXTERNAL_SSL_CREDENTIALS"
    CREDENTIAL_TYPE_MYSQL_EXTERNAL_SSL_CREDENTIALS = "MYSQL_EXTERNAL_SSL_CREDENTIALS"

    #: A constant which can be used with the credential_type property of a MySqlDatabaseConnectorSummary.
    #: This constant has a value of "MYSQL_EXTERNAL_SOCKET_CREDENTIALS"
    CREDENTIAL_TYPE_MYSQL_EXTERNAL_SOCKET_CREDENTIALS = "MYSQL_EXTERNAL_SOCKET_CREDENTIALS"

    #: A constant which can be used with the lifecycle_state property of a MySqlDatabaseConnectorSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a MySqlDatabaseConnectorSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a MySqlDatabaseConnectorSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MySqlDatabaseConnectorSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a MySqlDatabaseConnectorSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a MySqlDatabaseConnectorSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new MySqlDatabaseConnectorSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this MySqlDatabaseConnectorSummary.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MySqlDatabaseConnectorSummary.
        :type compartment_id: str

        :param associated_services:
            The value to assign to the associated_services property of this MySqlDatabaseConnectorSummary.
        :type associated_services: str

        :param id:
            The value to assign to the id property of this MySqlDatabaseConnectorSummary.
        :type id: str

        :param time_created:
            The value to assign to the time_created property of this MySqlDatabaseConnectorSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this MySqlDatabaseConnectorSummary.
        :type time_updated: datetime

        :param source_database:
            The value to assign to the source_database property of this MySqlDatabaseConnectorSummary.
        :type source_database: str

        :param source_database_type:
            The value to assign to the source_database_type property of this MySqlDatabaseConnectorSummary.
            Allowed values for this property are: "EXTERNAL", "MDS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type source_database_type: str

        :param connection_status:
            The value to assign to the connection_status property of this MySqlDatabaseConnectorSummary.
        :type connection_status: str

        :param time_connection_status_updated:
            The value to assign to the time_connection_status_updated property of this MySqlDatabaseConnectorSummary.
        :type time_connection_status_updated: datetime

        :param host_name:
            The value to assign to the host_name property of this MySqlDatabaseConnectorSummary.
        :type host_name: str

        :param macs_agent_id:
            The value to assign to the macs_agent_id property of this MySqlDatabaseConnectorSummary.
        :type macs_agent_id: str

        :param port:
            The value to assign to the port property of this MySqlDatabaseConnectorSummary.
        :type port: int

        :param connector_type:
            The value to assign to the connector_type property of this MySqlDatabaseConnectorSummary.
            Allowed values for this property are: "MACS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type connector_type: str

        :param network_protocol:
            The value to assign to the network_protocol property of this MySqlDatabaseConnectorSummary.
            Allowed values for this property are: "TCP", "TCPS", "SOCKETS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type network_protocol: str

        :param credential_type:
            The value to assign to the credential_type property of this MySqlDatabaseConnectorSummary.
            Allowed values for this property are: "MYSQL_EXTERNAL_NON_SSL_CREDENTIALS", "MYSQL_EXTERNAL_SSL_CREDENTIALS", "MYSQL_EXTERNAL_SOCKET_CREDENTIALS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type credential_type: str

        :param system_tags:
            The value to assign to the system_tags property of this MySqlDatabaseConnectorSummary.
        :type system_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MySqlDatabaseConnectorSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'name': 'str',
            'compartment_id': 'str',
            'associated_services': 'str',
            'id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'source_database': 'str',
            'source_database_type': 'str',
            'connection_status': 'str',
            'time_connection_status_updated': 'datetime',
            'host_name': 'str',
            'macs_agent_id': 'str',
            'port': 'int',
            'connector_type': 'str',
            'network_protocol': 'str',
            'credential_type': 'str',
            'system_tags': 'dict(str, dict(str, object))',
            'lifecycle_state': 'str'
        }
        self.attribute_map = {
            'name': 'name',
            'compartment_id': 'compartmentId',
            'associated_services': 'associatedServices',
            'id': 'id',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'source_database': 'sourceDatabase',
            'source_database_type': 'sourceDatabaseType',
            'connection_status': 'connectionStatus',
            'time_connection_status_updated': 'timeConnectionStatusUpdated',
            'host_name': 'hostName',
            'macs_agent_id': 'macsAgentId',
            'port': 'port',
            'connector_type': 'connectorType',
            'network_protocol': 'networkProtocol',
            'credential_type': 'credentialType',
            'system_tags': 'systemTags',
            'lifecycle_state': 'lifecycleState'
        }
        self._name = None
        self._compartment_id = None
        self._associated_services = None
        self._id = None
        self._time_created = None
        self._time_updated = None
        self._source_database = None
        self._source_database_type = None
        self._connection_status = None
        self._time_connection_status_updated = None
        self._host_name = None
        self._macs_agent_id = None
        self._port = None
        self._connector_type = None
        self._network_protocol = None
        self._credential_type = None
        self._system_tags = None
        self._lifecycle_state = None

    @property
    def name(self):
        """
        Gets the name of this MySqlDatabaseConnectorSummary.
        External MySQL Database Connector Name


        :return: The name of this MySqlDatabaseConnectorSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MySqlDatabaseConnectorSummary.
        External MySQL Database Connector Name


        :param name: The name of this MySqlDatabaseConnectorSummary.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this MySqlDatabaseConnectorSummary.
        OCID of compartment for the External MySQL connector.


        :return: The compartment_id of this MySqlDatabaseConnectorSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MySqlDatabaseConnectorSummary.
        OCID of compartment for the External MySQL connector.


        :param compartment_id: The compartment_id of this MySqlDatabaseConnectorSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def associated_services(self):
        """
        Gets the associated_services of this MySqlDatabaseConnectorSummary.
        OCI Services associated with this connector.


        :return: The associated_services of this MySqlDatabaseConnectorSummary.
        :rtype: str
        """
        return self._associated_services

    @associated_services.setter
    def associated_services(self, associated_services):
        """
        Sets the associated_services of this MySqlDatabaseConnectorSummary.
        OCI Services associated with this connector.


        :param associated_services: The associated_services of this MySqlDatabaseConnectorSummary.
        :type: str
        """
        self._associated_services = associated_services

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MySqlDatabaseConnectorSummary.
        OCID of MySQL Database Connector.


        :return: The id of this MySqlDatabaseConnectorSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MySqlDatabaseConnectorSummary.
        OCID of MySQL Database Connector.


        :param id: The id of this MySqlDatabaseConnectorSummary.
        :type: str
        """
        self._id = id

    @property
    def time_created(self):
        """
        Gets the time_created of this MySqlDatabaseConnectorSummary.
        Connector creation time.


        :return: The time_created of this MySqlDatabaseConnectorSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MySqlDatabaseConnectorSummary.
        Connector creation time.


        :param time_created: The time_created of this MySqlDatabaseConnectorSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this MySqlDatabaseConnectorSummary.
        Connector update time.


        :return: The time_updated of this MySqlDatabaseConnectorSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this MySqlDatabaseConnectorSummary.
        Connector update time.


        :param time_updated: The time_updated of this MySqlDatabaseConnectorSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def source_database(self):
        """
        Gets the source_database of this MySqlDatabaseConnectorSummary.
        Name of MySQL Database.


        :return: The source_database of this MySqlDatabaseConnectorSummary.
        :rtype: str
        """
        return self._source_database

    @source_database.setter
    def source_database(self, source_database):
        """
        Sets the source_database of this MySqlDatabaseConnectorSummary.
        Name of MySQL Database.


        :param source_database: The source_database of this MySqlDatabaseConnectorSummary.
        :type: str
        """
        self._source_database = source_database

    @property
    def source_database_type(self):
        """
        Gets the source_database_type of this MySqlDatabaseConnectorSummary.
        Type of MySQL Database.

        Allowed values for this property are: "EXTERNAL", "MDS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The source_database_type of this MySqlDatabaseConnectorSummary.
        :rtype: str
        """
        return self._source_database_type

    @source_database_type.setter
    def source_database_type(self, source_database_type):
        """
        Sets the source_database_type of this MySqlDatabaseConnectorSummary.
        Type of MySQL Database.


        :param source_database_type: The source_database_type of this MySqlDatabaseConnectorSummary.
        :type: str
        """
        allowed_values = ["EXTERNAL", "MDS"]
        if not value_allowed_none_or_none_sentinel(source_database_type, allowed_values):
            source_database_type = 'UNKNOWN_ENUM_VALUE'
        self._source_database_type = source_database_type

    @property
    def connection_status(self):
        """
        Gets the connection_status of this MySqlDatabaseConnectorSummary.
        Connection Status.


        :return: The connection_status of this MySqlDatabaseConnectorSummary.
        :rtype: str
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """
        Sets the connection_status of this MySqlDatabaseConnectorSummary.
        Connection Status.


        :param connection_status: The connection_status of this MySqlDatabaseConnectorSummary.
        :type: str
        """
        self._connection_status = connection_status

    @property
    def time_connection_status_updated(self):
        """
        Gets the time_connection_status_updated of this MySqlDatabaseConnectorSummary.
        Time when connection status was last updated.


        :return: The time_connection_status_updated of this MySqlDatabaseConnectorSummary.
        :rtype: datetime
        """
        return self._time_connection_status_updated

    @time_connection_status_updated.setter
    def time_connection_status_updated(self, time_connection_status_updated):
        """
        Sets the time_connection_status_updated of this MySqlDatabaseConnectorSummary.
        Time when connection status was last updated.


        :param time_connection_status_updated: The time_connection_status_updated of this MySqlDatabaseConnectorSummary.
        :type: datetime
        """
        self._time_connection_status_updated = time_connection_status_updated

    @property
    def host_name(self):
        """
        Gets the host_name of this MySqlDatabaseConnectorSummary.
        Host name for Connector.


        :return: The host_name of this MySqlDatabaseConnectorSummary.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this MySqlDatabaseConnectorSummary.
        Host name for Connector.


        :param host_name: The host_name of this MySqlDatabaseConnectorSummary.
        :type: str
        """
        self._host_name = host_name

    @property
    def macs_agent_id(self):
        """
        Gets the macs_agent_id of this MySqlDatabaseConnectorSummary.
        Agent Id of the MACS agent.


        :return: The macs_agent_id of this MySqlDatabaseConnectorSummary.
        :rtype: str
        """
        return self._macs_agent_id

    @macs_agent_id.setter
    def macs_agent_id(self, macs_agent_id):
        """
        Sets the macs_agent_id of this MySqlDatabaseConnectorSummary.
        Agent Id of the MACS agent.


        :param macs_agent_id: The macs_agent_id of this MySqlDatabaseConnectorSummary.
        :type: str
        """
        self._macs_agent_id = macs_agent_id

    @property
    def port(self):
        """
        Gets the port of this MySqlDatabaseConnectorSummary.
        Connector port.


        :return: The port of this MySqlDatabaseConnectorSummary.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this MySqlDatabaseConnectorSummary.
        Connector port.


        :param port: The port of this MySqlDatabaseConnectorSummary.
        :type: int
        """
        self._port = port

    @property
    def connector_type(self):
        """
        Gets the connector_type of this MySqlDatabaseConnectorSummary.
        Connector Type.

        Allowed values for this property are: "MACS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The connector_type of this MySqlDatabaseConnectorSummary.
        :rtype: str
        """
        return self._connector_type

    @connector_type.setter
    def connector_type(self, connector_type):
        """
        Sets the connector_type of this MySqlDatabaseConnectorSummary.
        Connector Type.


        :param connector_type: The connector_type of this MySqlDatabaseConnectorSummary.
        :type: str
        """
        allowed_values = ["MACS"]
        if not value_allowed_none_or_none_sentinel(connector_type, allowed_values):
            connector_type = 'UNKNOWN_ENUM_VALUE'
        self._connector_type = connector_type

    @property
    def network_protocol(self):
        """
        Gets the network_protocol of this MySqlDatabaseConnectorSummary.
        Network Protocol.

        Allowed values for this property are: "TCP", "TCPS", "SOCKETS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The network_protocol of this MySqlDatabaseConnectorSummary.
        :rtype: str
        """
        return self._network_protocol

    @network_protocol.setter
    def network_protocol(self, network_protocol):
        """
        Sets the network_protocol of this MySqlDatabaseConnectorSummary.
        Network Protocol.


        :param network_protocol: The network_protocol of this MySqlDatabaseConnectorSummary.
        :type: str
        """
        allowed_values = ["TCP", "TCPS", "SOCKETS"]
        if not value_allowed_none_or_none_sentinel(network_protocol, allowed_values):
            network_protocol = 'UNKNOWN_ENUM_VALUE'
        self._network_protocol = network_protocol

    @property
    def credential_type(self):
        """
        Gets the credential_type of this MySqlDatabaseConnectorSummary.
        Credential type used to connect to database.

        Allowed values for this property are: "MYSQL_EXTERNAL_NON_SSL_CREDENTIALS", "MYSQL_EXTERNAL_SSL_CREDENTIALS", "MYSQL_EXTERNAL_SOCKET_CREDENTIALS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The credential_type of this MySqlDatabaseConnectorSummary.
        :rtype: str
        """
        return self._credential_type

    @credential_type.setter
    def credential_type(self, credential_type):
        """
        Sets the credential_type of this MySqlDatabaseConnectorSummary.
        Credential type used to connect to database.


        :param credential_type: The credential_type of this MySqlDatabaseConnectorSummary.
        :type: str
        """
        allowed_values = ["MYSQL_EXTERNAL_NON_SSL_CREDENTIALS", "MYSQL_EXTERNAL_SSL_CREDENTIALS", "MYSQL_EXTERNAL_SOCKET_CREDENTIALS"]
        if not value_allowed_none_or_none_sentinel(credential_type, allowed_values):
            credential_type = 'UNKNOWN_ENUM_VALUE'
        self._credential_type = credential_type

    @property
    def system_tags(self):
        """
        Gets the system_tags of this MySqlDatabaseConnectorSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this MySqlDatabaseConnectorSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this MySqlDatabaseConnectorSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this MySqlDatabaseConnectorSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this MySqlDatabaseConnectorSummary.
        Indicates lifecycle  state of the resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this MySqlDatabaseConnectorSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MySqlDatabaseConnectorSummary.
        Indicates lifecycle  state of the resource.


        :param lifecycle_state: The lifecycle_state of this MySqlDatabaseConnectorSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
