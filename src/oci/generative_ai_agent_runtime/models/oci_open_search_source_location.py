# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531

from .source_location import SourceLocation
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OciOpenSearchSourceLocation(SourceLocation):
    """
    The location of the OCI Search with OpenSearch that the agent will use.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OciOpenSearchSourceLocation object with values from keyword arguments. The default value of the :py:attr:`~oci.generative_ai_agent_runtime.models.OciOpenSearchSourceLocation.source_location_type` attribute
        of this class is ``OCI_OPEN_SEARCH`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_location_type:
            The value to assign to the source_location_type property of this OciOpenSearchSourceLocation.
            Allowed values for this property are: "OCI_OBJECT_STORAGE", "OCI_OPEN_SEARCH", "OCI_DATABASE"
        :type source_location_type: str

        :param id:
            The value to assign to the id property of this OciOpenSearchSourceLocation.
        :type id: str

        :param index_name:
            The value to assign to the index_name property of this OciOpenSearchSourceLocation.
        :type index_name: str

        :param url:
            The value to assign to the url property of this OciOpenSearchSourceLocation.
        :type url: str

        """
        self.swagger_types = {
            'source_location_type': 'str',
            'id': 'str',
            'index_name': 'str',
            'url': 'str'
        }
        self.attribute_map = {
            'source_location_type': 'sourceLocationType',
            'id': 'id',
            'index_name': 'indexName',
            'url': 'url'
        }
        self._source_location_type = None
        self._id = None
        self._index_name = None
        self._url = None
        self._source_location_type = 'OCI_OPEN_SEARCH'

    @property
    def id(self):
        """
        Gets the id of this OciOpenSearchSourceLocation.
        The OCID of the OCI OpenSearch cluster.


        :return: The id of this OciOpenSearchSourceLocation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OciOpenSearchSourceLocation.
        The OCID of the OCI OpenSearch cluster.


        :param id: The id of this OciOpenSearchSourceLocation.
        :type: str
        """
        self._id = id

    @property
    def index_name(self):
        """
        Gets the index_name of this OciOpenSearchSourceLocation.
        The name of the index in OpenSearch that contains the source text.


        :return: The index_name of this OciOpenSearchSourceLocation.
        :rtype: str
        """
        return self._index_name

    @index_name.setter
    def index_name(self, index_name):
        """
        Sets the index_name of this OciOpenSearchSourceLocation.
        The name of the index in OpenSearch that contains the source text.


        :param index_name: The index_name of this OciOpenSearchSourceLocation.
        :type: str
        """
        self._index_name = index_name

    @property
    def url(self):
        """
        Gets the url of this OciOpenSearchSourceLocation.
        The URL of the retrieved document, if available.


        :return: The url of this OciOpenSearchSourceLocation.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this OciOpenSearchSourceLocation.
        The URL of the retrieved document, if available.


        :param url: The url of this OciOpenSearchSourceLocation.
        :type: str
        """
        self._url = url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
