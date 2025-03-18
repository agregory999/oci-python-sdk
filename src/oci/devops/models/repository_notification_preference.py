# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RepositoryNotificationPreference(object):
    """
    The notification preference of the repository.
    """

    #: A constant which can be used with the notification_preference property of a RepositoryNotificationPreference.
    #: This constant has a value of "WATCH"
    NOTIFICATION_PREFERENCE_WATCH = "WATCH"

    #: A constant which can be used with the notification_preference property of a RepositoryNotificationPreference.
    #: This constant has a value of "IGNORE"
    NOTIFICATION_PREFERENCE_IGNORE = "IGNORE"

    #: A constant which can be used with the notification_preference property of a RepositoryNotificationPreference.
    #: This constant has a value of "MENTION"
    NOTIFICATION_PREFERENCE_MENTION = "MENTION"

    #: A constant which can be used with the notification_preference property of a RepositoryNotificationPreference.
    #: This constant has a value of "INHERITED"
    NOTIFICATION_PREFERENCE_INHERITED = "INHERITED"

    def __init__(self, **kwargs):
        """
        Initializes a new RepositoryNotificationPreference object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param repository_id:
            The value to assign to the repository_id property of this RepositoryNotificationPreference.
        :type repository_id: str

        :param user_id:
            The value to assign to the user_id property of this RepositoryNotificationPreference.
        :type user_id: str

        :param notification_preference:
            The value to assign to the notification_preference property of this RepositoryNotificationPreference.
            Allowed values for this property are: "WATCH", "IGNORE", "MENTION", "INHERITED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type notification_preference: str

        """
        self.swagger_types = {
            'repository_id': 'str',
            'user_id': 'str',
            'notification_preference': 'str'
        }
        self.attribute_map = {
            'repository_id': 'repositoryId',
            'user_id': 'userId',
            'notification_preference': 'notificationPreference'
        }
        self._repository_id = None
        self._user_id = None
        self._notification_preference = None

    @property
    def repository_id(self):
        """
        **[Required]** Gets the repository_id of this RepositoryNotificationPreference.
        The ocid of repository resource


        :return: The repository_id of this RepositoryNotificationPreference.
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """
        Sets the repository_id of this RepositoryNotificationPreference.
        The ocid of repository resource


        :param repository_id: The repository_id of this RepositoryNotificationPreference.
        :type: str
        """
        self._repository_id = repository_id

    @property
    def user_id(self):
        """
        **[Required]** Gets the user_id of this RepositoryNotificationPreference.
        The ocid of user.


        :return: The user_id of this RepositoryNotificationPreference.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this RepositoryNotificationPreference.
        The ocid of user.


        :param user_id: The user_id of this RepositoryNotificationPreference.
        :type: str
        """
        self._user_id = user_id

    @property
    def notification_preference(self):
        """
        **[Required]** Gets the notification_preference of this RepositoryNotificationPreference.
        The override value of repository notification preference.

        Allowed values for this property are: "WATCH", "IGNORE", "MENTION", "INHERITED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The notification_preference of this RepositoryNotificationPreference.
        :rtype: str
        """
        return self._notification_preference

    @notification_preference.setter
    def notification_preference(self, notification_preference):
        """
        Sets the notification_preference of this RepositoryNotificationPreference.
        The override value of repository notification preference.


        :param notification_preference: The notification_preference of this RepositoryNotificationPreference.
        :type: str
        """
        allowed_values = ["WATCH", "IGNORE", "MENTION", "INHERITED"]
        if not value_allowed_none_or_none_sentinel(notification_preference, allowed_values):
            notification_preference = 'UNKNOWN_ENUM_VALUE'
        self._notification_preference = notification_preference

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
