# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20191001


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VerifyAddressDetails(object):
    """
    Verify address related details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VerifyAddressDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param address_key:
            The value to assign to the address_key property of this VerifyAddressDetails.
        :type address_key: str

        :param line1:
            The value to assign to the line1 property of this VerifyAddressDetails.
        :type line1: str

        :param line2:
            The value to assign to the line2 property of this VerifyAddressDetails.
        :type line2: str

        :param line3:
            The value to assign to the line3 property of this VerifyAddressDetails.
        :type line3: str

        :param line4:
            The value to assign to the line4 property of this VerifyAddressDetails.
        :type line4: str

        :param street_name:
            The value to assign to the street_name property of this VerifyAddressDetails.
        :type street_name: str

        :param street_number:
            The value to assign to the street_number property of this VerifyAddressDetails.
        :type street_number: str

        :param city:
            The value to assign to the city property of this VerifyAddressDetails.
        :type city: str

        :param county:
            The value to assign to the county property of this VerifyAddressDetails.
        :type county: str

        :param country:
            The value to assign to the country property of this VerifyAddressDetails.
        :type country: str

        :param province:
            The value to assign to the province property of this VerifyAddressDetails.
        :type province: str

        :param postal_code:
            The value to assign to the postal_code property of this VerifyAddressDetails.
        :type postal_code: str

        :param state:
            The value to assign to the state property of this VerifyAddressDetails.
        :type state: str

        :param email_address:
            The value to assign to the email_address property of this VerifyAddressDetails.
        :type email_address: str

        :param company_name:
            The value to assign to the company_name property of this VerifyAddressDetails.
        :type company_name: str

        :param first_name:
            The value to assign to the first_name property of this VerifyAddressDetails.
        :type first_name: str

        :param middle_name:
            The value to assign to the middle_name property of this VerifyAddressDetails.
        :type middle_name: str

        :param last_name:
            The value to assign to the last_name property of this VerifyAddressDetails.
        :type last_name: str

        :param phone_country_code:
            The value to assign to the phone_country_code property of this VerifyAddressDetails.
        :type phone_country_code: str

        :param phone_number:
            The value to assign to the phone_number property of this VerifyAddressDetails.
        :type phone_number: str

        :param job_title:
            The value to assign to the job_title property of this VerifyAddressDetails.
        :type job_title: str

        :param department_name:
            The value to assign to the department_name property of this VerifyAddressDetails.
        :type department_name: str

        :param internal_number:
            The value to assign to the internal_number property of this VerifyAddressDetails.
        :type internal_number: str

        :param contributor_class:
            The value to assign to the contributor_class property of this VerifyAddressDetails.
        :type contributor_class: str

        :param state_inscription:
            The value to assign to the state_inscription property of this VerifyAddressDetails.
        :type state_inscription: str

        :param municipal_inscription:
            The value to assign to the municipal_inscription property of this VerifyAddressDetails.
        :type municipal_inscription: str

        """
        self.swagger_types = {
            'address_key': 'str',
            'line1': 'str',
            'line2': 'str',
            'line3': 'str',
            'line4': 'str',
            'street_name': 'str',
            'street_number': 'str',
            'city': 'str',
            'county': 'str',
            'country': 'str',
            'province': 'str',
            'postal_code': 'str',
            'state': 'str',
            'email_address': 'str',
            'company_name': 'str',
            'first_name': 'str',
            'middle_name': 'str',
            'last_name': 'str',
            'phone_country_code': 'str',
            'phone_number': 'str',
            'job_title': 'str',
            'department_name': 'str',
            'internal_number': 'str',
            'contributor_class': 'str',
            'state_inscription': 'str',
            'municipal_inscription': 'str'
        }

        self.attribute_map = {
            'address_key': 'addressKey',
            'line1': 'line1',
            'line2': 'line2',
            'line3': 'line3',
            'line4': 'line4',
            'street_name': 'streetName',
            'street_number': 'streetNumber',
            'city': 'city',
            'county': 'county',
            'country': 'country',
            'province': 'province',
            'postal_code': 'postalCode',
            'state': 'state',
            'email_address': 'emailAddress',
            'company_name': 'companyName',
            'first_name': 'firstName',
            'middle_name': 'middleName',
            'last_name': 'lastName',
            'phone_country_code': 'phoneCountryCode',
            'phone_number': 'phoneNumber',
            'job_title': 'jobTitle',
            'department_name': 'departmentName',
            'internal_number': 'internalNumber',
            'contributor_class': 'contributorClass',
            'state_inscription': 'stateInscription',
            'municipal_inscription': 'municipalInscription'
        }

        self._address_key = None
        self._line1 = None
        self._line2 = None
        self._line3 = None
        self._line4 = None
        self._street_name = None
        self._street_number = None
        self._city = None
        self._county = None
        self._country = None
        self._province = None
        self._postal_code = None
        self._state = None
        self._email_address = None
        self._company_name = None
        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self._phone_country_code = None
        self._phone_number = None
        self._job_title = None
        self._department_name = None
        self._internal_number = None
        self._contributor_class = None
        self._state_inscription = None
        self._municipal_inscription = None

    @property
    def address_key(self):
        """
        Gets the address_key of this VerifyAddressDetails.
        Address identifier.


        :return: The address_key of this VerifyAddressDetails.
        :rtype: str
        """
        return self._address_key

    @address_key.setter
    def address_key(self, address_key):
        """
        Sets the address_key of this VerifyAddressDetails.
        Address identifier.


        :param address_key: The address_key of this VerifyAddressDetails.
        :type: str
        """
        self._address_key = address_key

    @property
    def line1(self):
        """
        Gets the line1 of this VerifyAddressDetails.
        Address line 1.


        :return: The line1 of this VerifyAddressDetails.
        :rtype: str
        """
        return self._line1

    @line1.setter
    def line1(self, line1):
        """
        Sets the line1 of this VerifyAddressDetails.
        Address line 1.


        :param line1: The line1 of this VerifyAddressDetails.
        :type: str
        """
        self._line1 = line1

    @property
    def line2(self):
        """
        Gets the line2 of this VerifyAddressDetails.
        Address line 2.


        :return: The line2 of this VerifyAddressDetails.
        :rtype: str
        """
        return self._line2

    @line2.setter
    def line2(self, line2):
        """
        Sets the line2 of this VerifyAddressDetails.
        Address line 2.


        :param line2: The line2 of this VerifyAddressDetails.
        :type: str
        """
        self._line2 = line2

    @property
    def line3(self):
        """
        Gets the line3 of this VerifyAddressDetails.
        Address line 3.


        :return: The line3 of this VerifyAddressDetails.
        :rtype: str
        """
        return self._line3

    @line3.setter
    def line3(self, line3):
        """
        Sets the line3 of this VerifyAddressDetails.
        Address line 3.


        :param line3: The line3 of this VerifyAddressDetails.
        :type: str
        """
        self._line3 = line3

    @property
    def line4(self):
        """
        Gets the line4 of this VerifyAddressDetails.
        Address line 4.


        :return: The line4 of this VerifyAddressDetails.
        :rtype: str
        """
        return self._line4

    @line4.setter
    def line4(self, line4):
        """
        Sets the line4 of this VerifyAddressDetails.
        Address line 4.


        :param line4: The line4 of this VerifyAddressDetails.
        :type: str
        """
        self._line4 = line4

    @property
    def street_name(self):
        """
        Gets the street_name of this VerifyAddressDetails.
        Street name of the address.


        :return: The street_name of this VerifyAddressDetails.
        :rtype: str
        """
        return self._street_name

    @street_name.setter
    def street_name(self, street_name):
        """
        Sets the street_name of this VerifyAddressDetails.
        Street name of the address.


        :param street_name: The street_name of this VerifyAddressDetails.
        :type: str
        """
        self._street_name = street_name

    @property
    def street_number(self):
        """
        Gets the street_number of this VerifyAddressDetails.
        Street number of the address.


        :return: The street_number of this VerifyAddressDetails.
        :rtype: str
        """
        return self._street_number

    @street_number.setter
    def street_number(self, street_number):
        """
        Sets the street_number of this VerifyAddressDetails.
        Street number of the address.


        :param street_number: The street_number of this VerifyAddressDetails.
        :type: str
        """
        self._street_number = street_number

    @property
    def city(self):
        """
        Gets the city of this VerifyAddressDetails.
        Name of the city.


        :return: The city of this VerifyAddressDetails.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this VerifyAddressDetails.
        Name of the city.


        :param city: The city of this VerifyAddressDetails.
        :type: str
        """
        self._city = city

    @property
    def county(self):
        """
        Gets the county of this VerifyAddressDetails.
        County of the address.


        :return: The county of this VerifyAddressDetails.
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """
        Sets the county of this VerifyAddressDetails.
        County of the address.


        :param county: The county of this VerifyAddressDetails.
        :type: str
        """
        self._county = county

    @property
    def country(self):
        """
        Gets the country of this VerifyAddressDetails.
        Country of the address.


        :return: The country of this VerifyAddressDetails.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this VerifyAddressDetails.
        Country of the address.


        :param country: The country of this VerifyAddressDetails.
        :type: str
        """
        self._country = country

    @property
    def province(self):
        """
        Gets the province of this VerifyAddressDetails.
        Province of the address.


        :return: The province of this VerifyAddressDetails.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """
        Sets the province of this VerifyAddressDetails.
        Province of the address.


        :param province: The province of this VerifyAddressDetails.
        :type: str
        """
        self._province = province

    @property
    def postal_code(self):
        """
        Gets the postal_code of this VerifyAddressDetails.
        Post code of the address.


        :return: The postal_code of this VerifyAddressDetails.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this VerifyAddressDetails.
        Post code of the address.


        :param postal_code: The postal_code of this VerifyAddressDetails.
        :type: str
        """
        self._postal_code = postal_code

    @property
    def state(self):
        """
        Gets the state of this VerifyAddressDetails.
        State of the address.


        :return: The state of this VerifyAddressDetails.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this VerifyAddressDetails.
        State of the address.


        :param state: The state of this VerifyAddressDetails.
        :type: str
        """
        self._state = state

    @property
    def email_address(self):
        """
        Gets the email_address of this VerifyAddressDetails.
        Contact person email address.


        :return: The email_address of this VerifyAddressDetails.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """
        Sets the email_address of this VerifyAddressDetails.
        Contact person email address.


        :param email_address: The email_address of this VerifyAddressDetails.
        :type: str
        """
        self._email_address = email_address

    @property
    def company_name(self):
        """
        Gets the company_name of this VerifyAddressDetails.
        Name of the customer company.


        :return: The company_name of this VerifyAddressDetails.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """
        Sets the company_name of this VerifyAddressDetails.
        Name of the customer company.


        :param company_name: The company_name of this VerifyAddressDetails.
        :type: str
        """
        self._company_name = company_name

    @property
    def first_name(self):
        """
        Gets the first_name of this VerifyAddressDetails.
        First name of the contact person.


        :return: The first_name of this VerifyAddressDetails.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this VerifyAddressDetails.
        First name of the contact person.


        :param first_name: The first_name of this VerifyAddressDetails.
        :type: str
        """
        self._first_name = first_name

    @property
    def middle_name(self):
        """
        Gets the middle_name of this VerifyAddressDetails.
        Middle name of the contact person.


        :return: The middle_name of this VerifyAddressDetails.
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """
        Sets the middle_name of this VerifyAddressDetails.
        Middle name of the contact person.


        :param middle_name: The middle_name of this VerifyAddressDetails.
        :type: str
        """
        self._middle_name = middle_name

    @property
    def last_name(self):
        """
        Gets the last_name of this VerifyAddressDetails.
        Last name of the contact person.


        :return: The last_name of this VerifyAddressDetails.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this VerifyAddressDetails.
        Last name of the contact person.


        :param last_name: The last_name of this VerifyAddressDetails.
        :type: str
        """
        self._last_name = last_name

    @property
    def phone_country_code(self):
        """
        Gets the phone_country_code of this VerifyAddressDetails.
        Phone country code of the contact person.


        :return: The phone_country_code of this VerifyAddressDetails.
        :rtype: str
        """
        return self._phone_country_code

    @phone_country_code.setter
    def phone_country_code(self, phone_country_code):
        """
        Sets the phone_country_code of this VerifyAddressDetails.
        Phone country code of the contact person.


        :param phone_country_code: The phone_country_code of this VerifyAddressDetails.
        :type: str
        """
        self._phone_country_code = phone_country_code

    @property
    def phone_number(self):
        """
        Gets the phone_number of this VerifyAddressDetails.
        Phone number of the contact person.


        :return: The phone_number of this VerifyAddressDetails.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this VerifyAddressDetails.
        Phone number of the contact person.


        :param phone_number: The phone_number of this VerifyAddressDetails.
        :type: str
        """
        self._phone_number = phone_number

    @property
    def job_title(self):
        """
        Gets the job_title of this VerifyAddressDetails.
        Job title of the contact person.


        :return: The job_title of this VerifyAddressDetails.
        :rtype: str
        """
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        """
        Sets the job_title of this VerifyAddressDetails.
        Job title of the contact person.


        :param job_title: The job_title of this VerifyAddressDetails.
        :type: str
        """
        self._job_title = job_title

    @property
    def department_name(self):
        """
        Gets the department_name of this VerifyAddressDetails.
        Department name of the customer company.


        :return: The department_name of this VerifyAddressDetails.
        :rtype: str
        """
        return self._department_name

    @department_name.setter
    def department_name(self, department_name):
        """
        Sets the department_name of this VerifyAddressDetails.
        Department name of the customer company.


        :param department_name: The department_name of this VerifyAddressDetails.
        :type: str
        """
        self._department_name = department_name

    @property
    def internal_number(self):
        """
        Gets the internal_number of this VerifyAddressDetails.
        Internal number of the customer company.


        :return: The internal_number of this VerifyAddressDetails.
        :rtype: str
        """
        return self._internal_number

    @internal_number.setter
    def internal_number(self, internal_number):
        """
        Sets the internal_number of this VerifyAddressDetails.
        Internal number of the customer company.


        :param internal_number: The internal_number of this VerifyAddressDetails.
        :type: str
        """
        self._internal_number = internal_number

    @property
    def contributor_class(self):
        """
        Gets the contributor_class of this VerifyAddressDetails.
        Contributor class of the customer company.


        :return: The contributor_class of this VerifyAddressDetails.
        :rtype: str
        """
        return self._contributor_class

    @contributor_class.setter
    def contributor_class(self, contributor_class):
        """
        Sets the contributor_class of this VerifyAddressDetails.
        Contributor class of the customer company.


        :param contributor_class: The contributor_class of this VerifyAddressDetails.
        :type: str
        """
        self._contributor_class = contributor_class

    @property
    def state_inscription(self):
        """
        Gets the state_inscription of this VerifyAddressDetails.
        State Inscription.


        :return: The state_inscription of this VerifyAddressDetails.
        :rtype: str
        """
        return self._state_inscription

    @state_inscription.setter
    def state_inscription(self, state_inscription):
        """
        Sets the state_inscription of this VerifyAddressDetails.
        State Inscription.


        :param state_inscription: The state_inscription of this VerifyAddressDetails.
        :type: str
        """
        self._state_inscription = state_inscription

    @property
    def municipal_inscription(self):
        """
        Gets the municipal_inscription of this VerifyAddressDetails.
        Municipal Inscription.


        :return: The municipal_inscription of this VerifyAddressDetails.
        :rtype: str
        """
        return self._municipal_inscription

    @municipal_inscription.setter
    def municipal_inscription(self, municipal_inscription):
        """
        Sets the municipal_inscription of this VerifyAddressDetails.
        Municipal Inscription.


        :param municipal_inscription: The municipal_inscription of this VerifyAddressDetails.
        :type: str
        """
        self._municipal_inscription = municipal_inscription

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
