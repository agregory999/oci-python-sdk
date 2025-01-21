# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataGuardGroup(object):
    """
    Details of Data Guard setup that the given database is part of.
    Also includes information about databases part of this Data Guard group and properties for their Data Guard configuration.
    """

    #: A constant which can be used with the protection_mode property of a DataGuardGroup.
    #: This constant has a value of "MAXIMUM_AVAILABILITY"
    PROTECTION_MODE_MAXIMUM_AVAILABILITY = "MAXIMUM_AVAILABILITY"

    #: A constant which can be used with the protection_mode property of a DataGuardGroup.
    #: This constant has a value of "MAXIMUM_PERFORMANCE"
    PROTECTION_MODE_MAXIMUM_PERFORMANCE = "MAXIMUM_PERFORMANCE"

    #: A constant which can be used with the protection_mode property of a DataGuardGroup.
    #: This constant has a value of "MAXIMUM_PROTECTION"
    PROTECTION_MODE_MAXIMUM_PROTECTION = "MAXIMUM_PROTECTION"

    def __init__(self, **kwargs):
        """
        Initializes a new DataGuardGroup object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param members:
            The value to assign to the members property of this DataGuardGroup.
        :type members: list[oci.database.models.DataGuardGroupMember]

        :param protection_mode:
            The value to assign to the protection_mode property of this DataGuardGroup.
            Allowed values for this property are: "MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", "MAXIMUM_PROTECTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type protection_mode: str

        """
        self.swagger_types = {
            'members': 'list[DataGuardGroupMember]',
            'protection_mode': 'str'
        }

        self.attribute_map = {
            'members': 'members',
            'protection_mode': 'protectionMode'
        }

        self._members = None
        self._protection_mode = None

    @property
    def members(self):
        """
        Gets the members of this DataGuardGroup.
        List of Data Guard members, representing each database that is part of Data Guard.


        :return: The members of this DataGuardGroup.
        :rtype: list[oci.database.models.DataGuardGroupMember]
        """
        return self._members

    @members.setter
    def members(self, members):
        """
        Sets the members of this DataGuardGroup.
        List of Data Guard members, representing each database that is part of Data Guard.


        :param members: The members of this DataGuardGroup.
        :type: list[oci.database.models.DataGuardGroupMember]
        """
        self._members = members

    @property
    def protection_mode(self):
        """
        Gets the protection_mode of this DataGuardGroup.
        The protection mode of this Data Guard. For more information, see
        `Oracle Data Guard Protection Modes`__
        in the Oracle Data Guard documentation.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000

        Allowed values for this property are: "MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", "MAXIMUM_PROTECTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The protection_mode of this DataGuardGroup.
        :rtype: str
        """
        return self._protection_mode

    @protection_mode.setter
    def protection_mode(self, protection_mode):
        """
        Sets the protection_mode of this DataGuardGroup.
        The protection mode of this Data Guard. For more information, see
        `Oracle Data Guard Protection Modes`__
        in the Oracle Data Guard documentation.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000


        :param protection_mode: The protection_mode of this DataGuardGroup.
        :type: str
        """
        allowed_values = ["MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", "MAXIMUM_PROTECTION"]
        if not value_allowed_none_or_none_sentinel(protection_mode, allowed_values):
            protection_mode = 'UNKNOWN_ENUM_VALUE'
        self._protection_mode = protection_mode

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
