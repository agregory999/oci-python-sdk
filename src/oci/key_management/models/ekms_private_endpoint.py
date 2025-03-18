# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: release


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EkmsPrivateEndpoint(object):
    """
    EKMS private endpoint created in customer subnet used to connect to external key manager system
    """

    #: A constant which can be used with the lifecycle_state property of a EkmsPrivateEndpoint.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a EkmsPrivateEndpoint.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a EkmsPrivateEndpoint.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a EkmsPrivateEndpoint.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a EkmsPrivateEndpoint.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new EkmsPrivateEndpoint object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this EkmsPrivateEndpoint.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this EkmsPrivateEndpoint.
        :type compartment_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this EkmsPrivateEndpoint.
        :type subnet_id: str

        :param display_name:
            The value to assign to the display_name property of this EkmsPrivateEndpoint.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this EkmsPrivateEndpoint.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this EkmsPrivateEndpoint.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this EkmsPrivateEndpoint.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this EkmsPrivateEndpoint.
        :type defined_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this EkmsPrivateEndpoint.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this EkmsPrivateEndpoint.
        :type lifecycle_details: str

        :param external_key_manager_ip:
            The value to assign to the external_key_manager_ip property of this EkmsPrivateEndpoint.
        :type external_key_manager_ip: str

        :param port:
            The value to assign to the port property of this EkmsPrivateEndpoint.
        :type port: int

        :param ca_bundle:
            The value to assign to the ca_bundle property of this EkmsPrivateEndpoint.
        :type ca_bundle: str

        :param private_endpoint_ip:
            The value to assign to the private_endpoint_ip property of this EkmsPrivateEndpoint.
        :type private_endpoint_ip: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'subnet_id': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'external_key_manager_ip': 'str',
            'port': 'int',
            'ca_bundle': 'str',
            'private_endpoint_ip': 'str'
        }
        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'subnet_id': 'subnetId',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'external_key_manager_ip': 'externalKeyManagerIp',
            'port': 'port',
            'ca_bundle': 'caBundle',
            'private_endpoint_ip': 'privateEndpointIp'
        }
        self._id = None
        self._compartment_id = None
        self._subnet_id = None
        self._display_name = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._external_key_manager_ip = None
        self._port = None
        self._ca_bundle = None
        self._private_endpoint_ip = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this EkmsPrivateEndpoint.
        Unique identifier that is immutable


        :return: The id of this EkmsPrivateEndpoint.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EkmsPrivateEndpoint.
        Unique identifier that is immutable


        :param id: The id of this EkmsPrivateEndpoint.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this EkmsPrivateEndpoint.
        Compartment Identifier.


        :return: The compartment_id of this EkmsPrivateEndpoint.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this EkmsPrivateEndpoint.
        Compartment Identifier.


        :param compartment_id: The compartment_id of this EkmsPrivateEndpoint.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this EkmsPrivateEndpoint.
        Subnet Identifier


        :return: The subnet_id of this EkmsPrivateEndpoint.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this EkmsPrivateEndpoint.
        Subnet Identifier


        :param subnet_id: The subnet_id of this EkmsPrivateEndpoint.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this EkmsPrivateEndpoint.
        EKMS Private Endpoint display name


        :return: The display_name of this EkmsPrivateEndpoint.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this EkmsPrivateEndpoint.
        EKMS Private Endpoint display name


        :param display_name: The display_name of this EkmsPrivateEndpoint.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this EkmsPrivateEndpoint.
        The time the EKMS private endpoint was created. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this EkmsPrivateEndpoint.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this EkmsPrivateEndpoint.
        The time the EKMS private endpoint was created. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this EkmsPrivateEndpoint.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this EkmsPrivateEndpoint.
        The time the EKMS private endpoint was updated. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this EkmsPrivateEndpoint.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this EkmsPrivateEndpoint.
        The time the EKMS private endpoint was updated. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this EkmsPrivateEndpoint.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this EkmsPrivateEndpoint.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this EkmsPrivateEndpoint.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this EkmsPrivateEndpoint.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this EkmsPrivateEndpoint.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this EkmsPrivateEndpoint.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this EkmsPrivateEndpoint.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this EkmsPrivateEndpoint.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this EkmsPrivateEndpoint.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this EkmsPrivateEndpoint.
        The current state of the EKMS private endpoint resource.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this EkmsPrivateEndpoint.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this EkmsPrivateEndpoint.
        The current state of the EKMS private endpoint resource.


        :param lifecycle_state: The lifecycle_state of this EkmsPrivateEndpoint.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this EkmsPrivateEndpoint.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in 'Failed' state.


        :return: The lifecycle_details of this EkmsPrivateEndpoint.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this EkmsPrivateEndpoint.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in 'Failed' state.


        :param lifecycle_details: The lifecycle_details of this EkmsPrivateEndpoint.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def external_key_manager_ip(self):
        """
        **[Required]** Gets the external_key_manager_ip of this EkmsPrivateEndpoint.
        Private IP of the external key manager system to connect to from the EKMS private endpoint


        :return: The external_key_manager_ip of this EkmsPrivateEndpoint.
        :rtype: str
        """
        return self._external_key_manager_ip

    @external_key_manager_ip.setter
    def external_key_manager_ip(self, external_key_manager_ip):
        """
        Sets the external_key_manager_ip of this EkmsPrivateEndpoint.
        Private IP of the external key manager system to connect to from the EKMS private endpoint


        :param external_key_manager_ip: The external_key_manager_ip of this EkmsPrivateEndpoint.
        :type: str
        """
        self._external_key_manager_ip = external_key_manager_ip

    @property
    def port(self):
        """
        Gets the port of this EkmsPrivateEndpoint.
        The port of the external key manager system


        :return: The port of this EkmsPrivateEndpoint.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this EkmsPrivateEndpoint.
        The port of the external key manager system


        :param port: The port of this EkmsPrivateEndpoint.
        :type: int
        """
        self._port = port

    @property
    def ca_bundle(self):
        """
        Gets the ca_bundle of this EkmsPrivateEndpoint.
        CABundle to validate TLS certificate of the external key manager system in PEM format


        :return: The ca_bundle of this EkmsPrivateEndpoint.
        :rtype: str
        """
        return self._ca_bundle

    @ca_bundle.setter
    def ca_bundle(self, ca_bundle):
        """
        Sets the ca_bundle of this EkmsPrivateEndpoint.
        CABundle to validate TLS certificate of the external key manager system in PEM format


        :param ca_bundle: The ca_bundle of this EkmsPrivateEndpoint.
        :type: str
        """
        self._ca_bundle = ca_bundle

    @property
    def private_endpoint_ip(self):
        """
        Gets the private_endpoint_ip of this EkmsPrivateEndpoint.
        The IP address in the customer's VCN for the EKMS private endpoint. This is taken from subnet


        :return: The private_endpoint_ip of this EkmsPrivateEndpoint.
        :rtype: str
        """
        return self._private_endpoint_ip

    @private_endpoint_ip.setter
    def private_endpoint_ip(self, private_endpoint_ip):
        """
        Sets the private_endpoint_ip of this EkmsPrivateEndpoint.
        The IP address in the customer's VCN for the EKMS private endpoint. This is taken from subnet


        :param private_endpoint_ip: The private_endpoint_ip of this EkmsPrivateEndpoint.
        :type: str
        """
        self._private_endpoint_ip = private_endpoint_ip

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
