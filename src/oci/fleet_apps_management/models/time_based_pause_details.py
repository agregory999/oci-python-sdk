# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831

from .pause_details import PauseDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TimeBasedPauseDetails(PauseDetails):
    """
    Time-based pause details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TimeBasedPauseDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_apps_management.models.TimeBasedPauseDetails.kind` attribute
        of this class is ``TIME_BASED`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this TimeBasedPauseDetails.
            Allowed values for this property are: "USER_ACTION", "TIME_BASED"
        :type kind: str

        :param duration_in_minutes:
            The value to assign to the duration_in_minutes property of this TimeBasedPauseDetails.
        :type duration_in_minutes: int

        """
        self.swagger_types = {
            'kind': 'str',
            'duration_in_minutes': 'int'
        }
        self.attribute_map = {
            'kind': 'kind',
            'duration_in_minutes': 'durationInMinutes'
        }
        self._kind = None
        self._duration_in_minutes = None
        self._kind = 'TIME_BASED'

    @property
    def duration_in_minutes(self):
        """
        **[Required]** Gets the duration_in_minutes of this TimeBasedPauseDetails.
        Time in minutes to apply Pause.


        :return: The duration_in_minutes of this TimeBasedPauseDetails.
        :rtype: int
        """
        return self._duration_in_minutes

    @duration_in_minutes.setter
    def duration_in_minutes(self, duration_in_minutes):
        """
        Sets the duration_in_minutes of this TimeBasedPauseDetails.
        Time in minutes to apply Pause.


        :param duration_in_minutes: The duration_in_minutes of this TimeBasedPauseDetails.
        :type: int
        """
        self._duration_in_minutes = duration_in_minutes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
