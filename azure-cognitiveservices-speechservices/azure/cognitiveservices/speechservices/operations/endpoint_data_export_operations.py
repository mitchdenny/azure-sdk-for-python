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


class EndpointDataExportOperations(object):
    """EndpointDataExportOperations operations.

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

    def create(
            self, endpoint_id, start_date, end_date, custom_headers=None, raw=False, **operation_config):
        """Create a new endpoint data export task.

        :param endpoint_id: The identifier of the endpoint.
        :type endpoint_id: str
        :param start_date: The start date of the demplyment data export
        :type start_date: datetime
        :param end_date: The end date of the demplyment data export
        :type end_date: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ErrorContent or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.speechservices.models.ErrorContent or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        endpoint_data_definition = models.EndpointDataDefinition(start_date=start_date, end_date=end_date)

        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'endpointId': self._serialize.url("endpoint_id", endpoint_id, 'str')
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
        body_content = self._serialize.body(endpoint_data_definition, 'EndpointDataDefinition')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [202, 400, 401, 403, 404, 429]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None
        header_dict = {}

        if response.status_code == 202:
            deserialized = self._deserialize('ErrorContent', response)
            header_dict = {
                'Location': 'str',
                'Operation-Location': 'str',
                'Retry-After': 'int',
                'X-RateLimit-Limit': 'int',
                'X-RateLimit-Remaining': 'int',
                'X-RateLimit-Reset': 'str',
            }
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorContent', response)
            header_dict = {
                'Location': 'str',
                'Operation-Location': 'str',
                'Retry-After': 'int',
                'X-RateLimit-Limit': 'int',
                'X-RateLimit-Remaining': 'int',
                'X-RateLimit-Reset': 'str',
            }
        if response.status_code == 401:
            deserialized = self._deserialize('ErrorContent', response)
            header_dict = {
                'Location': 'str',
                'Operation-Location': 'str',
                'Retry-After': 'int',
                'X-RateLimit-Limit': 'int',
                'X-RateLimit-Remaining': 'int',
                'X-RateLimit-Reset': 'str',
            }
        if response.status_code == 403:
            deserialized = self._deserialize('ErrorContent', response)
            header_dict = {
                'Location': 'str',
                'Operation-Location': 'str',
                'Retry-After': 'int',
                'X-RateLimit-Limit': 'int',
                'X-RateLimit-Remaining': 'int',
                'X-RateLimit-Reset': 'str',
            }
        if response.status_code == 404:
            deserialized = self._deserialize('ErrorContent', response)
            header_dict = {
                'Location': 'str',
                'Operation-Location': 'str',
                'Retry-After': 'int',
                'X-RateLimit-Limit': 'int',
                'X-RateLimit-Remaining': 'int',
                'X-RateLimit-Reset': 'str',
            }
        if response.status_code == 429:
            deserialized = self._deserialize('ErrorContent', response)
            header_dict = {
                'Location': 'str',
                'Operation-Location': 'str',
                'Retry-After': 'int',
                'X-RateLimit-Limit': 'int',
                'X-RateLimit-Remaining': 'int',
                'X-RateLimit-Reset': 'str',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    create.metadata = {'url': '/api/speechtotext/v2.0/endpoints/{endpointId}/data'}

    def get(
            self, endpoint_id, id, custom_headers=None, raw=False, **operation_config):
        """Gets the specified endpoint data export task for the authenticated
        user.

        :param endpoint_id: The identifier of the endpoint.
        :type endpoint_id: str
        :param id: The identifier of the data export.
        :type id: str
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
        path_format_arguments = {
            'endpointId': self._serialize.url("endpoint_id", endpoint_id, 'str'),
            'id': self._serialize.url("id", id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

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

        if response.status_code not in [200, 401, 403, 404, 429]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None
        header_dict = {}

        if response.status_code == 200:
            deserialized = self._deserialize('EndpointData', response)
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
        if response.status_code == 404:
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
    get.metadata = {'url': '/api/speechtotext/v2.0/endpoints/{endpointId}/data/{id}'}

    def delete(
            self, endpoint_id, id, custom_headers=None, raw=False, **operation_config):
        """Deletes the endpoint data export task identified by the given ID.

        :param endpoint_id: The identifier of the endpoint.
        :type endpoint_id: str
        :param id: The identifier of the endpoint data export.
        :type id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ErrorContent or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.speechservices.models.ErrorContent or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'endpointId': self._serialize.url("endpoint_id", endpoint_id, 'str'),
            'id': self._serialize.url("id", id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [204, 401, 403, 405, 429]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None
        header_dict = {}

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
        if response.status_code == 405:
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
    delete.metadata = {'url': '/api/speechtotext/v2.0/endpoints/{endpointId}/data/{id}'}
