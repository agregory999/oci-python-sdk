# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230801


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DelegationSubscriptionSummary(object):
    """
    Summary of the Delegation Subscription.
    """

    #: A constant which can be used with the subscribed_service_type property of a DelegationSubscriptionSummary.
    #: This constant has a value of "TROUBLESHOOTING"
    SUBSCRIBED_SERVICE_TYPE_TROUBLESHOOTING = "TROUBLESHOOTING"

    #: A constant which can be used with the subscribed_service_type property of a DelegationSubscriptionSummary.
    #: This constant has a value of "ASSISTED_PATCHING"
    SUBSCRIBED_SERVICE_TYPE_ASSISTED_PATCHING = "ASSISTED_PATCHING"

    def __init__(self, **kwargs):
        """
        Initializes a new DelegationSubscriptionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DelegationSubscriptionSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DelegationSubscriptionSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this DelegationSubscriptionSummary.
        :type display_name: str

        :param service_provider_id:
            The value to assign to the service_provider_id property of this DelegationSubscriptionSummary.
        :type service_provider_id: str

        :param subscribed_service_type:
            The value to assign to the subscribed_service_type property of this DelegationSubscriptionSummary.
            Allowed values for this property are: "TROUBLESHOOTING", "ASSISTED_PATCHING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type subscribed_service_type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DelegationSubscriptionSummary.
        :type lifecycle_state: str

        :param lifecycle_state_details:
            The value to assign to the lifecycle_state_details property of this DelegationSubscriptionSummary.
        :type lifecycle_state_details: str

        :param time_created:
            The value to assign to the time_created property of this DelegationSubscriptionSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DelegationSubscriptionSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DelegationSubscriptionSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DelegationSubscriptionSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DelegationSubscriptionSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'service_provider_id': 'str',
            'subscribed_service_type': 'str',
            'lifecycle_state': 'str',
            'lifecycle_state_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'service_provider_id': 'serviceProviderId',
            'subscribed_service_type': 'subscribedServiceType',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_state_details': 'lifecycleStateDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._service_provider_id = None
        self._subscribed_service_type = None
        self._lifecycle_state = None
        self._lifecycle_state_details = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DelegationSubscriptionSummary.
        Unique identifier for the Delegation Subscription.


        :return: The id of this DelegationSubscriptionSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DelegationSubscriptionSummary.
        Unique identifier for the Delegation Subscription.


        :param id: The id of this DelegationSubscriptionSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this DelegationSubscriptionSummary.
        The OCID of the compartment that contains the Delegation Subscription.


        :return: The compartment_id of this DelegationSubscriptionSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DelegationSubscriptionSummary.
        The OCID of the compartment that contains the Delegation Subscription.


        :param compartment_id: The compartment_id of this DelegationSubscriptionSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this DelegationSubscriptionSummary.
        Display name


        :return: The display_name of this DelegationSubscriptionSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DelegationSubscriptionSummary.
        Display name


        :param display_name: The display_name of this DelegationSubscriptionSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def service_provider_id(self):
        """
        **[Required]** Gets the service_provider_id of this DelegationSubscriptionSummary.
        Unique identifier of the Service Provider.


        :return: The service_provider_id of this DelegationSubscriptionSummary.
        :rtype: str
        """
        return self._service_provider_id

    @service_provider_id.setter
    def service_provider_id(self, service_provider_id):
        """
        Sets the service_provider_id of this DelegationSubscriptionSummary.
        Unique identifier of the Service Provider.


        :param service_provider_id: The service_provider_id of this DelegationSubscriptionSummary.
        :type: str
        """
        self._service_provider_id = service_provider_id

    @property
    def subscribed_service_type(self):
        """
        **[Required]** Gets the subscribed_service_type of this DelegationSubscriptionSummary.
        Subscribed Service Provider Service Type.

        Allowed values for this property are: "TROUBLESHOOTING", "ASSISTED_PATCHING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The subscribed_service_type of this DelegationSubscriptionSummary.
        :rtype: str
        """
        return self._subscribed_service_type

    @subscribed_service_type.setter
    def subscribed_service_type(self, subscribed_service_type):
        """
        Sets the subscribed_service_type of this DelegationSubscriptionSummary.
        Subscribed Service Provider Service Type.


        :param subscribed_service_type: The subscribed_service_type of this DelegationSubscriptionSummary.
        :type: str
        """
        allowed_values = ["TROUBLESHOOTING", "ASSISTED_PATCHING"]
        if not value_allowed_none_or_none_sentinel(subscribed_service_type, allowed_values):
            subscribed_service_type = 'UNKNOWN_ENUM_VALUE'
        self._subscribed_service_type = subscribed_service_type

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DelegationSubscriptionSummary.
        The current lifecycle state of the Service Provider.


        :return: The lifecycle_state of this DelegationSubscriptionSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DelegationSubscriptionSummary.
        The current lifecycle state of the Service Provider.


        :param lifecycle_state: The lifecycle_state of this DelegationSubscriptionSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_state_details(self):
        """
        Gets the lifecycle_state_details of this DelegationSubscriptionSummary.
        Description of the current lifecycle state in more detail.


        :return: The lifecycle_state_details of this DelegationSubscriptionSummary.
        :rtype: str
        """
        return self._lifecycle_state_details

    @lifecycle_state_details.setter
    def lifecycle_state_details(self, lifecycle_state_details):
        """
        Sets the lifecycle_state_details of this DelegationSubscriptionSummary.
        Description of the current lifecycle state in more detail.


        :param lifecycle_state_details: The lifecycle_state_details of this DelegationSubscriptionSummary.
        :type: str
        """
        self._lifecycle_state_details = lifecycle_state_details

    @property
    def time_created(self):
        """
        Gets the time_created of this DelegationSubscriptionSummary.
        Time when the Service Provider was created expressed in `RFC 3339`__ timestamp format, e.g. '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this DelegationSubscriptionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DelegationSubscriptionSummary.
        Time when the Service Provider was created expressed in `RFC 3339`__ timestamp format, e.g. '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this DelegationSubscriptionSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this DelegationSubscriptionSummary.
        Time when the Service Provider was last modified expressed in `RFC 3339`__ timestamp format, e.g. '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this DelegationSubscriptionSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DelegationSubscriptionSummary.
        Time when the Service Provider was last modified expressed in `RFC 3339`__ timestamp format, e.g. '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this DelegationSubscriptionSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DelegationSubscriptionSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this DelegationSubscriptionSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DelegationSubscriptionSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this DelegationSubscriptionSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DelegationSubscriptionSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this DelegationSubscriptionSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DelegationSubscriptionSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this DelegationSubscriptionSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DelegationSubscriptionSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this DelegationSubscriptionSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DelegationSubscriptionSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this DelegationSubscriptionSummary.
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
