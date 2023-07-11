# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlPlanBaselineSummary(object):
    """
    The summary of a SQL plan baseline.
    """

    #: A constant which can be used with the origin property of a SqlPlanBaselineSummary.
    #: This constant has a value of "ADDM_SQLTUNE"
    ORIGIN_ADDM_SQLTUNE = "ADDM_SQLTUNE"

    #: A constant which can be used with the origin property of a SqlPlanBaselineSummary.
    #: This constant has a value of "AUTO_CAPTURE"
    ORIGIN_AUTO_CAPTURE = "AUTO_CAPTURE"

    #: A constant which can be used with the origin property of a SqlPlanBaselineSummary.
    #: This constant has a value of "AUTO_SQLTUNE"
    ORIGIN_AUTO_SQLTUNE = "AUTO_SQLTUNE"

    #: A constant which can be used with the origin property of a SqlPlanBaselineSummary.
    #: This constant has a value of "EVOLVE_AUTO_INDEX_LOAD"
    ORIGIN_EVOLVE_AUTO_INDEX_LOAD = "EVOLVE_AUTO_INDEX_LOAD"

    #: A constant which can be used with the origin property of a SqlPlanBaselineSummary.
    #: This constant has a value of "EVOLVE_CREATE_FROM_ADAPTIVE"
    ORIGIN_EVOLVE_CREATE_FROM_ADAPTIVE = "EVOLVE_CREATE_FROM_ADAPTIVE"

    #: A constant which can be used with the origin property of a SqlPlanBaselineSummary.
    #: This constant has a value of "EVOLVE_LOAD_FROM_STS"
    ORIGIN_EVOLVE_LOAD_FROM_STS = "EVOLVE_LOAD_FROM_STS"

    #: A constant which can be used with the origin property of a SqlPlanBaselineSummary.
    #: This constant has a value of "EVOLVE_LOAD_FROM_AWR"
    ORIGIN_EVOLVE_LOAD_FROM_AWR = "EVOLVE_LOAD_FROM_AWR"

    #: A constant which can be used with the origin property of a SqlPlanBaselineSummary.
    #: This constant has a value of "EVOLVE_LOAD_FROM_CURSOR_CACHE"
    ORIGIN_EVOLVE_LOAD_FROM_CURSOR_CACHE = "EVOLVE_LOAD_FROM_CURSOR_CACHE"

    #: A constant which can be used with the origin property of a SqlPlanBaselineSummary.
    #: This constant has a value of "MANUAL_LOAD"
    ORIGIN_MANUAL_LOAD = "MANUAL_LOAD"

    #: A constant which can be used with the origin property of a SqlPlanBaselineSummary.
    #: This constant has a value of "MANUAL_LOAD_FROM_AWR"
    ORIGIN_MANUAL_LOAD_FROM_AWR = "MANUAL_LOAD_FROM_AWR"

    #: A constant which can be used with the origin property of a SqlPlanBaselineSummary.
    #: This constant has a value of "MANUAL_LOAD_FROM_CURSOR_CACHE"
    ORIGIN_MANUAL_LOAD_FROM_CURSOR_CACHE = "MANUAL_LOAD_FROM_CURSOR_CACHE"

    #: A constant which can be used with the origin property of a SqlPlanBaselineSummary.
    #: This constant has a value of "MANUAL_LOAD_FROM_STS"
    ORIGIN_MANUAL_LOAD_FROM_STS = "MANUAL_LOAD_FROM_STS"

    #: A constant which can be used with the origin property of a SqlPlanBaselineSummary.
    #: This constant has a value of "MANUAL_SQLTUNE"
    ORIGIN_MANUAL_SQLTUNE = "MANUAL_SQLTUNE"

    #: A constant which can be used with the origin property of a SqlPlanBaselineSummary.
    #: This constant has a value of "STORED_OUTLINE"
    ORIGIN_STORED_OUTLINE = "STORED_OUTLINE"

    #: A constant which can be used with the origin property of a SqlPlanBaselineSummary.
    #: This constant has a value of "UNKNOWN"
    ORIGIN_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new SqlPlanBaselineSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param plan_name:
            The value to assign to the plan_name property of this SqlPlanBaselineSummary.
        :type plan_name: str

        :param sql_handle:
            The value to assign to the sql_handle property of this SqlPlanBaselineSummary.
        :type sql_handle: str

        :param sql_text:
            The value to assign to the sql_text property of this SqlPlanBaselineSummary.
        :type sql_text: str

        :param origin:
            The value to assign to the origin property of this SqlPlanBaselineSummary.
            Allowed values for this property are: "ADDM_SQLTUNE", "AUTO_CAPTURE", "AUTO_SQLTUNE", "EVOLVE_AUTO_INDEX_LOAD", "EVOLVE_CREATE_FROM_ADAPTIVE", "EVOLVE_LOAD_FROM_STS", "EVOLVE_LOAD_FROM_AWR", "EVOLVE_LOAD_FROM_CURSOR_CACHE", "MANUAL_LOAD", "MANUAL_LOAD_FROM_AWR", "MANUAL_LOAD_FROM_CURSOR_CACHE", "MANUAL_LOAD_FROM_STS", "MANUAL_SQLTUNE", "STORED_OUTLINE", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type origin: str

        :param time_created:
            The value to assign to the time_created property of this SqlPlanBaselineSummary.
        :type time_created: datetime

        :param time_last_modified:
            The value to assign to the time_last_modified property of this SqlPlanBaselineSummary.
        :type time_last_modified: datetime

        :param time_last_executed:
            The value to assign to the time_last_executed property of this SqlPlanBaselineSummary.
        :type time_last_executed: datetime

        :param enabled:
            The value to assign to the enabled property of this SqlPlanBaselineSummary.
        :type enabled: str

        :param accepted:
            The value to assign to the accepted property of this SqlPlanBaselineSummary.
        :type accepted: str

        :param fixed:
            The value to assign to the fixed property of this SqlPlanBaselineSummary.
        :type fixed: str

        :param reproduced:
            The value to assign to the reproduced property of this SqlPlanBaselineSummary.
        :type reproduced: str

        :param auto_purge:
            The value to assign to the auto_purge property of this SqlPlanBaselineSummary.
        :type auto_purge: str

        :param adaptive:
            The value to assign to the adaptive property of this SqlPlanBaselineSummary.
        :type adaptive: str

        """
        self.swagger_types = {
            'plan_name': 'str',
            'sql_handle': 'str',
            'sql_text': 'str',
            'origin': 'str',
            'time_created': 'datetime',
            'time_last_modified': 'datetime',
            'time_last_executed': 'datetime',
            'enabled': 'str',
            'accepted': 'str',
            'fixed': 'str',
            'reproduced': 'str',
            'auto_purge': 'str',
            'adaptive': 'str'
        }

        self.attribute_map = {
            'plan_name': 'planName',
            'sql_handle': 'sqlHandle',
            'sql_text': 'sqlText',
            'origin': 'origin',
            'time_created': 'timeCreated',
            'time_last_modified': 'timeLastModified',
            'time_last_executed': 'timeLastExecuted',
            'enabled': 'enabled',
            'accepted': 'accepted',
            'fixed': 'fixed',
            'reproduced': 'reproduced',
            'auto_purge': 'autoPurge',
            'adaptive': 'adaptive'
        }

        self._plan_name = None
        self._sql_handle = None
        self._sql_text = None
        self._origin = None
        self._time_created = None
        self._time_last_modified = None
        self._time_last_executed = None
        self._enabled = None
        self._accepted = None
        self._fixed = None
        self._reproduced = None
        self._auto_purge = None
        self._adaptive = None

    @property
    def plan_name(self):
        """
        **[Required]** Gets the plan_name of this SqlPlanBaselineSummary.
        The unique plan identifier.


        :return: The plan_name of this SqlPlanBaselineSummary.
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """
        Sets the plan_name of this SqlPlanBaselineSummary.
        The unique plan identifier.


        :param plan_name: The plan_name of this SqlPlanBaselineSummary.
        :type: str
        """
        self._plan_name = plan_name

    @property
    def sql_handle(self):
        """
        **[Required]** Gets the sql_handle of this SqlPlanBaselineSummary.
        The unique SQL identifier.


        :return: The sql_handle of this SqlPlanBaselineSummary.
        :rtype: str
        """
        return self._sql_handle

    @sql_handle.setter
    def sql_handle(self, sql_handle):
        """
        Sets the sql_handle of this SqlPlanBaselineSummary.
        The unique SQL identifier.


        :param sql_handle: The sql_handle of this SqlPlanBaselineSummary.
        :type: str
        """
        self._sql_handle = sql_handle

    @property
    def sql_text(self):
        """
        **[Required]** Gets the sql_text of this SqlPlanBaselineSummary.
        The SQL text (truncated to the first 50 characters).


        :return: The sql_text of this SqlPlanBaselineSummary.
        :rtype: str
        """
        return self._sql_text

    @sql_text.setter
    def sql_text(self, sql_text):
        """
        Sets the sql_text of this SqlPlanBaselineSummary.
        The SQL text (truncated to the first 50 characters).


        :param sql_text: The sql_text of this SqlPlanBaselineSummary.
        :type: str
        """
        self._sql_text = sql_text

    @property
    def origin(self):
        """
        Gets the origin of this SqlPlanBaselineSummary.
        The origin of the SQL plan baseline.

        Allowed values for this property are: "ADDM_SQLTUNE", "AUTO_CAPTURE", "AUTO_SQLTUNE", "EVOLVE_AUTO_INDEX_LOAD", "EVOLVE_CREATE_FROM_ADAPTIVE", "EVOLVE_LOAD_FROM_STS", "EVOLVE_LOAD_FROM_AWR", "EVOLVE_LOAD_FROM_CURSOR_CACHE", "MANUAL_LOAD", "MANUAL_LOAD_FROM_AWR", "MANUAL_LOAD_FROM_CURSOR_CACHE", "MANUAL_LOAD_FROM_STS", "MANUAL_SQLTUNE", "STORED_OUTLINE", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The origin of this SqlPlanBaselineSummary.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """
        Sets the origin of this SqlPlanBaselineSummary.
        The origin of the SQL plan baseline.


        :param origin: The origin of this SqlPlanBaselineSummary.
        :type: str
        """
        allowed_values = ["ADDM_SQLTUNE", "AUTO_CAPTURE", "AUTO_SQLTUNE", "EVOLVE_AUTO_INDEX_LOAD", "EVOLVE_CREATE_FROM_ADAPTIVE", "EVOLVE_LOAD_FROM_STS", "EVOLVE_LOAD_FROM_AWR", "EVOLVE_LOAD_FROM_CURSOR_CACHE", "MANUAL_LOAD", "MANUAL_LOAD_FROM_AWR", "MANUAL_LOAD_FROM_CURSOR_CACHE", "MANUAL_LOAD_FROM_STS", "MANUAL_SQLTUNE", "STORED_OUTLINE", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(origin, allowed_values):
            origin = 'UNKNOWN_ENUM_VALUE'
        self._origin = origin

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this SqlPlanBaselineSummary.
        The date and time when the plan baseline was created.


        :return: The time_created of this SqlPlanBaselineSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SqlPlanBaselineSummary.
        The date and time when the plan baseline was created.


        :param time_created: The time_created of this SqlPlanBaselineSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_last_modified(self):
        """
        Gets the time_last_modified of this SqlPlanBaselineSummary.
        The date and time when the plan baseline was last modified.


        :return: The time_last_modified of this SqlPlanBaselineSummary.
        :rtype: datetime
        """
        return self._time_last_modified

    @time_last_modified.setter
    def time_last_modified(self, time_last_modified):
        """
        Sets the time_last_modified of this SqlPlanBaselineSummary.
        The date and time when the plan baseline was last modified.


        :param time_last_modified: The time_last_modified of this SqlPlanBaselineSummary.
        :type: datetime
        """
        self._time_last_modified = time_last_modified

    @property
    def time_last_executed(self):
        """
        Gets the time_last_executed of this SqlPlanBaselineSummary.
        The date and time when the plan baseline was last executed.

        **Note:** For performance reasons, database does not update this value
        immediately after each execution of the plan baseline. Therefore, the plan
        baseline may have been executed more recently than this value indicates.


        :return: The time_last_executed of this SqlPlanBaselineSummary.
        :rtype: datetime
        """
        return self._time_last_executed

    @time_last_executed.setter
    def time_last_executed(self, time_last_executed):
        """
        Sets the time_last_executed of this SqlPlanBaselineSummary.
        The date and time when the plan baseline was last executed.

        **Note:** For performance reasons, database does not update this value
        immediately after each execution of the plan baseline. Therefore, the plan
        baseline may have been executed more recently than this value indicates.


        :param time_last_executed: The time_last_executed of this SqlPlanBaselineSummary.
        :type: datetime
        """
        self._time_last_executed = time_last_executed

    @property
    def enabled(self):
        """
        Gets the enabled of this SqlPlanBaselineSummary.
        Indicates whether the plan baseline is enabled (`YES`) or disabled (`NO`).


        :return: The enabled of this SqlPlanBaselineSummary.
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this SqlPlanBaselineSummary.
        Indicates whether the plan baseline is enabled (`YES`) or disabled (`NO`).


        :param enabled: The enabled of this SqlPlanBaselineSummary.
        :type: str
        """
        self._enabled = enabled

    @property
    def accepted(self):
        """
        Gets the accepted of this SqlPlanBaselineSummary.
        Indicates whether the plan baseline is accepted (`YES`) or not (`NO`).


        :return: The accepted of this SqlPlanBaselineSummary.
        :rtype: str
        """
        return self._accepted

    @accepted.setter
    def accepted(self, accepted):
        """
        Sets the accepted of this SqlPlanBaselineSummary.
        Indicates whether the plan baseline is accepted (`YES`) or not (`NO`).


        :param accepted: The accepted of this SqlPlanBaselineSummary.
        :type: str
        """
        self._accepted = accepted

    @property
    def fixed(self):
        """
        Gets the fixed of this SqlPlanBaselineSummary.
        Indicates whether the plan baseline is fixed (`YES`) or not (`NO`).


        :return: The fixed of this SqlPlanBaselineSummary.
        :rtype: str
        """
        return self._fixed

    @fixed.setter
    def fixed(self, fixed):
        """
        Sets the fixed of this SqlPlanBaselineSummary.
        Indicates whether the plan baseline is fixed (`YES`) or not (`NO`).


        :param fixed: The fixed of this SqlPlanBaselineSummary.
        :type: str
        """
        self._fixed = fixed

    @property
    def reproduced(self):
        """
        Gets the reproduced of this SqlPlanBaselineSummary.
        Indicates whether the optimizer was able to reproduce the plan (`YES`) or not (`NO`).
        The value is set to `YES` when a plan is initially added to the plan baseline.


        :return: The reproduced of this SqlPlanBaselineSummary.
        :rtype: str
        """
        return self._reproduced

    @reproduced.setter
    def reproduced(self, reproduced):
        """
        Sets the reproduced of this SqlPlanBaselineSummary.
        Indicates whether the optimizer was able to reproduce the plan (`YES`) or not (`NO`).
        The value is set to `YES` when a plan is initially added to the plan baseline.


        :param reproduced: The reproduced of this SqlPlanBaselineSummary.
        :type: str
        """
        self._reproduced = reproduced

    @property
    def auto_purge(self):
        """
        Gets the auto_purge of this SqlPlanBaselineSummary.
        Indicates whether the plan baseline is auto-purged (`YES`) or not (`NO`).


        :return: The auto_purge of this SqlPlanBaselineSummary.
        :rtype: str
        """
        return self._auto_purge

    @auto_purge.setter
    def auto_purge(self, auto_purge):
        """
        Sets the auto_purge of this SqlPlanBaselineSummary.
        Indicates whether the plan baseline is auto-purged (`YES`) or not (`NO`).


        :param auto_purge: The auto_purge of this SqlPlanBaselineSummary.
        :type: str
        """
        self._auto_purge = auto_purge

    @property
    def adaptive(self):
        """
        Gets the adaptive of this SqlPlanBaselineSummary.
        Indicates whether a plan that is automatically captured by SQL plan management is marked adaptive or not.

        When a new adaptive plan is found for a SQL statement that has an existing SQL plan baseline, that new plan
        will be added to the SQL plan baseline as an unaccepted plan, and the `ADAPTIVE` property will be marked `YES`.
        When this new plan is verified (either manually or via the auto evolve task), the plan will be test executed
        and the final plan determined at execution will become an accepted plan if its performance is better than
        the existing plan baseline. At this point, the value of the `ADAPTIVE` property is set to `NO` since the plan
        is no longer adaptive, but resolved.


        :return: The adaptive of this SqlPlanBaselineSummary.
        :rtype: str
        """
        return self._adaptive

    @adaptive.setter
    def adaptive(self, adaptive):
        """
        Sets the adaptive of this SqlPlanBaselineSummary.
        Indicates whether a plan that is automatically captured by SQL plan management is marked adaptive or not.

        When a new adaptive plan is found for a SQL statement that has an existing SQL plan baseline, that new plan
        will be added to the SQL plan baseline as an unaccepted plan, and the `ADAPTIVE` property will be marked `YES`.
        When this new plan is verified (either manually or via the auto evolve task), the plan will be test executed
        and the final plan determined at execution will become an accepted plan if its performance is better than
        the existing plan baseline. At this point, the value of the `ADAPTIVE` property is set to `NO` since the plan
        is no longer adaptive, but resolved.


        :param adaptive: The adaptive of this SqlPlanBaselineSummary.
        :type: str
        """
        self._adaptive = adaptive

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
