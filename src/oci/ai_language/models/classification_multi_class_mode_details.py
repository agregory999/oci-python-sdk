# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221001

from .classification_type import ClassificationType
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ClassificationMultiClassModeDetails(ClassificationType):
    """
    Possible text classification multi class mode details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ClassificationMultiClassModeDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_language.models.ClassificationMultiClassModeDetails.classification_mode` attribute
        of this class is ``MULTI_CLASS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param classification_mode:
            The value to assign to the classification_mode property of this ClassificationMultiClassModeDetails.
            Allowed values for this property are: "MULTI_CLASS", "MULTI_LABEL"
        :type classification_mode: str

        :param version:
            The value to assign to the version property of this ClassificationMultiClassModeDetails.
        :type version: str

        """
        self.swagger_types = {
            'classification_mode': 'str',
            'version': 'str'
        }
        self.attribute_map = {
            'classification_mode': 'classificationMode',
            'version': 'version'
        }
        self._classification_mode = None
        self._version = None
        self._classification_mode = 'MULTI_CLASS'

    @property
    def version(self):
        """
        Gets the version of this ClassificationMultiClassModeDetails.
        Optional if nothing specified latest base model will be used for training. Supported versions can be found at /modelTypes/{modelType}


        :return: The version of this ClassificationMultiClassModeDetails.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ClassificationMultiClassModeDetails.
        Optional if nothing specified latest base model will be used for training. Supported versions can be found at /modelTypes/{modelType}


        :param version: The version of this ClassificationMultiClassModeDetails.
        :type: str
        """
        self._version = version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
