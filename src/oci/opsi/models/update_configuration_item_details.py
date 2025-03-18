# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateConfigurationItemDetails(object):
    """
    Configuration item details for OPSI configuration update.
    """

    #: A constant which can be used with the config_item_type property of a UpdateConfigurationItemDetails.
    #: This constant has a value of "BASIC"
    CONFIG_ITEM_TYPE_BASIC = "BASIC"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateConfigurationItemDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.opsi.models.UpdateBasicConfigurationItemDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_item_type:
            The value to assign to the config_item_type property of this UpdateConfigurationItemDetails.
            Allowed values for this property are: "BASIC"
        :type config_item_type: str

        """
        self.swagger_types = {
            'config_item_type': 'str'
        }
        self.attribute_map = {
            'config_item_type': 'configItemType'
        }
        self._config_item_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['configItemType']

        if type == 'BASIC':
            return 'UpdateBasicConfigurationItemDetails'
        else:
            return 'UpdateConfigurationItemDetails'

    @property
    def config_item_type(self):
        """
        **[Required]** Gets the config_item_type of this UpdateConfigurationItemDetails.
        Type of configuration item.

        Allowed values for this property are: "BASIC"


        :return: The config_item_type of this UpdateConfigurationItemDetails.
        :rtype: str
        """
        return self._config_item_type

    @config_item_type.setter
    def config_item_type(self, config_item_type):
        """
        Sets the config_item_type of this UpdateConfigurationItemDetails.
        Type of configuration item.


        :param config_item_type: The config_item_type of this UpdateConfigurationItemDetails.
        :type: str
        """
        allowed_values = ["BASIC"]
        if not value_allowed_none_or_none_sentinel(config_item_type, allowed_values):
            raise ValueError(
                f"Invalid value for `config_item_type`, must be None or one of {allowed_values}"
            )
        self._config_item_type = config_item_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
