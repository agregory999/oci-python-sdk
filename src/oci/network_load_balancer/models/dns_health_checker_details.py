# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DnsHealthCheckerDetails(object):
    """
    DNS healthcheck configurations.
    """

    #: A constant which can be used with the transport_protocol property of a DnsHealthCheckerDetails.
    #: This constant has a value of "UDP"
    TRANSPORT_PROTOCOL_UDP = "UDP"

    #: A constant which can be used with the transport_protocol property of a DnsHealthCheckerDetails.
    #: This constant has a value of "TCP"
    TRANSPORT_PROTOCOL_TCP = "TCP"

    #: A constant which can be used with the query_class property of a DnsHealthCheckerDetails.
    #: This constant has a value of "IN"
    QUERY_CLASS_IN = "IN"

    #: A constant which can be used with the query_class property of a DnsHealthCheckerDetails.
    #: This constant has a value of "CH"
    QUERY_CLASS_CH = "CH"

    #: A constant which can be used with the query_type property of a DnsHealthCheckerDetails.
    #: This constant has a value of "A"
    QUERY_TYPE_A = "A"

    #: A constant which can be used with the query_type property of a DnsHealthCheckerDetails.
    #: This constant has a value of "TXT"
    QUERY_TYPE_TXT = "TXT"

    #: A constant which can be used with the query_type property of a DnsHealthCheckerDetails.
    #: This constant has a value of "AAAA"
    QUERY_TYPE_AAAA = "AAAA"

    def __init__(self, **kwargs):
        """
        Initializes a new DnsHealthCheckerDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param transport_protocol:
            The value to assign to the transport_protocol property of this DnsHealthCheckerDetails.
            Allowed values for this property are: "UDP", "TCP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type transport_protocol: str

        :param domain_name:
            The value to assign to the domain_name property of this DnsHealthCheckerDetails.
        :type domain_name: str

        :param query_class:
            The value to assign to the query_class property of this DnsHealthCheckerDetails.
            Allowed values for this property are: "IN", "CH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type query_class: str

        :param query_type:
            The value to assign to the query_type property of this DnsHealthCheckerDetails.
            Allowed values for this property are: "A", "TXT", "AAAA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type query_type: str

        :param rcodes:
            The value to assign to the rcodes property of this DnsHealthCheckerDetails.
        :type rcodes: list[oci.network_load_balancer.models.DnsHealthCheckRCodes]

        """
        self.swagger_types = {
            'transport_protocol': 'str',
            'domain_name': 'str',
            'query_class': 'str',
            'query_type': 'str',
            'rcodes': 'list[DnsHealthCheckRCodes]'
        }
        self.attribute_map = {
            'transport_protocol': 'transportProtocol',
            'domain_name': 'domainName',
            'query_class': 'queryClass',
            'query_type': 'queryType',
            'rcodes': 'rcodes'
        }
        self._transport_protocol = None
        self._domain_name = None
        self._query_class = None
        self._query_type = None
        self._rcodes = None

    @property
    def transport_protocol(self):
        """
        Gets the transport_protocol of this DnsHealthCheckerDetails.
        DNS transport protocol; either UDP or TCP.

        Example: `UDP`

        Allowed values for this property are: "UDP", "TCP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The transport_protocol of this DnsHealthCheckerDetails.
        :rtype: str
        """
        return self._transport_protocol

    @transport_protocol.setter
    def transport_protocol(self, transport_protocol):
        """
        Sets the transport_protocol of this DnsHealthCheckerDetails.
        DNS transport protocol; either UDP or TCP.

        Example: `UDP`


        :param transport_protocol: The transport_protocol of this DnsHealthCheckerDetails.
        :type: str
        """
        allowed_values = ["UDP", "TCP"]
        if not value_allowed_none_or_none_sentinel(transport_protocol, allowed_values):
            transport_protocol = 'UNKNOWN_ENUM_VALUE'
        self._transport_protocol = transport_protocol

    @property
    def domain_name(self):
        """
        **[Required]** Gets the domain_name of this DnsHealthCheckerDetails.
        The absolute fully-qualified domain name to perform periodic DNS queries.
        If not provided, an extra dot will be added at the end of a domain name during the query.


        :return: The domain_name of this DnsHealthCheckerDetails.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """
        Sets the domain_name of this DnsHealthCheckerDetails.
        The absolute fully-qualified domain name to perform periodic DNS queries.
        If not provided, an extra dot will be added at the end of a domain name during the query.


        :param domain_name: The domain_name of this DnsHealthCheckerDetails.
        :type: str
        """
        self._domain_name = domain_name

    @property
    def query_class(self):
        """
        Gets the query_class of this DnsHealthCheckerDetails.
        The class the dns health check query to use; either IN or CH.

        Example: `IN`

        Allowed values for this property are: "IN", "CH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The query_class of this DnsHealthCheckerDetails.
        :rtype: str
        """
        return self._query_class

    @query_class.setter
    def query_class(self, query_class):
        """
        Sets the query_class of this DnsHealthCheckerDetails.
        The class the dns health check query to use; either IN or CH.

        Example: `IN`


        :param query_class: The query_class of this DnsHealthCheckerDetails.
        :type: str
        """
        allowed_values = ["IN", "CH"]
        if not value_allowed_none_or_none_sentinel(query_class, allowed_values):
            query_class = 'UNKNOWN_ENUM_VALUE'
        self._query_class = query_class

    @property
    def query_type(self):
        """
        Gets the query_type of this DnsHealthCheckerDetails.
        The type the dns health check query to use; A, AAAA, TXT.

        Example: `A`

        Allowed values for this property are: "A", "TXT", "AAAA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The query_type of this DnsHealthCheckerDetails.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        """
        Sets the query_type of this DnsHealthCheckerDetails.
        The type the dns health check query to use; A, AAAA, TXT.

        Example: `A`


        :param query_type: The query_type of this DnsHealthCheckerDetails.
        :type: str
        """
        allowed_values = ["A", "TXT", "AAAA"]
        if not value_allowed_none_or_none_sentinel(query_type, allowed_values):
            query_type = 'UNKNOWN_ENUM_VALUE'
        self._query_type = query_type

    @property
    def rcodes(self):
        """
        Gets the rcodes of this DnsHealthCheckerDetails.
        An array that represents accepetable RCODE values for DNS query response.
        Example: [\"NOERROR\", \"NXDOMAIN\"]


        :return: The rcodes of this DnsHealthCheckerDetails.
        :rtype: list[oci.network_load_balancer.models.DnsHealthCheckRCodes]
        """
        return self._rcodes

    @rcodes.setter
    def rcodes(self, rcodes):
        """
        Sets the rcodes of this DnsHealthCheckerDetails.
        An array that represents accepetable RCODE values for DNS query response.
        Example: [\"NOERROR\", \"NXDOMAIN\"]


        :param rcodes: The rcodes of this DnsHealthCheckerDetails.
        :type: list[oci.network_load_balancer.models.DnsHealthCheckRCodes]
        """
        self._rcodes = rcodes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
