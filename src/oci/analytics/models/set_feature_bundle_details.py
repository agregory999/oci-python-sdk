# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190331


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SetFeatureBundleDetails(object):
    """
    Input payload for the feature set of an Analytics instance.
    """

    #: A constant which can be used with the feature_bundle property of a SetFeatureBundleDetails.
    #: This constant has a value of "FAW_PAID"
    FEATURE_BUNDLE_FAW_PAID = "FAW_PAID"

    #: A constant which can be used with the feature_bundle property of a SetFeatureBundleDetails.
    #: This constant has a value of "FAW_FREE"
    FEATURE_BUNDLE_FAW_FREE = "FAW_FREE"

    #: A constant which can be used with the feature_bundle property of a SetFeatureBundleDetails.
    #: This constant has a value of "EE_EMBEDDED"
    FEATURE_BUNDLE_EE_EMBEDDED = "EE_EMBEDDED"

    #: A constant which can be used with the feature_bundle property of a SetFeatureBundleDetails.
    #: This constant has a value of "SE_EMBEDDED"
    FEATURE_BUNDLE_SE_EMBEDDED = "SE_EMBEDDED"

    def __init__(self, **kwargs):
        """
        Initializes a new SetFeatureBundleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param feature_bundle:
            The value to assign to the feature_bundle property of this SetFeatureBundleDetails.
            Allowed values for this property are: "FAW_PAID", "FAW_FREE", "EE_EMBEDDED", "SE_EMBEDDED"
        :type feature_bundle: str

        """
        self.swagger_types = {
            'feature_bundle': 'str'
        }
        self.attribute_map = {
            'feature_bundle': 'featureBundle'
        }
        self._feature_bundle = None

    @property
    def feature_bundle(self):
        """
        Gets the feature_bundle of this SetFeatureBundleDetails.
        The feature set of an Analytics instance.

        Allowed values for this property are: "FAW_PAID", "FAW_FREE", "EE_EMBEDDED", "SE_EMBEDDED"


        :return: The feature_bundle of this SetFeatureBundleDetails.
        :rtype: str
        """
        return self._feature_bundle

    @feature_bundle.setter
    def feature_bundle(self, feature_bundle):
        """
        Sets the feature_bundle of this SetFeatureBundleDetails.
        The feature set of an Analytics instance.


        :param feature_bundle: The feature_bundle of this SetFeatureBundleDetails.
        :type: str
        """
        allowed_values = ["FAW_PAID", "FAW_FREE", "EE_EMBEDDED", "SE_EMBEDDED"]
        if not value_allowed_none_or_none_sentinel(feature_bundle, allowed_values):
            raise ValueError(
                f"Invalid value for `feature_bundle`, must be None or one of {allowed_values}"
            )
        self._feature_bundle = feature_bundle

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
