# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630

from .merge_pull_request_details import MergePullRequestDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExecuteMergePullRequestDetails(MergePullRequestDetails):
    """
    The information about the merge.
    """

    #: A constant which can be used with the merge_strategy property of a ExecuteMergePullRequestDetails.
    #: This constant has a value of "MERGE_COMMIT"
    MERGE_STRATEGY_MERGE_COMMIT = "MERGE_COMMIT"

    #: A constant which can be used with the merge_strategy property of a ExecuteMergePullRequestDetails.
    #: This constant has a value of "FAST_FORWARD"
    MERGE_STRATEGY_FAST_FORWARD = "FAST_FORWARD"

    #: A constant which can be used with the merge_strategy property of a ExecuteMergePullRequestDetails.
    #: This constant has a value of "FAST_FORWARD_ONLY"
    MERGE_STRATEGY_FAST_FORWARD_ONLY = "FAST_FORWARD_ONLY"

    #: A constant which can be used with the merge_strategy property of a ExecuteMergePullRequestDetails.
    #: This constant has a value of "REBASE_AND_MERGE"
    MERGE_STRATEGY_REBASE_AND_MERGE = "REBASE_AND_MERGE"

    #: A constant which can be used with the merge_strategy property of a ExecuteMergePullRequestDetails.
    #: This constant has a value of "REBASE_AND_FAST_FORWARD"
    MERGE_STRATEGY_REBASE_AND_FAST_FORWARD = "REBASE_AND_FAST_FORWARD"

    #: A constant which can be used with the merge_strategy property of a ExecuteMergePullRequestDetails.
    #: This constant has a value of "SQUASH"
    MERGE_STRATEGY_SQUASH = "SQUASH"

    #: A constant which can be used with the merge_strategy property of a ExecuteMergePullRequestDetails.
    #: This constant has a value of "SQUASH_FAST_FORWARD_ONLY"
    MERGE_STRATEGY_SQUASH_FAST_FORWARD_ONLY = "SQUASH_FAST_FORWARD_ONLY"

    #: A constant which can be used with the post_merge_action property of a ExecuteMergePullRequestDetails.
    #: This constant has a value of "DELETE_SOURCE_BRANCH"
    POST_MERGE_ACTION_DELETE_SOURCE_BRANCH = "DELETE_SOURCE_BRANCH"

    #: A constant which can be used with the post_merge_action property of a ExecuteMergePullRequestDetails.
    #: This constant has a value of "KEEP_SOURCE_BRANCH"
    POST_MERGE_ACTION_KEEP_SOURCE_BRANCH = "KEEP_SOURCE_BRANCH"

    def __init__(self, **kwargs):
        """
        Initializes a new ExecuteMergePullRequestDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.ExecuteMergePullRequestDetails.action_type` attribute
        of this class is ``EXECUTE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action_type:
            The value to assign to the action_type property of this ExecuteMergePullRequestDetails.
            Allowed values for this property are: "EXECUTE", "VALIDATE"
        :type action_type: str

        :param commit_message:
            The value to assign to the commit_message property of this ExecuteMergePullRequestDetails.
        :type commit_message: str

        :param merge_strategy:
            The value to assign to the merge_strategy property of this ExecuteMergePullRequestDetails.
            Allowed values for this property are: "MERGE_COMMIT", "FAST_FORWARD", "FAST_FORWARD_ONLY", "REBASE_AND_MERGE", "REBASE_AND_FAST_FORWARD", "SQUASH", "SQUASH_FAST_FORWARD_ONLY"
        :type merge_strategy: str

        :param post_merge_action:
            The value to assign to the post_merge_action property of this ExecuteMergePullRequestDetails.
            Allowed values for this property are: "DELETE_SOURCE_BRANCH", "KEEP_SOURCE_BRANCH"
        :type post_merge_action: str

        """
        self.swagger_types = {
            'action_type': 'str',
            'commit_message': 'str',
            'merge_strategy': 'str',
            'post_merge_action': 'str'
        }
        self.attribute_map = {
            'action_type': 'actionType',
            'commit_message': 'commitMessage',
            'merge_strategy': 'mergeStrategy',
            'post_merge_action': 'postMergeAction'
        }
        self._action_type = None
        self._commit_message = None
        self._merge_strategy = None
        self._post_merge_action = None
        self._action_type = 'EXECUTE'

    @property
    def commit_message(self):
        """
        **[Required]** Gets the commit_message of this ExecuteMergePullRequestDetails.
        The commit message to be shown for this pull request in the destination branch after merge is done.


        :return: The commit_message of this ExecuteMergePullRequestDetails.
        :rtype: str
        """
        return self._commit_message

    @commit_message.setter
    def commit_message(self, commit_message):
        """
        Sets the commit_message of this ExecuteMergePullRequestDetails.
        The commit message to be shown for this pull request in the destination branch after merge is done.


        :param commit_message: The commit_message of this ExecuteMergePullRequestDetails.
        :type: str
        """
        self._commit_message = commit_message

    @property
    def merge_strategy(self):
        """
        **[Required]** Gets the merge_strategy of this ExecuteMergePullRequestDetails.
        the strategy of merging.

        Allowed values for this property are: "MERGE_COMMIT", "FAST_FORWARD", "FAST_FORWARD_ONLY", "REBASE_AND_MERGE", "REBASE_AND_FAST_FORWARD", "SQUASH", "SQUASH_FAST_FORWARD_ONLY"


        :return: The merge_strategy of this ExecuteMergePullRequestDetails.
        :rtype: str
        """
        return self._merge_strategy

    @merge_strategy.setter
    def merge_strategy(self, merge_strategy):
        """
        Sets the merge_strategy of this ExecuteMergePullRequestDetails.
        the strategy of merging.


        :param merge_strategy: The merge_strategy of this ExecuteMergePullRequestDetails.
        :type: str
        """
        allowed_values = ["MERGE_COMMIT", "FAST_FORWARD", "FAST_FORWARD_ONLY", "REBASE_AND_MERGE", "REBASE_AND_FAST_FORWARD", "SQUASH", "SQUASH_FAST_FORWARD_ONLY"]
        if not value_allowed_none_or_none_sentinel(merge_strategy, allowed_values):
            raise ValueError(
                f"Invalid value for `merge_strategy`, must be None or one of {allowed_values}"
            )
        self._merge_strategy = merge_strategy

    @property
    def post_merge_action(self):
        """
        Gets the post_merge_action of this ExecuteMergePullRequestDetails.
        What needs to happen after the merge is done successfully.

        Allowed values for this property are: "DELETE_SOURCE_BRANCH", "KEEP_SOURCE_BRANCH"


        :return: The post_merge_action of this ExecuteMergePullRequestDetails.
        :rtype: str
        """
        return self._post_merge_action

    @post_merge_action.setter
    def post_merge_action(self, post_merge_action):
        """
        Sets the post_merge_action of this ExecuteMergePullRequestDetails.
        What needs to happen after the merge is done successfully.


        :param post_merge_action: The post_merge_action of this ExecuteMergePullRequestDetails.
        :type: str
        """
        allowed_values = ["DELETE_SOURCE_BRANCH", "KEEP_SOURCE_BRANCH"]
        if not value_allowed_none_or_none_sentinel(post_merge_action, allowed_values):
            raise ValueError(
                f"Invalid value for `post_merge_action`, must be None or one of {allowed_values}"
            )
        self._post_merge_action = post_merge_action

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
