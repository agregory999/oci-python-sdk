# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateOfferDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateOfferDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateOfferDetails.
        :type display_name: str

        :param buyer_compartment_id:
            The value to assign to the buyer_compartment_id property of this UpdateOfferDetails.
        :type buyer_compartment_id: str

        :param description:
            The value to assign to the description property of this UpdateOfferDetails.
        :type description: str

        :param internal_notes:
            The value to assign to the internal_notes property of this UpdateOfferDetails.
        :type internal_notes: str

        :param time_start_date:
            The value to assign to the time_start_date property of this UpdateOfferDetails.
        :type time_start_date: datetime

        :param duration:
            The value to assign to the duration property of this UpdateOfferDetails.
        :type duration: str

        :param time_accept_by:
            The value to assign to the time_accept_by property of this UpdateOfferDetails.
        :type time_accept_by: datetime

        :param pricing:
            The value to assign to the pricing property of this UpdateOfferDetails.
        :type pricing: oci.marketplace_publisher.models.Pricing

        :param buyer_information:
            The value to assign to the buyer_information property of this UpdateOfferDetails.
        :type buyer_information: oci.marketplace_publisher.models.BuyerInformation

        :param seller_information:
            The value to assign to the seller_information property of this UpdateOfferDetails.
        :type seller_information: oci.marketplace_publisher.models.SellerInformation

        :param resource_bundles:
            The value to assign to the resource_bundles property of this UpdateOfferDetails.
        :type resource_bundles: list[oci.marketplace_publisher.models.ResourceBundle]

        :param custom_fields:
            The value to assign to the custom_fields property of this UpdateOfferDetails.
        :type custom_fields: list[oci.marketplace_publisher.models.CustomField]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateOfferDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateOfferDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'buyer_compartment_id': 'str',
            'description': 'str',
            'internal_notes': 'str',
            'time_start_date': 'datetime',
            'duration': 'str',
            'time_accept_by': 'datetime',
            'pricing': 'Pricing',
            'buyer_information': 'BuyerInformation',
            'seller_information': 'SellerInformation',
            'resource_bundles': 'list[ResourceBundle]',
            'custom_fields': 'list[CustomField]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'buyer_compartment_id': 'buyerCompartmentId',
            'description': 'description',
            'internal_notes': 'internalNotes',
            'time_start_date': 'timeStartDate',
            'duration': 'duration',
            'time_accept_by': 'timeAcceptBy',
            'pricing': 'pricing',
            'buyer_information': 'buyerInformation',
            'seller_information': 'sellerInformation',
            'resource_bundles': 'resourceBundles',
            'custom_fields': 'customFields',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._display_name = None
        self._buyer_compartment_id = None
        self._description = None
        self._internal_notes = None
        self._time_start_date = None
        self._duration = None
        self._time_accept_by = None
        self._pricing = None
        self._buyer_information = None
        self._seller_information = None
        self._resource_bundles = None
        self._custom_fields = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateOfferDetails.
        Offers Identifier


        :return: The display_name of this UpdateOfferDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateOfferDetails.
        Offers Identifier


        :param display_name: The display_name of this UpdateOfferDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def buyer_compartment_id(self):
        """
        Gets the buyer_compartment_id of this UpdateOfferDetails.
        OCID of the buyer's tenancy (root compartment).


        :return: The buyer_compartment_id of this UpdateOfferDetails.
        :rtype: str
        """
        return self._buyer_compartment_id

    @buyer_compartment_id.setter
    def buyer_compartment_id(self, buyer_compartment_id):
        """
        Sets the buyer_compartment_id of this UpdateOfferDetails.
        OCID of the buyer's tenancy (root compartment).


        :param buyer_compartment_id: The buyer_compartment_id of this UpdateOfferDetails.
        :type: str
        """
        self._buyer_compartment_id = buyer_compartment_id

    @property
    def description(self):
        """
        Gets the description of this UpdateOfferDetails.
        Description of the Offer


        :return: The description of this UpdateOfferDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateOfferDetails.
        Description of the Offer


        :param description: The description of this UpdateOfferDetails.
        :type: str
        """
        self._description = description

    @property
    def internal_notes(self):
        """
        Gets the internal_notes of this UpdateOfferDetails.
        Internal notes of the Offer


        :return: The internal_notes of this UpdateOfferDetails.
        :rtype: str
        """
        return self._internal_notes

    @internal_notes.setter
    def internal_notes(self, internal_notes):
        """
        Sets the internal_notes of this UpdateOfferDetails.
        Internal notes of the Offer


        :param internal_notes: The internal_notes of this UpdateOfferDetails.
        :type: str
        """
        self._internal_notes = internal_notes

    @property
    def time_start_date(self):
        """
        Gets the time_start_date of this UpdateOfferDetails.
        The time the Offer will become active after it has been accepted by the Buyer. An RFC3339 formatted datetime string


        :return: The time_start_date of this UpdateOfferDetails.
        :rtype: datetime
        """
        return self._time_start_date

    @time_start_date.setter
    def time_start_date(self, time_start_date):
        """
        Sets the time_start_date of this UpdateOfferDetails.
        The time the Offer will become active after it has been accepted by the Buyer. An RFC3339 formatted datetime string


        :param time_start_date: The time_start_date of this UpdateOfferDetails.
        :type: datetime
        """
        self._time_start_date = time_start_date

    @property
    def duration(self):
        """
        Gets the duration of this UpdateOfferDetails.
        Duration the Offer will be active after its start date. An ISO8601 extended formatted string.


        :return: The duration of this UpdateOfferDetails.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this UpdateOfferDetails.
        Duration the Offer will be active after its start date. An ISO8601 extended formatted string.


        :param duration: The duration of this UpdateOfferDetails.
        :type: str
        """
        self._duration = duration

    @property
    def time_accept_by(self):
        """
        Gets the time_accept_by of this UpdateOfferDetails.
        The time the Offer must be accepted by the Buyer before the Offer becomes invalid. An RFC3339 formatted datetime string


        :return: The time_accept_by of this UpdateOfferDetails.
        :rtype: datetime
        """
        return self._time_accept_by

    @time_accept_by.setter
    def time_accept_by(self, time_accept_by):
        """
        Sets the time_accept_by of this UpdateOfferDetails.
        The time the Offer must be accepted by the Buyer before the Offer becomes invalid. An RFC3339 formatted datetime string


        :param time_accept_by: The time_accept_by of this UpdateOfferDetails.
        :type: datetime
        """
        self._time_accept_by = time_accept_by

    @property
    def pricing(self):
        """
        Gets the pricing of this UpdateOfferDetails.

        :return: The pricing of this UpdateOfferDetails.
        :rtype: oci.marketplace_publisher.models.Pricing
        """
        return self._pricing

    @pricing.setter
    def pricing(self, pricing):
        """
        Sets the pricing of this UpdateOfferDetails.

        :param pricing: The pricing of this UpdateOfferDetails.
        :type: oci.marketplace_publisher.models.Pricing
        """
        self._pricing = pricing

    @property
    def buyer_information(self):
        """
        Gets the buyer_information of this UpdateOfferDetails.

        :return: The buyer_information of this UpdateOfferDetails.
        :rtype: oci.marketplace_publisher.models.BuyerInformation
        """
        return self._buyer_information

    @buyer_information.setter
    def buyer_information(self, buyer_information):
        """
        Sets the buyer_information of this UpdateOfferDetails.

        :param buyer_information: The buyer_information of this UpdateOfferDetails.
        :type: oci.marketplace_publisher.models.BuyerInformation
        """
        self._buyer_information = buyer_information

    @property
    def seller_information(self):
        """
        Gets the seller_information of this UpdateOfferDetails.

        :return: The seller_information of this UpdateOfferDetails.
        :rtype: oci.marketplace_publisher.models.SellerInformation
        """
        return self._seller_information

    @seller_information.setter
    def seller_information(self, seller_information):
        """
        Sets the seller_information of this UpdateOfferDetails.

        :param seller_information: The seller_information of this UpdateOfferDetails.
        :type: oci.marketplace_publisher.models.SellerInformation
        """
        self._seller_information = seller_information

    @property
    def resource_bundles(self):
        """
        Gets the resource_bundles of this UpdateOfferDetails.
        A list of Resource Bundles associated with an Offer.


        :return: The resource_bundles of this UpdateOfferDetails.
        :rtype: list[oci.marketplace_publisher.models.ResourceBundle]
        """
        return self._resource_bundles

    @resource_bundles.setter
    def resource_bundles(self, resource_bundles):
        """
        Sets the resource_bundles of this UpdateOfferDetails.
        A list of Resource Bundles associated with an Offer.


        :param resource_bundles: The resource_bundles of this UpdateOfferDetails.
        :type: list[oci.marketplace_publisher.models.ResourceBundle]
        """
        self._resource_bundles = resource_bundles

    @property
    def custom_fields(self):
        """
        Gets the custom_fields of this UpdateOfferDetails.
        A list of key value pairs specified by the seller


        :return: The custom_fields of this UpdateOfferDetails.
        :rtype: list[oci.marketplace_publisher.models.CustomField]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """
        Sets the custom_fields of this UpdateOfferDetails.
        A list of key value pairs specified by the seller


        :param custom_fields: The custom_fields of this UpdateOfferDetails.
        :type: list[oci.marketplace_publisher.models.CustomField]
        """
        self._custom_fields = custom_fields

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateOfferDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateOfferDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateOfferDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateOfferDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateOfferDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateOfferDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateOfferDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateOfferDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
