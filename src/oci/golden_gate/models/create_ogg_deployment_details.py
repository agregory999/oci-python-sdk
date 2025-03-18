# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOggDeploymentDetails(object):
    """
    Deployment Data for creating an OggDeployment
    """

    #: A constant which can be used with the credential_store property of a CreateOggDeploymentDetails.
    #: This constant has a value of "GOLDENGATE"
    CREDENTIAL_STORE_GOLDENGATE = "GOLDENGATE"

    #: A constant which can be used with the credential_store property of a CreateOggDeploymentDetails.
    #: This constant has a value of "IAM"
    CREDENTIAL_STORE_IAM = "IAM"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOggDeploymentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deployment_name:
            The value to assign to the deployment_name property of this CreateOggDeploymentDetails.
        :type deployment_name: str

        :param credential_store:
            The value to assign to the credential_store property of this CreateOggDeploymentDetails.
            Allowed values for this property are: "GOLDENGATE", "IAM"
        :type credential_store: str

        :param identity_domain_id:
            The value to assign to the identity_domain_id property of this CreateOggDeploymentDetails.
        :type identity_domain_id: str

        :param password_secret_id:
            The value to assign to the password_secret_id property of this CreateOggDeploymentDetails.
        :type password_secret_id: str

        :param admin_username:
            The value to assign to the admin_username property of this CreateOggDeploymentDetails.
        :type admin_username: str

        :param admin_password:
            The value to assign to the admin_password property of this CreateOggDeploymentDetails.
        :type admin_password: str

        :param certificate:
            The value to assign to the certificate property of this CreateOggDeploymentDetails.
        :type certificate: str

        :param key:
            The value to assign to the key property of this CreateOggDeploymentDetails.
        :type key: str

        :param ogg_version:
            The value to assign to the ogg_version property of this CreateOggDeploymentDetails.
        :type ogg_version: str

        :param group_to_roles_mapping:
            The value to assign to the group_to_roles_mapping property of this CreateOggDeploymentDetails.
        :type group_to_roles_mapping: oci.golden_gate.models.GroupToRolesMappingDetails

        """
        self.swagger_types = {
            'deployment_name': 'str',
            'credential_store': 'str',
            'identity_domain_id': 'str',
            'password_secret_id': 'str',
            'admin_username': 'str',
            'admin_password': 'str',
            'certificate': 'str',
            'key': 'str',
            'ogg_version': 'str',
            'group_to_roles_mapping': 'GroupToRolesMappingDetails'
        }
        self.attribute_map = {
            'deployment_name': 'deploymentName',
            'credential_store': 'credentialStore',
            'identity_domain_id': 'identityDomainId',
            'password_secret_id': 'passwordSecretId',
            'admin_username': 'adminUsername',
            'admin_password': 'adminPassword',
            'certificate': 'certificate',
            'key': 'key',
            'ogg_version': 'oggVersion',
            'group_to_roles_mapping': 'groupToRolesMapping'
        }
        self._deployment_name = None
        self._credential_store = None
        self._identity_domain_id = None
        self._password_secret_id = None
        self._admin_username = None
        self._admin_password = None
        self._certificate = None
        self._key = None
        self._ogg_version = None
        self._group_to_roles_mapping = None

    @property
    def deployment_name(self):
        """
        **[Required]** Gets the deployment_name of this CreateOggDeploymentDetails.
        The name given to the GoldenGate service deployment.
        The name must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.


        :return: The deployment_name of this CreateOggDeploymentDetails.
        :rtype: str
        """
        return self._deployment_name

    @deployment_name.setter
    def deployment_name(self, deployment_name):
        """
        Sets the deployment_name of this CreateOggDeploymentDetails.
        The name given to the GoldenGate service deployment.
        The name must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.


        :param deployment_name: The deployment_name of this CreateOggDeploymentDetails.
        :type: str
        """
        self._deployment_name = deployment_name

    @property
    def credential_store(self):
        """
        Gets the credential_store of this CreateOggDeploymentDetails.
        The type of credential store for OGG.

        Allowed values for this property are: "GOLDENGATE", "IAM"


        :return: The credential_store of this CreateOggDeploymentDetails.
        :rtype: str
        """
        return self._credential_store

    @credential_store.setter
    def credential_store(self, credential_store):
        """
        Sets the credential_store of this CreateOggDeploymentDetails.
        The type of credential store for OGG.


        :param credential_store: The credential_store of this CreateOggDeploymentDetails.
        :type: str
        """
        allowed_values = ["GOLDENGATE", "IAM"]
        if not value_allowed_none_or_none_sentinel(credential_store, allowed_values):
            raise ValueError(
                f"Invalid value for `credential_store`, must be None or one of {allowed_values}"
            )
        self._credential_store = credential_store

    @property
    def identity_domain_id(self):
        """
        Gets the identity_domain_id of this CreateOggDeploymentDetails.
        The `OCID`__ of the Identity Domain when IAM credential store is used.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The identity_domain_id of this CreateOggDeploymentDetails.
        :rtype: str
        """
        return self._identity_domain_id

    @identity_domain_id.setter
    def identity_domain_id(self, identity_domain_id):
        """
        Sets the identity_domain_id of this CreateOggDeploymentDetails.
        The `OCID`__ of the Identity Domain when IAM credential store is used.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param identity_domain_id: The identity_domain_id of this CreateOggDeploymentDetails.
        :type: str
        """
        self._identity_domain_id = identity_domain_id

    @property
    def password_secret_id(self):
        """
        Gets the password_secret_id of this CreateOggDeploymentDetails.
        The `OCID`__ of the Secret where the deployment password is stored.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The password_secret_id of this CreateOggDeploymentDetails.
        :rtype: str
        """
        return self._password_secret_id

    @password_secret_id.setter
    def password_secret_id(self, password_secret_id):
        """
        Sets the password_secret_id of this CreateOggDeploymentDetails.
        The `OCID`__ of the Secret where the deployment password is stored.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param password_secret_id: The password_secret_id of this CreateOggDeploymentDetails.
        :type: str
        """
        self._password_secret_id = password_secret_id

    @property
    def admin_username(self):
        """
        Gets the admin_username of this CreateOggDeploymentDetails.
        The GoldenGate deployment console username.


        :return: The admin_username of this CreateOggDeploymentDetails.
        :rtype: str
        """
        return self._admin_username

    @admin_username.setter
    def admin_username(self, admin_username):
        """
        Sets the admin_username of this CreateOggDeploymentDetails.
        The GoldenGate deployment console username.


        :param admin_username: The admin_username of this CreateOggDeploymentDetails.
        :type: str
        """
        self._admin_username = admin_username

    @property
    def admin_password(self):
        """
        Gets the admin_password of this CreateOggDeploymentDetails.
        The password associated with the GoldenGate deployment console username.
        The password must be 8 to 30 characters long and must contain at least 1 uppercase, 1 lowercase, 1 numeric,
        and 1 special character. Special characters such as '$', '^', or '?' are not allowed.
        This field will be deprecated and replaced by \"passwordSecretId\".


        :return: The admin_password of this CreateOggDeploymentDetails.
        :rtype: str
        """
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        """
        Sets the admin_password of this CreateOggDeploymentDetails.
        The password associated with the GoldenGate deployment console username.
        The password must be 8 to 30 characters long and must contain at least 1 uppercase, 1 lowercase, 1 numeric,
        and 1 special character. Special characters such as '$', '^', or '?' are not allowed.
        This field will be deprecated and replaced by \"passwordSecretId\".


        :param admin_password: The admin_password of this CreateOggDeploymentDetails.
        :type: str
        """
        self._admin_password = admin_password

    @property
    def certificate(self):
        """
        Gets the certificate of this CreateOggDeploymentDetails.
        The base64 encoded content of the PEM file containing the SSL certificate.


        :return: The certificate of this CreateOggDeploymentDetails.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """
        Sets the certificate of this CreateOggDeploymentDetails.
        The base64 encoded content of the PEM file containing the SSL certificate.


        :param certificate: The certificate of this CreateOggDeploymentDetails.
        :type: str
        """
        self._certificate = certificate

    @property
    def key(self):
        """
        Gets the key of this CreateOggDeploymentDetails.
        The base64 encoded content of the PEM file containing the private key.


        :return: The key of this CreateOggDeploymentDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CreateOggDeploymentDetails.
        The base64 encoded content of the PEM file containing the private key.


        :param key: The key of this CreateOggDeploymentDetails.
        :type: str
        """
        self._key = key

    @property
    def ogg_version(self):
        """
        Gets the ogg_version of this CreateOggDeploymentDetails.
        Version of OGG


        :return: The ogg_version of this CreateOggDeploymentDetails.
        :rtype: str
        """
        return self._ogg_version

    @ogg_version.setter
    def ogg_version(self, ogg_version):
        """
        Sets the ogg_version of this CreateOggDeploymentDetails.
        Version of OGG


        :param ogg_version: The ogg_version of this CreateOggDeploymentDetails.
        :type: str
        """
        self._ogg_version = ogg_version

    @property
    def group_to_roles_mapping(self):
        """
        Gets the group_to_roles_mapping of this CreateOggDeploymentDetails.

        :return: The group_to_roles_mapping of this CreateOggDeploymentDetails.
        :rtype: oci.golden_gate.models.GroupToRolesMappingDetails
        """
        return self._group_to_roles_mapping

    @group_to_roles_mapping.setter
    def group_to_roles_mapping(self, group_to_roles_mapping):
        """
        Sets the group_to_roles_mapping of this CreateOggDeploymentDetails.

        :param group_to_roles_mapping: The group_to_roles_mapping of this CreateOggDeploymentDetails.
        :type: oci.golden_gate.models.GroupToRolesMappingDetails
        """
        self._group_to_roles_mapping = group_to_roles_mapping

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
