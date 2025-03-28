# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190331

import oci  # noqa: F401
from oci.util import WAIT_RESOURCE_NOT_FOUND  # noqa: F401


class AnalyticsClientCompositeOperations(object):
    """
    This class provides a wrapper around :py:class:`~oci.analytics.AnalyticsClient` and offers convenience methods
    for operations that would otherwise need to be chained together. For example, instead of performing an action
    on a resource (e.g. launching an instance, creating a load balancer) and then using a waiter to wait for the resource
    to enter a given state, you can call a single method in this class to accomplish the same functionality
    """

    def __init__(self, client, **kwargs):
        """
        Creates a new AnalyticsClientCompositeOperations object

        :param AnalyticsClient client:
            The service client which will be wrapped by this object
        """
        self.client = client

    def change_analytics_instance_compartment_and_wait_for_state(self, analytics_instance_id, change_compartment_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.analytics.AnalyticsClient.change_analytics_instance_compartment` and waits for the :py:class:`~oci.analytics.models.WorkRequest`
        to enter the given state(s).

        :param str analytics_instance_id: (required)
            The OCID of the AnalyticsInstance.

        :param oci.analytics.models.ChangeCompartmentDetails change_compartment_details: (required)
            Input payload to move the resource to a different compartment.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.analytics.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.analytics.AnalyticsClient.change_analytics_instance_compartment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.change_analytics_instance_compartment(analytics_instance_id, change_compartment_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result
        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        if 'opc-work-request-id' not in operation_result.headers:
            return operation_result
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

    def change_analytics_instance_network_endpoint_and_wait_for_state(self, analytics_instance_id, change_analytics_instance_network_endpoint_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.analytics.AnalyticsClient.change_analytics_instance_network_endpoint` and waits for the :py:class:`~oci.analytics.models.WorkRequest`
        to enter the given state(s).

        :param str analytics_instance_id: (required)
            The OCID of the AnalyticsInstance.

        :param oci.analytics.models.ChangeAnalyticsInstanceNetworkEndpointDetails change_analytics_instance_network_endpoint_details: (required)
            Input payload for changing an Analytics instance network endpoint.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.analytics.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.analytics.AnalyticsClient.change_analytics_instance_network_endpoint`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.change_analytics_instance_network_endpoint(analytics_instance_id, change_analytics_instance_network_endpoint_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result
        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        if 'opc-work-request-id' not in operation_result.headers:
            return operation_result
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

    def create_analytics_instance_and_wait_for_state(self, create_analytics_instance_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.analytics.AnalyticsClient.create_analytics_instance` and waits for the :py:class:`~oci.analytics.models.WorkRequest`
        to enter the given state(s).

        :param oci.analytics.models.CreateAnalyticsInstanceDetails create_analytics_instance_details: (required)
            Analytics Instance details.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.analytics.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.analytics.AnalyticsClient.create_analytics_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_analytics_instance(create_analytics_instance_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result
        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        if 'opc-work-request-id' not in operation_result.headers:
            return operation_result
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

    def create_private_access_channel_and_wait_for_state(self, analytics_instance_id, create_private_access_channel_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.analytics.AnalyticsClient.create_private_access_channel` and waits for the :py:class:`~oci.analytics.models.WorkRequest`
        to enter the given state(s).

        :param str analytics_instance_id: (required)
            The OCID of the AnalyticsInstance.

        :param oci.analytics.models.CreatePrivateAccessChannelDetails create_private_access_channel_details: (required)
            Input payload for creating a private access channel for an Analytics instance.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.analytics.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.analytics.AnalyticsClient.create_private_access_channel`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_private_access_channel(analytics_instance_id, create_private_access_channel_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result
        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        if 'opc-work-request-id' not in operation_result.headers:
            return operation_result
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

    def create_vanity_url_and_wait_for_state(self, analytics_instance_id, create_vanity_url_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.analytics.AnalyticsClient.create_vanity_url` and waits for the :py:class:`~oci.analytics.models.WorkRequest`
        to enter the given state(s).

        :param str analytics_instance_id: (required)
            The OCID of the AnalyticsInstance.

        :param oci.analytics.models.CreateVanityUrlDetails create_vanity_url_details: (required)
            Vanity url details.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.analytics.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.analytics.AnalyticsClient.create_vanity_url`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_vanity_url(analytics_instance_id, create_vanity_url_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result
        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        if 'opc-work-request-id' not in operation_result.headers:
            return operation_result
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

    def delete_analytics_instance_and_wait_for_state(self, analytics_instance_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.analytics.AnalyticsClient.delete_analytics_instance` and waits for the :py:class:`~oci.analytics.models.WorkRequest`
        to enter the given state(s).

        :param str analytics_instance_id: (required)
            The OCID of the AnalyticsInstance.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.analytics.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.analytics.AnalyticsClient.delete_analytics_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_analytics_instance(analytics_instance_id, **operation_kwargs)
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                return WAIT_RESOURCE_NOT_FOUND
            else:
                raise e

        if not wait_for_states:
            return operation_result
        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        if 'opc-work-request-id' not in operation_result.headers:
            return operation_result
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

    def delete_private_access_channel_and_wait_for_state(self, private_access_channel_key, analytics_instance_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.analytics.AnalyticsClient.delete_private_access_channel` and waits for the :py:class:`~oci.analytics.models.WorkRequest`
        to enter the given state(s).

        :param str private_access_channel_key: (required)
            The unique identifier key of the Private Access Channel.

        :param str analytics_instance_id: (required)
            The OCID of the AnalyticsInstance.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.analytics.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.analytics.AnalyticsClient.delete_private_access_channel`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_private_access_channel(private_access_channel_key, analytics_instance_id, **operation_kwargs)
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                return WAIT_RESOURCE_NOT_FOUND
            else:
                raise e

        if not wait_for_states:
            return operation_result
        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        if 'opc-work-request-id' not in operation_result.headers:
            return operation_result
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

    def delete_vanity_url_and_wait_for_state(self, analytics_instance_id, vanity_url_key, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.analytics.AnalyticsClient.delete_vanity_url` and waits for the :py:class:`~oci.analytics.models.WorkRequest`
        to enter the given state(s).

        :param str analytics_instance_id: (required)
            The OCID of the AnalyticsInstance.

        :param str vanity_url_key: (required)
            Specify unique identifier key of a vanity url to update or delete.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.analytics.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.analytics.AnalyticsClient.delete_vanity_url`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_vanity_url(analytics_instance_id, vanity_url_key, **operation_kwargs)
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                return WAIT_RESOURCE_NOT_FOUND
            else:
                raise e

        if not wait_for_states:
            return operation_result
        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        if 'opc-work-request-id' not in operation_result.headers:
            return operation_result
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

    def scale_analytics_instance_and_wait_for_state(self, analytics_instance_id, scale_analytics_instance_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.analytics.AnalyticsClient.scale_analytics_instance` and waits for the :py:class:`~oci.analytics.models.WorkRequest`
        to enter the given state(s).

        :param str analytics_instance_id: (required)
            The OCID of the AnalyticsInstance.

        :param oci.analytics.models.ScaleAnalyticsInstanceDetails scale_analytics_instance_details: (required)
            Input payload for scaling an Analytics instance up or down.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.analytics.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.analytics.AnalyticsClient.scale_analytics_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.scale_analytics_instance(analytics_instance_id, scale_analytics_instance_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result
        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        if 'opc-work-request-id' not in operation_result.headers:
            return operation_result
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

    def set_feature_bundle_and_wait_for_state(self, analytics_instance_id, set_feature_bundle_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.analytics.AnalyticsClient.set_feature_bundle` and waits for the :py:class:`~oci.analytics.models.WorkRequest`
        to enter the given state(s).

        :param str analytics_instance_id: (required)
            The OCID of the AnalyticsInstance.

        :param oci.analytics.models.SetFeatureBundleDetails set_feature_bundle_details: (required)
            Input payload for the feature set of an Analytics instance.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.analytics.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.analytics.AnalyticsClient.set_feature_bundle`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.set_feature_bundle(analytics_instance_id, set_feature_bundle_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result
        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        if 'opc-work-request-id' not in operation_result.headers:
            return operation_result
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

    def set_kms_key_and_wait_for_state(self, analytics_instance_id, set_kms_key_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.analytics.AnalyticsClient.set_kms_key` and waits for the :py:class:`~oci.analytics.models.WorkRequest`
        to enter the given state(s).

        :param str analytics_instance_id: (required)
            The OCID of the AnalyticsInstance.

        :param oci.analytics.models.SetKmsKeyDetails set_kms_key_details: (required)
            Input payload to reset the OCI Vault encryption key.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.analytics.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.analytics.AnalyticsClient.set_kms_key`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.set_kms_key(analytics_instance_id, set_kms_key_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result
        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        if 'opc-work-request-id' not in operation_result.headers:
            return operation_result
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

    def start_analytics_instance_and_wait_for_state(self, analytics_instance_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.analytics.AnalyticsClient.start_analytics_instance` and waits for the :py:class:`~oci.analytics.models.WorkRequest`
        to enter the given state(s).

        :param str analytics_instance_id: (required)
            The OCID of the AnalyticsInstance.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.analytics.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.analytics.AnalyticsClient.start_analytics_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.start_analytics_instance(analytics_instance_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result
        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        if 'opc-work-request-id' not in operation_result.headers:
            return operation_result
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

    def stop_analytics_instance_and_wait_for_state(self, analytics_instance_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.analytics.AnalyticsClient.stop_analytics_instance` and waits for the :py:class:`~oci.analytics.models.WorkRequest`
        to enter the given state(s).

        :param str analytics_instance_id: (required)
            The OCID of the AnalyticsInstance.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.analytics.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.analytics.AnalyticsClient.stop_analytics_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.stop_analytics_instance(analytics_instance_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result
        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        if 'opc-work-request-id' not in operation_result.headers:
            return operation_result
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

    def update_analytics_instance_and_wait_for_state(self, analytics_instance_id, update_analytics_instance_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.analytics.AnalyticsClient.update_analytics_instance` and waits for the :py:class:`~oci.analytics.models.AnalyticsInstance` acted upon
        to enter the given state(s).

        :param str analytics_instance_id: (required)
            The OCID of the AnalyticsInstance.

        :param oci.analytics.models.UpdateAnalyticsInstanceDetails update_analytics_instance_details: (required)
            The Analytics Instance fields to update. Fields that are not provided
            will not be updated.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.analytics.models.AnalyticsInstance.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.analytics.AnalyticsClient.update_analytics_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_analytics_instance(analytics_instance_id, update_analytics_instance_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result
        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        analytics_instance_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_analytics_instance(analytics_instance_id),  # noqa: F821
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

    def update_private_access_channel_and_wait_for_state(self, private_access_channel_key, analytics_instance_id, update_private_access_channel_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.analytics.AnalyticsClient.update_private_access_channel` and waits for the :py:class:`~oci.analytics.models.WorkRequest`
        to enter the given state(s).

        :param str private_access_channel_key: (required)
            The unique identifier key of the Private Access Channel.

        :param str analytics_instance_id: (required)
            The OCID of the AnalyticsInstance.

        :param oci.analytics.models.UpdatePrivateAccessChannelDetails update_private_access_channel_details: (required)
            Update the Private Access Channel with the given unique identifier key in the specified Analytics Instance.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.analytics.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.analytics.AnalyticsClient.update_private_access_channel`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_private_access_channel(private_access_channel_key, analytics_instance_id, update_private_access_channel_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result
        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        if 'opc-work-request-id' not in operation_result.headers:
            return operation_result
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

    def update_vanity_url_and_wait_for_state(self, analytics_instance_id, vanity_url_key, update_vanity_url_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.analytics.AnalyticsClient.update_vanity_url` and waits for the :py:class:`~oci.analytics.models.WorkRequest`
        to enter the given state(s).

        :param str analytics_instance_id: (required)
            The OCID of the AnalyticsInstance.

        :param str vanity_url_key: (required)
            Specify unique identifier key of a vanity url to update or delete.

        :param oci.analytics.models.UpdateVanityUrlDetails update_vanity_url_details: (required)
            Vanity url details to update (certificate).

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.analytics.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.analytics.AnalyticsClient.update_vanity_url`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_vanity_url(analytics_instance_id, vanity_url_key, update_vanity_url_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result
        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        if 'opc-work-request-id' not in operation_result.headers:
            return operation_result
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
