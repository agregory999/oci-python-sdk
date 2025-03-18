# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExtensionEnterprise20User(object):
    """
    Enterprise User
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExtensionEnterprise20User object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param employee_number:
            The value to assign to the employee_number property of this ExtensionEnterprise20User.
        :type employee_number: str

        :param cost_center:
            The value to assign to the cost_center property of this ExtensionEnterprise20User.
        :type cost_center: str

        :param organization:
            The value to assign to the organization property of this ExtensionEnterprise20User.
        :type organization: str

        :param division:
            The value to assign to the division property of this ExtensionEnterprise20User.
        :type division: str

        :param department:
            The value to assign to the department property of this ExtensionEnterprise20User.
        :type department: str

        :param manager:
            The value to assign to the manager property of this ExtensionEnterprise20User.
        :type manager: oci.identity_domains.models.UserExtManager

        """
        self.swagger_types = {
            'employee_number': 'str',
            'cost_center': 'str',
            'organization': 'str',
            'division': 'str',
            'department': 'str',
            'manager': 'UserExtManager'
        }
        self.attribute_map = {
            'employee_number': 'employeeNumber',
            'cost_center': 'costCenter',
            'organization': 'organization',
            'division': 'division',
            'department': 'department',
            'manager': 'manager'
        }
        self._employee_number = None
        self._cost_center = None
        self._organization = None
        self._division = None
        self._department = None
        self._manager = None

    @property
    def employee_number(self):
        """
        Gets the employee_number of this ExtensionEnterprise20User.
        Numeric or alphanumeric identifier assigned to  a person, typically based on order of hire or association with an organization.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Employee Number
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Employee Number]]
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The employee_number of this ExtensionEnterprise20User.
        :rtype: str
        """
        return self._employee_number

    @employee_number.setter
    def employee_number(self, employee_number):
        """
        Sets the employee_number of this ExtensionEnterprise20User.
        Numeric or alphanumeric identifier assigned to  a person, typically based on order of hire or association with an organization.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Employee Number
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Employee Number]]
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param employee_number: The employee_number of this ExtensionEnterprise20User.
        :type: str
        """
        self._employee_number = employee_number

    @property
    def cost_center(self):
        """
        Gets the cost_center of this ExtensionEnterprise20User.
        Identifies the name of a cost center.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Cost Center
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Cost Center]]
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The cost_center of this ExtensionEnterprise20User.
        :rtype: str
        """
        return self._cost_center

    @cost_center.setter
    def cost_center(self, cost_center):
        """
        Sets the cost_center of this ExtensionEnterprise20User.
        Identifies the name of a cost center.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Cost Center
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Cost Center]]
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param cost_center: The cost_center of this ExtensionEnterprise20User.
        :type: str
        """
        self._cost_center = cost_center

    @property
    def organization(self):
        """
        Gets the organization of this ExtensionEnterprise20User.
        Identifies the name of an organization.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Organization
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Organization Name, deprecatedColumnHeaderName:Organization]]
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The organization of this ExtensionEnterprise20User.
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this ExtensionEnterprise20User.
        Identifies the name of an organization.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Organization
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Organization Name, deprecatedColumnHeaderName:Organization]]
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param organization: The organization of this ExtensionEnterprise20User.
        :type: str
        """
        self._organization = organization

    @property
    def division(self):
        """
        Gets the division of this ExtensionEnterprise20User.
        Identifies the name of a division.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Division
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Division]]
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The division of this ExtensionEnterprise20User.
        :rtype: str
        """
        return self._division

    @division.setter
    def division(self, division):
        """
        Sets the division of this ExtensionEnterprise20User.
        Identifies the name of a division.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Division
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Division]]
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param division: The division of this ExtensionEnterprise20User.
        :type: str
        """
        self._division = division

    @property
    def department(self):
        """
        Gets the department of this ExtensionEnterprise20User.
        Identifies the name of a department.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Department
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Department]]
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The department of this ExtensionEnterprise20User.
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        """
        Sets the department of this ExtensionEnterprise20User.
        Identifies the name of a department.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsCsvAttributeName: Department
         - idcsCsvAttributeNameMappings: [[columnHeaderName:Department]]
         - idcsPii: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param department: The department of this ExtensionEnterprise20User.
        :type: str
        """
        self._department = department

    @property
    def manager(self):
        """
        Gets the manager of this ExtensionEnterprise20User.

        :return: The manager of this ExtensionEnterprise20User.
        :rtype: oci.identity_domains.models.UserExtManager
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """
        Sets the manager of this ExtensionEnterprise20User.

        :param manager: The manager of this ExtensionEnterprise20User.
        :type: oci.identity_domains.models.UserExtManager
        """
        self._manager = manager

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
