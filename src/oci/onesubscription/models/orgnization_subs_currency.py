# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OrgnizationSubsCurrency(object):
    """
    Currency details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OrgnizationSubsCurrency object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this OrgnizationSubsCurrency.
        :type name: str

        :param iso_code:
            The value to assign to the iso_code property of this OrgnizationSubsCurrency.
        :type iso_code: str

        :param std_precision:
            The value to assign to the std_precision property of this OrgnizationSubsCurrency.
        :type std_precision: int

        """
        self.swagger_types = {
            'name': 'str',
            'iso_code': 'str',
            'std_precision': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'iso_code': 'isoCode',
            'std_precision': 'stdPrecision'
        }

        self._name = None
        self._iso_code = None
        self._std_precision = None

    @property
    def name(self):
        """
        Gets the name of this OrgnizationSubsCurrency.
        Currency name


        :return: The name of this OrgnizationSubsCurrency.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OrgnizationSubsCurrency.
        Currency name


        :param name: The name of this OrgnizationSubsCurrency.
        :type: str
        """
        self._name = name

    @property
    def iso_code(self):
        """
        **[Required]** Gets the iso_code of this OrgnizationSubsCurrency.
        Currency Code


        :return: The iso_code of this OrgnizationSubsCurrency.
        :rtype: str
        """
        return self._iso_code

    @iso_code.setter
    def iso_code(self, iso_code):
        """
        Sets the iso_code of this OrgnizationSubsCurrency.
        Currency Code


        :param iso_code: The iso_code of this OrgnizationSubsCurrency.
        :type: str
        """
        self._iso_code = iso_code

    @property
    def std_precision(self):
        """
        Gets the std_precision of this OrgnizationSubsCurrency.
        Standard Precision of the Currency


        :return: The std_precision of this OrgnizationSubsCurrency.
        :rtype: int
        """
        return self._std_precision

    @std_precision.setter
    def std_precision(self, std_precision):
        """
        Sets the std_precision of this OrgnizationSubsCurrency.
        Standard Precision of the Currency


        :param std_precision: The std_precision of this OrgnizationSubsCurrency.
        :type: int
        """
        self._std_precision = std_precision

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
