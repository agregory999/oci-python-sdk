# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630

from .pull_request_activity_summary import PullRequestActivitySummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PullRequestLifecycleActivitySummary(PullRequestActivitySummary):
    """
    activity describing a pull request state change
    """

    #: A constant which can be used with the state property of a PullRequestLifecycleActivitySummary.
    #: This constant has a value of "OPENED"
    STATE_OPENED = "OPENED"

    #: A constant which can be used with the state property of a PullRequestLifecycleActivitySummary.
    #: This constant has a value of "CLOSED"
    STATE_CLOSED = "CLOSED"

    #: A constant which can be used with the state property of a PullRequestLifecycleActivitySummary.
    #: This constant has a value of "MERGED"
    STATE_MERGED = "MERGED"

    #: A constant which can be used with the state property of a PullRequestLifecycleActivitySummary.
    #: This constant has a value of "REOPENED"
    STATE_REOPENED = "REOPENED"

    def __init__(self, **kwargs):
        """
        Initializes a new PullRequestLifecycleActivitySummary object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.PullRequestLifecycleActivitySummary.activity_type` attribute
        of this class is ``LIFECYCLE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this PullRequestLifecycleActivitySummary.
        :type id: str

        :param principal:
            The value to assign to the principal property of this PullRequestLifecycleActivitySummary.
        :type principal: oci.devops.models.PrincipalDetails

        :param pull_request_id:
            The value to assign to the pull_request_id property of this PullRequestLifecycleActivitySummary.
        :type pull_request_id: str

        :param time_occurred:
            The value to assign to the time_occurred property of this PullRequestLifecycleActivitySummary.
        :type time_occurred: datetime

        :param activity_type:
            The value to assign to the activity_type property of this PullRequestLifecycleActivitySummary.
            Allowed values for this property are: "LIFECYCLE", "APPROVAL", "COMMIT", "REVIEWER", "COMMENT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type activity_type: str

        :param state:
            The value to assign to the state property of this PullRequestLifecycleActivitySummary.
            Allowed values for this property are: "OPENED", "CLOSED", "MERGED", "REOPENED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type state: str

        """
        self.swagger_types = {
            'id': 'str',
            'principal': 'PrincipalDetails',
            'pull_request_id': 'str',
            'time_occurred': 'datetime',
            'activity_type': 'str',
            'state': 'str'
        }
        self.attribute_map = {
            'id': 'id',
            'principal': 'principal',
            'pull_request_id': 'pullRequestId',
            'time_occurred': 'timeOccurred',
            'activity_type': 'activityType',
            'state': 'state'
        }
        self._id = None
        self._principal = None
        self._pull_request_id = None
        self._time_occurred = None
        self._activity_type = None
        self._state = None
        self._activity_type = 'LIFECYCLE'

    @property
    def state(self):
        """
        **[Required]** Gets the state of this PullRequestLifecycleActivitySummary.
        The state of a pull request after an action.

        Allowed values for this property are: "OPENED", "CLOSED", "MERGED", "REOPENED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The state of this PullRequestLifecycleActivitySummary.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this PullRequestLifecycleActivitySummary.
        The state of a pull request after an action.


        :param state: The state of this PullRequestLifecycleActivitySummary.
        :type: str
        """
        allowed_values = ["OPENED", "CLOSED", "MERGED", "REOPENED"]
        if not value_allowed_none_or_none_sentinel(state, allowed_values):
            state = 'UNKNOWN_ENUM_VALUE'
        self._state = state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
