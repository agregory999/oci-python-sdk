# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SettingsImages(object):
    """
    References to various images
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SettingsImages object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this SettingsImages.
        :type value: str

        :param type:
            The value to assign to the type property of this SettingsImages.
        :type type: str

        :param display:
            The value to assign to the display property of this SettingsImages.
        :type display: str

        """
        self.swagger_types = {
            'value': 'str',
            'type': 'str',
            'display': 'str'
        }
        self.attribute_map = {
            'value': 'value',
            'type': 'type',
            'display': 'display'
        }
        self._value = None
        self._type = None
        self._display = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this SettingsImages.
        Image URI

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: reference


        :return: The value of this SettingsImages.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this SettingsImages.
        Image URI

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: reference


        :param value: The value of this SettingsImages.
        :type: str
        """
        self._value = value

    @property
    def type(self):
        """
        **[Required]** Gets the type of this SettingsImages.
        Indicates the image type

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string


        :return: The type of this SettingsImages.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SettingsImages.
        Indicates the image type

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string


        :param type: The type of this SettingsImages.
        :type: str
        """
        self._type = type

    @property
    def display(self):
        """
        Gets the display of this SettingsImages.
        A human-readable name, primarily used for display purposes

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string


        :return: The display of this SettingsImages.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this SettingsImages.
        A human-readable name, primarily used for display purposes

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string


        :param display: The display of this SettingsImages.
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
