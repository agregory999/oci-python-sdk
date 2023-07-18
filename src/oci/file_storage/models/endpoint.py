# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20171215


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Endpoint(object):
    """
    Combination of DNS server name and port.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Endpoint object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param hostname:
            The value to assign to the hostname property of this Endpoint.
        :type hostname: str

        :param port:
            The value to assign to the port property of this Endpoint.
        :type port: int

        """
        self.swagger_types = {
            'hostname': 'str',
            'port': 'int'
        }

        self.attribute_map = {
            'hostname': 'hostname',
            'port': 'port'
        }

        self._hostname = None
        self._port = None

    @property
    def hostname(self):
        """
        **[Required]** Gets the hostname of this Endpoint.
        Name of the DNS server.


        :return: The hostname of this Endpoint.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this Endpoint.
        Name of the DNS server.


        :param hostname: The hostname of this Endpoint.
        :type: str
        """
        self._hostname = hostname

    @property
    def port(self):
        """
        **[Required]** Gets the port of this Endpoint.
        Port of the DNS server.


        :return: The port of this Endpoint.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this Endpoint.
        Port of the DNS server.


        :param port: The port of this Endpoint.
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
