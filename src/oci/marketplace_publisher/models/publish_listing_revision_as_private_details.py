# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PublishListingRevisionAsPrivateDetails(object):
    """
    The model for an Oracle Cloud Infrastructure Marketplace Publisher publish as private listing revision.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PublishListingRevisionAsPrivateDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param allowed_tenancies:
            The value to assign to the allowed_tenancies property of this PublishListingRevisionAsPrivateDetails.
        :type allowed_tenancies: list[str]

        """
        self.swagger_types = {
            'allowed_tenancies': 'list[str]'
        }
        self.attribute_map = {
            'allowed_tenancies': 'allowedTenancies'
        }
        self._allowed_tenancies = None

    @property
    def allowed_tenancies(self):
        """
        Gets the allowed_tenancies of this PublishListingRevisionAsPrivateDetails.
        Allowed tenancies provided when a listing is published as private.


        :return: The allowed_tenancies of this PublishListingRevisionAsPrivateDetails.
        :rtype: list[str]
        """
        return self._allowed_tenancies

    @allowed_tenancies.setter
    def allowed_tenancies(self, allowed_tenancies):
        """
        Sets the allowed_tenancies of this PublishListingRevisionAsPrivateDetails.
        Allowed tenancies provided when a listing is published as private.


        :param allowed_tenancies: The allowed_tenancies of this PublishListingRevisionAsPrivateDetails.
        :type: list[str]
        """
        self._allowed_tenancies = allowed_tenancies

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
