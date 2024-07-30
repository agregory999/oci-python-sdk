# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTunnelInspectionRuleDetails(object):
    """
    Update Request for creating Tunnel Inspection Rule used in the firewall policy rules.
    Tunnel Inspection Rule determines whether tunnel inspection is applied on the traffic based on attributes
    such as Tunnel Inspect protocol, the source and destination IP address.
    """

    #: A constant which can be used with the action property of a UpdateTunnelInspectionRuleDetails.
    #: This constant has a value of "INSPECT"
    ACTION_INSPECT = "INSPECT"

    #: A constant which can be used with the action property of a UpdateTunnelInspectionRuleDetails.
    #: This constant has a value of "INSPECT_AND_CAPTURE_LOG"
    ACTION_INSPECT_AND_CAPTURE_LOG = "INSPECT_AND_CAPTURE_LOG"

    #: A constant which can be used with the protocol property of a UpdateTunnelInspectionRuleDetails.
    #: This constant has a value of "VXLAN"
    PROTOCOL_VXLAN = "VXLAN"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTunnelInspectionRuleDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.network_firewall.models.UpdateVxlanInspectionRuleDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this UpdateTunnelInspectionRuleDetails.
            Allowed values for this property are: "INSPECT", "INSPECT_AND_CAPTURE_LOG"
        :type action: str

        :param protocol:
            The value to assign to the protocol property of this UpdateTunnelInspectionRuleDetails.
            Allowed values for this property are: "VXLAN"
        :type protocol: str

        :param position:
            The value to assign to the position property of this UpdateTunnelInspectionRuleDetails.
        :type position: oci.network_firewall.models.RulePosition

        """
        self.swagger_types = {
            'action': 'str',
            'protocol': 'str',
            'position': 'RulePosition'
        }

        self.attribute_map = {
            'action': 'action',
            'protocol': 'protocol',
            'position': 'position'
        }

        self._action = None
        self._protocol = None
        self._position = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['protocol']

        if type == 'VXLAN':
            return 'UpdateVxlanInspectionRuleDetails'
        else:
            return 'UpdateTunnelInspectionRuleDetails'

    @property
    def action(self):
        """
        Gets the action of this UpdateTunnelInspectionRuleDetails.
        Types of Inspect Action on the Traffic flow.

          * INSPECT - Inspect the traffic.
          * INSPECT_AND_CAPTURE_LOG - Inspect and capture logs for the traffic.

        Allowed values for this property are: "INSPECT", "INSPECT_AND_CAPTURE_LOG"


        :return: The action of this UpdateTunnelInspectionRuleDetails.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this UpdateTunnelInspectionRuleDetails.
        Types of Inspect Action on the Traffic flow.

          * INSPECT - Inspect the traffic.
          * INSPECT_AND_CAPTURE_LOG - Inspect and capture logs for the traffic.


        :param action: The action of this UpdateTunnelInspectionRuleDetails.
        :type: str
        """
        allowed_values = ["INSPECT", "INSPECT_AND_CAPTURE_LOG"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            raise ValueError(
                f"Invalid value for `action`, must be None or one of {allowed_values}"
            )
        self._action = action

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this UpdateTunnelInspectionRuleDetails.
        Types of Tunnel Inspection Protocol to be applied on the traffic.

          * VXLAN - VXLAN Tunnel Inspection Protocol will be applied on the traffic.

        Allowed values for this property are: "VXLAN"


        :return: The protocol of this UpdateTunnelInspectionRuleDetails.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this UpdateTunnelInspectionRuleDetails.
        Types of Tunnel Inspection Protocol to be applied on the traffic.

          * VXLAN - VXLAN Tunnel Inspection Protocol will be applied on the traffic.


        :param protocol: The protocol of this UpdateTunnelInspectionRuleDetails.
        :type: str
        """
        allowed_values = ["VXLAN"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            raise ValueError(
                f"Invalid value for `protocol`, must be None or one of {allowed_values}"
            )
        self._protocol = protocol

    @property
    def position(self):
        """
        Gets the position of this UpdateTunnelInspectionRuleDetails.

        :return: The position of this UpdateTunnelInspectionRuleDetails.
        :rtype: oci.network_firewall.models.RulePosition
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this UpdateTunnelInspectionRuleDetails.

        :param position: The position of this UpdateTunnelInspectionRuleDetails.
        :type: oci.network_firewall.models.RulePosition
        """
        self._position = position

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other