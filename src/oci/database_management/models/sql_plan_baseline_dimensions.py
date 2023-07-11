# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlPlanBaselineDimensions(object):
    """
    The details of the SQL plan baseline dimensions.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlPlanBaselineDimensions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param attribute_name:
            The value to assign to the attribute_name property of this SqlPlanBaselineDimensions.
        :type attribute_name: str

        :param attribute_value:
            The value to assign to the attribute_value property of this SqlPlanBaselineDimensions.
        :type attribute_value: str

        """
        self.swagger_types = {
            'attribute_name': 'str',
            'attribute_value': 'str'
        }

        self.attribute_map = {
            'attribute_name': 'attributeName',
            'attribute_value': 'attributeValue'
        }

        self._attribute_name = None
        self._attribute_value = None

    @property
    def attribute_name(self):
        """
        **[Required]** Gets the attribute_name of this SqlPlanBaselineDimensions.
        The name of the SQL plan baseline attribute.


        :return: The attribute_name of this SqlPlanBaselineDimensions.
        :rtype: str
        """
        return self._attribute_name

    @attribute_name.setter
    def attribute_name(self, attribute_name):
        """
        Sets the attribute_name of this SqlPlanBaselineDimensions.
        The name of the SQL plan baseline attribute.


        :param attribute_name: The attribute_name of this SqlPlanBaselineDimensions.
        :type: str
        """
        self._attribute_name = attribute_name

    @property
    def attribute_value(self):
        """
        **[Required]** Gets the attribute_value of this SqlPlanBaselineDimensions.
        The value of the attribute.


        :return: The attribute_value of this SqlPlanBaselineDimensions.
        :rtype: str
        """
        return self._attribute_value

    @attribute_value.setter
    def attribute_value(self, attribute_value):
        """
        Sets the attribute_value of this SqlPlanBaselineDimensions.
        The value of the attribute.


        :param attribute_value: The attribute_value of this SqlPlanBaselineDimensions.
        :type: str
        """
        self._attribute_value = attribute_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
