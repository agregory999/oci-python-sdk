# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateNodeReplaceConfigurationDetails(object):
    """
    The information about the NodeReplaceConfiguration
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateNodeReplaceConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param level_type_details:
            The value to assign to the level_type_details property of this CreateNodeReplaceConfigurationDetails.
        :type level_type_details: oci.bds.models.LevelTypeDetails

        :param display_name:
            The value to assign to the display_name property of this CreateNodeReplaceConfigurationDetails.
        :type display_name: str

        :param cluster_admin_password:
            The value to assign to the cluster_admin_password property of this CreateNodeReplaceConfigurationDetails.
        :type cluster_admin_password: str

        :param metric_type:
            The value to assign to the metric_type property of this CreateNodeReplaceConfigurationDetails.
        :type metric_type: str

        :param duration_in_minutes:
            The value to assign to the duration_in_minutes property of this CreateNodeReplaceConfigurationDetails.
        :type duration_in_minutes: int

        """
        self.swagger_types = {
            'level_type_details': 'LevelTypeDetails',
            'display_name': 'str',
            'cluster_admin_password': 'str',
            'metric_type': 'str',
            'duration_in_minutes': 'int'
        }
        self.attribute_map = {
            'level_type_details': 'levelTypeDetails',
            'display_name': 'displayName',
            'cluster_admin_password': 'clusterAdminPassword',
            'metric_type': 'metricType',
            'duration_in_minutes': 'durationInMinutes'
        }
        self._level_type_details = None
        self._display_name = None
        self._cluster_admin_password = None
        self._metric_type = None
        self._duration_in_minutes = None

    @property
    def level_type_details(self):
        """
        **[Required]** Gets the level_type_details of this CreateNodeReplaceConfigurationDetails.

        :return: The level_type_details of this CreateNodeReplaceConfigurationDetails.
        :rtype: oci.bds.models.LevelTypeDetails
        """
        return self._level_type_details

    @level_type_details.setter
    def level_type_details(self, level_type_details):
        """
        Sets the level_type_details of this CreateNodeReplaceConfigurationDetails.

        :param level_type_details: The level_type_details of this CreateNodeReplaceConfigurationDetails.
        :type: oci.bds.models.LevelTypeDetails
        """
        self._level_type_details = level_type_details

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateNodeReplaceConfigurationDetails.
        A user-friendly name. Only ASCII alphanumeric characters with no spaces allowed. The name does not have to be unique, and it may be changed. Avoid entering confidential information.


        :return: The display_name of this CreateNodeReplaceConfigurationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateNodeReplaceConfigurationDetails.
        A user-friendly name. Only ASCII alphanumeric characters with no spaces allowed. The name does not have to be unique, and it may be changed. Avoid entering confidential information.


        :param display_name: The display_name of this CreateNodeReplaceConfigurationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def cluster_admin_password(self):
        """
        **[Required]** Gets the cluster_admin_password of this CreateNodeReplaceConfigurationDetails.
        Base-64 encoded password for the cluster admin user.


        :return: The cluster_admin_password of this CreateNodeReplaceConfigurationDetails.
        :rtype: str
        """
        return self._cluster_admin_password

    @cluster_admin_password.setter
    def cluster_admin_password(self, cluster_admin_password):
        """
        Sets the cluster_admin_password of this CreateNodeReplaceConfigurationDetails.
        Base-64 encoded password for the cluster admin user.


        :param cluster_admin_password: The cluster_admin_password of this CreateNodeReplaceConfigurationDetails.
        :type: str
        """
        self._cluster_admin_password = cluster_admin_password

    @property
    def metric_type(self):
        """
        **[Required]** Gets the metric_type of this CreateNodeReplaceConfigurationDetails.
        Type of compute instance health metric to use for node replacement


        :return: The metric_type of this CreateNodeReplaceConfigurationDetails.
        :rtype: str
        """
        return self._metric_type

    @metric_type.setter
    def metric_type(self, metric_type):
        """
        Sets the metric_type of this CreateNodeReplaceConfigurationDetails.
        Type of compute instance health metric to use for node replacement


        :param metric_type: The metric_type of this CreateNodeReplaceConfigurationDetails.
        :type: str
        """
        self._metric_type = metric_type

    @property
    def duration_in_minutes(self):
        """
        **[Required]** Gets the duration_in_minutes of this CreateNodeReplaceConfigurationDetails.
        This value is the minimum period of time to wait before triggering node replacement. The value is in minutes.


        :return: The duration_in_minutes of this CreateNodeReplaceConfigurationDetails.
        :rtype: int
        """
        return self._duration_in_minutes

    @duration_in_minutes.setter
    def duration_in_minutes(self, duration_in_minutes):
        """
        Sets the duration_in_minutes of this CreateNodeReplaceConfigurationDetails.
        This value is the minimum period of time to wait before triggering node replacement. The value is in minutes.


        :param duration_in_minutes: The duration_in_minutes of this CreateNodeReplaceConfigurationDetails.
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
