# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230501

from .application_summary import ApplicationSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Icmp6ApplicationSummary(ApplicationSummary):
    """
    Summary object for ICMP V6 application element in the network firewall policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Icmp6ApplicationSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.network_firewall.models.Icmp6ApplicationSummary.type` attribute
        of this class is ``ICMP_V6`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this Icmp6ApplicationSummary.
            Allowed values for this property are: "ICMP", "ICMP_V6"
        :type type: str

        :param name:
            The value to assign to the name property of this Icmp6ApplicationSummary.
        :type name: str

        :param parent_resource_id:
            The value to assign to the parent_resource_id property of this Icmp6ApplicationSummary.
        :type parent_resource_id: str

        :param icmp_type:
            The value to assign to the icmp_type property of this Icmp6ApplicationSummary.
        :type icmp_type: int

        :param icmp_code:
            The value to assign to the icmp_code property of this Icmp6ApplicationSummary.
        :type icmp_code: int

        """
        self.swagger_types = {
            'type': 'str',
            'name': 'str',
            'parent_resource_id': 'str',
            'icmp_type': 'int',
            'icmp_code': 'int'
        }
        self.attribute_map = {
            'type': 'type',
            'name': 'name',
            'parent_resource_id': 'parentResourceId',
            'icmp_type': 'icmpType',
            'icmp_code': 'icmpCode'
        }
        self._type = None
        self._name = None
        self._parent_resource_id = None
        self._icmp_type = None
        self._icmp_code = None
        self._type = 'ICMP_V6'

    @property
    def icmp_type(self):
        """
        **[Required]** Gets the icmp_type of this Icmp6ApplicationSummary.
        The value of the ICMP message Type field as defined by `RFC 792`__.

        __ https://www.rfc-editor.org/rfc/rfc792.html


        :return: The icmp_type of this Icmp6ApplicationSummary.
        :rtype: int
        """
        return self._icmp_type

    @icmp_type.setter
    def icmp_type(self, icmp_type):
        """
        Sets the icmp_type of this Icmp6ApplicationSummary.
        The value of the ICMP message Type field as defined by `RFC 792`__.

        __ https://www.rfc-editor.org/rfc/rfc792.html


        :param icmp_type: The icmp_type of this Icmp6ApplicationSummary.
        :type: int
        """
        self._icmp_type = icmp_type

    @property
    def icmp_code(self):
        """
        Gets the icmp_code of this Icmp6ApplicationSummary.
        The value of the ICMP message Code (subtype) field as defined by `RFC 792`__.

        __ https://www.rfc-editor.org/rfc/rfc792.html


        :return: The icmp_code of this Icmp6ApplicationSummary.
        :rtype: int
        """
        return self._icmp_code

    @icmp_code.setter
    def icmp_code(self, icmp_code):
        """
        Sets the icmp_code of this Icmp6ApplicationSummary.
        The value of the ICMP message Code (subtype) field as defined by `RFC 792`__.

        __ https://www.rfc-editor.org/rfc/rfc792.html


        :param icmp_code: The icmp_code of this Icmp6ApplicationSummary.
        :type: int
        """
        self._icmp_code = icmp_code

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
