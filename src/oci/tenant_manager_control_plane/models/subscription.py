# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230401


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Subscription(object):
    """
    Base subscription type, which carries shared properties for any subscription version.
    """

    #: A constant which can be used with the entity_version property of a Subscription.
    #: This constant has a value of "V1"
    ENTITY_VERSION_V1 = "V1"

    #: A constant which can be used with the entity_version property of a Subscription.
    #: This constant has a value of "V2"
    ENTITY_VERSION_V2 = "V2"

    def __init__(self, **kwargs):
        """
        Initializes a new Subscription object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.tenant_manager_control_plane.models.ClassicSubscription`
        * :class:`~oci.tenant_manager_control_plane.models.CloudSubscription`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_version:
            The value to assign to the entity_version property of this Subscription.
            Allowed values for this property are: "V1", "V2", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_version: str

        :param id:
            The value to assign to the id property of this Subscription.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Subscription.
        :type compartment_id: str

        :param service_name:
            The value to assign to the service_name property of this Subscription.
        :type service_name: str

        :param time_created:
            The value to assign to the time_created property of this Subscription.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Subscription.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Subscription.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Subscription.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'entity_version': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'service_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'entity_version': 'entityVersion',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'service_name': 'serviceName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._entity_version = None
        self._id = None
        self._compartment_id = None
        self._service_name = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['entityVersion']

        if type == 'V1':
            return 'ClassicSubscription'

        if type == 'V2':
            return 'CloudSubscription'
        else:
            return 'Subscription'

    @property
    def entity_version(self):
        """
        **[Required]** Gets the entity_version of this Subscription.
        The entity version of the subscription, whether V1 (the legacy schema version), or V2 (the latest 20230401 API version).

        Allowed values for this property are: "V1", "V2", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The entity_version of this Subscription.
        :rtype: str
        """
        return self._entity_version

    @entity_version.setter
    def entity_version(self, entity_version):
        """
        Sets the entity_version of this Subscription.
        The entity version of the subscription, whether V1 (the legacy schema version), or V2 (the latest 20230401 API version).


        :param entity_version: The entity_version of this Subscription.
        :type: str
        """
        allowed_values = ["V1", "V2"]
        if not value_allowed_none_or_none_sentinel(entity_version, allowed_values):
            entity_version = 'UNKNOWN_ENUM_VALUE'
        self._entity_version = entity_version

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Subscription.
        The Oracle ID (`OCID`__) of the subscription.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this Subscription.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Subscription.
        The Oracle ID (`OCID`__) of the subscription.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this Subscription.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Subscription.
        The Oracle ID (`OCID`__) of the owning compartment. Always a tenancy OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Subscription.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Subscription.
        The Oracle ID (`OCID`__) of the owning compartment. Always a tenancy OCID.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Subscription.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def service_name(self):
        """
        **[Required]** Gets the service_name of this Subscription.
        The type of subscription, such as 'UCM', 'SAAS', 'ERP', 'CRM'.


        :return: The service_name of this Subscription.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this Subscription.
        The type of subscription, such as 'UCM', 'SAAS', 'ERP', 'CRM'.


        :param service_name: The service_name of this Subscription.
        :type: str
        """
        self._service_name = service_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Subscription.
        The date and time of creation, as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this Subscription.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Subscription.
        The date and time of creation, as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this Subscription.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this Subscription.
        The date and time of update, as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_updated of this Subscription.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Subscription.
        The date and time of update, as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_updated: The time_updated of this Subscription.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this Subscription.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Subscription.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Subscription.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Subscription.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this Subscription.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Subscription.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Subscription.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Subscription.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
