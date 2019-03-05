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
from msrest.exceptions import HttpOperationError


class MachineLearningServiceError(Model):
    """Wrapper for error response to follow ARM guidelines.

    :param error: The error response.
    :type error: ~azure.mgmt.machinelearningservices.models.ErrorResponse
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorResponse'},
    }

    def __init__(self, **kwargs):
        super(MachineLearningServiceError, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class MachineLearningServiceErrorException(HttpOperationError):
    """Server responsed with exception of type: 'MachineLearningServiceError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(MachineLearningServiceErrorException, self).__init__(deserialize, response, 'MachineLearningServiceError', *args)
