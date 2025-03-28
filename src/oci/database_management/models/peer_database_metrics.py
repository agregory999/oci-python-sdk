# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PeerDatabaseMetrics(object):
    """
    The summary of resource usage metrics for the peer database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PeerDatabaseMetrics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param peer_db_metrics:
            The value to assign to the peer_db_metrics property of this PeerDatabaseMetrics.
        :type peer_db_metrics: list[oci.database_management.models.DatabaseUsageMetrics]

        """
        self.swagger_types = {
            'peer_db_metrics': 'list[DatabaseUsageMetrics]'
        }
        self.attribute_map = {
            'peer_db_metrics': 'peerDbMetrics'
        }
        self._peer_db_metrics = None

    @property
    def peer_db_metrics(self):
        """
        **[Required]** Gets the peer_db_metrics of this PeerDatabaseMetrics.
        A list of resource usage metrics for the peer database.


        :return: The peer_db_metrics of this PeerDatabaseMetrics.
        :rtype: list[oci.database_management.models.DatabaseUsageMetrics]
        """
        return self._peer_db_metrics

    @peer_db_metrics.setter
    def peer_db_metrics(self, peer_db_metrics):
        """
        Sets the peer_db_metrics of this PeerDatabaseMetrics.
        A list of resource usage metrics for the peer database.


        :param peer_db_metrics: The peer_db_metrics of this PeerDatabaseMetrics.
        :type: list[oci.database_management.models.DatabaseUsageMetrics]
        """
        self._peer_db_metrics = peer_db_metrics

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
