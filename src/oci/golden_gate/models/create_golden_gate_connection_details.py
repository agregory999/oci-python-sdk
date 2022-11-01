# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_connection_details import CreateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateGoldenGateConnectionDetails(CreateConnectionDetails):
    """
    The information about a new GoldenGate Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateGoldenGateConnectionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.CreateGoldenGateConnectionDetails.connection_type` attribute
        of this class is ``GOLDENGATE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this CreateGoldenGateConnectionDetails.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "MYSQL", "OCI_OBJECT_STORAGE", "ORACLE"
        :type connection_type: str

        :param display_name:
            The value to assign to the display_name property of this CreateGoldenGateConnectionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateGoldenGateConnectionDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateGoldenGateConnectionDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateGoldenGateConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateGoldenGateConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param vault_id:
            The value to assign to the vault_id property of this CreateGoldenGateConnectionDetails.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this CreateGoldenGateConnectionDetails.
        :type key_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateGoldenGateConnectionDetails.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateGoldenGateConnectionDetails.
        :type nsg_ids: list[str]

        :param technology_type:
            The value to assign to the technology_type property of this CreateGoldenGateConnectionDetails.
        :type technology_type: str

        :param deployment_id:
            The value to assign to the deployment_id property of this CreateGoldenGateConnectionDetails.
        :type deployment_id: str

        :param host:
            The value to assign to the host property of this CreateGoldenGateConnectionDetails.
        :type host: str

        :param port:
            The value to assign to the port property of this CreateGoldenGateConnectionDetails.
        :type port: int

        :param private_ip:
            The value to assign to the private_ip property of this CreateGoldenGateConnectionDetails.
        :type private_ip: str

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
            'technology_type': 'str',
            'deployment_id': 'str',
            'host': 'str',
            'port': 'int',
            'private_ip': 'str'
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
            'technology_type': 'technologyType',
            'deployment_id': 'deploymentId',
            'host': 'host',
            'port': 'port',
            'private_ip': 'privateIp'
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
        self._technology_type = None
        self._deployment_id = None
        self._host = None
        self._port = None
        self._private_ip = None
        self._connection_type = 'GOLDENGATE'

    @property
    def technology_type(self):
        """
        **[Required]** Gets the technology_type of this CreateGoldenGateConnectionDetails.
        The GoldenGate technology type.


        :return: The technology_type of this CreateGoldenGateConnectionDetails.
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """
        Sets the technology_type of this CreateGoldenGateConnectionDetails.
        The GoldenGate technology type.


        :param technology_type: The technology_type of this CreateGoldenGateConnectionDetails.
        :type: str
        """
        self._technology_type = technology_type

    @property
    def deployment_id(self):
        """
        Gets the deployment_id of this CreateGoldenGateConnectionDetails.
        The `OCID`__ of the deployment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The deployment_id of this CreateGoldenGateConnectionDetails.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """
        Sets the deployment_id of this CreateGoldenGateConnectionDetails.
        The `OCID`__ of the deployment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param deployment_id: The deployment_id of this CreateGoldenGateConnectionDetails.
        :type: str
        """
        self._deployment_id = deployment_id

    @property
    def host(self):
        """
        Gets the host of this CreateGoldenGateConnectionDetails.
        The name or address of a host.


        :return: The host of this CreateGoldenGateConnectionDetails.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this CreateGoldenGateConnectionDetails.
        The name or address of a host.


        :param host: The host of this CreateGoldenGateConnectionDetails.
        :type: str
        """
        self._host = host

    @property
    def port(self):
        """
        Gets the port of this CreateGoldenGateConnectionDetails.
        The port of an endpoint usually specified for a connection.


        :return: The port of this CreateGoldenGateConnectionDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this CreateGoldenGateConnectionDetails.
        The port of an endpoint usually specified for a connection.


        :param port: The port of this CreateGoldenGateConnectionDetails.
        :type: int
        """
        self._port = port

    @property
    def private_ip(self):
        """
        Gets the private_ip of this CreateGoldenGateConnectionDetails.
        The private IP address of the connection's endpoint in the customer's VCN, typically a
        database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
        In case the privateIp is provided, the subnetId must also be provided.
        In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
        In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.


        :return: The private_ip of this CreateGoldenGateConnectionDetails.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """
        Sets the private_ip of this CreateGoldenGateConnectionDetails.
        The private IP address of the connection's endpoint in the customer's VCN, typically a
        database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
        In case the privateIp is provided, the subnetId must also be provided.
        In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
        In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.


        :param private_ip: The private_ip of this CreateGoldenGateConnectionDetails.
        :type: str
        """
        self._private_ip = private_ip

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
