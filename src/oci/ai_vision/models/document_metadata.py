# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DocumentMetadata(object):
    """
    Document information.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DocumentMetadata object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param page_count:
            The value to assign to the page_count property of this DocumentMetadata.
        :type page_count: int

        :param mime_type:
            The value to assign to the mime_type property of this DocumentMetadata.
        :type mime_type: str

        """
        self.swagger_types = {
            'page_count': 'int',
            'mime_type': 'str'
        }

        self.attribute_map = {
            'page_count': 'pageCount',
            'mime_type': 'mimeType'
        }

        self._page_count = None
        self._mime_type = None

    @property
    def page_count(self):
        """
        **[Required]** Gets the page_count of this DocumentMetadata.
        Number of pages in the document.


        :return: The page_count of this DocumentMetadata.
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """
        Sets the page_count of this DocumentMetadata.
        Number of pages in the document.


        :param page_count: The page_count of this DocumentMetadata.
        :type: int
        """
        self._page_count = page_count

    @property
    def mime_type(self):
        """
        **[Required]** Gets the mime_type of this DocumentMetadata.
        Result data format.


        :return: The mime_type of this DocumentMetadata.
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """
        Sets the mime_type of this DocumentMetadata.
        Result data format.


        :param mime_type: The mime_type of this DocumentMetadata.
        :type: str
        """
        self._mime_type = mime_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
