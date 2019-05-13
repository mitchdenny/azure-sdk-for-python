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


class VirtualMachineScaleSetUpdateVMProfile(Model):
    """Describes a virtual machine scale set virtual machine profile.

    :param os_profile: The virtual machine scale set OS profile.
    :type os_profile:
     ~azure.mgmt.compute.v2019_03_01.models.VirtualMachineScaleSetUpdateOSProfile
    :param storage_profile: The virtual machine scale set storage profile.
    :type storage_profile:
     ~azure.mgmt.compute.v2019_03_01.models.VirtualMachineScaleSetUpdateStorageProfile
    :param network_profile: The virtual machine scale set network profile.
    :type network_profile:
     ~azure.mgmt.compute.v2019_03_01.models.VirtualMachineScaleSetUpdateNetworkProfile
    :param diagnostics_profile: The virtual machine scale set diagnostics
     profile.
    :type diagnostics_profile:
     ~azure.mgmt.compute.v2019_03_01.models.DiagnosticsProfile
    :param extension_profile: The virtual machine scale set extension profile.
    :type extension_profile:
     ~azure.mgmt.compute.v2019_03_01.models.VirtualMachineScaleSetExtensionProfile
    :param license_type: The license type, which is for bring your own license
     scenario.
    :type license_type: str
    """

    _attribute_map = {
        'os_profile': {'key': 'osProfile', 'type': 'VirtualMachineScaleSetUpdateOSProfile'},
        'storage_profile': {'key': 'storageProfile', 'type': 'VirtualMachineScaleSetUpdateStorageProfile'},
        'network_profile': {'key': 'networkProfile', 'type': 'VirtualMachineScaleSetUpdateNetworkProfile'},
        'diagnostics_profile': {'key': 'diagnosticsProfile', 'type': 'DiagnosticsProfile'},
        'extension_profile': {'key': 'extensionProfile', 'type': 'VirtualMachineScaleSetExtensionProfile'},
        'license_type': {'key': 'licenseType', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(VirtualMachineScaleSetUpdateVMProfile, self).__init__(**kwargs)
        self.os_profile = kwargs.get('os_profile', None)
        self.storage_profile = kwargs.get('storage_profile', None)
        self.network_profile = kwargs.get('network_profile', None)
        self.diagnostics_profile = kwargs.get('diagnostics_profile', None)
        self.extension_profile = kwargs.get('extension_profile', None)
        self.license_type = kwargs.get('license_type', None)
