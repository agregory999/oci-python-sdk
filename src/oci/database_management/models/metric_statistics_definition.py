# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MetricStatisticsDefinition(object):
    """
    The metric statistics values with dimension details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MetricStatisticsDefinition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param min:
            The value to assign to the min property of this MetricStatisticsDefinition.
        :type min: float

        :param max:
            The value to assign to the max property of this MetricStatisticsDefinition.
        :type max: float

        :param median:
            The value to assign to the median property of this MetricStatisticsDefinition.
        :type median: float

        :param lower_quartile:
            The value to assign to the lower_quartile property of this MetricStatisticsDefinition.
        :type lower_quartile: float

        :param upper_quartile:
            The value to assign to the upper_quartile property of this MetricStatisticsDefinition.
        :type upper_quartile: float

        :param unit:
            The value to assign to the unit property of this MetricStatisticsDefinition.
        :type unit: str

        :param dimensions:
            The value to assign to the dimensions property of this MetricStatisticsDefinition.
        :type dimensions: list[oci.database_management.models.MetricDimensionDefinition]

        """
        self.swagger_types = {
            'min': 'float',
            'max': 'float',
            'median': 'float',
            'lower_quartile': 'float',
            'upper_quartile': 'float',
            'unit': 'str',
            'dimensions': 'list[MetricDimensionDefinition]'
        }
        self.attribute_map = {
            'min': 'min',
            'max': 'max',
            'median': 'median',
            'lower_quartile': 'lowerQuartile',
            'upper_quartile': 'upperQuartile',
            'unit': 'unit',
            'dimensions': 'dimensions'
        }
        self._min = None
        self._max = None
        self._median = None
        self._lower_quartile = None
        self._upper_quartile = None
        self._unit = None
        self._dimensions = None

    @property
    def min(self):
        """
        Gets the min of this MetricStatisticsDefinition.
        The minimum value of the metric.


        :return: The min of this MetricStatisticsDefinition.
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """
        Sets the min of this MetricStatisticsDefinition.
        The minimum value of the metric.


        :param min: The min of this MetricStatisticsDefinition.
        :type: float
        """
        self._min = min

    @property
    def max(self):
        """
        Gets the max of this MetricStatisticsDefinition.
        The maximum value of the metric.


        :return: The max of this MetricStatisticsDefinition.
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """
        Sets the max of this MetricStatisticsDefinition.
        The maximum value of the metric.


        :param max: The max of this MetricStatisticsDefinition.
        :type: float
        """
        self._max = max

    @property
    def median(self):
        """
        Gets the median of this MetricStatisticsDefinition.
        The median value of the metric.


        :return: The median of this MetricStatisticsDefinition.
        :rtype: float
        """
        return self._median

    @median.setter
    def median(self, median):
        """
        Sets the median of this MetricStatisticsDefinition.
        The median value of the metric.


        :param median: The median of this MetricStatisticsDefinition.
        :type: float
        """
        self._median = median

    @property
    def lower_quartile(self):
        """
        Gets the lower_quartile of this MetricStatisticsDefinition.
        The first quartile value of the metric.


        :return: The lower_quartile of this MetricStatisticsDefinition.
        :rtype: float
        """
        return self._lower_quartile

    @lower_quartile.setter
    def lower_quartile(self, lower_quartile):
        """
        Sets the lower_quartile of this MetricStatisticsDefinition.
        The first quartile value of the metric.


        :param lower_quartile: The lower_quartile of this MetricStatisticsDefinition.
        :type: float
        """
        self._lower_quartile = lower_quartile

    @property
    def upper_quartile(self):
        """
        Gets the upper_quartile of this MetricStatisticsDefinition.
        The third quartile value of the metric.


        :return: The upper_quartile of this MetricStatisticsDefinition.
        :rtype: float
        """
        return self._upper_quartile

    @upper_quartile.setter
    def upper_quartile(self, upper_quartile):
        """
        Sets the upper_quartile of this MetricStatisticsDefinition.
        The third quartile value of the metric.


        :param upper_quartile: The upper_quartile of this MetricStatisticsDefinition.
        :type: float
        """
        self._upper_quartile = upper_quartile

    @property
    def unit(self):
        """
        Gets the unit of this MetricStatisticsDefinition.
        The unit of the metric value.


        :return: The unit of this MetricStatisticsDefinition.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this MetricStatisticsDefinition.
        The unit of the metric value.


        :param unit: The unit of this MetricStatisticsDefinition.
        :type: str
        """
        self._unit = unit

    @property
    def dimensions(self):
        """
        Gets the dimensions of this MetricStatisticsDefinition.
        The dimensions of the metric.


        :return: The dimensions of this MetricStatisticsDefinition.
        :rtype: list[oci.database_management.models.MetricDimensionDefinition]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this MetricStatisticsDefinition.
        The dimensions of the metric.


        :param dimensions: The dimensions of this MetricStatisticsDefinition.
        :type: list[oci.database_management.models.MetricDimensionDefinition]
        """
        self._dimensions = dimensions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
