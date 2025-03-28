# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MergeCheckCollection(object):
    """
    list of merge checks.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MergeCheckCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this MergeCheckCollection.
        :type items: list[oci.devops.models.MergeCheck]

        :param time_validated:
            The value to assign to the time_validated property of this MergeCheckCollection.
        :type time_validated: datetime

        """
        self.swagger_types = {
            'items': 'list[MergeCheck]',
            'time_validated': 'datetime'
        }
        self.attribute_map = {
            'items': 'items',
            'time_validated': 'timeValidated'
        }
        self._items = None
        self._time_validated = None

    @property
    def items(self):
        """
        Gets the items of this MergeCheckCollection.
        List of pullRequest mergeCheck objects.
         Example: {\"items\": [{ \"type\" : \"CONFLICT(ENUM values)\",
                                           \"status\" : \"FAILED(ENUM values)\"},
                                        {\"type\": \"APPROVAL_RULE(ENUM VALUE)\",
                                          \"ruleName\": \"rule 1\",
                                          \"status\" : \"NEEDS_APPROVAL(ENUM values)\",
                                          \"totalApprovalCount\":\"5\",
                                          \"currentApprovalCount\":\"1\",
                                          \"reviewers\":[<Reviewer OCID>],
                                          \"level\": \"PROJECT/REPOSITORY(ENUM values)\"},
                                        {\"type\": \"APPROVAL_RULE(ENUM VALUE)\",
                                          \"ruleName\": \"rule 2\",
                                        \"status\" : \"SUCCEEDED(ENUM values)\",
                                        \"totalApprovalCount\":\"5\",
                                        \"currentApprovalCount\":\"5\",
                                        \"reviewers\":[<Reviewer OCID>],
                                        \"level\": \"PROJECT/REPOSITORY(ENUM values)\"} ,
                                        {\"type\": \"BUILD(ENUM VALUE)\",
                                         \"pipelineId\": \"PipelineOCID\",
                                         \"buildRunId\": \"BuildRunOCID\",
                                         \"status\" : \"SUCCEEDED/PENDING/FAIlED/IN-PROGRESS(ENUM values)\"}
        ]}


        :return: The items of this MergeCheckCollection.
        :rtype: list[oci.devops.models.MergeCheck]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this MergeCheckCollection.
        List of pullRequest mergeCheck objects.
         Example: {\"items\": [{ \"type\" : \"CONFLICT(ENUM values)\",
                                           \"status\" : \"FAILED(ENUM values)\"},
                                        {\"type\": \"APPROVAL_RULE(ENUM VALUE)\",
                                          \"ruleName\": \"rule 1\",
                                          \"status\" : \"NEEDS_APPROVAL(ENUM values)\",
                                          \"totalApprovalCount\":\"5\",
                                          \"currentApprovalCount\":\"1\",
                                          \"reviewers\":[<Reviewer OCID>],
                                          \"level\": \"PROJECT/REPOSITORY(ENUM values)\"},
                                        {\"type\": \"APPROVAL_RULE(ENUM VALUE)\",
                                          \"ruleName\": \"rule 2\",
                                        \"status\" : \"SUCCEEDED(ENUM values)\",
                                        \"totalApprovalCount\":\"5\",
                                        \"currentApprovalCount\":\"5\",
                                        \"reviewers\":[<Reviewer OCID>],
                                        \"level\": \"PROJECT/REPOSITORY(ENUM values)\"} ,
                                        {\"type\": \"BUILD(ENUM VALUE)\",
                                         \"pipelineId\": \"PipelineOCID\",
                                         \"buildRunId\": \"BuildRunOCID\",
                                         \"status\" : \"SUCCEEDED/PENDING/FAIlED/IN-PROGRESS(ENUM values)\"}
        ]}


        :param items: The items of this MergeCheckCollection.
        :type: list[oci.devops.models.MergeCheck]
        """
        self._items = items

    @property
    def time_validated(self):
        """
        Gets the time_validated of this MergeCheckCollection.
        The time Stamp of the validation check.


        :return: The time_validated of this MergeCheckCollection.
        :rtype: datetime
        """
        return self._time_validated

    @time_validated.setter
    def time_validated(self, time_validated):
        """
        Sets the time_validated of this MergeCheckCollection.
        The time Stamp of the validation check.


        :param time_validated: The time_validated of this MergeCheckCollection.
        :type: datetime
        """
        self._time_validated = time_validated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
