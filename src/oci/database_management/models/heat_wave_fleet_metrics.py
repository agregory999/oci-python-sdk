# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HeatWaveFleetMetrics(object):
    """
    The details of the HeatWave cluster fleet health metrics.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HeatWaveFleetMetrics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param start_time:
            The value to assign to the start_time property of this HeatWaveFleetMetrics.
        :type start_time: str

        :param end_time:
            The value to assign to the end_time property of this HeatWaveFleetMetrics.
        :type end_time: str

        :param fleet_clusters:
            The value to assign to the fleet_clusters property of this HeatWaveFleetMetrics.
        :type fleet_clusters: list[oci.database_management.models.HeatWaveClusterUsageMetrics]

        :param fleet_summary:
            The value to assign to the fleet_summary property of this HeatWaveFleetMetrics.
        :type fleet_summary: list[oci.database_management.models.HeatWaveFleetSummary]

        """
        self.swagger_types = {
            'start_time': 'str',
            'end_time': 'str',
            'fleet_clusters': 'list[HeatWaveClusterUsageMetrics]',
            'fleet_summary': 'list[HeatWaveFleetSummary]'
        }
        self.attribute_map = {
            'start_time': 'startTime',
            'end_time': 'endTime',
            'fleet_clusters': 'fleetClusters',
            'fleet_summary': 'fleetSummary'
        }
        self._start_time = None
        self._end_time = None
        self._fleet_clusters = None
        self._fleet_summary = None

    @property
    def start_time(self):
        """
        **[Required]** Gets the start_time of this HeatWaveFleetMetrics.
        The beginning of the time range during which metric data is retrieved.


        :return: The start_time of this HeatWaveFleetMetrics.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this HeatWaveFleetMetrics.
        The beginning of the time range during which metric data is retrieved.


        :param start_time: The start_time of this HeatWaveFleetMetrics.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """
        **[Required]** Gets the end_time of this HeatWaveFleetMetrics.
        The end of the time range during which metric data is retrieved.


        :return: The end_time of this HeatWaveFleetMetrics.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this HeatWaveFleetMetrics.
        The end of the time range during which metric data is retrieved.


        :param end_time: The end_time of this HeatWaveFleetMetrics.
        :type: str
        """
        self._end_time = end_time

    @property
    def fleet_clusters(self):
        """
        **[Required]** Gets the fleet_clusters of this HeatWaveFleetMetrics.
        The list of HeatWave clusters in the fleet and their usage metrics.


        :return: The fleet_clusters of this HeatWaveFleetMetrics.
        :rtype: list[oci.database_management.models.HeatWaveClusterUsageMetrics]
        """
        return self._fleet_clusters

    @fleet_clusters.setter
    def fleet_clusters(self, fleet_clusters):
        """
        Sets the fleet_clusters of this HeatWaveFleetMetrics.
        The list of HeatWave clusters in the fleet and their usage metrics.


        :param fleet_clusters: The fleet_clusters of this HeatWaveFleetMetrics.
        :type: list[oci.database_management.models.HeatWaveClusterUsageMetrics]
        """
        self._fleet_clusters = fleet_clusters

    @property
    def fleet_summary(self):
        """
        **[Required]** Gets the fleet_summary of this HeatWaveFleetMetrics.
        The number of HeatWave clusters in the fleet and a summary of the metrics that provide the aggregated usage of CPU, storage, and so on of all the clusters.


        :return: The fleet_summary of this HeatWaveFleetMetrics.
        :rtype: list[oci.database_management.models.HeatWaveFleetSummary]
        """
        return self._fleet_summary

    @fleet_summary.setter
    def fleet_summary(self, fleet_summary):
        """
        Sets the fleet_summary of this HeatWaveFleetMetrics.
        The number of HeatWave clusters in the fleet and a summary of the metrics that provide the aggregated usage of CPU, storage, and so on of all the clusters.


        :param fleet_summary: The fleet_summary of this HeatWaveFleetMetrics.
        :type: list[oci.database_management.models.HeatWaveFleetSummary]
        """
        self._fleet_summary = fleet_summary

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
