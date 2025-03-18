# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230801


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DelegationControlResourceSummary(object):
    """
    Details of the resources that this Delegation Control is applicable to.
    """

    #: A constant which can be used with the resource_status property of a DelegationControlResourceSummary.
    #: This constant has a value of "CREATED"
    RESOURCE_STATUS_CREATED = "CREATED"

    #: A constant which can be used with the resource_status property of a DelegationControlResourceSummary.
    #: This constant has a value of "APPLYING"
    RESOURCE_STATUS_APPLYING = "APPLYING"

    #: A constant which can be used with the resource_status property of a DelegationControlResourceSummary.
    #: This constant has a value of "APPLIED"
    RESOURCE_STATUS_APPLIED = "APPLIED"

    #: A constant which can be used with the resource_status property of a DelegationControlResourceSummary.
    #: This constant has a value of "APPLY_FAILED"
    RESOURCE_STATUS_APPLY_FAILED = "APPLY_FAILED"

    #: A constant which can be used with the resource_status property of a DelegationControlResourceSummary.
    #: This constant has a value of "UPDATING"
    RESOURCE_STATUS_UPDATING = "UPDATING"

    #: A constant which can be used with the resource_status property of a DelegationControlResourceSummary.
    #: This constant has a value of "UPDATE_FAILED"
    RESOURCE_STATUS_UPDATE_FAILED = "UPDATE_FAILED"

    #: A constant which can be used with the resource_status property of a DelegationControlResourceSummary.
    #: This constant has a value of "DELETING"
    RESOURCE_STATUS_DELETING = "DELETING"

    #: A constant which can be used with the resource_status property of a DelegationControlResourceSummary.
    #: This constant has a value of "DELETED"
    RESOURCE_STATUS_DELETED = "DELETED"

    #: A constant which can be used with the resource_status property of a DelegationControlResourceSummary.
    #: This constant has a value of "DELETION_FAILED"
    RESOURCE_STATUS_DELETION_FAILED = "DELETION_FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DelegationControlResourceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DelegationControlResourceSummary.
        :type id: str

        :param resource_status:
            The value to assign to the resource_status property of this DelegationControlResourceSummary.
            Allowed values for this property are: "CREATED", "APPLYING", "APPLIED", "APPLY_FAILED", "UPDATING", "UPDATE_FAILED", "DELETING", "DELETED", "DELETION_FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_status: str

        """
        self.swagger_types = {
            'id': 'str',
            'resource_status': 'str'
        }
        self.attribute_map = {
            'id': 'id',
            'resource_status': 'resourceStatus'
        }
        self._id = None
        self._resource_status = None

    @property
    def id(self):
        """
        Gets the id of this DelegationControlResourceSummary.
        OCID of the resource.


        :return: The id of this DelegationControlResourceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DelegationControlResourceSummary.
        OCID of the resource.


        :param id: The id of this DelegationControlResourceSummary.
        :type: str
        """
        self._id = id

    @property
    def resource_status(self):
        """
        Gets the resource_status of this DelegationControlResourceSummary.
        The current status of the resource in Delegation Control.

        Allowed values for this property are: "CREATED", "APPLYING", "APPLIED", "APPLY_FAILED", "UPDATING", "UPDATE_FAILED", "DELETING", "DELETED", "DELETION_FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The resource_status of this DelegationControlResourceSummary.
        :rtype: str
        """
        return self._resource_status

    @resource_status.setter
    def resource_status(self, resource_status):
        """
        Sets the resource_status of this DelegationControlResourceSummary.
        The current status of the resource in Delegation Control.


        :param resource_status: The resource_status of this DelegationControlResourceSummary.
        :type: str
        """
        allowed_values = ["CREATED", "APPLYING", "APPLIED", "APPLY_FAILED", "UPDATING", "UPDATE_FAILED", "DELETING", "DELETED", "DELETION_FAILED"]
        if not value_allowed_none_or_none_sentinel(resource_status, allowed_values):
            resource_status = 'UNKNOWN_ENUM_VALUE'
        self._resource_status = resource_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
