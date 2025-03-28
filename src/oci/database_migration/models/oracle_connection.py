# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230518

from .connection import Connection
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OracleConnection(Connection):
    """
    Represents the metadata of an Oracle Database Connection.
    """

    #: A constant which can be used with the technology_type property of a OracleConnection.
    #: This constant has a value of "AMAZON_RDS_ORACLE"
    TECHNOLOGY_TYPE_AMAZON_RDS_ORACLE = "AMAZON_RDS_ORACLE"

    #: A constant which can be used with the technology_type property of a OracleConnection.
    #: This constant has a value of "OCI_AUTONOMOUS_DATABASE"
    TECHNOLOGY_TYPE_OCI_AUTONOMOUS_DATABASE = "OCI_AUTONOMOUS_DATABASE"

    #: A constant which can be used with the technology_type property of a OracleConnection.
    #: This constant has a value of "ORACLE_DATABASE"
    TECHNOLOGY_TYPE_ORACLE_DATABASE = "ORACLE_DATABASE"

    #: A constant which can be used with the technology_type property of a OracleConnection.
    #: This constant has a value of "ORACLE_EXADATA"
    TECHNOLOGY_TYPE_ORACLE_EXADATA = "ORACLE_EXADATA"

    def __init__(self, **kwargs):
        """
        Initializes a new OracleConnection object with values from keyword arguments. The default value of the :py:attr:`~oci.database_migration.models.OracleConnection.connection_type` attribute
        of this class is ``ORACLE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this OracleConnection.
            Allowed values for this property are: "MYSQL", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type connection_type: str

        :param id:
            The value to assign to the id property of this OracleConnection.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this OracleConnection.
        :type display_name: str

        :param description:
            The value to assign to the description property of this OracleConnection.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OracleConnection.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OracleConnection.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OracleConnection.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this OracleConnection.
        :type system_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OracleConnection.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this OracleConnection.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this OracleConnection.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OracleConnection.
        :type time_updated: datetime

        :param vault_id:
            The value to assign to the vault_id property of this OracleConnection.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this OracleConnection.
        :type key_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this OracleConnection.
        :type subnet_id: str

        :param ingress_ips:
            The value to assign to the ingress_ips property of this OracleConnection.
        :type ingress_ips: list[oci.database_migration.models.IngressIpDetails]

        :param nsg_ids:
            The value to assign to the nsg_ids property of this OracleConnection.
        :type nsg_ids: list[str]

        :param username:
            The value to assign to the username property of this OracleConnection.
        :type username: str

        :param password:
            The value to assign to the password property of this OracleConnection.
        :type password: str

        :param replication_username:
            The value to assign to the replication_username property of this OracleConnection.
        :type replication_username: str

        :param replication_password:
            The value to assign to the replication_password property of this OracleConnection.
        :type replication_password: str

        :param secret_id:
            The value to assign to the secret_id property of this OracleConnection.
        :type secret_id: str

        :param private_endpoint_id:
            The value to assign to the private_endpoint_id property of this OracleConnection.
        :type private_endpoint_id: str

        :param technology_type:
            The value to assign to the technology_type property of this OracleConnection.
            Allowed values for this property are: "AMAZON_RDS_ORACLE", "OCI_AUTONOMOUS_DATABASE", "ORACLE_DATABASE", "ORACLE_EXADATA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type technology_type: str

        :param connection_string:
            The value to assign to the connection_string property of this OracleConnection.
        :type connection_string: str

        :param database_id:
            The value to assign to the database_id property of this OracleConnection.
        :type database_id: str

        :param ssh_host:
            The value to assign to the ssh_host property of this OracleConnection.
        :type ssh_host: str

        :param ssh_key:
            The value to assign to the ssh_key property of this OracleConnection.
        :type ssh_key: str

        :param ssh_user:
            The value to assign to the ssh_user property of this OracleConnection.
        :type ssh_user: str

        :param ssh_sudo_location:
            The value to assign to the ssh_sudo_location property of this OracleConnection.
        :type ssh_sudo_location: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'vault_id': 'str',
            'key_id': 'str',
            'subnet_id': 'str',
            'ingress_ips': 'list[IngressIpDetails]',
            'nsg_ids': 'list[str]',
            'username': 'str',
            'password': 'str',
            'replication_username': 'str',
            'replication_password': 'str',
            'secret_id': 'str',
            'private_endpoint_id': 'str',
            'technology_type': 'str',
            'connection_string': 'str',
            'database_id': 'str',
            'ssh_host': 'str',
            'ssh_key': 'str',
            'ssh_user': 'str',
            'ssh_sudo_location': 'str'
        }
        self.attribute_map = {
            'connection_type': 'connectionType',
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'subnet_id': 'subnetId',
            'ingress_ips': 'ingressIps',
            'nsg_ids': 'nsgIds',
            'username': 'username',
            'password': 'password',
            'replication_username': 'replicationUsername',
            'replication_password': 'replicationPassword',
            'secret_id': 'secretId',
            'private_endpoint_id': 'privateEndpointId',
            'technology_type': 'technologyType',
            'connection_string': 'connectionString',
            'database_id': 'databaseId',
            'ssh_host': 'sshHost',
            'ssh_key': 'sshKey',
            'ssh_user': 'sshUser',
            'ssh_sudo_location': 'sshSudoLocation'
        }
        self._connection_type = None
        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._vault_id = None
        self._key_id = None
        self._subnet_id = None
        self._ingress_ips = None
        self._nsg_ids = None
        self._username = None
        self._password = None
        self._replication_username = None
        self._replication_password = None
        self._secret_id = None
        self._private_endpoint_id = None
        self._technology_type = None
        self._connection_string = None
        self._database_id = None
        self._ssh_host = None
        self._ssh_key = None
        self._ssh_user = None
        self._ssh_sudo_location = None
        self._connection_type = 'ORACLE'

    @property
    def technology_type(self):
        """
        **[Required]** Gets the technology_type of this OracleConnection.
        The Oracle technology type.

        Allowed values for this property are: "AMAZON_RDS_ORACLE", "OCI_AUTONOMOUS_DATABASE", "ORACLE_DATABASE", "ORACLE_EXADATA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The technology_type of this OracleConnection.
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """
        Sets the technology_type of this OracleConnection.
        The Oracle technology type.


        :param technology_type: The technology_type of this OracleConnection.
        :type: str
        """
        allowed_values = ["AMAZON_RDS_ORACLE", "OCI_AUTONOMOUS_DATABASE", "ORACLE_DATABASE", "ORACLE_EXADATA"]
        if not value_allowed_none_or_none_sentinel(technology_type, allowed_values):
            technology_type = 'UNKNOWN_ENUM_VALUE'
        self._technology_type = technology_type

    @property
    def connection_string(self):
        """
        Gets the connection_string of this OracleConnection.
        Connect descriptor or Easy Connect Naming method used to connect to a database.


        :return: The connection_string of this OracleConnection.
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """
        Sets the connection_string of this OracleConnection.
        Connect descriptor or Easy Connect Naming method used to connect to a database.


        :param connection_string: The connection_string of this OracleConnection.
        :type: str
        """
        self._connection_string = connection_string

    @property
    def database_id(self):
        """
        Gets the database_id of this OracleConnection.
        The OCID of the database being referenced.


        :return: The database_id of this OracleConnection.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this OracleConnection.
        The OCID of the database being referenced.


        :param database_id: The database_id of this OracleConnection.
        :type: str
        """
        self._database_id = database_id

    @property
    def ssh_host(self):
        """
        Gets the ssh_host of this OracleConnection.
        Name of the host the SSH key is valid for.


        :return: The ssh_host of this OracleConnection.
        :rtype: str
        """
        return self._ssh_host

    @ssh_host.setter
    def ssh_host(self, ssh_host):
        """
        Sets the ssh_host of this OracleConnection.
        Name of the host the SSH key is valid for.


        :param ssh_host: The ssh_host of this OracleConnection.
        :type: str
        """
        self._ssh_host = ssh_host

    @property
    def ssh_key(self):
        """
        Gets the ssh_key of this OracleConnection.
        Private SSH key string.


        :return: The ssh_key of this OracleConnection.
        :rtype: str
        """
        return self._ssh_key

    @ssh_key.setter
    def ssh_key(self, ssh_key):
        """
        Sets the ssh_key of this OracleConnection.
        Private SSH key string.


        :param ssh_key: The ssh_key of this OracleConnection.
        :type: str
        """
        self._ssh_key = ssh_key

    @property
    def ssh_user(self):
        """
        Gets the ssh_user of this OracleConnection.
        The username (credential) used when creating or updating this resource.


        :return: The ssh_user of this OracleConnection.
        :rtype: str
        """
        return self._ssh_user

    @ssh_user.setter
    def ssh_user(self, ssh_user):
        """
        Sets the ssh_user of this OracleConnection.
        The username (credential) used when creating or updating this resource.


        :param ssh_user: The ssh_user of this OracleConnection.
        :type: str
        """
        self._ssh_user = ssh_user

    @property
    def ssh_sudo_location(self):
        """
        Gets the ssh_sudo_location of this OracleConnection.
        Sudo location


        :return: The ssh_sudo_location of this OracleConnection.
        :rtype: str
        """
        return self._ssh_sudo_location

    @ssh_sudo_location.setter
    def ssh_sudo_location(self, ssh_sudo_location):
        """
        Sets the ssh_sudo_location of this OracleConnection.
        Sudo location


        :param ssh_sudo_location: The ssh_sudo_location of this OracleConnection.
        :type: str
        """
        self._ssh_sudo_location = ssh_sudo_location

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
