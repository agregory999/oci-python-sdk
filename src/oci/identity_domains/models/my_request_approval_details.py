# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MyRequestApprovalDetails(object):
    """
    Approvals created for this request.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MyRequestApprovalDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param approver_id:
            The value to assign to the approver_id property of this MyRequestApprovalDetails.
        :type approver_id: str

        :param approver_display_name:
            The value to assign to the approver_display_name property of this MyRequestApprovalDetails.
        :type approver_display_name: str

        :param justification:
            The value to assign to the justification property of this MyRequestApprovalDetails.
        :type justification: str

        :param status:
            The value to assign to the status property of this MyRequestApprovalDetails.
        :type status: str

        :param order:
            The value to assign to the order property of this MyRequestApprovalDetails.
        :type order: int

        :param approval_type:
            The value to assign to the approval_type property of this MyRequestApprovalDetails.
        :type approval_type: str

        :param time_updated:
            The value to assign to the time_updated property of this MyRequestApprovalDetails.
        :type time_updated: str

        """
        self.swagger_types = {
            'approver_id': 'str',
            'approver_display_name': 'str',
            'justification': 'str',
            'status': 'str',
            'order': 'int',
            'approval_type': 'str',
            'time_updated': 'str'
        }
        self.attribute_map = {
            'approver_id': 'approverId',
            'approver_display_name': 'approverDisplayName',
            'justification': 'justification',
            'status': 'status',
            'order': 'order',
            'approval_type': 'approvalType',
            'time_updated': 'timeUpdated'
        }
        self._approver_id = None
        self._approver_display_name = None
        self._justification = None
        self._status = None
        self._order = None
        self._approval_type = None
        self._time_updated = None

    @property
    def approver_id(self):
        """
        Gets the approver_id of this MyRequestApprovalDetails.
        Approver Id

        **Added In:** 2307071836

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - returned: default
         - type: string
         - uniqueness: none
         - mutability: readOnly


        :return: The approver_id of this MyRequestApprovalDetails.
        :rtype: str
        """
        return self._approver_id

    @approver_id.setter
    def approver_id(self, approver_id):
        """
        Sets the approver_id of this MyRequestApprovalDetails.
        Approver Id

        **Added In:** 2307071836

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - returned: default
         - type: string
         - uniqueness: none
         - mutability: readOnly


        :param approver_id: The approver_id of this MyRequestApprovalDetails.
        :type: str
        """
        self._approver_id = approver_id

    @property
    def approver_display_name(self):
        """
        Gets the approver_display_name of this MyRequestApprovalDetails.
        Approver display name

        **Added In:** 2307071836

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - returned: default
         - type: string
         - uniqueness: none
         - mutability: readOnly


        :return: The approver_display_name of this MyRequestApprovalDetails.
        :rtype: str
        """
        return self._approver_display_name

    @approver_display_name.setter
    def approver_display_name(self, approver_display_name):
        """
        Sets the approver_display_name of this MyRequestApprovalDetails.
        Approver display name

        **Added In:** 2307071836

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - returned: default
         - type: string
         - uniqueness: none
         - mutability: readOnly


        :param approver_display_name: The approver_display_name of this MyRequestApprovalDetails.
        :type: str
        """
        self._approver_display_name = approver_display_name

    @property
    def justification(self):
        """
        Gets the justification of this MyRequestApprovalDetails.
        Approval Justification

        **Added In:** 2307071836

        **SCIM++ Properties:**
         - multiValued: false
         - idcsSearchable: false
         - returned: default
         - type: string
         - uniqueness: none
         - mutability: readOnly


        :return: The justification of this MyRequestApprovalDetails.
        :rtype: str
        """
        return self._justification

    @justification.setter
    def justification(self, justification):
        """
        Sets the justification of this MyRequestApprovalDetails.
        Approval Justification

        **Added In:** 2307071836

        **SCIM++ Properties:**
         - multiValued: false
         - idcsSearchable: false
         - returned: default
         - type: string
         - uniqueness: none
         - mutability: readOnly


        :param justification: The justification of this MyRequestApprovalDetails.
        :type: str
        """
        self._justification = justification

    @property
    def status(self):
        """
        Gets the status of this MyRequestApprovalDetails.
        Approval Status

        **Added In:** 2307071836

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - returned: default
         - type: string
         - uniqueness: none
         - mutability: readOnly


        :return: The status of this MyRequestApprovalDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this MyRequestApprovalDetails.
        Approval Status

        **Added In:** 2307071836

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - returned: default
         - type: string
         - uniqueness: none
         - mutability: readOnly


        :param status: The status of this MyRequestApprovalDetails.
        :type: str
        """
        self._status = status

    @property
    def order(self):
        """
        Gets the order of this MyRequestApprovalDetails.
        Approval Order

        **Added In:** 2307071836

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - returned: default
         - type: integer
         - uniqueness: none
         - mutability: readOnly


        :return: The order of this MyRequestApprovalDetails.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this MyRequestApprovalDetails.
        Approval Order

        **Added In:** 2307071836

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - returned: default
         - type: integer
         - uniqueness: none
         - mutability: readOnly


        :param order: The order of this MyRequestApprovalDetails.
        :type: int
        """
        self._order = order

    @property
    def approval_type(self):
        """
        Gets the approval_type of this MyRequestApprovalDetails.
        Approval Type (Escalation or Regular)

        **Added In:** 2307071836

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - returned: default
         - type: string
         - uniqueness: none
         - mutability: readOnly


        :return: The approval_type of this MyRequestApprovalDetails.
        :rtype: str
        """
        return self._approval_type

    @approval_type.setter
    def approval_type(self, approval_type):
        """
        Sets the approval_type of this MyRequestApprovalDetails.
        Approval Type (Escalation or Regular)

        **Added In:** 2307071836

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - returned: default
         - type: string
         - uniqueness: none
         - mutability: readOnly


        :param approval_type: The approval_type of this MyRequestApprovalDetails.
        :type: str
        """
        self._approval_type = approval_type

    @property
    def time_updated(self):
        """
        Gets the time_updated of this MyRequestApprovalDetails.
        Approval Update Time

        **Added In:** 2307071836

        **SCIM++ Properties:**
         - multiValued: false
         - idcsSearchable: false
         - returned: default
         - type: dateTime
         - uniqueness: none
         - mutability: readOnly


        :return: The time_updated of this MyRequestApprovalDetails.
        :rtype: str
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this MyRequestApprovalDetails.
        Approval Update Time

        **Added In:** 2307071836

        **SCIM++ Properties:**
         - multiValued: false
         - idcsSearchable: false
         - returned: default
         - type: dateTime
         - uniqueness: none
         - mutability: readOnly


        :param time_updated: The time_updated of this MyRequestApprovalDetails.
        :type: str
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
