# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230518

from .create_connection_details import CreateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOracleConnectionDetails(CreateConnectionDetails):
    """
    The information about a new Oracle Database Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOracleConnectionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_migration.models.CreateOracleConnectionDetails.connection_type` attribute
        of this class is ``ORACLE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this CreateOracleConnectionDetails.
            Allowed values for this property are: "MYSQL", "ORACLE"
        :type connection_type: str

        :param display_name:
            The value to assign to the display_name property of this CreateOracleConnectionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateOracleConnectionDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateOracleConnectionDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateOracleConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateOracleConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param vault_id:
            The value to assign to the vault_id property of this CreateOracleConnectionDetails.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this CreateOracleConnectionDetails.
        :type key_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateOracleConnectionDetails.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateOracleConnectionDetails.
        :type nsg_ids: list[str]

        :param username:
            The value to assign to the username property of this CreateOracleConnectionDetails.
        :type username: str

        :param password:
            The value to assign to the password property of this CreateOracleConnectionDetails.
        :type password: str

        :param replication_username:
            The value to assign to the replication_username property of this CreateOracleConnectionDetails.
        :type replication_username: str

        :param replication_password:
            The value to assign to the replication_password property of this CreateOracleConnectionDetails.
        :type replication_password: str

        :param technology_type:
            The value to assign to the technology_type property of this CreateOracleConnectionDetails.
        :type technology_type: str

        :param connection_string:
            The value to assign to the connection_string property of this CreateOracleConnectionDetails.
        :type connection_string: str

        :param wallet:
            The value to assign to the wallet property of this CreateOracleConnectionDetails.
        :type wallet: str

        :param database_id:
            The value to assign to the database_id property of this CreateOracleConnectionDetails.
        :type database_id: str

        :param ssh_host:
            The value to assign to the ssh_host property of this CreateOracleConnectionDetails.
        :type ssh_host: str

        :param ssh_key:
            The value to assign to the ssh_key property of this CreateOracleConnectionDetails.
        :type ssh_key: str

        :param ssh_user:
            The value to assign to the ssh_user property of this CreateOracleConnectionDetails.
        :type ssh_user: str

        :param ssh_sudo_location:
            The value to assign to the ssh_sudo_location property of this CreateOracleConnectionDetails.
        :type ssh_sudo_location: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'vault_id': 'str',
            'key_id': 'str',
            'subnet_id': 'str',
            'nsg_ids': 'list[str]',
            'username': 'str',
            'password': 'str',
            'replication_username': 'str',
            'replication_password': 'str',
            'technology_type': 'str',
            'connection_string': 'str',
            'wallet': 'str',
            'database_id': 'str',
            'ssh_host': 'str',
            'ssh_key': 'str',
            'ssh_user': 'str',
            'ssh_sudo_location': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'subnet_id': 'subnetId',
            'nsg_ids': 'nsgIds',
            'username': 'username',
            'password': 'password',
            'replication_username': 'replicationUsername',
            'replication_password': 'replicationPassword',
            'technology_type': 'technologyType',
            'connection_string': 'connectionString',
            'wallet': 'wallet',
            'database_id': 'databaseId',
            'ssh_host': 'sshHost',
            'ssh_key': 'sshKey',
            'ssh_user': 'sshUser',
            'ssh_sudo_location': 'sshSudoLocation'
        }

        self._connection_type = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._vault_id = None
        self._key_id = None
        self._subnet_id = None
        self._nsg_ids = None
        self._username = None
        self._password = None
        self._replication_username = None
        self._replication_password = None
        self._technology_type = None
        self._connection_string = None
        self._wallet = None
        self._database_id = None
        self._ssh_host = None
        self._ssh_key = None
        self._ssh_user = None
        self._ssh_sudo_location = None
        self._connection_type = 'ORACLE'

    @property
    def technology_type(self):
        """
        **[Required]** Gets the technology_type of this CreateOracleConnectionDetails.
        The Oracle technology type.


        :return: The technology_type of this CreateOracleConnectionDetails.
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """
        Sets the technology_type of this CreateOracleConnectionDetails.
        The Oracle technology type.


        :param technology_type: The technology_type of this CreateOracleConnectionDetails.
        :type: str
        """
        self._technology_type = technology_type

    @property
    def connection_string(self):
        """
        Gets the connection_string of this CreateOracleConnectionDetails.
        Connect descriptor or Easy Connect Naming method used to connect to a database.


        :return: The connection_string of this CreateOracleConnectionDetails.
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """
        Sets the connection_string of this CreateOracleConnectionDetails.
        Connect descriptor or Easy Connect Naming method used to connect to a database.


        :param connection_string: The connection_string of this CreateOracleConnectionDetails.
        :type: str
        """
        self._connection_string = connection_string

    @property
    def wallet(self):
        """
        Gets the wallet of this CreateOracleConnectionDetails.
        The wallet contents used to make connections to a database.  This
        attribute is expected to be base64 encoded.


        :return: The wallet of this CreateOracleConnectionDetails.
        :rtype: str
        """
        return self._wallet

    @wallet.setter
    def wallet(self, wallet):
        """
        Sets the wallet of this CreateOracleConnectionDetails.
        The wallet contents used to make connections to a database.  This
        attribute is expected to be base64 encoded.


        :param wallet: The wallet of this CreateOracleConnectionDetails.
        :type: str
        """
        self._wallet = wallet

    @property
    def database_id(self):
        """
        Gets the database_id of this CreateOracleConnectionDetails.
        The OCID of the database being referenced.


        :return: The database_id of this CreateOracleConnectionDetails.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this CreateOracleConnectionDetails.
        The OCID of the database being referenced.


        :param database_id: The database_id of this CreateOracleConnectionDetails.
        :type: str
        """
        self._database_id = database_id

    @property
    def ssh_host(self):
        """
        Gets the ssh_host of this CreateOracleConnectionDetails.
        Name of the host the SSH key is valid for.


        :return: The ssh_host of this CreateOracleConnectionDetails.
        :rtype: str
        """
        return self._ssh_host

    @ssh_host.setter
    def ssh_host(self, ssh_host):
        """
        Sets the ssh_host of this CreateOracleConnectionDetails.
        Name of the host the SSH key is valid for.


        :param ssh_host: The ssh_host of this CreateOracleConnectionDetails.
        :type: str
        """
        self._ssh_host = ssh_host

    @property
    def ssh_key(self):
        """
        Gets the ssh_key of this CreateOracleConnectionDetails.
        Private SSH key string.


        :return: The ssh_key of this CreateOracleConnectionDetails.
        :rtype: str
        """
        return self._ssh_key

    @ssh_key.setter
    def ssh_key(self, ssh_key):
        """
        Sets the ssh_key of this CreateOracleConnectionDetails.
        Private SSH key string.


        :param ssh_key: The ssh_key of this CreateOracleConnectionDetails.
        :type: str
        """
        self._ssh_key = ssh_key

    @property
    def ssh_user(self):
        """
        Gets the ssh_user of this CreateOracleConnectionDetails.
        The username (credential) used when creating or updating this resource.


        :return: The ssh_user of this CreateOracleConnectionDetails.
        :rtype: str
        """
        return self._ssh_user

    @ssh_user.setter
    def ssh_user(self, ssh_user):
        """
        Sets the ssh_user of this CreateOracleConnectionDetails.
        The username (credential) used when creating or updating this resource.


        :param ssh_user: The ssh_user of this CreateOracleConnectionDetails.
        :type: str
        """
        self._ssh_user = ssh_user

    @property
    def ssh_sudo_location(self):
        """
        Gets the ssh_sudo_location of this CreateOracleConnectionDetails.
        Sudo location


        :return: The ssh_sudo_location of this CreateOracleConnectionDetails.
        :rtype: str
        """
        return self._ssh_sudo_location

    @ssh_sudo_location.setter
    def ssh_sudo_location(self, ssh_sudo_location):
        """
        Sets the ssh_sudo_location of this CreateOracleConnectionDetails.
        Sudo location


        :param ssh_sudo_location: The ssh_sudo_location of this CreateOracleConnectionDetails.
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