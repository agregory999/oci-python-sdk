# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AlarmCondition(object):
    """
    The information about template condition in the same monitoringTemplate in a compartment.
    """

    #: A constant which can be used with the condition_type property of a AlarmCondition.
    #: This constant has a value of "FIXED"
    CONDITION_TYPE_FIXED = "FIXED"

    #: A constant which can be used with the condition_type property of a AlarmCondition.
    #: This constant has a value of "AVAILABILITY"
    CONDITION_TYPE_AVAILABILITY = "AVAILABILITY"

    #: A constant which can be used with the status property of a AlarmCondition.
    #: This constant has a value of "NOT_APPLIED"
    STATUS_NOT_APPLIED = "NOT_APPLIED"

    #: A constant which can be used with the status property of a AlarmCondition.
    #: This constant has a value of "APPLIED"
    STATUS_APPLIED = "APPLIED"

    #: A constant which can be used with the status property of a AlarmCondition.
    #: This constant has a value of "PARTIAL_APPLIED"
    STATUS_PARTIAL_APPLIED = "PARTIAL_APPLIED"

    #: A constant which can be used with the status property of a AlarmCondition.
    #: This constant has a value of "ERROR"
    STATUS_ERROR = "ERROR"

    #: A constant which can be used with the lifecycle_state property of a AlarmCondition.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a AlarmCondition.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AlarmCondition.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AlarmCondition.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AlarmCondition.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new AlarmCondition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AlarmCondition.
        :type id: str

        :param monitoring_template_id:
            The value to assign to the monitoring_template_id property of this AlarmCondition.
        :type monitoring_template_id: str

        :param namespace:
            The value to assign to the namespace property of this AlarmCondition.
        :type namespace: str

        :param composite_type:
            The value to assign to the composite_type property of this AlarmCondition.
        :type composite_type: str

        :param resource_type:
            The value to assign to the resource_type property of this AlarmCondition.
        :type resource_type: str

        :param metric_name:
            The value to assign to the metric_name property of this AlarmCondition.
        :type metric_name: str

        :param condition_type:
            The value to assign to the condition_type property of this AlarmCondition.
            Allowed values for this property are: "FIXED", "AVAILABILITY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type condition_type: str

        :param conditions:
            The value to assign to the conditions property of this AlarmCondition.
        :type conditions: list[oci.stack_monitoring.models.Condition]

        :param status:
            The value to assign to the status property of this AlarmCondition.
            Allowed values for this property are: "NOT_APPLIED", "APPLIED", "PARTIAL_APPLIED", "ERROR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AlarmCondition.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this AlarmCondition.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AlarmCondition.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AlarmCondition.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AlarmCondition.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this AlarmCondition.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'monitoring_template_id': 'str',
            'namespace': 'str',
            'composite_type': 'str',
            'resource_type': 'str',
            'metric_name': 'str',
            'condition_type': 'str',
            'conditions': 'list[Condition]',
            'status': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'monitoring_template_id': 'monitoringTemplateId',
            'namespace': 'namespace',
            'composite_type': 'compositeType',
            'resource_type': 'resourceType',
            'metric_name': 'metricName',
            'condition_type': 'conditionType',
            'conditions': 'conditions',
            'status': 'status',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._monitoring_template_id = None
        self._namespace = None
        self._composite_type = None
        self._resource_type = None
        self._metric_name = None
        self._condition_type = None
        self._conditions = None
        self._status = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AlarmCondition.
        The `OCID`__ of the Alarm Condition.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this AlarmCondition.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AlarmCondition.
        The `OCID`__ of the Alarm Condition.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this AlarmCondition.
        :type: str
        """
        self._id = id

    @property
    def monitoring_template_id(self):
        """
        **[Required]** Gets the monitoring_template_id of this AlarmCondition.
        The `OCID`__ of the monitoring template.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The monitoring_template_id of this AlarmCondition.
        :rtype: str
        """
        return self._monitoring_template_id

    @monitoring_template_id.setter
    def monitoring_template_id(self, monitoring_template_id):
        """
        Sets the monitoring_template_id of this AlarmCondition.
        The `OCID`__ of the monitoring template.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param monitoring_template_id: The monitoring_template_id of this AlarmCondition.
        :type: str
        """
        self._monitoring_template_id = monitoring_template_id

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this AlarmCondition.
        The stack monitoring service or application emitting the metric that is evaluated by the alarm.


        :return: The namespace of this AlarmCondition.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this AlarmCondition.
        The stack monitoring service or application emitting the metric that is evaluated by the alarm.


        :param namespace: The namespace of this AlarmCondition.
        :type: str
        """
        self._namespace = namespace

    @property
    def composite_type(self):
        """
        Gets the composite_type of this AlarmCondition.
        The OCID of the composite resource type like EBS/PEOPLE_SOFT.


        :return: The composite_type of this AlarmCondition.
        :rtype: str
        """
        return self._composite_type

    @composite_type.setter
    def composite_type(self, composite_type):
        """
        Sets the composite_type of this AlarmCondition.
        The OCID of the composite resource type like EBS/PEOPLE_SOFT.


        :param composite_type: The composite_type of this AlarmCondition.
        :type: str
        """
        self._composite_type = composite_type

    @property
    def resource_type(self):
        """
        **[Required]** Gets the resource_type of this AlarmCondition.
        The resource type OCID.


        :return: The resource_type of this AlarmCondition.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this AlarmCondition.
        The resource type OCID.


        :param resource_type: The resource_type of this AlarmCondition.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def metric_name(self):
        """
        **[Required]** Gets the metric_name of this AlarmCondition.
        The metric name.


        :return: The metric_name of this AlarmCondition.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """
        Sets the metric_name of this AlarmCondition.
        The metric name.


        :param metric_name: The metric_name of this AlarmCondition.
        :type: str
        """
        self._metric_name = metric_name

    @property
    def condition_type(self):
        """
        **[Required]** Gets the condition_type of this AlarmCondition.
        Type of defined monitoring template.

        Allowed values for this property are: "FIXED", "AVAILABILITY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The condition_type of this AlarmCondition.
        :rtype: str
        """
        return self._condition_type

    @condition_type.setter
    def condition_type(self, condition_type):
        """
        Sets the condition_type of this AlarmCondition.
        Type of defined monitoring template.


        :param condition_type: The condition_type of this AlarmCondition.
        :type: str
        """
        allowed_values = ["FIXED", "AVAILABILITY"]
        if not value_allowed_none_or_none_sentinel(condition_type, allowed_values):
            condition_type = 'UNKNOWN_ENUM_VALUE'
        self._condition_type = condition_type

    @property
    def conditions(self):
        """
        **[Required]** Gets the conditions of this AlarmCondition.
        Monitoring template conditions


        :return: The conditions of this AlarmCondition.
        :rtype: list[oci.stack_monitoring.models.Condition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this AlarmCondition.
        Monitoring template conditions


        :param conditions: The conditions of this AlarmCondition.
        :type: list[oci.stack_monitoring.models.Condition]
        """
        self._conditions = conditions

    @property
    def status(self):
        """
        **[Required]** Gets the status of this AlarmCondition.
        The current status of the monitoring template i.e. whether it is Published or Unpublished

        Allowed values for this property are: "NOT_APPLIED", "APPLIED", "PARTIAL_APPLIED", "ERROR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this AlarmCondition.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AlarmCondition.
        The current status of the monitoring template i.e. whether it is Published or Unpublished


        :param status: The status of this AlarmCondition.
        :type: str
        """
        allowed_values = ["NOT_APPLIED", "APPLIED", "PARTIAL_APPLIED", "ERROR"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AlarmCondition.
        The current lifecycle state of the monitoring template

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AlarmCondition.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AlarmCondition.
        The current lifecycle state of the monitoring template


        :param lifecycle_state: The lifecycle_state of this AlarmCondition.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this AlarmCondition.
        The date and time the alarm condition was created. Format defined by RFC3339.


        :return: The time_created of this AlarmCondition.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AlarmCondition.
        The date and time the alarm condition was created. Format defined by RFC3339.


        :param time_created: The time_created of this AlarmCondition.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this AlarmCondition.
        The date and time the alarm condition was updated. Format defined by RFC3339.


        :return: The time_updated of this AlarmCondition.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AlarmCondition.
        The date and time the alarm condition was updated. Format defined by RFC3339.


        :param time_updated: The time_updated of this AlarmCondition.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AlarmCondition.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this AlarmCondition.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AlarmCondition.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this AlarmCondition.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AlarmCondition.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this AlarmCondition.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AlarmCondition.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this AlarmCondition.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this AlarmCondition.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this AlarmCondition.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this AlarmCondition.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this AlarmCondition.
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
