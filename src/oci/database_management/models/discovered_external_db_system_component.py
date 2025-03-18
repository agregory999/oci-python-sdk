# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DiscoveredExternalDbSystemComponent(object):
    """
    The details of an external DB system component.
    """

    #: A constant which can be used with the component_type property of a DiscoveredExternalDbSystemComponent.
    #: This constant has a value of "ASM"
    COMPONENT_TYPE_ASM = "ASM"

    #: A constant which can be used with the component_type property of a DiscoveredExternalDbSystemComponent.
    #: This constant has a value of "ASM_INSTANCE"
    COMPONENT_TYPE_ASM_INSTANCE = "ASM_INSTANCE"

    #: A constant which can be used with the component_type property of a DiscoveredExternalDbSystemComponent.
    #: This constant has a value of "CLUSTER"
    COMPONENT_TYPE_CLUSTER = "CLUSTER"

    #: A constant which can be used with the component_type property of a DiscoveredExternalDbSystemComponent.
    #: This constant has a value of "CLUSTER_INSTANCE"
    COMPONENT_TYPE_CLUSTER_INSTANCE = "CLUSTER_INSTANCE"

    #: A constant which can be used with the component_type property of a DiscoveredExternalDbSystemComponent.
    #: This constant has a value of "DATABASE"
    COMPONENT_TYPE_DATABASE = "DATABASE"

    #: A constant which can be used with the component_type property of a DiscoveredExternalDbSystemComponent.
    #: This constant has a value of "DATABASE_INSTANCE"
    COMPONENT_TYPE_DATABASE_INSTANCE = "DATABASE_INSTANCE"

    #: A constant which can be used with the component_type property of a DiscoveredExternalDbSystemComponent.
    #: This constant has a value of "DATABASE_HOME"
    COMPONENT_TYPE_DATABASE_HOME = "DATABASE_HOME"

    #: A constant which can be used with the component_type property of a DiscoveredExternalDbSystemComponent.
    #: This constant has a value of "DATABASE_NODE"
    COMPONENT_TYPE_DATABASE_NODE = "DATABASE_NODE"

    #: A constant which can be used with the component_type property of a DiscoveredExternalDbSystemComponent.
    #: This constant has a value of "DBSYSTEM"
    COMPONENT_TYPE_DBSYSTEM = "DBSYSTEM"

    #: A constant which can be used with the component_type property of a DiscoveredExternalDbSystemComponent.
    #: This constant has a value of "LISTENER"
    COMPONENT_TYPE_LISTENER = "LISTENER"

    #: A constant which can be used with the component_type property of a DiscoveredExternalDbSystemComponent.
    #: This constant has a value of "PLUGGABLE_DATABASE"
    COMPONENT_TYPE_PLUGGABLE_DATABASE = "PLUGGABLE_DATABASE"

    #: A constant which can be used with the status property of a DiscoveredExternalDbSystemComponent.
    #: This constant has a value of "NEW"
    STATUS_NEW = "NEW"

    #: A constant which can be used with the status property of a DiscoveredExternalDbSystemComponent.
    #: This constant has a value of "EXISTING"
    STATUS_EXISTING = "EXISTING"

    #: A constant which can be used with the status property of a DiscoveredExternalDbSystemComponent.
    #: This constant has a value of "MARKED_FOR_DELETION"
    STATUS_MARKED_FOR_DELETION = "MARKED_FOR_DELETION"

    #: A constant which can be used with the status property of a DiscoveredExternalDbSystemComponent.
    #: This constant has a value of "UNKNOWN"
    STATUS_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new DiscoveredExternalDbSystemComponent object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_management.models.DiscoveredExternalCluster`
        * :class:`~oci.database_management.models.DiscoveredExternalDbHome`
        * :class:`~oci.database_management.models.DiscoveredExternalDatabase`
        * :class:`~oci.database_management.models.DiscoveredExternalPluggableDatabase`
        * :class:`~oci.database_management.models.DiscoveredExternalClusterInstance`
        * :class:`~oci.database_management.models.DiscoveredExternalListener`
        * :class:`~oci.database_management.models.DiscoveredExternalDbNode`
        * :class:`~oci.database_management.models.DiscoveredExternalAsm`
        * :class:`~oci.database_management.models.DiscoveredExternalAsmInstance`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param component_id:
            The value to assign to the component_id property of this DiscoveredExternalDbSystemComponent.
        :type component_id: str

        :param display_name:
            The value to assign to the display_name property of this DiscoveredExternalDbSystemComponent.
        :type display_name: str

        :param component_name:
            The value to assign to the component_name property of this DiscoveredExternalDbSystemComponent.
        :type component_name: str

        :param component_type:
            The value to assign to the component_type property of this DiscoveredExternalDbSystemComponent.
            Allowed values for this property are: "ASM", "ASM_INSTANCE", "CLUSTER", "CLUSTER_INSTANCE", "DATABASE", "DATABASE_INSTANCE", "DATABASE_HOME", "DATABASE_NODE", "DBSYSTEM", "LISTENER", "PLUGGABLE_DATABASE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type component_type: str

        :param resource_id:
            The value to assign to the resource_id property of this DiscoveredExternalDbSystemComponent.
        :type resource_id: str

        :param is_selected_for_monitoring:
            The value to assign to the is_selected_for_monitoring property of this DiscoveredExternalDbSystemComponent.
        :type is_selected_for_monitoring: bool

        :param status:
            The value to assign to the status property of this DiscoveredExternalDbSystemComponent.
            Allowed values for this property are: "NEW", "EXISTING", "MARKED_FOR_DELETION", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param associated_components:
            The value to assign to the associated_components property of this DiscoveredExternalDbSystemComponent.
        :type associated_components: list[oci.database_management.models.AssociatedComponent]

        """
        self.swagger_types = {
            'component_id': 'str',
            'display_name': 'str',
            'component_name': 'str',
            'component_type': 'str',
            'resource_id': 'str',
            'is_selected_for_monitoring': 'bool',
            'status': 'str',
            'associated_components': 'list[AssociatedComponent]'
        }
        self.attribute_map = {
            'component_id': 'componentId',
            'display_name': 'displayName',
            'component_name': 'componentName',
            'component_type': 'componentType',
            'resource_id': 'resourceId',
            'is_selected_for_monitoring': 'isSelectedForMonitoring',
            'status': 'status',
            'associated_components': 'associatedComponents'
        }
        self._component_id = None
        self._display_name = None
        self._component_name = None
        self._component_type = None
        self._resource_id = None
        self._is_selected_for_monitoring = None
        self._status = None
        self._associated_components = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['componentType']

        if type == 'CLUSTER':
            return 'DiscoveredExternalCluster'

        if type == 'DATABASE_HOME':
            return 'DiscoveredExternalDbHome'

        if type == 'DATABASE':
            return 'DiscoveredExternalDatabase'

        if type == 'PLUGGABLE_DATABASE':
            return 'DiscoveredExternalPluggableDatabase'

        if type == 'CLUSTER_INSTANCE':
            return 'DiscoveredExternalClusterInstance'

        if type == 'LISTENER':
            return 'DiscoveredExternalListener'

        if type == 'DATABASE_NODE':
            return 'DiscoveredExternalDbNode'

        if type == 'ASM':
            return 'DiscoveredExternalAsm'

        if type == 'ASM_INSTANCE':
            return 'DiscoveredExternalAsmInstance'
        else:
            return 'DiscoveredExternalDbSystemComponent'

    @property
    def component_id(self):
        """
        **[Required]** Gets the component_id of this DiscoveredExternalDbSystemComponent.
        The identifier of the discovered DB system component.


        :return: The component_id of this DiscoveredExternalDbSystemComponent.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """
        Sets the component_id of this DiscoveredExternalDbSystemComponent.
        The identifier of the discovered DB system component.


        :param component_id: The component_id of this DiscoveredExternalDbSystemComponent.
        :type: str
        """
        self._component_id = component_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DiscoveredExternalDbSystemComponent.
        The user-friendly name for the discovered DB system component. The name does not have to be unique.


        :return: The display_name of this DiscoveredExternalDbSystemComponent.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DiscoveredExternalDbSystemComponent.
        The user-friendly name for the discovered DB system component. The name does not have to be unique.


        :param display_name: The display_name of this DiscoveredExternalDbSystemComponent.
        :type: str
        """
        self._display_name = display_name

    @property
    def component_name(self):
        """
        **[Required]** Gets the component_name of this DiscoveredExternalDbSystemComponent.
        The name of the discovered DB system component.


        :return: The component_name of this DiscoveredExternalDbSystemComponent.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        """
        Sets the component_name of this DiscoveredExternalDbSystemComponent.
        The name of the discovered DB system component.


        :param component_name: The component_name of this DiscoveredExternalDbSystemComponent.
        :type: str
        """
        self._component_name = component_name

    @property
    def component_type(self):
        """
        **[Required]** Gets the component_type of this DiscoveredExternalDbSystemComponent.
        The external DB system component type.

        Allowed values for this property are: "ASM", "ASM_INSTANCE", "CLUSTER", "CLUSTER_INSTANCE", "DATABASE", "DATABASE_INSTANCE", "DATABASE_HOME", "DATABASE_NODE", "DBSYSTEM", "LISTENER", "PLUGGABLE_DATABASE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The component_type of this DiscoveredExternalDbSystemComponent.
        :rtype: str
        """
        return self._component_type

    @component_type.setter
    def component_type(self, component_type):
        """
        Sets the component_type of this DiscoveredExternalDbSystemComponent.
        The external DB system component type.


        :param component_type: The component_type of this DiscoveredExternalDbSystemComponent.
        :type: str
        """
        allowed_values = ["ASM", "ASM_INSTANCE", "CLUSTER", "CLUSTER_INSTANCE", "DATABASE", "DATABASE_INSTANCE", "DATABASE_HOME", "DATABASE_NODE", "DBSYSTEM", "LISTENER", "PLUGGABLE_DATABASE"]
        if not value_allowed_none_or_none_sentinel(component_type, allowed_values):
            component_type = 'UNKNOWN_ENUM_VALUE'
        self._component_type = component_type

    @property
    def resource_id(self):
        """
        Gets the resource_id of this DiscoveredExternalDbSystemComponent.
        The `OCID`__ of the existing OCI resource matching the discovered DB system component.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The resource_id of this DiscoveredExternalDbSystemComponent.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this DiscoveredExternalDbSystemComponent.
        The `OCID`__ of the existing OCI resource matching the discovered DB system component.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param resource_id: The resource_id of this DiscoveredExternalDbSystemComponent.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def is_selected_for_monitoring(self):
        """
        Gets the is_selected_for_monitoring of this DiscoveredExternalDbSystemComponent.
        Indicates whether the DB system component should be provisioned as an OCI resource or not.


        :return: The is_selected_for_monitoring of this DiscoveredExternalDbSystemComponent.
        :rtype: bool
        """
        return self._is_selected_for_monitoring

    @is_selected_for_monitoring.setter
    def is_selected_for_monitoring(self, is_selected_for_monitoring):
        """
        Sets the is_selected_for_monitoring of this DiscoveredExternalDbSystemComponent.
        Indicates whether the DB system component should be provisioned as an OCI resource or not.


        :param is_selected_for_monitoring: The is_selected_for_monitoring of this DiscoveredExternalDbSystemComponent.
        :type: bool
        """
        self._is_selected_for_monitoring = is_selected_for_monitoring

    @property
    def status(self):
        """
        Gets the status of this DiscoveredExternalDbSystemComponent.
        The state of the discovered DB system component.

        Allowed values for this property are: "NEW", "EXISTING", "MARKED_FOR_DELETION", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this DiscoveredExternalDbSystemComponent.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this DiscoveredExternalDbSystemComponent.
        The state of the discovered DB system component.


        :param status: The status of this DiscoveredExternalDbSystemComponent.
        :type: str
        """
        allowed_values = ["NEW", "EXISTING", "MARKED_FOR_DELETION", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def associated_components(self):
        """
        Gets the associated_components of this DiscoveredExternalDbSystemComponent.
        The list of associated components.


        :return: The associated_components of this DiscoveredExternalDbSystemComponent.
        :rtype: list[oci.database_management.models.AssociatedComponent]
        """
        return self._associated_components

    @associated_components.setter
    def associated_components(self, associated_components):
        """
        Sets the associated_components of this DiscoveredExternalDbSystemComponent.
        The list of associated components.


        :param associated_components: The associated_components of this DiscoveredExternalDbSystemComponent.
        :type: list[oci.database_management.models.AssociatedComponent]
        """
        self._associated_components = associated_components

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
