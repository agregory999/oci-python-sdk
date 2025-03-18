# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: release


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateEkmsPrivateEndpointDetails(object):
    """
    Information needed to create EKMS private endpoint resource
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateEkmsPrivateEndpointDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateEkmsPrivateEndpointDetails.
        :type subnet_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateEkmsPrivateEndpointDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateEkmsPrivateEndpointDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateEkmsPrivateEndpointDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateEkmsPrivateEndpointDetails.
        :type display_name: str

        :param external_key_manager_ip:
            The value to assign to the external_key_manager_ip property of this CreateEkmsPrivateEndpointDetails.
        :type external_key_manager_ip: str

        :param ca_bundle:
            The value to assign to the ca_bundle property of this CreateEkmsPrivateEndpointDetails.
        :type ca_bundle: str

        :param port:
            The value to assign to the port property of this CreateEkmsPrivateEndpointDetails.
        :type port: int

        """
        self.swagger_types = {
            'subnet_id': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'external_key_manager_ip': 'str',
            'ca_bundle': 'str',
            'port': 'int'
        }
        self.attribute_map = {
            'subnet_id': 'subnetId',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'external_key_manager_ip': 'externalKeyManagerIp',
            'ca_bundle': 'caBundle',
            'port': 'port'
        }
        self._subnet_id = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._display_name = None
        self._external_key_manager_ip = None
        self._ca_bundle = None
        self._port = None

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreateEkmsPrivateEndpointDetails.
        The OCID of subnet in which the EKMS private endpoint is to be created


        :return: The subnet_id of this CreateEkmsPrivateEndpointDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateEkmsPrivateEndpointDetails.
        The OCID of subnet in which the EKMS private endpoint is to be created


        :param subnet_id: The subnet_id of this CreateEkmsPrivateEndpointDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateEkmsPrivateEndpointDetails.
        Compartment identifier.


        :return: The compartment_id of this CreateEkmsPrivateEndpointDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateEkmsPrivateEndpointDetails.
        Compartment identifier.


        :param compartment_id: The compartment_id of this CreateEkmsPrivateEndpointDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateEkmsPrivateEndpointDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateEkmsPrivateEndpointDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateEkmsPrivateEndpointDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateEkmsPrivateEndpointDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateEkmsPrivateEndpointDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateEkmsPrivateEndpointDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateEkmsPrivateEndpointDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateEkmsPrivateEndpointDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateEkmsPrivateEndpointDetails.
        Display name of the EKMS private endpoint resource being created.


        :return: The display_name of this CreateEkmsPrivateEndpointDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateEkmsPrivateEndpointDetails.
        Display name of the EKMS private endpoint resource being created.


        :param display_name: The display_name of this CreateEkmsPrivateEndpointDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def external_key_manager_ip(self):
        """
        **[Required]** Gets the external_key_manager_ip of this CreateEkmsPrivateEndpointDetails.
        External private IP to connect to from this EKMS private endpoint


        :return: The external_key_manager_ip of this CreateEkmsPrivateEndpointDetails.
        :rtype: str
        """
        return self._external_key_manager_ip

    @external_key_manager_ip.setter
    def external_key_manager_ip(self, external_key_manager_ip):
        """
        Sets the external_key_manager_ip of this CreateEkmsPrivateEndpointDetails.
        External private IP to connect to from this EKMS private endpoint


        :param external_key_manager_ip: The external_key_manager_ip of this CreateEkmsPrivateEndpointDetails.
        :type: str
        """
        self._external_key_manager_ip = external_key_manager_ip

    @property
    def ca_bundle(self):
        """
        **[Required]** Gets the ca_bundle of this CreateEkmsPrivateEndpointDetails.
        CABundle to validate TLS certificate of the external key manager system in PEM format


        :return: The ca_bundle of this CreateEkmsPrivateEndpointDetails.
        :rtype: str
        """
        return self._ca_bundle

    @ca_bundle.setter
    def ca_bundle(self, ca_bundle):
        """
        Sets the ca_bundle of this CreateEkmsPrivateEndpointDetails.
        CABundle to validate TLS certificate of the external key manager system in PEM format


        :param ca_bundle: The ca_bundle of this CreateEkmsPrivateEndpointDetails.
        :type: str
        """
        self._ca_bundle = ca_bundle

    @property
    def port(self):
        """
        Gets the port of this CreateEkmsPrivateEndpointDetails.
        The port of the external key manager system


        :return: The port of this CreateEkmsPrivateEndpointDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this CreateEkmsPrivateEndpointDetails.
        The port of the external key manager system


        :param port: The port of this CreateEkmsPrivateEndpointDetails.
        :type: int
        """
        self._port = port

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
