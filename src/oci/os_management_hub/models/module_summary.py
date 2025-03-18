# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModuleSummary(object):
    """
    Provides summary information about a module which is provided by a software source.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ModuleSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ModuleSummary.
        :type name: str

        :param streams:
            The value to assign to the streams property of this ModuleSummary.
        :type streams: list[str]

        :param software_source_id:
            The value to assign to the software_source_id property of this ModuleSummary.
        :type software_source_id: str

        """
        self.swagger_types = {
            'name': 'str',
            'streams': 'list[str]',
            'software_source_id': 'str'
        }
        self.attribute_map = {
            'name': 'name',
            'streams': 'streams',
            'software_source_id': 'softwareSourceId'
        }
        self._name = None
        self._streams = None
        self._software_source_id = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ModuleSummary.
        The name of the module.


        :return: The name of this ModuleSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ModuleSummary.
        The name of the module.


        :param name: The name of this ModuleSummary.
        :type: str
        """
        self._name = name

    @property
    def streams(self):
        """
        Gets the streams of this ModuleSummary.
        List of stream names.


        :return: The streams of this ModuleSummary.
        :rtype: list[str]
        """
        return self._streams

    @streams.setter
    def streams(self, streams):
        """
        Sets the streams of this ModuleSummary.
        List of stream names.


        :param streams: The streams of this ModuleSummary.
        :type: list[str]
        """
        self._streams = streams

    @property
    def software_source_id(self):
        """
        **[Required]** Gets the software_source_id of this ModuleSummary.
        The `OCID`__ of the software source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The software_source_id of this ModuleSummary.
        :rtype: str
        """
        return self._software_source_id

    @software_source_id.setter
    def software_source_id(self, software_source_id):
        """
        Sets the software_source_id of this ModuleSummary.
        The `OCID`__ of the software source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param software_source_id: The software_source_id of this ModuleSummary.
        :type: str
        """
        self._software_source_id = software_source_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
