# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221001


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigurationDetails(object):
    """
    training model details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param configuration_map:
            The value to assign to the configuration_map property of this ConfigurationDetails.
        :type configuration_map: dict(str, str)

        """
        self.swagger_types = {
            'configuration_map': 'dict(str, str)'
        }
        self.attribute_map = {
            'configuration_map': 'configurationMap'
        }
        self._configuration_map = None

    @property
    def configuration_map(self):
        """
        Gets the configuration_map of this ConfigurationDetails.
        model configuration details
        For PII : ConfigurationDetails will be PiiEntityMasking can be anyone of the following
        ex.{ \"mode\" : \"MASK\",\"maskingCharacter\" : \"&\",\"leaveCharactersUnmasked\": 3,\"isUnmaskedFromEnd\" : true  }
           { \"mode\" : \"MASK\",\"replaceWith\" : \"&\"  }
           { \"mode\" : \"REPLACE\" }
        For language translation :  { \"languageCodes\" : [\"cs\", \"ar\"]}
        Language code supported
                  Automatically detect language - auto
                  Arabic - ar
                  Brazilian Portuguese -  pt-BR
                  Czech - cs
                  Danish - da
                  Dutch - nl
                  English - en
                  Finnish - fi
                  French - fr
                  Canadian French - fr-CA
                  German - de
                  Italian - it
                  Japanese - ja
                  Korean - ko
                  Norwegian - no
                  Polish - pl
                  Romanian - ro
                  Simplified Chinese - zh-CN
                  Spanish - es
                  Swedish - sv
                  Traditional Chinese - zh-TW
                  Turkish - tr
                  Greek - el
                  Hebrew - he


        :return: The configuration_map of this ConfigurationDetails.
        :rtype: dict(str, str)
        """
        return self._configuration_map

    @configuration_map.setter
    def configuration_map(self, configuration_map):
        """
        Sets the configuration_map of this ConfigurationDetails.
        model configuration details
        For PII : ConfigurationDetails will be PiiEntityMasking can be anyone of the following
        ex.{ \"mode\" : \"MASK\",\"maskingCharacter\" : \"&\",\"leaveCharactersUnmasked\": 3,\"isUnmaskedFromEnd\" : true  }
           { \"mode\" : \"MASK\",\"replaceWith\" : \"&\"  }
           { \"mode\" : \"REPLACE\" }
        For language translation :  { \"languageCodes\" : [\"cs\", \"ar\"]}
        Language code supported
                  Automatically detect language - auto
                  Arabic - ar
                  Brazilian Portuguese -  pt-BR
                  Czech - cs
                  Danish - da
                  Dutch - nl
                  English - en
                  Finnish - fi
                  French - fr
                  Canadian French - fr-CA
                  German - de
                  Italian - it
                  Japanese - ja
                  Korean - ko
                  Norwegian - no
                  Polish - pl
                  Romanian - ro
                  Simplified Chinese - zh-CN
                  Spanish - es
                  Swedish - sv
                  Traditional Chinese - zh-TW
                  Turkish - tr
                  Greek - el
                  Hebrew - he


        :param configuration_map: The configuration_map of this ConfigurationDetails.
        :type: dict(str, str)
        """
        self._configuration_map = configuration_map

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
