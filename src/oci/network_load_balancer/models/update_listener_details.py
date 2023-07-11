# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateListenerDetails(object):
    """
    The configuration of the listener.
    For more information about backend set configuration, see
    `Managing Network Load Balancer Listeners`__.

    __ https://docs.cloud.oracle.com/Content/Balance/Tasks/managinglisteners.htm
    """

    #: A constant which can be used with the protocol property of a UpdateListenerDetails.
    #: This constant has a value of "ANY"
    PROTOCOL_ANY = "ANY"

    #: A constant which can be used with the protocol property of a UpdateListenerDetails.
    #: This constant has a value of "TCP"
    PROTOCOL_TCP = "TCP"

    #: A constant which can be used with the protocol property of a UpdateListenerDetails.
    #: This constant has a value of "UDP"
    PROTOCOL_UDP = "UDP"

    #: A constant which can be used with the protocol property of a UpdateListenerDetails.
    #: This constant has a value of "TCP_AND_UDP"
    PROTOCOL_TCP_AND_UDP = "TCP_AND_UDP"

    #: A constant which can be used with the ip_version property of a UpdateListenerDetails.
    #: This constant has a value of "IPV4"
    IP_VERSION_IPV4 = "IPV4"

    #: A constant which can be used with the ip_version property of a UpdateListenerDetails.
    #: This constant has a value of "IPV6"
    IP_VERSION_IPV6 = "IPV6"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateListenerDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param default_backend_set_name:
            The value to assign to the default_backend_set_name property of this UpdateListenerDetails.
        :type default_backend_set_name: str

        :param port:
            The value to assign to the port property of this UpdateListenerDetails.
        :type port: int

        :param protocol:
            The value to assign to the protocol property of this UpdateListenerDetails.
            Allowed values for this property are: "ANY", "TCP", "UDP", "TCP_AND_UDP"
        :type protocol: str

        :param ip_version:
            The value to assign to the ip_version property of this UpdateListenerDetails.
            Allowed values for this property are: "IPV4", "IPV6"
        :type ip_version: str

        """
        self.swagger_types = {
            'default_backend_set_name': 'str',
            'port': 'int',
            'protocol': 'str',
            'ip_version': 'str'
        }

        self.attribute_map = {
            'default_backend_set_name': 'defaultBackendSetName',
            'port': 'port',
            'protocol': 'protocol',
            'ip_version': 'ipVersion'
        }

        self._default_backend_set_name = None
        self._port = None
        self._protocol = None
        self._ip_version = None

    @property
    def default_backend_set_name(self):
        """
        Gets the default_backend_set_name of this UpdateListenerDetails.
        The name of the associated backend set.

        Example: `example_backend_set`


        :return: The default_backend_set_name of this UpdateListenerDetails.
        :rtype: str
        """
        return self._default_backend_set_name

    @default_backend_set_name.setter
    def default_backend_set_name(self, default_backend_set_name):
        """
        Sets the default_backend_set_name of this UpdateListenerDetails.
        The name of the associated backend set.

        Example: `example_backend_set`


        :param default_backend_set_name: The default_backend_set_name of this UpdateListenerDetails.
        :type: str
        """
        self._default_backend_set_name = default_backend_set_name

    @property
    def port(self):
        """
        Gets the port of this UpdateListenerDetails.
        The communication port for the listener.

        Example: `80`


        :return: The port of this UpdateListenerDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this UpdateListenerDetails.
        The communication port for the listener.

        Example: `80`


        :param port: The port of this UpdateListenerDetails.
        :type: int
        """
        self._port = port

    @property
    def protocol(self):
        """
        Gets the protocol of this UpdateListenerDetails.
        The protocol on which the listener accepts connection requests.
        For public network load balancers, ANY protocol refers to TCP/UDP.
        For private network load balancers, ANY protocol refers to TCP/UDP/ICMP (note that ICMP requires isPreserveSourceDestination to be set to true).
        To get a list of valid protocols, use the :func:`list_network_load_balancers_protocols`
        operation.

        Example: `TCP`

        Allowed values for this property are: "ANY", "TCP", "UDP", "TCP_AND_UDP"


        :return: The protocol of this UpdateListenerDetails.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this UpdateListenerDetails.
        The protocol on which the listener accepts connection requests.
        For public network load balancers, ANY protocol refers to TCP/UDP.
        For private network load balancers, ANY protocol refers to TCP/UDP/ICMP (note that ICMP requires isPreserveSourceDestination to be set to true).
        To get a list of valid protocols, use the :func:`list_network_load_balancers_protocols`
        operation.

        Example: `TCP`


        :param protocol: The protocol of this UpdateListenerDetails.
        :type: str
        """
        allowed_values = ["ANY", "TCP", "UDP", "TCP_AND_UDP"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            raise ValueError(
                "Invalid value for `protocol`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._protocol = protocol

    @property
    def ip_version(self):
        """
        Gets the ip_version of this UpdateListenerDetails.
        IP version associated with the listener.

        Allowed values for this property are: "IPV4", "IPV6"


        :return: The ip_version of this UpdateListenerDetails.
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """
        Sets the ip_version of this UpdateListenerDetails.
        IP version associated with the listener.


        :param ip_version: The ip_version of this UpdateListenerDetails.
        :type: str
        """
        allowed_values = ["IPV4", "IPV6"]
        if not value_allowed_none_or_none_sentinel(ip_version, allowed_values):
            raise ValueError(
                "Invalid value for `ip_version`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._ip_version = ip_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
