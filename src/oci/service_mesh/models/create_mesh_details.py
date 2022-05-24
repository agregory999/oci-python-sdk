# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMeshDetails(object):
    """
    The information about a new Mesh.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMeshDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateMeshDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateMeshDetails.
        :type description: str

        :param certificate_authorities:
            The value to assign to the certificate_authorities property of this CreateMeshDetails.
        :type certificate_authorities: list[oci.service_mesh.models.CertificateAuthority]

        :param mtls:
            The value to assign to the mtls property of this CreateMeshDetails.
        :type mtls: oci.service_mesh.models.MeshMutualTransportLayerSecurity

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateMeshDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateMeshDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateMeshDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'certificate_authorities': 'list[CertificateAuthority]',
            'mtls': 'MeshMutualTransportLayerSecurity',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'certificate_authorities': 'certificateAuthorities',
            'mtls': 'mtls',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._certificate_authorities = None
        self._mtls = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateMeshDetails.
        A user-friendly name. The name does not have to be unique and can be changed after creation.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this CreateMeshDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateMeshDetails.
        A user-friendly name. The name does not have to be unique and can be changed after creation.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this CreateMeshDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateMeshDetails.
        Description of the resource. It can be changed after creation.
        Avoid entering confidential information.

        Example: `This is my new resource`


        :return: The description of this CreateMeshDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateMeshDetails.
        Description of the resource. It can be changed after creation.
        Avoid entering confidential information.

        Example: `This is my new resource`


        :param description: The description of this CreateMeshDetails.
        :type: str
        """
        self._description = description

    @property
    def certificate_authorities(self):
        """
        **[Required]** Gets the certificate_authorities of this CreateMeshDetails.
        The OCID of the certificate authority resource OCID to use for creating leaf certificates.


        :return: The certificate_authorities of this CreateMeshDetails.
        :rtype: list[oci.service_mesh.models.CertificateAuthority]
        """
        return self._certificate_authorities

    @certificate_authorities.setter
    def certificate_authorities(self, certificate_authorities):
        """
        Sets the certificate_authorities of this CreateMeshDetails.
        The OCID of the certificate authority resource OCID to use for creating leaf certificates.


        :param certificate_authorities: The certificate_authorities of this CreateMeshDetails.
        :type: list[oci.service_mesh.models.CertificateAuthority]
        """
        self._certificate_authorities = certificate_authorities

    @property
    def mtls(self):
        """
        Gets the mtls of this CreateMeshDetails.

        :return: The mtls of this CreateMeshDetails.
        :rtype: oci.service_mesh.models.MeshMutualTransportLayerSecurity
        """
        return self._mtls

    @mtls.setter
    def mtls(self, mtls):
        """
        Sets the mtls of this CreateMeshDetails.

        :param mtls: The mtls of this CreateMeshDetails.
        :type: oci.service_mesh.models.MeshMutualTransportLayerSecurity
        """
        self._mtls = mtls

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateMeshDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateMeshDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateMeshDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateMeshDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateMeshDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateMeshDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateMeshDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateMeshDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateMeshDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateMeshDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateMeshDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateMeshDetails.
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