# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MaskingPolicyHealthReportSummary(object):
    """
    Summary of a masking policy health report.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MaskingPolicyHealthReportSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MaskingPolicyHealthReportSummary.
        :type id: str

        :param masking_policy_id:
            The value to assign to the masking_policy_id property of this MaskingPolicyHealthReportSummary.
        :type masking_policy_id: str

        :param target_id:
            The value to assign to the target_id property of this MaskingPolicyHealthReportSummary.
        :type target_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MaskingPolicyHealthReportSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this MaskingPolicyHealthReportSummary.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this MaskingPolicyHealthReportSummary.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MaskingPolicyHealthReportSummary.
        :type lifecycle_state: str

        :param description:
            The value to assign to the description property of this MaskingPolicyHealthReportSummary.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MaskingPolicyHealthReportSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MaskingPolicyHealthReportSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'masking_policy_id': 'str',
            'target_id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'masking_policy_id': 'maskingPolicyId',
            'target_id': 'targetId',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._masking_policy_id = None
        self._target_id = None
        self._compartment_id = None
        self._display_name = None
        self._time_created = None
        self._lifecycle_state = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MaskingPolicyHealthReportSummary.
        The OCID of the health report.


        :return: The id of this MaskingPolicyHealthReportSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MaskingPolicyHealthReportSummary.
        The OCID of the health report.


        :param id: The id of this MaskingPolicyHealthReportSummary.
        :type: str
        """
        self._id = id

    @property
    def masking_policy_id(self):
        """
        **[Required]** Gets the masking_policy_id of this MaskingPolicyHealthReportSummary.
        The OCID of the masking policy.


        :return: The masking_policy_id of this MaskingPolicyHealthReportSummary.
        :rtype: str
        """
        return self._masking_policy_id

    @masking_policy_id.setter
    def masking_policy_id(self, masking_policy_id):
        """
        Sets the masking_policy_id of this MaskingPolicyHealthReportSummary.
        The OCID of the masking policy.


        :param masking_policy_id: The masking_policy_id of this MaskingPolicyHealthReportSummary.
        :type: str
        """
        self._masking_policy_id = masking_policy_id

    @property
    def target_id(self):
        """
        **[Required]** Gets the target_id of this MaskingPolicyHealthReportSummary.
        The OCID of the target database for which this report was created.


        :return: The target_id of this MaskingPolicyHealthReportSummary.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this MaskingPolicyHealthReportSummary.
        The OCID of the target database for which this report was created.


        :param target_id: The target_id of this MaskingPolicyHealthReportSummary.
        :type: str
        """
        self._target_id = target_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MaskingPolicyHealthReportSummary.
        The OCID of the compartment that contains the health report.


        :return: The compartment_id of this MaskingPolicyHealthReportSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MaskingPolicyHealthReportSummary.
        The OCID of the compartment that contains the health report.


        :param compartment_id: The compartment_id of this MaskingPolicyHealthReportSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this MaskingPolicyHealthReportSummary.
        The display name of the health report.


        :return: The display_name of this MaskingPolicyHealthReportSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MaskingPolicyHealthReportSummary.
        The display name of the health report.


        :param display_name: The display_name of this MaskingPolicyHealthReportSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this MaskingPolicyHealthReportSummary.
        The date and time the report was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this MaskingPolicyHealthReportSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MaskingPolicyHealthReportSummary.
        The date and time the report was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this MaskingPolicyHealthReportSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this MaskingPolicyHealthReportSummary.
        The current state of the health report.


        :return: The lifecycle_state of this MaskingPolicyHealthReportSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MaskingPolicyHealthReportSummary.
        The current state of the health report.


        :param lifecycle_state: The lifecycle_state of this MaskingPolicyHealthReportSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def description(self):
        """
        Gets the description of this MaskingPolicyHealthReportSummary.
        The description of the masking health report.


        :return: The description of this MaskingPolicyHealthReportSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this MaskingPolicyHealthReportSummary.
        The description of the masking health report.


        :param description: The description of this MaskingPolicyHealthReportSummary.
        :type: str
        """
        self._description = description

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this MaskingPolicyHealthReportSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this MaskingPolicyHealthReportSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this MaskingPolicyHealthReportSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this MaskingPolicyHealthReportSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this MaskingPolicyHealthReportSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this MaskingPolicyHealthReportSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this MaskingPolicyHealthReportSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this MaskingPolicyHealthReportSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
