# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AccountMgmtInfoApp(object):
    """
    Application on which the account is based

    **SCIM++ Properties:**
    - idcsSearchable: true
    - multiValued: false
    - mutability: immutable
    - required: true
    - returned: default
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AccountMgmtInfoApp object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this AccountMgmtInfoApp.
        :type value: str

        :param ref:
            The value to assign to the ref property of this AccountMgmtInfoApp.
        :type ref: str

        :param display:
            The value to assign to the display property of this AccountMgmtInfoApp.
        :type display: str

        :param description:
            The value to assign to the description property of this AccountMgmtInfoApp.
        :type description: str

        :param is_login_target:
            The value to assign to the is_login_target property of this AccountMgmtInfoApp.
        :type is_login_target: bool

        :param show_in_my_apps:
            The value to assign to the show_in_my_apps property of this AccountMgmtInfoApp.
        :type show_in_my_apps: bool

        :param active:
            The value to assign to the active property of this AccountMgmtInfoApp.
        :type active: bool

        :param login_mechanism:
            The value to assign to the login_mechanism property of this AccountMgmtInfoApp.
        :type login_mechanism: str

        :param app_icon:
            The value to assign to the app_icon property of this AccountMgmtInfoApp.
        :type app_icon: str

        :param app_thumbnail:
            The value to assign to the app_thumbnail property of this AccountMgmtInfoApp.
        :type app_thumbnail: str

        :param is_unmanaged_app:
            The value to assign to the is_unmanaged_app property of this AccountMgmtInfoApp.
        :type is_unmanaged_app: bool

        :param is_managed_app:
            The value to assign to the is_managed_app property of this AccountMgmtInfoApp.
        :type is_managed_app: bool

        :param is_alias_app:
            The value to assign to the is_alias_app property of this AccountMgmtInfoApp.
        :type is_alias_app: bool

        :param is_opc_service:
            The value to assign to the is_opc_service property of this AccountMgmtInfoApp.
        :type is_opc_service: bool

        :param service_type_urn:
            The value to assign to the service_type_urn property of this AccountMgmtInfoApp.
        :type service_type_urn: str

        :param is_authoritative:
            The value to assign to the is_authoritative property of this AccountMgmtInfoApp.
        :type is_authoritative: bool

        :param meter_as_opc_service:
            The value to assign to the meter_as_opc_service property of this AccountMgmtInfoApp.
        :type meter_as_opc_service: bool

        :param is_o_auth_resource:
            The value to assign to the is_o_auth_resource property of this AccountMgmtInfoApp.
        :type is_o_auth_resource: bool

        :param audience:
            The value to assign to the audience property of this AccountMgmtInfoApp.
        :type audience: str

        """
        self.swagger_types = {
            'value': 'str',
            'ref': 'str',
            'display': 'str',
            'description': 'str',
            'is_login_target': 'bool',
            'show_in_my_apps': 'bool',
            'active': 'bool',
            'login_mechanism': 'str',
            'app_icon': 'str',
            'app_thumbnail': 'str',
            'is_unmanaged_app': 'bool',
            'is_managed_app': 'bool',
            'is_alias_app': 'bool',
            'is_opc_service': 'bool',
            'service_type_urn': 'str',
            'is_authoritative': 'bool',
            'meter_as_opc_service': 'bool',
            'is_o_auth_resource': 'bool',
            'audience': 'str'
        }
        self.attribute_map = {
            'value': 'value',
            'ref': '$ref',
            'display': 'display',
            'description': 'description',
            'is_login_target': 'isLoginTarget',
            'show_in_my_apps': 'showInMyApps',
            'active': 'active',
            'login_mechanism': 'loginMechanism',
            'app_icon': 'appIcon',
            'app_thumbnail': 'appThumbnail',
            'is_unmanaged_app': 'isUnmanagedApp',
            'is_managed_app': 'isManagedApp',
            'is_alias_app': 'isAliasApp',
            'is_opc_service': 'isOPCService',
            'service_type_urn': 'serviceTypeURN',
            'is_authoritative': 'isAuthoritative',
            'meter_as_opc_service': 'meterAsOPCService',
            'is_o_auth_resource': 'isOAuthResource',
            'audience': 'audience'
        }
        self._value = None
        self._ref = None
        self._display = None
        self._description = None
        self._is_login_target = None
        self._show_in_my_apps = None
        self._active = None
        self._login_mechanism = None
        self._app_icon = None
        self._app_thumbnail = None
        self._is_unmanaged_app = None
        self._is_managed_app = None
        self._is_alias_app = None
        self._is_opc_service = None
        self._service_type_urn = None
        self._is_authoritative = None
        self._meter_as_opc_service = None
        self._is_o_auth_resource = None
        self._audience = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this AccountMgmtInfoApp.
        Application identifier

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :return: The value of this AccountMgmtInfoApp.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this AccountMgmtInfoApp.
        Application identifier

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :param value: The value of this AccountMgmtInfoApp.
        :type: str
        """
        self._value = value

    @property
    def ref(self):
        """
        Gets the ref of this AccountMgmtInfoApp.
        Application URI

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this AccountMgmtInfoApp.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this AccountMgmtInfoApp.
        Application URI

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this AccountMgmtInfoApp.
        :type: str
        """
        self._ref = ref

    @property
    def display(self):
        """
        Gets the display of this AccountMgmtInfoApp.
        Application display name

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The display of this AccountMgmtInfoApp.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this AccountMgmtInfoApp.
        Application display name

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param display: The display of this AccountMgmtInfoApp.
        :type: str
        """
        self._display = display

    @property
    def description(self):
        """
        Gets the description of this AccountMgmtInfoApp.
        Application description

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The description of this AccountMgmtInfoApp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AccountMgmtInfoApp.
        Application description

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param description: The description of this AccountMgmtInfoApp.
        :type: str
        """
        self._description = description

    @property
    def is_login_target(self):
        """
        Gets the is_login_target of this AccountMgmtInfoApp.
        If true, this App allows runtime services to log end users in to this App automatically

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :return: The is_login_target of this AccountMgmtInfoApp.
        :rtype: bool
        """
        return self._is_login_target

    @is_login_target.setter
    def is_login_target(self, is_login_target):
        """
        Sets the is_login_target of this AccountMgmtInfoApp.
        If true, this App allows runtime services to log end users in to this App automatically

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :param is_login_target: The is_login_target of this AccountMgmtInfoApp.
        :type: bool
        """
        self._is_login_target = is_login_target

    @property
    def show_in_my_apps(self):
        """
        Gets the show_in_my_apps of this AccountMgmtInfoApp.
        If true, this App will be displayed in the MyApps page of each end-user who has access to the App.

        **Added In:** 18.1.2

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :return: The show_in_my_apps of this AccountMgmtInfoApp.
        :rtype: bool
        """
        return self._show_in_my_apps

    @show_in_my_apps.setter
    def show_in_my_apps(self, show_in_my_apps):
        """
        Sets the show_in_my_apps of this AccountMgmtInfoApp.
        If true, this App will be displayed in the MyApps page of each end-user who has access to the App.

        **Added In:** 18.1.2

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :param show_in_my_apps: The show_in_my_apps of this AccountMgmtInfoApp.
        :type: bool
        """
        self._show_in_my_apps = show_in_my_apps

    @property
    def active(self):
        """
        Gets the active of this AccountMgmtInfoApp.
        If true, this App is able to participate in runtime services, such as automatic-login, OAuth, and SAML. If false, all runtime services are disabled for this App and only administrative operations can be performed.

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :return: The active of this AccountMgmtInfoApp.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this AccountMgmtInfoApp.
        If true, this App is able to participate in runtime services, such as automatic-login, OAuth, and SAML. If false, all runtime services are disabled for this App and only administrative operations can be performed.

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :param active: The active of this AccountMgmtInfoApp.
        :type: bool
        """
        self._active = active

    @property
    def login_mechanism(self):
        """
        Gets the login_mechanism of this AccountMgmtInfoApp.
        The protocol that runtime services will use to log end users in to this App automatically. If 'OIDC', then runtime services use the OpenID Connect protocol. If 'SAML', then runtime services use the Security Assertion Markup Language protocol.

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The login_mechanism of this AccountMgmtInfoApp.
        :rtype: str
        """
        return self._login_mechanism

    @login_mechanism.setter
    def login_mechanism(self, login_mechanism):
        """
        Sets the login_mechanism of this AccountMgmtInfoApp.
        The protocol that runtime services will use to log end users in to this App automatically. If 'OIDC', then runtime services use the OpenID Connect protocol. If 'SAML', then runtime services use the Security Assertion Markup Language protocol.

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param login_mechanism: The login_mechanism of this AccountMgmtInfoApp.
        :type: str
        """
        self._login_mechanism = login_mechanism

    @property
    def app_icon(self):
        """
        Gets the app_icon of this AccountMgmtInfoApp.
        Application icon.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The app_icon of this AccountMgmtInfoApp.
        :rtype: str
        """
        return self._app_icon

    @app_icon.setter
    def app_icon(self, app_icon):
        """
        Sets the app_icon of this AccountMgmtInfoApp.
        Application icon.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param app_icon: The app_icon of this AccountMgmtInfoApp.
        :type: str
        """
        self._app_icon = app_icon

    @property
    def app_thumbnail(self):
        """
        Gets the app_thumbnail of this AccountMgmtInfoApp.
        Application thumbnail.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The app_thumbnail of this AccountMgmtInfoApp.
        :rtype: str
        """
        return self._app_thumbnail

    @app_thumbnail.setter
    def app_thumbnail(self, app_thumbnail):
        """
        Sets the app_thumbnail of this AccountMgmtInfoApp.
        Application thumbnail.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param app_thumbnail: The app_thumbnail of this AccountMgmtInfoApp.
        :type: str
        """
        self._app_thumbnail = app_thumbnail

    @property
    def is_unmanaged_app(self):
        """
        Gets the is_unmanaged_app of this AccountMgmtInfoApp.
        If true, indicates that this application accepts an Oracle Identity Cloud Service user as a login-identity (does not require an account) and relies on authorization of the user's memberships in AppRoles

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :return: The is_unmanaged_app of this AccountMgmtInfoApp.
        :rtype: bool
        """
        return self._is_unmanaged_app

    @is_unmanaged_app.setter
    def is_unmanaged_app(self, is_unmanaged_app):
        """
        Sets the is_unmanaged_app of this AccountMgmtInfoApp.
        If true, indicates that this application accepts an Oracle Identity Cloud Service user as a login-identity (does not require an account) and relies on authorization of the user's memberships in AppRoles

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :param is_unmanaged_app: The is_unmanaged_app of this AccountMgmtInfoApp.
        :type: bool
        """
        self._is_unmanaged_app = is_unmanaged_app

    @property
    def is_managed_app(self):
        """
        Gets the is_managed_app of this AccountMgmtInfoApp.
        If true, indicates that access to this App requires an account. That is, in order to log in to the App, a User must use an application-specific identity that is maintained in the remote identity-repository of that App.

        **Added In:** 17.4.6

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :return: The is_managed_app of this AccountMgmtInfoApp.
        :rtype: bool
        """
        return self._is_managed_app

    @is_managed_app.setter
    def is_managed_app(self, is_managed_app):
        """
        Sets the is_managed_app of this AccountMgmtInfoApp.
        If true, indicates that access to this App requires an account. That is, in order to log in to the App, a User must use an application-specific identity that is maintained in the remote identity-repository of that App.

        **Added In:** 17.4.6

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :param is_managed_app: The is_managed_app of this AccountMgmtInfoApp.
        :type: bool
        """
        self._is_managed_app = is_managed_app

    @property
    def is_alias_app(self):
        """
        Gets the is_alias_app of this AccountMgmtInfoApp.
        If true, this App is an AliasApp and it cannot be granted to an end user directly

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :return: The is_alias_app of this AccountMgmtInfoApp.
        :rtype: bool
        """
        return self._is_alias_app

    @is_alias_app.setter
    def is_alias_app(self, is_alias_app):
        """
        Sets the is_alias_app of this AccountMgmtInfoApp.
        If true, this App is an AliasApp and it cannot be granted to an end user directly

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :param is_alias_app: The is_alias_app of this AccountMgmtInfoApp.
        :type: bool
        """
        self._is_alias_app = is_alias_app

    @property
    def is_opc_service(self):
        """
        Gets the is_opc_service of this AccountMgmtInfoApp.
        If true, this application is an Oracle Public Cloud service-instance.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :return: The is_opc_service of this AccountMgmtInfoApp.
        :rtype: bool
        """
        return self._is_opc_service

    @is_opc_service.setter
    def is_opc_service(self, is_opc_service):
        """
        Sets the is_opc_service of this AccountMgmtInfoApp.
        If true, this application is an Oracle Public Cloud service-instance.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :param is_opc_service: The is_opc_service of this AccountMgmtInfoApp.
        :type: bool
        """
        self._is_opc_service = is_opc_service

    @property
    def service_type_urn(self):
        """
        Gets the service_type_urn of this AccountMgmtInfoApp.
        This Uniform Resource Name (URN) value identifies the type of Oracle Public Cloud service of which this app is an instance.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The service_type_urn of this AccountMgmtInfoApp.
        :rtype: str
        """
        return self._service_type_urn

    @service_type_urn.setter
    def service_type_urn(self, service_type_urn):
        """
        Sets the service_type_urn of this AccountMgmtInfoApp.
        This Uniform Resource Name (URN) value identifies the type of Oracle Public Cloud service of which this app is an instance.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param service_type_urn: The service_type_urn of this AccountMgmtInfoApp.
        :type: str
        """
        self._service_type_urn = service_type_urn

    @property
    def is_authoritative(self):
        """
        Gets the is_authoritative of this AccountMgmtInfoApp.
        If true, sync from the managed app will be performed as authoritative sync.

        **Added In:** 17.4.6

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :return: The is_authoritative of this AccountMgmtInfoApp.
        :rtype: bool
        """
        return self._is_authoritative

    @is_authoritative.setter
    def is_authoritative(self, is_authoritative):
        """
        Sets the is_authoritative of this AccountMgmtInfoApp.
        If true, sync from the managed app will be performed as authoritative sync.

        **Added In:** 17.4.6

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :param is_authoritative: The is_authoritative of this AccountMgmtInfoApp.
        :type: bool
        """
        self._is_authoritative = is_authoritative

    @property
    def meter_as_opc_service(self):
        """
        Gets the meter_as_opc_service of this AccountMgmtInfoApp.
        If true, customer is not billed for runtime operations of the app.

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :return: The meter_as_opc_service of this AccountMgmtInfoApp.
        :rtype: bool
        """
        return self._meter_as_opc_service

    @meter_as_opc_service.setter
    def meter_as_opc_service(self, meter_as_opc_service):
        """
        Sets the meter_as_opc_service of this AccountMgmtInfoApp.
        If true, customer is not billed for runtime operations of the app.

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :param meter_as_opc_service: The meter_as_opc_service of this AccountMgmtInfoApp.
        :type: bool
        """
        self._meter_as_opc_service = meter_as_opc_service

    @property
    def is_o_auth_resource(self):
        """
        Gets the is_o_auth_resource of this AccountMgmtInfoApp.
        If true, indicates that this application acts as an OAuth Resource.

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :return: The is_o_auth_resource of this AccountMgmtInfoApp.
        :rtype: bool
        """
        return self._is_o_auth_resource

    @is_o_auth_resource.setter
    def is_o_auth_resource(self, is_o_auth_resource):
        """
        Sets the is_o_auth_resource of this AccountMgmtInfoApp.
        If true, indicates that this application acts as an OAuth Resource.

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :param is_o_auth_resource: The is_o_auth_resource of this AccountMgmtInfoApp.
        :type: bool
        """
        self._is_o_auth_resource = is_o_auth_resource

    @property
    def audience(self):
        """
        Gets the audience of this AccountMgmtInfoApp.
        The base URI for all of the scopes defined in this App. The value of 'audience' is combined with the 'value' of each scope to form an 'fqs' or fully qualified scope.

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The audience of this AccountMgmtInfoApp.
        :rtype: str
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """
        Sets the audience of this AccountMgmtInfoApp.
        The base URI for all of the scopes defined in this App. The value of 'audience' is combined with the 'value' of each scope to form an 'fqs' or fully qualified scope.

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param audience: The audience of this AccountMgmtInfoApp.
        :type: str
        """
        self._audience = audience

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
