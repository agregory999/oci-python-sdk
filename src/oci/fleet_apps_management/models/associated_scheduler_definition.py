# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AssociatedSchedulerDefinition(object):
    """
    SchedulerDefinition  associated with the job.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AssociatedSchedulerDefinition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AssociatedSchedulerDefinition.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this AssociatedSchedulerDefinition.
        :type display_name: str

        :param tenancy_id:
            The value to assign to the tenancy_id property of this AssociatedSchedulerDefinition.
        :type tenancy_id: str

        :param is_recurring:
            The value to assign to the is_recurring property of this AssociatedSchedulerDefinition.
        :type is_recurring: bool

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'tenancy_id': 'str',
            'is_recurring': 'bool'
        }
        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'tenancy_id': 'tenancyId',
            'is_recurring': 'isRecurring'
        }
        self._id = None
        self._display_name = None
        self._tenancy_id = None
        self._is_recurring = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AssociatedSchedulerDefinition.
        The OCID of the resource.


        :return: The id of this AssociatedSchedulerDefinition.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AssociatedSchedulerDefinition.
        The OCID of the resource.


        :param id: The id of this AssociatedSchedulerDefinition.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AssociatedSchedulerDefinition.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this AssociatedSchedulerDefinition.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AssociatedSchedulerDefinition.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this AssociatedSchedulerDefinition.
        :type: str
        """
        self._display_name = display_name

    @property
    def tenancy_id(self):
        """
        **[Required]** Gets the tenancy_id of this AssociatedSchedulerDefinition.
        OCID of the tenancy to which the resource belongs to.


        :return: The tenancy_id of this AssociatedSchedulerDefinition.
        :rtype: str
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        """
        Sets the tenancy_id of this AssociatedSchedulerDefinition.
        OCID of the tenancy to which the resource belongs to.


        :param tenancy_id: The tenancy_id of this AssociatedSchedulerDefinition.
        :type: str
        """
        self._tenancy_id = tenancy_id

    @property
    def is_recurring(self):
        """
        **[Required]** Gets the is_recurring of this AssociatedSchedulerDefinition.
        Is this a recurring schedule?


        :return: The is_recurring of this AssociatedSchedulerDefinition.
        :rtype: bool
        """
        return self._is_recurring

    @is_recurring.setter
    def is_recurring(self, is_recurring):
        """
        Sets the is_recurring of this AssociatedSchedulerDefinition.
        Is this a recurring schedule?


        :param is_recurring: The is_recurring of this AssociatedSchedulerDefinition.
        :type: bool
        """
        self._is_recurring = is_recurring

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
