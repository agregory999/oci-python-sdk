# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20211201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResetFusionEnvironmentPasswordDetails(object):
    """
    IDM admin credentials
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResetFusionEnvironmentPasswordDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param password:
            The value to assign to the password property of this ResetFusionEnvironmentPasswordDetails.
        :type password: str

        """
        self.swagger_types = {
            'password': 'str'
        }
        self.attribute_map = {
            'password': 'password'
        }
        self._password = None

    @property
    def password(self):
        """
        **[Required]** Gets the password of this ResetFusionEnvironmentPasswordDetails.
        Admin password


        :return: The password of this ResetFusionEnvironmentPasswordDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this ResetFusionEnvironmentPasswordDetails.
        Admin password


        :param password: The password of this ResetFusionEnvironmentPasswordDetails.
        :type: str
        """
        self._password = password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
