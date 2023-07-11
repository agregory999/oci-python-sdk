# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlTuningAdvisorTaskSummaryReportIndexFindingSummary(object):
    """
    A summary for all the index findings in a SQL Tuning Advisor task. Includes the index's hash value, table name, schema, index name, reference count and index columns
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlTuningAdvisorTaskSummaryReportIndexFindingSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param index_hash_value:
            The value to assign to the index_hash_value property of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        :type index_hash_value: int

        :param index_name:
            The value to assign to the index_name property of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        :type index_name: str

        :param table_name:
            The value to assign to the table_name property of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        :type table_name: str

        :param schema:
            The value to assign to the schema property of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        :type schema: str

        :param reference_count:
            The value to assign to the reference_count property of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        :type reference_count: int

        :param index_columns:
            The value to assign to the index_columns property of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        :type index_columns: list[str]

        """
        self.swagger_types = {
            'index_hash_value': 'int',
            'index_name': 'str',
            'table_name': 'str',
            'schema': 'str',
            'reference_count': 'int',
            'index_columns': 'list[str]'
        }

        self.attribute_map = {
            'index_hash_value': 'indexHashValue',
            'index_name': 'indexName',
            'table_name': 'tableName',
            'schema': 'schema',
            'reference_count': 'referenceCount',
            'index_columns': 'indexColumns'
        }

        self._index_hash_value = None
        self._index_name = None
        self._table_name = None
        self._schema = None
        self._reference_count = None
        self._index_columns = None

    @property
    def index_hash_value(self):
        """
        **[Required]** Gets the index_hash_value of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        Numerical representation of the index.


        :return: The index_hash_value of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        :rtype: int
        """
        return self._index_hash_value

    @index_hash_value.setter
    def index_hash_value(self, index_hash_value):
        """
        Sets the index_hash_value of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        Numerical representation of the index.


        :param index_hash_value: The index_hash_value of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        :type: int
        """
        self._index_hash_value = index_hash_value

    @property
    def index_name(self):
        """
        **[Required]** Gets the index_name of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        Name of the index.


        :return: The index_name of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        :rtype: str
        """
        return self._index_name

    @index_name.setter
    def index_name(self, index_name):
        """
        Sets the index_name of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        Name of the index.


        :param index_name: The index_name of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        :type: str
        """
        self._index_name = index_name

    @property
    def table_name(self):
        """
        **[Required]** Gets the table_name of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        Table's name related to the index.


        :return: The table_name of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """
        Sets the table_name of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        Table's name related to the index.


        :param table_name: The table_name of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        :type: str
        """
        self._table_name = table_name

    @property
    def schema(self):
        """
        **[Required]** Gets the schema of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        Schema related to the index.


        :return: The schema of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """
        Sets the schema of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        Schema related to the index.


        :param schema: The schema of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        :type: str
        """
        self._schema = schema

    @property
    def reference_count(self):
        """
        **[Required]** Gets the reference_count of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        The number of times the index is referenced within the SQL Tuning advisor task findings.


        :return: The reference_count of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        :rtype: int
        """
        return self._reference_count

    @reference_count.setter
    def reference_count(self, reference_count):
        """
        Sets the reference_count of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        The number of times the index is referenced within the SQL Tuning advisor task findings.


        :param reference_count: The reference_count of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        :type: int
        """
        self._reference_count = reference_count

    @property
    def index_columns(self):
        """
        **[Required]** Gets the index_columns of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        Columns of the index.


        :return: The index_columns of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        :rtype: list[str]
        """
        return self._index_columns

    @index_columns.setter
    def index_columns(self, index_columns):
        """
        Sets the index_columns of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        Columns of the index.


        :param index_columns: The index_columns of this SqlTuningAdvisorTaskSummaryReportIndexFindingSummary.
        :type: list[str]
        """
        self._index_columns = index_columns

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
