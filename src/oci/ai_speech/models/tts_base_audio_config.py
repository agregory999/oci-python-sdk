# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220101

from .tts_audio_config import TtsAudioConfig
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TtsBaseAudioConfig(TtsAudioConfig):
    """
    Use this audio config for saving the audio response at specified path.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TtsBaseAudioConfig object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_speech.models.TtsBaseAudioConfig.config_type` attribute
        of this class is ``BASE_AUDIO_CONFIG`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_type:
            The value to assign to the config_type property of this TtsBaseAudioConfig.
            Allowed values for this property are: "BASE_AUDIO_CONFIG"
        :type config_type: str

        :param save_path:
            The value to assign to the save_path property of this TtsBaseAudioConfig.
        :type save_path: str

        """
        self.swagger_types = {
            'config_type': 'str',
            'save_path': 'str'
        }
        self.attribute_map = {
            'config_type': 'configType',
            'save_path': 'savePath'
        }
        self._config_type = None
        self._save_path = None
        self._config_type = 'BASE_AUDIO_CONFIG'

    @property
    def save_path(self):
        """
        **[Required]** Gets the save_path of this TtsBaseAudioConfig.
        Specify the path where you want to save the audio response.


        :return: The save_path of this TtsBaseAudioConfig.
        :rtype: str
        """
        return self._save_path

    @save_path.setter
    def save_path(self, save_path):
        """
        Sets the save_path of this TtsBaseAudioConfig.
        Specify the path where you want to save the audio response.


        :param save_path: The save_path of this TtsBaseAudioConfig.
        :type: str
        """
        self._save_path = save_path

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
