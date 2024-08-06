# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CommitAnalyticsAuthorSummary(object):
    """
    Object containing summary of Commit Analytics author.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CommitAnalyticsAuthorSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param author_name:
            The value to assign to the author_name property of this CommitAnalyticsAuthorSummary.
        :type author_name: str

        :param author_email:
            The value to assign to the author_email property of this CommitAnalyticsAuthorSummary.
        :type author_email: str

        """
        self.swagger_types = {
            'author_name': 'str',
            'author_email': 'str'
        }

        self.attribute_map = {
            'author_name': 'authorName',
            'author_email': 'authorEmail'
        }

        self._author_name = None
        self._author_email = None

    @property
    def author_name(self):
        """
        **[Required]** Gets the author_name of this CommitAnalyticsAuthorSummary.
        Author name.


        :return: The author_name of this CommitAnalyticsAuthorSummary.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        """
        Sets the author_name of this CommitAnalyticsAuthorSummary.
        Author name.


        :param author_name: The author_name of this CommitAnalyticsAuthorSummary.
        :type: str
        """
        self._author_name = author_name

    @property
    def author_email(self):
        """
        **[Required]** Gets the author_email of this CommitAnalyticsAuthorSummary.
        Author email.


        :return: The author_email of this CommitAnalyticsAuthorSummary.
        :rtype: str
        """
        return self._author_email

    @author_email.setter
    def author_email(self, author_email):
        """
        Sets the author_email of this CommitAnalyticsAuthorSummary.
        Author email.


        :param author_email: The author_email of this CommitAnalyticsAuthorSummary.
        :type: str
        """
        self._author_email = author_email

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
