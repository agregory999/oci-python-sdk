# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDeployPipelineDetails(object):
    """
    The information to be updated for the given deloyment pipeline.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDeployPipelineDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateDeployPipelineDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this UpdateDeployPipelineDetails.
        :type display_name: str

        :param deploy_pipeline_parameters:
            The value to assign to the deploy_pipeline_parameters property of this UpdateDeployPipelineDetails.
        :type deploy_pipeline_parameters: oci.devops.models.DeployPipelineParameterCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDeployPipelineDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDeployPipelineDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'deploy_pipeline_parameters': 'DeployPipelineParameterCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'deploy_pipeline_parameters': 'deployPipelineParameters',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._description = None
        self._display_name = None
        self._deploy_pipeline_parameters = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def description(self):
        """
        Gets the description of this UpdateDeployPipelineDetails.
        Optional description about the deloyment pipeline.


        :return: The description of this UpdateDeployPipelineDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateDeployPipelineDetails.
        Optional description about the deloyment pipeline.


        :param description: The description of this UpdateDeployPipelineDetails.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateDeployPipelineDetails.
        Deloyment pipeline display name. Avoid entering confidential information.


        :return: The display_name of this UpdateDeployPipelineDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateDeployPipelineDetails.
        Deloyment pipeline display name. Avoid entering confidential information.


        :param display_name: The display_name of this UpdateDeployPipelineDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def deploy_pipeline_parameters(self):
        """
        Gets the deploy_pipeline_parameters of this UpdateDeployPipelineDetails.

        :return: The deploy_pipeline_parameters of this UpdateDeployPipelineDetails.
        :rtype: oci.devops.models.DeployPipelineParameterCollection
        """
        return self._deploy_pipeline_parameters

    @deploy_pipeline_parameters.setter
    def deploy_pipeline_parameters(self, deploy_pipeline_parameters):
        """
        Sets the deploy_pipeline_parameters of this UpdateDeployPipelineDetails.

        :param deploy_pipeline_parameters: The deploy_pipeline_parameters of this UpdateDeployPipelineDetails.
        :type: oci.devops.models.DeployPipelineParameterCollection
        """
        self._deploy_pipeline_parameters = deploy_pipeline_parameters

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateDeployPipelineDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateDeployPipelineDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateDeployPipelineDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateDeployPipelineDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateDeployPipelineDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateDeployPipelineDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateDeployPipelineDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateDeployPipelineDetails.
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
