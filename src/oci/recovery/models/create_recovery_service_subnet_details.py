# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210216


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateRecoveryServiceSubnetDetails(object):
    """
    Describes the parameters required to create a Recovery Service Subnet.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateRecoveryServiceSubnetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateRecoveryServiceSubnetDetails.
        :type display_name: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateRecoveryServiceSubnetDetails.
        :type subnet_id: str

        :param subnets:
            The value to assign to the subnets property of this CreateRecoveryServiceSubnetDetails.
        :type subnets: list[str]

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateRecoveryServiceSubnetDetails.
        :type nsg_ids: list[str]

        :param vcn_id:
            The value to assign to the vcn_id property of this CreateRecoveryServiceSubnetDetails.
        :type vcn_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateRecoveryServiceSubnetDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateRecoveryServiceSubnetDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateRecoveryServiceSubnetDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'subnet_id': 'str',
            'subnets': 'list[str]',
            'nsg_ids': 'list[str]',
            'vcn_id': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'subnet_id': 'subnetId',
            'subnets': 'subnets',
            'nsg_ids': 'nsgIds',
            'vcn_id': 'vcnId',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._display_name = None
        self._subnet_id = None
        self._subnets = None
        self._nsg_ids = None
        self._vcn_id = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateRecoveryServiceSubnetDetails.
        A user-provided name for the recovery service subnet. The 'displayName' does not have to be unique, and it can be modified. Avoid entering confidential information.


        :return: The display_name of this CreateRecoveryServiceSubnetDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateRecoveryServiceSubnetDetails.
        A user-provided name for the recovery service subnet. The 'displayName' does not have to be unique, and it can be modified. Avoid entering confidential information.


        :param display_name: The display_name of this CreateRecoveryServiceSubnetDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this CreateRecoveryServiceSubnetDetails.
        Deprecated. One of the subnets associated with the Recovery Service subnet.


        :return: The subnet_id of this CreateRecoveryServiceSubnetDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateRecoveryServiceSubnetDetails.
        Deprecated. One of the subnets associated with the Recovery Service subnet.


        :param subnet_id: The subnet_id of this CreateRecoveryServiceSubnetDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def subnets(self):
        """
        Gets the subnets of this CreateRecoveryServiceSubnetDetails.
        A list of OCIDs of the subnets associated with the Recovery Service subnet.


        :return: The subnets of this CreateRecoveryServiceSubnetDetails.
        :rtype: list[str]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        """
        Sets the subnets of this CreateRecoveryServiceSubnetDetails.
        A list of OCIDs of the subnets associated with the Recovery Service subnet.


        :param subnets: The subnets of this CreateRecoveryServiceSubnetDetails.
        :type: list[str]
        """
        self._subnets = subnets

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this CreateRecoveryServiceSubnetDetails.
        A list of network security group (NSG) OCIDs that are associated with the Recovery Service subnet.
        You can specify a maximum of 5 unique OCIDs, which implies that you can associate a maximum of 5 NSGs to each Recovery Service subnet.
        Specify an empty array if you want to remove all the associated NSGs from a Recovery Service subnet.
        See :class:`NetworkSecurityGroup` for more information.


        :return: The nsg_ids of this CreateRecoveryServiceSubnetDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this CreateRecoveryServiceSubnetDetails.
        A list of network security group (NSG) OCIDs that are associated with the Recovery Service subnet.
        You can specify a maximum of 5 unique OCIDs, which implies that you can associate a maximum of 5 NSGs to each Recovery Service subnet.
        Specify an empty array if you want to remove all the associated NSGs from a Recovery Service subnet.
        See :class:`NetworkSecurityGroup` for more information.


        :param nsg_ids: The nsg_ids of this CreateRecoveryServiceSubnetDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this CreateRecoveryServiceSubnetDetails.
        The OCID of the virtual cloud network (VCN) that contains the recovery service subnet. You can create a single recovery service subnet per VCN.


        :return: The vcn_id of this CreateRecoveryServiceSubnetDetails.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this CreateRecoveryServiceSubnetDetails.
        The OCID of the virtual cloud network (VCN) that contains the recovery service subnet. You can create a single recovery service subnet per VCN.


        :param vcn_id: The vcn_id of this CreateRecoveryServiceSubnetDetails.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateRecoveryServiceSubnetDetails.
        The compartment OCID.


        :return: The compartment_id of this CreateRecoveryServiceSubnetDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateRecoveryServiceSubnetDetails.
        The compartment OCID.


        :param compartment_id: The compartment_id of this CreateRecoveryServiceSubnetDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateRecoveryServiceSubnetDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateRecoveryServiceSubnetDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateRecoveryServiceSubnetDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateRecoveryServiceSubnetDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateRecoveryServiceSubnetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see `Resource Tags`__

        __ https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateRecoveryServiceSubnetDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateRecoveryServiceSubnetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see `Resource Tags`__

        __ https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateRecoveryServiceSubnetDetails.
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
