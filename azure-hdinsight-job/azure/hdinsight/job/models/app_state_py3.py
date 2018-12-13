# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AppState(Model):
    """The State of the application.

    :param state: The State of the application. Possible values include:
     'NEW', 'NEW_SAVING', 'SUBMITTED', 'ACCEPTED', 'RUNNING', 'FINISHED',
     'FAILED', 'KILLED'
    :type state: str or ~azure.hdinsight.job.models.ApplicationState
    """

    _attribute_map = {
        'state': {'key': 'state', 'type': 'ApplicationState'},
    }

    def __init__(self, *, state=None, **kwargs) -> None:
        super(AppState, self).__init__(**kwargs)
        self.state = state
