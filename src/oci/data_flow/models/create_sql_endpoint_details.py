# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200129


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSqlEndpointDetails(object):
    """
    The information about a new SQL Endpoint.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSqlEndpointDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateSqlEndpointDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateSqlEndpointDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateSqlEndpointDetails.
        :type description: str

        :param sql_endpoint_version:
            The value to assign to the sql_endpoint_version property of this CreateSqlEndpointDetails.
        :type sql_endpoint_version: str

        :param driver_shape:
            The value to assign to the driver_shape property of this CreateSqlEndpointDetails.
        :type driver_shape: str

        :param driver_shape_config:
            The value to assign to the driver_shape_config property of this CreateSqlEndpointDetails.
        :type driver_shape_config: oci.data_flow.models.ShapeConfig

        :param executor_shape:
            The value to assign to the executor_shape property of this CreateSqlEndpointDetails.
        :type executor_shape: str

        :param executor_shape_config:
            The value to assign to the executor_shape_config property of this CreateSqlEndpointDetails.
        :type executor_shape_config: oci.data_flow.models.ShapeConfig

        :param min_executor_count:
            The value to assign to the min_executor_count property of this CreateSqlEndpointDetails.
        :type min_executor_count: int

        :param max_executor_count:
            The value to assign to the max_executor_count property of this CreateSqlEndpointDetails.
        :type max_executor_count: int

        :param metastore_id:
            The value to assign to the metastore_id property of this CreateSqlEndpointDetails.
        :type metastore_id: str

        :param lake_id:
            The value to assign to the lake_id property of this CreateSqlEndpointDetails.
        :type lake_id: str

        :param warehouse_bucket_uri:
            The value to assign to the warehouse_bucket_uri property of this CreateSqlEndpointDetails.
        :type warehouse_bucket_uri: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateSqlEndpointDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateSqlEndpointDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param spark_advanced_configurations:
            The value to assign to the spark_advanced_configurations property of this CreateSqlEndpointDetails.
        :type spark_advanced_configurations: dict(str, str)

        :param network_configuration:
            The value to assign to the network_configuration property of this CreateSqlEndpointDetails.
        :type network_configuration: oci.data_flow.models.SqlEndpointNetworkConfiguration

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'sql_endpoint_version': 'str',
            'driver_shape': 'str',
            'driver_shape_config': 'ShapeConfig',
            'executor_shape': 'str',
            'executor_shape_config': 'ShapeConfig',
            'min_executor_count': 'int',
            'max_executor_count': 'int',
            'metastore_id': 'str',
            'lake_id': 'str',
            'warehouse_bucket_uri': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'spark_advanced_configurations': 'dict(str, str)',
            'network_configuration': 'SqlEndpointNetworkConfiguration'
        }
        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'sql_endpoint_version': 'sqlEndpointVersion',
            'driver_shape': 'driverShape',
            'driver_shape_config': 'driverShapeConfig',
            'executor_shape': 'executorShape',
            'executor_shape_config': 'executorShapeConfig',
            'min_executor_count': 'minExecutorCount',
            'max_executor_count': 'maxExecutorCount',
            'metastore_id': 'metastoreId',
            'lake_id': 'lakeId',
            'warehouse_bucket_uri': 'warehouseBucketUri',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'spark_advanced_configurations': 'sparkAdvancedConfigurations',
            'network_configuration': 'networkConfiguration'
        }
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._sql_endpoint_version = None
        self._driver_shape = None
        self._driver_shape_config = None
        self._executor_shape = None
        self._executor_shape_config = None
        self._min_executor_count = None
        self._max_executor_count = None
        self._metastore_id = None
        self._lake_id = None
        self._warehouse_bucket_uri = None
        self._freeform_tags = None
        self._defined_tags = None
        self._spark_advanced_configurations = None
        self._network_configuration = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateSqlEndpointDetails.
        The identifier of the compartment used with the SQL Endpoint.


        :return: The compartment_id of this CreateSqlEndpointDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateSqlEndpointDetails.
        The identifier of the compartment used with the SQL Endpoint.


        :param compartment_id: The compartment_id of this CreateSqlEndpointDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateSqlEndpointDetails.
        The SQL Endpoint name, which can be changed.


        :return: The display_name of this CreateSqlEndpointDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateSqlEndpointDetails.
        The SQL Endpoint name, which can be changed.


        :param display_name: The display_name of this CreateSqlEndpointDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateSqlEndpointDetails.
        The description of CreateSQLEndpointDetails.


        :return: The description of this CreateSqlEndpointDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateSqlEndpointDetails.
        The description of CreateSQLEndpointDetails.


        :param description: The description of this CreateSqlEndpointDetails.
        :type: str
        """
        self._description = description

    @property
    def sql_endpoint_version(self):
        """
        **[Required]** Gets the sql_endpoint_version of this CreateSqlEndpointDetails.
        The version of the SQL Endpoint.


        :return: The sql_endpoint_version of this CreateSqlEndpointDetails.
        :rtype: str
        """
        return self._sql_endpoint_version

    @sql_endpoint_version.setter
    def sql_endpoint_version(self, sql_endpoint_version):
        """
        Sets the sql_endpoint_version of this CreateSqlEndpointDetails.
        The version of the SQL Endpoint.


        :param sql_endpoint_version: The sql_endpoint_version of this CreateSqlEndpointDetails.
        :type: str
        """
        self._sql_endpoint_version = sql_endpoint_version

    @property
    def driver_shape(self):
        """
        **[Required]** Gets the driver_shape of this CreateSqlEndpointDetails.
        The shape of the SQL Endpoint driver instance.


        :return: The driver_shape of this CreateSqlEndpointDetails.
        :rtype: str
        """
        return self._driver_shape

    @driver_shape.setter
    def driver_shape(self, driver_shape):
        """
        Sets the driver_shape of this CreateSqlEndpointDetails.
        The shape of the SQL Endpoint driver instance.


        :param driver_shape: The driver_shape of this CreateSqlEndpointDetails.
        :type: str
        """
        self._driver_shape = driver_shape

    @property
    def driver_shape_config(self):
        """
        Gets the driver_shape_config of this CreateSqlEndpointDetails.

        :return: The driver_shape_config of this CreateSqlEndpointDetails.
        :rtype: oci.data_flow.models.ShapeConfig
        """
        return self._driver_shape_config

    @driver_shape_config.setter
    def driver_shape_config(self, driver_shape_config):
        """
        Sets the driver_shape_config of this CreateSqlEndpointDetails.

        :param driver_shape_config: The driver_shape_config of this CreateSqlEndpointDetails.
        :type: oci.data_flow.models.ShapeConfig
        """
        self._driver_shape_config = driver_shape_config

    @property
    def executor_shape(self):
        """
        **[Required]** Gets the executor_shape of this CreateSqlEndpointDetails.
        The shape of the SQL Endpoint worker instance.


        :return: The executor_shape of this CreateSqlEndpointDetails.
        :rtype: str
        """
        return self._executor_shape

    @executor_shape.setter
    def executor_shape(self, executor_shape):
        """
        Sets the executor_shape of this CreateSqlEndpointDetails.
        The shape of the SQL Endpoint worker instance.


        :param executor_shape: The executor_shape of this CreateSqlEndpointDetails.
        :type: str
        """
        self._executor_shape = executor_shape

    @property
    def executor_shape_config(self):
        """
        Gets the executor_shape_config of this CreateSqlEndpointDetails.

        :return: The executor_shape_config of this CreateSqlEndpointDetails.
        :rtype: oci.data_flow.models.ShapeConfig
        """
        return self._executor_shape_config

    @executor_shape_config.setter
    def executor_shape_config(self, executor_shape_config):
        """
        Sets the executor_shape_config of this CreateSqlEndpointDetails.

        :param executor_shape_config: The executor_shape_config of this CreateSqlEndpointDetails.
        :type: oci.data_flow.models.ShapeConfig
        """
        self._executor_shape_config = executor_shape_config

    @property
    def min_executor_count(self):
        """
        **[Required]** Gets the min_executor_count of this CreateSqlEndpointDetails.
        The minimum number of executors.


        :return: The min_executor_count of this CreateSqlEndpointDetails.
        :rtype: int
        """
        return self._min_executor_count

    @min_executor_count.setter
    def min_executor_count(self, min_executor_count):
        """
        Sets the min_executor_count of this CreateSqlEndpointDetails.
        The minimum number of executors.


        :param min_executor_count: The min_executor_count of this CreateSqlEndpointDetails.
        :type: int
        """
        self._min_executor_count = min_executor_count

    @property
    def max_executor_count(self):
        """
        **[Required]** Gets the max_executor_count of this CreateSqlEndpointDetails.
        The maximum number of executors.


        :return: The max_executor_count of this CreateSqlEndpointDetails.
        :rtype: int
        """
        return self._max_executor_count

    @max_executor_count.setter
    def max_executor_count(self, max_executor_count):
        """
        Sets the max_executor_count of this CreateSqlEndpointDetails.
        The maximum number of executors.


        :param max_executor_count: The max_executor_count of this CreateSqlEndpointDetails.
        :type: int
        """
        self._max_executor_count = max_executor_count

    @property
    def metastore_id(self):
        """
        **[Required]** Gets the metastore_id of this CreateSqlEndpointDetails.
        Metastore OCID


        :return: The metastore_id of this CreateSqlEndpointDetails.
        :rtype: str
        """
        return self._metastore_id

    @metastore_id.setter
    def metastore_id(self, metastore_id):
        """
        Sets the metastore_id of this CreateSqlEndpointDetails.
        Metastore OCID


        :param metastore_id: The metastore_id of this CreateSqlEndpointDetails.
        :type: str
        """
        self._metastore_id = metastore_id

    @property
    def lake_id(self):
        """
        **[Required]** Gets the lake_id of this CreateSqlEndpointDetails.
        OCI lake OCID


        :return: The lake_id of this CreateSqlEndpointDetails.
        :rtype: str
        """
        return self._lake_id

    @lake_id.setter
    def lake_id(self, lake_id):
        """
        Sets the lake_id of this CreateSqlEndpointDetails.
        OCI lake OCID


        :param lake_id: The lake_id of this CreateSqlEndpointDetails.
        :type: str
        """
        self._lake_id = lake_id

    @property
    def warehouse_bucket_uri(self):
        """
        **[Required]** Gets the warehouse_bucket_uri of this CreateSqlEndpointDetails.
        The warehouse bucket URI. It is a Oracle Cloud Infrastructure Object Storage bucket URI as defined here https://docs.oracle.com/en/cloud/paas/atp-cloud/atpud/object-storage-uris.html


        :return: The warehouse_bucket_uri of this CreateSqlEndpointDetails.
        :rtype: str
        """
        return self._warehouse_bucket_uri

    @warehouse_bucket_uri.setter
    def warehouse_bucket_uri(self, warehouse_bucket_uri):
        """
        Sets the warehouse_bucket_uri of this CreateSqlEndpointDetails.
        The warehouse bucket URI. It is a Oracle Cloud Infrastructure Object Storage bucket URI as defined here https://docs.oracle.com/en/cloud/paas/atp-cloud/atpud/object-storage-uris.html


        :param warehouse_bucket_uri: The warehouse_bucket_uri of this CreateSqlEndpointDetails.
        :type: str
        """
        self._warehouse_bucket_uri = warehouse_bucket_uri

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateSqlEndpointDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateSqlEndpointDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateSqlEndpointDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateSqlEndpointDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateSqlEndpointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateSqlEndpointDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateSqlEndpointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateSqlEndpointDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def spark_advanced_configurations(self):
        """
        Gets the spark_advanced_configurations of this CreateSqlEndpointDetails.
        The Spark configuration passed to the running process.
        See https://spark.apache.org/docs/latest/configuration.html#available-properties.
        Example: { \"spark.app.name\" : \"My App Name\", \"spark.shuffle.io.maxRetries\" : \"4\" }
        Note: Not all Spark properties are permitted to be set.  Attempting to set a property that is
        not allowed to be overwritten will cause a 400 status to be returned.


        :return: The spark_advanced_configurations of this CreateSqlEndpointDetails.
        :rtype: dict(str, str)
        """
        return self._spark_advanced_configurations

    @spark_advanced_configurations.setter
    def spark_advanced_configurations(self, spark_advanced_configurations):
        """
        Sets the spark_advanced_configurations of this CreateSqlEndpointDetails.
        The Spark configuration passed to the running process.
        See https://spark.apache.org/docs/latest/configuration.html#available-properties.
        Example: { \"spark.app.name\" : \"My App Name\", \"spark.shuffle.io.maxRetries\" : \"4\" }
        Note: Not all Spark properties are permitted to be set.  Attempting to set a property that is
        not allowed to be overwritten will cause a 400 status to be returned.


        :param spark_advanced_configurations: The spark_advanced_configurations of this CreateSqlEndpointDetails.
        :type: dict(str, str)
        """
        self._spark_advanced_configurations = spark_advanced_configurations

    @property
    def network_configuration(self):
        """
        **[Required]** Gets the network_configuration of this CreateSqlEndpointDetails.

        :return: The network_configuration of this CreateSqlEndpointDetails.
        :rtype: oci.data_flow.models.SqlEndpointNetworkConfiguration
        """
        return self._network_configuration

    @network_configuration.setter
    def network_configuration(self, network_configuration):
        """
        Sets the network_configuration of this CreateSqlEndpointDetails.

        :param network_configuration: The network_configuration of this CreateSqlEndpointDetails.
        :type: oci.data_flow.models.SqlEndpointNetworkConfiguration
        """
        self._network_configuration = network_configuration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
