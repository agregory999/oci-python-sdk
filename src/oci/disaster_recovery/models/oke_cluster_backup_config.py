# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OkeClusterBackupConfig(object):
    """
    The details of backup performed on OKE Cluster.
    """

    #: A constant which can be used with the replicate_images property of a OkeClusterBackupConfig.
    #: This constant has a value of "ENABLE"
    REPLICATE_IMAGES_ENABLE = "ENABLE"

    #: A constant which can be used with the replicate_images property of a OkeClusterBackupConfig.
    #: This constant has a value of "DISABLE"
    REPLICATE_IMAGES_DISABLE = "DISABLE"

    def __init__(self, **kwargs):
        """
        Initializes a new OkeClusterBackupConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param namespaces:
            The value to assign to the namespaces property of this OkeClusterBackupConfig.
        :type namespaces: list[str]

        :param backup_schedule:
            The value to assign to the backup_schedule property of this OkeClusterBackupConfig.
        :type backup_schedule: str

        :param replicate_images:
            The value to assign to the replicate_images property of this OkeClusterBackupConfig.
            Allowed values for this property are: "ENABLE", "DISABLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type replicate_images: str

        :param max_number_of_backups_retained:
            The value to assign to the max_number_of_backups_retained property of this OkeClusterBackupConfig.
        :type max_number_of_backups_retained: int

        :param image_replication_vault_secret_id:
            The value to assign to the image_replication_vault_secret_id property of this OkeClusterBackupConfig.
        :type image_replication_vault_secret_id: str

        """
        self.swagger_types = {
            'namespaces': 'list[str]',
            'backup_schedule': 'str',
            'replicate_images': 'str',
            'max_number_of_backups_retained': 'int',
            'image_replication_vault_secret_id': 'str'
        }
        self.attribute_map = {
            'namespaces': 'namespaces',
            'backup_schedule': 'backupSchedule',
            'replicate_images': 'replicateImages',
            'max_number_of_backups_retained': 'maxNumberOfBackupsRetained',
            'image_replication_vault_secret_id': 'imageReplicationVaultSecretId'
        }
        self._namespaces = None
        self._backup_schedule = None
        self._replicate_images = None
        self._max_number_of_backups_retained = None
        self._image_replication_vault_secret_id = None

    @property
    def namespaces(self):
        """
        Gets the namespaces of this OkeClusterBackupConfig.
        A list of namespaces that need to be backed up.
        The default value is null. If a list of namespaces is not provided, all namespaces will be backed up.
        This property applies to the OKE cluster member in primary region.

        Example: [\"default\", \"pv-nginx\"]


        :return: The namespaces of this OkeClusterBackupConfig.
        :rtype: list[str]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """
        Sets the namespaces of this OkeClusterBackupConfig.
        A list of namespaces that need to be backed up.
        The default value is null. If a list of namespaces is not provided, all namespaces will be backed up.
        This property applies to the OKE cluster member in primary region.

        Example: [\"default\", \"pv-nginx\"]


        :param namespaces: The namespaces of this OkeClusterBackupConfig.
        :type: list[str]
        """
        self._namespaces = namespaces

    @property
    def backup_schedule(self):
        """
        Gets the backup_schedule of this OkeClusterBackupConfig.
        The schedule for backing up namespaces to the destination region. If a backup schedule is not specified, only a single backup will be created. This format of the string specifying the backup schedule must conform with RFC-5545.
        This schedule will use the UTC timezone.
        This property applies to the OKE cluster member in primary region.

        Example: FREQ=WEEKLY;BYDAY=MO,TU,WE,TH;BYHOUR=10;INTERVAL=1


        :return: The backup_schedule of this OkeClusterBackupConfig.
        :rtype: str
        """
        return self._backup_schedule

    @backup_schedule.setter
    def backup_schedule(self, backup_schedule):
        """
        Sets the backup_schedule of this OkeClusterBackupConfig.
        The schedule for backing up namespaces to the destination region. If a backup schedule is not specified, only a single backup will be created. This format of the string specifying the backup schedule must conform with RFC-5545.
        This schedule will use the UTC timezone.
        This property applies to the OKE cluster member in primary region.

        Example: FREQ=WEEKLY;BYDAY=MO,TU,WE,TH;BYHOUR=10;INTERVAL=1


        :param backup_schedule: The backup_schedule of this OkeClusterBackupConfig.
        :type: str
        """
        self._backup_schedule = backup_schedule

    @property
    def replicate_images(self):
        """
        Gets the replicate_images of this OkeClusterBackupConfig.
        Controls the behaviour of image replication across regions.
        This property applies to the OKE cluster member in primary region.

        Allowed values for this property are: "ENABLE", "DISABLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The replicate_images of this OkeClusterBackupConfig.
        :rtype: str
        """
        return self._replicate_images

    @replicate_images.setter
    def replicate_images(self, replicate_images):
        """
        Sets the replicate_images of this OkeClusterBackupConfig.
        Controls the behaviour of image replication across regions.
        This property applies to the OKE cluster member in primary region.


        :param replicate_images: The replicate_images of this OkeClusterBackupConfig.
        :type: str
        """
        allowed_values = ["ENABLE", "DISABLE"]
        if not value_allowed_none_or_none_sentinel(replicate_images, allowed_values):
            replicate_images = 'UNKNOWN_ENUM_VALUE'
        self._replicate_images = replicate_images

    @property
    def max_number_of_backups_retained(self):
        """
        Gets the max_number_of_backups_retained of this OkeClusterBackupConfig.
        The maximum number of backups that should be retained.
        This property applies to the OKE cluster member in primary region.


        :return: The max_number_of_backups_retained of this OkeClusterBackupConfig.
        :rtype: int
        """
        return self._max_number_of_backups_retained

    @max_number_of_backups_retained.setter
    def max_number_of_backups_retained(self, max_number_of_backups_retained):
        """
        Sets the max_number_of_backups_retained of this OkeClusterBackupConfig.
        The maximum number of backups that should be retained.
        This property applies to the OKE cluster member in primary region.


        :param max_number_of_backups_retained: The max_number_of_backups_retained of this OkeClusterBackupConfig.
        :type: int
        """
        self._max_number_of_backups_retained = max_number_of_backups_retained

    @property
    def image_replication_vault_secret_id(self):
        """
        Gets the image_replication_vault_secret_id of this OkeClusterBackupConfig.
        The OCID of the vault secret that stores the image credential.
        This property applies to the OKE cluster member in both the primary and standby region.


        :return: The image_replication_vault_secret_id of this OkeClusterBackupConfig.
        :rtype: str
        """
        return self._image_replication_vault_secret_id

    @image_replication_vault_secret_id.setter
    def image_replication_vault_secret_id(self, image_replication_vault_secret_id):
        """
        Sets the image_replication_vault_secret_id of this OkeClusterBackupConfig.
        The OCID of the vault secret that stores the image credential.
        This property applies to the OKE cluster member in both the primary and standby region.


        :param image_replication_vault_secret_id: The image_replication_vault_secret_id of this OkeClusterBackupConfig.
        :type: str
        """
        self._image_replication_vault_secret_id = image_replication_vault_secret_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
