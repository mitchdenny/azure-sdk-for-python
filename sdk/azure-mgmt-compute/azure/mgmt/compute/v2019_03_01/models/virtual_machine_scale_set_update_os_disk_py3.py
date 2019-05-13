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


class VirtualMachineScaleSetUpdateOSDisk(Model):
    """Describes virtual machine scale set operating system disk Update Object.
    This should be used for Updating VMSS OS Disk.

    :param caching: The caching type. Possible values include: 'None',
     'ReadOnly', 'ReadWrite'
    :type caching: str or ~azure.mgmt.compute.v2019_03_01.models.CachingTypes
    :param write_accelerator_enabled: Specifies whether writeAccelerator
     should be enabled or disabled on the disk.
    :type write_accelerator_enabled: bool
    :param disk_size_gb: Specifies the size of the operating system disk in
     gigabytes. This element can be used to overwrite the size of the disk in a
     virtual machine image. <br><br> This value cannot be larger than 1023 GB
    :type disk_size_gb: int
    :param image: The Source User Image VirtualHardDisk. This VirtualHardDisk
     will be copied before using it to attach to the Virtual Machine. If
     SourceImage is provided, the destination VirtualHardDisk should not exist.
    :type image: ~azure.mgmt.compute.v2019_03_01.models.VirtualHardDisk
    :param vhd_containers: The list of virtual hard disk container uris.
    :type vhd_containers: list[str]
    :param managed_disk: The managed disk parameters.
    :type managed_disk:
     ~azure.mgmt.compute.v2019_03_01.models.VirtualMachineScaleSetManagedDiskParameters
    """

    _attribute_map = {
        'caching': {'key': 'caching', 'type': 'CachingTypes'},
        'write_accelerator_enabled': {'key': 'writeAcceleratorEnabled', 'type': 'bool'},
        'disk_size_gb': {'key': 'diskSizeGB', 'type': 'int'},
        'image': {'key': 'image', 'type': 'VirtualHardDisk'},
        'vhd_containers': {'key': 'vhdContainers', 'type': '[str]'},
        'managed_disk': {'key': 'managedDisk', 'type': 'VirtualMachineScaleSetManagedDiskParameters'},
    }

    def __init__(self, *, caching=None, write_accelerator_enabled: bool=None, disk_size_gb: int=None, image=None, vhd_containers=None, managed_disk=None, **kwargs) -> None:
        super(VirtualMachineScaleSetUpdateOSDisk, self).__init__(**kwargs)
        self.caching = caching
        self.write_accelerator_enabled = write_accelerator_enabled
        self.disk_size_gb = disk_size_gb
        self.image = image
        self.vhd_containers = vhd_containers
        self.managed_disk = managed_disk
