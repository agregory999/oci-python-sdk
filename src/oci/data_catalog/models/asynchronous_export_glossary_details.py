# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190325


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AsynchronousExportGlossaryDetails(object):
    """
    Details needed by the glossary export request.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AsynchronousExportGlossaryDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param object_storage_target:
            The value to assign to the object_storage_target property of this AsynchronousExportGlossaryDetails.
        :type object_storage_target: oci.data_catalog.models.ObjectStorageObjectReference

        """
        self.swagger_types = {
            'object_storage_target': 'ObjectStorageObjectReference'
        }
        self.attribute_map = {
            'object_storage_target': 'objectStorageTarget'
        }
        self._object_storage_target = None

    @property
    def object_storage_target(self):
        """
        Gets the object_storage_target of this AsynchronousExportGlossaryDetails.

        :return: The object_storage_target of this AsynchronousExportGlossaryDetails.
        :rtype: oci.data_catalog.models.ObjectStorageObjectReference
        """
        return self._object_storage_target

    @object_storage_target.setter
    def object_storage_target(self, object_storage_target):
        """
        Sets the object_storage_target of this AsynchronousExportGlossaryDetails.

        :param object_storage_target: The object_storage_target of this AsynchronousExportGlossaryDetails.
        :type: oci.data_catalog.models.ObjectStorageObjectReference
        """
        self._object_storage_target = object_storage_target

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
