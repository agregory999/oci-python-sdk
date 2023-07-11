# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BuildRunnerShapeConfig(object):
    """
    The information about build runner.
    """

    #: A constant which can be used with the build_runner_type property of a BuildRunnerShapeConfig.
    #: This constant has a value of "CUSTOM"
    BUILD_RUNNER_TYPE_CUSTOM = "CUSTOM"

    #: A constant which can be used with the build_runner_type property of a BuildRunnerShapeConfig.
    #: This constant has a value of "DEFAULT"
    BUILD_RUNNER_TYPE_DEFAULT = "DEFAULT"

    def __init__(self, **kwargs):
        """
        Initializes a new BuildRunnerShapeConfig object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.DefaultBuildRunnerShapeConfig`
        * :class:`~oci.devops.models.CustomBuildRunnerShapeConfig`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param build_runner_type:
            The value to assign to the build_runner_type property of this BuildRunnerShapeConfig.
            Allowed values for this property are: "CUSTOM", "DEFAULT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type build_runner_type: str

        """
        self.swagger_types = {
            'build_runner_type': 'str'
        }

        self.attribute_map = {
            'build_runner_type': 'buildRunnerType'
        }

        self._build_runner_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['buildRunnerType']

        if type == 'DEFAULT':
            return 'DefaultBuildRunnerShapeConfig'

        if type == 'CUSTOM':
            return 'CustomBuildRunnerShapeConfig'
        else:
            return 'BuildRunnerShapeConfig'

    @property
    def build_runner_type(self):
        """
        **[Required]** Gets the build_runner_type of this BuildRunnerShapeConfig.
        Name of the build runner shape in which the execution occurs. If not specified, the default shape is chosen.

        Allowed values for this property are: "CUSTOM", "DEFAULT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The build_runner_type of this BuildRunnerShapeConfig.
        :rtype: str
        """
        return self._build_runner_type

    @build_runner_type.setter
    def build_runner_type(self, build_runner_type):
        """
        Sets the build_runner_type of this BuildRunnerShapeConfig.
        Name of the build runner shape in which the execution occurs. If not specified, the default shape is chosen.


        :param build_runner_type: The build_runner_type of this BuildRunnerShapeConfig.
        :type: str
        """
        allowed_values = ["CUSTOM", "DEFAULT"]
        if not value_allowed_none_or_none_sentinel(build_runner_type, allowed_values):
            build_runner_type = 'UNKNOWN_ENUM_VALUE'
        self._build_runner_type = build_runner_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
