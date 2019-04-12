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


class VoiceDatasetOperations(object):
    """VoiceDatasetOperations operations.

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

    def upload(
            self, name=None, description=None, locale=None, data_import_kind=None, properties=None, audiodata=None, transcriptions=None, custom_headers=None, raw=False, **operation_config):
        """Uploads data and creates a new voice data object.

        :param name: The name of this data import (always add this string for
         any import).
        :type name: str
        :param description: Optional description of this data import.
        :type description: str
        :param locale: The locale of this data import (always add this string
         for any import).
        :type locale: str
        :param data_import_kind: The kind of the data import (always add this
         string for any import). Possible values include: 'None', 'Language',
         'Acoustic', 'Pronunciation', 'CustomVoice', 'LanguageGeneration'
        :type data_import_kind: str
        :param properties: Optional properties of this data import (json
         serialized object with key/values, where all values must be strings)
        :type properties: str
        :param audiodata: A zip file containing the audio data.
        :type audiodata: Generator
        :param transcriptions: The transcriptions text file of the audio data.
        :type transcriptions: Generator
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
        url = self.upload.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'multipart/form-data'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct form data
        form_data_content = {
            'name': name,
            'description': description,
            'locale': locale,
            'dataImportKind': data_import_kind,
            'properties': properties,
            'audiodata': audiodata,
            'transcriptions': transcriptions,
        }

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, form_content=form_data_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [202, 400, 401, 403, 415, 429]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None
        header_dict = {}

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
        if response.status_code == 415:
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
    upload.metadata = {'url': '/api/texttospeech/v2.0/datasets/upload'}

    def delete(
            self, id, custom_headers=None, raw=False, **operation_config):
        """Deletes the voice dataset with the given id.

        :param id: The identifier of the voice dataset
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
    delete.metadata = {'url': '/api/texttospeech/v2.0/datasets/{id}'}

    def update(
            self, id, name, description=None, custom_headers=None, raw=False, **operation_config):
        """Updates the mutable details of the voice dataset identified by its ID.

        :param id: The identifier of the voice dataset.
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
        dataset_update = models.DatasetUpdate(name=name, description=description)

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
        body_content = self._serialize.body(dataset_update, 'DatasetUpdate')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 400, 401, 403, 409, 415, 429]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None
        header_dict = {}

        if response.status_code == 200:
            deserialized = self._deserialize('Dataset', response)
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
    update.metadata = {'url': '/api/texttospeech/v2.0/datasets/{id}'}
