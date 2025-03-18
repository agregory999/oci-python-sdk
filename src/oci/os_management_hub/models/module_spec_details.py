# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModuleSpecDetails(object):
    """
    Details about a specific appstream module.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ModuleSpecDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ModuleSpecDetails.
        :type name: str

        :param stream:
            The value to assign to the stream property of this ModuleSpecDetails.
        :type stream: str

        :param profile:
            The value to assign to the profile property of this ModuleSpecDetails.
        :type profile: str

        """
        self.swagger_types = {
            'name': 'str',
            'stream': 'str',
            'profile': 'str'
        }
        self.attribute_map = {
            'name': 'name',
            'stream': 'stream',
            'profile': 'profile'
        }
        self._name = None
        self._stream = None
        self._profile = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ModuleSpecDetails.
        Name of the module.


        :return: The name of this ModuleSpecDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ModuleSpecDetails.
        Name of the module.


        :param name: The name of this ModuleSpecDetails.
        :type: str
        """
        self._name = name

    @property
    def stream(self):
        """
        Gets the stream of this ModuleSpecDetails.
        The stream of the module.


        :return: The stream of this ModuleSpecDetails.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """
        Sets the stream of this ModuleSpecDetails.
        The stream of the module.


        :param stream: The stream of this ModuleSpecDetails.
        :type: str
        """
        self._stream = stream

    @property
    def profile(self):
        """
        Gets the profile of this ModuleSpecDetails.
        The module profile to be used.


        :return: The profile of this ModuleSpecDetails.
        :rtype: str
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """
        Sets the profile of this ModuleSpecDetails.
        The module profile to be used.


        :param profile: The profile of this ModuleSpecDetails.
        :type: str
        """
        self._profile = profile

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
