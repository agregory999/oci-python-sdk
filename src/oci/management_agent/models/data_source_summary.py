# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200202


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataSourceSummary(object):
    """
    The information about the dataSources that agent is associated to.
    """

    #: A constant which can be used with the type property of a DataSourceSummary.
    #: This constant has a value of "KUBERNETES_CLUSTER"
    TYPE_KUBERNETES_CLUSTER = "KUBERNETES_CLUSTER"

    #: A constant which can be used with the type property of a DataSourceSummary.
    #: This constant has a value of "PROMETHEUS_EMITTER"
    TYPE_PROMETHEUS_EMITTER = "PROMETHEUS_EMITTER"

    def __init__(self, **kwargs):
        """
        Initializes a new DataSourceSummary object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.management_agent.models.PrometheusEmitterDataSourceSummary`
        * :class:`~oci.management_agent.models.KubernetesClusterDataSourceSummary`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this DataSourceSummary.
        :type key: str

        :param type:
            The value to assign to the type property of this DataSourceSummary.
            Allowed values for this property are: "KUBERNETES_CLUSTER", "PROMETHEUS_EMITTER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param name:
            The value to assign to the name property of this DataSourceSummary.
        :type name: str

        """
        self.swagger_types = {
            'key': 'str',
            'type': 'str',
            'name': 'str'
        }
        self.attribute_map = {
            'key': 'key',
            'type': 'type',
            'name': 'name'
        }
        self._key = None
        self._type = None
        self._name = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'PROMETHEUS_EMITTER':
            return 'PrometheusEmitterDataSourceSummary'

        if type == 'KUBERNETES_CLUSTER':
            return 'KubernetesClusterDataSourceSummary'
        else:
            return 'DataSourceSummary'

    @property
    def key(self):
        """
        **[Required]** Gets the key of this DataSourceSummary.
        Data source type and name identifier.


        :return: The key of this DataSourceSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this DataSourceSummary.
        Data source type and name identifier.


        :param key: The key of this DataSourceSummary.
        :type: str
        """
        self._key = key

    @property
    def type(self):
        """
        **[Required]** Gets the type of this DataSourceSummary.
        The type of the dataSource.

        Allowed values for this property are: "KUBERNETES_CLUSTER", "PROMETHEUS_EMITTER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this DataSourceSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DataSourceSummary.
        The type of the dataSource.


        :param type: The type of this DataSourceSummary.
        :type: str
        """
        allowed_values = ["KUBERNETES_CLUSTER", "PROMETHEUS_EMITTER"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DataSourceSummary.
        Unique name of the dataSource.


        :return: The name of this DataSourceSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DataSourceSummary.
        Unique name of the dataSource.


        :param name: The name of this DataSourceSummary.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
