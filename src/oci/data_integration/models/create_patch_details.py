# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePatchDetails(object):
    """
    Properties used in patch create operations.
    """

    #: A constant which can be used with the patch_type property of a CreatePatchDetails.
    #: This constant has a value of "PUBLISH"
    PATCH_TYPE_PUBLISH = "PUBLISH"

    #: A constant which can be used with the patch_type property of a CreatePatchDetails.
    #: This constant has a value of "REFRESH"
    PATCH_TYPE_REFRESH = "REFRESH"

    #: A constant which can be used with the patch_type property of a CreatePatchDetails.
    #: This constant has a value of "UNPUBLISH"
    PATCH_TYPE_UNPUBLISH = "UNPUBLISH"

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePatchDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this CreatePatchDetails.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this CreatePatchDetails.
        :type model_version: str

        :param name:
            The value to assign to the name property of this CreatePatchDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreatePatchDetails.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this CreatePatchDetails.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this CreatePatchDetails.
        :type identifier: str

        :param patch_type:
            The value to assign to the patch_type property of this CreatePatchDetails.
            Allowed values for this property are: "PUBLISH", "REFRESH", "UNPUBLISH"
        :type patch_type: str

        :param object_keys:
            The value to assign to the object_keys property of this CreatePatchDetails.
        :type object_keys: list[str]

        :param registry_metadata:
            The value to assign to the registry_metadata property of this CreatePatchDetails.
        :type registry_metadata: RegistryMetadata

        """
        self.swagger_types = {
            'key': 'str',
            'model_version': 'str',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'identifier': 'str',
            'patch_type': 'str',
            'object_keys': 'list[str]',
            'registry_metadata': 'RegistryMetadata'
        }

        self.attribute_map = {
            'key': 'key',
            'model_version': 'modelVersion',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'patch_type': 'patchType',
            'object_keys': 'objectKeys',
            'registry_metadata': 'registryMetadata'
        }

        self._key = None
        self._model_version = None
        self._name = None
        self._description = None
        self._object_status = None
        self._identifier = None
        self._patch_type = None
        self._object_keys = None
        self._registry_metadata = None

    @property
    def key(self):
        """
        Gets the key of this CreatePatchDetails.
        The object's key.


        :return: The key of this CreatePatchDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CreatePatchDetails.
        The object's key.


        :param key: The key of this CreatePatchDetails.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this CreatePatchDetails.
        The object's model version.


        :return: The model_version of this CreatePatchDetails.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this CreatePatchDetails.
        The object's model version.


        :param model_version: The model_version of this CreatePatchDetails.
        :type: str
        """
        self._model_version = model_version

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreatePatchDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this CreatePatchDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreatePatchDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this CreatePatchDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreatePatchDetails.
        Detailed description for the object.


        :return: The description of this CreatePatchDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreatePatchDetails.
        Detailed description for the object.


        :param description: The description of this CreatePatchDetails.
        :type: str
        """
        self._description = description

    @property
    def object_status(self):
        """
        Gets the object_status of this CreatePatchDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this CreatePatchDetails.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this CreatePatchDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this CreatePatchDetails.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        **[Required]** Gets the identifier of this CreatePatchDetails.
        Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this CreatePatchDetails.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this CreatePatchDetails.
        Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this CreatePatchDetails.
        :type: str
        """
        self._identifier = identifier

    @property
    def patch_type(self):
        """
        **[Required]** Gets the patch_type of this CreatePatchDetails.
        The type of the patch applied or being applied on the application.

        Allowed values for this property are: "PUBLISH", "REFRESH", "UNPUBLISH"


        :return: The patch_type of this CreatePatchDetails.
        :rtype: str
        """
        return self._patch_type

    @patch_type.setter
    def patch_type(self, patch_type):
        """
        Sets the patch_type of this CreatePatchDetails.
        The type of the patch applied or being applied on the application.


        :param patch_type: The patch_type of this CreatePatchDetails.
        :type: str
        """
        allowed_values = ["PUBLISH", "REFRESH", "UNPUBLISH"]
        if not value_allowed_none_or_none_sentinel(patch_type, allowed_values):
            raise ValueError(
                "Invalid value for `patch_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._patch_type = patch_type

    @property
    def object_keys(self):
        """
        **[Required]** Gets the object_keys of this CreatePatchDetails.
        The array of object keys to publish into application.


        :return: The object_keys of this CreatePatchDetails.
        :rtype: list[str]
        """
        return self._object_keys

    @object_keys.setter
    def object_keys(self, object_keys):
        """
        Sets the object_keys of this CreatePatchDetails.
        The array of object keys to publish into application.


        :param object_keys: The object_keys of this CreatePatchDetails.
        :type: list[str]
        """
        self._object_keys = object_keys

    @property
    def registry_metadata(self):
        """
        Gets the registry_metadata of this CreatePatchDetails.

        :return: The registry_metadata of this CreatePatchDetails.
        :rtype: RegistryMetadata
        """
        return self._registry_metadata

    @registry_metadata.setter
    def registry_metadata(self, registry_metadata):
        """
        Sets the registry_metadata of this CreatePatchDetails.

        :param registry_metadata: The registry_metadata of this CreatePatchDetails.
        :type: RegistryMetadata
        """
        self._registry_metadata = registry_metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other