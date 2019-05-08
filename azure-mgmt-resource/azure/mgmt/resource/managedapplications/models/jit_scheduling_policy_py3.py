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


class JitSchedulingPolicy(Model):
    """The JIT scheduling policies.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. The type of JIT schedule. Possible values include:
     'NotSpecified', 'Once', 'Recurring'
    :type type: str or
     ~azure.mgmt.resource.managedapplications.models.JitSchedulingType
    :param duration: Required. The required duration of the JIT request.
    :type duration: timedelta
    :param start_time: The start time of the request.
    :type start_time: datetime
    """

    _validation = {
        'type': {'required': True},
        'duration': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'Type', 'type': 'str'},
        'duration': {'key': 'Duration', 'type': 'duration'},
        'start_time': {'key': 'StartTime', 'type': 'iso-8601'},
    }

    def __init__(self, *, type, duration, start_time=None, **kwargs) -> None:
        super(JitSchedulingPolicy, self).__init__(**kwargs)
        self.type = type
        self.duration = duration
        self.start_time = start_time
