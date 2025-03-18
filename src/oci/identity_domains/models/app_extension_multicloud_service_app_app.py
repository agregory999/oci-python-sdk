# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppExtensionMulticloudServiceAppApp(object):
    """
    This extension defines attributes specific to Apps that represent instances of Multicloud Service App
    """

    #: A constant which can be used with the multicloud_service_type property of a AppExtensionMulticloudServiceAppApp.
    #: This constant has a value of "AWSCognito"
    MULTICLOUD_SERVICE_TYPE_AWS_COGNITO = "AWSCognito"

    def __init__(self, **kwargs):
        """
        Initializes a new AppExtensionMulticloudServiceAppApp object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param multicloud_service_type:
            The value to assign to the multicloud_service_type property of this AppExtensionMulticloudServiceAppApp.
            Allowed values for this property are: "AWSCognito", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type multicloud_service_type: str

        :param multicloud_platform_url:
            The value to assign to the multicloud_platform_url property of this AppExtensionMulticloudServiceAppApp.
        :type multicloud_platform_url: str

        """
        self.swagger_types = {
            'multicloud_service_type': 'str',
            'multicloud_platform_url': 'str'
        }
        self.attribute_map = {
            'multicloud_service_type': 'multicloudServiceType',
            'multicloud_platform_url': 'multicloudPlatformUrl'
        }
        self._multicloud_service_type = None
        self._multicloud_platform_url = None

    @property
    def multicloud_service_type(self):
        """
        **[Required]** Gets the multicloud_service_type of this AppExtensionMulticloudServiceAppApp.
        Specifies the service type for which the application is configured for multicloud integration. For applicable external service types, app will invoke multicloud service for runtime operations

        **Added In:** 2301202328

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: request
         - type: string
         - uniqueness: none

        Allowed values for this property are: "AWSCognito", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The multicloud_service_type of this AppExtensionMulticloudServiceAppApp.
        :rtype: str
        """
        return self._multicloud_service_type

    @multicloud_service_type.setter
    def multicloud_service_type(self, multicloud_service_type):
        """
        Sets the multicloud_service_type of this AppExtensionMulticloudServiceAppApp.
        Specifies the service type for which the application is configured for multicloud integration. For applicable external service types, app will invoke multicloud service for runtime operations

        **Added In:** 2301202328

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: request
         - type: string
         - uniqueness: none


        :param multicloud_service_type: The multicloud_service_type of this AppExtensionMulticloudServiceAppApp.
        :type: str
        """
        allowed_values = ["AWSCognito"]
        if not value_allowed_none_or_none_sentinel(multicloud_service_type, allowed_values):
            multicloud_service_type = 'UNKNOWN_ENUM_VALUE'
        self._multicloud_service_type = multicloud_service_type

    @property
    def multicloud_platform_url(self):
        """
        Gets the multicloud_platform_url of this AppExtensionMulticloudServiceAppApp.
        The multicloud platform service URL which the application will invoke for runtime operations such as AWSCredentials api invocation

        **Added In:** 2301202328

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The multicloud_platform_url of this AppExtensionMulticloudServiceAppApp.
        :rtype: str
        """
        return self._multicloud_platform_url

    @multicloud_platform_url.setter
    def multicloud_platform_url(self, multicloud_platform_url):
        """
        Sets the multicloud_platform_url of this AppExtensionMulticloudServiceAppApp.
        The multicloud platform service URL which the application will invoke for runtime operations such as AWSCredentials api invocation

        **Added In:** 2301202328

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param multicloud_platform_url: The multicloud_platform_url of this AppExtensionMulticloudServiceAppApp.
        :type: str
        """
        self._multicloud_platform_url = multicloud_platform_url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
