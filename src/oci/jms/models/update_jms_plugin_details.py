# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210610


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateJmsPluginDetails(object):
    """
    Attributes to update a JmsPlugin.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateJmsPluginDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param fleet_id:
            The value to assign to the fleet_id property of this UpdateJmsPluginDetails.
        :type fleet_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateJmsPluginDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateJmsPluginDetails.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'fleet_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)'
        }
        self.attribute_map = {
            'fleet_id': 'fleetId',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags'
        }
        self._fleet_id = None
        self._defined_tags = None
        self._freeform_tags = None

    @property
    def fleet_id(self):
        """
        Gets the fleet_id of this UpdateJmsPluginDetails.
        The `OCID`__ of the fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The fleet_id of this UpdateJmsPluginDetails.
        :rtype: str
        """
        return self._fleet_id

    @fleet_id.setter
    def fleet_id(self, fleet_id):
        """
        Sets the fleet_id of this UpdateJmsPluginDetails.
        The `OCID`__ of the fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param fleet_id: The fleet_id of this UpdateJmsPluginDetails.
        :type: str
        """
        self._fleet_id = fleet_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateJmsPluginDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See `Understanding Free-form Tags`__).

        __ https://docs.cloud.oracle.com/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm


        :return: The defined_tags of this UpdateJmsPluginDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateJmsPluginDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See `Understanding Free-form Tags`__).

        __ https://docs.cloud.oracle.com/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm


        :param defined_tags: The defined_tags of this UpdateJmsPluginDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateJmsPluginDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`. (See `Managing Tags and Tag Namespaces`__.)

        __ https://docs.cloud.oracle.com/Content/Tagging/Concepts/understandingfreeformtags.htm


        :return: The freeform_tags of this UpdateJmsPluginDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateJmsPluginDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`. (See `Managing Tags and Tag Namespaces`__.)

        __ https://docs.cloud.oracle.com/Content/Tagging/Concepts/understandingfreeformtags.htm


        :param freeform_tags: The freeform_tags of this UpdateJmsPluginDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
