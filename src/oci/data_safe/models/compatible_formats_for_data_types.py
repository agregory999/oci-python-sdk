# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CompatibleFormatsForDataTypes(object):
    """
    A list of basic masking formats compatible with and grouped by the supported data types. The data types are grouped into
    the following categories -
    Character - Includes CHAR, NCHAR, VARCHAR2, and NVARCHAR2
    Numeric - Includes NUMBER, FLOAT, RAW, BINARY_FLOAT, and BINARY_DOUBLE
    Date - Includes DATE and TIMESTAMP
    LOB - Includes BLOB, CLOB, and NCLOB
    All - Includes all the supported data types
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CompatibleFormatsForDataTypes object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param formats_for_data_type:
            The value to assign to the formats_for_data_type property of this CompatibleFormatsForDataTypes.
        :type formats_for_data_type: list[oci.data_safe.models.FormatsForDataType]

        """
        self.swagger_types = {
            'formats_for_data_type': 'list[FormatsForDataType]'
        }

        self.attribute_map = {
            'formats_for_data_type': 'formatsForDataType'
        }

        self._formats_for_data_type = None

    @property
    def formats_for_data_type(self):
        """
        **[Required]** Gets the formats_for_data_type of this CompatibleFormatsForDataTypes.
        An array of lists of basic masking formats compatible with the supported data types.


        :return: The formats_for_data_type of this CompatibleFormatsForDataTypes.
        :rtype: list[oci.data_safe.models.FormatsForDataType]
        """
        return self._formats_for_data_type

    @formats_for_data_type.setter
    def formats_for_data_type(self, formats_for_data_type):
        """
        Sets the formats_for_data_type of this CompatibleFormatsForDataTypes.
        An array of lists of basic masking formats compatible with the supported data types.


        :param formats_for_data_type: The formats_for_data_type of this CompatibleFormatsForDataTypes.
        :type: list[oci.data_safe.models.FormatsForDataType]
        """
        self._formats_for_data_type = formats_for_data_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
