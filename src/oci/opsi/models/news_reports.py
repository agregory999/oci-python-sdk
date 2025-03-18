# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NewsReports(object):
    """
    Logical grouping used for Operations Insights news reports related operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NewsReports object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param news_reports:
            The value to assign to the news_reports property of this NewsReports.
        :type news_reports: object

        """
        self.swagger_types = {
            'news_reports': 'object'
        }
        self.attribute_map = {
            'news_reports': 'newsReports'
        }
        self._news_reports = None

    @property
    def news_reports(self):
        """
        Gets the news_reports of this NewsReports.
        News report object.


        :return: The news_reports of this NewsReports.
        :rtype: object
        """
        return self._news_reports

    @news_reports.setter
    def news_reports(self, news_reports):
        """
        Sets the news_reports of this NewsReports.
        News report object.


        :param news_reports: The news_reports of this NewsReports.
        :type: object
        """
        self._news_reports = news_reports

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
