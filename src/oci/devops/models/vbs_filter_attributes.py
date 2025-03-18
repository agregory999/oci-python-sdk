# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VbsFilterAttributes(object):
    """
    Attributes to filter VBS events.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VbsFilterAttributes object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param head_ref:
            The value to assign to the head_ref property of this VbsFilterAttributes.
        :type head_ref: str

        :param base_ref:
            The value to assign to the base_ref property of this VbsFilterAttributes.
        :type base_ref: str

        :param repository_name:
            The value to assign to the repository_name property of this VbsFilterAttributes.
        :type repository_name: str

        :param file_filter:
            The value to assign to the file_filter property of this VbsFilterAttributes.
        :type file_filter: oci.devops.models.FileFilter

        """
        self.swagger_types = {
            'head_ref': 'str',
            'base_ref': 'str',
            'repository_name': 'str',
            'file_filter': 'FileFilter'
        }
        self.attribute_map = {
            'head_ref': 'headRef',
            'base_ref': 'baseRef',
            'repository_name': 'repositoryName',
            'file_filter': 'fileFilter'
        }
        self._head_ref = None
        self._base_ref = None
        self._repository_name = None
        self._file_filter = None

    @property
    def head_ref(self):
        """
        Gets the head_ref of this VbsFilterAttributes.
        Branch for push event; source branch for pull requests.


        :return: The head_ref of this VbsFilterAttributes.
        :rtype: str
        """
        return self._head_ref

    @head_ref.setter
    def head_ref(self, head_ref):
        """
        Sets the head_ref of this VbsFilterAttributes.
        Branch for push event; source branch for pull requests.


        :param head_ref: The head_ref of this VbsFilterAttributes.
        :type: str
        """
        self._head_ref = head_ref

    @property
    def base_ref(self):
        """
        Gets the base_ref of this VbsFilterAttributes.
        The target branch for pull requests; not applicable for push requests.


        :return: The base_ref of this VbsFilterAttributes.
        :rtype: str
        """
        return self._base_ref

    @base_ref.setter
    def base_ref(self, base_ref):
        """
        Sets the base_ref of this VbsFilterAttributes.
        The target branch for pull requests; not applicable for push requests.


        :param base_ref: The base_ref of this VbsFilterAttributes.
        :type: str
        """
        self._base_ref = base_ref

    @property
    def repository_name(self):
        """
        Gets the repository_name of this VbsFilterAttributes.
        The repository name for trigger events.


        :return: The repository_name of this VbsFilterAttributes.
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        """
        Sets the repository_name of this VbsFilterAttributes.
        The repository name for trigger events.


        :param repository_name: The repository_name of this VbsFilterAttributes.
        :type: str
        """
        self._repository_name = repository_name

    @property
    def file_filter(self):
        """
        Gets the file_filter of this VbsFilterAttributes.

        :return: The file_filter of this VbsFilterAttributes.
        :rtype: oci.devops.models.FileFilter
        """
        return self._file_filter

    @file_filter.setter
    def file_filter(self, file_filter):
        """
        Sets the file_filter of this VbsFilterAttributes.

        :param file_filter: The file_filter of this VbsFilterAttributes.
        :type: oci.devops.models.FileFilter
        """
        self._file_filter = file_filter

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
