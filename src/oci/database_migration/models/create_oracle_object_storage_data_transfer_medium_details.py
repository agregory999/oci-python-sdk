# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230518

from .create_oracle_data_transfer_medium_details import CreateOracleDataTransferMediumDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOracleObjectStorageDataTransferMediumDetails(CreateOracleDataTransferMediumDetails):
    """
    OCI Object Storage bucket will be used to store Data Pump dump files for the migration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOracleObjectStorageDataTransferMediumDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_migration.models.CreateOracleObjectStorageDataTransferMediumDetails.type` attribute
        of this class is ``OBJECT_STORAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this CreateOracleObjectStorageDataTransferMediumDetails.
            Allowed values for this property are: "DBLINK", "OBJECT_STORAGE", "AWS_S3", "NFS"
        :type type: str

        :param object_storage_bucket:
            The value to assign to the object_storage_bucket property of this CreateOracleObjectStorageDataTransferMediumDetails.
        :type object_storage_bucket: oci.database_migration.models.CreateObjectStoreBucket

        :param source:
            The value to assign to the source property of this CreateOracleObjectStorageDataTransferMediumDetails.
        :type source: oci.database_migration.models.HostDumpTransferDetails

        :param target:
            The value to assign to the target property of this CreateOracleObjectStorageDataTransferMediumDetails.
        :type target: oci.database_migration.models.HostDumpTransferDetails

        """
        self.swagger_types = {
            'type': 'str',
            'object_storage_bucket': 'CreateObjectStoreBucket',
            'source': 'HostDumpTransferDetails',
            'target': 'HostDumpTransferDetails'
        }
        self.attribute_map = {
            'type': 'type',
            'object_storage_bucket': 'objectStorageBucket',
            'source': 'source',
            'target': 'target'
        }
        self._type = None
        self._object_storage_bucket = None
        self._source = None
        self._target = None
        self._type = 'OBJECT_STORAGE'

    @property
    def object_storage_bucket(self):
        """
        Gets the object_storage_bucket of this CreateOracleObjectStorageDataTransferMediumDetails.

        :return: The object_storage_bucket of this CreateOracleObjectStorageDataTransferMediumDetails.
        :rtype: oci.database_migration.models.CreateObjectStoreBucket
        """
        return self._object_storage_bucket

    @object_storage_bucket.setter
    def object_storage_bucket(self, object_storage_bucket):
        """
        Sets the object_storage_bucket of this CreateOracleObjectStorageDataTransferMediumDetails.

        :param object_storage_bucket: The object_storage_bucket of this CreateOracleObjectStorageDataTransferMediumDetails.
        :type: oci.database_migration.models.CreateObjectStoreBucket
        """
        self._object_storage_bucket = object_storage_bucket

    @property
    def source(self):
        """
        Gets the source of this CreateOracleObjectStorageDataTransferMediumDetails.

        :return: The source of this CreateOracleObjectStorageDataTransferMediumDetails.
        :rtype: oci.database_migration.models.HostDumpTransferDetails
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this CreateOracleObjectStorageDataTransferMediumDetails.

        :param source: The source of this CreateOracleObjectStorageDataTransferMediumDetails.
        :type: oci.database_migration.models.HostDumpTransferDetails
        """
        self._source = source

    @property
    def target(self):
        """
        Gets the target of this CreateOracleObjectStorageDataTransferMediumDetails.

        :return: The target of this CreateOracleObjectStorageDataTransferMediumDetails.
        :rtype: oci.database_migration.models.HostDumpTransferDetails
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this CreateOracleObjectStorageDataTransferMediumDetails.

        :param target: The target of this CreateOracleObjectStorageDataTransferMediumDetails.
        :type: oci.database_migration.models.HostDumpTransferDetails
        """
        self._target = target

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
