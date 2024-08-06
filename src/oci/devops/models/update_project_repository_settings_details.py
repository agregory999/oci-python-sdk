# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateProjectRepositorySettingsDetails(object):
    """
    Information to update custom project repository settings.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateProjectRepositorySettingsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param merge_settings:
            The value to assign to the merge_settings property of this UpdateProjectRepositorySettingsDetails.
        :type merge_settings: oci.devops.models.MergeSettings

        :param approval_rules:
            The value to assign to the approval_rules property of this UpdateProjectRepositorySettingsDetails.
        :type approval_rules: oci.devops.models.UpdateApprovalRuleDetailsCollection

        """
        self.swagger_types = {
            'merge_settings': 'MergeSettings',
            'approval_rules': 'UpdateApprovalRuleDetailsCollection'
        }

        self.attribute_map = {
            'merge_settings': 'mergeSettings',
            'approval_rules': 'approvalRules'
        }

        self._merge_settings = None
        self._approval_rules = None

    @property
    def merge_settings(self):
        """
        Gets the merge_settings of this UpdateProjectRepositorySettingsDetails.

        :return: The merge_settings of this UpdateProjectRepositorySettingsDetails.
        :rtype: oci.devops.models.MergeSettings
        """
        return self._merge_settings

    @merge_settings.setter
    def merge_settings(self, merge_settings):
        """
        Sets the merge_settings of this UpdateProjectRepositorySettingsDetails.

        :param merge_settings: The merge_settings of this UpdateProjectRepositorySettingsDetails.
        :type: oci.devops.models.MergeSettings
        """
        self._merge_settings = merge_settings

    @property
    def approval_rules(self):
        """
        Gets the approval_rules of this UpdateProjectRepositorySettingsDetails.

        :return: The approval_rules of this UpdateProjectRepositorySettingsDetails.
        :rtype: oci.devops.models.UpdateApprovalRuleDetailsCollection
        """
        return self._approval_rules

    @approval_rules.setter
    def approval_rules(self, approval_rules):
        """
        Sets the approval_rules of this UpdateProjectRepositorySettingsDetails.

        :param approval_rules: The approval_rules of this UpdateProjectRepositorySettingsDetails.
        :type: oci.devops.models.UpdateApprovalRuleDetailsCollection
        """
        self._approval_rules = approval_rules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
