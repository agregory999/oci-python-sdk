# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901

from .package_summary import PackageSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstalledPackageSummary(PackageSummary):
    """
    Provides summary information for a software package installed on a managed instance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstalledPackageSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.os_management_hub.models.InstalledPackageSummary.package_classification` attribute
        of this class is ``INSTALLED`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this InstalledPackageSummary.
        :type display_name: str

        :param name:
            The value to assign to the name property of this InstalledPackageSummary.
        :type name: str

        :param type:
            The value to assign to the type property of this InstalledPackageSummary.
        :type type: str

        :param version:
            The value to assign to the version property of this InstalledPackageSummary.
        :type version: str

        :param architecture:
            The value to assign to the architecture property of this InstalledPackageSummary.
            Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", "I386", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type architecture: str

        :param software_sources:
            The value to assign to the software_sources property of this InstalledPackageSummary.
        :type software_sources: list[oci.os_management_hub.models.SoftwareSourceDetails]

        :param package_classification:
            The value to assign to the package_classification property of this InstalledPackageSummary.
            Allowed values for this property are: "INSTALLED", "AVAILABLE", "UPDATABLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type package_classification: str

        :param time_installed:
            The value to assign to the time_installed property of this InstalledPackageSummary.
        :type time_installed: datetime

        :param time_issued:
            The value to assign to the time_issued property of this InstalledPackageSummary.
        :type time_issued: datetime

        """
        self.swagger_types = {
            'display_name': 'str',
            'name': 'str',
            'type': 'str',
            'version': 'str',
            'architecture': 'str',
            'software_sources': 'list[SoftwareSourceDetails]',
            'package_classification': 'str',
            'time_installed': 'datetime',
            'time_issued': 'datetime'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'name': 'name',
            'type': 'type',
            'version': 'version',
            'architecture': 'architecture',
            'software_sources': 'softwareSources',
            'package_classification': 'packageClassification',
            'time_installed': 'timeInstalled',
            'time_issued': 'timeIssued'
        }
        self._display_name = None
        self._name = None
        self._type = None
        self._version = None
        self._architecture = None
        self._software_sources = None
        self._package_classification = None
        self._time_installed = None
        self._time_issued = None
        self._package_classification = 'INSTALLED'

    @property
    def time_installed(self):
        """
        **[Required]** Gets the time_installed of this InstalledPackageSummary.
        The date and time the package was installed, as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_installed of this InstalledPackageSummary.
        :rtype: datetime
        """
        return self._time_installed

    @time_installed.setter
    def time_installed(self, time_installed):
        """
        Sets the time_installed of this InstalledPackageSummary.
        The date and time the package was installed, as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_installed: The time_installed of this InstalledPackageSummary.
        :type: datetime
        """
        self._time_installed = time_installed

    @property
    def time_issued(self):
        """
        Gets the time_issued of this InstalledPackageSummary.
        The date and time the package was issued by a providing erratum (in `RFC 3339`__ format).

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_issued of this InstalledPackageSummary.
        :rtype: datetime
        """
        return self._time_issued

    @time_issued.setter
    def time_issued(self, time_issued):
        """
        Sets the time_issued of this InstalledPackageSummary.
        The date and time the package was issued by a providing erratum (in `RFC 3339`__ format).

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_issued: The time_issued of this InstalledPackageSummary.
        :type: datetime
        """
        self._time_issued = time_issued

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
