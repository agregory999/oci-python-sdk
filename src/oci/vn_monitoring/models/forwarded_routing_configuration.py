# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ForwardedRoutingConfiguration(object):
    """
    Defines the type of the resource that forwarded traffic.
    """

    #: A constant which can be used with the type property of a ForwardedRoutingConfiguration.
    #: This constant has a value of "VCN"
    TYPE_VCN = "VCN"

    #: A constant which can be used with the type property of a ForwardedRoutingConfiguration.
    #: This constant has a value of "DRG"
    TYPE_DRG = "DRG"

    def __init__(self, **kwargs):
        """
        Initializes a new ForwardedRoutingConfiguration object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.vn_monitoring.models.VcnRoutingConfiguration`
        * :class:`~oci.vn_monitoring.models.DrgRoutingConfiguration`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ForwardedRoutingConfiguration.
            Allowed values for this property are: "VCN", "DRG", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'VCN':
            return 'VcnRoutingConfiguration'

        if type == 'DRG':
            return 'DrgRoutingConfiguration'
        else:
            return 'ForwardedRoutingConfiguration'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ForwardedRoutingConfiguration.
        Type of the forwarded routing configuration.

        Allowed values for this property are: "VCN", "DRG", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this ForwardedRoutingConfiguration.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ForwardedRoutingConfiguration.
        Type of the forwarded routing configuration.


        :param type: The type of this ForwardedRoutingConfiguration.
        :type: str
        """
        allowed_values = ["VCN", "DRG"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
