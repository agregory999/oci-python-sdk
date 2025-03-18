# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AwrHubSourceSummary(object):
    """
    Awr hub source object
    """

    #: A constant which can be used with the type property of a AwrHubSourceSummary.
    #: This constant has a value of "ADW_S"
    TYPE_ADW_S = "ADW_S"

    #: A constant which can be used with the type property of a AwrHubSourceSummary.
    #: This constant has a value of "ATP_S"
    TYPE_ATP_S = "ATP_S"

    #: A constant which can be used with the type property of a AwrHubSourceSummary.
    #: This constant has a value of "ADW_D"
    TYPE_ADW_D = "ADW_D"

    #: A constant which can be used with the type property of a AwrHubSourceSummary.
    #: This constant has a value of "ATP_D"
    TYPE_ATP_D = "ATP_D"

    #: A constant which can be used with the type property of a AwrHubSourceSummary.
    #: This constant has a value of "EXTERNAL_PDB"
    TYPE_EXTERNAL_PDB = "EXTERNAL_PDB"

    #: A constant which can be used with the type property of a AwrHubSourceSummary.
    #: This constant has a value of "EXTERNAL_NONCDB"
    TYPE_EXTERNAL_NONCDB = "EXTERNAL_NONCDB"

    #: A constant which can be used with the type property of a AwrHubSourceSummary.
    #: This constant has a value of "COMANAGED_VM_CDB"
    TYPE_COMANAGED_VM_CDB = "COMANAGED_VM_CDB"

    #: A constant which can be used with the type property of a AwrHubSourceSummary.
    #: This constant has a value of "COMANAGED_VM_PDB"
    TYPE_COMANAGED_VM_PDB = "COMANAGED_VM_PDB"

    #: A constant which can be used with the type property of a AwrHubSourceSummary.
    #: This constant has a value of "COMANAGED_VM_NONCDB"
    TYPE_COMANAGED_VM_NONCDB = "COMANAGED_VM_NONCDB"

    #: A constant which can be used with the type property of a AwrHubSourceSummary.
    #: This constant has a value of "COMANAGED_BM_CDB"
    TYPE_COMANAGED_BM_CDB = "COMANAGED_BM_CDB"

    #: A constant which can be used with the type property of a AwrHubSourceSummary.
    #: This constant has a value of "COMANAGED_BM_PDB"
    TYPE_COMANAGED_BM_PDB = "COMANAGED_BM_PDB"

    #: A constant which can be used with the type property of a AwrHubSourceSummary.
    #: This constant has a value of "COMANAGED_BM_NONCDB"
    TYPE_COMANAGED_BM_NONCDB = "COMANAGED_BM_NONCDB"

    #: A constant which can be used with the type property of a AwrHubSourceSummary.
    #: This constant has a value of "COMANAGED_EXACS_CDB"
    TYPE_COMANAGED_EXACS_CDB = "COMANAGED_EXACS_CDB"

    #: A constant which can be used with the type property of a AwrHubSourceSummary.
    #: This constant has a value of "COMANAGED_EXACS_PDB"
    TYPE_COMANAGED_EXACS_PDB = "COMANAGED_EXACS_PDB"

    #: A constant which can be used with the type property of a AwrHubSourceSummary.
    #: This constant has a value of "COMANAGED_EXACS_NONCDB"
    TYPE_COMANAGED_EXACS_NONCDB = "COMANAGED_EXACS_NONCDB"

    #: A constant which can be used with the type property of a AwrHubSourceSummary.
    #: This constant has a value of "UNDEFINED"
    TYPE_UNDEFINED = "UNDEFINED"

    #: A constant which can be used with the lifecycle_state property of a AwrHubSourceSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a AwrHubSourceSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AwrHubSourceSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AwrHubSourceSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a AwrHubSourceSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a AwrHubSourceSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the status property of a AwrHubSourceSummary.
    #: This constant has a value of "ACCEPTING"
    STATUS_ACCEPTING = "ACCEPTING"

    #: A constant which can be used with the status property of a AwrHubSourceSummary.
    #: This constant has a value of "NOT_ACCEPTING"
    STATUS_NOT_ACCEPTING = "NOT_ACCEPTING"

    #: A constant which can be used with the status property of a AwrHubSourceSummary.
    #: This constant has a value of "NOT_REGISTERED"
    STATUS_NOT_REGISTERED = "NOT_REGISTERED"

    #: A constant which can be used with the status property of a AwrHubSourceSummary.
    #: This constant has a value of "TERMINATED"
    STATUS_TERMINATED = "TERMINATED"

    def __init__(self, **kwargs):
        """
        Initializes a new AwrHubSourceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AwrHubSourceSummary.
        :type name: str

        :param awr_hub_id:
            The value to assign to the awr_hub_id property of this AwrHubSourceSummary.
        :type awr_hub_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AwrHubSourceSummary.
        :type compartment_id: str

        :param type:
            The value to assign to the type property of this AwrHubSourceSummary.
            Allowed values for this property are: "ADW_S", "ATP_S", "ADW_D", "ATP_D", "EXTERNAL_PDB", "EXTERNAL_NONCDB", "COMANAGED_VM_CDB", "COMANAGED_VM_PDB", "COMANAGED_VM_NONCDB", "COMANAGED_BM_CDB", "COMANAGED_BM_PDB", "COMANAGED_BM_NONCDB", "COMANAGED_EXACS_CDB", "COMANAGED_EXACS_PDB", "COMANAGED_EXACS_NONCDB", "UNDEFINED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param id:
            The value to assign to the id property of this AwrHubSourceSummary.
        :type id: str

        :param awr_hub_opsi_source_id:
            The value to assign to the awr_hub_opsi_source_id property of this AwrHubSourceSummary.
        :type awr_hub_opsi_source_id: str

        :param source_mail_box_url:
            The value to assign to the source_mail_box_url property of this AwrHubSourceSummary.
        :type source_mail_box_url: str

        :param associated_resource_id:
            The value to assign to the associated_resource_id property of this AwrHubSourceSummary.
        :type associated_resource_id: str

        :param associated_opsi_id:
            The value to assign to the associated_opsi_id property of this AwrHubSourceSummary.
        :type associated_opsi_id: str

        :param time_created:
            The value to assign to the time_created property of this AwrHubSourceSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AwrHubSourceSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AwrHubSourceSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AwrHubSourceSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this AwrHubSourceSummary.
        :type system_tags: dict(str, dict(str, object))

        :param is_registered_with_awr_hub:
            The value to assign to the is_registered_with_awr_hub property of this AwrHubSourceSummary.
        :type is_registered_with_awr_hub: bool

        :param awr_source_database_id:
            The value to assign to the awr_source_database_id property of this AwrHubSourceSummary.
        :type awr_source_database_id: str

        :param min_snapshot_identifier:
            The value to assign to the min_snapshot_identifier property of this AwrHubSourceSummary.
        :type min_snapshot_identifier: float

        :param max_snapshot_identifier:
            The value to assign to the max_snapshot_identifier property of this AwrHubSourceSummary.
        :type max_snapshot_identifier: float

        :param time_first_snapshot_generated:
            The value to assign to the time_first_snapshot_generated property of this AwrHubSourceSummary.
        :type time_first_snapshot_generated: datetime

        :param time_last_snapshot_generated:
            The value to assign to the time_last_snapshot_generated property of this AwrHubSourceSummary.
        :type time_last_snapshot_generated: datetime

        :param hours_since_last_import:
            The value to assign to the hours_since_last_import property of this AwrHubSourceSummary.
        :type hours_since_last_import: float

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AwrHubSourceSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param status:
            The value to assign to the status property of this AwrHubSourceSummary.
            Allowed values for this property are: "ACCEPTING", "NOT_ACCEPTING", "NOT_REGISTERED", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        """
        self.swagger_types = {
            'name': 'str',
            'awr_hub_id': 'str',
            'compartment_id': 'str',
            'type': 'str',
            'id': 'str',
            'awr_hub_opsi_source_id': 'str',
            'source_mail_box_url': 'str',
            'associated_resource_id': 'str',
            'associated_opsi_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'is_registered_with_awr_hub': 'bool',
            'awr_source_database_id': 'str',
            'min_snapshot_identifier': 'float',
            'max_snapshot_identifier': 'float',
            'time_first_snapshot_generated': 'datetime',
            'time_last_snapshot_generated': 'datetime',
            'hours_since_last_import': 'float',
            'lifecycle_state': 'str',
            'status': 'str'
        }
        self.attribute_map = {
            'name': 'name',
            'awr_hub_id': 'awrHubId',
            'compartment_id': 'compartmentId',
            'type': 'type',
            'id': 'id',
            'awr_hub_opsi_source_id': 'awrHubOpsiSourceId',
            'source_mail_box_url': 'sourceMailBoxUrl',
            'associated_resource_id': 'associatedResourceId',
            'associated_opsi_id': 'associatedOpsiId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'is_registered_with_awr_hub': 'isRegisteredWithAwrHub',
            'awr_source_database_id': 'awrSourceDatabaseId',
            'min_snapshot_identifier': 'minSnapshotIdentifier',
            'max_snapshot_identifier': 'maxSnapshotIdentifier',
            'time_first_snapshot_generated': 'timeFirstSnapshotGenerated',
            'time_last_snapshot_generated': 'timeLastSnapshotGenerated',
            'hours_since_last_import': 'hoursSinceLastImport',
            'lifecycle_state': 'lifecycleState',
            'status': 'status'
        }
        self._name = None
        self._awr_hub_id = None
        self._compartment_id = None
        self._type = None
        self._id = None
        self._awr_hub_opsi_source_id = None
        self._source_mail_box_url = None
        self._associated_resource_id = None
        self._associated_opsi_id = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._is_registered_with_awr_hub = None
        self._awr_source_database_id = None
        self._min_snapshot_identifier = None
        self._max_snapshot_identifier = None
        self._time_first_snapshot_generated = None
        self._time_last_snapshot_generated = None
        self._hours_since_last_import = None
        self._lifecycle_state = None
        self._status = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AwrHubSourceSummary.
        The name of the Awr Hub source database.


        :return: The name of this AwrHubSourceSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AwrHubSourceSummary.
        The name of the Awr Hub source database.


        :param name: The name of this AwrHubSourceSummary.
        :type: str
        """
        self._name = name

    @property
    def awr_hub_id(self):
        """
        **[Required]** Gets the awr_hub_id of this AwrHubSourceSummary.
        AWR Hub OCID


        :return: The awr_hub_id of this AwrHubSourceSummary.
        :rtype: str
        """
        return self._awr_hub_id

    @awr_hub_id.setter
    def awr_hub_id(self, awr_hub_id):
        """
        Sets the awr_hub_id of this AwrHubSourceSummary.
        AWR Hub OCID


        :param awr_hub_id: The awr_hub_id of this AwrHubSourceSummary.
        :type: str
        """
        self._awr_hub_id = awr_hub_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AwrHubSourceSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this AwrHubSourceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AwrHubSourceSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this AwrHubSourceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def type(self):
        """
        **[Required]** Gets the type of this AwrHubSourceSummary.
        source type of the database

        Allowed values for this property are: "ADW_S", "ATP_S", "ADW_D", "ATP_D", "EXTERNAL_PDB", "EXTERNAL_NONCDB", "COMANAGED_VM_CDB", "COMANAGED_VM_PDB", "COMANAGED_VM_NONCDB", "COMANAGED_BM_CDB", "COMANAGED_BM_PDB", "COMANAGED_BM_NONCDB", "COMANAGED_EXACS_CDB", "COMANAGED_EXACS_PDB", "COMANAGED_EXACS_NONCDB", "UNDEFINED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this AwrHubSourceSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AwrHubSourceSummary.
        source type of the database


        :param type: The type of this AwrHubSourceSummary.
        :type: str
        """
        allowed_values = ["ADW_S", "ATP_S", "ADW_D", "ATP_D", "EXTERNAL_PDB", "EXTERNAL_NONCDB", "COMANAGED_VM_CDB", "COMANAGED_VM_PDB", "COMANAGED_VM_NONCDB", "COMANAGED_BM_CDB", "COMANAGED_BM_PDB", "COMANAGED_BM_NONCDB", "COMANAGED_EXACS_CDB", "COMANAGED_EXACS_PDB", "COMANAGED_EXACS_NONCDB", "UNDEFINED"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AwrHubSourceSummary.
        The `OCID`__ of the Awr Hub source database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this AwrHubSourceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AwrHubSourceSummary.
        The `OCID`__ of the Awr Hub source database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this AwrHubSourceSummary.
        :type: str
        """
        self._id = id

    @property
    def awr_hub_opsi_source_id(self):
        """
        **[Required]** Gets the awr_hub_opsi_source_id of this AwrHubSourceSummary.
        The shorted string of the Awr Hub source database identifier.


        :return: The awr_hub_opsi_source_id of this AwrHubSourceSummary.
        :rtype: str
        """
        return self._awr_hub_opsi_source_id

    @awr_hub_opsi_source_id.setter
    def awr_hub_opsi_source_id(self, awr_hub_opsi_source_id):
        """
        Sets the awr_hub_opsi_source_id of this AwrHubSourceSummary.
        The shorted string of the Awr Hub source database identifier.


        :param awr_hub_opsi_source_id: The awr_hub_opsi_source_id of this AwrHubSourceSummary.
        :type: str
        """
        self._awr_hub_opsi_source_id = awr_hub_opsi_source_id

    @property
    def source_mail_box_url(self):
        """
        **[Required]** Gets the source_mail_box_url of this AwrHubSourceSummary.
        Opsi Mailbox URL based on the Awr Hub and Awr Hub source.


        :return: The source_mail_box_url of this AwrHubSourceSummary.
        :rtype: str
        """
        return self._source_mail_box_url

    @source_mail_box_url.setter
    def source_mail_box_url(self, source_mail_box_url):
        """
        Sets the source_mail_box_url of this AwrHubSourceSummary.
        Opsi Mailbox URL based on the Awr Hub and Awr Hub source.


        :param source_mail_box_url: The source_mail_box_url of this AwrHubSourceSummary.
        :type: str
        """
        self._source_mail_box_url = source_mail_box_url

    @property
    def associated_resource_id(self):
        """
        Gets the associated_resource_id of this AwrHubSourceSummary.
        The `OCID`__ of the database id.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The associated_resource_id of this AwrHubSourceSummary.
        :rtype: str
        """
        return self._associated_resource_id

    @associated_resource_id.setter
    def associated_resource_id(self, associated_resource_id):
        """
        Sets the associated_resource_id of this AwrHubSourceSummary.
        The `OCID`__ of the database id.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param associated_resource_id: The associated_resource_id of this AwrHubSourceSummary.
        :type: str
        """
        self._associated_resource_id = associated_resource_id

    @property
    def associated_opsi_id(self):
        """
        Gets the associated_opsi_id of this AwrHubSourceSummary.
        The `OCID`__ of the database id.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The associated_opsi_id of this AwrHubSourceSummary.
        :rtype: str
        """
        return self._associated_opsi_id

    @associated_opsi_id.setter
    def associated_opsi_id(self, associated_opsi_id):
        """
        Sets the associated_opsi_id of this AwrHubSourceSummary.
        The `OCID`__ of the database id.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param associated_opsi_id: The associated_opsi_id of this AwrHubSourceSummary.
        :type: str
        """
        self._associated_opsi_id = associated_opsi_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this AwrHubSourceSummary.
        The time at which the resource was first created. An RFC3339 formatted datetime string


        :return: The time_created of this AwrHubSourceSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AwrHubSourceSummary.
        The time at which the resource was first created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this AwrHubSourceSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this AwrHubSourceSummary.
        The time at which the resource was last updated. An RFC3339 formatted datetime string


        :return: The time_updated of this AwrHubSourceSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AwrHubSourceSummary.
        The time at which the resource was last updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this AwrHubSourceSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AwrHubSourceSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this AwrHubSourceSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AwrHubSourceSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this AwrHubSourceSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AwrHubSourceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this AwrHubSourceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AwrHubSourceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this AwrHubSourceSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this AwrHubSourceSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this AwrHubSourceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this AwrHubSourceSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this AwrHubSourceSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def is_registered_with_awr_hub(self):
        """
        Gets the is_registered_with_awr_hub of this AwrHubSourceSummary.
        This is `true` if the source databse is registered with a Awr Hub, otherwise `false`


        :return: The is_registered_with_awr_hub of this AwrHubSourceSummary.
        :rtype: bool
        """
        return self._is_registered_with_awr_hub

    @is_registered_with_awr_hub.setter
    def is_registered_with_awr_hub(self, is_registered_with_awr_hub):
        """
        Sets the is_registered_with_awr_hub of this AwrHubSourceSummary.
        This is `true` if the source databse is registered with a Awr Hub, otherwise `false`


        :param is_registered_with_awr_hub: The is_registered_with_awr_hub of this AwrHubSourceSummary.
        :type: bool
        """
        self._is_registered_with_awr_hub = is_registered_with_awr_hub

    @property
    def awr_source_database_id(self):
        """
        Gets the awr_source_database_id of this AwrHubSourceSummary.
        DatabaseId of the Source database for which AWR Data will be uploaded to AWR Hub.


        :return: The awr_source_database_id of this AwrHubSourceSummary.
        :rtype: str
        """
        return self._awr_source_database_id

    @awr_source_database_id.setter
    def awr_source_database_id(self, awr_source_database_id):
        """
        Sets the awr_source_database_id of this AwrHubSourceSummary.
        DatabaseId of the Source database for which AWR Data will be uploaded to AWR Hub.


        :param awr_source_database_id: The awr_source_database_id of this AwrHubSourceSummary.
        :type: str
        """
        self._awr_source_database_id = awr_source_database_id

    @property
    def min_snapshot_identifier(self):
        """
        Gets the min_snapshot_identifier of this AwrHubSourceSummary.
        The minimum snapshot identifier of the source database for which AWR data is uploaded to AWR Hub.


        :return: The min_snapshot_identifier of this AwrHubSourceSummary.
        :rtype: float
        """
        return self._min_snapshot_identifier

    @min_snapshot_identifier.setter
    def min_snapshot_identifier(self, min_snapshot_identifier):
        """
        Sets the min_snapshot_identifier of this AwrHubSourceSummary.
        The minimum snapshot identifier of the source database for which AWR data is uploaded to AWR Hub.


        :param min_snapshot_identifier: The min_snapshot_identifier of this AwrHubSourceSummary.
        :type: float
        """
        self._min_snapshot_identifier = min_snapshot_identifier

    @property
    def max_snapshot_identifier(self):
        """
        Gets the max_snapshot_identifier of this AwrHubSourceSummary.
        The maximum snapshot identifier of the source database for which AWR data is uploaded to AWR Hub.


        :return: The max_snapshot_identifier of this AwrHubSourceSummary.
        :rtype: float
        """
        return self._max_snapshot_identifier

    @max_snapshot_identifier.setter
    def max_snapshot_identifier(self, max_snapshot_identifier):
        """
        Sets the max_snapshot_identifier of this AwrHubSourceSummary.
        The maximum snapshot identifier of the source database for which AWR data is uploaded to AWR Hub.


        :param max_snapshot_identifier: The max_snapshot_identifier of this AwrHubSourceSummary.
        :type: float
        """
        self._max_snapshot_identifier = max_snapshot_identifier

    @property
    def time_first_snapshot_generated(self):
        """
        Gets the time_first_snapshot_generated of this AwrHubSourceSummary.
        The time at which the earliest snapshot was generated in the source database for which data is uploaded to AWR Hub. An RFC3339 formatted datetime string


        :return: The time_first_snapshot_generated of this AwrHubSourceSummary.
        :rtype: datetime
        """
        return self._time_first_snapshot_generated

    @time_first_snapshot_generated.setter
    def time_first_snapshot_generated(self, time_first_snapshot_generated):
        """
        Sets the time_first_snapshot_generated of this AwrHubSourceSummary.
        The time at which the earliest snapshot was generated in the source database for which data is uploaded to AWR Hub. An RFC3339 formatted datetime string


        :param time_first_snapshot_generated: The time_first_snapshot_generated of this AwrHubSourceSummary.
        :type: datetime
        """
        self._time_first_snapshot_generated = time_first_snapshot_generated

    @property
    def time_last_snapshot_generated(self):
        """
        Gets the time_last_snapshot_generated of this AwrHubSourceSummary.
        The time at which the latest snapshot was generated in the source database for which data is uploaded to AWR Hub. An RFC3339 formatted datetime string


        :return: The time_last_snapshot_generated of this AwrHubSourceSummary.
        :rtype: datetime
        """
        return self._time_last_snapshot_generated

    @time_last_snapshot_generated.setter
    def time_last_snapshot_generated(self, time_last_snapshot_generated):
        """
        Sets the time_last_snapshot_generated of this AwrHubSourceSummary.
        The time at which the latest snapshot was generated in the source database for which data is uploaded to AWR Hub. An RFC3339 formatted datetime string


        :param time_last_snapshot_generated: The time_last_snapshot_generated of this AwrHubSourceSummary.
        :type: datetime
        """
        self._time_last_snapshot_generated = time_last_snapshot_generated

    @property
    def hours_since_last_import(self):
        """
        Gets the hours_since_last_import of this AwrHubSourceSummary.
        Number of hours since last AWR snapshots import happened from the Source database.


        :return: The hours_since_last_import of this AwrHubSourceSummary.
        :rtype: float
        """
        return self._hours_since_last_import

    @hours_since_last_import.setter
    def hours_since_last_import(self, hours_since_last_import):
        """
        Sets the hours_since_last_import of this AwrHubSourceSummary.
        Number of hours since last AWR snapshots import happened from the Source database.


        :param hours_since_last_import: The hours_since_last_import of this AwrHubSourceSummary.
        :type: float
        """
        self._hours_since_last_import = hours_since_last_import

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AwrHubSourceSummary.
        the current state of the source database

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AwrHubSourceSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AwrHubSourceSummary.
        the current state of the source database


        :param lifecycle_state: The lifecycle_state of this AwrHubSourceSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def status(self):
        """
        **[Required]** Gets the status of this AwrHubSourceSummary.
        Indicates the status of a source database in Operations Insights

        Allowed values for this property are: "ACCEPTING", "NOT_ACCEPTING", "NOT_REGISTERED", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this AwrHubSourceSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AwrHubSourceSummary.
        Indicates the status of a source database in Operations Insights


        :param status: The status of this AwrHubSourceSummary.
        :type: str
        """
        allowed_values = ["ACCEPTING", "NOT_ACCEPTING", "NOT_REGISTERED", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
