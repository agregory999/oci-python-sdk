# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdatePrivateEndpointDetails(object):
    """
    Information that can be updated for a private endpoint.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdatePrivateEndpointDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this UpdatePrivateEndpointDetails.
        :type name: str

        :param namespace:
            The value to assign to the namespace property of this UpdatePrivateEndpointDetails.
        :type namespace: str

        :param access_targets:
            The value to assign to the access_targets property of this UpdatePrivateEndpointDetails.
        :type access_targets: list[oci.object_storage.models.AccessTargetDetails]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdatePrivateEndpointDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdatePrivateEndpointDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'name': 'str',
            'namespace': 'str',
            'access_targets': 'list[AccessTargetDetails]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'name': 'name',
            'namespace': 'namespace',
            'access_targets': 'accessTargets',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._name = None
        self._namespace = None
        self._access_targets = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def name(self):
        """
        Gets the name of this UpdatePrivateEndpointDetails.
        This name associated with the endpoint. Valid characters are uppercase or lowercase letters, numbers, hyphens,
         underscores, and periods.
        Example: my-new-private-endpoint1


        :return: The name of this UpdatePrivateEndpointDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdatePrivateEndpointDetails.
        This name associated with the endpoint. Valid characters are uppercase or lowercase letters, numbers, hyphens,
         underscores, and periods.
        Example: my-new-private-endpoint1


        :param name: The name of this UpdatePrivateEndpointDetails.
        :type: str
        """
        self._name = name

    @property
    def namespace(self):
        """
        Gets the namespace of this UpdatePrivateEndpointDetails.
        The Object Storage namespace which will associated with the private endpoint.


        :return: The namespace of this UpdatePrivateEndpointDetails.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this UpdatePrivateEndpointDetails.
        The Object Storage namespace which will associated with the private endpoint.


        :param namespace: The namespace of this UpdatePrivateEndpointDetails.
        :type: str
        """
        self._namespace = namespace

    @property
    def access_targets(self):
        """
        Gets the access_targets of this UpdatePrivateEndpointDetails.
        A list of targets that can be accessed by the private endpoint.


        :return: The access_targets of this UpdatePrivateEndpointDetails.
        :rtype: list[oci.object_storage.models.AccessTargetDetails]
        """
        return self._access_targets

    @access_targets.setter
    def access_targets(self, access_targets):
        """
        Sets the access_targets of this UpdatePrivateEndpointDetails.
        A list of targets that can be accessed by the private endpoint.


        :param access_targets: The access_targets of this UpdatePrivateEndpointDetails.
        :type: list[oci.object_storage.models.AccessTargetDetails]
        """
        self._access_targets = access_targets

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdatePrivateEndpointDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdatePrivateEndpointDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdatePrivateEndpointDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdatePrivateEndpointDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdatePrivateEndpointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdatePrivateEndpointDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdatePrivateEndpointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdatePrivateEndpointDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
