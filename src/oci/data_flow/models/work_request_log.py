# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200129


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequestLog(object):
    """
    A Data Flow work request log object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequestLog object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this WorkRequestLog.
        :type id: int

        :param message:
            The value to assign to the message property of this WorkRequestLog.
        :type message: str

        :param timestamp:
            The value to assign to the timestamp property of this WorkRequestLog.
        :type timestamp: datetime

        :param work_requestid:
            The value to assign to the work_requestid property of this WorkRequestLog.
        :type work_requestid: str

        """
        self.swagger_types = {
            'id': 'int',
            'message': 'str',
            'timestamp': 'datetime',
            'work_requestid': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'message': 'message',
            'timestamp': 'timestamp',
            'work_requestid': 'workRequestid'
        }

        self._id = None
        self._message = None
        self._timestamp = None
        self._work_requestid = None

    @property
    def id(self):
        """
        Gets the id of this WorkRequestLog.
        The id of a work request log.


        :return: The id of this WorkRequestLog.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkRequestLog.
        The id of a work request log.


        :param id: The id of this WorkRequestLog.
        :type: int
        """
        self._id = id

    @property
    def message(self):
        """
        **[Required]** Gets the message of this WorkRequestLog.
        A human readable log message.


        :return: The message of this WorkRequestLog.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this WorkRequestLog.
        A human readable log message.


        :param message: The message of this WorkRequestLog.
        :type: str
        """
        self._message = message

    @property
    def timestamp(self):
        """
        **[Required]** Gets the timestamp of this WorkRequestLog.
        The time the log message was written. An RFC3339 formatted datetime string.


        :return: The timestamp of this WorkRequestLog.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this WorkRequestLog.
        The time the log message was written. An RFC3339 formatted datetime string.


        :param timestamp: The timestamp of this WorkRequestLog.
        :type: datetime
        """
        self._timestamp = timestamp

    @property
    def work_requestid(self):
        """
        Gets the work_requestid of this WorkRequestLog.
        The OCID of a work request.


        :return: The work_requestid of this WorkRequestLog.
        :rtype: str
        """
        return self._work_requestid

    @work_requestid.setter
    def work_requestid(self, work_requestid):
        """
        Sets the work_requestid of this WorkRequestLog.
        The OCID of a work request.


        :param work_requestid: The work_requestid of this WorkRequestLog.
        :type: str
        """
        self._work_requestid = work_requestid

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
