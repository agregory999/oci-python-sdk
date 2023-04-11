# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalAsmUserSummary(object):
    """
    The summary of an ASM user.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalAsmUserSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ExternalAsmUserSummary.
        :type name: str

        :param privileges:
            The value to assign to the privileges property of this ExternalAsmUserSummary.
        :type privileges: list[str]

        :param asm_id:
            The value to assign to the asm_id property of this ExternalAsmUserSummary.
        :type asm_id: str

        """
        self.swagger_types = {
            'name': 'str',
            'privileges': 'list[str]',
            'asm_id': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'privileges': 'privileges',
            'asm_id': 'asmId'
        }

        self._name = None
        self._privileges = None
        self._asm_id = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ExternalAsmUserSummary.
        The name of the ASM user.


        :return: The name of this ExternalAsmUserSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ExternalAsmUserSummary.
        The name of the ASM user.


        :param name: The name of this ExternalAsmUserSummary.
        :type: str
        """
        self._name = name

    @property
    def privileges(self):
        """
        **[Required]** Gets the privileges of this ExternalAsmUserSummary.
        The list of privileges of the ASM user.


        :return: The privileges of this ExternalAsmUserSummary.
        :rtype: list[str]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """
        Sets the privileges of this ExternalAsmUserSummary.
        The list of privileges of the ASM user.


        :param privileges: The privileges of this ExternalAsmUserSummary.
        :type: list[str]
        """
        self._privileges = privileges

    @property
    def asm_id(self):
        """
        Gets the asm_id of this ExternalAsmUserSummary.
        The `OCID`__ of the external ASM.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The asm_id of this ExternalAsmUserSummary.
        :rtype: str
        """
        return self._asm_id

    @asm_id.setter
    def asm_id(self, asm_id):
        """
        Sets the asm_id of this ExternalAsmUserSummary.
        The `OCID`__ of the external ASM.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param asm_id: The asm_id of this ExternalAsmUserSummary.
        :type: str
        """
        self._asm_id = asm_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other