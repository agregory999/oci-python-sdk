# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20191001


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Field(object):
    """
    Field information
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Field object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Field.
        :type name: str

        :param is_required:
            The value to assign to the is_required property of this Field.
        :type is_required: bool

        :param format:
            The value to assign to the format property of this Field.
        :type format: oci.osp_gateway.models.Format

        :param label:
            The value to assign to the label property of this Field.
        :type label: oci.osp_gateway.models.Label

        :param language:
            The value to assign to the language property of this Field.
        :type language: str

        """
        self.swagger_types = {
            'name': 'str',
            'is_required': 'bool',
            'format': 'Format',
            'label': 'Label',
            'language': 'str'
        }
        self.attribute_map = {
            'name': 'name',
            'is_required': 'isRequired',
            'format': 'format',
            'label': 'label',
            'language': 'language'
        }
        self._name = None
        self._is_required = None
        self._format = None
        self._label = None
        self._language = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Field.
        The field name


        :return: The name of this Field.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Field.
        The field name


        :param name: The name of this Field.
        :type: str
        """
        self._name = name

    @property
    def is_required(self):
        """
        **[Required]** Gets the is_required of this Field.
        The given field is requeired or not


        :return: The is_required of this Field.
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """
        Sets the is_required of this Field.
        The given field is requeired or not


        :param is_required: The is_required of this Field.
        :type: bool
        """
        self._is_required = is_required

    @property
    def format(self):
        """
        Gets the format of this Field.

        :return: The format of this Field.
        :rtype: oci.osp_gateway.models.Format
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this Field.

        :param format: The format of this Field.
        :type: oci.osp_gateway.models.Format
        """
        self._format = format

    @property
    def label(self):
        """
        Gets the label of this Field.

        :return: The label of this Field.
        :rtype: oci.osp_gateway.models.Label
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this Field.

        :param label: The label of this Field.
        :type: oci.osp_gateway.models.Label
        """
        self._label = label

    @property
    def language(self):
        """
        Gets the language of this Field.
        Locale code (rfc4646 format) of a forced language (e.g.: jp addresses require jp always)


        :return: The language of this Field.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this Field.
        Locale code (rfc4646 format) of a forced language (e.g.: jp addresses require jp always)


        :param language: The language of this Field.
        :type: str
        """
        self._language = language

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
