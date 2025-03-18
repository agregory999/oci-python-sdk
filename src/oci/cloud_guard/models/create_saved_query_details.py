# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSavedQueryDetails(object):
    """
    Details of query to be saved
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSavedQueryDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateSavedQueryDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateSavedQueryDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateSavedQueryDetails.
        :type compartment_id: str

        :param query:
            The value to assign to the query property of this CreateSavedQueryDetails.
        :type query: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateSavedQueryDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateSavedQueryDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'query': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'query': 'query',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._query = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateSavedQueryDetails.
        Display name of the saved query


        :return: The display_name of this CreateSavedQueryDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateSavedQueryDetails.
        Display name of the saved query


        :param display_name: The display_name of this CreateSavedQueryDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateSavedQueryDetails.
        Description of the saved query


        :return: The description of this CreateSavedQueryDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateSavedQueryDetails.
        Description of the saved query


        :param description: The description of this CreateSavedQueryDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateSavedQueryDetails.
        Compartment OCID of the saved query


        :return: The compartment_id of this CreateSavedQueryDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateSavedQueryDetails.
        Compartment OCID of the saved query


        :param compartment_id: The compartment_id of this CreateSavedQueryDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def query(self):
        """
        **[Required]** Gets the query of this CreateSavedQueryDetails.
        The adhoc query expression that is run


        :return: The query of this CreateSavedQueryDetails.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this CreateSavedQueryDetails.
        The adhoc query expression that is run


        :param query: The query of this CreateSavedQueryDetails.
        :type: str
        """
        self._query = query

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateSavedQueryDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :return: The freeform_tags of this CreateSavedQueryDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateSavedQueryDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :param freeform_tags: The freeform_tags of this CreateSavedQueryDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateSavedQueryDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateSavedQueryDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateSavedQueryDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateSavedQueryDetails.
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
