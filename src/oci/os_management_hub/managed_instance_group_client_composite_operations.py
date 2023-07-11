# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901

import oci  # noqa: F401
from oci.util import WAIT_RESOURCE_NOT_FOUND  # noqa: F401


class ManagedInstanceGroupClientCompositeOperations(object):
    """
    This class provides a wrapper around :py:class:`~oci.os_management_hub.ManagedInstanceGroupClient` and offers convenience methods
    for operations that would otherwise need to be chained together. For example, instead of performing an action
    on a resource (e.g. launching an instance, creating a load balancer) and then using a waiter to wait for the resource
    to enter a given state, you can call a single method in this class to accomplish the same functionality
    """

    def __init__(self, client, **kwargs):
        """
        Creates a new ManagedInstanceGroupClientCompositeOperations object

        :param ManagedInstanceGroupClient client:
            The service client which will be wrapped by this object
        """
        self.client = client

    def attach_managed_instances_to_managed_instance_group_and_wait_for_state(self, managed_instance_group_id, attach_managed_instances_to_managed_instance_group_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.attach_managed_instances_to_managed_instance_group` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_group_id: (required)
            The managed instance group OCID.

        :param oci.os_management_hub.models.AttachManagedInstancesToManagedInstanceGroupDetails attach_managed_instances_to_managed_instance_group_details: (required)
            Details for managed instances to attach to the managed instance group.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.attach_managed_instances_to_managed_instance_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.attach_managed_instances_to_managed_instance_group(managed_instance_group_id, attach_managed_instances_to_managed_instance_group_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_managed_instance_group_and_wait_for_state(self, create_managed_instance_group_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.create_managed_instance_group` and waits for the :py:class:`~oci.os_management_hub.models.ManagedInstanceGroup` acted upon
        to enter the given state(s).

        :param oci.os_management_hub.models.CreateManagedInstanceGroupDetails create_managed_instance_group_details: (required)
            Details for the new managed instance group.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.ManagedInstanceGroup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.create_managed_instance_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_managed_instance_group(create_managed_instance_group_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        managed_instance_group_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_managed_instance_group(managed_instance_group_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_managed_instance_group_and_wait_for_state(self, managed_instance_group_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.delete_managed_instance_group` and waits for the :py:class:`~oci.os_management_hub.models.ManagedInstanceGroup` acted upon
        to enter the given state(s).

        :param str managed_instance_group_id: (required)
            The managed instance group OCID.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.ManagedInstanceGroup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.delete_managed_instance_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_managed_instance_group(managed_instance_group_id)
        operation_result = None
        try:
            operation_result = self.client.delete_managed_instance_group(managed_instance_group_id, **operation_kwargs)
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                return WAIT_RESOURCE_NOT_FOUND
            else:
                raise e

        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]

        try:
            if ("succeed_on_not_found" in waiter_kwargs) and (waiter_kwargs["succeed_on_not_found"] is False):
                self.client.base_client.logger.warning("The waiter kwarg succeed_on_not_found was passed as False for the delete composite operation delete_managed_instance_group, this would result in the operation to fail if the resource is not found! Please, do not pass this kwarg if this was not intended")
            else:
                """
                If the user does not send in this value, we set it to True by default.
                We are doing this because during a delete resource scenario and waiting on its state, the service can
                return a 404 NOT FOUND exception as the resource was deleted and a get on its state would fail
                """
                waiter_kwargs["succeed_on_not_found"] = True
            waiter_result = oci.wait_until(
                self.client,
                initial_get_result,  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def disable_module_stream_on_managed_instance_group_and_wait_for_state(self, managed_instance_group_id, disable_module_stream_on_managed_instance_group_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.disable_module_stream_on_managed_instance_group` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_group_id: (required)
            The managed instance group OCID.

        :param oci.os_management_hub.models.DisableModuleStreamOnManagedInstanceGroupDetails disable_module_stream_on_managed_instance_group_details: (required)
            Details for modules to disable on the managed instance group.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.disable_module_stream_on_managed_instance_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.disable_module_stream_on_managed_instance_group(managed_instance_group_id, disable_module_stream_on_managed_instance_group_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def enable_module_stream_on_managed_instance_group_and_wait_for_state(self, managed_instance_group_id, enable_module_stream_on_managed_instance_group_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.enable_module_stream_on_managed_instance_group` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_group_id: (required)
            The managed instance group OCID.

        :param oci.os_management_hub.models.EnableModuleStreamOnManagedInstanceGroupDetails enable_module_stream_on_managed_instance_group_details: (required)
            Details for modules to enable on the managed instance group.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.enable_module_stream_on_managed_instance_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.enable_module_stream_on_managed_instance_group(managed_instance_group_id, enable_module_stream_on_managed_instance_group_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def install_module_stream_profile_on_managed_instance_group_and_wait_for_state(self, managed_instance_group_id, install_module_stream_profile_on_managed_instance_group_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.install_module_stream_profile_on_managed_instance_group` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_group_id: (required)
            The managed instance group OCID.

        :param oci.os_management_hub.models.InstallModuleStreamProfileOnManagedInstanceGroupDetails install_module_stream_profile_on_managed_instance_group_details: (required)
            Details for profiles to install on the managed instance group.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.install_module_stream_profile_on_managed_instance_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.install_module_stream_profile_on_managed_instance_group(managed_instance_group_id, install_module_stream_profile_on_managed_instance_group_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def install_packages_on_managed_instance_group_and_wait_for_state(self, managed_instance_group_id, install_packages_on_managed_instance_group_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.install_packages_on_managed_instance_group` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_group_id: (required)
            The managed instance group OCID.

        :param oci.os_management_hub.models.InstallPackagesOnManagedInstanceGroupDetails install_packages_on_managed_instance_group_details: (required)
            Details for packages to install on the specified managed instance group.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.install_packages_on_managed_instance_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.install_packages_on_managed_instance_group(managed_instance_group_id, install_packages_on_managed_instance_group_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def list_managed_instance_group_modules_and_wait_for_state(self, managed_instance_group_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.list_managed_instance_group_modules` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_group_id: (required)
            The managed instance group OCID.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.list_managed_instance_group_modules`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.list_managed_instance_group_modules(managed_instance_group_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def manage_module_streams_on_managed_instance_group_and_wait_for_state(self, managed_instance_group_id, manage_module_streams_on_managed_instance_group_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.manage_module_streams_on_managed_instance_group` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_group_id: (required)
            The managed instance group OCID.

        :param oci.os_management_hub.models.ManageModuleStreamsOnManagedInstanceGroupDetails manage_module_streams_on_managed_instance_group_details: (required)
            A description of an operation to perform against the modules, streams, and profiles of a managed instance group

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.manage_module_streams_on_managed_instance_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.manage_module_streams_on_managed_instance_group(managed_instance_group_id, manage_module_streams_on_managed_instance_group_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def remove_module_stream_profile_from_managed_instance_group_and_wait_for_state(self, managed_instance_group_id, remove_module_stream_profile_from_managed_instance_group_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.remove_module_stream_profile_from_managed_instance_group` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_group_id: (required)
            The managed instance group OCID.

        :param oci.os_management_hub.models.RemoveModuleStreamProfileFromManagedInstanceGroupDetails remove_module_stream_profile_from_managed_instance_group_details: (required)
            Details for profiles to remove from the managed instance group.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.remove_module_stream_profile_from_managed_instance_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.remove_module_stream_profile_from_managed_instance_group(managed_instance_group_id, remove_module_stream_profile_from_managed_instance_group_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def remove_packages_from_managed_instance_group_and_wait_for_state(self, managed_instance_group_id, remove_packages_from_managed_instance_group_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.remove_packages_from_managed_instance_group` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_group_id: (required)
            The managed instance group OCID.

        :param oci.os_management_hub.models.RemovePackagesFromManagedInstanceGroupDetails remove_packages_from_managed_instance_group_details: (required)
            Details for packages to remove from the managed instance group.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.remove_packages_from_managed_instance_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.remove_packages_from_managed_instance_group(managed_instance_group_id, remove_packages_from_managed_instance_group_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_all_packages_on_managed_instance_group_and_wait_for_state(self, managed_instance_group_id, update_all_packages_on_managed_instance_group_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.update_all_packages_on_managed_instance_group` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_group_id: (required)
            The managed instance group OCID.

        :param oci.os_management_hub.models.UpdateAllPackagesOnManagedInstanceGroupDetails update_all_packages_on_managed_instance_group_details: (required)
            Details for update operation on the managed instance group.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.update_all_packages_on_managed_instance_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_all_packages_on_managed_instance_group(managed_instance_group_id, update_all_packages_on_managed_instance_group_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_managed_instance_group_and_wait_for_state(self, managed_instance_group_id, update_managed_instance_group_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.update_managed_instance_group` and waits for the :py:class:`~oci.os_management_hub.models.ManagedInstanceGroup` acted upon
        to enter the given state(s).

        :param str managed_instance_group_id: (required)
            The managed instance group OCID.

        :param oci.os_management_hub.models.UpdateManagedInstanceGroupDetails update_managed_instance_group_details: (required)
            The information to be updated.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.ManagedInstanceGroup.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceGroupClient.update_managed_instance_group`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_managed_instance_group(managed_instance_group_id, update_managed_instance_group_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        managed_instance_group_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_managed_instance_group(managed_instance_group_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
