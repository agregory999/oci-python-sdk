# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuthenticationFactorSettingsNotificationSettings(object):
    """
    Settings related to the Mobile App Notification channel, such as pull

    **Added In:** 17.4.2

    **SCIM++ Properties:**
    - idcsSearchable: false
    - multiValued: false
    - mutability: readWrite
    - required: true
    - returned: default
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AuthenticationFactorSettingsNotificationSettings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param pull_enabled:
            The value to assign to the pull_enabled property of this AuthenticationFactorSettingsNotificationSettings.
        :type pull_enabled: bool

        """
        self.swagger_types = {
            'pull_enabled': 'bool'
        }

        self.attribute_map = {
            'pull_enabled': 'pullEnabled'
        }

        self._pull_enabled = None

    @property
    def pull_enabled(self):
        """
        **[Required]** Gets the pull_enabled of this AuthenticationFactorSettingsNotificationSettings.
        If true, indicates that the Mobile App Pull Notification channel is enabled for authentication

        **Added In:** 17.4.2

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The pull_enabled of this AuthenticationFactorSettingsNotificationSettings.
        :rtype: bool
        """
        return self._pull_enabled

    @pull_enabled.setter
    def pull_enabled(self, pull_enabled):
        """
        Sets the pull_enabled of this AuthenticationFactorSettingsNotificationSettings.
        If true, indicates that the Mobile App Pull Notification channel is enabled for authentication

        **Added In:** 17.4.2

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: boolean
         - uniqueness: none


        :param pull_enabled: The pull_enabled of this AuthenticationFactorSettingsNotificationSettings.
        :type: bool
        """
        self._pull_enabled = pull_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other