# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180222


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OpenIdConnectTokenAuthenticationConfig(object):
    """
    The properties that configure OIDC token authentication in kube-apiserver.
    For more information, see `Configuring the API Server`__.

    __ https://kubernetes.io/docs/reference/access-authn-authz/authentication/#using-flags
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OpenIdConnectTokenAuthenticationConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param issuer_url:
            The value to assign to the issuer_url property of this OpenIdConnectTokenAuthenticationConfig.
        :type issuer_url: str

        :param client_id:
            The value to assign to the client_id property of this OpenIdConnectTokenAuthenticationConfig.
        :type client_id: str

        :param username_claim:
            The value to assign to the username_claim property of this OpenIdConnectTokenAuthenticationConfig.
        :type username_claim: str

        :param username_prefix:
            The value to assign to the username_prefix property of this OpenIdConnectTokenAuthenticationConfig.
        :type username_prefix: str

        :param groups_claim:
            The value to assign to the groups_claim property of this OpenIdConnectTokenAuthenticationConfig.
        :type groups_claim: str

        :param groups_prefix:
            The value to assign to the groups_prefix property of this OpenIdConnectTokenAuthenticationConfig.
        :type groups_prefix: str

        :param required_claims:
            The value to assign to the required_claims property of this OpenIdConnectTokenAuthenticationConfig.
        :type required_claims: list[oci.container_engine.models.KeyValue]

        :param ca_certificate:
            The value to assign to the ca_certificate property of this OpenIdConnectTokenAuthenticationConfig.
        :type ca_certificate: str

        :param signing_algorithms:
            The value to assign to the signing_algorithms property of this OpenIdConnectTokenAuthenticationConfig.
        :type signing_algorithms: list[str]

        :param is_open_id_connect_auth_enabled:
            The value to assign to the is_open_id_connect_auth_enabled property of this OpenIdConnectTokenAuthenticationConfig.
        :type is_open_id_connect_auth_enabled: bool

        :param configuration_file:
            The value to assign to the configuration_file property of this OpenIdConnectTokenAuthenticationConfig.
        :type configuration_file: str

        """
        self.swagger_types = {
            'issuer_url': 'str',
            'client_id': 'str',
            'username_claim': 'str',
            'username_prefix': 'str',
            'groups_claim': 'str',
            'groups_prefix': 'str',
            'required_claims': 'list[KeyValue]',
            'ca_certificate': 'str',
            'signing_algorithms': 'list[str]',
            'is_open_id_connect_auth_enabled': 'bool',
            'configuration_file': 'str'
        }
        self.attribute_map = {
            'issuer_url': 'issuerUrl',
            'client_id': 'clientId',
            'username_claim': 'usernameClaim',
            'username_prefix': 'usernamePrefix',
            'groups_claim': 'groupsClaim',
            'groups_prefix': 'groupsPrefix',
            'required_claims': 'requiredClaims',
            'ca_certificate': 'caCertificate',
            'signing_algorithms': 'signingAlgorithms',
            'is_open_id_connect_auth_enabled': 'isOpenIdConnectAuthEnabled',
            'configuration_file': 'configurationFile'
        }
        self._issuer_url = None
        self._client_id = None
        self._username_claim = None
        self._username_prefix = None
        self._groups_claim = None
        self._groups_prefix = None
        self._required_claims = None
        self._ca_certificate = None
        self._signing_algorithms = None
        self._is_open_id_connect_auth_enabled = None
        self._configuration_file = None

    @property
    def issuer_url(self):
        """
        Gets the issuer_url of this OpenIdConnectTokenAuthenticationConfig.
        URL of the provider that allows the API server to discover public signing keys.
        Only URLs that use the https:// scheme are accepted. This is typically the provider's discovery URL,
        changed to have an empty path.


        :return: The issuer_url of this OpenIdConnectTokenAuthenticationConfig.
        :rtype: str
        """
        return self._issuer_url

    @issuer_url.setter
    def issuer_url(self, issuer_url):
        """
        Sets the issuer_url of this OpenIdConnectTokenAuthenticationConfig.
        URL of the provider that allows the API server to discover public signing keys.
        Only URLs that use the https:// scheme are accepted. This is typically the provider's discovery URL,
        changed to have an empty path.


        :param issuer_url: The issuer_url of this OpenIdConnectTokenAuthenticationConfig.
        :type: str
        """
        self._issuer_url = issuer_url

    @property
    def client_id(self):
        """
        Gets the client_id of this OpenIdConnectTokenAuthenticationConfig.
        A client id that all tokens must be issued for.


        :return: The client_id of this OpenIdConnectTokenAuthenticationConfig.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this OpenIdConnectTokenAuthenticationConfig.
        A client id that all tokens must be issued for.


        :param client_id: The client_id of this OpenIdConnectTokenAuthenticationConfig.
        :type: str
        """
        self._client_id = client_id

    @property
    def username_claim(self):
        """
        Gets the username_claim of this OpenIdConnectTokenAuthenticationConfig.
        JWT claim to use as the user name. By default sub, which is expected to be a unique identifier of the end
        user. Admins can choose other claims, such as email or name, depending on their provider. However, claims
        other than email will be prefixed with the issuer URL to prevent naming clashes with other plugins.


        :return: The username_claim of this OpenIdConnectTokenAuthenticationConfig.
        :rtype: str
        """
        return self._username_claim

    @username_claim.setter
    def username_claim(self, username_claim):
        """
        Sets the username_claim of this OpenIdConnectTokenAuthenticationConfig.
        JWT claim to use as the user name. By default sub, which is expected to be a unique identifier of the end
        user. Admins can choose other claims, such as email or name, depending on their provider. However, claims
        other than email will be prefixed with the issuer URL to prevent naming clashes with other plugins.


        :param username_claim: The username_claim of this OpenIdConnectTokenAuthenticationConfig.
        :type: str
        """
        self._username_claim = username_claim

    @property
    def username_prefix(self):
        """
        Gets the username_prefix of this OpenIdConnectTokenAuthenticationConfig.
        Prefix prepended to username claims to prevent clashes with existing names (such as system:users).
        For example, the value oidc: will create usernames like oidc:jane.doe. If this flag isn't provided and
        --oidc-username-claim is a value other than email the prefix defaults to ( Issuer URL )# where
        ( Issuer URL ) is the value of --oidc-issuer-url. The value - can be used to disable all prefixing.


        :return: The username_prefix of this OpenIdConnectTokenAuthenticationConfig.
        :rtype: str
        """
        return self._username_prefix

    @username_prefix.setter
    def username_prefix(self, username_prefix):
        """
        Sets the username_prefix of this OpenIdConnectTokenAuthenticationConfig.
        Prefix prepended to username claims to prevent clashes with existing names (such as system:users).
        For example, the value oidc: will create usernames like oidc:jane.doe. If this flag isn't provided and
        --oidc-username-claim is a value other than email the prefix defaults to ( Issuer URL )# where
        ( Issuer URL ) is the value of --oidc-issuer-url. The value - can be used to disable all prefixing.


        :param username_prefix: The username_prefix of this OpenIdConnectTokenAuthenticationConfig.
        :type: str
        """
        self._username_prefix = username_prefix

    @property
    def groups_claim(self):
        """
        Gets the groups_claim of this OpenIdConnectTokenAuthenticationConfig.
        JWT claim to use as the user's group. If the claim is present it must be an array of strings.


        :return: The groups_claim of this OpenIdConnectTokenAuthenticationConfig.
        :rtype: str
        """
        return self._groups_claim

    @groups_claim.setter
    def groups_claim(self, groups_claim):
        """
        Sets the groups_claim of this OpenIdConnectTokenAuthenticationConfig.
        JWT claim to use as the user's group. If the claim is present it must be an array of strings.


        :param groups_claim: The groups_claim of this OpenIdConnectTokenAuthenticationConfig.
        :type: str
        """
        self._groups_claim = groups_claim

    @property
    def groups_prefix(self):
        """
        Gets the groups_prefix of this OpenIdConnectTokenAuthenticationConfig.
        Prefix prepended to group claims to prevent clashes with existing names (such as system:groups).


        :return: The groups_prefix of this OpenIdConnectTokenAuthenticationConfig.
        :rtype: str
        """
        return self._groups_prefix

    @groups_prefix.setter
    def groups_prefix(self, groups_prefix):
        """
        Sets the groups_prefix of this OpenIdConnectTokenAuthenticationConfig.
        Prefix prepended to group claims to prevent clashes with existing names (such as system:groups).


        :param groups_prefix: The groups_prefix of this OpenIdConnectTokenAuthenticationConfig.
        :type: str
        """
        self._groups_prefix = groups_prefix

    @property
    def required_claims(self):
        """
        Gets the required_claims of this OpenIdConnectTokenAuthenticationConfig.
        A key=value pair that describes a required claim in the ID Token. If set, the claim is verified to be present
        in the ID Token with a matching value. Repeat this flag to specify multiple claims.


        :return: The required_claims of this OpenIdConnectTokenAuthenticationConfig.
        :rtype: list[oci.container_engine.models.KeyValue]
        """
        return self._required_claims

    @required_claims.setter
    def required_claims(self, required_claims):
        """
        Sets the required_claims of this OpenIdConnectTokenAuthenticationConfig.
        A key=value pair that describes a required claim in the ID Token. If set, the claim is verified to be present
        in the ID Token with a matching value. Repeat this flag to specify multiple claims.


        :param required_claims: The required_claims of this OpenIdConnectTokenAuthenticationConfig.
        :type: list[oci.container_engine.models.KeyValue]
        """
        self._required_claims = required_claims

    @property
    def ca_certificate(self):
        """
        Gets the ca_certificate of this OpenIdConnectTokenAuthenticationConfig.
        A Base64 encoded public RSA or ECDSA certificates used to signed your identity provider's web certificate.


        :return: The ca_certificate of this OpenIdConnectTokenAuthenticationConfig.
        :rtype: str
        """
        return self._ca_certificate

    @ca_certificate.setter
    def ca_certificate(self, ca_certificate):
        """
        Sets the ca_certificate of this OpenIdConnectTokenAuthenticationConfig.
        A Base64 encoded public RSA or ECDSA certificates used to signed your identity provider's web certificate.


        :param ca_certificate: The ca_certificate of this OpenIdConnectTokenAuthenticationConfig.
        :type: str
        """
        self._ca_certificate = ca_certificate

    @property
    def signing_algorithms(self):
        """
        Gets the signing_algorithms of this OpenIdConnectTokenAuthenticationConfig.
        The signing algorithms accepted. Default is [\"RS256\"].


        :return: The signing_algorithms of this OpenIdConnectTokenAuthenticationConfig.
        :rtype: list[str]
        """
        return self._signing_algorithms

    @signing_algorithms.setter
    def signing_algorithms(self, signing_algorithms):
        """
        Sets the signing_algorithms of this OpenIdConnectTokenAuthenticationConfig.
        The signing algorithms accepted. Default is [\"RS256\"].


        :param signing_algorithms: The signing_algorithms of this OpenIdConnectTokenAuthenticationConfig.
        :type: list[str]
        """
        self._signing_algorithms = signing_algorithms

    @property
    def is_open_id_connect_auth_enabled(self):
        """
        **[Required]** Gets the is_open_id_connect_auth_enabled of this OpenIdConnectTokenAuthenticationConfig.
        Whether the cluster has OIDC Auth Config enabled. Defaults to false.


        :return: The is_open_id_connect_auth_enabled of this OpenIdConnectTokenAuthenticationConfig.
        :rtype: bool
        """
        return self._is_open_id_connect_auth_enabled

    @is_open_id_connect_auth_enabled.setter
    def is_open_id_connect_auth_enabled(self, is_open_id_connect_auth_enabled):
        """
        Sets the is_open_id_connect_auth_enabled of this OpenIdConnectTokenAuthenticationConfig.
        Whether the cluster has OIDC Auth Config enabled. Defaults to false.


        :param is_open_id_connect_auth_enabled: The is_open_id_connect_auth_enabled of this OpenIdConnectTokenAuthenticationConfig.
        :type: bool
        """
        self._is_open_id_connect_auth_enabled = is_open_id_connect_auth_enabled

    @property
    def configuration_file(self):
        """
        Gets the configuration_file of this OpenIdConnectTokenAuthenticationConfig.
        A Base64 encoded string of a Kubernetes OIDC Auth Config file. More info `here`__

        __ https://kubernetes.io/docs/reference/access-authn-authz/authentication/#using-authentication-configuration


        :return: The configuration_file of this OpenIdConnectTokenAuthenticationConfig.
        :rtype: str
        """
        return self._configuration_file

    @configuration_file.setter
    def configuration_file(self, configuration_file):
        """
        Sets the configuration_file of this OpenIdConnectTokenAuthenticationConfig.
        A Base64 encoded string of a Kubernetes OIDC Auth Config file. More info `here`__

        __ https://kubernetes.io/docs/reference/access-authn-authz/authentication/#using-authentication-configuration


        :param configuration_file: The configuration_file of this OpenIdConnectTokenAuthenticationConfig.
        :type: str
        """
        self._configuration_file = configuration_file

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
