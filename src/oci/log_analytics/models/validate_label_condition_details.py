# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200601


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ValidateLabelConditionDetails(object):
    """
    Required information needed to evaluate a source label condition.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ValidateLabelConditionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param condition_string:
            The value to assign to the condition_string property of this ValidateLabelConditionDetails.
        :type condition_string: str

        :param condition_block:
            The value to assign to the condition_block property of this ValidateLabelConditionDetails.
        :type condition_block: oci.log_analytics.models.ConditionBlock

        :param field_values:
            The value to assign to the field_values property of this ValidateLabelConditionDetails.
        :type field_values: list[oci.log_analytics.models.LogAnalyticsProperty]

        """
        self.swagger_types = {
            'condition_string': 'str',
            'condition_block': 'ConditionBlock',
            'field_values': 'list[LogAnalyticsProperty]'
        }
        self.attribute_map = {
            'condition_string': 'conditionString',
            'condition_block': 'conditionBlock',
            'field_values': 'fieldValues'
        }
        self._condition_string = None
        self._condition_block = None
        self._field_values = None

    @property
    def condition_string(self):
        """
        Gets the condition_string of this ValidateLabelConditionDetails.
        String representation of the label condition to validate.


        :return: The condition_string of this ValidateLabelConditionDetails.
        :rtype: str
        """
        return self._condition_string

    @condition_string.setter
    def condition_string(self, condition_string):
        """
        Sets the condition_string of this ValidateLabelConditionDetails.
        String representation of the label condition to validate.


        :param condition_string: The condition_string of this ValidateLabelConditionDetails.
        :type: str
        """
        self._condition_string = condition_string

    @property
    def condition_block(self):
        """
        Gets the condition_block of this ValidateLabelConditionDetails.

        :return: The condition_block of this ValidateLabelConditionDetails.
        :rtype: oci.log_analytics.models.ConditionBlock
        """
        return self._condition_block

    @condition_block.setter
    def condition_block(self, condition_block):
        """
        Sets the condition_block of this ValidateLabelConditionDetails.

        :param condition_block: The condition_block of this ValidateLabelConditionDetails.
        :type: oci.log_analytics.models.ConditionBlock
        """
        self._condition_block = condition_block

    @property
    def field_values(self):
        """
        Gets the field_values of this ValidateLabelConditionDetails.
        An array of field name-value pairs to evaluate the label condition.


        :return: The field_values of this ValidateLabelConditionDetails.
        :rtype: list[oci.log_analytics.models.LogAnalyticsProperty]
        """
        return self._field_values

    @field_values.setter
    def field_values(self, field_values):
        """
        Sets the field_values of this ValidateLabelConditionDetails.
        An array of field name-value pairs to evaluate the label condition.


        :param field_values: The field_values of this ValidateLabelConditionDetails.
        :type: list[oci.log_analytics.models.LogAnalyticsProperty]
        """
        self._field_values = field_values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
