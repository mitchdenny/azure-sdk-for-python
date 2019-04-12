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

from msrest.pipeline import ClientRawResponse
from msrest.exceptions import HttpOperationError

from .. import models


class ModelsOperations(object):
    """ModelsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def get(
            self, custom_headers=None, raw=False, **operation_config):
        """Gets the list of models for the authenticated subscription.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 401, 403, 429]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None
        header_dict = {}

        if response.status_code == 200:
            deserialized = self._deserialize('[Model]', response)
            header_dict = {
                'X-RateLimit-Limit': 'int',
                'X-RateLimit-Remaining': 'int',
                'X-RateLimit-Reset': 'str',
                'Retry-After': 'int',
            }
        if response.status_code == 401:
            deserialized = self._deserialize('ErrorContent', response)
            header_dict = {
                'X-RateLimit-Limit': 'int',
                'X-RateLimit-Remaining': 'int',
                'X-RateLimit-Reset': 'str',
                'Retry-After': 'int',
            }
        if response.status_code == 403:
            deserialized = self._deserialize('ErrorContent', response)
            header_dict = {
                'X-RateLimit-Limit': 'int',
                'X-RateLimit-Remaining': 'int',
                'X-RateLimit-Reset': 'str',
                'Retry-After': 'int',
            }
        if response.status_code == 429:
            deserialized = self._deserialize('ErrorContent', response)
            header_dict = {
                'X-RateLimit-Limit': 'int',
                'X-RateLimit-Remaining': 'int',
                'X-RateLimit-Reset': 'str',
                'Retry-After': 'int',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/api/speechtotext/v2.0/models'}
