# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MySqlSqlStats(object):
    """
    MySql Sql Stats type object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MySqlSqlStats object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param digest:
            The value to assign to the digest property of this MySqlSqlStats.
        :type digest: str

        :param time_collected:
            The value to assign to the time_collected property of this MySqlSqlStats.
        :type time_collected: datetime

        :param command_type:
            The value to assign to the command_type property of this MySqlSqlStats.
        :type command_type: str

        :param total_rows:
            The value to assign to the total_rows property of this MySqlSqlStats.
        :type total_rows: int

        :param perf_schema_used_percent:
            The value to assign to the perf_schema_used_percent property of this MySqlSqlStats.
        :type perf_schema_used_percent: int

        :param schema_name:
            The value to assign to the schema_name property of this MySqlSqlStats.
        :type schema_name: str

        :param exec_count:
            The value to assign to the exec_count property of this MySqlSqlStats.
        :type exec_count: int

        :param total_latency_in_ps:
            The value to assign to the total_latency_in_ps property of this MySqlSqlStats.
        :type total_latency_in_ps: int

        :param lock_latency_in_ps:
            The value to assign to the lock_latency_in_ps property of this MySqlSqlStats.
        :type lock_latency_in_ps: int

        :param err_count:
            The value to assign to the err_count property of this MySqlSqlStats.
        :type err_count: int

        :param warn_count:
            The value to assign to the warn_count property of this MySqlSqlStats.
        :type warn_count: int

        :param rows_affected:
            The value to assign to the rows_affected property of this MySqlSqlStats.
        :type rows_affected: int

        :param rows_sent:
            The value to assign to the rows_sent property of this MySqlSqlStats.
        :type rows_sent: int

        :param rows_examined:
            The value to assign to the rows_examined property of this MySqlSqlStats.
        :type rows_examined: int

        :param tmp_disk_tables:
            The value to assign to the tmp_disk_tables property of this MySqlSqlStats.
        :type tmp_disk_tables: int

        :param tmp_tables:
            The value to assign to the tmp_tables property of this MySqlSqlStats.
        :type tmp_tables: int

        :param select_full_join:
            The value to assign to the select_full_join property of this MySqlSqlStats.
        :type select_full_join: int

        :param select_full_range_join:
            The value to assign to the select_full_range_join property of this MySqlSqlStats.
        :type select_full_range_join: int

        :param select_range:
            The value to assign to the select_range property of this MySqlSqlStats.
        :type select_range: int

        :param select_range_check:
            The value to assign to the select_range_check property of this MySqlSqlStats.
        :type select_range_check: int

        :param select_scan:
            The value to assign to the select_scan property of this MySqlSqlStats.
        :type select_scan: int

        :param sort_merge_passes:
            The value to assign to the sort_merge_passes property of this MySqlSqlStats.
        :type sort_merge_passes: int

        :param sort_range:
            The value to assign to the sort_range property of this MySqlSqlStats.
        :type sort_range: int

        :param rows_sorted:
            The value to assign to the rows_sorted property of this MySqlSqlStats.
        :type rows_sorted: int

        :param sort_scan:
            The value to assign to the sort_scan property of this MySqlSqlStats.
        :type sort_scan: int

        :param no_index_used_count:
            The value to assign to the no_index_used_count property of this MySqlSqlStats.
        :type no_index_used_count: int

        :param no_good_index_used_count:
            The value to assign to the no_good_index_used_count property of this MySqlSqlStats.
        :type no_good_index_used_count: int

        :param cpu_latency_in_ps:
            The value to assign to the cpu_latency_in_ps property of this MySqlSqlStats.
        :type cpu_latency_in_ps: int

        :param max_controlled_memory_in_bytes:
            The value to assign to the max_controlled_memory_in_bytes property of this MySqlSqlStats.
        :type max_controlled_memory_in_bytes: int

        :param max_total_memory_in_bytes:
            The value to assign to the max_total_memory_in_bytes property of this MySqlSqlStats.
        :type max_total_memory_in_bytes: int

        :param exec_count_secondary:
            The value to assign to the exec_count_secondary property of this MySqlSqlStats.
        :type exec_count_secondary: int

        :param time_first_seen:
            The value to assign to the time_first_seen property of this MySqlSqlStats.
        :type time_first_seen: datetime

        :param time_last_seen:
            The value to assign to the time_last_seen property of this MySqlSqlStats.
        :type time_last_seen: datetime

        """
        self.swagger_types = {
            'digest': 'str',
            'time_collected': 'datetime',
            'command_type': 'str',
            'total_rows': 'int',
            'perf_schema_used_percent': 'int',
            'schema_name': 'str',
            'exec_count': 'int',
            'total_latency_in_ps': 'int',
            'lock_latency_in_ps': 'int',
            'err_count': 'int',
            'warn_count': 'int',
            'rows_affected': 'int',
            'rows_sent': 'int',
            'rows_examined': 'int',
            'tmp_disk_tables': 'int',
            'tmp_tables': 'int',
            'select_full_join': 'int',
            'select_full_range_join': 'int',
            'select_range': 'int',
            'select_range_check': 'int',
            'select_scan': 'int',
            'sort_merge_passes': 'int',
            'sort_range': 'int',
            'rows_sorted': 'int',
            'sort_scan': 'int',
            'no_index_used_count': 'int',
            'no_good_index_used_count': 'int',
            'cpu_latency_in_ps': 'int',
            'max_controlled_memory_in_bytes': 'int',
            'max_total_memory_in_bytes': 'int',
            'exec_count_secondary': 'int',
            'time_first_seen': 'datetime',
            'time_last_seen': 'datetime'
        }
        self.attribute_map = {
            'digest': 'digest',
            'time_collected': 'timeCollected',
            'command_type': 'commandType',
            'total_rows': 'totalRows',
            'perf_schema_used_percent': 'perfSchemaUsedPercent',
            'schema_name': 'schemaName',
            'exec_count': 'execCount',
            'total_latency_in_ps': 'totalLatencyInPs',
            'lock_latency_in_ps': 'lockLatencyInPs',
            'err_count': 'errCount',
            'warn_count': 'warnCount',
            'rows_affected': 'rowsAffected',
            'rows_sent': 'rowsSent',
            'rows_examined': 'rowsExamined',
            'tmp_disk_tables': 'tmpDiskTables',
            'tmp_tables': 'tmpTables',
            'select_full_join': 'selectFullJoin',
            'select_full_range_join': 'selectFullRangeJoin',
            'select_range': 'selectRange',
            'select_range_check': 'selectRangeCheck',
            'select_scan': 'selectScan',
            'sort_merge_passes': 'sortMergePasses',
            'sort_range': 'sortRange',
            'rows_sorted': 'rowsSorted',
            'sort_scan': 'sortScan',
            'no_index_used_count': 'noIndexUsedCount',
            'no_good_index_used_count': 'noGoodIndexUsedCount',
            'cpu_latency_in_ps': 'cpuLatencyInPs',
            'max_controlled_memory_in_bytes': 'maxControlledMemoryInBytes',
            'max_total_memory_in_bytes': 'maxTotalMemoryInBytes',
            'exec_count_secondary': 'execCountSecondary',
            'time_first_seen': 'timeFirstSeen',
            'time_last_seen': 'timeLastSeen'
        }
        self._digest = None
        self._time_collected = None
        self._command_type = None
        self._total_rows = None
        self._perf_schema_used_percent = None
        self._schema_name = None
        self._exec_count = None
        self._total_latency_in_ps = None
        self._lock_latency_in_ps = None
        self._err_count = None
        self._warn_count = None
        self._rows_affected = None
        self._rows_sent = None
        self._rows_examined = None
        self._tmp_disk_tables = None
        self._tmp_tables = None
        self._select_full_join = None
        self._select_full_range_join = None
        self._select_range = None
        self._select_range_check = None
        self._select_scan = None
        self._sort_merge_passes = None
        self._sort_range = None
        self._rows_sorted = None
        self._sort_scan = None
        self._no_index_used_count = None
        self._no_good_index_used_count = None
        self._cpu_latency_in_ps = None
        self._max_controlled_memory_in_bytes = None
        self._max_total_memory_in_bytes = None
        self._exec_count_secondary = None
        self._time_first_seen = None
        self._time_last_seen = None

    @property
    def digest(self):
        """
        **[Required]** Gets the digest of this MySqlSqlStats.
        Unique SQL ID Digest for a MySql Statement.
        Example: `\"c20fcea11911be36651b7ca7bd3712d4ed9ac1134cee9c6620039e1fb13b5eff\"`


        :return: The digest of this MySqlSqlStats.
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """
        Sets the digest of this MySqlSqlStats.
        Unique SQL ID Digest for a MySql Statement.
        Example: `\"c20fcea11911be36651b7ca7bd3712d4ed9ac1134cee9c6620039e1fb13b5eff\"`


        :param digest: The digest of this MySqlSqlStats.
        :type: str
        """
        self._digest = digest

    @property
    def time_collected(self):
        """
        **[Required]** Gets the time_collected of this MySqlSqlStats.
        Collection timestamp.
        Example: `\"2020-03-31T00:00:00.000Z\"`


        :return: The time_collected of this MySqlSqlStats.
        :rtype: datetime
        """
        return self._time_collected

    @time_collected.setter
    def time_collected(self, time_collected):
        """
        Sets the time_collected of this MySqlSqlStats.
        Collection timestamp.
        Example: `\"2020-03-31T00:00:00.000Z\"`


        :param time_collected: The time_collected of this MySqlSqlStats.
        :type: datetime
        """
        self._time_collected = time_collected

    @property
    def command_type(self):
        """
        Gets the command_type of this MySqlSqlStats.
        Type of statement such as select, update or delete.


        :return: The command_type of this MySqlSqlStats.
        :rtype: str
        """
        return self._command_type

    @command_type.setter
    def command_type(self, command_type):
        """
        Sets the command_type of this MySqlSqlStats.
        Type of statement such as select, update or delete.


        :param command_type: The command_type of this MySqlSqlStats.
        :type: str
        """
        self._command_type = command_type

    @property
    def total_rows(self):
        """
        Gets the total_rows of this MySqlSqlStats.
        Total number of SQL statements used in collection ranking calculation.


        :return: The total_rows of this MySqlSqlStats.
        :rtype: int
        """
        return self._total_rows

    @total_rows.setter
    def total_rows(self, total_rows):
        """
        Sets the total_rows of this MySqlSqlStats.
        Total number of SQL statements used in collection ranking calculation.


        :param total_rows: The total_rows of this MySqlSqlStats.
        :type: int
        """
        self._total_rows = total_rows

    @property
    def perf_schema_used_percent(self):
        """
        Gets the perf_schema_used_percent of this MySqlSqlStats.
        Percent of SQL statements in the perf schema table relative to max or overflow count set in @@GLOBAL.performance_schema_digests_size.


        :return: The perf_schema_used_percent of this MySqlSqlStats.
        :rtype: int
        """
        return self._perf_schema_used_percent

    @perf_schema_used_percent.setter
    def perf_schema_used_percent(self, perf_schema_used_percent):
        """
        Sets the perf_schema_used_percent of this MySqlSqlStats.
        Percent of SQL statements in the perf schema table relative to max or overflow count set in @@GLOBAL.performance_schema_digests_size.


        :param perf_schema_used_percent: The perf_schema_used_percent of this MySqlSqlStats.
        :type: int
        """
        self._perf_schema_used_percent = perf_schema_used_percent

    @property
    def schema_name(self):
        """
        Gets the schema_name of this MySqlSqlStats.
        Name of Database Schema.
        Example: `\"performance_schema\"`


        :return: The schema_name of this MySqlSqlStats.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """
        Sets the schema_name of this MySqlSqlStats.
        Name of Database Schema.
        Example: `\"performance_schema\"`


        :param schema_name: The schema_name of this MySqlSqlStats.
        :type: str
        """
        self._schema_name = schema_name

    @property
    def exec_count(self):
        """
        Gets the exec_count of this MySqlSqlStats.
        The total number of times the statement has executed.


        :return: The exec_count of this MySqlSqlStats.
        :rtype: int
        """
        return self._exec_count

    @exec_count.setter
    def exec_count(self, exec_count):
        """
        Sets the exec_count of this MySqlSqlStats.
        The total number of times the statement has executed.


        :param exec_count: The exec_count of this MySqlSqlStats.
        :type: int
        """
        self._exec_count = exec_count

    @property
    def total_latency_in_ps(self):
        """
        Gets the total_latency_in_ps of this MySqlSqlStats.
        The total wait time (in picoseconds) of timed occurrences of the statement.


        :return: The total_latency_in_ps of this MySqlSqlStats.
        :rtype: int
        """
        return self._total_latency_in_ps

    @total_latency_in_ps.setter
    def total_latency_in_ps(self, total_latency_in_ps):
        """
        Sets the total_latency_in_ps of this MySqlSqlStats.
        The total wait time (in picoseconds) of timed occurrences of the statement.


        :param total_latency_in_ps: The total_latency_in_ps of this MySqlSqlStats.
        :type: int
        """
        self._total_latency_in_ps = total_latency_in_ps

    @property
    def lock_latency_in_ps(self):
        """
        Gets the lock_latency_in_ps of this MySqlSqlStats.
        The total time waiting (in picoseconds) for locks by timed occurrences of the statement.


        :return: The lock_latency_in_ps of this MySqlSqlStats.
        :rtype: int
        """
        return self._lock_latency_in_ps

    @lock_latency_in_ps.setter
    def lock_latency_in_ps(self, lock_latency_in_ps):
        """
        Sets the lock_latency_in_ps of this MySqlSqlStats.
        The total time waiting (in picoseconds) for locks by timed occurrences of the statement.


        :param lock_latency_in_ps: The lock_latency_in_ps of this MySqlSqlStats.
        :type: int
        """
        self._lock_latency_in_ps = lock_latency_in_ps

    @property
    def err_count(self):
        """
        Gets the err_count of this MySqlSqlStats.
        The total number of errors produced by occurrences of the statement.


        :return: The err_count of this MySqlSqlStats.
        :rtype: int
        """
        return self._err_count

    @err_count.setter
    def err_count(self, err_count):
        """
        Sets the err_count of this MySqlSqlStats.
        The total number of errors produced by occurrences of the statement.


        :param err_count: The err_count of this MySqlSqlStats.
        :type: int
        """
        self._err_count = err_count

    @property
    def warn_count(self):
        """
        Gets the warn_count of this MySqlSqlStats.
        The total number of warnings produced by occurrences of the statement.


        :return: The warn_count of this MySqlSqlStats.
        :rtype: int
        """
        return self._warn_count

    @warn_count.setter
    def warn_count(self, warn_count):
        """
        Sets the warn_count of this MySqlSqlStats.
        The total number of warnings produced by occurrences of the statement.


        :param warn_count: The warn_count of this MySqlSqlStats.
        :type: int
        """
        self._warn_count = warn_count

    @property
    def rows_affected(self):
        """
        Gets the rows_affected of this MySqlSqlStats.
        The total number of rows affected by occurrences of the statement.


        :return: The rows_affected of this MySqlSqlStats.
        :rtype: int
        """
        return self._rows_affected

    @rows_affected.setter
    def rows_affected(self, rows_affected):
        """
        Sets the rows_affected of this MySqlSqlStats.
        The total number of rows affected by occurrences of the statement.


        :param rows_affected: The rows_affected of this MySqlSqlStats.
        :type: int
        """
        self._rows_affected = rows_affected

    @property
    def rows_sent(self):
        """
        Gets the rows_sent of this MySqlSqlStats.
        The total number of rows returned by occurrences of the statement.


        :return: The rows_sent of this MySqlSqlStats.
        :rtype: int
        """
        return self._rows_sent

    @rows_sent.setter
    def rows_sent(self, rows_sent):
        """
        Sets the rows_sent of this MySqlSqlStats.
        The total number of rows returned by occurrences of the statement.


        :param rows_sent: The rows_sent of this MySqlSqlStats.
        :type: int
        """
        self._rows_sent = rows_sent

    @property
    def rows_examined(self):
        """
        Gets the rows_examined of this MySqlSqlStats.
        The total number of rows read from storage engines by occurrences of the statement.


        :return: The rows_examined of this MySqlSqlStats.
        :rtype: int
        """
        return self._rows_examined

    @rows_examined.setter
    def rows_examined(self, rows_examined):
        """
        Sets the rows_examined of this MySqlSqlStats.
        The total number of rows read from storage engines by occurrences of the statement.


        :param rows_examined: The rows_examined of this MySqlSqlStats.
        :type: int
        """
        self._rows_examined = rows_examined

    @property
    def tmp_disk_tables(self):
        """
        Gets the tmp_disk_tables of this MySqlSqlStats.
        The total number of internal on-disk temporary tables created by occurrences of the statement.


        :return: The tmp_disk_tables of this MySqlSqlStats.
        :rtype: int
        """
        return self._tmp_disk_tables

    @tmp_disk_tables.setter
    def tmp_disk_tables(self, tmp_disk_tables):
        """
        Sets the tmp_disk_tables of this MySqlSqlStats.
        The total number of internal on-disk temporary tables created by occurrences of the statement.


        :param tmp_disk_tables: The tmp_disk_tables of this MySqlSqlStats.
        :type: int
        """
        self._tmp_disk_tables = tmp_disk_tables

    @property
    def tmp_tables(self):
        """
        Gets the tmp_tables of this MySqlSqlStats.
        The total number of internal in-memory temporary tables created by occurrences of the statement Count


        :return: The tmp_tables of this MySqlSqlStats.
        :rtype: int
        """
        return self._tmp_tables

    @tmp_tables.setter
    def tmp_tables(self, tmp_tables):
        """
        Sets the tmp_tables of this MySqlSqlStats.
        The total number of internal in-memory temporary tables created by occurrences of the statement Count


        :param tmp_tables: The tmp_tables of this MySqlSqlStats.
        :type: int
        """
        self._tmp_tables = tmp_tables

    @property
    def select_full_join(self):
        """
        Gets the select_full_join of this MySqlSqlStats.
        The total number of joins that perform table scans because they do not use indexes by occurrences of the statement. If this value is not 0


        :return: The select_full_join of this MySqlSqlStats.
        :rtype: int
        """
        return self._select_full_join

    @select_full_join.setter
    def select_full_join(self, select_full_join):
        """
        Sets the select_full_join of this MySqlSqlStats.
        The total number of joins that perform table scans because they do not use indexes by occurrences of the statement. If this value is not 0


        :param select_full_join: The select_full_join of this MySqlSqlStats.
        :type: int
        """
        self._select_full_join = select_full_join

    @property
    def select_full_range_join(self):
        """
        Gets the select_full_range_join of this MySqlSqlStats.
        The total number of joins that used a range search on a reference table by occurrences of the statement


        :return: The select_full_range_join of this MySqlSqlStats.
        :rtype: int
        """
        return self._select_full_range_join

    @select_full_range_join.setter
    def select_full_range_join(self, select_full_range_join):
        """
        Sets the select_full_range_join of this MySqlSqlStats.
        The total number of joins that used a range search on a reference table by occurrences of the statement


        :param select_full_range_join: The select_full_range_join of this MySqlSqlStats.
        :type: int
        """
        self._select_full_range_join = select_full_range_join

    @property
    def select_range(self):
        """
        Gets the select_range of this MySqlSqlStats.
        The total number of joins that used ranges on the first table by occurrences of the statement. This is normally not a critical issue even if the value is quite large. Count


        :return: The select_range of this MySqlSqlStats.
        :rtype: int
        """
        return self._select_range

    @select_range.setter
    def select_range(self, select_range):
        """
        Sets the select_range of this MySqlSqlStats.
        The total number of joins that used ranges on the first table by occurrences of the statement. This is normally not a critical issue even if the value is quite large. Count


        :param select_range: The select_range of this MySqlSqlStats.
        :type: int
        """
        self._select_range = select_range

    @property
    def select_range_check(self):
        """
        Gets the select_range_check of this MySqlSqlStats.
        The total number of joins without keys that check for key usage after each row by occurrences of the statement. If this is not 0


        :return: The select_range_check of this MySqlSqlStats.
        :rtype: int
        """
        return self._select_range_check

    @select_range_check.setter
    def select_range_check(self, select_range_check):
        """
        Sets the select_range_check of this MySqlSqlStats.
        The total number of joins without keys that check for key usage after each row by occurrences of the statement. If this is not 0


        :param select_range_check: The select_range_check of this MySqlSqlStats.
        :type: int
        """
        self._select_range_check = select_range_check

    @property
    def select_scan(self):
        """
        Gets the select_scan of this MySqlSqlStats.
        The total number of joins that did a full scan of the first table by occurrences of the statement Count


        :return: The select_scan of this MySqlSqlStats.
        :rtype: int
        """
        return self._select_scan

    @select_scan.setter
    def select_scan(self, select_scan):
        """
        Sets the select_scan of this MySqlSqlStats.
        The total number of joins that did a full scan of the first table by occurrences of the statement Count


        :param select_scan: The select_scan of this MySqlSqlStats.
        :type: int
        """
        self._select_scan = select_scan

    @property
    def sort_merge_passes(self):
        """
        Gets the sort_merge_passes of this MySqlSqlStats.
        The total number of sort merge passes by occurrences of the statement.


        :return: The sort_merge_passes of this MySqlSqlStats.
        :rtype: int
        """
        return self._sort_merge_passes

    @sort_merge_passes.setter
    def sort_merge_passes(self, sort_merge_passes):
        """
        Sets the sort_merge_passes of this MySqlSqlStats.
        The total number of sort merge passes by occurrences of the statement.


        :param sort_merge_passes: The sort_merge_passes of this MySqlSqlStats.
        :type: int
        """
        self._sort_merge_passes = sort_merge_passes

    @property
    def sort_range(self):
        """
        Gets the sort_range of this MySqlSqlStats.
        The total number of sorts that were done using ranges by occurrences of the statement.


        :return: The sort_range of this MySqlSqlStats.
        :rtype: int
        """
        return self._sort_range

    @sort_range.setter
    def sort_range(self, sort_range):
        """
        Sets the sort_range of this MySqlSqlStats.
        The total number of sorts that were done using ranges by occurrences of the statement.


        :param sort_range: The sort_range of this MySqlSqlStats.
        :type: int
        """
        self._sort_range = sort_range

    @property
    def rows_sorted(self):
        """
        Gets the rows_sorted of this MySqlSqlStats.
        The total number of rows sorted by occurrences of the statement.


        :return: The rows_sorted of this MySqlSqlStats.
        :rtype: int
        """
        return self._rows_sorted

    @rows_sorted.setter
    def rows_sorted(self, rows_sorted):
        """
        Sets the rows_sorted of this MySqlSqlStats.
        The total number of rows sorted by occurrences of the statement.


        :param rows_sorted: The rows_sorted of this MySqlSqlStats.
        :type: int
        """
        self._rows_sorted = rows_sorted

    @property
    def sort_scan(self):
        """
        Gets the sort_scan of this MySqlSqlStats.
        The total number of sorts that were done by scanning the table by occurrences of the statement.


        :return: The sort_scan of this MySqlSqlStats.
        :rtype: int
        """
        return self._sort_scan

    @sort_scan.setter
    def sort_scan(self, sort_scan):
        """
        Sets the sort_scan of this MySqlSqlStats.
        The total number of sorts that were done by scanning the table by occurrences of the statement.


        :param sort_scan: The sort_scan of this MySqlSqlStats.
        :type: int
        """
        self._sort_scan = sort_scan

    @property
    def no_index_used_count(self):
        """
        Gets the no_index_used_count of this MySqlSqlStats.
        The number of occurences of the statement which performed a table scan without using an index Count


        :return: The no_index_used_count of this MySqlSqlStats.
        :rtype: int
        """
        return self._no_index_used_count

    @no_index_used_count.setter
    def no_index_used_count(self, no_index_used_count):
        """
        Sets the no_index_used_count of this MySqlSqlStats.
        The number of occurences of the statement which performed a table scan without using an index Count


        :param no_index_used_count: The no_index_used_count of this MySqlSqlStats.
        :type: int
        """
        self._no_index_used_count = no_index_used_count

    @property
    def no_good_index_used_count(self):
        """
        Gets the no_good_index_used_count of this MySqlSqlStats.
        The number of occurences of the statement where the server found no good index to use Count


        :return: The no_good_index_used_count of this MySqlSqlStats.
        :rtype: int
        """
        return self._no_good_index_used_count

    @no_good_index_used_count.setter
    def no_good_index_used_count(self, no_good_index_used_count):
        """
        Sets the no_good_index_used_count of this MySqlSqlStats.
        The number of occurences of the statement where the server found no good index to use Count


        :param no_good_index_used_count: The no_good_index_used_count of this MySqlSqlStats.
        :type: int
        """
        self._no_good_index_used_count = no_good_index_used_count

    @property
    def cpu_latency_in_ps(self):
        """
        Gets the cpu_latency_in_ps of this MySqlSqlStats.
        The total time spent on CPU (in picoseconds) for the current thread.


        :return: The cpu_latency_in_ps of this MySqlSqlStats.
        :rtype: int
        """
        return self._cpu_latency_in_ps

    @cpu_latency_in_ps.setter
    def cpu_latency_in_ps(self, cpu_latency_in_ps):
        """
        Sets the cpu_latency_in_ps of this MySqlSqlStats.
        The total time spent on CPU (in picoseconds) for the current thread.


        :param cpu_latency_in_ps: The cpu_latency_in_ps of this MySqlSqlStats.
        :type: int
        """
        self._cpu_latency_in_ps = cpu_latency_in_ps

    @property
    def max_controlled_memory_in_bytes(self):
        """
        Gets the max_controlled_memory_in_bytes of this MySqlSqlStats.
        The maximum amount of controlled memory (in bytes) used by the statement.


        :return: The max_controlled_memory_in_bytes of this MySqlSqlStats.
        :rtype: int
        """
        return self._max_controlled_memory_in_bytes

    @max_controlled_memory_in_bytes.setter
    def max_controlled_memory_in_bytes(self, max_controlled_memory_in_bytes):
        """
        Sets the max_controlled_memory_in_bytes of this MySqlSqlStats.
        The maximum amount of controlled memory (in bytes) used by the statement.


        :param max_controlled_memory_in_bytes: The max_controlled_memory_in_bytes of this MySqlSqlStats.
        :type: int
        """
        self._max_controlled_memory_in_bytes = max_controlled_memory_in_bytes

    @property
    def max_total_memory_in_bytes(self):
        """
        Gets the max_total_memory_in_bytes of this MySqlSqlStats.
        The maximum amount of memory (in bytes) used by the statement.


        :return: The max_total_memory_in_bytes of this MySqlSqlStats.
        :rtype: int
        """
        return self._max_total_memory_in_bytes

    @max_total_memory_in_bytes.setter
    def max_total_memory_in_bytes(self, max_total_memory_in_bytes):
        """
        Sets the max_total_memory_in_bytes of this MySqlSqlStats.
        The maximum amount of memory (in bytes) used by the statement.


        :param max_total_memory_in_bytes: The max_total_memory_in_bytes of this MySqlSqlStats.
        :type: int
        """
        self._max_total_memory_in_bytes = max_total_memory_in_bytes

    @property
    def exec_count_secondary(self):
        """
        Gets the exec_count_secondary of this MySqlSqlStats.
        The total number of times a query was processed on the secondary engine (HEATWAVE) for occurrences of this statement Count.


        :return: The exec_count_secondary of this MySqlSqlStats.
        :rtype: int
        """
        return self._exec_count_secondary

    @exec_count_secondary.setter
    def exec_count_secondary(self, exec_count_secondary):
        """
        Sets the exec_count_secondary of this MySqlSqlStats.
        The total number of times a query was processed on the secondary engine (HEATWAVE) for occurrences of this statement Count.


        :param exec_count_secondary: The exec_count_secondary of this MySqlSqlStats.
        :type: int
        """
        self._exec_count_secondary = exec_count_secondary

    @property
    def time_first_seen(self):
        """
        Gets the time_first_seen of this MySqlSqlStats.
        The time at which statement was first seen.
        Example: `\"2023-01-16 08:04:31.533577\"`


        :return: The time_first_seen of this MySqlSqlStats.
        :rtype: datetime
        """
        return self._time_first_seen

    @time_first_seen.setter
    def time_first_seen(self, time_first_seen):
        """
        Sets the time_first_seen of this MySqlSqlStats.
        The time at which statement was first seen.
        Example: `\"2023-01-16 08:04:31.533577\"`


        :param time_first_seen: The time_first_seen of this MySqlSqlStats.
        :type: datetime
        """
        self._time_first_seen = time_first_seen

    @property
    def time_last_seen(self):
        """
        Gets the time_last_seen of this MySqlSqlStats.
        The time at which statement was most recently seen for all occurrences of the statement.
        Example: `\"2023-01-30 02:17:08.067961\"`


        :return: The time_last_seen of this MySqlSqlStats.
        :rtype: datetime
        """
        return self._time_last_seen

    @time_last_seen.setter
    def time_last_seen(self, time_last_seen):
        """
        Sets the time_last_seen of this MySqlSqlStats.
        The time at which statement was most recently seen for all occurrences of the statement.
        Example: `\"2023-01-30 02:17:08.067961\"`


        :param time_last_seen: The time_last_seen of this MySqlSqlStats.
        :type: datetime
        """
        self._time_last_seen = time_last_seen

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
