# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateProfileDetails(object):
    """
    The information about new registration profile.
    """

    #: A constant which can be used with the profile_type property of a CreateProfileDetails.
    #: This constant has a value of "SOFTWARESOURCE"
    PROFILE_TYPE_SOFTWARESOURCE = "SOFTWARESOURCE"

    #: A constant which can be used with the profile_type property of a CreateProfileDetails.
    #: This constant has a value of "GROUP"
    PROFILE_TYPE_GROUP = "GROUP"

    #: A constant which can be used with the profile_type property of a CreateProfileDetails.
    #: This constant has a value of "LIFECYCLE"
    PROFILE_TYPE_LIFECYCLE = "LIFECYCLE"

    #: A constant which can be used with the profile_type property of a CreateProfileDetails.
    #: This constant has a value of "STATION"
    PROFILE_TYPE_STATION = "STATION"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateProfileDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.os_management_hub.models.CreateGroupProfileDetails`
        * :class:`~oci.os_management_hub.models.CreateStationProfileDetails`
        * :class:`~oci.os_management_hub.models.CreateSoftwareSourceProfileDetails`
        * :class:`~oci.os_management_hub.models.CreateLifecycleProfileDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateProfileDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateProfileDetails.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this CreateProfileDetails.
        :type description: str

        :param management_station_id:
            The value to assign to the management_station_id property of this CreateProfileDetails.
        :type management_station_id: str

        :param profile_type:
            The value to assign to the profile_type property of this CreateProfileDetails.
            Allowed values for this property are: "SOFTWARESOURCE", "GROUP", "LIFECYCLE", "STATION"
        :type profile_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateProfileDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateProfileDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'description': 'str',
            'management_station_id': 'str',
            'profile_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'description': 'description',
            'management_station_id': 'managementStationId',
            'profile_type': 'profileType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._description = None
        self._management_station_id = None
        self._profile_type = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['profileType']

        if type == 'GROUP':
            return 'CreateGroupProfileDetails'

        if type == 'STATION':
            return 'CreateStationProfileDetails'

        if type == 'SOFTWARESOURCE':
            return 'CreateSoftwareSourceProfileDetails'

        if type == 'LIFECYCLE':
            return 'CreateLifecycleProfileDetails'
        else:
            return 'CreateProfileDetails'

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateProfileDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateProfileDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateProfileDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateProfileDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateProfileDetails.
        The OCID of the tenancy containing the registration profile.


        :return: The compartment_id of this CreateProfileDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateProfileDetails.
        The OCID of the tenancy containing the registration profile.


        :param compartment_id: The compartment_id of this CreateProfileDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def description(self):
        """
        Gets the description of this CreateProfileDetails.
        The description of the registration profile.


        :return: The description of this CreateProfileDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateProfileDetails.
        The description of the registration profile.


        :param description: The description of this CreateProfileDetails.
        :type: str
        """
        self._description = description

    @property
    def management_station_id(self):
        """
        Gets the management_station_id of this CreateProfileDetails.
        The OCID of the management station.


        :return: The management_station_id of this CreateProfileDetails.
        :rtype: str
        """
        return self._management_station_id

    @management_station_id.setter
    def management_station_id(self, management_station_id):
        """
        Sets the management_station_id of this CreateProfileDetails.
        The OCID of the management station.


        :param management_station_id: The management_station_id of this CreateProfileDetails.
        :type: str
        """
        self._management_station_id = management_station_id

    @property
    def profile_type(self):
        """
        **[Required]** Gets the profile_type of this CreateProfileDetails.
        The type of registration profile. Either SOFTWARESOURCE, GROUP or LIFECYCLE.

        Allowed values for this property are: "SOFTWARESOURCE", "GROUP", "LIFECYCLE", "STATION"


        :return: The profile_type of this CreateProfileDetails.
        :rtype: str
        """
        return self._profile_type

    @profile_type.setter
    def profile_type(self, profile_type):
        """
        Sets the profile_type of this CreateProfileDetails.
        The type of registration profile. Either SOFTWARESOURCE, GROUP or LIFECYCLE.


        :param profile_type: The profile_type of this CreateProfileDetails.
        :type: str
        """
        allowed_values = ["SOFTWARESOURCE", "GROUP", "LIFECYCLE", "STATION"]
        if not value_allowed_none_or_none_sentinel(profile_type, allowed_values):
            raise ValueError(
                "Invalid value for `profile_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._profile_type = profile_type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateProfileDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateProfileDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateProfileDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateProfileDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateProfileDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateProfileDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateProfileDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateProfileDetails.
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
