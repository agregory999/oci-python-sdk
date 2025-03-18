# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20250320


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateNodeConfigDetails(object):
    """
    The data to update a new NodeConfig.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateNodeConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param mac_address:
            The value to assign to the mac_address property of this UpdateNodeConfigDetails.
        :type mac_address: str

        :param mac_order_id:
            The value to assign to the mac_order_id property of this UpdateNodeConfigDetails.
        :type mac_order_id: str

        :param switch_hostname:
            The value to assign to the switch_hostname property of this UpdateNodeConfigDetails.
        :type switch_hostname: str

        :param switch_eth_port:
            The value to assign to the switch_eth_port property of this UpdateNodeConfigDetails.
        :type switch_eth_port: str

        :param ip_kvm_hostname:
            The value to assign to the ip_kvm_hostname property of this UpdateNodeConfigDetails.
        :type ip_kvm_hostname: str

        :param ip_kvm_port_number:
            The value to assign to the ip_kvm_port_number property of this UpdateNodeConfigDetails.
        :type ip_kvm_port_number: int

        :param pdu_hostname:
            The value to assign to the pdu_hostname property of this UpdateNodeConfigDetails.
        :type pdu_hostname: str

        :param pdu_port:
            The value to assign to the pdu_port property of this UpdateNodeConfigDetails.
        :type pdu_port: int

        :param build_vlan_id:
            The value to assign to the build_vlan_id property of this UpdateNodeConfigDetails.
        :type build_vlan_id: int

        :param build_ip_address:
            The value to assign to the build_ip_address property of this UpdateNodeConfigDetails.
        :type build_ip_address: str

        :param prod_vlan_id:
            The value to assign to the prod_vlan_id property of this UpdateNodeConfigDetails.
        :type prod_vlan_id: int

        :param prod_ip_address:
            The value to assign to the prod_ip_address property of this UpdateNodeConfigDetails.
        :type prod_ip_address: str

        :param rack_location:
            The value to assign to the rack_location property of this UpdateNodeConfigDetails.
        :type rack_location: str

        :param chip_set:
            The value to assign to the chip_set property of this UpdateNodeConfigDetails.
        :type chip_set: str

        :param os_version:
            The value to assign to the os_version property of this UpdateNodeConfigDetails.
        :type os_version: str

        :param tenancy_id:
            The value to assign to the tenancy_id property of this UpdateNodeConfigDetails.
        :type tenancy_id: str

        """
        self.swagger_types = {
            'mac_address': 'str',
            'mac_order_id': 'str',
            'switch_hostname': 'str',
            'switch_eth_port': 'str',
            'ip_kvm_hostname': 'str',
            'ip_kvm_port_number': 'int',
            'pdu_hostname': 'str',
            'pdu_port': 'int',
            'build_vlan_id': 'int',
            'build_ip_address': 'str',
            'prod_vlan_id': 'int',
            'prod_ip_address': 'str',
            'rack_location': 'str',
            'chip_set': 'str',
            'os_version': 'str',
            'tenancy_id': 'str'
        }
        self.attribute_map = {
            'mac_address': 'macAddress',
            'mac_order_id': 'macOrderId',
            'switch_hostname': 'switchHostname',
            'switch_eth_port': 'switchEthPort',
            'ip_kvm_hostname': 'ipKvmHostname',
            'ip_kvm_port_number': 'ipKvmPortNumber',
            'pdu_hostname': 'pduHostname',
            'pdu_port': 'pduPort',
            'build_vlan_id': 'buildVlanId',
            'build_ip_address': 'buildIpAddress',
            'prod_vlan_id': 'prodVlanId',
            'prod_ip_address': 'prodIpAddress',
            'rack_location': 'rackLocation',
            'chip_set': 'chipSet',
            'os_version': 'osVersion',
            'tenancy_id': 'tenancyId'
        }
        self._mac_address = None
        self._mac_order_id = None
        self._switch_hostname = None
        self._switch_eth_port = None
        self._ip_kvm_hostname = None
        self._ip_kvm_port_number = None
        self._pdu_hostname = None
        self._pdu_port = None
        self._build_vlan_id = None
        self._build_ip_address = None
        self._prod_vlan_id = None
        self._prod_ip_address = None
        self._rack_location = None
        self._chip_set = None
        self._os_version = None
        self._tenancy_id = None

    @property
    def mac_address(self):
        """
        Gets the mac_address of this UpdateNodeConfigDetails.
        The macAddress.


        :return: The mac_address of this UpdateNodeConfigDetails.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """
        Sets the mac_address of this UpdateNodeConfigDetails.
        The macAddress.


        :param mac_address: The mac_address of this UpdateNodeConfigDetails.
        :type: str
        """
        self._mac_address = mac_address

    @property
    def mac_order_id(self):
        """
        Gets the mac_order_id of this UpdateNodeConfigDetails.
        The macOrderId.


        :return: The mac_order_id of this UpdateNodeConfigDetails.
        :rtype: str
        """
        return self._mac_order_id

    @mac_order_id.setter
    def mac_order_id(self, mac_order_id):
        """
        Sets the mac_order_id of this UpdateNodeConfigDetails.
        The macOrderId.


        :param mac_order_id: The mac_order_id of this UpdateNodeConfigDetails.
        :type: str
        """
        self._mac_order_id = mac_order_id

    @property
    def switch_hostname(self):
        """
        Gets the switch_hostname of this UpdateNodeConfigDetails.
        The switchHostname.


        :return: The switch_hostname of this UpdateNodeConfigDetails.
        :rtype: str
        """
        return self._switch_hostname

    @switch_hostname.setter
    def switch_hostname(self, switch_hostname):
        """
        Sets the switch_hostname of this UpdateNodeConfigDetails.
        The switchHostname.


        :param switch_hostname: The switch_hostname of this UpdateNodeConfigDetails.
        :type: str
        """
        self._switch_hostname = switch_hostname

    @property
    def switch_eth_port(self):
        """
        Gets the switch_eth_port of this UpdateNodeConfigDetails.
        The switchEthPort.


        :return: The switch_eth_port of this UpdateNodeConfigDetails.
        :rtype: str
        """
        return self._switch_eth_port

    @switch_eth_port.setter
    def switch_eth_port(self, switch_eth_port):
        """
        Sets the switch_eth_port of this UpdateNodeConfigDetails.
        The switchEthPort.


        :param switch_eth_port: The switch_eth_port of this UpdateNodeConfigDetails.
        :type: str
        """
        self._switch_eth_port = switch_eth_port

    @property
    def ip_kvm_hostname(self):
        """
        Gets the ip_kvm_hostname of this UpdateNodeConfigDetails.
        The ipKvmHostname.


        :return: The ip_kvm_hostname of this UpdateNodeConfigDetails.
        :rtype: str
        """
        return self._ip_kvm_hostname

    @ip_kvm_hostname.setter
    def ip_kvm_hostname(self, ip_kvm_hostname):
        """
        Sets the ip_kvm_hostname of this UpdateNodeConfigDetails.
        The ipKvmHostname.


        :param ip_kvm_hostname: The ip_kvm_hostname of this UpdateNodeConfigDetails.
        :type: str
        """
        self._ip_kvm_hostname = ip_kvm_hostname

    @property
    def ip_kvm_port_number(self):
        """
        Gets the ip_kvm_port_number of this UpdateNodeConfigDetails.
        The ipKvmPortNumber.


        :return: The ip_kvm_port_number of this UpdateNodeConfigDetails.
        :rtype: int
        """
        return self._ip_kvm_port_number

    @ip_kvm_port_number.setter
    def ip_kvm_port_number(self, ip_kvm_port_number):
        """
        Sets the ip_kvm_port_number of this UpdateNodeConfigDetails.
        The ipKvmPortNumber.


        :param ip_kvm_port_number: The ip_kvm_port_number of this UpdateNodeConfigDetails.
        :type: int
        """
        self._ip_kvm_port_number = ip_kvm_port_number

    @property
    def pdu_hostname(self):
        """
        Gets the pdu_hostname of this UpdateNodeConfigDetails.
        The pduHostname.


        :return: The pdu_hostname of this UpdateNodeConfigDetails.
        :rtype: str
        """
        return self._pdu_hostname

    @pdu_hostname.setter
    def pdu_hostname(self, pdu_hostname):
        """
        Sets the pdu_hostname of this UpdateNodeConfigDetails.
        The pduHostname.


        :param pdu_hostname: The pdu_hostname of this UpdateNodeConfigDetails.
        :type: str
        """
        self._pdu_hostname = pdu_hostname

    @property
    def pdu_port(self):
        """
        Gets the pdu_port of this UpdateNodeConfigDetails.
        The pduPort.


        :return: The pdu_port of this UpdateNodeConfigDetails.
        :rtype: int
        """
        return self._pdu_port

    @pdu_port.setter
    def pdu_port(self, pdu_port):
        """
        Sets the pdu_port of this UpdateNodeConfigDetails.
        The pduPort.


        :param pdu_port: The pdu_port of this UpdateNodeConfigDetails.
        :type: int
        """
        self._pdu_port = pdu_port

    @property
    def build_vlan_id(self):
        """
        Gets the build_vlan_id of this UpdateNodeConfigDetails.
        The buildVlanId.


        :return: The build_vlan_id of this UpdateNodeConfigDetails.
        :rtype: int
        """
        return self._build_vlan_id

    @build_vlan_id.setter
    def build_vlan_id(self, build_vlan_id):
        """
        Sets the build_vlan_id of this UpdateNodeConfigDetails.
        The buildVlanId.


        :param build_vlan_id: The build_vlan_id of this UpdateNodeConfigDetails.
        :type: int
        """
        self._build_vlan_id = build_vlan_id

    @property
    def build_ip_address(self):
        """
        Gets the build_ip_address of this UpdateNodeConfigDetails.
        The buildIpAddress.


        :return: The build_ip_address of this UpdateNodeConfigDetails.
        :rtype: str
        """
        return self._build_ip_address

    @build_ip_address.setter
    def build_ip_address(self, build_ip_address):
        """
        Sets the build_ip_address of this UpdateNodeConfigDetails.
        The buildIpAddress.


        :param build_ip_address: The build_ip_address of this UpdateNodeConfigDetails.
        :type: str
        """
        self._build_ip_address = build_ip_address

    @property
    def prod_vlan_id(self):
        """
        Gets the prod_vlan_id of this UpdateNodeConfigDetails.
        The prodVlanId.


        :return: The prod_vlan_id of this UpdateNodeConfigDetails.
        :rtype: int
        """
        return self._prod_vlan_id

    @prod_vlan_id.setter
    def prod_vlan_id(self, prod_vlan_id):
        """
        Sets the prod_vlan_id of this UpdateNodeConfigDetails.
        The prodVlanId.


        :param prod_vlan_id: The prod_vlan_id of this UpdateNodeConfigDetails.
        :type: int
        """
        self._prod_vlan_id = prod_vlan_id

    @property
    def prod_ip_address(self):
        """
        Gets the prod_ip_address of this UpdateNodeConfigDetails.
        The prodIpAddress.


        :return: The prod_ip_address of this UpdateNodeConfigDetails.
        :rtype: str
        """
        return self._prod_ip_address

    @prod_ip_address.setter
    def prod_ip_address(self, prod_ip_address):
        """
        Sets the prod_ip_address of this UpdateNodeConfigDetails.
        The prodIpAddress.


        :param prod_ip_address: The prod_ip_address of this UpdateNodeConfigDetails.
        :type: str
        """
        self._prod_ip_address = prod_ip_address

    @property
    def rack_location(self):
        """
        Gets the rack_location of this UpdateNodeConfigDetails.
        The rackLocation.


        :return: The rack_location of this UpdateNodeConfigDetails.
        :rtype: str
        """
        return self._rack_location

    @rack_location.setter
    def rack_location(self, rack_location):
        """
        Sets the rack_location of this UpdateNodeConfigDetails.
        The rackLocation.


        :param rack_location: The rack_location of this UpdateNodeConfigDetails.
        :type: str
        """
        self._rack_location = rack_location

    @property
    def chip_set(self):
        """
        Gets the chip_set of this UpdateNodeConfigDetails.
        The chipSetn.


        :return: The chip_set of this UpdateNodeConfigDetails.
        :rtype: str
        """
        return self._chip_set

    @chip_set.setter
    def chip_set(self, chip_set):
        """
        Sets the chip_set of this UpdateNodeConfigDetails.
        The chipSetn.


        :param chip_set: The chip_set of this UpdateNodeConfigDetails.
        :type: str
        """
        self._chip_set = chip_set

    @property
    def os_version(self):
        """
        Gets the os_version of this UpdateNodeConfigDetails.
        The osVersion.


        :return: The os_version of this UpdateNodeConfigDetails.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """
        Sets the os_version of this UpdateNodeConfigDetails.
        The osVersion.


        :param os_version: The os_version of this UpdateNodeConfigDetails.
        :type: str
        """
        self._os_version = os_version

    @property
    def tenancy_id(self):
        """
        Gets the tenancy_id of this UpdateNodeConfigDetails.
        The tenancyId.


        :return: The tenancy_id of this UpdateNodeConfigDetails.
        :rtype: str
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        """
        Sets the tenancy_id of this UpdateNodeConfigDetails.
        The tenancyId.


        :param tenancy_id: The tenancy_id of this UpdateNodeConfigDetails.
        :type: str
        """
        self._tenancy_id = tenancy_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
