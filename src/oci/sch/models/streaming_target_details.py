# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200909

from .target_details import TargetDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StreamingTargetDetails(TargetDetails):
    """
    The destination stream for data transferred from the source.
    For configuration instructions, see
    `Creating a Connector`__.

    __ https://docs.cloud.oracle.com/iaas/Content/connector-hub/create-service-connector.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StreamingTargetDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.sch.models.StreamingTargetDetails.kind` attribute
        of this class is ``streaming`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this StreamingTargetDetails.
            Allowed values for this property are: "functions", "loggingAnalytics", "monitoring", "notifications", "objectStorage", "streaming"
        :type kind: str

        :param stream_id:
            The value to assign to the stream_id property of this StreamingTargetDetails.
        :type stream_id: str

        """
        self.swagger_types = {
            'kind': 'str',
            'stream_id': 'str'
        }
        self.attribute_map = {
            'kind': 'kind',
            'stream_id': 'streamId'
        }
        self._kind = None
        self._stream_id = None
        self._kind = 'streaming'

    @property
    def stream_id(self):
        """
        **[Required]** Gets the stream_id of this StreamingTargetDetails.
        The `OCID`__ of the stream.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The stream_id of this StreamingTargetDetails.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """
        Sets the stream_id of this StreamingTargetDetails.
        The `OCID`__ of the stream.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param stream_id: The stream_id of this StreamingTargetDetails.
        :type: str
        """
        self._stream_id = stream_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
