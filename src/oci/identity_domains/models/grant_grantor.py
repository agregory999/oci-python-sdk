# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GrantGrantor(object):
    """
    User conferring the grant to the beneficiary

    **SCIM++ Properties:**
    - idcsSearchable: true
    - multiValued: false
    - mutability: readOnly
    - idcsIgnoreReadOnlyAndImmutableRefAttrsDuringForceDelete: true
    - required: false
    - returned: default
    - type: complex
    """

    #: A constant which can be used with the type property of a GrantGrantor.
    #: This constant has a value of "User"
    TYPE_USER = "User"

    #: A constant which can be used with the type property of a GrantGrantor.
    #: This constant has a value of "App"
    TYPE_APP = "App"

    #: A constant which can be used with the type property of a GrantGrantor.
    #: This constant has a value of "Group"
    TYPE_GROUP = "Group"

    #: A constant which can be used with the type property of a GrantGrantor.
    #: This constant has a value of "AppEntitlementCollection"
    TYPE_APP_ENTITLEMENT_COLLECTION = "AppEntitlementCollection"

    #: A constant which can be used with the type property of a GrantGrantor.
    #: This constant has a value of "DynamicResourceGroup"
    TYPE_DYNAMIC_RESOURCE_GROUP = "DynamicResourceGroup"

    def __init__(self, **kwargs):
        """
        Initializes a new GrantGrantor object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this GrantGrantor.
        :type value: str

        :param ref:
            The value to assign to the ref property of this GrantGrantor.
        :type ref: str

        :param type:
            The value to assign to the type property of this GrantGrantor.
            Allowed values for this property are: "User", "App", "Group", "AppEntitlementCollection", "DynamicResourceGroup", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param display:
            The value to assign to the display property of this GrantGrantor.
        :type display: str

        """
        self.swagger_types = {
            'value': 'str',
            'ref': 'str',
            'type': 'str',
            'display': 'str'
        }
        self.attribute_map = {
            'value': 'value',
            'ref': '$ref',
            'type': 'type',
            'display': 'display'
        }
        self._value = None
        self._ref = None
        self._type = None
        self._display = None

    @property
    def value(self):
        """
        Gets the value of this GrantGrantor.
        Grantor user identifier

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The value of this GrantGrantor.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this GrantGrantor.
        Grantor user identifier

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param value: The value of this GrantGrantor.
        :type: str
        """
        self._value = value

    @property
    def ref(self):
        """
        Gets the ref of this GrantGrantor.
        Grantor URI

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this GrantGrantor.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this GrantGrantor.
        Grantor URI

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this GrantGrantor.
        :type: str
        """
        self._ref = ref

    @property
    def type(self):
        """
        **[Required]** Gets the type of this GrantGrantor.
        Resource type of the grantor. Allowed values are User and App.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsDefaultValue: User
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "User", "App", "Group", "AppEntitlementCollection", "DynamicResourceGroup", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this GrantGrantor.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this GrantGrantor.
        Resource type of the grantor. Allowed values are User and App.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsDefaultValue: User
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param type: The type of this GrantGrantor.
        :type: str
        """
        allowed_values = ["User", "App", "Group", "AppEntitlementCollection", "DynamicResourceGroup"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def display(self):
        """
        Gets the display of this GrantGrantor.
        Grantor display name

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The display of this GrantGrantor.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this GrantGrantor.
        Grantor display name

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param display: The display of this GrantGrantor.
        :type: str
        """
        self._display = display

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
