# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .routing_action import RoutingAction
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IndeterminateRoutingAction(RoutingAction):
    """
    Defines the routing action taken on a traffic node where the routing action is INDETERMINATE.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IndeterminateRoutingAction object with values from keyword arguments. The default value of the :py:attr:`~oci.vn_monitoring.models.IndeterminateRoutingAction.action` attribute
        of this class is ``INDETERMINATE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this IndeterminateRoutingAction.
            Allowed values for this property are: "FORWARDED", "NO_ROUTE", "INDETERMINATE"
        :type action: str

        :param action_type:
            The value to assign to the action_type property of this IndeterminateRoutingAction.
            Allowed values for this property are: "EXPLICIT", "IMPLICIT", "NOT_SUPPORTED"
        :type action_type: str

        """
        self.swagger_types = {
            'action': 'str',
            'action_type': 'str'
        }

        self.attribute_map = {
            'action': 'action',
            'action_type': 'actionType'
        }

        self._action = None
        self._action_type = None
        self._action = 'INDETERMINATE'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
