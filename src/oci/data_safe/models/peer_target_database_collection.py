# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PeerTargetDatabaseCollection(object):
    """
    Summary of peer target databases of a primary target database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PeerTargetDatabaseCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this PeerTargetDatabaseCollection.
        :type compartment_id: str

        :param target_database_id:
            The value to assign to the target_database_id property of this PeerTargetDatabaseCollection.
        :type target_database_id: str

        :param items:
            The value to assign to the items property of this PeerTargetDatabaseCollection.
        :type items: list[oci.data_safe.models.PeerTargetDatabaseSummary]

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'target_database_id': 'str',
            'items': 'list[PeerTargetDatabaseSummary]'
        }
        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'target_database_id': 'targetDatabaseId',
            'items': 'items'
        }
        self._compartment_id = None
        self._target_database_id = None
        self._items = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this PeerTargetDatabaseCollection.
        The OCID of the compartment that contains the primary target database.


        :return: The compartment_id of this PeerTargetDatabaseCollection.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this PeerTargetDatabaseCollection.
        The OCID of the compartment that contains the primary target database.


        :param compartment_id: The compartment_id of this PeerTargetDatabaseCollection.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def target_database_id(self):
        """
        **[Required]** Gets the target_database_id of this PeerTargetDatabaseCollection.
        The OCID of the Data Safe target database.


        :return: The target_database_id of this PeerTargetDatabaseCollection.
        :rtype: str
        """
        return self._target_database_id

    @target_database_id.setter
    def target_database_id(self, target_database_id):
        """
        Sets the target_database_id of this PeerTargetDatabaseCollection.
        The OCID of the Data Safe target database.


        :param target_database_id: The target_database_id of this PeerTargetDatabaseCollection.
        :type: str
        """
        self._target_database_id = target_database_id

    @property
    def items(self):
        """
        Gets the items of this PeerTargetDatabaseCollection.
        The list of peer target databases associated to the primary target database.


        :return: The items of this PeerTargetDatabaseCollection.
        :rtype: list[oci.data_safe.models.PeerTargetDatabaseSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this PeerTargetDatabaseCollection.
        The list of peer target databases associated to the primary target database.


        :param items: The items of this PeerTargetDatabaseCollection.
        :type: list[oci.data_safe.models.PeerTargetDatabaseSummary]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
