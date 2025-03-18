# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230518

from .host_dump_transfer_details import HostDumpTransferDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CurlTransferDetails(HostDumpTransferDetails):
    """
    Optional properties for Curl-based dump transfer in source or target host.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CurlTransferDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_migration.models.CurlTransferDetails.kind` attribute
        of this class is ``CURL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param wallet_location:
            The value to assign to the wallet_location property of this CurlTransferDetails.
        :type wallet_location: str

        :param kind:
            The value to assign to the kind property of this CurlTransferDetails.
            Allowed values for this property are: "CURL", "OCI_CLI"
        :type kind: str

        """
        self.swagger_types = {
            'wallet_location': 'str',
            'kind': 'str'
        }
        self.attribute_map = {
            'wallet_location': 'walletLocation',
            'kind': 'kind'
        }
        self._wallet_location = None
        self._kind = None
        self._kind = 'CURL'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
