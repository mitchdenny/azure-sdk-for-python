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


class MaintenanceRedeployStatus(Model):
    """Maintenance Operation Status.

    :param is_customer_initiated_maintenance_allowed: True, if customer is
     allowed to perform Maintenance.
    :type is_customer_initiated_maintenance_allowed: bool
    :param pre_maintenance_window_start_time: Start Time for the Pre
     Maintenance Window.
    :type pre_maintenance_window_start_time: datetime
    :param pre_maintenance_window_end_time: End Time for the Pre Maintenance
     Window.
    :type pre_maintenance_window_end_time: datetime
    :param maintenance_window_start_time: Start Time for the Maintenance
     Window.
    :type maintenance_window_start_time: datetime
    :param maintenance_window_end_time: End Time for the Maintenance Window.
    :type maintenance_window_end_time: datetime
    :param last_operation_result_code: The Last Maintenance Operation Result
     Code. Possible values include: 'None', 'RetryLater', 'MaintenanceAborted',
     'MaintenanceCompleted'
    :type last_operation_result_code: str or
     ~azure.mgmt.compute.v2018_06_01.models.MaintenanceOperationResultCodeTypes
    :param last_operation_message: Message returned for the last Maintenance
     Operation.
    :type last_operation_message: str
    """

    _attribute_map = {
        'is_customer_initiated_maintenance_allowed': {'key': 'isCustomerInitiatedMaintenanceAllowed', 'type': 'bool'},
        'pre_maintenance_window_start_time': {'key': 'preMaintenanceWindowStartTime', 'type': 'iso-8601'},
        'pre_maintenance_window_end_time': {'key': 'preMaintenanceWindowEndTime', 'type': 'iso-8601'},
        'maintenance_window_start_time': {'key': 'maintenanceWindowStartTime', 'type': 'iso-8601'},
        'maintenance_window_end_time': {'key': 'maintenanceWindowEndTime', 'type': 'iso-8601'},
        'last_operation_result_code': {'key': 'lastOperationResultCode', 'type': 'MaintenanceOperationResultCodeTypes'},
        'last_operation_message': {'key': 'lastOperationMessage', 'type': 'str'},
    }

    def __init__(self, *, is_customer_initiated_maintenance_allowed: bool=None, pre_maintenance_window_start_time=None, pre_maintenance_window_end_time=None, maintenance_window_start_time=None, maintenance_window_end_time=None, last_operation_result_code=None, last_operation_message: str=None, **kwargs) -> None:
        super(MaintenanceRedeployStatus, self).__init__(**kwargs)
        self.is_customer_initiated_maintenance_allowed = is_customer_initiated_maintenance_allowed
        self.pre_maintenance_window_start_time = pre_maintenance_window_start_time
        self.pre_maintenance_window_end_time = pre_maintenance_window_end_time
        self.maintenance_window_start_time = maintenance_window_start_time
        self.maintenance_window_end_time = maintenance_window_end_time
        self.last_operation_result_code = last_operation_result_code
        self.last_operation_message = last_operation_message
