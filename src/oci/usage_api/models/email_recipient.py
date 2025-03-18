# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200107


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EmailRecipient(object):
    """
    The email recipient to receive usage statements for the subscription.
    """

    #: A constant which can be used with the lifecycle_state property of a EmailRecipient.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a EmailRecipient.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new EmailRecipient object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param first_name:
            The value to assign to the first_name property of this EmailRecipient.
        :type first_name: str

        :param last_name:
            The value to assign to the last_name property of this EmailRecipient.
        :type last_name: str

        :param email_id:
            The value to assign to the email_id property of this EmailRecipient.
        :type email_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this EmailRecipient.
            Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'first_name': 'str',
            'last_name': 'str',
            'email_id': 'str',
            'lifecycle_state': 'str'
        }
        self.attribute_map = {
            'first_name': 'firstName',
            'last_name': 'lastName',
            'email_id': 'emailId',
            'lifecycle_state': 'lifecycleState'
        }
        self._first_name = None
        self._last_name = None
        self._email_id = None
        self._lifecycle_state = None

    @property
    def first_name(self):
        """
        Gets the first_name of this EmailRecipient.
        the first name of the recipient.


        :return: The first_name of this EmailRecipient.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this EmailRecipient.
        the first name of the recipient.


        :param first_name: The first_name of this EmailRecipient.
        :type: str
        """
        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this EmailRecipient.
        the last name of the recipient.


        :return: The last_name of this EmailRecipient.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this EmailRecipient.
        the last name of the recipient.


        :param last_name: The last_name of this EmailRecipient.
        :type: str
        """
        self._last_name = last_name

    @property
    def email_id(self):
        """
        **[Required]** Gets the email_id of this EmailRecipient.
        the email of the recipient.


        :return: The email_id of this EmailRecipient.
        :rtype: str
        """
        return self._email_id

    @email_id.setter
    def email_id(self, email_id):
        """
        Sets the email_id of this EmailRecipient.
        the email of the recipient.


        :param email_id: The email_id of this EmailRecipient.
        :type: str
        """
        self._email_id = email_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this EmailRecipient.
        The email recipient lifecycle state.

        Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this EmailRecipient.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this EmailRecipient.
        The email recipient lifecycle state.


        :param lifecycle_state: The lifecycle_state of this EmailRecipient.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
