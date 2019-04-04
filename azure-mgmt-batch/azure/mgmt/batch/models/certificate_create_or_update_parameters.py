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

from .proxy_resource import ProxyResource


class CertificateCreateOrUpdateParameters(ProxyResource):
    """Contains information about a certificate.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The ID of the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :ivar etag: The ETag of the resource, used for concurrency statements.
    :vartype etag: str
    :param thumbprint_algorithm: The algorithm of the certificate thumbprint.
     This must match the first portion of the certificate name. Currently
     required to be 'SHA1'.
    :type thumbprint_algorithm: str
    :param thumbprint: The thumbprint of the certificate. This must match the
     thumbprint from the name.
    :type thumbprint: str
    :param format: The format of the certificate - either Pfx or Cer. If
     omitted, the default is Pfx. Possible values include: 'Pfx', 'Cer'
    :type format: str or ~azure.mgmt.batch.models.CertificateFormat
    :param data: Required. The base64-encoded contents of the certificate. The
     maximum size is 10KB.
    :type data: str
    :param password: The password to access the certificate's private key.
     This is required if the certificate format is pfx and must be omitted if
     the certificate format is cer.
    :type password: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'etag': {'readonly': True},
        'data': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'thumbprint_algorithm': {'key': 'properties.thumbprintAlgorithm', 'type': 'str'},
        'thumbprint': {'key': 'properties.thumbprint', 'type': 'str'},
        'format': {'key': 'properties.format', 'type': 'CertificateFormat'},
        'data': {'key': 'properties.data', 'type': 'str'},
        'password': {'key': 'properties.password', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CertificateCreateOrUpdateParameters, self).__init__(**kwargs)
        self.thumbprint_algorithm = kwargs.get('thumbprint_algorithm', None)
        self.thumbprint = kwargs.get('thumbprint', None)
        self.format = kwargs.get('format', None)
        self.data = kwargs.get('data', None)
        self.password = kwargs.get('password', None)
