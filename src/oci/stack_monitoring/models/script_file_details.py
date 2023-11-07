# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScriptFileDetails(object):
    """
    Script details applicable to any OS Command based Metric Extension which needs to run a script to collect data
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScriptFileDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ScriptFileDetails.
        :type name: str

        :param content:
            The value to assign to the content property of this ScriptFileDetails.
        :type content: str

        """
        self.swagger_types = {
            'name': 'str',
            'content': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'content': 'content'
        }

        self._name = None
        self._content = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ScriptFileDetails.
        Name of the script file


        :return: The name of this ScriptFileDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ScriptFileDetails.
        Name of the script file


        :param name: The name of this ScriptFileDetails.
        :type: str
        """
        self._name = name

    @property
    def content(self):
        """
        **[Required]** Gets the content of this ScriptFileDetails.
        Content of the script file as base64 encoded string


        :return: The content of this ScriptFileDetails.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this ScriptFileDetails.
        Content of the script file as base64 encoded string


        :param content: The content of this ScriptFileDetails.
        :type: str
        """
        self._content = content

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other