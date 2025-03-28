# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190325


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImportGlossaryDetails(object):
    """
    Import glossary from the contents of the glossary definition file.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImportGlossaryDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param glossary_file_contents:
            The value to assign to the glossary_file_contents property of this ImportGlossaryDetails.
        :type glossary_file_contents: str

        """
        self.swagger_types = {
            'glossary_file_contents': 'str'
        }
        self.attribute_map = {
            'glossary_file_contents': 'glossaryFileContents'
        }
        self._glossary_file_contents = None

    @property
    def glossary_file_contents(self):
        """
        Gets the glossary_file_contents of this ImportGlossaryDetails.
        The file contents used for the import of glossary.


        :return: The glossary_file_contents of this ImportGlossaryDetails.
        :rtype: str
        """
        return self._glossary_file_contents

    @glossary_file_contents.setter
    def glossary_file_contents(self, glossary_file_contents):
        """
        Sets the glossary_file_contents of this ImportGlossaryDetails.
        The file contents used for the import of glossary.


        :param glossary_file_contents: The glossary_file_contents of this ImportGlossaryDetails.
        :type: str
        """
        self._glossary_file_contents = glossary_file_contents

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
