# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101

from .database_feature_configuration import DatabaseFeatureConfiguration
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseDiagnosticsAndManagementFeatureConfiguration(DatabaseFeatureConfiguration):
    """
    The details required to enable the Diagnostics and Management feature.
    """

    #: A constant which can be used with the license_model property of a DatabaseDiagnosticsAndManagementFeatureConfiguration.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a DatabaseDiagnosticsAndManagementFeatureConfiguration.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseDiagnosticsAndManagementFeatureConfiguration object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.DatabaseDiagnosticsAndManagementFeatureConfiguration.feature` attribute
        of this class is ``DIAGNOSTICS_AND_MANAGEMENT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param feature:
            The value to assign to the feature property of this DatabaseDiagnosticsAndManagementFeatureConfiguration.
            Allowed values for this property are: "DIAGNOSTICS_AND_MANAGEMENT", "DB_LIFECYCLE_MANAGEMENT", "SQLWATCH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type feature: str

        :param feature_status:
            The value to assign to the feature_status property of this DatabaseDiagnosticsAndManagementFeatureConfiguration.
            Allowed values for this property are: "ENABLED", "NOT_ENABLED", "UNSUPPORTED", "FAILED_ENABLING", "FAILED_DISABLING", "FAILED", "ENABLED_WITH_WARNINGS", "PENDING_DISABLE", "ENABLING", "DISABLING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type feature_status: str

        :param connector_details:
            The value to assign to the connector_details property of this DatabaseDiagnosticsAndManagementFeatureConfiguration.
        :type connector_details: oci.database_management.models.ConnectorDetails

        :param database_connection_details:
            The value to assign to the database_connection_details property of this DatabaseDiagnosticsAndManagementFeatureConfiguration.
        :type database_connection_details: oci.database_management.models.DatabaseConnectionDetails

        :param license_model:
            The value to assign to the license_model property of this DatabaseDiagnosticsAndManagementFeatureConfiguration.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type license_model: str

        """
        self.swagger_types = {
            'feature': 'str',
            'feature_status': 'str',
            'connector_details': 'ConnectorDetails',
            'database_connection_details': 'DatabaseConnectionDetails',
            'license_model': 'str'
        }
        self.attribute_map = {
            'feature': 'feature',
            'feature_status': 'featureStatus',
            'connector_details': 'connectorDetails',
            'database_connection_details': 'databaseConnectionDetails',
            'license_model': 'licenseModel'
        }
        self._feature = None
        self._feature_status = None
        self._connector_details = None
        self._database_connection_details = None
        self._license_model = None
        self._feature = 'DIAGNOSTICS_AND_MANAGEMENT'

    @property
    def license_model(self):
        """
        Gets the license_model of this DatabaseDiagnosticsAndManagementFeatureConfiguration.
        The Oracle license model that applies to the external database.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The license_model of this DatabaseDiagnosticsAndManagementFeatureConfiguration.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this DatabaseDiagnosticsAndManagementFeatureConfiguration.
        The Oracle license model that applies to the external database.


        :param license_model: The license_model of this DatabaseDiagnosticsAndManagementFeatureConfiguration.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            license_model = 'UNKNOWN_ENUM_VALUE'
        self._license_model = license_model

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
