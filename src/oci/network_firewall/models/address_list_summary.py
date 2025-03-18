# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddressListSummary(object):
    """
    Address List Summary in the network firewall policy
    """

    #: A constant which can be used with the type property of a AddressListSummary.
    #: This constant has a value of "FQDN"
    TYPE_FQDN = "FQDN"

    #: A constant which can be used with the type property of a AddressListSummary.
    #: This constant has a value of "IP"
    TYPE_IP = "IP"

    def __init__(self, **kwargs):
        """
        Initializes a new AddressListSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AddressListSummary.
        :type name: str

        :param type:
            The value to assign to the type property of this AddressListSummary.
            Allowed values for this property are: "FQDN", "IP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param total_addresses:
            The value to assign to the total_addresses property of this AddressListSummary.
        :type total_addresses: int

        :param parent_resource_id:
            The value to assign to the parent_resource_id property of this AddressListSummary.
        :type parent_resource_id: str

        """
        self.swagger_types = {
            'name': 'str',
            'type': 'str',
            'total_addresses': 'int',
            'parent_resource_id': 'str'
        }
        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'total_addresses': 'totalAddresses',
            'parent_resource_id': 'parentResourceId'
        }
        self._name = None
        self._type = None
        self._total_addresses = None
        self._parent_resource_id = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AddressListSummary.
        Name of Address List


        :return: The name of this AddressListSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AddressListSummary.
        Name of Address List


        :param name: The name of this AddressListSummary.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this AddressListSummary.
        Type of address List. The accepted values are - * FQDN * IP

        Allowed values for this property are: "FQDN", "IP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this AddressListSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AddressListSummary.
        Type of address List. The accepted values are - * FQDN * IP


        :param type: The type of this AddressListSummary.
        :type: str
        """
        allowed_values = ["FQDN", "IP"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def total_addresses(self):
        """
        **[Required]** Gets the total_addresses of this AddressListSummary.
        Count of total Addresses in the AddressList


        :return: The total_addresses of this AddressListSummary.
        :rtype: int
        """
        return self._total_addresses

    @total_addresses.setter
    def total_addresses(self, total_addresses):
        """
        Sets the total_addresses of this AddressListSummary.
        Count of total Addresses in the AddressList


        :param total_addresses: The total_addresses of this AddressListSummary.
        :type: int
        """
        self._total_addresses = total_addresses

    @property
    def parent_resource_id(self):
        """
        **[Required]** Gets the parent_resource_id of this AddressListSummary.
        OCID of the Network Firewall Policy this address list belongs to.


        :return: The parent_resource_id of this AddressListSummary.
        :rtype: str
        """
        return self._parent_resource_id

    @parent_resource_id.setter
    def parent_resource_id(self, parent_resource_id):
        """
        Sets the parent_resource_id of this AddressListSummary.
        OCID of the Network Firewall Policy this address list belongs to.


        :param parent_resource_id: The parent_resource_id of this AddressListSummary.
        :type: str
        """
        self._parent_resource_id = parent_resource_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
