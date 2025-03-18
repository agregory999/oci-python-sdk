# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630

from .configuration_items_collection import ConfigurationItemsCollection
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UxConfigurationItemsCollection(ConfigurationItemsCollection):
    """
    Collection of ux configuration item summary objects.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UxConfigurationItemsCollection object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.UxConfigurationItemsCollection.opsi_config_type` attribute
        of this class is ``UX_CONFIGURATION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param opsi_config_type:
            The value to assign to the opsi_config_type property of this UxConfigurationItemsCollection.
            Allowed values for this property are: "UX_CONFIGURATION"
        :type opsi_config_type: str

        :param config_items:
            The value to assign to the config_items property of this UxConfigurationItemsCollection.
        :type config_items: list[oci.opsi.models.ConfigurationItemSummary]

        """
        self.swagger_types = {
            'opsi_config_type': 'str',
            'config_items': 'list[ConfigurationItemSummary]'
        }
        self.attribute_map = {
            'opsi_config_type': 'opsiConfigType',
            'config_items': 'configItems'
        }
        self._opsi_config_type = None
        self._config_items = None
        self._opsi_config_type = 'UX_CONFIGURATION'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
