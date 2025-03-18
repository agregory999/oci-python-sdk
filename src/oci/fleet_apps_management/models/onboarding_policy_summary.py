# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OnboardingPolicySummary(object):
    """
    Summary of the Fleet Application Management Onboard Policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OnboardingPolicySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OnboardingPolicySummary.
        :type id: str

        :param time_created:
            The value to assign to the time_created property of this OnboardingPolicySummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OnboardingPolicySummary.
        :type time_updated: datetime

        :param statements:
            The value to assign to the statements property of this OnboardingPolicySummary.
        :type statements: list[str]

        :param system_tags:
            The value to assign to the system_tags property of this OnboardingPolicySummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'statements': 'list[str]',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'statements': 'statements',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._time_created = None
        self._time_updated = None
        self._statements = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OnboardingPolicySummary.
        The unique id of the resource.


        :return: The id of this OnboardingPolicySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OnboardingPolicySummary.
        The unique id of the resource.


        :param id: The id of this OnboardingPolicySummary.
        :type: str
        """
        self._id = id

    @property
    def time_created(self):
        """
        Gets the time_created of this OnboardingPolicySummary.
        The time this resource was created. An RFC3339 formatted datetime string.


        :return: The time_created of this OnboardingPolicySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OnboardingPolicySummary.
        The time this resource was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this OnboardingPolicySummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this OnboardingPolicySummary.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this OnboardingPolicySummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this OnboardingPolicySummary.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this OnboardingPolicySummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def statements(self):
        """
        Gets the statements of this OnboardingPolicySummary.
        Policy statements.


        :return: The statements of this OnboardingPolicySummary.
        :rtype: list[str]
        """
        return self._statements

    @statements.setter
    def statements(self, statements):
        """
        Sets the statements of this OnboardingPolicySummary.
        Policy statements.


        :param statements: The statements of this OnboardingPolicySummary.
        :type: list[str]
        """
        self._statements = statements

    @property
    def system_tags(self):
        """
        Gets the system_tags of this OnboardingPolicySummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this OnboardingPolicySummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this OnboardingPolicySummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this OnboardingPolicySummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
