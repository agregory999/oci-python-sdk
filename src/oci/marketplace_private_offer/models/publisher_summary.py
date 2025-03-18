# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PublisherSummary(object):
    """
    The model for a publisher.
    """

    #: A constant which can be used with the publisher_type property of a PublisherSummary.
    #: This constant has a value of "INTERNAL"
    PUBLISHER_TYPE_INTERNAL = "INTERNAL"

    #: A constant which can be used with the publisher_type property of a PublisherSummary.
    #: This constant has a value of "EXTERNAL"
    PUBLISHER_TYPE_EXTERNAL = "EXTERNAL"

    def __init__(self, **kwargs):
        """
        Initializes a new PublisherSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this PublisherSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this PublisherSummary.
        :type compartment_id: str

        :param registry_namespace:
            The value to assign to the registry_namespace property of this PublisherSummary.
        :type registry_namespace: str

        :param legacy_id:
            The value to assign to the legacy_id property of this PublisherSummary.
        :type legacy_id: str

        :param display_name:
            The value to assign to the display_name property of this PublisherSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this PublisherSummary.
        :type description: str

        :param year_founded:
            The value to assign to the year_founded property of this PublisherSummary.
        :type year_founded: int

        :param website_url:
            The value to assign to the website_url property of this PublisherSummary.
        :type website_url: str

        :param contact_email:
            The value to assign to the contact_email property of this PublisherSummary.
        :type contact_email: str

        :param contact_phone:
            The value to assign to the contact_phone property of this PublisherSummary.
        :type contact_phone: str

        :param hq_address:
            The value to assign to the hq_address property of this PublisherSummary.
        :type hq_address: str

        :param logo:
            The value to assign to the logo property of this PublisherSummary.
        :type logo: oci.marketplace_private_offer.models.UploadData

        :param facebook_url:
            The value to assign to the facebook_url property of this PublisherSummary.
        :type facebook_url: str

        :param twitter_url:
            The value to assign to the twitter_url property of this PublisherSummary.
        :type twitter_url: str

        :param linkedin_url:
            The value to assign to the linkedin_url property of this PublisherSummary.
        :type linkedin_url: str

        :param publisher_type:
            The value to assign to the publisher_type property of this PublisherSummary.
            Allowed values for this property are: "INTERNAL", "EXTERNAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type publisher_type: str

        :param time_created:
            The value to assign to the time_created property of this PublisherSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this PublisherSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this PublisherSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this PublisherSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this PublisherSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'registry_namespace': 'str',
            'legacy_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'year_founded': 'int',
            'website_url': 'str',
            'contact_email': 'str',
            'contact_phone': 'str',
            'hq_address': 'str',
            'logo': 'UploadData',
            'facebook_url': 'str',
            'twitter_url': 'str',
            'linkedin_url': 'str',
            'publisher_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'registry_namespace': 'registryNamespace',
            'legacy_id': 'legacyId',
            'display_name': 'displayName',
            'description': 'description',
            'year_founded': 'yearFounded',
            'website_url': 'websiteUrl',
            'contact_email': 'contactEmail',
            'contact_phone': 'contactPhone',
            'hq_address': 'hqAddress',
            'logo': 'logo',
            'facebook_url': 'facebookUrl',
            'twitter_url': 'twitterUrl',
            'linkedin_url': 'linkedinUrl',
            'publisher_type': 'publisherType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._compartment_id = None
        self._registry_namespace = None
        self._legacy_id = None
        self._display_name = None
        self._description = None
        self._year_founded = None
        self._website_url = None
        self._contact_email = None
        self._contact_phone = None
        self._hq_address = None
        self._logo = None
        self._facebook_url = None
        self._twitter_url = None
        self._linkedin_url = None
        self._publisher_type = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this PublisherSummary.
        Unique OCID identifier for the publisher.


        :return: The id of this PublisherSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PublisherSummary.
        Unique OCID identifier for the publisher.


        :param id: The id of this PublisherSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this PublisherSummary.
        The root compartment of the Publisher.


        :return: The compartment_id of this PublisherSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this PublisherSummary.
        The root compartment of the Publisher.


        :param compartment_id: The compartment_id of this PublisherSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def registry_namespace(self):
        """
        **[Required]** Gets the registry_namespace of this PublisherSummary.
        The namespace for the publisher registry to persist artifacts.


        :return: The registry_namespace of this PublisherSummary.
        :rtype: str
        """
        return self._registry_namespace

    @registry_namespace.setter
    def registry_namespace(self, registry_namespace):
        """
        Sets the registry_namespace of this PublisherSummary.
        The namespace for the publisher registry to persist artifacts.


        :param registry_namespace: The registry_namespace of this PublisherSummary.
        :type: str
        """
        self._registry_namespace = registry_namespace

    @property
    def legacy_id(self):
        """
        Gets the legacy_id of this PublisherSummary.
        Unique legacy service identifier for the publisher.


        :return: The legacy_id of this PublisherSummary.
        :rtype: str
        """
        return self._legacy_id

    @legacy_id.setter
    def legacy_id(self, legacy_id):
        """
        Sets the legacy_id of this PublisherSummary.
        Unique legacy service identifier for the publisher.


        :param legacy_id: The legacy_id of this PublisherSummary.
        :type: str
        """
        self._legacy_id = legacy_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this PublisherSummary.
        The name of the publisher.


        :return: The display_name of this PublisherSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this PublisherSummary.
        The name of the publisher.


        :param display_name: The display_name of this PublisherSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this PublisherSummary.
        A description of the publisher.


        :return: The description of this PublisherSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PublisherSummary.
        A description of the publisher.


        :param description: The description of this PublisherSummary.
        :type: str
        """
        self._description = description

    @property
    def year_founded(self):
        """
        Gets the year_founded of this PublisherSummary.
        The year the publisher's company or organization was founded.


        :return: The year_founded of this PublisherSummary.
        :rtype: int
        """
        return self._year_founded

    @year_founded.setter
    def year_founded(self, year_founded):
        """
        Sets the year_founded of this PublisherSummary.
        The year the publisher's company or organization was founded.


        :param year_founded: The year_founded of this PublisherSummary.
        :type: int
        """
        self._year_founded = year_founded

    @property
    def website_url(self):
        """
        Gets the website_url of this PublisherSummary.
        The publisher's website.


        :return: The website_url of this PublisherSummary.
        :rtype: str
        """
        return self._website_url

    @website_url.setter
    def website_url(self, website_url):
        """
        Sets the website_url of this PublisherSummary.
        The publisher's website.


        :param website_url: The website_url of this PublisherSummary.
        :type: str
        """
        self._website_url = website_url

    @property
    def contact_email(self):
        """
        **[Required]** Gets the contact_email of this PublisherSummary.
        The public email address of the publisher for customers.


        :return: The contact_email of this PublisherSummary.
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """
        Sets the contact_email of this PublisherSummary.
        The public email address of the publisher for customers.


        :param contact_email: The contact_email of this PublisherSummary.
        :type: str
        """
        self._contact_email = contact_email

    @property
    def contact_phone(self):
        """
        **[Required]** Gets the contact_phone of this PublisherSummary.
        The phone number of the publisher in E.164 format.


        :return: The contact_phone of this PublisherSummary.
        :rtype: str
        """
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, contact_phone):
        """
        Sets the contact_phone of this PublisherSummary.
        The phone number of the publisher in E.164 format.


        :param contact_phone: The contact_phone of this PublisherSummary.
        :type: str
        """
        self._contact_phone = contact_phone

    @property
    def hq_address(self):
        """
        Gets the hq_address of this PublisherSummary.
        The address of the publisher's headquarters.


        :return: The hq_address of this PublisherSummary.
        :rtype: str
        """
        return self._hq_address

    @hq_address.setter
    def hq_address(self, hq_address):
        """
        Sets the hq_address of this PublisherSummary.
        The address of the publisher's headquarters.


        :param hq_address: The hq_address of this PublisherSummary.
        :type: str
        """
        self._hq_address = hq_address

    @property
    def logo(self):
        """
        Gets the logo of this PublisherSummary.

        :return: The logo of this PublisherSummary.
        :rtype: oci.marketplace_private_offer.models.UploadData
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """
        Sets the logo of this PublisherSummary.

        :param logo: The logo of this PublisherSummary.
        :type: oci.marketplace_private_offer.models.UploadData
        """
        self._logo = logo

    @property
    def facebook_url(self):
        """
        Gets the facebook_url of this PublisherSummary.
        Publisher's Facebook URL


        :return: The facebook_url of this PublisherSummary.
        :rtype: str
        """
        return self._facebook_url

    @facebook_url.setter
    def facebook_url(self, facebook_url):
        """
        Sets the facebook_url of this PublisherSummary.
        Publisher's Facebook URL


        :param facebook_url: The facebook_url of this PublisherSummary.
        :type: str
        """
        self._facebook_url = facebook_url

    @property
    def twitter_url(self):
        """
        Gets the twitter_url of this PublisherSummary.
        Publisher's Twitter URL


        :return: The twitter_url of this PublisherSummary.
        :rtype: str
        """
        return self._twitter_url

    @twitter_url.setter
    def twitter_url(self, twitter_url):
        """
        Sets the twitter_url of this PublisherSummary.
        Publisher's Twitter URL


        :param twitter_url: The twitter_url of this PublisherSummary.
        :type: str
        """
        self._twitter_url = twitter_url

    @property
    def linkedin_url(self):
        """
        Gets the linkedin_url of this PublisherSummary.
        Publisher's LinkedIn URL


        :return: The linkedin_url of this PublisherSummary.
        :rtype: str
        """
        return self._linkedin_url

    @linkedin_url.setter
    def linkedin_url(self, linkedin_url):
        """
        Sets the linkedin_url of this PublisherSummary.
        Publisher's LinkedIn URL


        :param linkedin_url: The linkedin_url of this PublisherSummary.
        :type: str
        """
        self._linkedin_url = linkedin_url

    @property
    def publisher_type(self):
        """
        **[Required]** Gets the publisher_type of this PublisherSummary.
        publisher type.

        Allowed values for this property are: "INTERNAL", "EXTERNAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The publisher_type of this PublisherSummary.
        :rtype: str
        """
        return self._publisher_type

    @publisher_type.setter
    def publisher_type(self, publisher_type):
        """
        Sets the publisher_type of this PublisherSummary.
        publisher type.


        :param publisher_type: The publisher_type of this PublisherSummary.
        :type: str
        """
        allowed_values = ["INTERNAL", "EXTERNAL"]
        if not value_allowed_none_or_none_sentinel(publisher_type, allowed_values):
            publisher_type = 'UNKNOWN_ENUM_VALUE'
        self._publisher_type = publisher_type

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this PublisherSummary.
        The time the publisher was created. An RFC3339 formatted datetime string.


        :return: The time_created of this PublisherSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PublisherSummary.
        The time the publisher was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this PublisherSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this PublisherSummary.
        The time the publisher was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this PublisherSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this PublisherSummary.
        The time the publisher was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this PublisherSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this PublisherSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this PublisherSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this PublisherSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this PublisherSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this PublisherSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this PublisherSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this PublisherSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this PublisherSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this PublisherSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this PublisherSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this PublisherSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this PublisherSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
