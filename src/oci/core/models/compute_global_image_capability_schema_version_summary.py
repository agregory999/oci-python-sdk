# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputeGlobalImageCapabilitySchemaVersionSummary(object):
    """
    Summary information for a compute global image capability schema
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ComputeGlobalImageCapabilitySchemaVersionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ComputeGlobalImageCapabilitySchemaVersionSummary.
        :type name: str

        :param compute_global_image_capability_schema_id:
            The value to assign to the compute_global_image_capability_schema_id property of this ComputeGlobalImageCapabilitySchemaVersionSummary.
        :type compute_global_image_capability_schema_id: str

        :param display_name:
            The value to assign to the display_name property of this ComputeGlobalImageCapabilitySchemaVersionSummary.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this ComputeGlobalImageCapabilitySchemaVersionSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'name': 'str',
            'compute_global_image_capability_schema_id': 'str',
            'display_name': 'str',
            'time_created': 'datetime'
        }
        self.attribute_map = {
            'name': 'name',
            'compute_global_image_capability_schema_id': 'computeGlobalImageCapabilitySchemaId',
            'display_name': 'displayName',
            'time_created': 'timeCreated'
        }
        self._name = None
        self._compute_global_image_capability_schema_id = None
        self._display_name = None
        self._time_created = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ComputeGlobalImageCapabilitySchemaVersionSummary.
        The compute global image capability schema version name


        :return: The name of this ComputeGlobalImageCapabilitySchemaVersionSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ComputeGlobalImageCapabilitySchemaVersionSummary.
        The compute global image capability schema version name


        :param name: The name of this ComputeGlobalImageCapabilitySchemaVersionSummary.
        :type: str
        """
        self._name = name

    @property
    def compute_global_image_capability_schema_id(self):
        """
        **[Required]** Gets the compute_global_image_capability_schema_id of this ComputeGlobalImageCapabilitySchemaVersionSummary.
        The OCID of the compute global image capability schema


        :return: The compute_global_image_capability_schema_id of this ComputeGlobalImageCapabilitySchemaVersionSummary.
        :rtype: str
        """
        return self._compute_global_image_capability_schema_id

    @compute_global_image_capability_schema_id.setter
    def compute_global_image_capability_schema_id(self, compute_global_image_capability_schema_id):
        """
        Sets the compute_global_image_capability_schema_id of this ComputeGlobalImageCapabilitySchemaVersionSummary.
        The OCID of the compute global image capability schema


        :param compute_global_image_capability_schema_id: The compute_global_image_capability_schema_id of this ComputeGlobalImageCapabilitySchemaVersionSummary.
        :type: str
        """
        self._compute_global_image_capability_schema_id = compute_global_image_capability_schema_id

    @property
    def display_name(self):
        """
        Gets the display_name of this ComputeGlobalImageCapabilitySchemaVersionSummary.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this ComputeGlobalImageCapabilitySchemaVersionSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ComputeGlobalImageCapabilitySchemaVersionSummary.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this ComputeGlobalImageCapabilitySchemaVersionSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ComputeGlobalImageCapabilitySchemaVersionSummary.
        The date and time the compute global image capability schema version was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ComputeGlobalImageCapabilitySchemaVersionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ComputeGlobalImageCapabilitySchemaVersionSummary.
        The date and time the compute global image capability schema version was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ComputeGlobalImageCapabilitySchemaVersionSummary.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
