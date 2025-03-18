# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PatchProduct(object):
    """
    Product
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PatchProduct object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param platform_configuration_id:
            The value to assign to the platform_configuration_id property of this PatchProduct.
        :type platform_configuration_id: str

        :param version:
            The value to assign to the version property of this PatchProduct.
        :type version: str

        """
        self.swagger_types = {
            'platform_configuration_id': 'str',
            'version': 'str'
        }
        self.attribute_map = {
            'platform_configuration_id': 'platformConfigurationId',
            'version': 'version'
        }
        self._platform_configuration_id = None
        self._version = None

    @property
    def platform_configuration_id(self):
        """
        **[Required]** Gets the platform_configuration_id of this PatchProduct.
        PlatformConfiguration Id corresponding to the Product


        :return: The platform_configuration_id of this PatchProduct.
        :rtype: str
        """
        return self._platform_configuration_id

    @platform_configuration_id.setter
    def platform_configuration_id(self, platform_configuration_id):
        """
        Sets the platform_configuration_id of this PatchProduct.
        PlatformConfiguration Id corresponding to the Product


        :param platform_configuration_id: The platform_configuration_id of this PatchProduct.
        :type: str
        """
        self._platform_configuration_id = platform_configuration_id

    @property
    def version(self):
        """
        Gets the version of this PatchProduct.
        product version.


        :return: The version of this PatchProduct.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this PatchProduct.
        product version.


        :param version: The version of this PatchProduct.
        :type: str
        """
        self._version = version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
