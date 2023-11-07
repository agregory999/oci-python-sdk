# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230601


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenerateArtifactDownloadUrlDetails(object):
    """
    The attributes to generate a DownloadUrl for a Java runtime artifact.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GenerateArtifactDownloadUrlDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param artifact_id:
            The value to assign to the artifact_id property of this GenerateArtifactDownloadUrlDetails.
        :type artifact_id: int

        """
        self.swagger_types = {
            'artifact_id': 'int'
        }

        self.attribute_map = {
            'artifact_id': 'artifactId'
        }

        self._artifact_id = None

    @property
    def artifact_id(self):
        """
        **[Required]** Gets the artifact_id of this GenerateArtifactDownloadUrlDetails.
        Unique identifier for the Java runtime artifact.


        :return: The artifact_id of this GenerateArtifactDownloadUrlDetails.
        :rtype: int
        """
        return self._artifact_id

    @artifact_id.setter
    def artifact_id(self, artifact_id):
        """
        Sets the artifact_id of this GenerateArtifactDownloadUrlDetails.
        Unique identifier for the Java runtime artifact.


        :param artifact_id: The artifact_id of this GenerateArtifactDownloadUrlDetails.
        :type: int
        """
        self._artifact_id = artifact_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other