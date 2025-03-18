# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlCollectionAggregation(object):
    """
    The details of SQL collections.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlCollectionAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param dimensions:
            The value to assign to the dimensions property of this SqlCollectionAggregation.
        :type dimensions: oci.data_safe.models.SqlCollectionDimensions

        :param count:
            The value to assign to the count property of this SqlCollectionAggregation.
        :type count: int

        """
        self.swagger_types = {
            'dimensions': 'SqlCollectionDimensions',
            'count': 'int'
        }
        self.attribute_map = {
            'dimensions': 'dimensions',
            'count': 'count'
        }
        self._dimensions = None
        self._count = None

    @property
    def dimensions(self):
        """
        **[Required]** Gets the dimensions of this SqlCollectionAggregation.

        :return: The dimensions of this SqlCollectionAggregation.
        :rtype: oci.data_safe.models.SqlCollectionDimensions
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this SqlCollectionAggregation.

        :param dimensions: The dimensions of this SqlCollectionAggregation.
        :type: oci.data_safe.models.SqlCollectionDimensions
        """
        self._dimensions = dimensions

    @property
    def count(self):
        """
        **[Required]** Gets the count of this SqlCollectionAggregation.
        The total count of the aggregated metric.


        :return: The count of this SqlCollectionAggregation.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this SqlCollectionAggregation.
        The total count of the aggregated metric.


        :param count: The count of this SqlCollectionAggregation.
        :type: int
        """
        self._count = count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
