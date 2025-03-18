# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VideoFeature(object):
    """
    Details about a video feature request.
    """

    #: A constant which can be used with the feature_type property of a VideoFeature.
    #: This constant has a value of "LABEL_DETECTION"
    FEATURE_TYPE_LABEL_DETECTION = "LABEL_DETECTION"

    #: A constant which can be used with the feature_type property of a VideoFeature.
    #: This constant has a value of "OBJECT_DETECTION"
    FEATURE_TYPE_OBJECT_DETECTION = "OBJECT_DETECTION"

    #: A constant which can be used with the feature_type property of a VideoFeature.
    #: This constant has a value of "TEXT_DETECTION"
    FEATURE_TYPE_TEXT_DETECTION = "TEXT_DETECTION"

    #: A constant which can be used with the feature_type property of a VideoFeature.
    #: This constant has a value of "FACE_DETECTION"
    FEATURE_TYPE_FACE_DETECTION = "FACE_DETECTION"

    #: A constant which can be used with the feature_type property of a VideoFeature.
    #: This constant has a value of "OBJECT_TRACKING"
    FEATURE_TYPE_OBJECT_TRACKING = "OBJECT_TRACKING"

    def __init__(self, **kwargs):
        """
        Initializes a new VideoFeature object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.ai_vision.models.VideoObjectDetectionFeature`
        * :class:`~oci.ai_vision.models.VideoFaceDetectionFeature`
        * :class:`~oci.ai_vision.models.VideoTextDetectionFeature`
        * :class:`~oci.ai_vision.models.VideoObjectTrackingFeature`
        * :class:`~oci.ai_vision.models.VideoLabelDetectionFeature`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param feature_type:
            The value to assign to the feature_type property of this VideoFeature.
            Allowed values for this property are: "LABEL_DETECTION", "OBJECT_DETECTION", "TEXT_DETECTION", "FACE_DETECTION", "OBJECT_TRACKING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type feature_type: str

        """
        self.swagger_types = {
            'feature_type': 'str'
        }
        self.attribute_map = {
            'feature_type': 'featureType'
        }
        self._feature_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['featureType']

        if type == 'OBJECT_DETECTION':
            return 'VideoObjectDetectionFeature'

        if type == 'FACE_DETECTION':
            return 'VideoFaceDetectionFeature'

        if type == 'TEXT_DETECTION':
            return 'VideoTextDetectionFeature'

        if type == 'OBJECT_TRACKING':
            return 'VideoObjectTrackingFeature'

        if type == 'LABEL_DETECTION':
            return 'VideoLabelDetectionFeature'
        else:
            return 'VideoFeature'

    @property
    def feature_type(self):
        """
        **[Required]** Gets the feature_type of this VideoFeature.
        The feature of video analysis.
        Allowed values are:
        - LABEL_DETECTION: Label detection feature(IC).
        - OBJECT_DETECTION: Object detection feature(OD).
        - TEXT_DETECTION: Text detection feature(OCR).
        - FACE_DETECTION: Face detection feature(fd).
        - OBJECT_TRACKING: Object tracking feature(OT).

        Allowed values for this property are: "LABEL_DETECTION", "OBJECT_DETECTION", "TEXT_DETECTION", "FACE_DETECTION", "OBJECT_TRACKING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The feature_type of this VideoFeature.
        :rtype: str
        """
        return self._feature_type

    @feature_type.setter
    def feature_type(self, feature_type):
        """
        Sets the feature_type of this VideoFeature.
        The feature of video analysis.
        Allowed values are:
        - LABEL_DETECTION: Label detection feature(IC).
        - OBJECT_DETECTION: Object detection feature(OD).
        - TEXT_DETECTION: Text detection feature(OCR).
        - FACE_DETECTION: Face detection feature(fd).
        - OBJECT_TRACKING: Object tracking feature(OT).


        :param feature_type: The feature_type of this VideoFeature.
        :type: str
        """
        allowed_values = ["LABEL_DETECTION", "OBJECT_DETECTION", "TEXT_DETECTION", "FACE_DETECTION", "OBJECT_TRACKING"]
        if not value_allowed_none_or_none_sentinel(feature_type, allowed_values):
            feature_type = 'UNKNOWN_ENUM_VALUE'
        self._feature_type = feature_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
