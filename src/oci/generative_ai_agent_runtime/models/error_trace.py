# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531

from .trace import Trace
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ErrorTrace(Trace):
    """
    The trace information about the error.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ErrorTrace object with values from keyword arguments. The default value of the :py:attr:`~oci.generative_ai_agent_runtime.models.ErrorTrace.trace_type` attribute
        of this class is ``ERROR_TRACE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_created:
            The value to assign to the time_created property of this ErrorTrace.
        :type time_created: datetime

        :param trace_type:
            The value to assign to the trace_type property of this ErrorTrace.
            Allowed values for this property are: "ERROR_TRACE", "RETRIEVAL_TRACE", "GENERATION_TRACE"
        :type trace_type: str

        :param error_message:
            The value to assign to the error_message property of this ErrorTrace.
        :type error_message: str

        """
        self.swagger_types = {
            'time_created': 'datetime',
            'trace_type': 'str',
            'error_message': 'str'
        }
        self.attribute_map = {
            'time_created': 'timeCreated',
            'trace_type': 'traceType',
            'error_message': 'errorMessage'
        }
        self._time_created = None
        self._trace_type = None
        self._error_message = None
        self._trace_type = 'ERROR_TRACE'

    @property
    def error_message(self):
        """
        Gets the error_message of this ErrorTrace.
        The error message in this trace.


        :return: The error_message of this ErrorTrace.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this ErrorTrace.
        The error message in this trace.


        :param error_message: The error_message of this ErrorTrace.
        :type: str
        """
        self._error_message = error_message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
