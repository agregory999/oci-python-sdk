# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901

from .create_software_source_details import CreateSoftwareSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateVendorSoftwareSourceDetails(CreateSoftwareSourceDetails):
    """
    Provides the information used to replicated a vendor software source into another compartment (other than root).
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateVendorSoftwareSourceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.os_management_hub.models.CreateVendorSoftwareSourceDetails.software_source_type` attribute
        of this class is ``VENDOR`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateVendorSoftwareSourceDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateVendorSoftwareSourceDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateVendorSoftwareSourceDetails.
        :type description: str

        :param software_source_type:
            The value to assign to the software_source_type property of this CreateVendorSoftwareSourceDetails.
            Allowed values for this property are: "VENDOR", "CUSTOM", "VERSIONED"
        :type software_source_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateVendorSoftwareSourceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateVendorSoftwareSourceDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param origin_software_source_id:
            The value to assign to the origin_software_source_id property of this CreateVendorSoftwareSourceDetails.
        :type origin_software_source_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'software_source_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'origin_software_source_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'software_source_type': 'softwareSourceType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'origin_software_source_id': 'originSoftwareSourceId'
        }

        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._software_source_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._origin_software_source_id = None
        self._software_source_type = 'VENDOR'

    @property
    def origin_software_source_id(self):
        """
        **[Required]** Gets the origin_software_source_id of this CreateVendorSoftwareSourceDetails.
        The `OCID`__ of the vendor software source in the root compartment that is being replicated.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The origin_software_source_id of this CreateVendorSoftwareSourceDetails.
        :rtype: str
        """
        return self._origin_software_source_id

    @origin_software_source_id.setter
    def origin_software_source_id(self, origin_software_source_id):
        """
        Sets the origin_software_source_id of this CreateVendorSoftwareSourceDetails.
        The `OCID`__ of the vendor software source in the root compartment that is being replicated.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param origin_software_source_id: The origin_software_source_id of this CreateVendorSoftwareSourceDetails.
        :type: str
        """
        self._origin_software_source_id = origin_software_source_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other