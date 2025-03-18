# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CloudGateMappingGatewayApp(object):
    """
    Reference to gateway application protected by this Cloud Gate

    **SCIM++ Properties:**
    - caseExact: false
    - idcsSearchable: true
    - multiValued: false
    - mutability: readWrite
    - required: true
    - returned: default
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CloudGateMappingGatewayApp object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CloudGateMappingGatewayApp.
        :type name: str

        :param value:
            The value to assign to the value property of this CloudGateMappingGatewayApp.
        :type value: str

        :param ref:
            The value to assign to the ref property of this CloudGateMappingGatewayApp.
        :type ref: str

        """
        self.swagger_types = {
            'name': 'str',
            'value': 'str',
            'ref': 'str'
        }
        self.attribute_map = {
            'name': 'name',
            'value': 'value',
            'ref': '$ref'
        }
        self._name = None
        self._value = None
        self._ref = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CloudGateMappingGatewayApp.
        The name (Client ID) of the gateway application protected by this Cloud Gate.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The name of this CloudGateMappingGatewayApp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CloudGateMappingGatewayApp.
        The name (Client ID) of the gateway application protected by this Cloud Gate.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param name: The name of this CloudGateMappingGatewayApp.
        :type: str
        """
        self._name = name

    @property
    def value(self):
        """
        **[Required]** Gets the value of this CloudGateMappingGatewayApp.
        The id of the gateway application protected by this Cloud Gate.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The value of this CloudGateMappingGatewayApp.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this CloudGateMappingGatewayApp.
        The id of the gateway application protected by this Cloud Gate.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param value: The value of this CloudGateMappingGatewayApp.
        :type: str
        """
        self._value = value

    @property
    def ref(self):
        """
        Gets the ref of this CloudGateMappingGatewayApp.
        The URI to the gateway application protected by this Cloud Gate

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this CloudGateMappingGatewayApp.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this CloudGateMappingGatewayApp.
        The URI to the gateway application protected by this Cloud Gate

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this CloudGateMappingGatewayApp.
        :type: str
        """
        self._ref = ref

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
