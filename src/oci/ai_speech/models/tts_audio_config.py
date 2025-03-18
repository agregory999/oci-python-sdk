# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TtsAudioConfig(object):
    """
    Use this schema to specify handling of audio response.
    If audioConfig is not provided, raw response is handed over for the user to handle.
    """

    #: A constant which can be used with the config_type property of a TtsAudioConfig.
    #: This constant has a value of "BASE_AUDIO_CONFIG"
    CONFIG_TYPE_BASE_AUDIO_CONFIG = "BASE_AUDIO_CONFIG"

    def __init__(self, **kwargs):
        """
        Initializes a new TtsAudioConfig object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.ai_speech.models.TtsBaseAudioConfig`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_type:
            The value to assign to the config_type property of this TtsAudioConfig.
            Allowed values for this property are: "BASE_AUDIO_CONFIG"
        :type config_type: str

        """
        self.swagger_types = {
            'config_type': 'str'
        }
        self.attribute_map = {
            'config_type': 'configType'
        }
        self._config_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['configType']

        if type == 'BASE_AUDIO_CONFIG':
            return 'TtsBaseAudioConfig'
        else:
            return 'TtsAudioConfig'

    @property
    def config_type(self):
        """
        **[Required]** Gets the config_type of this TtsAudioConfig.
        The audio config type to use for handling the audio output.
        Supported config types are:
        - BASE_AUDIO_CONFIG

        Allowed values for this property are: "BASE_AUDIO_CONFIG"


        :return: The config_type of this TtsAudioConfig.
        :rtype: str
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        """
        Sets the config_type of this TtsAudioConfig.
        The audio config type to use for handling the audio output.
        Supported config types are:
        - BASE_AUDIO_CONFIG


        :param config_type: The config_type of this TtsAudioConfig.
        :type: str
        """
        allowed_values = ["BASE_AUDIO_CONFIG"]
        if not value_allowed_none_or_none_sentinel(config_type, allowed_values):
            raise ValueError(
                f"Invalid value for `config_type`, must be None or one of {allowed_values}"
            )
        self._config_type = config_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
