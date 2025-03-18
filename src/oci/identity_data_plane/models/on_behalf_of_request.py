# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OnBehalfOfRequest(object):
    """
    OnBehalfOfRequest model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OnBehalfOfRequest object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param request_headers:
            The value to assign to the request_headers property of this OnBehalfOfRequest.
        :type request_headers: dict(str, list[str])

        :param target_service_name:
            The value to assign to the target_service_name property of this OnBehalfOfRequest.
        :type target_service_name: str

        :param obo_token:
            The value to assign to the obo_token property of this OnBehalfOfRequest.
        :type obo_token: str

        :param expiration:
            The value to assign to the expiration property of this OnBehalfOfRequest.
        :type expiration: str

        """
        self.swagger_types = {
            'request_headers': 'dict(str, list[str])',
            'target_service_name': 'str',
            'obo_token': 'str',
            'expiration': 'str'
        }
        self.attribute_map = {
            'request_headers': 'requestHeaders',
            'target_service_name': 'targetServiceName',
            'obo_token': 'oboToken',
            'expiration': 'expiration'
        }
        self._request_headers = None
        self._target_service_name = None
        self._obo_token = None
        self._expiration = None

    @property
    def request_headers(self):
        """
        **[Required]** Gets the request_headers of this OnBehalfOfRequest.
        The signed headers of the customer call.


        :return: The request_headers of this OnBehalfOfRequest.
        :rtype: dict(str, list[str])
        """
        return self._request_headers

    @request_headers.setter
    def request_headers(self, request_headers):
        """
        Sets the request_headers of this OnBehalfOfRequest.
        The signed headers of the customer call.


        :param request_headers: The request_headers of this OnBehalfOfRequest.
        :type: dict(str, list[str])
        """
        self._request_headers = request_headers

    @property
    def target_service_name(self):
        """
        **[Required]** Gets the target_service_name of this OnBehalfOfRequest.
        The name of the target service.


        :return: The target_service_name of this OnBehalfOfRequest.
        :rtype: str
        """
        return self._target_service_name

    @target_service_name.setter
    def target_service_name(self, target_service_name):
        """
        Sets the target_service_name of this OnBehalfOfRequest.
        The name of the target service.


        :param target_service_name: The target_service_name of this OnBehalfOfRequest.
        :type: str
        """
        self._target_service_name = target_service_name

    @property
    def obo_token(self):
        """
        Gets the obo_token of this OnBehalfOfRequest.
        If you have an obo token already, exchange that for a new obo token.


        :return: The obo_token of this OnBehalfOfRequest.
        :rtype: str
        """
        return self._obo_token

    @obo_token.setter
    def obo_token(self, obo_token):
        """
        Sets the obo_token of this OnBehalfOfRequest.
        If you have an obo token already, exchange that for a new obo token.


        :param obo_token: The obo_token of this OnBehalfOfRequest.
        :type: str
        """
        self._obo_token = obo_token

    @property
    def expiration(self):
        """
        Gets the expiration of this OnBehalfOfRequest.
        A duration for which the obo token is requested to be valid.


        :return: The expiration of this OnBehalfOfRequest.
        :rtype: str
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """
        Sets the expiration of this OnBehalfOfRequest.
        A duration for which the obo token is requested to be valid.


        :param expiration: The expiration of this OnBehalfOfRequest.
        :type: str
        """
        self._expiration = expiration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
