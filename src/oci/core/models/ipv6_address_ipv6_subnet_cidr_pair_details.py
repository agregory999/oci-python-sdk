# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Ipv6AddressIpv6SubnetCidrPairDetails(object):
    """
    Details to assign an IPv6 subnet prefix and IPv6 address on VNIC creation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Ipv6AddressIpv6SubnetCidrPairDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ipv6_subnet_cidr:
            The value to assign to the ipv6_subnet_cidr property of this Ipv6AddressIpv6SubnetCidrPairDetails.
        :type ipv6_subnet_cidr: str

        :param ipv6_address:
            The value to assign to the ipv6_address property of this Ipv6AddressIpv6SubnetCidrPairDetails.
        :type ipv6_address: str

        """
        self.swagger_types = {
            'ipv6_subnet_cidr': 'str',
            'ipv6_address': 'str'
        }

        self.attribute_map = {
            'ipv6_subnet_cidr': 'ipv6SubnetCidr',
            'ipv6_address': 'ipv6Address'
        }

        self._ipv6_subnet_cidr = None
        self._ipv6_address = None

    @property
    def ipv6_subnet_cidr(self):
        """
        Gets the ipv6_subnet_cidr of this Ipv6AddressIpv6SubnetCidrPairDetails.
        The IPv6 prefix allocated to the subnet.


        :return: The ipv6_subnet_cidr of this Ipv6AddressIpv6SubnetCidrPairDetails.
        :rtype: str
        """
        return self._ipv6_subnet_cidr

    @ipv6_subnet_cidr.setter
    def ipv6_subnet_cidr(self, ipv6_subnet_cidr):
        """
        Sets the ipv6_subnet_cidr of this Ipv6AddressIpv6SubnetCidrPairDetails.
        The IPv6 prefix allocated to the subnet.


        :param ipv6_subnet_cidr: The ipv6_subnet_cidr of this Ipv6AddressIpv6SubnetCidrPairDetails.
        :type: str
        """
        self._ipv6_subnet_cidr = ipv6_subnet_cidr

    @property
    def ipv6_address(self):
        """
        Gets the ipv6_address of this Ipv6AddressIpv6SubnetCidrPairDetails.
        An IPv6 address of your choice. Must be an available IPv6 address within the subnet's prefix.
        If an IPv6 address is not provided:
        - Oracle will automatically assign an IPv6 address from the subnet's IPv6 prefix if and only if there is only one IPv6 prefix on the subnet.
        - Oracle will automatically assign an IPv6 address from the subnet's IPv6 Oracle GUA prefix if it exists on the subnet.


        :return: The ipv6_address of this Ipv6AddressIpv6SubnetCidrPairDetails.
        :rtype: str
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, ipv6_address):
        """
        Sets the ipv6_address of this Ipv6AddressIpv6SubnetCidrPairDetails.
        An IPv6 address of your choice. Must be an available IPv6 address within the subnet's prefix.
        If an IPv6 address is not provided:
        - Oracle will automatically assign an IPv6 address from the subnet's IPv6 prefix if and only if there is only one IPv6 prefix on the subnet.
        - Oracle will automatically assign an IPv6 address from the subnet's IPv6 Oracle GUA prefix if it exists on the subnet.


        :param ipv6_address: The ipv6_address of this Ipv6AddressIpv6SubnetCidrPairDetails.
        :type: str
        """
        self._ipv6_address = ipv6_address

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other