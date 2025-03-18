# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220618


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDesktopPoolDesktopSessionLifecycleActions(object):
    """
    The details of action to be triggered in case of inactivity or disconnect
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDesktopPoolDesktopSessionLifecycleActions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param inactivity:
            The value to assign to the inactivity property of this CreateDesktopPoolDesktopSessionLifecycleActions.
        :type inactivity: oci.desktops.models.InactivityConfig

        :param disconnect:
            The value to assign to the disconnect property of this CreateDesktopPoolDesktopSessionLifecycleActions.
        :type disconnect: oci.desktops.models.DisconnectConfig

        """
        self.swagger_types = {
            'inactivity': 'InactivityConfig',
            'disconnect': 'DisconnectConfig'
        }
        self.attribute_map = {
            'inactivity': 'inactivity',
            'disconnect': 'disconnect'
        }
        self._inactivity = None
        self._disconnect = None

    @property
    def inactivity(self):
        """
        Gets the inactivity of this CreateDesktopPoolDesktopSessionLifecycleActions.

        :return: The inactivity of this CreateDesktopPoolDesktopSessionLifecycleActions.
        :rtype: oci.desktops.models.InactivityConfig
        """
        return self._inactivity

    @inactivity.setter
    def inactivity(self, inactivity):
        """
        Sets the inactivity of this CreateDesktopPoolDesktopSessionLifecycleActions.

        :param inactivity: The inactivity of this CreateDesktopPoolDesktopSessionLifecycleActions.
        :type: oci.desktops.models.InactivityConfig
        """
        self._inactivity = inactivity

    @property
    def disconnect(self):
        """
        Gets the disconnect of this CreateDesktopPoolDesktopSessionLifecycleActions.

        :return: The disconnect of this CreateDesktopPoolDesktopSessionLifecycleActions.
        :rtype: oci.desktops.models.DisconnectConfig
        """
        return self._disconnect

    @disconnect.setter
    def disconnect(self, disconnect):
        """
        Sets the disconnect of this CreateDesktopPoolDesktopSessionLifecycleActions.

        :param disconnect: The disconnect of this CreateDesktopPoolDesktopSessionLifecycleActions.
        :type: oci.desktops.models.DisconnectConfig
        """
        self._disconnect = disconnect

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
