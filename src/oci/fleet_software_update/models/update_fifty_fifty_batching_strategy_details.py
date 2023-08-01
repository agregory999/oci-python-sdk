# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528

from .update_batching_strategy_details import UpdateBatchingStrategyDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateFiftyFiftyBatchingStrategyDetails(UpdateBatchingStrategyDetails):
    """
    Fifty-Fifty batching strategy details to use during PRECHECK and APPLY Cycle Actions.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateFiftyFiftyBatchingStrategyDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_software_update.models.UpdateFiftyFiftyBatchingStrategyDetails.type` attribute
        of this class is ``FIFTY_FIFTY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this UpdateFiftyFiftyBatchingStrategyDetails.
            Allowed values for this property are: "SEQUENTIAL", "FIFTY_FIFTY", "SERVICE_AVAILABILITY_FACTOR", "NON_ROLLING", "NONE"
        :type type: str

        :param is_wait_for_batch_resume:
            The value to assign to the is_wait_for_batch_resume property of this UpdateFiftyFiftyBatchingStrategyDetails.
        :type is_wait_for_batch_resume: bool

        :param is_force_rolling:
            The value to assign to the is_force_rolling property of this UpdateFiftyFiftyBatchingStrategyDetails.
        :type is_force_rolling: bool

        """
        self.swagger_types = {
            'type': 'str',
            'is_wait_for_batch_resume': 'bool',
            'is_force_rolling': 'bool'
        }

        self.attribute_map = {
            'type': 'type',
            'is_wait_for_batch_resume': 'isWaitForBatchResume',
            'is_force_rolling': 'isForceRolling'
        }

        self._type = None
        self._is_wait_for_batch_resume = None
        self._is_force_rolling = None
        self._type = 'FIFTY_FIFTY'

    @property
    def is_wait_for_batch_resume(self):
        """
        Gets the is_wait_for_batch_resume of this UpdateFiftyFiftyBatchingStrategyDetails.
        True to wait for customer to resume the Apply Action once the first half is done.
        False to automatically patch the second half.


        :return: The is_wait_for_batch_resume of this UpdateFiftyFiftyBatchingStrategyDetails.
        :rtype: bool
        """
        return self._is_wait_for_batch_resume

    @is_wait_for_batch_resume.setter
    def is_wait_for_batch_resume(self, is_wait_for_batch_resume):
        """
        Sets the is_wait_for_batch_resume of this UpdateFiftyFiftyBatchingStrategyDetails.
        True to wait for customer to resume the Apply Action once the first half is done.
        False to automatically patch the second half.


        :param is_wait_for_batch_resume: The is_wait_for_batch_resume of this UpdateFiftyFiftyBatchingStrategyDetails.
        :type: bool
        """
        self._is_wait_for_batch_resume = is_wait_for_batch_resume

    @property
    def is_force_rolling(self):
        """
        Gets the is_force_rolling of this UpdateFiftyFiftyBatchingStrategyDetails.
        True to force rolling patching.


        :return: The is_force_rolling of this UpdateFiftyFiftyBatchingStrategyDetails.
        :rtype: bool
        """
        return self._is_force_rolling

    @is_force_rolling.setter
    def is_force_rolling(self, is_force_rolling):
        """
        Sets the is_force_rolling of this UpdateFiftyFiftyBatchingStrategyDetails.
        True to force rolling patching.


        :param is_force_rolling: The is_force_rolling of this UpdateFiftyFiftyBatchingStrategyDetails.
        :type: bool
        """
        self._is_force_rolling = is_force_rolling

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
