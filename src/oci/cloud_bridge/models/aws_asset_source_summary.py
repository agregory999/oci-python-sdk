# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220509

from .asset_source_summary import AssetSourceSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AwsAssetSourceSummary(AssetSourceSummary):
    """
    Summary of an AWS asset source provided in the list.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AwsAssetSourceSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_bridge.models.AwsAssetSourceSummary.type` attribute
        of this class is ``AWS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this AwsAssetSourceSummary.
            Allowed values for this property are: "VMWARE", "AWS"
        :type type: str

        :param id:
            The value to assign to the id property of this AwsAssetSourceSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AwsAssetSourceSummary.
        :type compartment_id: str

        :param environment_id:
            The value to assign to the environment_id property of this AwsAssetSourceSummary.
        :type environment_id: str

        :param display_name:
            The value to assign to the display_name property of this AwsAssetSourceSummary.
        :type display_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AwsAssetSourceSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING", "NEEDS_ATTENTION"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AwsAssetSourceSummary.
        :type lifecycle_details: str

        :param inventory_id:
            The value to assign to the inventory_id property of this AwsAssetSourceSummary.
        :type inventory_id: str

        :param assets_compartment_id:
            The value to assign to the assets_compartment_id property of this AwsAssetSourceSummary.
        :type assets_compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this AwsAssetSourceSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AwsAssetSourceSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AwsAssetSourceSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AwsAssetSourceSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this AwsAssetSourceSummary.
        :type system_tags: dict(str, dict(str, object))

        :param aws_region:
            The value to assign to the aws_region property of this AwsAssetSourceSummary.
        :type aws_region: str

        :param aws_account_key:
            The value to assign to the aws_account_key property of this AwsAssetSourceSummary.
        :type aws_account_key: str

        """
        self.swagger_types = {
            'type': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'environment_id': 'str',
            'display_name': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'inventory_id': 'str',
            'assets_compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'aws_region': 'str',
            'aws_account_key': 'str'
        }
        self.attribute_map = {
            'type': 'type',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'environment_id': 'environmentId',
            'display_name': 'displayName',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'inventory_id': 'inventoryId',
            'assets_compartment_id': 'assetsCompartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'aws_region': 'awsRegion',
            'aws_account_key': 'awsAccountKey'
        }
        self._type = None
        self._id = None
        self._compartment_id = None
        self._environment_id = None
        self._display_name = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._inventory_id = None
        self._assets_compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._aws_region = None
        self._aws_account_key = None
        self._type = 'AWS'

    @property
    def aws_region(self):
        """
        **[Required]** Gets the aws_region of this AwsAssetSourceSummary.
        AWS region information, from where the resources are discovered.


        :return: The aws_region of this AwsAssetSourceSummary.
        :rtype: str
        """
        return self._aws_region

    @aws_region.setter
    def aws_region(self, aws_region):
        """
        Sets the aws_region of this AwsAssetSourceSummary.
        AWS region information, from where the resources are discovered.


        :param aws_region: The aws_region of this AwsAssetSourceSummary.
        :type: str
        """
        self._aws_region = aws_region

    @property
    def aws_account_key(self):
        """
        **[Required]** Gets the aws_account_key of this AwsAssetSourceSummary.
        The key of customer's aws account to be discovered/migrated.


        :return: The aws_account_key of this AwsAssetSourceSummary.
        :rtype: str
        """
        return self._aws_account_key

    @aws_account_key.setter
    def aws_account_key(self, aws_account_key):
        """
        Sets the aws_account_key of this AwsAssetSourceSummary.
        The key of customer's aws account to be discovered/migrated.


        :param aws_account_key: The aws_account_key of this AwsAssetSourceSummary.
        :type: str
        """
        self._aws_account_key = aws_account_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
