# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200430


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScopeReference(object):
    """
    The `ScopeReference` class is a base class for any model object that wraps a scope reference to a TypedObject.
    """

    #: A constant which can be used with the reference_type property of a ScopeReference.
    #: This constant has a value of "DIRECT_REF"
    REFERENCE_TYPE_DIRECT_REF = "DIRECT_REF"

    #: A constant which can be used with the reference_type property of a ScopeReference.
    #: This constant has a value of "BOUND_ENTITY_SHAPE"
    REFERENCE_TYPE_BOUND_ENTITY_SHAPE = "BOUND_ENTITY_SHAPE"

    #: A constant which can be used with the reference_type property of a ScopeReference.
    #: This constant has a value of "BOUND_ENTITY_SHAPE_FIELD"
    REFERENCE_TYPE_BOUND_ENTITY_SHAPE_FIELD = "BOUND_ENTITY_SHAPE_FIELD"

    #: A constant which can be used with the reference_type property of a ScopeReference.
    #: This constant has a value of "OCI_FUNCTION_INPUT_SHAPE"
    REFERENCE_TYPE_OCI_FUNCTION_INPUT_SHAPE = "OCI_FUNCTION_INPUT_SHAPE"

    #: A constant which can be used with the reference_type property of a ScopeReference.
    #: This constant has a value of "OCI_FUNCTION_OUTPUT_SHAPE"
    REFERENCE_TYPE_OCI_FUNCTION_OUTPUT_SHAPE = "OCI_FUNCTION_OUTPUT_SHAPE"

    def __init__(self, **kwargs):
        """
        Initializes a new ScopeReference object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param reference_object:
            The value to assign to the reference_object property of this ScopeReference.
        :type reference_object: str

        :param reference_type:
            The value to assign to the reference_type property of this ScopeReference.
            Allowed values for this property are: "DIRECT_REF", "BOUND_ENTITY_SHAPE", "BOUND_ENTITY_SHAPE_FIELD", "OCI_FUNCTION_INPUT_SHAPE", "OCI_FUNCTION_OUTPUT_SHAPE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type reference_type: str

        :param ref_object_name:
            The value to assign to the ref_object_name property of this ScopeReference.
        :type ref_object_name: str

        """
        self.swagger_types = {
            'reference_object': 'str',
            'reference_type': 'str',
            'ref_object_name': 'str'
        }
        self.attribute_map = {
            'reference_object': 'referenceObject',
            'reference_type': 'referenceType',
            'ref_object_name': 'refObjectName'
        }
        self._reference_object = None
        self._reference_type = None
        self._ref_object_name = None

    @property
    def reference_object(self):
        """
        **[Required]** Gets the reference_object of this ScopeReference.
        A key or shallow reference to an object.  For direct reference, it points to the actual scope object.  For BOUND_ENTITY_SHAPE or BOUND_ENTITY_SHAPE_FIELD, it points to the source or target operator.   For OCI_FUNCTION_INPUT_SHAPE or OCI_FUNCTION_OUTPUT_SHAPE, it points to the OCI Function object.


        :return: The reference_object of this ScopeReference.
        :rtype: str
        """
        return self._reference_object

    @reference_object.setter
    def reference_object(self, reference_object):
        """
        Sets the reference_object of this ScopeReference.
        A key or shallow reference to an object.  For direct reference, it points to the actual scope object.  For BOUND_ENTITY_SHAPE or BOUND_ENTITY_SHAPE_FIELD, it points to the source or target operator.   For OCI_FUNCTION_INPUT_SHAPE or OCI_FUNCTION_OUTPUT_SHAPE, it points to the OCI Function object.


        :param reference_object: The reference_object of this ScopeReference.
        :type: str
        """
        self._reference_object = reference_object

    @property
    def reference_type(self):
        """
        Gets the reference_type of this ScopeReference.
        The reference type for this reference.  Set to null for a direct reference, for indirect references set to a type of association such as \"BOUND_ENTITY_SHAPE\".   Current known reference type values are \"BOUND_ENTITY_SHAPE\", \"BOUND_ENTITY_SHAPE_FIELD\", \"OCI_FUNCTION_INPUT_SHAPE\", \"OCI_FUNCTION_OUTPUT_SHAPE\"

        Allowed values for this property are: "DIRECT_REF", "BOUND_ENTITY_SHAPE", "BOUND_ENTITY_SHAPE_FIELD", "OCI_FUNCTION_INPUT_SHAPE", "OCI_FUNCTION_OUTPUT_SHAPE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The reference_type of this ScopeReference.
        :rtype: str
        """
        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type):
        """
        Sets the reference_type of this ScopeReference.
        The reference type for this reference.  Set to null for a direct reference, for indirect references set to a type of association such as \"BOUND_ENTITY_SHAPE\".   Current known reference type values are \"BOUND_ENTITY_SHAPE\", \"BOUND_ENTITY_SHAPE_FIELD\", \"OCI_FUNCTION_INPUT_SHAPE\", \"OCI_FUNCTION_OUTPUT_SHAPE\"


        :param reference_type: The reference_type of this ScopeReference.
        :type: str
        """
        allowed_values = ["DIRECT_REF", "BOUND_ENTITY_SHAPE", "BOUND_ENTITY_SHAPE_FIELD", "OCI_FUNCTION_INPUT_SHAPE", "OCI_FUNCTION_OUTPUT_SHAPE"]
        if not value_allowed_none_or_none_sentinel(reference_type, allowed_values):
            reference_type = 'UNKNOWN_ENUM_VALUE'
        self._reference_type = reference_type

    @property
    def ref_object_name(self):
        """
        Gets the ref_object_name of this ScopeReference.
        The referenced object name for this reference.  Set to the field name if the referenceType is BOUND_ENTITY_SHAPE_FIELD, else set to null.


        :return: The ref_object_name of this ScopeReference.
        :rtype: str
        """
        return self._ref_object_name

    @ref_object_name.setter
    def ref_object_name(self, ref_object_name):
        """
        Sets the ref_object_name of this ScopeReference.
        The referenced object name for this reference.  Set to the field name if the referenceType is BOUND_ENTITY_SHAPE_FIELD, else set to null.


        :param ref_object_name: The ref_object_name of this ScopeReference.
        :type: str
        """
        self._ref_object_name = ref_object_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
