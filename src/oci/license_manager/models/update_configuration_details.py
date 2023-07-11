# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220430


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateConfigurationDetails(object):
    """
    The compartment-specific configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param email_ids:
            The value to assign to the email_ids property of this UpdateConfigurationDetails.
        :type email_ids: list[str]

        """
        self.swagger_types = {
            'email_ids': 'list[str]'
        }

        self.attribute_map = {
            'email_ids': 'emailIds'
        }

        self._email_ids = None

    @property
    def email_ids(self):
        """
        **[Required]** Gets the email_ids of this UpdateConfigurationDetails.
        List of email IDs associated with the configuration.


        :return: The email_ids of this UpdateConfigurationDetails.
        :rtype: list[str]
        """
        return self._email_ids

    @email_ids.setter
    def email_ids(self, email_ids):
        """
        Sets the email_ids of this UpdateConfigurationDetails.
        List of email IDs associated with the configuration.


        :param email_ids: The email_ids of this UpdateConfigurationDetails.
        :type: list[str]
        """
        self._email_ids = email_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
