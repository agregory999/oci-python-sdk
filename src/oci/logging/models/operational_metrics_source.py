# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OperationalMetricsSource(object):
    """
    Unified monitoring agent operational metrics source object.
    """

    #: A constant which can be used with the type property of a OperationalMetricsSource.
    #: This constant has a value of "UMA_METRICS"
    TYPE_UMA_METRICS = "UMA_METRICS"

    def __init__(self, **kwargs):
        """
        Initializes a new OperationalMetricsSource object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this OperationalMetricsSource.
            Allowed values for this property are: "UMA_METRICS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param metrics:
            The value to assign to the metrics property of this OperationalMetricsSource.
        :type metrics: list[str]

        :param record_input:
            The value to assign to the record_input property of this OperationalMetricsSource.
        :type record_input: oci.logging.models.OperationalMetricsRecordInput

        """
        self.swagger_types = {
            'type': 'str',
            'metrics': 'list[str]',
            'record_input': 'OperationalMetricsRecordInput'
        }
        self.attribute_map = {
            'type': 'type',
            'metrics': 'metrics',
            'record_input': 'recordInput'
        }
        self._type = None
        self._metrics = None
        self._record_input = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this OperationalMetricsSource.
        Type of the unified monitoring agent operational metrics source object.

        Allowed values for this property are: "UMA_METRICS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this OperationalMetricsSource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this OperationalMetricsSource.
        Type of the unified monitoring agent operational metrics source object.


        :param type: The type of this OperationalMetricsSource.
        :type: str
        """
        allowed_values = ["UMA_METRICS"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def metrics(self):
        """
        Gets the metrics of this OperationalMetricsSource.
        List of unified monitoring agent operational metrics.


        :return: The metrics of this OperationalMetricsSource.
        :rtype: list[str]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """
        Sets the metrics of this OperationalMetricsSource.
        List of unified monitoring agent operational metrics.


        :param metrics: The metrics of this OperationalMetricsSource.
        :type: list[str]
        """
        self._metrics = metrics

    @property
    def record_input(self):
        """
        **[Required]** Gets the record_input of this OperationalMetricsSource.

        :return: The record_input of this OperationalMetricsSource.
        :rtype: oci.logging.models.OperationalMetricsRecordInput
        """
        return self._record_input

    @record_input.setter
    def record_input(self, record_input):
        """
        Sets the record_input of this OperationalMetricsSource.

        :param record_input: The record_input of this OperationalMetricsSource.
        :type: oci.logging.models.OperationalMetricsRecordInput
        """
        self._record_input = record_input

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
