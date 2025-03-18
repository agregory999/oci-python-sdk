# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NotificationSetting(object):
    """
    Notification resource.
    """

    #: A constant which can be used with the idcs_prevented_operations property of a NotificationSetting.
    #: This constant has a value of "replace"
    IDCS_PREVENTED_OPERATIONS_REPLACE = "replace"

    #: A constant which can be used with the idcs_prevented_operations property of a NotificationSetting.
    #: This constant has a value of "update"
    IDCS_PREVENTED_OPERATIONS_UPDATE = "update"

    #: A constant which can be used with the idcs_prevented_operations property of a NotificationSetting.
    #: This constant has a value of "delete"
    IDCS_PREVENTED_OPERATIONS_DELETE = "delete"

    def __init__(self, **kwargs):
        """
        Initializes a new NotificationSetting object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this NotificationSetting.
        :type id: str

        :param ocid:
            The value to assign to the ocid property of this NotificationSetting.
        :type ocid: str

        :param schemas:
            The value to assign to the schemas property of this NotificationSetting.
        :type schemas: list[str]

        :param meta:
            The value to assign to the meta property of this NotificationSetting.
        :type meta: oci.identity_domains.models.Meta

        :param idcs_created_by:
            The value to assign to the idcs_created_by property of this NotificationSetting.
        :type idcs_created_by: oci.identity_domains.models.IdcsCreatedBy

        :param idcs_last_modified_by:
            The value to assign to the idcs_last_modified_by property of this NotificationSetting.
        :type idcs_last_modified_by: oci.identity_domains.models.IdcsLastModifiedBy

        :param idcs_prevented_operations:
            The value to assign to the idcs_prevented_operations property of this NotificationSetting.
            Allowed values for items in this list are: "replace", "update", "delete", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type idcs_prevented_operations: list[str]

        :param tags:
            The value to assign to the tags property of this NotificationSetting.
        :type tags: list[oci.identity_domains.models.Tags]

        :param delete_in_progress:
            The value to assign to the delete_in_progress property of this NotificationSetting.
        :type delete_in_progress: bool

        :param idcs_last_upgraded_in_release:
            The value to assign to the idcs_last_upgraded_in_release property of this NotificationSetting.
        :type idcs_last_upgraded_in_release: str

        :param domain_ocid:
            The value to assign to the domain_ocid property of this NotificationSetting.
        :type domain_ocid: str

        :param compartment_ocid:
            The value to assign to the compartment_ocid property of this NotificationSetting.
        :type compartment_ocid: str

        :param tenancy_ocid:
            The value to assign to the tenancy_ocid property of this NotificationSetting.
        :type tenancy_ocid: str

        :param external_id:
            The value to assign to the external_id property of this NotificationSetting.
        :type external_id: str

        :param notification_enabled:
            The value to assign to the notification_enabled property of this NotificationSetting.
        :type notification_enabled: bool

        :param test_mode_enabled:
            The value to assign to the test_mode_enabled property of this NotificationSetting.
        :type test_mode_enabled: bool

        :param test_recipients:
            The value to assign to the test_recipients property of this NotificationSetting.
        :type test_recipients: list[str]

        :param send_notifications_to_secondary_email:
            The value to assign to the send_notifications_to_secondary_email property of this NotificationSetting.
        :type send_notifications_to_secondary_email: bool

        :param send_notification_to_old_and_new_primary_emails_when_admin_changes_primary_email:
            The value to assign to the send_notification_to_old_and_new_primary_emails_when_admin_changes_primary_email property of this NotificationSetting.
        :type send_notification_to_old_and_new_primary_emails_when_admin_changes_primary_email: bool

        :param from_email_address:
            The value to assign to the from_email_address property of this NotificationSetting.
        :type from_email_address: oci.identity_domains.models.NotificationSettingsFromEmailAddress

        :param event_settings:
            The value to assign to the event_settings property of this NotificationSetting.
        :type event_settings: list[oci.identity_domains.models.NotificationSettingsEventSettings]

        """
        self.swagger_types = {
            'id': 'str',
            'ocid': 'str',
            'schemas': 'list[str]',
            'meta': 'Meta',
            'idcs_created_by': 'IdcsCreatedBy',
            'idcs_last_modified_by': 'IdcsLastModifiedBy',
            'idcs_prevented_operations': 'list[str]',
            'tags': 'list[Tags]',
            'delete_in_progress': 'bool',
            'idcs_last_upgraded_in_release': 'str',
            'domain_ocid': 'str',
            'compartment_ocid': 'str',
            'tenancy_ocid': 'str',
            'external_id': 'str',
            'notification_enabled': 'bool',
            'test_mode_enabled': 'bool',
            'test_recipients': 'list[str]',
            'send_notifications_to_secondary_email': 'bool',
            'send_notification_to_old_and_new_primary_emails_when_admin_changes_primary_email': 'bool',
            'from_email_address': 'NotificationSettingsFromEmailAddress',
            'event_settings': 'list[NotificationSettingsEventSettings]'
        }
        self.attribute_map = {
            'id': 'id',
            'ocid': 'ocid',
            'schemas': 'schemas',
            'meta': 'meta',
            'idcs_created_by': 'idcsCreatedBy',
            'idcs_last_modified_by': 'idcsLastModifiedBy',
            'idcs_prevented_operations': 'idcsPreventedOperations',
            'tags': 'tags',
            'delete_in_progress': 'deleteInProgress',
            'idcs_last_upgraded_in_release': 'idcsLastUpgradedInRelease',
            'domain_ocid': 'domainOcid',
            'compartment_ocid': 'compartmentOcid',
            'tenancy_ocid': 'tenancyOcid',
            'external_id': 'externalId',
            'notification_enabled': 'notificationEnabled',
            'test_mode_enabled': 'testModeEnabled',
            'test_recipients': 'testRecipients',
            'send_notifications_to_secondary_email': 'sendNotificationsToSecondaryEmail',
            'send_notification_to_old_and_new_primary_emails_when_admin_changes_primary_email': 'sendNotificationToOldAndNewPrimaryEmailsWhenAdminChangesPrimaryEmail',
            'from_email_address': 'fromEmailAddress',
            'event_settings': 'eventSettings'
        }
        self._id = None
        self._ocid = None
        self._schemas = None
        self._meta = None
        self._idcs_created_by = None
        self._idcs_last_modified_by = None
        self._idcs_prevented_operations = None
        self._tags = None
        self._delete_in_progress = None
        self._idcs_last_upgraded_in_release = None
        self._domain_ocid = None
        self._compartment_ocid = None
        self._tenancy_ocid = None
        self._external_id = None
        self._notification_enabled = None
        self._test_mode_enabled = None
        self._test_recipients = None
        self._send_notifications_to_secondary_email = None
        self._send_notification_to_old_and_new_primary_emails_when_admin_changes_primary_email = None
        self._from_email_address = None
        self._event_settings = None

    @property
    def id(self):
        """
        Gets the id of this NotificationSetting.
        Unique identifier for the SCIM Resource as defined by the Service Provider. Each representation of the Resource MUST include a non-empty id value. This identifier MUST be unique across the Service Provider's entire set of Resources. It MUST be a stable, non-reassignable identifier that does not change when the same Resource is returned in subsequent requests. The value of the id attribute is always issued by the Service Provider and MUST never be specified by the Service Consumer. bulkId: is a reserved keyword and MUST NOT be used in the unique identifier.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: global


        :return: The id of this NotificationSetting.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this NotificationSetting.
        Unique identifier for the SCIM Resource as defined by the Service Provider. Each representation of the Resource MUST include a non-empty id value. This identifier MUST be unique across the Service Provider's entire set of Resources. It MUST be a stable, non-reassignable identifier that does not change when the same Resource is returned in subsequent requests. The value of the id attribute is always issued by the Service Provider and MUST never be specified by the Service Consumer. bulkId: is a reserved keyword and MUST NOT be used in the unique identifier.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: global


        :param id: The id of this NotificationSetting.
        :type: str
        """
        self._id = id

    @property
    def ocid(self):
        """
        Gets the ocid of this NotificationSetting.
        Unique OCI identifier for the SCIM Resource.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: string
         - uniqueness: global


        :return: The ocid of this NotificationSetting.
        :rtype: str
        """
        return self._ocid

    @ocid.setter
    def ocid(self, ocid):
        """
        Sets the ocid of this NotificationSetting.
        Unique OCI identifier for the SCIM Resource.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: string
         - uniqueness: global


        :param ocid: The ocid of this NotificationSetting.
        :type: str
        """
        self._ocid = ocid

    @property
    def schemas(self):
        """
        **[Required]** Gets the schemas of this NotificationSetting.
        REQUIRED. The schemas attribute is an array of Strings which allows introspection of the supported schema version for a SCIM representation as well any schema extensions supported by that representation. Each String value must be a unique URI. This specification defines URIs for User, Group, and a standard \\\"enterprise\\\" extension. All representations of SCIM schema MUST include a non-zero value array with value(s) of the URIs supported by that representation. Duplicate values MUST NOT be included. Value order is not specified and MUST not impact behavior.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: true
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The schemas of this NotificationSetting.
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """
        Sets the schemas of this NotificationSetting.
        REQUIRED. The schemas attribute is an array of Strings which allows introspection of the supported schema version for a SCIM representation as well any schema extensions supported by that representation. Each String value must be a unique URI. This specification defines URIs for User, Group, and a standard \\\"enterprise\\\" extension. All representations of SCIM schema MUST include a non-zero value array with value(s) of the URIs supported by that representation. Duplicate values MUST NOT be included. Value order is not specified and MUST not impact behavior.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: true
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param schemas: The schemas of this NotificationSetting.
        :type: list[str]
        """
        self._schemas = schemas

    @property
    def meta(self):
        """
        Gets the meta of this NotificationSetting.

        :return: The meta of this NotificationSetting.
        :rtype: oci.identity_domains.models.Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """
        Sets the meta of this NotificationSetting.

        :param meta: The meta of this NotificationSetting.
        :type: oci.identity_domains.models.Meta
        """
        self._meta = meta

    @property
    def idcs_created_by(self):
        """
        Gets the idcs_created_by of this NotificationSetting.

        :return: The idcs_created_by of this NotificationSetting.
        :rtype: oci.identity_domains.models.IdcsCreatedBy
        """
        return self._idcs_created_by

    @idcs_created_by.setter
    def idcs_created_by(self, idcs_created_by):
        """
        Sets the idcs_created_by of this NotificationSetting.

        :param idcs_created_by: The idcs_created_by of this NotificationSetting.
        :type: oci.identity_domains.models.IdcsCreatedBy
        """
        self._idcs_created_by = idcs_created_by

    @property
    def idcs_last_modified_by(self):
        """
        Gets the idcs_last_modified_by of this NotificationSetting.

        :return: The idcs_last_modified_by of this NotificationSetting.
        :rtype: oci.identity_domains.models.IdcsLastModifiedBy
        """
        return self._idcs_last_modified_by

    @idcs_last_modified_by.setter
    def idcs_last_modified_by(self, idcs_last_modified_by):
        """
        Sets the idcs_last_modified_by of this NotificationSetting.

        :param idcs_last_modified_by: The idcs_last_modified_by of this NotificationSetting.
        :type: oci.identity_domains.models.IdcsLastModifiedBy
        """
        self._idcs_last_modified_by = idcs_last_modified_by

    @property
    def idcs_prevented_operations(self):
        """
        Gets the idcs_prevented_operations of this NotificationSetting.
        Each value of this attribute specifies an operation that only an internal client may perform on this particular resource.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: true
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none

        Allowed values for items in this list are: "replace", "update", "delete", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The idcs_prevented_operations of this NotificationSetting.
        :rtype: list[str]
        """
        return self._idcs_prevented_operations

    @idcs_prevented_operations.setter
    def idcs_prevented_operations(self, idcs_prevented_operations):
        """
        Sets the idcs_prevented_operations of this NotificationSetting.
        Each value of this attribute specifies an operation that only an internal client may perform on this particular resource.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: true
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param idcs_prevented_operations: The idcs_prevented_operations of this NotificationSetting.
        :type: list[str]
        """
        allowed_values = ["replace", "update", "delete"]
        if idcs_prevented_operations:
            idcs_prevented_operations[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in idcs_prevented_operations]
        self._idcs_prevented_operations = idcs_prevented_operations

    @property
    def tags(self):
        """
        Gets the tags of this NotificationSetting.
        A list of tags on this resource.

        **SCIM++ Properties:**
         - idcsCompositeKey: [key, value]
         - idcsSearchable: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: request
         - type: complex
         - uniqueness: none


        :return: The tags of this NotificationSetting.
        :rtype: list[oci.identity_domains.models.Tags]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this NotificationSetting.
        A list of tags on this resource.

        **SCIM++ Properties:**
         - idcsCompositeKey: [key, value]
         - idcsSearchable: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: request
         - type: complex
         - uniqueness: none


        :param tags: The tags of this NotificationSetting.
        :type: list[oci.identity_domains.models.Tags]
        """
        self._tags = tags

    @property
    def delete_in_progress(self):
        """
        Gets the delete_in_progress of this NotificationSetting.
        A boolean flag indicating this resource in the process of being deleted. Usually set to true when synchronous deletion of the resource would take too long.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The delete_in_progress of this NotificationSetting.
        :rtype: bool
        """
        return self._delete_in_progress

    @delete_in_progress.setter
    def delete_in_progress(self, delete_in_progress):
        """
        Sets the delete_in_progress of this NotificationSetting.
        A boolean flag indicating this resource in the process of being deleted. Usually set to true when synchronous deletion of the resource would take too long.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param delete_in_progress: The delete_in_progress of this NotificationSetting.
        :type: bool
        """
        self._delete_in_progress = delete_in_progress

    @property
    def idcs_last_upgraded_in_release(self):
        """
        Gets the idcs_last_upgraded_in_release of this NotificationSetting.
        The release number when the resource was upgraded.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The idcs_last_upgraded_in_release of this NotificationSetting.
        :rtype: str
        """
        return self._idcs_last_upgraded_in_release

    @idcs_last_upgraded_in_release.setter
    def idcs_last_upgraded_in_release(self, idcs_last_upgraded_in_release):
        """
        Sets the idcs_last_upgraded_in_release of this NotificationSetting.
        The release number when the resource was upgraded.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param idcs_last_upgraded_in_release: The idcs_last_upgraded_in_release of this NotificationSetting.
        :type: str
        """
        self._idcs_last_upgraded_in_release = idcs_last_upgraded_in_release

    @property
    def domain_ocid(self):
        """
        Gets the domain_ocid of this NotificationSetting.
        OCI Domain Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The domain_ocid of this NotificationSetting.
        :rtype: str
        """
        return self._domain_ocid

    @domain_ocid.setter
    def domain_ocid(self, domain_ocid):
        """
        Sets the domain_ocid of this NotificationSetting.
        OCI Domain Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param domain_ocid: The domain_ocid of this NotificationSetting.
        :type: str
        """
        self._domain_ocid = domain_ocid

    @property
    def compartment_ocid(self):
        """
        Gets the compartment_ocid of this NotificationSetting.
        OCI Compartment Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The compartment_ocid of this NotificationSetting.
        :rtype: str
        """
        return self._compartment_ocid

    @compartment_ocid.setter
    def compartment_ocid(self, compartment_ocid):
        """
        Sets the compartment_ocid of this NotificationSetting.
        OCI Compartment Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param compartment_ocid: The compartment_ocid of this NotificationSetting.
        :type: str
        """
        self._compartment_ocid = compartment_ocid

    @property
    def tenancy_ocid(self):
        """
        Gets the tenancy_ocid of this NotificationSetting.
        OCI Tenant Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The tenancy_ocid of this NotificationSetting.
        :rtype: str
        """
        return self._tenancy_ocid

    @tenancy_ocid.setter
    def tenancy_ocid(self, tenancy_ocid):
        """
        Sets the tenancy_ocid of this NotificationSetting.
        OCI Tenant Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param tenancy_ocid: The tenancy_ocid of this NotificationSetting.
        :type: str
        """
        self._tenancy_ocid = tenancy_ocid

    @property
    def external_id(self):
        """
        Gets the external_id of this NotificationSetting.
        An identifier for the Resource as defined by the Service Consumer. The externalId may simplify identification of the Resource between Service Consumer and Service Provider by allowing the Consumer to refer to the Resource with its own identifier, obviating the need to store a local mapping between the local identifier of the Resource and the identifier used by the Service Provider. Each Resource MAY include a non-empty externalId value. The value of the externalId attribute is always issued by the Service Consumer and can never be specified by the Service Provider. The Service Provider MUST always interpret the externalId as scoped to the Service Consumer's tenant.

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The external_id of this NotificationSetting.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this NotificationSetting.
        An identifier for the Resource as defined by the Service Consumer. The externalId may simplify identification of the Resource between Service Consumer and Service Provider by allowing the Consumer to refer to the Resource with its own identifier, obviating the need to store a local mapping between the local identifier of the Resource and the identifier used by the Service Provider. Each Resource MAY include a non-empty externalId value. The value of the externalId attribute is always issued by the Service Consumer and can never be specified by the Service Provider. The Service Provider MUST always interpret the externalId as scoped to the Service Consumer's tenant.

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param external_id: The external_id of this NotificationSetting.
        :type: str
        """
        self._external_id = external_id

    @property
    def notification_enabled(self):
        """
        **[Required]** Gets the notification_enabled of this NotificationSetting.
        Tenant level settings for the notification service

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The notification_enabled of this NotificationSetting.
        :rtype: bool
        """
        return self._notification_enabled

    @notification_enabled.setter
    def notification_enabled(self, notification_enabled):
        """
        Sets the notification_enabled of this NotificationSetting.
        Tenant level settings for the notification service

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: boolean
         - uniqueness: none


        :param notification_enabled: The notification_enabled of this NotificationSetting.
        :type: bool
        """
        self._notification_enabled = notification_enabled

    @property
    def test_mode_enabled(self):
        """
        Gets the test_mode_enabled of this NotificationSetting.
        Specify if the notification service is in test mode

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The test_mode_enabled of this NotificationSetting.
        :rtype: bool
        """
        return self._test_mode_enabled

    @test_mode_enabled.setter
    def test_mode_enabled(self, test_mode_enabled):
        """
        Sets the test_mode_enabled of this NotificationSetting.
        Specify if the notification service is in test mode

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param test_mode_enabled: The test_mode_enabled of this NotificationSetting.
        :type: bool
        """
        self._test_mode_enabled = test_mode_enabled

    @property
    def test_recipients(self):
        """
        Gets the test_recipients of this NotificationSetting.
        List of the test recipient email addresses

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The test_recipients of this NotificationSetting.
        :rtype: list[str]
        """
        return self._test_recipients

    @test_recipients.setter
    def test_recipients(self, test_recipients):
        """
        Sets the test_recipients of this NotificationSetting.
        List of the test recipient email addresses

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param test_recipients: The test_recipients of this NotificationSetting.
        :type: list[str]
        """
        self._test_recipients = test_recipients

    @property
    def send_notifications_to_secondary_email(self):
        """
        Gets the send_notifications_to_secondary_email of this NotificationSetting.
        Indicates whether to allow notifications on a secondary email.

        **Deprecated Since: 19.2.1**

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The send_notifications_to_secondary_email of this NotificationSetting.
        :rtype: bool
        """
        return self._send_notifications_to_secondary_email

    @send_notifications_to_secondary_email.setter
    def send_notifications_to_secondary_email(self, send_notifications_to_secondary_email):
        """
        Sets the send_notifications_to_secondary_email of this NotificationSetting.
        Indicates whether to allow notifications on a secondary email.

        **Deprecated Since: 19.2.1**

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param send_notifications_to_secondary_email: The send_notifications_to_secondary_email of this NotificationSetting.
        :type: bool
        """
        self._send_notifications_to_secondary_email = send_notifications_to_secondary_email

    @property
    def send_notification_to_old_and_new_primary_emails_when_admin_changes_primary_email(self):
        """
        Gets the send_notification_to_old_and_new_primary_emails_when_admin_changes_primary_email of this NotificationSetting.
        If true and admin changed user's primary email, send user's profile changed email to old and new primary email address.

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The send_notification_to_old_and_new_primary_emails_when_admin_changes_primary_email of this NotificationSetting.
        :rtype: bool
        """
        return self._send_notification_to_old_and_new_primary_emails_when_admin_changes_primary_email

    @send_notification_to_old_and_new_primary_emails_when_admin_changes_primary_email.setter
    def send_notification_to_old_and_new_primary_emails_when_admin_changes_primary_email(self, send_notification_to_old_and_new_primary_emails_when_admin_changes_primary_email):
        """
        Sets the send_notification_to_old_and_new_primary_emails_when_admin_changes_primary_email of this NotificationSetting.
        If true and admin changed user's primary email, send user's profile changed email to old and new primary email address.

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param send_notification_to_old_and_new_primary_emails_when_admin_changes_primary_email: The send_notification_to_old_and_new_primary_emails_when_admin_changes_primary_email of this NotificationSetting.
        :type: bool
        """
        self._send_notification_to_old_and_new_primary_emails_when_admin_changes_primary_email = send_notification_to_old_and_new_primary_emails_when_admin_changes_primary_email

    @property
    def from_email_address(self):
        """
        **[Required]** Gets the from_email_address of this NotificationSetting.

        :return: The from_email_address of this NotificationSetting.
        :rtype: oci.identity_domains.models.NotificationSettingsFromEmailAddress
        """
        return self._from_email_address

    @from_email_address.setter
    def from_email_address(self, from_email_address):
        """
        Sets the from_email_address of this NotificationSetting.

        :param from_email_address: The from_email_address of this NotificationSetting.
        :type: oci.identity_domains.models.NotificationSettingsFromEmailAddress
        """
        self._from_email_address = from_email_address

    @property
    def event_settings(self):
        """
        **[Required]** Gets the event_settings of this NotificationSetting.
        Event settings

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCompositeKey: [eventId]
         - idcsSearchable: false
         - multiValued: true
         - mutability: readWrite
         - required: true
         - returned: default
         - type: complex
         - uniqueness: none


        :return: The event_settings of this NotificationSetting.
        :rtype: list[oci.identity_domains.models.NotificationSettingsEventSettings]
        """
        return self._event_settings

    @event_settings.setter
    def event_settings(self, event_settings):
        """
        Sets the event_settings of this NotificationSetting.
        Event settings

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCompositeKey: [eventId]
         - idcsSearchable: false
         - multiValued: true
         - mutability: readWrite
         - required: true
         - returned: default
         - type: complex
         - uniqueness: none


        :param event_settings: The event_settings of this NotificationSetting.
        :type: list[oci.identity_domains.models.NotificationSettingsEventSettings]
        """
        self._event_settings = event_settings

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
