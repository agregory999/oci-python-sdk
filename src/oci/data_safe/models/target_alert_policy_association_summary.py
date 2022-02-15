# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TargetAlertPolicyAssociationSummary(object):
    """
    A summary of target to alert policy association.
    """

    #: A constant which can be used with the lifecycle_state property of a TargetAlertPolicyAssociationSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a TargetAlertPolicyAssociationSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a TargetAlertPolicyAssociationSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a TargetAlertPolicyAssociationSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a TargetAlertPolicyAssociationSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a TargetAlertPolicyAssociationSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new TargetAlertPolicyAssociationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this TargetAlertPolicyAssociationSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this TargetAlertPolicyAssociationSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this TargetAlertPolicyAssociationSummary.
        :type description: str

        :param policy_id:
            The value to assign to the policy_id property of this TargetAlertPolicyAssociationSummary.
        :type policy_id: str

        :param target_id:
            The value to assign to the target_id property of this TargetAlertPolicyAssociationSummary.
        :type target_id: str

        :param is_enabled:
            The value to assign to the is_enabled property of this TargetAlertPolicyAssociationSummary.
        :type is_enabled: bool

        :param compartment_id:
            The value to assign to the compartment_id property of this TargetAlertPolicyAssociationSummary.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this TargetAlertPolicyAssociationSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this TargetAlertPolicyAssociationSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TargetAlertPolicyAssociationSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this TargetAlertPolicyAssociationSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this TargetAlertPolicyAssociationSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'policy_id': 'str',
            'target_id': 'str',
            'is_enabled': 'bool',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'policy_id': 'policyId',
            'target_id': 'targetId',
            'is_enabled': 'isEnabled',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._policy_id = None
        self._target_id = None
        self._is_enabled = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this TargetAlertPolicyAssociationSummary.
        The OCID of the target-alert policy association.


        :return: The id of this TargetAlertPolicyAssociationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TargetAlertPolicyAssociationSummary.
        The OCID of the target-alert policy association.


        :param id: The id of this TargetAlertPolicyAssociationSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this TargetAlertPolicyAssociationSummary.
        The display name of the target-alert policy association.


        :return: The display_name of this TargetAlertPolicyAssociationSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this TargetAlertPolicyAssociationSummary.
        The display name of the target-alert policy association.


        :param display_name: The display_name of this TargetAlertPolicyAssociationSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this TargetAlertPolicyAssociationSummary.
        Describes the target-alert policy association.


        :return: The description of this TargetAlertPolicyAssociationSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TargetAlertPolicyAssociationSummary.
        Describes the target-alert policy association.


        :param description: The description of this TargetAlertPolicyAssociationSummary.
        :type: str
        """
        self._description = description

    @property
    def policy_id(self):
        """
        Gets the policy_id of this TargetAlertPolicyAssociationSummary.
        The OCID of the alert policy.


        :return: The policy_id of this TargetAlertPolicyAssociationSummary.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """
        Sets the policy_id of this TargetAlertPolicyAssociationSummary.
        The OCID of the alert policy.


        :param policy_id: The policy_id of this TargetAlertPolicyAssociationSummary.
        :type: str
        """
        self._policy_id = policy_id

    @property
    def target_id(self):
        """
        Gets the target_id of this TargetAlertPolicyAssociationSummary.
        The OCID of the target on which alert policy is to be applied.


        :return: The target_id of this TargetAlertPolicyAssociationSummary.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this TargetAlertPolicyAssociationSummary.
        The OCID of the target on which alert policy is to be applied.


        :param target_id: The target_id of this TargetAlertPolicyAssociationSummary.
        :type: str
        """
        self._target_id = target_id

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this TargetAlertPolicyAssociationSummary.
        Indicates if the target-alert policy association is enabled or disabled.


        :return: The is_enabled of this TargetAlertPolicyAssociationSummary.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this TargetAlertPolicyAssociationSummary.
        Indicates if the target-alert policy association is enabled or disabled.


        :param is_enabled: The is_enabled of this TargetAlertPolicyAssociationSummary.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this TargetAlertPolicyAssociationSummary.
        The OCID of the compartment that contains the target-alert policy association.


        :return: The compartment_id of this TargetAlertPolicyAssociationSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this TargetAlertPolicyAssociationSummary.
        The OCID of the compartment that contains the target-alert policy association.


        :param compartment_id: The compartment_id of this TargetAlertPolicyAssociationSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this TargetAlertPolicyAssociationSummary.
        Creation date and time of the target-alert policy association, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this TargetAlertPolicyAssociationSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TargetAlertPolicyAssociationSummary.
        Creation date and time of the target-alert policy association, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this TargetAlertPolicyAssociationSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this TargetAlertPolicyAssociationSummary.
        Last date and time the target-alert policy association was updated, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this TargetAlertPolicyAssociationSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this TargetAlertPolicyAssociationSummary.
        Last date and time the target-alert policy association was updated, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this TargetAlertPolicyAssociationSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this TargetAlertPolicyAssociationSummary.
        The current state of the target-alert policy association.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this TargetAlertPolicyAssociationSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TargetAlertPolicyAssociationSummary.
        The current state of the target-alert policy association.


        :param lifecycle_state: The lifecycle_state of this TargetAlertPolicyAssociationSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this TargetAlertPolicyAssociationSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this TargetAlertPolicyAssociationSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this TargetAlertPolicyAssociationSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this TargetAlertPolicyAssociationSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this TargetAlertPolicyAssociationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this TargetAlertPolicyAssociationSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this TargetAlertPolicyAssociationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this TargetAlertPolicyAssociationSummary.
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
