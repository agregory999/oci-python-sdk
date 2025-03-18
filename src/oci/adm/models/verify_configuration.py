# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220421


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VerifyConfiguration(object):
    """
    The Verify stage configuration specifies a build service to run a pipeline for the recommended code changes.
    The build pipeline will be initiated to ensure that there is no breaking change after the dependency versions
    have been updated in source to avoid vulnerabilities.
    """

    #: A constant which can be used with the build_service_type property of a VerifyConfiguration.
    #: This constant has a value of "OCI_DEVOPS_BUILD"
    BUILD_SERVICE_TYPE_OCI_DEVOPS_BUILD = "OCI_DEVOPS_BUILD"

    #: A constant which can be used with the build_service_type property of a VerifyConfiguration.
    #: This constant has a value of "GITLAB_PIPELINE"
    BUILD_SERVICE_TYPE_GITLAB_PIPELINE = "GITLAB_PIPELINE"

    #: A constant which can be used with the build_service_type property of a VerifyConfiguration.
    #: This constant has a value of "GITHUB_ACTIONS"
    BUILD_SERVICE_TYPE_GITHUB_ACTIONS = "GITHUB_ACTIONS"

    #: A constant which can be used with the build_service_type property of a VerifyConfiguration.
    #: This constant has a value of "JENKINS_PIPELINE"
    BUILD_SERVICE_TYPE_JENKINS_PIPELINE = "JENKINS_PIPELINE"

    #: A constant which can be used with the build_service_type property of a VerifyConfiguration.
    #: This constant has a value of "NONE"
    BUILD_SERVICE_TYPE_NONE = "NONE"

    def __init__(self, **kwargs):
        """
        Initializes a new VerifyConfiguration object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.adm.models.JenkinsPipelineConfiguration`
        * :class:`~oci.adm.models.NoneVerifyConfiguration`
        * :class:`~oci.adm.models.OciDevOpsBuildConfiguration`
        * :class:`~oci.adm.models.GitHubActionsConfiguration`
        * :class:`~oci.adm.models.GitLabPipelineConfiguration`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param build_service_type:
            The value to assign to the build_service_type property of this VerifyConfiguration.
            Allowed values for this property are: "OCI_DEVOPS_BUILD", "GITLAB_PIPELINE", "GITHUB_ACTIONS", "JENKINS_PIPELINE", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type build_service_type: str

        """
        self.swagger_types = {
            'build_service_type': 'str'
        }
        self.attribute_map = {
            'build_service_type': 'buildServiceType'
        }
        self._build_service_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['buildServiceType']

        if type == 'JENKINS_PIPELINE':
            return 'JenkinsPipelineConfiguration'

        if type == 'NONE':
            return 'NoneVerifyConfiguration'

        if type == 'OCI_DEVOPS_BUILD':
            return 'OciDevOpsBuildConfiguration'

        if type == 'GITHUB_ACTIONS':
            return 'GitHubActionsConfiguration'

        if type == 'GITLAB_PIPELINE':
            return 'GitLabPipelineConfiguration'
        else:
            return 'VerifyConfiguration'

    @property
    def build_service_type(self):
        """
        **[Required]** Gets the build_service_type of this VerifyConfiguration.
        The type of Build Service.

        Allowed values for this property are: "OCI_DEVOPS_BUILD", "GITLAB_PIPELINE", "GITHUB_ACTIONS", "JENKINS_PIPELINE", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The build_service_type of this VerifyConfiguration.
        :rtype: str
        """
        return self._build_service_type

    @build_service_type.setter
    def build_service_type(self, build_service_type):
        """
        Sets the build_service_type of this VerifyConfiguration.
        The type of Build Service.


        :param build_service_type: The build_service_type of this VerifyConfiguration.
        :type: str
        """
        allowed_values = ["OCI_DEVOPS_BUILD", "GITLAB_PIPELINE", "GITHUB_ACTIONS", "JENKINS_PIPELINE", "NONE"]
        if not value_allowed_none_or_none_sentinel(build_service_type, allowed_values):
            build_service_type = 'UNKNOWN_ENUM_VALUE'
        self._build_service_type = build_service_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
