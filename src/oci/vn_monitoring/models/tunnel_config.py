# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TunnelConfig(object):
    """
    Specific connection details for an IPSec tunnel.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TunnelConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ip_address:
            The value to assign to the ip_address property of this TunnelConfig.
        :type ip_address: str

        :param shared_secret:
            The value to assign to the shared_secret property of this TunnelConfig.
        :type shared_secret: str

        :param time_created:
            The value to assign to the time_created property of this TunnelConfig.
        :type time_created: datetime

        """
        self.swagger_types = {
            'ip_address': 'str',
            'shared_secret': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'ip_address': 'ipAddress',
            'shared_secret': 'sharedSecret',
            'time_created': 'timeCreated'
        }

        self._ip_address = None
        self._shared_secret = None
        self._time_created = None

    @property
    def ip_address(self):
        """
        **[Required]** Gets the ip_address of this TunnelConfig.
        The IP address of Oracle's VPN headend.

        Example: `203.0.113.50 `


        :return: The ip_address of this TunnelConfig.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this TunnelConfig.
        The IP address of Oracle's VPN headend.

        Example: `203.0.113.50 `


        :param ip_address: The ip_address of this TunnelConfig.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def shared_secret(self):
        """
        **[Required]** Gets the shared_secret of this TunnelConfig.
        The shared secret of the IPSec tunnel.


        :return: The shared_secret of this TunnelConfig.
        :rtype: str
        """
        return self._shared_secret

    @shared_secret.setter
    def shared_secret(self, shared_secret):
        """
        Sets the shared_secret of this TunnelConfig.
        The shared secret of the IPSec tunnel.


        :param shared_secret: The shared_secret of this TunnelConfig.
        :type: str
        """
        self._shared_secret = shared_secret

    @property
    def time_created(self):
        """
        Gets the time_created of this TunnelConfig.
        The date and time the IPSec connection was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this TunnelConfig.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TunnelConfig.
        The date and time the IPSec connection was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this TunnelConfig.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
