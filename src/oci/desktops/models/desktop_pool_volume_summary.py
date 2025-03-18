# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220618


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DesktopPoolVolumeSummary(object):
    """
    Provides information about a volume within the desktop pool.
    """

    #: A constant which can be used with the lifecycle_state property of a DesktopPoolVolumeSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DesktopPoolVolumeSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new DesktopPoolVolumeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DesktopPoolVolumeSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this DesktopPoolVolumeSummary.
        :type name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DesktopPoolVolumeSummary.
            Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param user_name:
            The value to assign to the user_name property of this DesktopPoolVolumeSummary.
        :type user_name: str

        :param pool_id:
            The value to assign to the pool_id property of this DesktopPoolVolumeSummary.
        :type pool_id: str

        :param availability_domain:
            The value to assign to the availability_domain property of this DesktopPoolVolumeSummary.
        :type availability_domain: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DesktopPoolVolumeSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DesktopPoolVolumeSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'lifecycle_state': 'str',
            'user_name': 'str',
            'pool_id': 'str',
            'availability_domain': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'lifecycle_state': 'lifecycleState',
            'user_name': 'userName',
            'pool_id': 'poolId',
            'availability_domain': 'availabilityDomain',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._id = None
        self._name = None
        self._lifecycle_state = None
        self._user_name = None
        self._pool_id = None
        self._availability_domain = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DesktopPoolVolumeSummary.
        The OCID of the desktop pool volume.


        :return: The id of this DesktopPoolVolumeSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DesktopPoolVolumeSummary.
        The OCID of the desktop pool volume.


        :param id: The id of this DesktopPoolVolumeSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DesktopPoolVolumeSummary.
        The name of the desktop pool volume.


        :return: The name of this DesktopPoolVolumeSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DesktopPoolVolumeSummary.
        The name of the desktop pool volume.


        :param name: The name of this DesktopPoolVolumeSummary.
        :type: str
        """
        self._name = name

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DesktopPoolVolumeSummary.
        The state of the desktop pool volume.

        Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DesktopPoolVolumeSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DesktopPoolVolumeSummary.
        The state of the desktop pool volume.


        :param lifecycle_state: The lifecycle_state of this DesktopPoolVolumeSummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def user_name(self):
        """
        **[Required]** Gets the user_name of this DesktopPoolVolumeSummary.
        The owner of the desktop pool volume.


        :return: The user_name of this DesktopPoolVolumeSummary.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this DesktopPoolVolumeSummary.
        The owner of the desktop pool volume.


        :param user_name: The user_name of this DesktopPoolVolumeSummary.
        :type: str
        """
        self._user_name = user_name

    @property
    def pool_id(self):
        """
        Gets the pool_id of this DesktopPoolVolumeSummary.
        The OCID of the desktop pool to which this volume belongs.


        :return: The pool_id of this DesktopPoolVolumeSummary.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """
        Sets the pool_id of this DesktopPoolVolumeSummary.
        The OCID of the desktop pool to which this volume belongs.


        :param pool_id: The pool_id of this DesktopPoolVolumeSummary.
        :type: str
        """
        self._pool_id = pool_id

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this DesktopPoolVolumeSummary.
        The availability domain of the desktop pool.


        :return: The availability_domain of this DesktopPoolVolumeSummary.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this DesktopPoolVolumeSummary.
        The availability domain of the desktop pool.


        :param availability_domain: The availability_domain of this DesktopPoolVolumeSummary.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DesktopPoolVolumeSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this DesktopPoolVolumeSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DesktopPoolVolumeSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this DesktopPoolVolumeSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DesktopPoolVolumeSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this DesktopPoolVolumeSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DesktopPoolVolumeSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this DesktopPoolVolumeSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
