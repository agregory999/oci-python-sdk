# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210610


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PluginErrorAggregationSummary(object):
    """
    High level view of plugin error aggregations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PluginErrorAggregationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param healthy_plugin_count:
            The value to assign to the healthy_plugin_count property of this PluginErrorAggregationSummary.
        :type healthy_plugin_count: int

        :param plugin_error_aggregations:
            The value to assign to the plugin_error_aggregations property of this PluginErrorAggregationSummary.
        :type plugin_error_aggregations: list[oci.jms.models.PluginErrorAggregation]

        """
        self.swagger_types = {
            'healthy_plugin_count': 'int',
            'plugin_error_aggregations': 'list[PluginErrorAggregation]'
        }
        self.attribute_map = {
            'healthy_plugin_count': 'healthyPluginCount',
            'plugin_error_aggregations': 'pluginErrorAggregations'
        }
        self._healthy_plugin_count = None
        self._plugin_error_aggregations = None

    @property
    def healthy_plugin_count(self):
        """
        **[Required]** Gets the healthy_plugin_count of this PluginErrorAggregationSummary.
        Count of plugins with no problems.


        :return: The healthy_plugin_count of this PluginErrorAggregationSummary.
        :rtype: int
        """
        return self._healthy_plugin_count

    @healthy_plugin_count.setter
    def healthy_plugin_count(self, healthy_plugin_count):
        """
        Sets the healthy_plugin_count of this PluginErrorAggregationSummary.
        Count of plugins with no problems.


        :param healthy_plugin_count: The healthy_plugin_count of this PluginErrorAggregationSummary.
        :type: int
        """
        self._healthy_plugin_count = healthy_plugin_count

    @property
    def plugin_error_aggregations(self):
        """
        **[Required]** Gets the plugin_error_aggregations of this PluginErrorAggregationSummary.
        List of plugin aggregation errors.


        :return: The plugin_error_aggregations of this PluginErrorAggregationSummary.
        :rtype: list[oci.jms.models.PluginErrorAggregation]
        """
        return self._plugin_error_aggregations

    @plugin_error_aggregations.setter
    def plugin_error_aggregations(self, plugin_error_aggregations):
        """
        Sets the plugin_error_aggregations of this PluginErrorAggregationSummary.
        List of plugin aggregation errors.


        :param plugin_error_aggregations: The plugin_error_aggregations of this PluginErrorAggregationSummary.
        :type: list[oci.jms.models.PluginErrorAggregation]
        """
        self._plugin_error_aggregations = plugin_error_aggregations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
