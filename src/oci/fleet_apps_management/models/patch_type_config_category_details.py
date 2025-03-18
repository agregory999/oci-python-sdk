# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831

from .config_category_details import ConfigCategoryDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PatchTypeConfigCategoryDetails(ConfigCategoryDetails):
    """
    Patch Type Config Category Details.
    Defines software patch types as per product standards referred under available Patches for supported products.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PatchTypeConfigCategoryDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_apps_management.models.PatchTypeConfigCategoryDetails.config_category` attribute
        of this class is ``PATCH_TYPE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_category:
            The value to assign to the config_category property of this PatchTypeConfigCategoryDetails.
            Allowed values for this property are: "PRODUCT", "PRODUCT_STACK", "ENVIRONMENT", "PATCH_TYPE", "CREDENTIAL"
        :type config_category: str

        """
        self.swagger_types = {
            'config_category': 'str'
        }
        self.attribute_map = {
            'config_category': 'configCategory'
        }
        self._config_category = None
        self._config_category = 'PATCH_TYPE'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
