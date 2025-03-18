# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppExtensionFormFillAppTemplateAppTemplate(object):
    """
    This extension provides attributes for Form-Fill facet of AppTemplate
    """

    #: A constant which can be used with the form_type property of a AppExtensionFormFillAppTemplateAppTemplate.
    #: This constant has a value of "WebApplication"
    FORM_TYPE_WEB_APPLICATION = "WebApplication"

    #: A constant which can be used with the form_cred_method property of a AppExtensionFormFillAppTemplateAppTemplate.
    #: This constant has a value of "ADMIN_SETS_CREDENTIALS"
    FORM_CRED_METHOD_ADMIN_SETS_CREDENTIALS = "ADMIN_SETS_CREDENTIALS"

    #: A constant which can be used with the form_cred_method property of a AppExtensionFormFillAppTemplateAppTemplate.
    #: This constant has a value of "ADMIN_SETS_SHARED_CREDENTIALS"
    FORM_CRED_METHOD_ADMIN_SETS_SHARED_CREDENTIALS = "ADMIN_SETS_SHARED_CREDENTIALS"

    #: A constant which can be used with the form_cred_method property of a AppExtensionFormFillAppTemplateAppTemplate.
    #: This constant has a value of "USER_SETS_PASSWORD_ONLY"
    FORM_CRED_METHOD_USER_SETS_PASSWORD_ONLY = "USER_SETS_PASSWORD_ONLY"

    #: A constant which can be used with the form_cred_method property of a AppExtensionFormFillAppTemplateAppTemplate.
    #: This constant has a value of "USER_SETS_CREDENTIALS"
    FORM_CRED_METHOD_USER_SETS_CREDENTIALS = "USER_SETS_CREDENTIALS"

    #: A constant which can be used with the form_cred_method property of a AppExtensionFormFillAppTemplateAppTemplate.
    #: This constant has a value of "SSO_CREDENTIALS_AS_APP_CREDENTIALS"
    FORM_CRED_METHOD_SSO_CREDENTIALS_AS_APP_CREDENTIALS = "SSO_CREDENTIALS_AS_APP_CREDENTIALS"

    def __init__(self, **kwargs):
        """
        Initializes a new AppExtensionFormFillAppTemplateAppTemplate object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param form_type:
            The value to assign to the form_type property of this AppExtensionFormFillAppTemplateAppTemplate.
            Allowed values for this property are: "WebApplication", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type form_type: str

        :param form_credential_sharing_group_id:
            The value to assign to the form_credential_sharing_group_id property of this AppExtensionFormFillAppTemplateAppTemplate.
        :type form_credential_sharing_group_id: str

        :param reveal_password_on_form:
            The value to assign to the reveal_password_on_form property of this AppExtensionFormFillAppTemplateAppTemplate.
        :type reveal_password_on_form: bool

        :param user_name_form_template:
            The value to assign to the user_name_form_template property of this AppExtensionFormFillAppTemplateAppTemplate.
        :type user_name_form_template: str

        :param user_name_form_expression:
            The value to assign to the user_name_form_expression property of this AppExtensionFormFillAppTemplateAppTemplate.
        :type user_name_form_expression: str

        :param form_cred_method:
            The value to assign to the form_cred_method property of this AppExtensionFormFillAppTemplateAppTemplate.
            Allowed values for this property are: "ADMIN_SETS_CREDENTIALS", "ADMIN_SETS_SHARED_CREDENTIALS", "USER_SETS_PASSWORD_ONLY", "USER_SETS_CREDENTIALS", "SSO_CREDENTIALS_AS_APP_CREDENTIALS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type form_cred_method: str

        :param configuration:
            The value to assign to the configuration property of this AppExtensionFormFillAppTemplateAppTemplate.
        :type configuration: str

        :param sync_from_template:
            The value to assign to the sync_from_template property of this AppExtensionFormFillAppTemplateAppTemplate.
        :type sync_from_template: bool

        :param form_fill_url_match:
            The value to assign to the form_fill_url_match property of this AppExtensionFormFillAppTemplateAppTemplate.
        :type form_fill_url_match: list[oci.identity_domains.models.AppFormFillUrlMatch]

        """
        self.swagger_types = {
            'form_type': 'str',
            'form_credential_sharing_group_id': 'str',
            'reveal_password_on_form': 'bool',
            'user_name_form_template': 'str',
            'user_name_form_expression': 'str',
            'form_cred_method': 'str',
            'configuration': 'str',
            'sync_from_template': 'bool',
            'form_fill_url_match': 'list[AppFormFillUrlMatch]'
        }
        self.attribute_map = {
            'form_type': 'formType',
            'form_credential_sharing_group_id': 'formCredentialSharingGroupID',
            'reveal_password_on_form': 'revealPasswordOnForm',
            'user_name_form_template': 'userNameFormTemplate',
            'user_name_form_expression': 'userNameFormExpression',
            'form_cred_method': 'formCredMethod',
            'configuration': 'configuration',
            'sync_from_template': 'syncFromTemplate',
            'form_fill_url_match': 'formFillUrlMatch'
        }
        self._form_type = None
        self._form_credential_sharing_group_id = None
        self._reveal_password_on_form = None
        self._user_name_form_template = None
        self._user_name_form_expression = None
        self._form_cred_method = None
        self._configuration = None
        self._sync_from_template = None
        self._form_fill_url_match = None

    @property
    def form_type(self):
        """
        Gets the form_type of this AppExtensionFormFillAppTemplateAppTemplate.
        Type of the FormFill application like WebApplication, MainFrameApplication, WindowsApplication. Initially, we will support only WebApplication.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "WebApplication", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The form_type of this AppExtensionFormFillAppTemplateAppTemplate.
        :rtype: str
        """
        return self._form_type

    @form_type.setter
    def form_type(self, form_type):
        """
        Sets the form_type of this AppExtensionFormFillAppTemplateAppTemplate.
        Type of the FormFill application like WebApplication, MainFrameApplication, WindowsApplication. Initially, we will support only WebApplication.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param form_type: The form_type of this AppExtensionFormFillAppTemplateAppTemplate.
        :type: str
        """
        allowed_values = ["WebApplication"]
        if not value_allowed_none_or_none_sentinel(form_type, allowed_values):
            form_type = 'UNKNOWN_ENUM_VALUE'
        self._form_type = form_type

    @property
    def form_credential_sharing_group_id(self):
        """
        Gets the form_credential_sharing_group_id of this AppExtensionFormFillAppTemplateAppTemplate.
        Credential Sharing Group to which this form-fill application belongs.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The form_credential_sharing_group_id of this AppExtensionFormFillAppTemplateAppTemplate.
        :rtype: str
        """
        return self._form_credential_sharing_group_id

    @form_credential_sharing_group_id.setter
    def form_credential_sharing_group_id(self, form_credential_sharing_group_id):
        """
        Sets the form_credential_sharing_group_id of this AppExtensionFormFillAppTemplateAppTemplate.
        Credential Sharing Group to which this form-fill application belongs.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param form_credential_sharing_group_id: The form_credential_sharing_group_id of this AppExtensionFormFillAppTemplateAppTemplate.
        :type: str
        """
        self._form_credential_sharing_group_id = form_credential_sharing_group_id

    @property
    def reveal_password_on_form(self):
        """
        Gets the reveal_password_on_form of this AppExtensionFormFillAppTemplateAppTemplate.
        If true, indicates that system is allowed to show the password in plain-text for this account after re-authentication.

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The reveal_password_on_form of this AppExtensionFormFillAppTemplateAppTemplate.
        :rtype: bool
        """
        return self._reveal_password_on_form

    @reveal_password_on_form.setter
    def reveal_password_on_form(self, reveal_password_on_form):
        """
        Sets the reveal_password_on_form of this AppExtensionFormFillAppTemplateAppTemplate.
        If true, indicates that system is allowed to show the password in plain-text for this account after re-authentication.

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param reveal_password_on_form: The reveal_password_on_form of this AppExtensionFormFillAppTemplateAppTemplate.
        :type: bool
        """
        self._reveal_password_on_form = reveal_password_on_form

    @property
    def user_name_form_template(self):
        """
        Gets the user_name_form_template of this AppExtensionFormFillAppTemplateAppTemplate.
        Format for generating a username.  This value can be Username or Email Address; any other value will be treated as a custom expression.  A custom expression may combine 'concat' and 'substring' operations with literals and with any attribute of the Oracle Identity Cloud Service user.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The user_name_form_template of this AppExtensionFormFillAppTemplateAppTemplate.
        :rtype: str
        """
        return self._user_name_form_template

    @user_name_form_template.setter
    def user_name_form_template(self, user_name_form_template):
        """
        Sets the user_name_form_template of this AppExtensionFormFillAppTemplateAppTemplate.
        Format for generating a username.  This value can be Username or Email Address; any other value will be treated as a custom expression.  A custom expression may combine 'concat' and 'substring' operations with literals and with any attribute of the Oracle Identity Cloud Service user.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param user_name_form_template: The user_name_form_template of this AppExtensionFormFillAppTemplateAppTemplate.
        :type: str
        """
        self._user_name_form_template = user_name_form_template

    @property
    def user_name_form_expression(self):
        """
        Gets the user_name_form_expression of this AppExtensionFormFillAppTemplateAppTemplate.
        Indicates the custom expression, which can combine concat and substring operations with literals and with any attribute of the Oracle Identity Cloud Service User

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The user_name_form_expression of this AppExtensionFormFillAppTemplateAppTemplate.
        :rtype: str
        """
        return self._user_name_form_expression

    @user_name_form_expression.setter
    def user_name_form_expression(self, user_name_form_expression):
        """
        Sets the user_name_form_expression of this AppExtensionFormFillAppTemplateAppTemplate.
        Indicates the custom expression, which can combine concat and substring operations with literals and with any attribute of the Oracle Identity Cloud Service User

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param user_name_form_expression: The user_name_form_expression of this AppExtensionFormFillAppTemplateAppTemplate.
        :type: str
        """
        self._user_name_form_expression = user_name_form_expression

    @property
    def form_cred_method(self):
        """
        Gets the form_cred_method of this AppExtensionFormFillAppTemplateAppTemplate.
        Indicates how FormFill obtains the username and password of the account that FormFill will use to sign into the target App.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "ADMIN_SETS_CREDENTIALS", "ADMIN_SETS_SHARED_CREDENTIALS", "USER_SETS_PASSWORD_ONLY", "USER_SETS_CREDENTIALS", "SSO_CREDENTIALS_AS_APP_CREDENTIALS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The form_cred_method of this AppExtensionFormFillAppTemplateAppTemplate.
        :rtype: str
        """
        return self._form_cred_method

    @form_cred_method.setter
    def form_cred_method(self, form_cred_method):
        """
        Sets the form_cred_method of this AppExtensionFormFillAppTemplateAppTemplate.
        Indicates how FormFill obtains the username and password of the account that FormFill will use to sign into the target App.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param form_cred_method: The form_cred_method of this AppExtensionFormFillAppTemplateAppTemplate.
        :type: str
        """
        allowed_values = ["ADMIN_SETS_CREDENTIALS", "ADMIN_SETS_SHARED_CREDENTIALS", "USER_SETS_PASSWORD_ONLY", "USER_SETS_CREDENTIALS", "SSO_CREDENTIALS_AS_APP_CREDENTIALS"]
        if not value_allowed_none_or_none_sentinel(form_cred_method, allowed_values):
            form_cred_method = 'UNKNOWN_ENUM_VALUE'
        self._form_cred_method = form_cred_method

    @property
    def configuration(self):
        """
        Gets the configuration of this AppExtensionFormFillAppTemplateAppTemplate.
        FormFill Application Configuration CLOB which has to be maintained in Form-Fill APP for legacy code to do Form-Fill injection

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The configuration of this AppExtensionFormFillAppTemplateAppTemplate.
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """
        Sets the configuration of this AppExtensionFormFillAppTemplateAppTemplate.
        FormFill Application Configuration CLOB which has to be maintained in Form-Fill APP for legacy code to do Form-Fill injection

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param configuration: The configuration of this AppExtensionFormFillAppTemplateAppTemplate.
        :type: str
        """
        self._configuration = configuration

    @property
    def sync_from_template(self):
        """
        Gets the sync_from_template of this AppExtensionFormFillAppTemplateAppTemplate.
        If true, indicates that each of the Form-Fill-related attributes that can be inherited from the template actually will be inherited from the template. If false, indicates that the AppTemplate disabled inheritance for these Form-Fill-related attributes.

        **Added In:** 17.4.2

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The sync_from_template of this AppExtensionFormFillAppTemplateAppTemplate.
        :rtype: bool
        """
        return self._sync_from_template

    @sync_from_template.setter
    def sync_from_template(self, sync_from_template):
        """
        Sets the sync_from_template of this AppExtensionFormFillAppTemplateAppTemplate.
        If true, indicates that each of the Form-Fill-related attributes that can be inherited from the template actually will be inherited from the template. If false, indicates that the AppTemplate disabled inheritance for these Form-Fill-related attributes.

        **Added In:** 17.4.2

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param sync_from_template: The sync_from_template of this AppExtensionFormFillAppTemplateAppTemplate.
        :type: bool
        """
        self._sync_from_template = sync_from_template

    @property
    def form_fill_url_match(self):
        """
        Gets the form_fill_url_match of this AppExtensionFormFillAppTemplateAppTemplate.
        A list of application-formURLs that FormFill should match against any formUrl that the user-specifies when signing in to the target service.  Each item in the list also indicates how FormFill should interpret that formUrl.

        **SCIM++ Properties:**
         - idcsCompositeKey: [formUrl]
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: complex
         - uniqueness: none


        :return: The form_fill_url_match of this AppExtensionFormFillAppTemplateAppTemplate.
        :rtype: list[oci.identity_domains.models.AppFormFillUrlMatch]
        """
        return self._form_fill_url_match

    @form_fill_url_match.setter
    def form_fill_url_match(self, form_fill_url_match):
        """
        Sets the form_fill_url_match of this AppExtensionFormFillAppTemplateAppTemplate.
        A list of application-formURLs that FormFill should match against any formUrl that the user-specifies when signing in to the target service.  Each item in the list also indicates how FormFill should interpret that formUrl.

        **SCIM++ Properties:**
         - idcsCompositeKey: [formUrl]
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: complex
         - uniqueness: none


        :param form_fill_url_match: The form_fill_url_match of this AppExtensionFormFillAppTemplateAppTemplate.
        :type: list[oci.identity_domains.models.AppFormFillUrlMatch]
        """
        self._form_fill_url_match = form_fill_url_match

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
