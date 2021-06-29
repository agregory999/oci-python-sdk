# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataAssetExportScope(object):
    """
    Scope of asset export, which consists of a container object (bucket, folder, schema, etc) within the asset,
    and types of child objects contained by that object to be included.
    objectKey - Key of the container object to be exported. For example, key of schema_1.
    exportTypeIds - Type key(s) of objects within the container object to be exported. For example, type key of table or view.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataAssetExportScope object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param object_key:
            The value to assign to the object_key property of this DataAssetExportScope.
        :type object_key: str

        :param export_type_ids:
            The value to assign to the export_type_ids property of this DataAssetExportScope.
        :type export_type_ids: list[str]

        """
        self.swagger_types = {
            'object_key': 'str',
            'export_type_ids': 'list[str]'
        }

        self.attribute_map = {
            'object_key': 'objectKey',
            'export_type_ids': 'exportTypeIds'
        }

        self._object_key = None
        self._export_type_ids = None

    @property
    def object_key(self):
        """
        Gets the object_key of this DataAssetExportScope.
        Unique key of the object selected for export.


        :return: The object_key of this DataAssetExportScope.
        :rtype: str
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key):
        """
        Sets the object_key of this DataAssetExportScope.
        Unique key of the object selected for export.


        :param object_key: The object_key of this DataAssetExportScope.
        :type: str
        """
        self._object_key = object_key

    @property
    def export_type_ids(self):
        """
        Gets the export_type_ids of this DataAssetExportScope.
        Array of type keys selected for export.


        :return: The export_type_ids of this DataAssetExportScope.
        :rtype: list[str]
        """
        return self._export_type_ids

    @export_type_ids.setter
    def export_type_ids(self, export_type_ids):
        """
        Sets the export_type_ids of this DataAssetExportScope.
        Array of type keys selected for export.


        :param export_type_ids: The export_type_ids of this DataAssetExportScope.
        :type: list[str]
        """
        self._export_type_ids = export_type_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
