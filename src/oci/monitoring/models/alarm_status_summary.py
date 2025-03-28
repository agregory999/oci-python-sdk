# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180401


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AlarmStatusSummary(object):
    """
    A summary of properties for the specified alarm and its current evaluation status.
    For information about alarms, see
    `Alarms Overview`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    For information about endpoints and signing API requests, see
    `About the API`__.
    For information about available SDKs and tools, see
    `SDKS and Other Tools`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#AlarmsOverview
    __ https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm
    __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm
    __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/sdks.htm
    """

    #: A constant which can be used with the severity property of a AlarmStatusSummary.
    #: This constant has a value of "CRITICAL"
    SEVERITY_CRITICAL = "CRITICAL"

    #: A constant which can be used with the severity property of a AlarmStatusSummary.
    #: This constant has a value of "ERROR"
    SEVERITY_ERROR = "ERROR"

    #: A constant which can be used with the severity property of a AlarmStatusSummary.
    #: This constant has a value of "WARNING"
    SEVERITY_WARNING = "WARNING"

    #: A constant which can be used with the severity property of a AlarmStatusSummary.
    #: This constant has a value of "INFO"
    SEVERITY_INFO = "INFO"

    #: A constant which can be used with the status property of a AlarmStatusSummary.
    #: This constant has a value of "FIRING"
    STATUS_FIRING = "FIRING"

    #: A constant which can be used with the status property of a AlarmStatusSummary.
    #: This constant has a value of "OK"
    STATUS_OK = "OK"

    #: A constant which can be used with the status property of a AlarmStatusSummary.
    #: This constant has a value of "SUSPENDED"
    STATUS_SUSPENDED = "SUSPENDED"

    def __init__(self, **kwargs):
        """
        Initializes a new AlarmStatusSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AlarmStatusSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this AlarmStatusSummary.
        :type display_name: str

        :param severity:
            The value to assign to the severity property of this AlarmStatusSummary.
            Allowed values for this property are: "CRITICAL", "ERROR", "WARNING", "INFO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type severity: str

        :param rule_name:
            The value to assign to the rule_name property of this AlarmStatusSummary.
        :type rule_name: str

        :param timestamp_triggered:
            The value to assign to the timestamp_triggered property of this AlarmStatusSummary.
        :type timestamp_triggered: datetime

        :param alarm_summary:
            The value to assign to the alarm_summary property of this AlarmStatusSummary.
        :type alarm_summary: str

        :param status:
            The value to assign to the status property of this AlarmStatusSummary.
            Allowed values for this property are: "FIRING", "OK", "SUSPENDED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param suppression:
            The value to assign to the suppression property of this AlarmStatusSummary.
        :type suppression: oci.monitoring.models.Suppression

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'severity': 'str',
            'rule_name': 'str',
            'timestamp_triggered': 'datetime',
            'alarm_summary': 'str',
            'status': 'str',
            'suppression': 'Suppression'
        }
        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'severity': 'severity',
            'rule_name': 'ruleName',
            'timestamp_triggered': 'timestampTriggered',
            'alarm_summary': 'alarmSummary',
            'status': 'status',
            'suppression': 'suppression'
        }
        self._id = None
        self._display_name = None
        self._severity = None
        self._rule_name = None
        self._timestamp_triggered = None
        self._alarm_summary = None
        self._status = None
        self._suppression = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AlarmStatusSummary.
        The `OCID`__ of the alarm.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this AlarmStatusSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AlarmStatusSummary.
        The `OCID`__ of the alarm.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this AlarmStatusSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AlarmStatusSummary.
        The configured name of the alarm.

        Example: `High CPU Utilization`


        :return: The display_name of this AlarmStatusSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AlarmStatusSummary.
        The configured name of the alarm.

        Example: `High CPU Utilization`


        :param display_name: The display_name of this AlarmStatusSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def severity(self):
        """
        **[Required]** Gets the severity of this AlarmStatusSummary.
        The perceived type of response required when the alarm is in the \"FIRING\" state.

        Example: `CRITICAL`

        Allowed values for this property are: "CRITICAL", "ERROR", "WARNING", "INFO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The severity of this AlarmStatusSummary.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this AlarmStatusSummary.
        The perceived type of response required when the alarm is in the \"FIRING\" state.

        Example: `CRITICAL`


        :param severity: The severity of this AlarmStatusSummary.
        :type: str
        """
        allowed_values = ["CRITICAL", "ERROR", "WARNING", "INFO"]
        if not value_allowed_none_or_none_sentinel(severity, allowed_values):
            severity = 'UNKNOWN_ENUM_VALUE'
        self._severity = severity

    @property
    def rule_name(self):
        """
        **[Required]** Gets the rule_name of this AlarmStatusSummary.
        Identifier of the alarm's base values for alarm evaluation, for use when the alarm contains overrides.
        Default value is `BASE`. For information about alarm overrides, see :func:`alarm_override`.


        :return: The rule_name of this AlarmStatusSummary.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """
        Sets the rule_name of this AlarmStatusSummary.
        Identifier of the alarm's base values for alarm evaluation, for use when the alarm contains overrides.
        Default value is `BASE`. For information about alarm overrides, see :func:`alarm_override`.


        :param rule_name: The rule_name of this AlarmStatusSummary.
        :type: str
        """
        self._rule_name = rule_name

    @property
    def timestamp_triggered(self):
        """
        **[Required]** Gets the timestamp_triggered of this AlarmStatusSummary.
        Timestamp for the transition of the alarm state. For example, the time when the alarm transitioned from OK to Firing.
        Note: A three-minute lag for this value accounts for any late-arriving metrics.

        Example: `2023-02-01T01:02:29.600Z`


        :return: The timestamp_triggered of this AlarmStatusSummary.
        :rtype: datetime
        """
        return self._timestamp_triggered

    @timestamp_triggered.setter
    def timestamp_triggered(self, timestamp_triggered):
        """
        Sets the timestamp_triggered of this AlarmStatusSummary.
        Timestamp for the transition of the alarm state. For example, the time when the alarm transitioned from OK to Firing.
        Note: A three-minute lag for this value accounts for any late-arriving metrics.

        Example: `2023-02-01T01:02:29.600Z`


        :param timestamp_triggered: The timestamp_triggered of this AlarmStatusSummary.
        :type: datetime
        """
        self._timestamp_triggered = timestamp_triggered

    @property
    def alarm_summary(self):
        """
        **[Required]** Gets the alarm_summary of this AlarmStatusSummary.
        Customizable alarm summary (`alarmSummary` `alarm message parameter`__).
        Optionally include `dynamic variables`__.
        The alarm summary appears within the body of the alarm message and in responses to
        :func:`list_alarms_status`
        :func:`get_alarm_history` and
        :func:`retrieve_dimension_states`.

        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/alarm-message-format.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm


        :return: The alarm_summary of this AlarmStatusSummary.
        :rtype: str
        """
        return self._alarm_summary

    @alarm_summary.setter
    def alarm_summary(self, alarm_summary):
        """
        Sets the alarm_summary of this AlarmStatusSummary.
        Customizable alarm summary (`alarmSummary` `alarm message parameter`__).
        Optionally include `dynamic variables`__.
        The alarm summary appears within the body of the alarm message and in responses to
        :func:`list_alarms_status`
        :func:`get_alarm_history` and
        :func:`retrieve_dimension_states`.

        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/alarm-message-format.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm


        :param alarm_summary: The alarm_summary of this AlarmStatusSummary.
        :type: str
        """
        self._alarm_summary = alarm_summary

    @property
    def status(self):
        """
        **[Required]** Gets the status of this AlarmStatusSummary.
        The status of this alarm.
        Status is collective, across all metric streams in the alarm.
        To list alarm status for each metric stream, use :func:`retrieve_dimension_states`.

        Example: `FIRING`

        Allowed values for this property are: "FIRING", "OK", "SUSPENDED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this AlarmStatusSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AlarmStatusSummary.
        The status of this alarm.
        Status is collective, across all metric streams in the alarm.
        To list alarm status for each metric stream, use :func:`retrieve_dimension_states`.

        Example: `FIRING`


        :param status: The status of this AlarmStatusSummary.
        :type: str
        """
        allowed_values = ["FIRING", "OK", "SUSPENDED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def suppression(self):
        """
        Gets the suppression of this AlarmStatusSummary.
        The configuration details for suppressing an alarm.


        :return: The suppression of this AlarmStatusSummary.
        :rtype: oci.monitoring.models.Suppression
        """
        return self._suppression

    @suppression.setter
    def suppression(self, suppression):
        """
        Sets the suppression of this AlarmStatusSummary.
        The configuration details for suppressing an alarm.


        :param suppression: The suppression of this AlarmStatusSummary.
        :type: oci.monitoring.models.Suppression
        """
        self._suppression = suppression

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
