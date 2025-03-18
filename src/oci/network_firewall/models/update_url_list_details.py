# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateUrlListDetails(object):
    """
    The request details to be updated in the URL List for the policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateUrlListDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param urls:
            The value to assign to the urls property of this UpdateUrlListDetails.
        :type urls: list[oci.network_firewall.models.UrlPattern]

        """
        self.swagger_types = {
            'urls': 'list[UrlPattern]'
        }
        self.attribute_map = {
            'urls': 'urls'
        }
        self._urls = None

    @property
    def urls(self):
        """
        **[Required]** Gets the urls of this UpdateUrlListDetails.
        List of urls.


        :return: The urls of this UpdateUrlListDetails.
        :rtype: list[oci.network_firewall.models.UrlPattern]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """
        Sets the urls of this UpdateUrlListDetails.
        List of urls.


        :param urls: The urls of this UpdateUrlListDetails.
        :type: list[oci.network_firewall.models.UrlPattern]
        """
        self._urls = urls

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
