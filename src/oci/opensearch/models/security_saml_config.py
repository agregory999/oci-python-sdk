# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180828


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecuritySamlConfig(object):
    """
    SAML policy is optionally used for Opensearch cluster to config SAML authentication
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SecuritySamlConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this SecuritySamlConfig.
        :type is_enabled: bool

        :param idp_metadata_content:
            The value to assign to the idp_metadata_content property of this SecuritySamlConfig.
        :type idp_metadata_content: str

        :param idp_entity_id:
            The value to assign to the idp_entity_id property of this SecuritySamlConfig.
        :type idp_entity_id: str

        :param opendashboard_url:
            The value to assign to the opendashboard_url property of this SecuritySamlConfig.
        :type opendashboard_url: str

        :param admin_backend_role:
            The value to assign to the admin_backend_role property of this SecuritySamlConfig.
        :type admin_backend_role: str

        :param subject_key:
            The value to assign to the subject_key property of this SecuritySamlConfig.
        :type subject_key: str

        :param roles_key:
            The value to assign to the roles_key property of this SecuritySamlConfig.
        :type roles_key: str

        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'idp_metadata_content': 'str',
            'idp_entity_id': 'str',
            'opendashboard_url': 'str',
            'admin_backend_role': 'str',
            'subject_key': 'str',
            'roles_key': 'str'
        }
        self.attribute_map = {
            'is_enabled': 'isEnabled',
            'idp_metadata_content': 'idpMetadataContent',
            'idp_entity_id': 'idpEntityId',
            'opendashboard_url': 'opendashboardUrl',
            'admin_backend_role': 'adminBackendRole',
            'subject_key': 'subjectKey',
            'roles_key': 'rolesKey'
        }
        self._is_enabled = None
        self._idp_metadata_content = None
        self._idp_entity_id = None
        self._opendashboard_url = None
        self._admin_backend_role = None
        self._subject_key = None
        self._roles_key = None

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this SecuritySamlConfig.
        A flag determine whether SAML is enabled


        :return: The is_enabled of this SecuritySamlConfig.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this SecuritySamlConfig.
        A flag determine whether SAML is enabled


        :param is_enabled: The is_enabled of this SecuritySamlConfig.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def idp_metadata_content(self):
        """
        **[Required]** Gets the idp_metadata_content of this SecuritySamlConfig.
        The content of identity provider metadata


        :return: The idp_metadata_content of this SecuritySamlConfig.
        :rtype: str
        """
        return self._idp_metadata_content

    @idp_metadata_content.setter
    def idp_metadata_content(self, idp_metadata_content):
        """
        Sets the idp_metadata_content of this SecuritySamlConfig.
        The content of identity provider metadata


        :param idp_metadata_content: The idp_metadata_content of this SecuritySamlConfig.
        :type: str
        """
        self._idp_metadata_content = idp_metadata_content

    @property
    def idp_entity_id(self):
        """
        **[Required]** Gets the idp_entity_id of this SecuritySamlConfig.
        The unique name for a identity provider entity


        :return: The idp_entity_id of this SecuritySamlConfig.
        :rtype: str
        """
        return self._idp_entity_id

    @idp_entity_id.setter
    def idp_entity_id(self, idp_entity_id):
        """
        Sets the idp_entity_id of this SecuritySamlConfig.
        The unique name for a identity provider entity


        :param idp_entity_id: The idp_entity_id of this SecuritySamlConfig.
        :type: str
        """
        self._idp_entity_id = idp_entity_id

    @property
    def opendashboard_url(self):
        """
        Gets the opendashboard_url of this SecuritySamlConfig.
        The endpoint of opendashboard


        :return: The opendashboard_url of this SecuritySamlConfig.
        :rtype: str
        """
        return self._opendashboard_url

    @opendashboard_url.setter
    def opendashboard_url(self, opendashboard_url):
        """
        Sets the opendashboard_url of this SecuritySamlConfig.
        The endpoint of opendashboard


        :param opendashboard_url: The opendashboard_url of this SecuritySamlConfig.
        :type: str
        """
        self._opendashboard_url = opendashboard_url

    @property
    def admin_backend_role(self):
        """
        Gets the admin_backend_role of this SecuritySamlConfig.
        The backend role of admins who have all permissions like local master user


        :return: The admin_backend_role of this SecuritySamlConfig.
        :rtype: str
        """
        return self._admin_backend_role

    @admin_backend_role.setter
    def admin_backend_role(self, admin_backend_role):
        """
        Sets the admin_backend_role of this SecuritySamlConfig.
        The backend role of admins who have all permissions like local master user


        :param admin_backend_role: The admin_backend_role of this SecuritySamlConfig.
        :type: str
        """
        self._admin_backend_role = admin_backend_role

    @property
    def subject_key(self):
        """
        Gets the subject_key of this SecuritySamlConfig.
        The subject key is used to get username from SAML assertion. By default, it is NameID


        :return: The subject_key of this SecuritySamlConfig.
        :rtype: str
        """
        return self._subject_key

    @subject_key.setter
    def subject_key(self, subject_key):
        """
        Sets the subject_key of this SecuritySamlConfig.
        The subject key is used to get username from SAML assertion. By default, it is NameID


        :param subject_key: The subject_key of this SecuritySamlConfig.
        :type: str
        """
        self._subject_key = subject_key

    @property
    def roles_key(self):
        """
        Gets the roles_key of this SecuritySamlConfig.
        The roles key is sued to get backend roles from SAML assertion


        :return: The roles_key of this SecuritySamlConfig.
        :rtype: str
        """
        return self._roles_key

    @roles_key.setter
    def roles_key(self, roles_key):
        """
        Sets the roles_key of this SecuritySamlConfig.
        The roles key is sued to get backend roles from SAML assertion


        :param roles_key: The roles_key of this SecuritySamlConfig.
        :type: str
        """
        self._roles_key = roles_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
