# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateJobDetails(object):
    """
    The details required to update a job.
    """

    #: A constant which can be used with the job_type property of a UpdateJobDetails.
    #: This constant has a value of "SQL"
    JOB_TYPE_SQL = "SQL"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateJobDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_management.models.UpdateSqlJobDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateJobDetails.
        :type description: str

        :param job_type:
            The value to assign to the job_type property of this UpdateJobDetails.
            Allowed values for this property are: "SQL"
        :type job_type: str

        :param timeout:
            The value to assign to the timeout property of this UpdateJobDetails.
        :type timeout: str

        :param result_location:
            The value to assign to the result_location property of this UpdateJobDetails.
        :type result_location: oci.database_management.models.JobExecutionResultLocation

        :param schedule_details:
            The value to assign to the schedule_details property of this UpdateJobDetails.
        :type schedule_details: oci.database_management.models.JobScheduleDetails

        """
        self.swagger_types = {
            'description': 'str',
            'job_type': 'str',
            'timeout': 'str',
            'result_location': 'JobExecutionResultLocation',
            'schedule_details': 'JobScheduleDetails'
        }
        self.attribute_map = {
            'description': 'description',
            'job_type': 'jobType',
            'timeout': 'timeout',
            'result_location': 'resultLocation',
            'schedule_details': 'scheduleDetails'
        }
        self._description = None
        self._job_type = None
        self._timeout = None
        self._result_location = None
        self._schedule_details = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['jobType']

        if type == 'SQL':
            return 'UpdateSqlJobDetails'
        else:
            return 'UpdateJobDetails'

    @property
    def description(self):
        """
        Gets the description of this UpdateJobDetails.
        The description of the job.


        :return: The description of this UpdateJobDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateJobDetails.
        The description of the job.


        :param description: The description of this UpdateJobDetails.
        :type: str
        """
        self._description = description

    @property
    def job_type(self):
        """
        Gets the job_type of this UpdateJobDetails.
        The type of job.

        Allowed values for this property are: "SQL"


        :return: The job_type of this UpdateJobDetails.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """
        Sets the job_type of this UpdateJobDetails.
        The type of job.


        :param job_type: The job_type of this UpdateJobDetails.
        :type: str
        """
        allowed_values = ["SQL"]
        if not value_allowed_none_or_none_sentinel(job_type, allowed_values):
            raise ValueError(
                f"Invalid value for `job_type`, must be None or one of {allowed_values}"
            )
        self._job_type = job_type

    @property
    def timeout(self):
        """
        Gets the timeout of this UpdateJobDetails.
        The job timeout duration, which is expressed like \"1h 10m 15s\".


        :return: The timeout of this UpdateJobDetails.
        :rtype: str
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """
        Sets the timeout of this UpdateJobDetails.
        The job timeout duration, which is expressed like \"1h 10m 15s\".


        :param timeout: The timeout of this UpdateJobDetails.
        :type: str
        """
        self._timeout = timeout

    @property
    def result_location(self):
        """
        Gets the result_location of this UpdateJobDetails.

        :return: The result_location of this UpdateJobDetails.
        :rtype: oci.database_management.models.JobExecutionResultLocation
        """
        return self._result_location

    @result_location.setter
    def result_location(self, result_location):
        """
        Sets the result_location of this UpdateJobDetails.

        :param result_location: The result_location of this UpdateJobDetails.
        :type: oci.database_management.models.JobExecutionResultLocation
        """
        self._result_location = result_location

    @property
    def schedule_details(self):
        """
        Gets the schedule_details of this UpdateJobDetails.

        :return: The schedule_details of this UpdateJobDetails.
        :rtype: oci.database_management.models.JobScheduleDetails
        """
        return self._schedule_details

    @schedule_details.setter
    def schedule_details(self, schedule_details):
        """
        Sets the schedule_details of this UpdateJobDetails.

        :param schedule_details: The schedule_details of this UpdateJobDetails.
        :type: oci.database_management.models.JobScheduleDetails
        """
        self._schedule_details = schedule_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
