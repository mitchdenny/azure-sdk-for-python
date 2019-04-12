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


class VoiceEndpointOperations(object):
    """VoiceEndpointOperations operations.

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

    def update(
            self, id, name, description=None, custom_headers=None, raw=False, **operation_config):
        """Updates the name and description of the endpoint identified by the
        given ID.

        :param id: The identifier of the endpoint.
        :type id: str
        :param name: The name of the object
        :type name: str
        :param description: The description of the object
        :type description: str
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
        endpoint_update = models.EndpointUpdate(name=name, description=description)

        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'id': self._serialize.url("id", id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(endpoint_update, 'EndpointUpdate')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 400, 401, 403, 409, 415, 429]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None
        header_dict = {}

        if response.status_code == 200:
            deserialized = self._deserialize('Endpoint', response)
            header_dict = {
                'X-RateLimit-Limit': 'int',
                'X-RateLimit-Remaining': 'int',
                'X-RateLimit-Reset': 'str',
                'Retry-After': 'int',
            }
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorContent', response)
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
        if response.status_code == 409:
            deserialized = self._deserialize('ErrorContent', response)
            header_dict = {
                'X-RateLimit-Limit': 'int',
                'X-RateLimit-Remaining': 'int',
                'X-RateLimit-Reset': 'str',
                'Retry-After': 'int',
            }
        if response.status_code == 415:
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
    update.metadata = {'url': '/api/texttospeech/v2.0/endpoints/{id}'}
