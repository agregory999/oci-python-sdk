# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20171215


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LdapIdmap(object):
    """
    Mount target details about the LDAP ID mapping configuration.
    """

    #: A constant which can be used with the schema_type property of a LdapIdmap.
    #: This constant has a value of "RFC2307"
    SCHEMA_TYPE_RFC2307 = "RFC2307"

    def __init__(self, **kwargs):
        """
        Initializes a new LdapIdmap object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param schema_type:
            The value to assign to the schema_type property of this LdapIdmap.
            Allowed values for this property are: "RFC2307", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type schema_type: str

        :param cache_refresh_interval_seconds:
            The value to assign to the cache_refresh_interval_seconds property of this LdapIdmap.
        :type cache_refresh_interval_seconds: int

        :param cache_lifetime_seconds:
            The value to assign to the cache_lifetime_seconds property of this LdapIdmap.
        :type cache_lifetime_seconds: int

        :param negative_cache_lifetime_seconds:
            The value to assign to the negative_cache_lifetime_seconds property of this LdapIdmap.
        :type negative_cache_lifetime_seconds: int

        :param user_search_base:
            The value to assign to the user_search_base property of this LdapIdmap.
        :type user_search_base: str

        :param group_search_base:
            The value to assign to the group_search_base property of this LdapIdmap.
        :type group_search_base: str

        :param outbound_connector1_id:
            The value to assign to the outbound_connector1_id property of this LdapIdmap.
        :type outbound_connector1_id: str

        :param outbound_connector2_id:
            The value to assign to the outbound_connector2_id property of this LdapIdmap.
        :type outbound_connector2_id: str

        """
        self.swagger_types = {
            'schema_type': 'str',
            'cache_refresh_interval_seconds': 'int',
            'cache_lifetime_seconds': 'int',
            'negative_cache_lifetime_seconds': 'int',
            'user_search_base': 'str',
            'group_search_base': 'str',
            'outbound_connector1_id': 'str',
            'outbound_connector2_id': 'str'
        }

        self.attribute_map = {
            'schema_type': 'schemaType',
            'cache_refresh_interval_seconds': 'cacheRefreshIntervalSeconds',
            'cache_lifetime_seconds': 'cacheLifetimeSeconds',
            'negative_cache_lifetime_seconds': 'negativeCacheLifetimeSeconds',
            'user_search_base': 'userSearchBase',
            'group_search_base': 'groupSearchBase',
            'outbound_connector1_id': 'outboundConnector1Id',
            'outbound_connector2_id': 'outboundConnector2Id'
        }

        self._schema_type = None
        self._cache_refresh_interval_seconds = None
        self._cache_lifetime_seconds = None
        self._negative_cache_lifetime_seconds = None
        self._user_search_base = None
        self._group_search_base = None
        self._outbound_connector1_id = None
        self._outbound_connector2_id = None

    @property
    def schema_type(self):
        """
        Gets the schema_type of this LdapIdmap.
        Schema type of the LDAP account.

        Allowed values for this property are: "RFC2307", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The schema_type of this LdapIdmap.
        :rtype: str
        """
        return self._schema_type

    @schema_type.setter
    def schema_type(self, schema_type):
        """
        Sets the schema_type of this LdapIdmap.
        Schema type of the LDAP account.


        :param schema_type: The schema_type of this LdapIdmap.
        :type: str
        """
        allowed_values = ["RFC2307"]
        if not value_allowed_none_or_none_sentinel(schema_type, allowed_values):
            schema_type = 'UNKNOWN_ENUM_VALUE'
        self._schema_type = schema_type

    @property
    def cache_refresh_interval_seconds(self):
        """
        Gets the cache_refresh_interval_seconds of this LdapIdmap.
        The amount of time that the mount target should allow an entry to persist in its cache before attempting to refresh the entry.


        :return: The cache_refresh_interval_seconds of this LdapIdmap.
        :rtype: int
        """
        return self._cache_refresh_interval_seconds

    @cache_refresh_interval_seconds.setter
    def cache_refresh_interval_seconds(self, cache_refresh_interval_seconds):
        """
        Sets the cache_refresh_interval_seconds of this LdapIdmap.
        The amount of time that the mount target should allow an entry to persist in its cache before attempting to refresh the entry.


        :param cache_refresh_interval_seconds: The cache_refresh_interval_seconds of this LdapIdmap.
        :type: int
        """
        self._cache_refresh_interval_seconds = cache_refresh_interval_seconds

    @property
    def cache_lifetime_seconds(self):
        """
        Gets the cache_lifetime_seconds of this LdapIdmap.
        The maximum amount of time the mount target is allowed to use a cached entry.


        :return: The cache_lifetime_seconds of this LdapIdmap.
        :rtype: int
        """
        return self._cache_lifetime_seconds

    @cache_lifetime_seconds.setter
    def cache_lifetime_seconds(self, cache_lifetime_seconds):
        """
        Sets the cache_lifetime_seconds of this LdapIdmap.
        The maximum amount of time the mount target is allowed to use a cached entry.


        :param cache_lifetime_seconds: The cache_lifetime_seconds of this LdapIdmap.
        :type: int
        """
        self._cache_lifetime_seconds = cache_lifetime_seconds

    @property
    def negative_cache_lifetime_seconds(self):
        """
        Gets the negative_cache_lifetime_seconds of this LdapIdmap.
        The amount of time that a mount target will maintain information that a user is not found in the ID mapping configuration.


        :return: The negative_cache_lifetime_seconds of this LdapIdmap.
        :rtype: int
        """
        return self._negative_cache_lifetime_seconds

    @negative_cache_lifetime_seconds.setter
    def negative_cache_lifetime_seconds(self, negative_cache_lifetime_seconds):
        """
        Sets the negative_cache_lifetime_seconds of this LdapIdmap.
        The amount of time that a mount target will maintain information that a user is not found in the ID mapping configuration.


        :param negative_cache_lifetime_seconds: The negative_cache_lifetime_seconds of this LdapIdmap.
        :type: int
        """
        self._negative_cache_lifetime_seconds = negative_cache_lifetime_seconds

    @property
    def user_search_base(self):
        """
        Gets the user_search_base of this LdapIdmap.
        All LDAP searches are recursive starting at this user.

        Example: `CN=User,DC=domain,DC=com`


        :return: The user_search_base of this LdapIdmap.
        :rtype: str
        """
        return self._user_search_base

    @user_search_base.setter
    def user_search_base(self, user_search_base):
        """
        Sets the user_search_base of this LdapIdmap.
        All LDAP searches are recursive starting at this user.

        Example: `CN=User,DC=domain,DC=com`


        :param user_search_base: The user_search_base of this LdapIdmap.
        :type: str
        """
        self._user_search_base = user_search_base

    @property
    def group_search_base(self):
        """
        Gets the group_search_base of this LdapIdmap.
        All LDAP searches are recursive starting at this group.

        Example: `CN=Group,DC=domain,DC=com`


        :return: The group_search_base of this LdapIdmap.
        :rtype: str
        """
        return self._group_search_base

    @group_search_base.setter
    def group_search_base(self, group_search_base):
        """
        Sets the group_search_base of this LdapIdmap.
        All LDAP searches are recursive starting at this group.

        Example: `CN=Group,DC=domain,DC=com`


        :param group_search_base: The group_search_base of this LdapIdmap.
        :type: str
        """
        self._group_search_base = group_search_base

    @property
    def outbound_connector1_id(self):
        """
        Gets the outbound_connector1_id of this LdapIdmap.
        The `OCID`__ of the first connector to use to communicate with the LDAP server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The outbound_connector1_id of this LdapIdmap.
        :rtype: str
        """
        return self._outbound_connector1_id

    @outbound_connector1_id.setter
    def outbound_connector1_id(self, outbound_connector1_id):
        """
        Sets the outbound_connector1_id of this LdapIdmap.
        The `OCID`__ of the first connector to use to communicate with the LDAP server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param outbound_connector1_id: The outbound_connector1_id of this LdapIdmap.
        :type: str
        """
        self._outbound_connector1_id = outbound_connector1_id

    @property
    def outbound_connector2_id(self):
        """
        Gets the outbound_connector2_id of this LdapIdmap.
        The `OCID`__ of the second connector to use to communicate with the LDAP server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The outbound_connector2_id of this LdapIdmap.
        :rtype: str
        """
        return self._outbound_connector2_id

    @outbound_connector2_id.setter
    def outbound_connector2_id(self, outbound_connector2_id):
        """
        Sets the outbound_connector2_id of this LdapIdmap.
        The `OCID`__ of the second connector to use to communicate with the LDAP server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param outbound_connector2_id: The outbound_connector2_id of this LdapIdmap.
        :type: str
        """
        self._outbound_connector2_id = outbound_connector2_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
