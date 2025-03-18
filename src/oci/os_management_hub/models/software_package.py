# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SoftwarePackage(object):
    """
    An object that defines a software package.
    """

    #: A constant which can be used with the architecture property of a SoftwarePackage.
    #: This constant has a value of "I386"
    ARCHITECTURE_I386 = "I386"

    #: A constant which can be used with the architecture property of a SoftwarePackage.
    #: This constant has a value of "I686"
    ARCHITECTURE_I686 = "I686"

    #: A constant which can be used with the architecture property of a SoftwarePackage.
    #: This constant has a value of "AARCH64"
    ARCHITECTURE_AARCH64 = "AARCH64"

    #: A constant which can be used with the architecture property of a SoftwarePackage.
    #: This constant has a value of "X86_64"
    ARCHITECTURE_X86_64 = "X86_64"

    #: A constant which can be used with the architecture property of a SoftwarePackage.
    #: This constant has a value of "SRC"
    ARCHITECTURE_SRC = "SRC"

    #: A constant which can be used with the architecture property of a SoftwarePackage.
    #: This constant has a value of "NOARCH"
    ARCHITECTURE_NOARCH = "NOARCH"

    #: A constant which can be used with the architecture property of a SoftwarePackage.
    #: This constant has a value of "OTHER"
    ARCHITECTURE_OTHER = "OTHER"

    def __init__(self, **kwargs):
        """
        Initializes a new SoftwarePackage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this SoftwarePackage.
        :type display_name: str

        :param name:
            The value to assign to the name property of this SoftwarePackage.
        :type name: str

        :param type:
            The value to assign to the type property of this SoftwarePackage.
        :type type: str

        :param version:
            The value to assign to the version property of this SoftwarePackage.
        :type version: str

        :param architecture:
            The value to assign to the architecture property of this SoftwarePackage.
            Allowed values for this property are: "I386", "I686", "AARCH64", "X86_64", "SRC", "NOARCH", "OTHER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type architecture: str

        :param last_modified_date:
            The value to assign to the last_modified_date property of this SoftwarePackage.
        :type last_modified_date: str

        :param checksum:
            The value to assign to the checksum property of this SoftwarePackage.
        :type checksum: str

        :param checksum_type:
            The value to assign to the checksum_type property of this SoftwarePackage.
        :type checksum_type: str

        :param description:
            The value to assign to the description property of this SoftwarePackage.
        :type description: str

        :param size_in_bytes:
            The value to assign to the size_in_bytes property of this SoftwarePackage.
        :type size_in_bytes: int

        :param dependencies:
            The value to assign to the dependencies property of this SoftwarePackage.
        :type dependencies: list[oci.os_management_hub.models.SoftwarePackageDependency]

        :param files:
            The value to assign to the files property of this SoftwarePackage.
        :type files: list[oci.os_management_hub.models.SoftwarePackageFile]

        :param software_sources:
            The value to assign to the software_sources property of this SoftwarePackage.
        :type software_sources: list[oci.os_management_hub.models.SoftwareSourceDetails]

        :param is_latest:
            The value to assign to the is_latest property of this SoftwarePackage.
        :type is_latest: bool

        :param os_families:
            The value to assign to the os_families property of this SoftwarePackage.
        :type os_families: list[oci.os_management_hub.models.OsFamily]

        """
        self.swagger_types = {
            'display_name': 'str',
            'name': 'str',
            'type': 'str',
            'version': 'str',
            'architecture': 'str',
            'last_modified_date': 'str',
            'checksum': 'str',
            'checksum_type': 'str',
            'description': 'str',
            'size_in_bytes': 'int',
            'dependencies': 'list[SoftwarePackageDependency]',
            'files': 'list[SoftwarePackageFile]',
            'software_sources': 'list[SoftwareSourceDetails]',
            'is_latest': 'bool',
            'os_families': 'list[OsFamily]'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'name': 'name',
            'type': 'type',
            'version': 'version',
            'architecture': 'architecture',
            'last_modified_date': 'lastModifiedDate',
            'checksum': 'checksum',
            'checksum_type': 'checksumType',
            'description': 'description',
            'size_in_bytes': 'sizeInBytes',
            'dependencies': 'dependencies',
            'files': 'files',
            'software_sources': 'softwareSources',
            'is_latest': 'isLatest',
            'os_families': 'osFamilies'
        }
        self._display_name = None
        self._name = None
        self._type = None
        self._version = None
        self._architecture = None
        self._last_modified_date = None
        self._checksum = None
        self._checksum_type = None
        self._description = None
        self._size_in_bytes = None
        self._dependencies = None
        self._files = None
        self._software_sources = None
        self._is_latest = None
        self._os_families = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this SoftwarePackage.
        Package name.


        :return: The display_name of this SoftwarePackage.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SoftwarePackage.
        Package name.


        :param display_name: The display_name of this SoftwarePackage.
        :type: str
        """
        self._display_name = display_name

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SoftwarePackage.
        Unique identifier for the package. Note that this is not an OCID.


        :return: The name of this SoftwarePackage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SoftwarePackage.
        Unique identifier for the package. Note that this is not an OCID.


        :param name: The name of this SoftwarePackage.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this SoftwarePackage.
        Type of the package.


        :return: The type of this SoftwarePackage.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SoftwarePackage.
        Type of the package.


        :param type: The type of this SoftwarePackage.
        :type: str
        """
        self._type = type

    @property
    def version(self):
        """
        **[Required]** Gets the version of this SoftwarePackage.
        Version of the package.


        :return: The version of this SoftwarePackage.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this SoftwarePackage.
        Version of the package.


        :param version: The version of this SoftwarePackage.
        :type: str
        """
        self._version = version

    @property
    def architecture(self):
        """
        Gets the architecture of this SoftwarePackage.
        The architecture for which this software was built

        Allowed values for this property are: "I386", "I686", "AARCH64", "X86_64", "SRC", "NOARCH", "OTHER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The architecture of this SoftwarePackage.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """
        Sets the architecture of this SoftwarePackage.
        The architecture for which this software was built


        :param architecture: The architecture of this SoftwarePackage.
        :type: str
        """
        allowed_values = ["I386", "I686", "AARCH64", "X86_64", "SRC", "NOARCH", "OTHER"]
        if not value_allowed_none_or_none_sentinel(architecture, allowed_values):
            architecture = 'UNKNOWN_ENUM_VALUE'
        self._architecture = architecture

    @property
    def last_modified_date(self):
        """
        Gets the last_modified_date of this SoftwarePackage.
        The date and time the package was last modified (in `RFC 3339`__ format).

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The last_modified_date of this SoftwarePackage.
        :rtype: str
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """
        Sets the last_modified_date of this SoftwarePackage.
        The date and time the package was last modified (in `RFC 3339`__ format).

        __ https://tools.ietf.org/rfc/rfc3339


        :param last_modified_date: The last_modified_date of this SoftwarePackage.
        :type: str
        """
        self._last_modified_date = last_modified_date

    @property
    def checksum(self):
        """
        Gets the checksum of this SoftwarePackage.
        Checksum of the package.


        :return: The checksum of this SoftwarePackage.
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """
        Sets the checksum of this SoftwarePackage.
        Checksum of the package.


        :param checksum: The checksum of this SoftwarePackage.
        :type: str
        """
        self._checksum = checksum

    @property
    def checksum_type(self):
        """
        Gets the checksum_type of this SoftwarePackage.
        Type of the checksum.


        :return: The checksum_type of this SoftwarePackage.
        :rtype: str
        """
        return self._checksum_type

    @checksum_type.setter
    def checksum_type(self, checksum_type):
        """
        Sets the checksum_type of this SoftwarePackage.
        Type of the checksum.


        :param checksum_type: The checksum_type of this SoftwarePackage.
        :type: str
        """
        self._checksum_type = checksum_type

    @property
    def description(self):
        """
        Gets the description of this SoftwarePackage.
        Description of the package.


        :return: The description of this SoftwarePackage.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SoftwarePackage.
        Description of the package.


        :param description: The description of this SoftwarePackage.
        :type: str
        """
        self._description = description

    @property
    def size_in_bytes(self):
        """
        Gets the size_in_bytes of this SoftwarePackage.
        Size of the package in bytes.


        :return: The size_in_bytes of this SoftwarePackage.
        :rtype: int
        """
        return self._size_in_bytes

    @size_in_bytes.setter
    def size_in_bytes(self, size_in_bytes):
        """
        Sets the size_in_bytes of this SoftwarePackage.
        Size of the package in bytes.


        :param size_in_bytes: The size_in_bytes of this SoftwarePackage.
        :type: int
        """
        self._size_in_bytes = size_in_bytes

    @property
    def dependencies(self):
        """
        Gets the dependencies of this SoftwarePackage.
        List of dependencies for the software package.


        :return: The dependencies of this SoftwarePackage.
        :rtype: list[oci.os_management_hub.models.SoftwarePackageDependency]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """
        Sets the dependencies of this SoftwarePackage.
        List of dependencies for the software package.


        :param dependencies: The dependencies of this SoftwarePackage.
        :type: list[oci.os_management_hub.models.SoftwarePackageDependency]
        """
        self._dependencies = dependencies

    @property
    def files(self):
        """
        Gets the files of this SoftwarePackage.
        List of files for the software package.


        :return: The files of this SoftwarePackage.
        :rtype: list[oci.os_management_hub.models.SoftwarePackageFile]
        """
        return self._files

    @files.setter
    def files(self, files):
        """
        Sets the files of this SoftwarePackage.
        List of files for the software package.


        :param files: The files of this SoftwarePackage.
        :type: list[oci.os_management_hub.models.SoftwarePackageFile]
        """
        self._files = files

    @property
    def software_sources(self):
        """
        Gets the software_sources of this SoftwarePackage.
        List of software sources that provide the software package. This property is deprecated and it will be removed in a future API release.


        :return: The software_sources of this SoftwarePackage.
        :rtype: list[oci.os_management_hub.models.SoftwareSourceDetails]
        """
        return self._software_sources

    @software_sources.setter
    def software_sources(self, software_sources):
        """
        Sets the software_sources of this SoftwarePackage.
        List of software sources that provide the software package. This property is deprecated and it will be removed in a future API release.


        :param software_sources: The software_sources of this SoftwarePackage.
        :type: list[oci.os_management_hub.models.SoftwareSourceDetails]
        """
        self._software_sources = software_sources

    @property
    def is_latest(self):
        """
        Gets the is_latest of this SoftwarePackage.
        Indicates whether this package is the latest version.


        :return: The is_latest of this SoftwarePackage.
        :rtype: bool
        """
        return self._is_latest

    @is_latest.setter
    def is_latest(self, is_latest):
        """
        Sets the is_latest of this SoftwarePackage.
        Indicates whether this package is the latest version.


        :param is_latest: The is_latest of this SoftwarePackage.
        :type: bool
        """
        self._is_latest = is_latest

    @property
    def os_families(self):
        """
        Gets the os_families of this SoftwarePackage.
        The OS families the package belongs to.


        :return: The os_families of this SoftwarePackage.
        :rtype: list[oci.os_management_hub.models.OsFamily]
        """
        return self._os_families

    @os_families.setter
    def os_families(self, os_families):
        """
        Sets the os_families of this SoftwarePackage.
        The OS families the package belongs to.


        :param os_families: The os_families of this SoftwarePackage.
        :type: list[oci.os_management_hub.models.OsFamily]
        """
        self._os_families = os_families

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
