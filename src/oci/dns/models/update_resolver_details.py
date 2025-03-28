# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180115


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateResolverDetails(object):
    """
    The body for updating an existing resolver.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateResolverDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateResolverDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateResolverDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateResolverDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param attached_views:
            The value to assign to the attached_views property of this UpdateResolverDetails.
        :type attached_views: list[oci.dns.models.AttachedViewDetails]

        :param rules:
            The value to assign to the rules property of this UpdateResolverDetails.
        :type rules: list[oci.dns.models.ResolverRuleDetails]

        """
        self.swagger_types = {
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'attached_views': 'list[AttachedViewDetails]',
            'rules': 'list[ResolverRuleDetails]'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'attached_views': 'attachedViews',
            'rules': 'rules'
        }
        self._display_name = None
        self._freeform_tags = None
        self._defined_tags = None
        self._attached_views = None
        self._rules = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateResolverDetails.
        The display name of the resolver.


        :return: The display_name of this UpdateResolverDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateResolverDetails.
        The display name of the resolver.


        :param display_name: The display_name of this UpdateResolverDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateResolverDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateResolverDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateResolverDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateResolverDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateResolverDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateResolverDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateResolverDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateResolverDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def attached_views(self):
        """
        Gets the attached_views of this UpdateResolverDetails.
        The attached views. Views are evaluated in order.


        :return: The attached_views of this UpdateResolverDetails.
        :rtype: list[oci.dns.models.AttachedViewDetails]
        """
        return self._attached_views

    @attached_views.setter
    def attached_views(self, attached_views):
        """
        Sets the attached_views of this UpdateResolverDetails.
        The attached views. Views are evaluated in order.


        :param attached_views: The attached_views of this UpdateResolverDetails.
        :type: list[oci.dns.models.AttachedViewDetails]
        """
        self._attached_views = attached_views

    @property
    def rules(self):
        """
        Gets the rules of this UpdateResolverDetails.
        Rules for the resolver. Rules are evaluated in order.


        :return: The rules of this UpdateResolverDetails.
        :rtype: list[oci.dns.models.ResolverRuleDetails]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this UpdateResolverDetails.
        Rules for the resolver. Rules are evaluated in order.


        :param rules: The rules of this UpdateResolverDetails.
        :type: list[oci.dns.models.ResolverRuleDetails]
        """
        self._rules = rules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
