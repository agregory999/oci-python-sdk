# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190325


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CustomPropertySetUsage(object):
    """
    Details of a single custom property.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CustomPropertySetUsage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this CustomPropertySetUsage.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this CustomPropertySetUsage.
        :type display_name: str

        :param value:
            The value to assign to the value property of this CustomPropertySetUsage.
        :type value: str

        :param namespace_name:
            The value to assign to the namespace_name property of this CustomPropertySetUsage.
        :type namespace_name: str

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'value': 'str',
            'namespace_name': 'str'
        }
        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'value': 'value',
            'namespace_name': 'namespaceName'
        }
        self._key = None
        self._display_name = None
        self._value = None
        self._namespace_name = None

    @property
    def key(self):
        """
        Gets the key of this CustomPropertySetUsage.
        Unique Identifier of the attribute which is ID


        :return: The key of this CustomPropertySetUsage.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CustomPropertySetUsage.
        Unique Identifier of the attribute which is ID


        :param key: The key of this CustomPropertySetUsage.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        Gets the display_name of this CustomPropertySetUsage.
        Name of the custom property


        :return: The display_name of this CustomPropertySetUsage.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CustomPropertySetUsage.
        Name of the custom property


        :param display_name: The display_name of this CustomPropertySetUsage.
        :type: str
        """
        self._display_name = display_name

    @property
    def value(self):
        """
        Gets the value of this CustomPropertySetUsage.
        The custom property value


        :return: The value of this CustomPropertySetUsage.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this CustomPropertySetUsage.
        The custom property value


        :param value: The value of this CustomPropertySetUsage.
        :type: str
        """
        self._value = value

    @property
    def namespace_name(self):
        """
        Gets the namespace_name of this CustomPropertySetUsage.
        Namespace name of the custom property


        :return: The namespace_name of this CustomPropertySetUsage.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this CustomPropertySetUsage.
        Namespace name of the custom property


        :param namespace_name: The namespace_name of this CustomPropertySetUsage.
        :type: str
        """
        self._namespace_name = namespace_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
