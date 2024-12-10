# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RotateAutonomousDatabaseEncryptionKeyDetails(object):
    """
    Key details provided by the user for rotate key operation for Autonomous Database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RotateAutonomousDatabaseEncryptionKeyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key_version_id:
            The value to assign to the key_version_id property of this RotateAutonomousDatabaseEncryptionKeyDetails.
        :type key_version_id: str

        """
        self.swagger_types = {
            'key_version_id': 'str'
        }

        self.attribute_map = {
            'key_version_id': 'keyVersionId'
        }

        self._key_version_id = None

    @property
    def key_version_id(self):
        """
        Gets the key_version_id of this RotateAutonomousDatabaseEncryptionKeyDetails.
        Key version ocid of the key provided by the user for rotate operation. `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The key_version_id of this RotateAutonomousDatabaseEncryptionKeyDetails.
        :rtype: str
        """
        return self._key_version_id

    @key_version_id.setter
    def key_version_id(self, key_version_id):
        """
        Sets the key_version_id of this RotateAutonomousDatabaseEncryptionKeyDetails.
        Key version ocid of the key provided by the user for rotate operation. `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param key_version_id: The key_version_id of this RotateAutonomousDatabaseEncryptionKeyDetails.
        :type: str
        """
        self._key_version_id = key_version_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
