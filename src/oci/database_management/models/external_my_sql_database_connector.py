# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalMySqlDatabaseConnector(object):
    """
    Details of external database connector.
    """

    #: A constant which can be used with the lifecycle_state property of a ExternalMySqlDatabaseConnector.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ExternalMySqlDatabaseConnector.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ExternalMySqlDatabaseConnector.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ExternalMySqlDatabaseConnector.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ExternalMySqlDatabaseConnector.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ExternalMySqlDatabaseConnector.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the source_database_type property of a ExternalMySqlDatabaseConnector.
    #: This constant has a value of "EXTERNAL"
    SOURCE_DATABASE_TYPE_EXTERNAL = "EXTERNAL"

    #: A constant which can be used with the source_database_type property of a ExternalMySqlDatabaseConnector.
    #: This constant has a value of "MDS"
    SOURCE_DATABASE_TYPE_MDS = "MDS"

    #: A constant which can be used with the connector_type property of a ExternalMySqlDatabaseConnector.
    #: This constant has a value of "MACS"
    CONNECTOR_TYPE_MACS = "MACS"

    #: A constant which can be used with the network_protocol property of a ExternalMySqlDatabaseConnector.
    #: This constant has a value of "TCP"
    NETWORK_PROTOCOL_TCP = "TCP"

    #: A constant which can be used with the network_protocol property of a ExternalMySqlDatabaseConnector.
    #: This constant has a value of "TCPS"
    NETWORK_PROTOCOL_TCPS = "TCPS"

    #: A constant which can be used with the network_protocol property of a ExternalMySqlDatabaseConnector.
    #: This constant has a value of "SOCKETS"
    NETWORK_PROTOCOL_SOCKETS = "SOCKETS"

    #: A constant which can be used with the credential_type property of a ExternalMySqlDatabaseConnector.
    #: This constant has a value of "MYSQL_EXTERNAL_NON_SSL_CREDENTIALS"
    CREDENTIAL_TYPE_MYSQL_EXTERNAL_NON_SSL_CREDENTIALS = "MYSQL_EXTERNAL_NON_SSL_CREDENTIALS"

    #: A constant which can be used with the credential_type property of a ExternalMySqlDatabaseConnector.
    #: This constant has a value of "MYSQL_EXTERNAL_SSL_CREDENTIALS"
    CREDENTIAL_TYPE_MYSQL_EXTERNAL_SSL_CREDENTIALS = "MYSQL_EXTERNAL_SSL_CREDENTIALS"

    #: A constant which can be used with the credential_type property of a ExternalMySqlDatabaseConnector.
    #: This constant has a value of "MYSQL_EXTERNAL_SOCKET_CREDENTIALS"
    CREDENTIAL_TYPE_MYSQL_EXTERNAL_SOCKET_CREDENTIALS = "MYSQL_EXTERNAL_SOCKET_CREDENTIALS"

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalMySqlDatabaseConnector object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ExternalMySqlDatabaseConnector.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ExternalMySqlDatabaseConnector.
        :type compartment_id: str

        :param associated_services:
            The value to assign to the associated_services property of this ExternalMySqlDatabaseConnector.
        :type associated_services: str

        :param external_database_id:
            The value to assign to the external_database_id property of this ExternalMySqlDatabaseConnector.
        :type external_database_id: str

        :param id:
            The value to assign to the id property of this ExternalMySqlDatabaseConnector.
        :type id: str

        :param time_updated:
            The value to assign to the time_updated property of this ExternalMySqlDatabaseConnector.
        :type time_updated: datetime

        :param time_created:
            The value to assign to the time_created property of this ExternalMySqlDatabaseConnector.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ExternalMySqlDatabaseConnector.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param source_database:
            The value to assign to the source_database property of this ExternalMySqlDatabaseConnector.
        :type source_database: str

        :param source_database_type:
            The value to assign to the source_database_type property of this ExternalMySqlDatabaseConnector.
            Allowed values for this property are: "EXTERNAL", "MDS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type source_database_type: str

        :param macs_agent_id:
            The value to assign to the macs_agent_id property of this ExternalMySqlDatabaseConnector.
        :type macs_agent_id: str

        :param connection_status:
            The value to assign to the connection_status property of this ExternalMySqlDatabaseConnector.
        :type connection_status: str

        :param time_connection_status_updated:
            The value to assign to the time_connection_status_updated property of this ExternalMySqlDatabaseConnector.
        :type time_connection_status_updated: datetime

        :param host_name:
            The value to assign to the host_name property of this ExternalMySqlDatabaseConnector.
        :type host_name: str

        :param port:
            The value to assign to the port property of this ExternalMySqlDatabaseConnector.
        :type port: int

        :param connector_type:
            The value to assign to the connector_type property of this ExternalMySqlDatabaseConnector.
            Allowed values for this property are: "MACS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type connector_type: str

        :param network_protocol:
            The value to assign to the network_protocol property of this ExternalMySqlDatabaseConnector.
            Allowed values for this property are: "TCP", "TCPS", "SOCKETS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type network_protocol: str

        :param credential_type:
            The value to assign to the credential_type property of this ExternalMySqlDatabaseConnector.
            Allowed values for this property are: "MYSQL_EXTERNAL_NON_SSL_CREDENTIALS", "MYSQL_EXTERNAL_SSL_CREDENTIALS", "MYSQL_EXTERNAL_SOCKET_CREDENTIALS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type credential_type: str

        :param ssl_secret_id:
            The value to assign to the ssl_secret_id property of this ExternalMySqlDatabaseConnector.
        :type ssl_secret_id: str

        :param ssl_secret_name:
            The value to assign to the ssl_secret_name property of this ExternalMySqlDatabaseConnector.
        :type ssl_secret_name: str

        """
        self.swagger_types = {
            'name': 'str',
            'compartment_id': 'str',
            'associated_services': 'str',
            'external_database_id': 'str',
            'id': 'str',
            'time_updated': 'datetime',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'source_database': 'str',
            'source_database_type': 'str',
            'macs_agent_id': 'str',
            'connection_status': 'str',
            'time_connection_status_updated': 'datetime',
            'host_name': 'str',
            'port': 'int',
            'connector_type': 'str',
            'network_protocol': 'str',
            'credential_type': 'str',
            'ssl_secret_id': 'str',
            'ssl_secret_name': 'str'
        }
        self.attribute_map = {
            'name': 'name',
            'compartment_id': 'compartmentId',
            'associated_services': 'associatedServices',
            'external_database_id': 'externalDatabaseId',
            'id': 'id',
            'time_updated': 'timeUpdated',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'source_database': 'sourceDatabase',
            'source_database_type': 'sourceDatabaseType',
            'macs_agent_id': 'macsAgentId',
            'connection_status': 'connectionStatus',
            'time_connection_status_updated': 'timeConnectionStatusUpdated',
            'host_name': 'hostName',
            'port': 'port',
            'connector_type': 'connectorType',
            'network_protocol': 'networkProtocol',
            'credential_type': 'credentialType',
            'ssl_secret_id': 'sslSecretId',
            'ssl_secret_name': 'sslSecretName'
        }
        self._name = None
        self._compartment_id = None
        self._associated_services = None
        self._external_database_id = None
        self._id = None
        self._time_updated = None
        self._time_created = None
        self._lifecycle_state = None
        self._source_database = None
        self._source_database_type = None
        self._macs_agent_id = None
        self._connection_status = None
        self._time_connection_status_updated = None
        self._host_name = None
        self._port = None
        self._connector_type = None
        self._network_protocol = None
        self._credential_type = None
        self._ssl_secret_id = None
        self._ssl_secret_name = None

    @property
    def name(self):
        """
        Gets the name of this ExternalMySqlDatabaseConnector.
        External MySQL Database Connector Name.


        :return: The name of this ExternalMySqlDatabaseConnector.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ExternalMySqlDatabaseConnector.
        External MySQL Database Connector Name.


        :param name: The name of this ExternalMySqlDatabaseConnector.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this ExternalMySqlDatabaseConnector.
        OCID of compartment for the External MySQL connector.


        :return: The compartment_id of this ExternalMySqlDatabaseConnector.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ExternalMySqlDatabaseConnector.
        OCID of compartment for the External MySQL connector.


        :param compartment_id: The compartment_id of this ExternalMySqlDatabaseConnector.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def associated_services(self):
        """
        Gets the associated_services of this ExternalMySqlDatabaseConnector.
        OCI Services associated with this connector.


        :return: The associated_services of this ExternalMySqlDatabaseConnector.
        :rtype: str
        """
        return self._associated_services

    @associated_services.setter
    def associated_services(self, associated_services):
        """
        Sets the associated_services of this ExternalMySqlDatabaseConnector.
        OCI Services associated with this connector.


        :param associated_services: The associated_services of this ExternalMySqlDatabaseConnector.
        :type: str
        """
        self._associated_services = associated_services

    @property
    def external_database_id(self):
        """
        Gets the external_database_id of this ExternalMySqlDatabaseConnector.
        OCID of MySQL Database resource


        :return: The external_database_id of this ExternalMySqlDatabaseConnector.
        :rtype: str
        """
        return self._external_database_id

    @external_database_id.setter
    def external_database_id(self, external_database_id):
        """
        Sets the external_database_id of this ExternalMySqlDatabaseConnector.
        OCID of MySQL Database resource


        :param external_database_id: The external_database_id of this ExternalMySqlDatabaseConnector.
        :type: str
        """
        self._external_database_id = external_database_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ExternalMySqlDatabaseConnector.
        OCID of MySQL Database Connector.


        :return: The id of this ExternalMySqlDatabaseConnector.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExternalMySqlDatabaseConnector.
        OCID of MySQL Database Connector.


        :param id: The id of this ExternalMySqlDatabaseConnector.
        :type: str
        """
        self._id = id

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ExternalMySqlDatabaseConnector.
        Connector update time.


        :return: The time_updated of this ExternalMySqlDatabaseConnector.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ExternalMySqlDatabaseConnector.
        Connector update time.


        :param time_updated: The time_updated of this ExternalMySqlDatabaseConnector.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_created(self):
        """
        Gets the time_created of this ExternalMySqlDatabaseConnector.
        Connector creation time.


        :return: The time_created of this ExternalMySqlDatabaseConnector.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ExternalMySqlDatabaseConnector.
        Connector creation time.


        :param time_created: The time_created of this ExternalMySqlDatabaseConnector.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ExternalMySqlDatabaseConnector.
        Indicates lifecycle  state of the resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ExternalMySqlDatabaseConnector.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ExternalMySqlDatabaseConnector.
        Indicates lifecycle  state of the resource.


        :param lifecycle_state: The lifecycle_state of this ExternalMySqlDatabaseConnector.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def source_database(self):
        """
        Gets the source_database of this ExternalMySqlDatabaseConnector.
        Name of MySQL Database.


        :return: The source_database of this ExternalMySqlDatabaseConnector.
        :rtype: str
        """
        return self._source_database

    @source_database.setter
    def source_database(self, source_database):
        """
        Sets the source_database of this ExternalMySqlDatabaseConnector.
        Name of MySQL Database.


        :param source_database: The source_database of this ExternalMySqlDatabaseConnector.
        :type: str
        """
        self._source_database = source_database

    @property
    def source_database_type(self):
        """
        Gets the source_database_type of this ExternalMySqlDatabaseConnector.
        Type of MySQL Database.

        Allowed values for this property are: "EXTERNAL", "MDS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The source_database_type of this ExternalMySqlDatabaseConnector.
        :rtype: str
        """
        return self._source_database_type

    @source_database_type.setter
    def source_database_type(self, source_database_type):
        """
        Sets the source_database_type of this ExternalMySqlDatabaseConnector.
        Type of MySQL Database.


        :param source_database_type: The source_database_type of this ExternalMySqlDatabaseConnector.
        :type: str
        """
        allowed_values = ["EXTERNAL", "MDS"]
        if not value_allowed_none_or_none_sentinel(source_database_type, allowed_values):
            source_database_type = 'UNKNOWN_ENUM_VALUE'
        self._source_database_type = source_database_type

    @property
    def macs_agent_id(self):
        """
        Gets the macs_agent_id of this ExternalMySqlDatabaseConnector.
        Agent Id of the MACS agent.


        :return: The macs_agent_id of this ExternalMySqlDatabaseConnector.
        :rtype: str
        """
        return self._macs_agent_id

    @macs_agent_id.setter
    def macs_agent_id(self, macs_agent_id):
        """
        Sets the macs_agent_id of this ExternalMySqlDatabaseConnector.
        Agent Id of the MACS agent.


        :param macs_agent_id: The macs_agent_id of this ExternalMySqlDatabaseConnector.
        :type: str
        """
        self._macs_agent_id = macs_agent_id

    @property
    def connection_status(self):
        """
        Gets the connection_status of this ExternalMySqlDatabaseConnector.
        Connection Status


        :return: The connection_status of this ExternalMySqlDatabaseConnector.
        :rtype: str
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """
        Sets the connection_status of this ExternalMySqlDatabaseConnector.
        Connection Status


        :param connection_status: The connection_status of this ExternalMySqlDatabaseConnector.
        :type: str
        """
        self._connection_status = connection_status

    @property
    def time_connection_status_updated(self):
        """
        Gets the time_connection_status_updated of this ExternalMySqlDatabaseConnector.
        Time when connection status was last updated.


        :return: The time_connection_status_updated of this ExternalMySqlDatabaseConnector.
        :rtype: datetime
        """
        return self._time_connection_status_updated

    @time_connection_status_updated.setter
    def time_connection_status_updated(self, time_connection_status_updated):
        """
        Sets the time_connection_status_updated of this ExternalMySqlDatabaseConnector.
        Time when connection status was last updated.


        :param time_connection_status_updated: The time_connection_status_updated of this ExternalMySqlDatabaseConnector.
        :type: datetime
        """
        self._time_connection_status_updated = time_connection_status_updated

    @property
    def host_name(self):
        """
        Gets the host_name of this ExternalMySqlDatabaseConnector.
        Host name for Connector.


        :return: The host_name of this ExternalMySqlDatabaseConnector.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this ExternalMySqlDatabaseConnector.
        Host name for Connector.


        :param host_name: The host_name of this ExternalMySqlDatabaseConnector.
        :type: str
        """
        self._host_name = host_name

    @property
    def port(self):
        """
        Gets the port of this ExternalMySqlDatabaseConnector.
        Connector port.


        :return: The port of this ExternalMySqlDatabaseConnector.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this ExternalMySqlDatabaseConnector.
        Connector port.


        :param port: The port of this ExternalMySqlDatabaseConnector.
        :type: int
        """
        self._port = port

    @property
    def connector_type(self):
        """
        Gets the connector_type of this ExternalMySqlDatabaseConnector.
        Connector Type.

        Allowed values for this property are: "MACS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The connector_type of this ExternalMySqlDatabaseConnector.
        :rtype: str
        """
        return self._connector_type

    @connector_type.setter
    def connector_type(self, connector_type):
        """
        Sets the connector_type of this ExternalMySqlDatabaseConnector.
        Connector Type.


        :param connector_type: The connector_type of this ExternalMySqlDatabaseConnector.
        :type: str
        """
        allowed_values = ["MACS"]
        if not value_allowed_none_or_none_sentinel(connector_type, allowed_values):
            connector_type = 'UNKNOWN_ENUM_VALUE'
        self._connector_type = connector_type

    @property
    def network_protocol(self):
        """
        Gets the network_protocol of this ExternalMySqlDatabaseConnector.
        Network Protocol.

        Allowed values for this property are: "TCP", "TCPS", "SOCKETS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The network_protocol of this ExternalMySqlDatabaseConnector.
        :rtype: str
        """
        return self._network_protocol

    @network_protocol.setter
    def network_protocol(self, network_protocol):
        """
        Sets the network_protocol of this ExternalMySqlDatabaseConnector.
        Network Protocol.


        :param network_protocol: The network_protocol of this ExternalMySqlDatabaseConnector.
        :type: str
        """
        allowed_values = ["TCP", "TCPS", "SOCKETS"]
        if not value_allowed_none_or_none_sentinel(network_protocol, allowed_values):
            network_protocol = 'UNKNOWN_ENUM_VALUE'
        self._network_protocol = network_protocol

    @property
    def credential_type(self):
        """
        Gets the credential_type of this ExternalMySqlDatabaseConnector.
        Credential type used to connect to database.

        Allowed values for this property are: "MYSQL_EXTERNAL_NON_SSL_CREDENTIALS", "MYSQL_EXTERNAL_SSL_CREDENTIALS", "MYSQL_EXTERNAL_SOCKET_CREDENTIALS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The credential_type of this ExternalMySqlDatabaseConnector.
        :rtype: str
        """
        return self._credential_type

    @credential_type.setter
    def credential_type(self, credential_type):
        """
        Sets the credential_type of this ExternalMySqlDatabaseConnector.
        Credential type used to connect to database.


        :param credential_type: The credential_type of this ExternalMySqlDatabaseConnector.
        :type: str
        """
        allowed_values = ["MYSQL_EXTERNAL_NON_SSL_CREDENTIALS", "MYSQL_EXTERNAL_SSL_CREDENTIALS", "MYSQL_EXTERNAL_SOCKET_CREDENTIALS"]
        if not value_allowed_none_or_none_sentinel(credential_type, allowed_values):
            credential_type = 'UNKNOWN_ENUM_VALUE'
        self._credential_type = credential_type

    @property
    def ssl_secret_id(self):
        """
        Gets the ssl_secret_id of this ExternalMySqlDatabaseConnector.
        OCID of the SSL secret, if TCPS with SSL is used to connect to database.


        :return: The ssl_secret_id of this ExternalMySqlDatabaseConnector.
        :rtype: str
        """
        return self._ssl_secret_id

    @ssl_secret_id.setter
    def ssl_secret_id(self, ssl_secret_id):
        """
        Sets the ssl_secret_id of this ExternalMySqlDatabaseConnector.
        OCID of the SSL secret, if TCPS with SSL is used to connect to database.


        :param ssl_secret_id: The ssl_secret_id of this ExternalMySqlDatabaseConnector.
        :type: str
        """
        self._ssl_secret_id = ssl_secret_id

    @property
    def ssl_secret_name(self):
        """
        Gets the ssl_secret_name of this ExternalMySqlDatabaseConnector.
        Name of the SSL secret, if TCPS with SSL is used to connect to database.


        :return: The ssl_secret_name of this ExternalMySqlDatabaseConnector.
        :rtype: str
        """
        return self._ssl_secret_name

    @ssl_secret_name.setter
    def ssl_secret_name(self, ssl_secret_name):
        """
        Sets the ssl_secret_name of this ExternalMySqlDatabaseConnector.
        Name of the SSL secret, if TCPS with SSL is used to connect to database.


        :param ssl_secret_name: The ssl_secret_name of this ExternalMySqlDatabaseConnector.
        :type: str
        """
        self._ssl_secret_name = ssl_secret_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
