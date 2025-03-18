# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230501

from .create_tunnel_inspection_rule_details import CreateTunnelInspectionRuleDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateVxlanInspectionRuleDetails(CreateTunnelInspectionRuleDetails):
    """
    Request for creating Vxlan Tunnel Inspection Rule used in the firewall policy rules.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateVxlanInspectionRuleDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.network_firewall.models.CreateVxlanInspectionRuleDetails.protocol` attribute
        of this class is ``VXLAN`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateVxlanInspectionRuleDetails.
        :type name: str

        :param action:
            The value to assign to the action property of this CreateVxlanInspectionRuleDetails.
            Allowed values for this property are: "INSPECT", "INSPECT_AND_CAPTURE_LOG"
        :type action: str

        :param protocol:
            The value to assign to the protocol property of this CreateVxlanInspectionRuleDetails.
            Allowed values for this property are: "VXLAN"
        :type protocol: str

        :param position:
            The value to assign to the position property of this CreateVxlanInspectionRuleDetails.
        :type position: oci.network_firewall.models.RulePosition

        :param condition:
            The value to assign to the condition property of this CreateVxlanInspectionRuleDetails.
        :type condition: oci.network_firewall.models.VxlanInspectionRuleMatchCriteria

        :param profile:
            The value to assign to the profile property of this CreateVxlanInspectionRuleDetails.
        :type profile: oci.network_firewall.models.VxlanInspectionRuleProfile

        """
        self.swagger_types = {
            'name': 'str',
            'action': 'str',
            'protocol': 'str',
            'position': 'RulePosition',
            'condition': 'VxlanInspectionRuleMatchCriteria',
            'profile': 'VxlanInspectionRuleProfile'
        }
        self.attribute_map = {
            'name': 'name',
            'action': 'action',
            'protocol': 'protocol',
            'position': 'position',
            'condition': 'condition',
            'profile': 'profile'
        }
        self._name = None
        self._action = None
        self._protocol = None
        self._position = None
        self._condition = None
        self._profile = None
        self._protocol = 'VXLAN'

    @property
    def condition(self):
        """
        **[Required]** Gets the condition of this CreateVxlanInspectionRuleDetails.

        :return: The condition of this CreateVxlanInspectionRuleDetails.
        :rtype: oci.network_firewall.models.VxlanInspectionRuleMatchCriteria
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this CreateVxlanInspectionRuleDetails.

        :param condition: The condition of this CreateVxlanInspectionRuleDetails.
        :type: oci.network_firewall.models.VxlanInspectionRuleMatchCriteria
        """
        self._condition = condition

    @property
    def profile(self):
        """
        Gets the profile of this CreateVxlanInspectionRuleDetails.

        :return: The profile of this CreateVxlanInspectionRuleDetails.
        :rtype: oci.network_firewall.models.VxlanInspectionRuleProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """
        Sets the profile of this CreateVxlanInspectionRuleDetails.

        :param profile: The profile of this CreateVxlanInspectionRuleDetails.
        :type: oci.network_firewall.models.VxlanInspectionRuleProfile
        """
        self._profile = profile

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
