# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlTuningSet(object):
    """
    Details of the Sql tuning set.
    """

    #: A constant which can be used with the status property of a SqlTuningSet.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    #: A constant which can be used with the status property of a SqlTuningSet.
    #: This constant has a value of "RETRY_SCHEDULED"
    STATUS_RETRY_SCHEDULED = "RETRY_SCHEDULED"

    #: A constant which can be used with the status property of a SqlTuningSet.
    #: This constant has a value of "SCHEDULED"
    STATUS_SCHEDULED = "SCHEDULED"

    #: A constant which can be used with the status property of a SqlTuningSet.
    #: This constant has a value of "BLOCKED"
    STATUS_BLOCKED = "BLOCKED"

    #: A constant which can be used with the status property of a SqlTuningSet.
    #: This constant has a value of "RUNNING"
    STATUS_RUNNING = "RUNNING"

    #: A constant which can be used with the status property of a SqlTuningSet.
    #: This constant has a value of "COMPLETED"
    STATUS_COMPLETED = "COMPLETED"

    #: A constant which can be used with the status property of a SqlTuningSet.
    #: This constant has a value of "BROKEN"
    STATUS_BROKEN = "BROKEN"

    #: A constant which can be used with the status property of a SqlTuningSet.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a SqlTuningSet.
    #: This constant has a value of "REMOTE"
    STATUS_REMOTE = "REMOTE"

    #: A constant which can be used with the status property of a SqlTuningSet.
    #: This constant has a value of "RESOURCE_UNAVAILABLE"
    STATUS_RESOURCE_UNAVAILABLE = "RESOURCE_UNAVAILABLE"

    #: A constant which can be used with the status property of a SqlTuningSet.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a SqlTuningSet.
    #: This constant has a value of "CHAIN_STALLED"
    STATUS_CHAIN_STALLED = "CHAIN_STALLED"

    #: A constant which can be used with the all_sql_statements_fetched property of a SqlTuningSet.
    #: This constant has a value of "YES"
    ALL_SQL_STATEMENTS_FETCHED_YES = "YES"

    #: A constant which can be used with the all_sql_statements_fetched property of a SqlTuningSet.
    #: This constant has a value of "NO"
    ALL_SQL_STATEMENTS_FETCHED_NO = "NO"

    def __init__(self, **kwargs):
        """
        Initializes a new SqlTuningSet object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SqlTuningSet.
        :type id: int

        :param owner:
            The value to assign to the owner property of this SqlTuningSet.
        :type owner: str

        :param name:
            The value to assign to the name property of this SqlTuningSet.
        :type name: str

        :param statement_count:
            The value to assign to the statement_count property of this SqlTuningSet.
        :type statement_count: int

        :param time_created:
            The value to assign to the time_created property of this SqlTuningSet.
        :type time_created: datetime

        :param description:
            The value to assign to the description property of this SqlTuningSet.
        :type description: str

        :param time_last_modified:
            The value to assign to the time_last_modified property of this SqlTuningSet.
        :type time_last_modified: datetime

        :param status:
            The value to assign to the status property of this SqlTuningSet.
            Allowed values for this property are: "DISABLED", "RETRY_SCHEDULED", "SCHEDULED", "BLOCKED", "RUNNING", "COMPLETED", "BROKEN", "FAILED", "REMOTE", "RESOURCE_UNAVAILABLE", "SUCCEEDED", "CHAIN_STALLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param scheduled_job_name:
            The value to assign to the scheduled_job_name property of this SqlTuningSet.
        :type scheduled_job_name: str

        :param error_message:
            The value to assign to the error_message property of this SqlTuningSet.
        :type error_message: str

        :param all_sql_statements_fetched:
            The value to assign to the all_sql_statements_fetched property of this SqlTuningSet.
            Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type all_sql_statements_fetched: str

        :param sql_list:
            The value to assign to the sql_list property of this SqlTuningSet.
        :type sql_list: list[oci.database_management.models.SqlInSqlTuningSet]

        """
        self.swagger_types = {
            'id': 'int',
            'owner': 'str',
            'name': 'str',
            'statement_count': 'int',
            'time_created': 'datetime',
            'description': 'str',
            'time_last_modified': 'datetime',
            'status': 'str',
            'scheduled_job_name': 'str',
            'error_message': 'str',
            'all_sql_statements_fetched': 'str',
            'sql_list': 'list[SqlInSqlTuningSet]'
        }
        self.attribute_map = {
            'id': 'id',
            'owner': 'owner',
            'name': 'name',
            'statement_count': 'statementCount',
            'time_created': 'timeCreated',
            'description': 'description',
            'time_last_modified': 'timeLastModified',
            'status': 'status',
            'scheduled_job_name': 'scheduledJobName',
            'error_message': 'errorMessage',
            'all_sql_statements_fetched': 'allSqlStatementsFetched',
            'sql_list': 'sqlList'
        }
        self._id = None
        self._owner = None
        self._name = None
        self._statement_count = None
        self._time_created = None
        self._description = None
        self._time_last_modified = None
        self._status = None
        self._scheduled_job_name = None
        self._error_message = None
        self._all_sql_statements_fetched = None
        self._sql_list = None

    @property
    def id(self):
        """
        Gets the id of this SqlTuningSet.
        The unique Sql tuning set identifier.


        :return: The id of this SqlTuningSet.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SqlTuningSet.
        The unique Sql tuning set identifier.


        :param id: The id of this SqlTuningSet.
        :type: int
        """
        self._id = id

    @property
    def owner(self):
        """
        **[Required]** Gets the owner of this SqlTuningSet.
        The owner of the Sql tuning set.


        :return: The owner of this SqlTuningSet.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this SqlTuningSet.
        The owner of the Sql tuning set.


        :param owner: The owner of this SqlTuningSet.
        :type: str
        """
        self._owner = owner

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SqlTuningSet.
        The name of the Sql tuning set.


        :return: The name of this SqlTuningSet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SqlTuningSet.
        The name of the Sql tuning set.


        :param name: The name of this SqlTuningSet.
        :type: str
        """
        self._name = name

    @property
    def statement_count(self):
        """
        Gets the statement_count of this SqlTuningSet.
        Number of statements in the Sql tuning set


        :return: The statement_count of this SqlTuningSet.
        :rtype: int
        """
        return self._statement_count

    @statement_count.setter
    def statement_count(self, statement_count):
        """
        Sets the statement_count of this SqlTuningSet.
        Number of statements in the Sql tuning set


        :param statement_count: The statement_count of this SqlTuningSet.
        :type: int
        """
        self._statement_count = statement_count

    @property
    def time_created(self):
        """
        Gets the time_created of this SqlTuningSet.
        The created time of the Sql tuning set.


        :return: The time_created of this SqlTuningSet.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SqlTuningSet.
        The created time of the Sql tuning set.


        :param time_created: The time_created of this SqlTuningSet.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def description(self):
        """
        Gets the description of this SqlTuningSet.
        The description of the Sql tuning set.


        :return: The description of this SqlTuningSet.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SqlTuningSet.
        The description of the Sql tuning set.


        :param description: The description of this SqlTuningSet.
        :type: str
        """
        self._description = description

    @property
    def time_last_modified(self):
        """
        Gets the time_last_modified of this SqlTuningSet.
        Last modified time of the Sql tuning set.


        :return: The time_last_modified of this SqlTuningSet.
        :rtype: datetime
        """
        return self._time_last_modified

    @time_last_modified.setter
    def time_last_modified(self, time_last_modified):
        """
        Sets the time_last_modified of this SqlTuningSet.
        Last modified time of the Sql tuning set.


        :param time_last_modified: The time_last_modified of this SqlTuningSet.
        :type: datetime
        """
        self._time_last_modified = time_last_modified

    @property
    def status(self):
        """
        Gets the status of this SqlTuningSet.
        Current status of the Sql tuning set.

        Allowed values for this property are: "DISABLED", "RETRY_SCHEDULED", "SCHEDULED", "BLOCKED", "RUNNING", "COMPLETED", "BROKEN", "FAILED", "REMOTE", "RESOURCE_UNAVAILABLE", "SUCCEEDED", "CHAIN_STALLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this SqlTuningSet.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this SqlTuningSet.
        Current status of the Sql tuning set.


        :param status: The status of this SqlTuningSet.
        :type: str
        """
        allowed_values = ["DISABLED", "RETRY_SCHEDULED", "SCHEDULED", "BLOCKED", "RUNNING", "COMPLETED", "BROKEN", "FAILED", "REMOTE", "RESOURCE_UNAVAILABLE", "SUCCEEDED", "CHAIN_STALLED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def scheduled_job_name(self):
        """
        Gets the scheduled_job_name of this SqlTuningSet.
        Name of the Sql tuning set scheduler job.


        :return: The scheduled_job_name of this SqlTuningSet.
        :rtype: str
        """
        return self._scheduled_job_name

    @scheduled_job_name.setter
    def scheduled_job_name(self, scheduled_job_name):
        """
        Sets the scheduled_job_name of this SqlTuningSet.
        Name of the Sql tuning set scheduler job.


        :param scheduled_job_name: The scheduled_job_name of this SqlTuningSet.
        :type: str
        """
        self._scheduled_job_name = scheduled_job_name

    @property
    def error_message(self):
        """
        Gets the error_message of this SqlTuningSet.
        Latest execution error of the plsql that was submitted as a scheduler job.


        :return: The error_message of this SqlTuningSet.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this SqlTuningSet.
        Latest execution error of the plsql that was submitted as a scheduler job.


        :param error_message: The error_message of this SqlTuningSet.
        :type: str
        """
        self._error_message = error_message

    @property
    def all_sql_statements_fetched(self):
        """
        Gets the all_sql_statements_fetched of this SqlTuningSet.
        In OCI database management, there is a limit to fetch only 2000 rows.
        This flag indicates whether all Sql statements of this Sql tuning set matching the filter criteria are fetched or not.
        Possible values are 'Yes' or 'No'
          - Yes - All Sql statements matching the filter criteria are fetched.
          - No  - There are more Sql statements matching the fitler criteria.
                  User should fine tune the filter criteria to narrow down the result set.

        Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The all_sql_statements_fetched of this SqlTuningSet.
        :rtype: str
        """
        return self._all_sql_statements_fetched

    @all_sql_statements_fetched.setter
    def all_sql_statements_fetched(self, all_sql_statements_fetched):
        """
        Sets the all_sql_statements_fetched of this SqlTuningSet.
        In OCI database management, there is a limit to fetch only 2000 rows.
        This flag indicates whether all Sql statements of this Sql tuning set matching the filter criteria are fetched or not.
        Possible values are 'Yes' or 'No'
          - Yes - All Sql statements matching the filter criteria are fetched.
          - No  - There are more Sql statements matching the fitler criteria.
                  User should fine tune the filter criteria to narrow down the result set.


        :param all_sql_statements_fetched: The all_sql_statements_fetched of this SqlTuningSet.
        :type: str
        """
        allowed_values = ["YES", "NO"]
        if not value_allowed_none_or_none_sentinel(all_sql_statements_fetched, allowed_values):
            all_sql_statements_fetched = 'UNKNOWN_ENUM_VALUE'
        self._all_sql_statements_fetched = all_sql_statements_fetched

    @property
    def sql_list(self):
        """
        Gets the sql_list of this SqlTuningSet.
        A list of the Sqls associated with the Sql tuning set.


        :return: The sql_list of this SqlTuningSet.
        :rtype: list[oci.database_management.models.SqlInSqlTuningSet]
        """
        return self._sql_list

    @sql_list.setter
    def sql_list(self, sql_list):
        """
        Sets the sql_list of this SqlTuningSet.
        A list of the Sqls associated with the Sql tuning set.


        :param sql_list: The sql_list of this SqlTuningSet.
        :type: list[oci.database_management.models.SqlInSqlTuningSet]
        """
        self._sql_list = sql_list

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
