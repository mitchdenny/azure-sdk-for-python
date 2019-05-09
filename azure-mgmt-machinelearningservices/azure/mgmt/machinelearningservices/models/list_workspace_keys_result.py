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


class ListWorkspaceKeysResult(Model):
    """ListWorkspaceKeysResult.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar user_storage_key:
    :vartype user_storage_key: str
    :ivar user_storage_resource_id:
    :vartype user_storage_resource_id: str
    :ivar app_insights_instrumentation_key:
    :vartype app_insights_instrumentation_key: str
    :ivar container_registry_credentials:
    :vartype container_registry_credentials:
     ~azure.mgmt.machinelearningservices.models.RegistryListCredentialsResult
    """

    _validation = {
        'user_storage_key': {'readonly': True},
        'user_storage_resource_id': {'readonly': True},
        'app_insights_instrumentation_key': {'readonly': True},
        'container_registry_credentials': {'readonly': True},
    }

    _attribute_map = {
        'user_storage_key': {'key': 'userStorageKey', 'type': 'str'},
        'user_storage_resource_id': {'key': 'userStorageResourceId', 'type': 'str'},
        'app_insights_instrumentation_key': {'key': 'appInsightsInstrumentationKey', 'type': 'str'},
        'container_registry_credentials': {'key': 'containerRegistryCredentials', 'type': 'RegistryListCredentialsResult'},
    }

    def __init__(self, **kwargs):
        super(ListWorkspaceKeysResult, self).__init__(**kwargs)
        self.user_storage_key = None
        self.user_storage_resource_id = None
        self.app_insights_instrumentation_key = None
        self.container_registry_credentials = None
