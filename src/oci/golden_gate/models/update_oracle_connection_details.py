# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407

from .update_connection_details import UpdateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateOracleConnectionDetails(UpdateConnectionDetails):
    """
    The information to update an Oracle Database Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateOracleConnectionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.UpdateOracleConnectionDetails.connection_type` attribute
        of this class is ``ORACLE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this UpdateOracleConnectionDetails.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", "AMAZON_KINESIS", "AMAZON_REDSHIFT", "DB2", "REDIS", "ELASTICSEARCH", "GENERIC", "GOOGLE_CLOUD_STORAGE", "GOOGLE_BIGQUERY", "DATABRICKS", "GOOGLE_PUBSUB", "MICROSOFT_FABRIC"
        :type connection_type: str

        :param display_name:
            The value to assign to the display_name property of this UpdateOracleConnectionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateOracleConnectionDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateOracleConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateOracleConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param vault_id:
            The value to assign to the vault_id property of this UpdateOracleConnectionDetails.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this UpdateOracleConnectionDetails.
        :type key_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateOracleConnectionDetails.
        :type nsg_ids: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this UpdateOracleConnectionDetails.
        :type subnet_id: str

        :param routing_method:
            The value to assign to the routing_method property of this UpdateOracleConnectionDetails.
            Allowed values for this property are: "SHARED_SERVICE_ENDPOINT", "SHARED_DEPLOYMENT_ENDPOINT", "DEDICATED_ENDPOINT"
        :type routing_method: str

        :param does_use_secret_ids:
            The value to assign to the does_use_secret_ids property of this UpdateOracleConnectionDetails.
        :type does_use_secret_ids: bool

        :param username:
            The value to assign to the username property of this UpdateOracleConnectionDetails.
        :type username: str

        :param password:
            The value to assign to the password property of this UpdateOracleConnectionDetails.
        :type password: str

        :param password_secret_id:
            The value to assign to the password_secret_id property of this UpdateOracleConnectionDetails.
        :type password_secret_id: str

        :param connection_string:
            The value to assign to the connection_string property of this UpdateOracleConnectionDetails.
        :type connection_string: str

        :param authentication_mode:
            The value to assign to the authentication_mode property of this UpdateOracleConnectionDetails.
        :type authentication_mode: str

        :param wallet:
            The value to assign to the wallet property of this UpdateOracleConnectionDetails.
        :type wallet: str

        :param wallet_secret_id:
            The value to assign to the wallet_secret_id property of this UpdateOracleConnectionDetails.
        :type wallet_secret_id: str

        :param session_mode:
            The value to assign to the session_mode property of this UpdateOracleConnectionDetails.
        :type session_mode: str

        :param private_ip:
            The value to assign to the private_ip property of this UpdateOracleConnectionDetails.
        :type private_ip: str

        :param database_id:
            The value to assign to the database_id property of this UpdateOracleConnectionDetails.
        :type database_id: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'vault_id': 'str',
            'key_id': 'str',
            'nsg_ids': 'list[str]',
            'subnet_id': 'str',
            'routing_method': 'str',
            'does_use_secret_ids': 'bool',
            'username': 'str',
            'password': 'str',
            'password_secret_id': 'str',
            'connection_string': 'str',
            'authentication_mode': 'str',
            'wallet': 'str',
            'wallet_secret_id': 'str',
            'session_mode': 'str',
            'private_ip': 'str',
            'database_id': 'str'
        }
        self.attribute_map = {
            'connection_type': 'connectionType',
            'display_name': 'displayName',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'nsg_ids': 'nsgIds',
            'subnet_id': 'subnetId',
            'routing_method': 'routingMethod',
            'does_use_secret_ids': 'doesUseSecretIds',
            'username': 'username',
            'password': 'password',
            'password_secret_id': 'passwordSecretId',
            'connection_string': 'connectionString',
            'authentication_mode': 'authenticationMode',
            'wallet': 'wallet',
            'wallet_secret_id': 'walletSecretId',
            'session_mode': 'sessionMode',
            'private_ip': 'privateIp',
            'database_id': 'databaseId'
        }
        self._connection_type = None
        self._display_name = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._vault_id = None
        self._key_id = None
        self._nsg_ids = None
        self._subnet_id = None
        self._routing_method = None
        self._does_use_secret_ids = None
        self._username = None
        self._password = None
        self._password_secret_id = None
        self._connection_string = None
        self._authentication_mode = None
        self._wallet = None
        self._wallet_secret_id = None
        self._session_mode = None
        self._private_ip = None
        self._database_id = None
        self._connection_type = 'ORACLE'

    @property
    def username(self):
        """
        Gets the username of this UpdateOracleConnectionDetails.
        The username Oracle GoldenGate uses to connect the associated system of the given technology.
        This username must already exist and be available by the system/application to be connected to
        and must conform to the case sensitivty requirments defined in it.


        :return: The username of this UpdateOracleConnectionDetails.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this UpdateOracleConnectionDetails.
        The username Oracle GoldenGate uses to connect the associated system of the given technology.
        This username must already exist and be available by the system/application to be connected to
        and must conform to the case sensitivty requirments defined in it.


        :param username: The username of this UpdateOracleConnectionDetails.
        :type: str
        """
        self._username = username

    @property
    def password(self):
        """
        Gets the password of this UpdateOracleConnectionDetails.
        The password Oracle GoldenGate uses to connect the associated system of the given technology.
        It must conform to the specific security requirements including length, case sensitivity, and so on.
        Deprecated: This field is deprecated and replaced by \"passwordSecretId\". This field will be removed after February 15 2026.


        :return: The password of this UpdateOracleConnectionDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this UpdateOracleConnectionDetails.
        The password Oracle GoldenGate uses to connect the associated system of the given technology.
        It must conform to the specific security requirements including length, case sensitivity, and so on.
        Deprecated: This field is deprecated and replaced by \"passwordSecretId\". This field will be removed after February 15 2026.


        :param password: The password of this UpdateOracleConnectionDetails.
        :type: str
        """
        self._password = password

    @property
    def password_secret_id(self):
        """
        Gets the password_secret_id of this UpdateOracleConnectionDetails.
        The `OCID`__ of the Secret where the password is stored.
        The password Oracle GoldenGate uses to connect the associated system of the given technology.
        It must conform to the specific security requirements including length, case sensitivity, and so on.
        If secretId is used plaintext field must not be provided.
        Note: When provided, 'password' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The password_secret_id of this UpdateOracleConnectionDetails.
        :rtype: str
        """
        return self._password_secret_id

    @password_secret_id.setter
    def password_secret_id(self, password_secret_id):
        """
        Sets the password_secret_id of this UpdateOracleConnectionDetails.
        The `OCID`__ of the Secret where the password is stored.
        The password Oracle GoldenGate uses to connect the associated system of the given technology.
        It must conform to the specific security requirements including length, case sensitivity, and so on.
        If secretId is used plaintext field must not be provided.
        Note: When provided, 'password' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param password_secret_id: The password_secret_id of this UpdateOracleConnectionDetails.
        :type: str
        """
        self._password_secret_id = password_secret_id

    @property
    def connection_string(self):
        """
        Gets the connection_string of this UpdateOracleConnectionDetails.
        Connect descriptor or Easy Connect Naming method used to connect to a database.


        :return: The connection_string of this UpdateOracleConnectionDetails.
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """
        Sets the connection_string of this UpdateOracleConnectionDetails.
        Connect descriptor or Easy Connect Naming method used to connect to a database.


        :param connection_string: The connection_string of this UpdateOracleConnectionDetails.
        :type: str
        """
        self._connection_string = connection_string

    @property
    def authentication_mode(self):
        """
        Gets the authentication_mode of this UpdateOracleConnectionDetails.
        Authentication mode. It can be provided at creation of Oracle Autonomous Database Serverless connections,
        when a databaseId is provided. The default value is MTLS.


        :return: The authentication_mode of this UpdateOracleConnectionDetails.
        :rtype: str
        """
        return self._authentication_mode

    @authentication_mode.setter
    def authentication_mode(self, authentication_mode):
        """
        Sets the authentication_mode of this UpdateOracleConnectionDetails.
        Authentication mode. It can be provided at creation of Oracle Autonomous Database Serverless connections,
        when a databaseId is provided. The default value is MTLS.


        :param authentication_mode: The authentication_mode of this UpdateOracleConnectionDetails.
        :type: str
        """
        self._authentication_mode = authentication_mode

    @property
    def wallet(self):
        """
        Gets the wallet of this UpdateOracleConnectionDetails.
        The wallet contents Oracle GoldenGate uses to make connections to a database.
        This attribute is expected to be base64 encoded.
        Deprecated: This field is deprecated and replaced by \"walletSecretId\". This field will be removed after February 15 2026.


        :return: The wallet of this UpdateOracleConnectionDetails.
        :rtype: str
        """
        return self._wallet

    @wallet.setter
    def wallet(self, wallet):
        """
        Sets the wallet of this UpdateOracleConnectionDetails.
        The wallet contents Oracle GoldenGate uses to make connections to a database.
        This attribute is expected to be base64 encoded.
        Deprecated: This field is deprecated and replaced by \"walletSecretId\". This field will be removed after February 15 2026.


        :param wallet: The wallet of this UpdateOracleConnectionDetails.
        :type: str
        """
        self._wallet = wallet

    @property
    def wallet_secret_id(self):
        """
        Gets the wallet_secret_id of this UpdateOracleConnectionDetails.
        The `OCID`__ of the Secret where the wallet file is stored.
        The wallet contents Oracle GoldenGate uses to make connections to a database.
        Note: When provided, 'wallet' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The wallet_secret_id of this UpdateOracleConnectionDetails.
        :rtype: str
        """
        return self._wallet_secret_id

    @wallet_secret_id.setter
    def wallet_secret_id(self, wallet_secret_id):
        """
        Sets the wallet_secret_id of this UpdateOracleConnectionDetails.
        The `OCID`__ of the Secret where the wallet file is stored.
        The wallet contents Oracle GoldenGate uses to make connections to a database.
        Note: When provided, 'wallet' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param wallet_secret_id: The wallet_secret_id of this UpdateOracleConnectionDetails.
        :type: str
        """
        self._wallet_secret_id = wallet_secret_id

    @property
    def session_mode(self):
        """
        Gets the session_mode of this UpdateOracleConnectionDetails.
        The mode of the database connection session to be established by the data client.
        'REDIRECT' - for a RAC database, 'DIRECT' - for a non-RAC database.
        Connection to a RAC database involves a redirection received from the SCAN listeners
        to the database node to connect to. By default the mode would be DIRECT.


        :return: The session_mode of this UpdateOracleConnectionDetails.
        :rtype: str
        """
        return self._session_mode

    @session_mode.setter
    def session_mode(self, session_mode):
        """
        Sets the session_mode of this UpdateOracleConnectionDetails.
        The mode of the database connection session to be established by the data client.
        'REDIRECT' - for a RAC database, 'DIRECT' - for a non-RAC database.
        Connection to a RAC database involves a redirection received from the SCAN listeners
        to the database node to connect to. By default the mode would be DIRECT.


        :param session_mode: The session_mode of this UpdateOracleConnectionDetails.
        :type: str
        """
        self._session_mode = session_mode

    @property
    def private_ip(self):
        """
        Gets the private_ip of this UpdateOracleConnectionDetails.
        Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host
        field, or make sure the host name is resolvable in the target VCN.

        The private IP address of the connection's endpoint in the customer's VCN, typically a
        database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
        In case the privateIp is provided, the subnetId must also be provided.
        In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
        In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.


        :return: The private_ip of this UpdateOracleConnectionDetails.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """
        Sets the private_ip of this UpdateOracleConnectionDetails.
        Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host
        field, or make sure the host name is resolvable in the target VCN.

        The private IP address of the connection's endpoint in the customer's VCN, typically a
        database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
        In case the privateIp is provided, the subnetId must also be provided.
        In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
        In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.


        :param private_ip: The private_ip of this UpdateOracleConnectionDetails.
        :type: str
        """
        self._private_ip = private_ip

    @property
    def database_id(self):
        """
        Gets the database_id of this UpdateOracleConnectionDetails.
        The `OCID`__ of the database being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The database_id of this UpdateOracleConnectionDetails.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this UpdateOracleConnectionDetails.
        The `OCID`__ of the database being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param database_id: The database_id of this UpdateOracleConnectionDetails.
        :type: str
        """
        self._database_id = database_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
