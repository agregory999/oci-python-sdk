# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190325


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EntityLineage(object):
    """
    Lineage for a data entity.
    """

    #: A constant which can be used with the direction property of a EntityLineage.
    #: This constant has a value of "UPSTREAM"
    DIRECTION_UPSTREAM = "UPSTREAM"

    #: A constant which can be used with the direction property of a EntityLineage.
    #: This constant has a value of "BOTH"
    DIRECTION_BOTH = "BOTH"

    #: A constant which can be used with the direction property of a EntityLineage.
    #: This constant has a value of "DOWNSTREAM"
    DIRECTION_DOWNSTREAM = "DOWNSTREAM"

    def __init__(self, **kwargs):
        """
        Initializes a new EntityLineage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param level:
            The value to assign to the level property of this EntityLineage.
        :type level: int

        :param direction:
            The value to assign to the direction property of this EntityLineage.
            Allowed values for this property are: "UPSTREAM", "BOTH", "DOWNSTREAM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type direction: str

        :param objects:
            The value to assign to the objects property of this EntityLineage.
        :type objects: list[oci.data_catalog.models.LineageObject]

        :param relationships:
            The value to assign to the relationships property of this EntityLineage.
        :type relationships: list[oci.data_catalog.models.LineageRelationship]

        :param annotations:
            The value to assign to the annotations property of this EntityLineage.
        :type annotations: dict(str, dict(str, str))

        """
        self.swagger_types = {
            'level': 'int',
            'direction': 'str',
            'objects': 'list[LineageObject]',
            'relationships': 'list[LineageRelationship]',
            'annotations': 'dict(str, dict(str, str))'
        }
        self.attribute_map = {
            'level': 'level',
            'direction': 'direction',
            'objects': 'objects',
            'relationships': 'relationships',
            'annotations': 'annotations'
        }
        self._level = None
        self._direction = None
        self._objects = None
        self._relationships = None
        self._annotations = None

    @property
    def level(self):
        """
        **[Required]** Gets the level of this EntityLineage.
        Object level at which the lineage is returned.


        :return: The level of this EntityLineage.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """
        Sets the level of this EntityLineage.
        Object level at which the lineage is returned.


        :param level: The level of this EntityLineage.
        :type: int
        """
        self._level = level

    @property
    def direction(self):
        """
        **[Required]** Gets the direction of this EntityLineage.
        Direction of the lineage returned.

        Allowed values for this property are: "UPSTREAM", "BOTH", "DOWNSTREAM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The direction of this EntityLineage.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this EntityLineage.
        Direction of the lineage returned.


        :param direction: The direction of this EntityLineage.
        :type: str
        """
        allowed_values = ["UPSTREAM", "BOTH", "DOWNSTREAM"]
        if not value_allowed_none_or_none_sentinel(direction, allowed_values):
            direction = 'UNKNOWN_ENUM_VALUE'
        self._direction = direction

    @property
    def objects(self):
        """
        Gets the objects of this EntityLineage.
        Set of objects that are involved in the lineage.


        :return: The objects of this EntityLineage.
        :rtype: list[oci.data_catalog.models.LineageObject]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        """
        Sets the objects of this EntityLineage.
        Set of objects that are involved in the lineage.


        :param objects: The objects of this EntityLineage.
        :type: list[oci.data_catalog.models.LineageObject]
        """
        self._objects = objects

    @property
    def relationships(self):
        """
        Gets the relationships of this EntityLineage.
        Set of relationships between the objects in the 'objects' set.


        :return: The relationships of this EntityLineage.
        :rtype: list[oci.data_catalog.models.LineageRelationship]
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """
        Sets the relationships of this EntityLineage.
        Set of relationships between the objects in the 'objects' set.


        :param relationships: The relationships of this EntityLineage.
        :type: list[oci.data_catalog.models.LineageRelationship]
        """
        self._relationships = relationships

    @property
    def annotations(self):
        """
        Gets the annotations of this EntityLineage.
        A map of maps that contains additional information in explanation of the lineage returned. The map keys are
        categories of information and the values are maps of annotation names to their corresponding values.
        Every annotation is contained inside a category.
        Example: `{\"annotations\": { \"category\": { \"key\": \"value\"}}}`


        :return: The annotations of this EntityLineage.
        :rtype: dict(str, dict(str, str))
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """
        Sets the annotations of this EntityLineage.
        A map of maps that contains additional information in explanation of the lineage returned. The map keys are
        categories of information and the values are maps of annotation names to their corresponding values.
        Every annotation is contained inside a category.
        Example: `{\"annotations\": { \"category\": { \"key\": \"value\"}}}`


        :param annotations: The annotations of this EntityLineage.
        :type: dict(str, dict(str, str))
        """
        self._annotations = annotations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
