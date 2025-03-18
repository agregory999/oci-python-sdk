# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AnalyzeVideoResult(object):
    """
    Video analysis results.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AnalyzeVideoResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param video_metadata:
            The value to assign to the video_metadata property of this AnalyzeVideoResult.
        :type video_metadata: oci.ai_vision.models.VideoMetadata

        :param video_labels:
            The value to assign to the video_labels property of this AnalyzeVideoResult.
        :type video_labels: list[oci.ai_vision.models.VideoLabel]

        :param video_objects:
            The value to assign to the video_objects property of this AnalyzeVideoResult.
        :type video_objects: list[oci.ai_vision.models.VideoObject]

        :param video_tracked_objects:
            The value to assign to the video_tracked_objects property of this AnalyzeVideoResult.
        :type video_tracked_objects: list[oci.ai_vision.models.VideoTrackedObject]

        :param video_text:
            The value to assign to the video_text property of this AnalyzeVideoResult.
        :type video_text: list[oci.ai_vision.models.VideoText]

        :param video_faces:
            The value to assign to the video_faces property of this AnalyzeVideoResult.
        :type video_faces: list[oci.ai_vision.models.VideoFace]

        :param ontology_classes:
            The value to assign to the ontology_classes property of this AnalyzeVideoResult.
        :type ontology_classes: list[oci.ai_vision.models.OntologyClass]

        :param label_detection_model_version:
            The value to assign to the label_detection_model_version property of this AnalyzeVideoResult.
        :type label_detection_model_version: str

        :param object_detection_model_version:
            The value to assign to the object_detection_model_version property of this AnalyzeVideoResult.
        :type object_detection_model_version: str

        :param object_tracking_model_version:
            The value to assign to the object_tracking_model_version property of this AnalyzeVideoResult.
        :type object_tracking_model_version: str

        :param text_detection_model_version:
            The value to assign to the text_detection_model_version property of this AnalyzeVideoResult.
        :type text_detection_model_version: str

        :param face_detection_model_version:
            The value to assign to the face_detection_model_version property of this AnalyzeVideoResult.
        :type face_detection_model_version: str

        :param errors:
            The value to assign to the errors property of this AnalyzeVideoResult.
        :type errors: list[oci.ai_vision.models.ProcessingError]

        """
        self.swagger_types = {
            'video_metadata': 'VideoMetadata',
            'video_labels': 'list[VideoLabel]',
            'video_objects': 'list[VideoObject]',
            'video_tracked_objects': 'list[VideoTrackedObject]',
            'video_text': 'list[VideoText]',
            'video_faces': 'list[VideoFace]',
            'ontology_classes': 'list[OntologyClass]',
            'label_detection_model_version': 'str',
            'object_detection_model_version': 'str',
            'object_tracking_model_version': 'str',
            'text_detection_model_version': 'str',
            'face_detection_model_version': 'str',
            'errors': 'list[ProcessingError]'
        }
        self.attribute_map = {
            'video_metadata': 'videoMetadata',
            'video_labels': 'videoLabels',
            'video_objects': 'videoObjects',
            'video_tracked_objects': 'videoTrackedObjects',
            'video_text': 'videoText',
            'video_faces': 'videoFaces',
            'ontology_classes': 'ontologyClasses',
            'label_detection_model_version': 'labelDetectionModelVersion',
            'object_detection_model_version': 'objectDetectionModelVersion',
            'object_tracking_model_version': 'objectTrackingModelVersion',
            'text_detection_model_version': 'textDetectionModelVersion',
            'face_detection_model_version': 'faceDetectionModelVersion',
            'errors': 'errors'
        }
        self._video_metadata = None
        self._video_labels = None
        self._video_objects = None
        self._video_tracked_objects = None
        self._video_text = None
        self._video_faces = None
        self._ontology_classes = None
        self._label_detection_model_version = None
        self._object_detection_model_version = None
        self._object_tracking_model_version = None
        self._text_detection_model_version = None
        self._face_detection_model_version = None
        self._errors = None

    @property
    def video_metadata(self):
        """
        **[Required]** Gets the video_metadata of this AnalyzeVideoResult.

        :return: The video_metadata of this AnalyzeVideoResult.
        :rtype: oci.ai_vision.models.VideoMetadata
        """
        return self._video_metadata

    @video_metadata.setter
    def video_metadata(self, video_metadata):
        """
        Sets the video_metadata of this AnalyzeVideoResult.

        :param video_metadata: The video_metadata of this AnalyzeVideoResult.
        :type: oci.ai_vision.models.VideoMetadata
        """
        self._video_metadata = video_metadata

    @property
    def video_labels(self):
        """
        Gets the video_labels of this AnalyzeVideoResult.
        Detected labels in a video.


        :return: The video_labels of this AnalyzeVideoResult.
        :rtype: list[oci.ai_vision.models.VideoLabel]
        """
        return self._video_labels

    @video_labels.setter
    def video_labels(self, video_labels):
        """
        Sets the video_labels of this AnalyzeVideoResult.
        Detected labels in a video.


        :param video_labels: The video_labels of this AnalyzeVideoResult.
        :type: list[oci.ai_vision.models.VideoLabel]
        """
        self._video_labels = video_labels

    @property
    def video_objects(self):
        """
        Gets the video_objects of this AnalyzeVideoResult.
        Detected objects in a video.


        :return: The video_objects of this AnalyzeVideoResult.
        :rtype: list[oci.ai_vision.models.VideoObject]
        """
        return self._video_objects

    @video_objects.setter
    def video_objects(self, video_objects):
        """
        Sets the video_objects of this AnalyzeVideoResult.
        Detected objects in a video.


        :param video_objects: The video_objects of this AnalyzeVideoResult.
        :type: list[oci.ai_vision.models.VideoObject]
        """
        self._video_objects = video_objects

    @property
    def video_tracked_objects(self):
        """
        Gets the video_tracked_objects of this AnalyzeVideoResult.
        Tracked objects in a video.


        :return: The video_tracked_objects of this AnalyzeVideoResult.
        :rtype: list[oci.ai_vision.models.VideoTrackedObject]
        """
        return self._video_tracked_objects

    @video_tracked_objects.setter
    def video_tracked_objects(self, video_tracked_objects):
        """
        Sets the video_tracked_objects of this AnalyzeVideoResult.
        Tracked objects in a video.


        :param video_tracked_objects: The video_tracked_objects of this AnalyzeVideoResult.
        :type: list[oci.ai_vision.models.VideoTrackedObject]
        """
        self._video_tracked_objects = video_tracked_objects

    @property
    def video_text(self):
        """
        Gets the video_text of this AnalyzeVideoResult.
        Detected text in a video.


        :return: The video_text of this AnalyzeVideoResult.
        :rtype: list[oci.ai_vision.models.VideoText]
        """
        return self._video_text

    @video_text.setter
    def video_text(self, video_text):
        """
        Sets the video_text of this AnalyzeVideoResult.
        Detected text in a video.


        :param video_text: The video_text of this AnalyzeVideoResult.
        :type: list[oci.ai_vision.models.VideoText]
        """
        self._video_text = video_text

    @property
    def video_faces(self):
        """
        Gets the video_faces of this AnalyzeVideoResult.
        Detected faces in a video.


        :return: The video_faces of this AnalyzeVideoResult.
        :rtype: list[oci.ai_vision.models.VideoFace]
        """
        return self._video_faces

    @video_faces.setter
    def video_faces(self, video_faces):
        """
        Sets the video_faces of this AnalyzeVideoResult.
        Detected faces in a video.


        :param video_faces: The video_faces of this AnalyzeVideoResult.
        :type: list[oci.ai_vision.models.VideoFace]
        """
        self._video_faces = video_faces

    @property
    def ontology_classes(self):
        """
        Gets the ontology_classes of this AnalyzeVideoResult.
        The ontologyClasses of video labels.


        :return: The ontology_classes of this AnalyzeVideoResult.
        :rtype: list[oci.ai_vision.models.OntologyClass]
        """
        return self._ontology_classes

    @ontology_classes.setter
    def ontology_classes(self, ontology_classes):
        """
        Sets the ontology_classes of this AnalyzeVideoResult.
        The ontologyClasses of video labels.


        :param ontology_classes: The ontology_classes of this AnalyzeVideoResult.
        :type: list[oci.ai_vision.models.OntologyClass]
        """
        self._ontology_classes = ontology_classes

    @property
    def label_detection_model_version(self):
        """
        Gets the label_detection_model_version of this AnalyzeVideoResult.
        Label Detection model version.


        :return: The label_detection_model_version of this AnalyzeVideoResult.
        :rtype: str
        """
        return self._label_detection_model_version

    @label_detection_model_version.setter
    def label_detection_model_version(self, label_detection_model_version):
        """
        Sets the label_detection_model_version of this AnalyzeVideoResult.
        Label Detection model version.


        :param label_detection_model_version: The label_detection_model_version of this AnalyzeVideoResult.
        :type: str
        """
        self._label_detection_model_version = label_detection_model_version

    @property
    def object_detection_model_version(self):
        """
        Gets the object_detection_model_version of this AnalyzeVideoResult.
        Object Detection model version.


        :return: The object_detection_model_version of this AnalyzeVideoResult.
        :rtype: str
        """
        return self._object_detection_model_version

    @object_detection_model_version.setter
    def object_detection_model_version(self, object_detection_model_version):
        """
        Sets the object_detection_model_version of this AnalyzeVideoResult.
        Object Detection model version.


        :param object_detection_model_version: The object_detection_model_version of this AnalyzeVideoResult.
        :type: str
        """
        self._object_detection_model_version = object_detection_model_version

    @property
    def object_tracking_model_version(self):
        """
        Gets the object_tracking_model_version of this AnalyzeVideoResult.
        Object Tracking model version.


        :return: The object_tracking_model_version of this AnalyzeVideoResult.
        :rtype: str
        """
        return self._object_tracking_model_version

    @object_tracking_model_version.setter
    def object_tracking_model_version(self, object_tracking_model_version):
        """
        Sets the object_tracking_model_version of this AnalyzeVideoResult.
        Object Tracking model version.


        :param object_tracking_model_version: The object_tracking_model_version of this AnalyzeVideoResult.
        :type: str
        """
        self._object_tracking_model_version = object_tracking_model_version

    @property
    def text_detection_model_version(self):
        """
        Gets the text_detection_model_version of this AnalyzeVideoResult.
        Text Detection model version.


        :return: The text_detection_model_version of this AnalyzeVideoResult.
        :rtype: str
        """
        return self._text_detection_model_version

    @text_detection_model_version.setter
    def text_detection_model_version(self, text_detection_model_version):
        """
        Sets the text_detection_model_version of this AnalyzeVideoResult.
        Text Detection model version.


        :param text_detection_model_version: The text_detection_model_version of this AnalyzeVideoResult.
        :type: str
        """
        self._text_detection_model_version = text_detection_model_version

    @property
    def face_detection_model_version(self):
        """
        Gets the face_detection_model_version of this AnalyzeVideoResult.
        Face Detection model version.


        :return: The face_detection_model_version of this AnalyzeVideoResult.
        :rtype: str
        """
        return self._face_detection_model_version

    @face_detection_model_version.setter
    def face_detection_model_version(self, face_detection_model_version):
        """
        Sets the face_detection_model_version of this AnalyzeVideoResult.
        Face Detection model version.


        :param face_detection_model_version: The face_detection_model_version of this AnalyzeVideoResult.
        :type: str
        """
        self._face_detection_model_version = face_detection_model_version

    @property
    def errors(self):
        """
        Gets the errors of this AnalyzeVideoResult.
        Array of possible errors.


        :return: The errors of this AnalyzeVideoResult.
        :rtype: list[oci.ai_vision.models.ProcessingError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this AnalyzeVideoResult.
        Array of possible errors.


        :param errors: The errors of this AnalyzeVideoResult.
        :type: list[oci.ai_vision.models.ProcessingError]
        """
        self._errors = errors

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
