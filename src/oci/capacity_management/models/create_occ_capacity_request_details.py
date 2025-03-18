# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231107


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOccCapacityRequestDetails(object):
    """
    Details about the create request for the capacity request.
    """

    #: A constant which can be used with the namespace property of a CreateOccCapacityRequestDetails.
    #: This constant has a value of "COMPUTE"
    NAMESPACE_COMPUTE = "COMPUTE"

    #: A constant which can be used with the request_state property of a CreateOccCapacityRequestDetails.
    #: This constant has a value of "CREATED"
    REQUEST_STATE_CREATED = "CREATED"

    #: A constant which can be used with the request_state property of a CreateOccCapacityRequestDetails.
    #: This constant has a value of "SUBMITTED"
    REQUEST_STATE_SUBMITTED = "SUBMITTED"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOccCapacityRequestDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateOccCapacityRequestDetails.
        :type compartment_id: str

        :param occ_availability_catalog_id:
            The value to assign to the occ_availability_catalog_id property of this CreateOccCapacityRequestDetails.
        :type occ_availability_catalog_id: str

        :param namespace:
            The value to assign to the namespace property of this CreateOccCapacityRequestDetails.
            Allowed values for this property are: "COMPUTE"
        :type namespace: str

        :param region:
            The value to assign to the region property of this CreateOccCapacityRequestDetails.
        :type region: str

        :param display_name:
            The value to assign to the display_name property of this CreateOccCapacityRequestDetails.
        :type display_name: str

        :param request_type:
            The value to assign to the request_type property of this CreateOccCapacityRequestDetails.
        :type request_type: str

        :param description:
            The value to assign to the description property of this CreateOccCapacityRequestDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateOccCapacityRequestDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateOccCapacityRequestDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this CreateOccCapacityRequestDetails.
        :type lifecycle_details: str

        :param availability_domain:
            The value to assign to the availability_domain property of this CreateOccCapacityRequestDetails.
        :type availability_domain: str

        :param date_expected_capacity_handover:
            The value to assign to the date_expected_capacity_handover property of this CreateOccCapacityRequestDetails.
        :type date_expected_capacity_handover: datetime

        :param request_state:
            The value to assign to the request_state property of this CreateOccCapacityRequestDetails.
            Allowed values for this property are: "CREATED", "SUBMITTED"
        :type request_state: str

        :param details:
            The value to assign to the details property of this CreateOccCapacityRequestDetails.
        :type details: list[oci.capacity_management.models.OccCapacityRequestBaseDetails]

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'occ_availability_catalog_id': 'str',
            'namespace': 'str',
            'region': 'str',
            'display_name': 'str',
            'request_type': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'lifecycle_details': 'str',
            'availability_domain': 'str',
            'date_expected_capacity_handover': 'datetime',
            'request_state': 'str',
            'details': 'list[OccCapacityRequestBaseDetails]'
        }
        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'occ_availability_catalog_id': 'occAvailabilityCatalogId',
            'namespace': 'namespace',
            'region': 'region',
            'display_name': 'displayName',
            'request_type': 'requestType',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'lifecycle_details': 'lifecycleDetails',
            'availability_domain': 'availabilityDomain',
            'date_expected_capacity_handover': 'dateExpectedCapacityHandover',
            'request_state': 'requestState',
            'details': 'details'
        }
        self._compartment_id = None
        self._occ_availability_catalog_id = None
        self._namespace = None
        self._region = None
        self._display_name = None
        self._request_type = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._lifecycle_details = None
        self._availability_domain = None
        self._date_expected_capacity_handover = None
        self._request_state = None
        self._details = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateOccCapacityRequestDetails.
        Since all resources are at tenancy level hence this will be the ocid of the tenancy where operation is to be performed.


        :return: The compartment_id of this CreateOccCapacityRequestDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateOccCapacityRequestDetails.
        Since all resources are at tenancy level hence this will be the ocid of the tenancy where operation is to be performed.


        :param compartment_id: The compartment_id of this CreateOccCapacityRequestDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def occ_availability_catalog_id(self):
        """
        Gets the occ_availability_catalog_id of this CreateOccCapacityRequestDetails.
        The OCID of the availability catalog against which capacity request is made.


        :return: The occ_availability_catalog_id of this CreateOccCapacityRequestDetails.
        :rtype: str
        """
        return self._occ_availability_catalog_id

    @occ_availability_catalog_id.setter
    def occ_availability_catalog_id(self, occ_availability_catalog_id):
        """
        Sets the occ_availability_catalog_id of this CreateOccCapacityRequestDetails.
        The OCID of the availability catalog against which capacity request is made.


        :param occ_availability_catalog_id: The occ_availability_catalog_id of this CreateOccCapacityRequestDetails.
        :type: str
        """
        self._occ_availability_catalog_id = occ_availability_catalog_id

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this CreateOccCapacityRequestDetails.
        The name of the OCI service in consideration. For example, Compute, Exadata, and so on.

        Allowed values for this property are: "COMPUTE"


        :return: The namespace of this CreateOccCapacityRequestDetails.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this CreateOccCapacityRequestDetails.
        The name of the OCI service in consideration. For example, Compute, Exadata, and so on.


        :param namespace: The namespace of this CreateOccCapacityRequestDetails.
        :type: str
        """
        allowed_values = ["COMPUTE"]
        if not value_allowed_none_or_none_sentinel(namespace, allowed_values):
            raise ValueError(
                f"Invalid value for `namespace`, must be None or one of {allowed_values}"
            )
        self._namespace = namespace

    @property
    def region(self):
        """
        **[Required]** Gets the region of this CreateOccCapacityRequestDetails.
        The name of the region for which the capacity request is made.


        :return: The region of this CreateOccCapacityRequestDetails.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this CreateOccCapacityRequestDetails.
        The name of the region for which the capacity request is made.


        :param region: The region of this CreateOccCapacityRequestDetails.
        :type: str
        """
        self._region = region

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateOccCapacityRequestDetails.
        An user-friendly name for the capacity request. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateOccCapacityRequestDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateOccCapacityRequestDetails.
        An user-friendly name for the capacity request. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateOccCapacityRequestDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def request_type(self):
        """
        Gets the request_type of this CreateOccCapacityRequestDetails.
        Type of Capacity Request(New or Transfer)


        :return: The request_type of this CreateOccCapacityRequestDetails.
        :rtype: str
        """
        return self._request_type

    @request_type.setter
    def request_type(self, request_type):
        """
        Sets the request_type of this CreateOccCapacityRequestDetails.
        Type of Capacity Request(New or Transfer)


        :param request_type: The request_type of this CreateOccCapacityRequestDetails.
        :type: str
        """
        self._request_type = request_type

    @property
    def description(self):
        """
        Gets the description of this CreateOccCapacityRequestDetails.
        Meaningful text about the capacity request.


        :return: The description of this CreateOccCapacityRequestDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateOccCapacityRequestDetails.
        Meaningful text about the capacity request.


        :param description: The description of this CreateOccCapacityRequestDetails.
        :type: str
        """
        self._description = description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateOccCapacityRequestDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateOccCapacityRequestDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateOccCapacityRequestDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateOccCapacityRequestDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateOccCapacityRequestDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateOccCapacityRequestDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateOccCapacityRequestDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateOccCapacityRequestDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this CreateOccCapacityRequestDetails.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed State.


        :return: The lifecycle_details of this CreateOccCapacityRequestDetails.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this CreateOccCapacityRequestDetails.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed State.


        :param lifecycle_details: The lifecycle_details of this CreateOccCapacityRequestDetails.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this CreateOccCapacityRequestDetails.
        The availability domain (AD) in which the new resource is to be placed. If this is specified then the capacity will be validated and fulfilled within the scope of this AD. Note that this field is NOT required for Capacity request Transfer requests.


        :return: The availability_domain of this CreateOccCapacityRequestDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CreateOccCapacityRequestDetails.
        The availability domain (AD) in which the new resource is to be placed. If this is specified then the capacity will be validated and fulfilled within the scope of this AD. Note that this field is NOT required for Capacity request Transfer requests.


        :param availability_domain: The availability_domain of this CreateOccCapacityRequestDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def date_expected_capacity_handover(self):
        """
        **[Required]** Gets the date_expected_capacity_handover of this CreateOccCapacityRequestDetails.
        The date by which the capacity requested by customers before dateFinalCustomerOrder needs to be fulfilled.


        :return: The date_expected_capacity_handover of this CreateOccCapacityRequestDetails.
        :rtype: datetime
        """
        return self._date_expected_capacity_handover

    @date_expected_capacity_handover.setter
    def date_expected_capacity_handover(self, date_expected_capacity_handover):
        """
        Sets the date_expected_capacity_handover of this CreateOccCapacityRequestDetails.
        The date by which the capacity requested by customers before dateFinalCustomerOrder needs to be fulfilled.


        :param date_expected_capacity_handover: The date_expected_capacity_handover of this CreateOccCapacityRequestDetails.
        :type: datetime
        """
        self._date_expected_capacity_handover = date_expected_capacity_handover

    @property
    def request_state(self):
        """
        Gets the request_state of this CreateOccCapacityRequestDetails.
        The subset of request states available for creating the capacity request.

        Allowed values for this property are: "CREATED", "SUBMITTED"


        :return: The request_state of this CreateOccCapacityRequestDetails.
        :rtype: str
        """
        return self._request_state

    @request_state.setter
    def request_state(self, request_state):
        """
        Sets the request_state of this CreateOccCapacityRequestDetails.
        The subset of request states available for creating the capacity request.


        :param request_state: The request_state of this CreateOccCapacityRequestDetails.
        :type: str
        """
        allowed_values = ["CREATED", "SUBMITTED"]
        if not value_allowed_none_or_none_sentinel(request_state, allowed_values):
            raise ValueError(
                f"Invalid value for `request_state`, must be None or one of {allowed_values}"
            )
        self._request_state = request_state

    @property
    def details(self):
        """
        **[Required]** Gets the details of this CreateOccCapacityRequestDetails.
        A list of different resources requested by the user.


        :return: The details of this CreateOccCapacityRequestDetails.
        :rtype: list[oci.capacity_management.models.OccCapacityRequestBaseDetails]
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this CreateOccCapacityRequestDetails.
        A list of different resources requested by the user.


        :param details: The details of this CreateOccCapacityRequestDetails.
        :type: list[oci.capacity_management.models.OccCapacityRequestBaseDetails]
        """
        self._details = details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
