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

from msrest.service_client import SDKClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from msrest.exceptions import HttpOperationError
from .operations.accuracy_tests_operations import AccuracyTestsOperations
from .operations.accuracy_test_operations import AccuracyTestOperations
from .operations.datasets_operations import DatasetsOperations
from .operations.dataset_operations import DatasetOperations
from .operations.supported_locales_for_datasets_operations import SupportedLocalesForDatasetsOperations
from .operations.endpoints_operations import EndpointsOperations
from .operations.endpoint_operations import EndpointOperations
from .operations.supported_locales_for_endpoints_operations import SupportedLocalesForEndpointsOperations
from .operations.endpoint_data_exports_operations import EndpointDataExportsOperations
from .operations.endpoint_data_export_operations import EndpointDataExportOperations
from .operations.endpoint_data_operations import EndpointDataOperations
from .operations.models_operations import ModelsOperations
from .operations.model_operations import ModelOperations
from .operations.supported_locales_for_models_operations import SupportedLocalesForModelsOperations
from .operations.transcriptions_operations import TranscriptionsOperations
from .operations.transcription_operations import TranscriptionOperations
from .operations.supported_locales_for_transcriptions_operations import SupportedLocalesForTranscriptionsOperations
from .operations.language_generation_endpoints_operations import LanguageGenerationEndpointsOperations
from .operations.language_generation_endpoint_operations import LanguageGenerationEndpointOperations
from .operations.supported_locales_for_language_generation_endpoints_operations import SupportedLocalesForLanguageGenerationEndpointsOperations
from .operations.language_generation_models_operations import LanguageGenerationModelsOperations
from .operations.language_generation_model_operations import LanguageGenerationModelOperations
from .operations.supported_locales_for_language_generation_models_operations import SupportedLocalesForLanguageGenerationModelsOperations
from .operations.health_status_operations import HealthStatusOperations
from .operations.voice_datasets_operations import VoiceDatasetsOperations
from .operations.supported_locales_for_voice_datasets_operations import SupportedLocalesForVoiceDatasetsOperations
from .operations.voice_dataset_operations import VoiceDatasetOperations
from .operations.voice_deployments_operations import VoiceDeploymentsOperations
from .operations.voice_deployment_operations import VoiceDeploymentOperations
from .operations.deployment_operations import DeploymentOperations
from .operations.voice_endpoint_operations import VoiceEndpointOperations
from .operations.supported_locales_for_voice_endpoints_operations import SupportedLocalesForVoiceEndpointsOperations
from .operations.voice_models_operations import VoiceModelsOperations
from .operations.voice_model_operations import VoiceModelOperations
from .operations.supported_locales_for_voice_models_operations import SupportedLocalesForVoiceModelsOperations
from .operations.voice_test_operations import VoiceTestOperations
from . import models


class SpeechServicesAPIv20Configuration(Configuration):
    """Configuration for SpeechServicesAPIv20
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'https://westus.cris.ai'

        super(SpeechServicesAPIv20Configuration, self).__init__(base_url)

        self.add_user_agent('azure-cognitiveservices-speechservices/{}'.format(VERSION))

        self.credentials = credentials


class SpeechServicesAPIv20(SDKClient):
    """Speech Services API v2.0.

    :ivar config: Configuration for client.
    :vartype config: SpeechServicesAPIv20Configuration

    :ivar accuracy_tests: AccuracyTests operations
    :vartype accuracy_tests: azure.cognitiveservices.speechservices.operations.AccuracyTestsOperations
    :ivar accuracy_test: AccuracyTest operations
    :vartype accuracy_test: azure.cognitiveservices.speechservices.operations.AccuracyTestOperations
    :ivar datasets: Datasets operations
    :vartype datasets: azure.cognitiveservices.speechservices.operations.DatasetsOperations
    :ivar dataset: Dataset operations
    :vartype dataset: azure.cognitiveservices.speechservices.operations.DatasetOperations
    :ivar supported_locales_for_datasets: SupportedLocalesForDatasets operations
    :vartype supported_locales_for_datasets: azure.cognitiveservices.speechservices.operations.SupportedLocalesForDatasetsOperations
    :ivar endpoints: Endpoints operations
    :vartype endpoints: azure.cognitiveservices.speechservices.operations.EndpointsOperations
    :ivar endpoint: Endpoint operations
    :vartype endpoint: azure.cognitiveservices.speechservices.operations.EndpointOperations
    :ivar supported_locales_for_endpoints: SupportedLocalesForEndpoints operations
    :vartype supported_locales_for_endpoints: azure.cognitiveservices.speechservices.operations.SupportedLocalesForEndpointsOperations
    :ivar endpoint_data_exports: EndpointDataExports operations
    :vartype endpoint_data_exports: azure.cognitiveservices.speechservices.operations.EndpointDataExportsOperations
    :ivar endpoint_data_export: EndpointDataExport operations
    :vartype endpoint_data_export: azure.cognitiveservices.speechservices.operations.EndpointDataExportOperations
    :ivar endpoint_data: EndpointData operations
    :vartype endpoint_data: azure.cognitiveservices.speechservices.operations.EndpointDataOperations
    :ivar models: Models operations
    :vartype models: azure.cognitiveservices.speechservices.operations.ModelsOperations
    :ivar model: Model operations
    :vartype model: azure.cognitiveservices.speechservices.operations.ModelOperations
    :ivar supported_locales_for_models: SupportedLocalesForModels operations
    :vartype supported_locales_for_models: azure.cognitiveservices.speechservices.operations.SupportedLocalesForModelsOperations
    :ivar transcriptions: Transcriptions operations
    :vartype transcriptions: azure.cognitiveservices.speechservices.operations.TranscriptionsOperations
    :ivar transcription: Transcription operations
    :vartype transcription: azure.cognitiveservices.speechservices.operations.TranscriptionOperations
    :ivar supported_locales_for_transcriptions: SupportedLocalesForTranscriptions operations
    :vartype supported_locales_for_transcriptions: azure.cognitiveservices.speechservices.operations.SupportedLocalesForTranscriptionsOperations
    :ivar language_generation_endpoints: LanguageGenerationEndpoints operations
    :vartype language_generation_endpoints: azure.cognitiveservices.speechservices.operations.LanguageGenerationEndpointsOperations
    :ivar language_generation_endpoint: LanguageGenerationEndpoint operations
    :vartype language_generation_endpoint: azure.cognitiveservices.speechservices.operations.LanguageGenerationEndpointOperations
    :ivar supported_locales_for_language_generation_endpoints: SupportedLocalesForLanguageGenerationEndpoints operations
    :vartype supported_locales_for_language_generation_endpoints: azure.cognitiveservices.speechservices.operations.SupportedLocalesForLanguageGenerationEndpointsOperations
    :ivar language_generation_models: LanguageGenerationModels operations
    :vartype language_generation_models: azure.cognitiveservices.speechservices.operations.LanguageGenerationModelsOperations
    :ivar language_generation_model: LanguageGenerationModel operations
    :vartype language_generation_model: azure.cognitiveservices.speechservices.operations.LanguageGenerationModelOperations
    :ivar supported_locales_for_language_generation_models: SupportedLocalesForLanguageGenerationModels operations
    :vartype supported_locales_for_language_generation_models: azure.cognitiveservices.speechservices.operations.SupportedLocalesForLanguageGenerationModelsOperations
    :ivar health_status: HealthStatus operations
    :vartype health_status: azure.cognitiveservices.speechservices.operations.HealthStatusOperations
    :ivar voice_datasets: VoiceDatasets operations
    :vartype voice_datasets: azure.cognitiveservices.speechservices.operations.VoiceDatasetsOperations
    :ivar supported_locales_for_voice_datasets: SupportedLocalesForVoiceDatasets operations
    :vartype supported_locales_for_voice_datasets: azure.cognitiveservices.speechservices.operations.SupportedLocalesForVoiceDatasetsOperations
    :ivar voice_dataset: VoiceDataset operations
    :vartype voice_dataset: azure.cognitiveservices.speechservices.operations.VoiceDatasetOperations
    :ivar voice_deployments: VoiceDeployments operations
    :vartype voice_deployments: azure.cognitiveservices.speechservices.operations.VoiceDeploymentsOperations
    :ivar voice_deployment: VoiceDeployment operations
    :vartype voice_deployment: azure.cognitiveservices.speechservices.operations.VoiceDeploymentOperations
    :ivar deployment: Deployment operations
    :vartype deployment: azure.cognitiveservices.speechservices.operations.DeploymentOperations
    :ivar voice_endpoint: VoiceEndpoint operations
    :vartype voice_endpoint: azure.cognitiveservices.speechservices.operations.VoiceEndpointOperations
    :ivar supported_locales_for_voice_endpoints: SupportedLocalesForVoiceEndpoints operations
    :vartype supported_locales_for_voice_endpoints: azure.cognitiveservices.speechservices.operations.SupportedLocalesForVoiceEndpointsOperations
    :ivar voice_models: VoiceModels operations
    :vartype voice_models: azure.cognitiveservices.speechservices.operations.VoiceModelsOperations
    :ivar voice_model: VoiceModel operations
    :vartype voice_model: azure.cognitiveservices.speechservices.operations.VoiceModelOperations
    :ivar supported_locales_for_voice_models: SupportedLocalesForVoiceModels operations
    :vartype supported_locales_for_voice_models: azure.cognitiveservices.speechservices.operations.SupportedLocalesForVoiceModelsOperations
    :ivar voice_test: VoiceTest operations
    :vartype voice_test: azure.cognitiveservices.speechservices.operations.VoiceTestOperations

    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = SpeechServicesAPIv20Configuration(credentials, base_url)
        super(SpeechServicesAPIv20, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = 'v2.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.accuracy_tests = AccuracyTestsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.accuracy_test = AccuracyTestOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.datasets = DatasetsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.dataset = DatasetOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.supported_locales_for_datasets = SupportedLocalesForDatasetsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.endpoints = EndpointsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.endpoint = EndpointOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.supported_locales_for_endpoints = SupportedLocalesForEndpointsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.endpoint_data_exports = EndpointDataExportsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.endpoint_data_export = EndpointDataExportOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.endpoint_data = EndpointDataOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.models = ModelsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.model = ModelOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.supported_locales_for_models = SupportedLocalesForModelsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.transcriptions = TranscriptionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.transcription = TranscriptionOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.supported_locales_for_transcriptions = SupportedLocalesForTranscriptionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.language_generation_endpoints = LanguageGenerationEndpointsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.language_generation_endpoint = LanguageGenerationEndpointOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.supported_locales_for_language_generation_endpoints = SupportedLocalesForLanguageGenerationEndpointsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.language_generation_models = LanguageGenerationModelsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.language_generation_model = LanguageGenerationModelOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.supported_locales_for_language_generation_models = SupportedLocalesForLanguageGenerationModelsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.health_status = HealthStatusOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.voice_datasets = VoiceDatasetsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.supported_locales_for_voice_datasets = SupportedLocalesForVoiceDatasetsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.voice_dataset = VoiceDatasetOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.voice_deployments = VoiceDeploymentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.voice_deployment = VoiceDeploymentOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.deployment = DeploymentOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.voice_endpoint = VoiceEndpointOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.supported_locales_for_voice_endpoints = SupportedLocalesForVoiceEndpointsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.voice_models = VoiceModelsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.voice_model = VoiceModelOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.supported_locales_for_voice_models = SupportedLocalesForVoiceModelsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.voice_test = VoiceTestOperations(
            self._client, self.config, self._serialize, self._deserialize)
