# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseToolsRelatedResourceMySql(object):
    """
    A related resource
    """

    #: A constant which can be used with the entity_type property of a DatabaseToolsRelatedResourceMySql.
    #: This constant has a value of "MYSQLDBSYSTEM"
    ENTITY_TYPE_MYSQLDBSYSTEM = "MYSQLDBSYSTEM"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseToolsRelatedResourceMySql object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_type:
            The value to assign to the entity_type property of this DatabaseToolsRelatedResourceMySql.
            Allowed values for this property are: "MYSQLDBSYSTEM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_type: str

        :param identifier:
            The value to assign to the identifier property of this DatabaseToolsRelatedResourceMySql.
        :type identifier: str

        """
        self.swagger_types = {
            'entity_type': 'str',
            'identifier': 'str'
        }

        self.attribute_map = {
            'entity_type': 'entityType',
            'identifier': 'identifier'
        }

        self._entity_type = None
        self._identifier = None

    @property
    def entity_type(self):
        """
        **[Required]** Gets the entity_type of this DatabaseToolsRelatedResourceMySql.
        The resource entity type.

        Allowed values for this property are: "MYSQLDBSYSTEM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The entity_type of this DatabaseToolsRelatedResourceMySql.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this DatabaseToolsRelatedResourceMySql.
        The resource entity type.


        :param entity_type: The entity_type of this DatabaseToolsRelatedResourceMySql.
        :type: str
        """
        allowed_values = ["MYSQLDBSYSTEM"]
        if not value_allowed_none_or_none_sentinel(entity_type, allowed_values):
            entity_type = 'UNKNOWN_ENUM_VALUE'
        self._entity_type = entity_type

    @property
    def identifier(self):
        """
        **[Required]** Gets the identifier of this DatabaseToolsRelatedResourceMySql.
        The `OCID`__ of the related resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The identifier of this DatabaseToolsRelatedResourceMySql.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this DatabaseToolsRelatedResourceMySql.
        The `OCID`__ of the related resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param identifier: The identifier of this DatabaseToolsRelatedResourceMySql.
        :type: str
        """
        self._identifier = identifier

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
