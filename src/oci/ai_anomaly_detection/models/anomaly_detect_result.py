# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AnomalyDetectResult(object):
    """
    Results of the detect anomalies call.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AnomalyDetectResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param detection_results:
            The value to assign to the detection_results property of this AnomalyDetectResult.
        :type detection_results: list[oci.ai_anomaly_detection.models.DetectionResultItem]

        """
        self.swagger_types = {
            'detection_results': 'list[DetectionResultItem]'
        }
        self.attribute_map = {
            'detection_results': 'detectionResults'
        }
        self._detection_results = None

    @property
    def detection_results(self):
        """
        **[Required]** Gets the detection_results of this AnomalyDetectResult.
        A list to hold anomaly points grouped by timestamp/row.


        :return: The detection_results of this AnomalyDetectResult.
        :rtype: list[oci.ai_anomaly_detection.models.DetectionResultItem]
        """
        return self._detection_results

    @detection_results.setter
    def detection_results(self, detection_results):
        """
        Sets the detection_results of this AnomalyDetectResult.
        A list to hold anomaly points grouped by timestamp/row.


        :param detection_results: The detection_results of this AnomalyDetectResult.
        :type: list[oci.ai_anomaly_detection.models.DetectionResultItem]
        """
        self._detection_results = detection_results

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
