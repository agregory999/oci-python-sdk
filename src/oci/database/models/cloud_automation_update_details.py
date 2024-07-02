# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CloudAutomationUpdateDetails(object):
    """
    Specifies the properties necessary for cloud automation updates. This includes modifying the apply update time preference, enabling or disabling early adoption, and enabling, modifying, or disabling the update freeze period.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CloudAutomationUpdateDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_early_adoption_enabled:
            The value to assign to the is_early_adoption_enabled property of this CloudAutomationUpdateDetails.
        :type is_early_adoption_enabled: bool

        :param is_freeze_period_enabled:
            The value to assign to the is_freeze_period_enabled property of this CloudAutomationUpdateDetails.
        :type is_freeze_period_enabled: bool

        :param apply_update_time_preference:
            The value to assign to the apply_update_time_preference property of this CloudAutomationUpdateDetails.
        :type apply_update_time_preference: oci.database.models.CloudAutomationApplyUpdateTimePreference

        :param freeze_period:
            The value to assign to the freeze_period property of this CloudAutomationUpdateDetails.
        :type freeze_period: oci.database.models.CloudAutomationFreezePeriod

        """
        self.swagger_types = {
            'is_early_adoption_enabled': 'bool',
            'is_freeze_period_enabled': 'bool',
            'apply_update_time_preference': 'CloudAutomationApplyUpdateTimePreference',
            'freeze_period': 'CloudAutomationFreezePeriod'
        }

        self.attribute_map = {
            'is_early_adoption_enabled': 'isEarlyAdoptionEnabled',
            'is_freeze_period_enabled': 'isFreezePeriodEnabled',
            'apply_update_time_preference': 'applyUpdateTimePreference',
            'freeze_period': 'freezePeriod'
        }

        self._is_early_adoption_enabled = None
        self._is_freeze_period_enabled = None
        self._apply_update_time_preference = None
        self._freeze_period = None

    @property
    def is_early_adoption_enabled(self):
        """
        Gets the is_early_adoption_enabled of this CloudAutomationUpdateDetails.
        Annotates whether the cluster should be part of early access to apply VM cloud automation software updates. Those clusters annotated as early access will download the software bits for cloud automation in the first week after the update is available, while other clusters will have to wait until the following week.


        :return: The is_early_adoption_enabled of this CloudAutomationUpdateDetails.
        :rtype: bool
        """
        return self._is_early_adoption_enabled

    @is_early_adoption_enabled.setter
    def is_early_adoption_enabled(self, is_early_adoption_enabled):
        """
        Sets the is_early_adoption_enabled of this CloudAutomationUpdateDetails.
        Annotates whether the cluster should be part of early access to apply VM cloud automation software updates. Those clusters annotated as early access will download the software bits for cloud automation in the first week after the update is available, while other clusters will have to wait until the following week.


        :param is_early_adoption_enabled: The is_early_adoption_enabled of this CloudAutomationUpdateDetails.
        :type: bool
        """
        self._is_early_adoption_enabled = is_early_adoption_enabled

    @property
    def is_freeze_period_enabled(self):
        """
        Gets the is_freeze_period_enabled of this CloudAutomationUpdateDetails.
        Specifies if the freeze period is enabled for the VM cluster to prevent the VMs from receiving cloud automation software updates during critical business cycles. Freeze period starts at 12:00 AM UTC and ends at 11:59:59 PM UTC on the selected date. Ensure that the freezing period does not exceed 45 days.


        :return: The is_freeze_period_enabled of this CloudAutomationUpdateDetails.
        :rtype: bool
        """
        return self._is_freeze_period_enabled

    @is_freeze_period_enabled.setter
    def is_freeze_period_enabled(self, is_freeze_period_enabled):
        """
        Sets the is_freeze_period_enabled of this CloudAutomationUpdateDetails.
        Specifies if the freeze period is enabled for the VM cluster to prevent the VMs from receiving cloud automation software updates during critical business cycles. Freeze period starts at 12:00 AM UTC and ends at 11:59:59 PM UTC on the selected date. Ensure that the freezing period does not exceed 45 days.


        :param is_freeze_period_enabled: The is_freeze_period_enabled of this CloudAutomationUpdateDetails.
        :type: bool
        """
        self._is_freeze_period_enabled = is_freeze_period_enabled

    @property
    def apply_update_time_preference(self):
        """
        Gets the apply_update_time_preference of this CloudAutomationUpdateDetails.

        :return: The apply_update_time_preference of this CloudAutomationUpdateDetails.
        :rtype: oci.database.models.CloudAutomationApplyUpdateTimePreference
        """
        return self._apply_update_time_preference

    @apply_update_time_preference.setter
    def apply_update_time_preference(self, apply_update_time_preference):
        """
        Sets the apply_update_time_preference of this CloudAutomationUpdateDetails.

        :param apply_update_time_preference: The apply_update_time_preference of this CloudAutomationUpdateDetails.
        :type: oci.database.models.CloudAutomationApplyUpdateTimePreference
        """
        self._apply_update_time_preference = apply_update_time_preference

    @property
    def freeze_period(self):
        """
        Gets the freeze_period of this CloudAutomationUpdateDetails.

        :return: The freeze_period of this CloudAutomationUpdateDetails.
        :rtype: oci.database.models.CloudAutomationFreezePeriod
        """
        return self._freeze_period

    @freeze_period.setter
    def freeze_period(self, freeze_period):
        """
        Sets the freeze_period of this CloudAutomationUpdateDetails.

        :param freeze_period: The freeze_period of this CloudAutomationUpdateDetails.
        :type: oci.database.models.CloudAutomationFreezePeriod
        """
        self._freeze_period = freeze_period

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
