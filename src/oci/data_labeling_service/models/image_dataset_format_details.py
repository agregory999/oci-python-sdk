# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20211001

from .dataset_format_details import DatasetFormatDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImageDatasetFormatDetails(DatasetFormatDetails):
    """
    It indicates the dataset is comprised of images.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImageDatasetFormatDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_labeling_service.models.ImageDatasetFormatDetails.format_type` attribute
        of this class is ``IMAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param format_type:
            The value to assign to the format_type property of this ImageDatasetFormatDetails.
            Allowed values for this property are: "DOCUMENT", "IMAGE", "TEXT"
        :type format_type: str

        """
        self.swagger_types = {
            'format_type': 'str'
        }

        self.attribute_map = {
            'format_type': 'formatType'
        }

        self._format_type = None
        self._format_type = 'IMAGE'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
