# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ParentGroup(object):
    """
    The parent Managed Database Group of a Managed Database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ParentGroup object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ParentGroup.
        :type id: str

        :param name:
            The value to assign to the name property of this ParentGroup.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ParentGroup.
        :type compartment_id: str

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'compartment_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'compartment_id': 'compartmentId'
        }

        self._id = None
        self._name = None
        self._compartment_id = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ParentGroup.
        The `OCID`__ of the Managed Database Group.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ParentGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ParentGroup.
        The `OCID`__ of the Managed Database Group.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ParentGroup.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ParentGroup.
        The name of the Managed Database Group.


        :return: The name of this ParentGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ParentGroup.
        The name of the Managed Database Group.


        :param name: The name of this ParentGroup.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ParentGroup.
        The `OCID`__ of the compartment in which the Managed Database Group resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ParentGroup.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ParentGroup.
        The `OCID`__ of the compartment in which the Managed Database Group resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ParentGroup.
        :type: str
        """
        self._compartment_id = compartment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
