# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from knack.arguments import CLIArgumentType
from azure.cli.core.commands.parameters import (
    tags_type,
    get_three_state_flag,
    resource_group_name_type,
    get_location_type
)
from azext_storageimportexport.action import (
    AddReturnAddress,
    AddReturnShipping,
    AddDeliveryPackage,
    AddDriveList
)


def load_arguments(self, _):

    with self.argument_context('storageimportexport location list') as c:
        pass

    with self.argument_context('storageimportexport location show') as c:
        c.argument('location_name', help='The name of the location. For example, West US or westus.')

    with self.argument_context('storageimportexport job list') as c:
        c.argument('top', help='An integer value that specifies how many jobs at most should be returned. The value can'
                   'not exceed 100.')
        c.argument('filter', help='Can be used to restrict the results to certain conditions.')
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name uniquely identifies t'
                   'he resource group within the user subscription.')

    with self.argument_context('storageimportexport job show') as c:
        c.argument('job_name', help='The name of the import/export job.')
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name uniquely identifies t'
                   'he resource group within the user subscription.')

    with self.argument_context('storageimportexport job create') as c:
        c.argument('job_name', help='The name of the import/export job.')
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name uniquely identifies t'
                   'he resource group within the user subscription.')
        c.argument('client_tenant_id', help='The tenant ID of the client making the request.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='Specifies the supported Azure location w'
                   'here the job should be created')
        c.argument('tags', tags_type, help='Specifies the tags that will be assigned to the job.')
        c.argument('properties', arg_type=CLIArgumentType(options_list=['--properties'], help='Specifies the job proper'
                   'ties'))

    with self.argument_context('storageimportexport job update') as c:
        c.argument('job_name', help='The name of the import/export job.')
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name uniquely identifies t'
                   'he resource group within the user subscription.')
        c.argument('tags', tags_type, help='Specifies the tags that will be assigned to the job')
        c.argument('properties_cancel_requested', arg_type=get_three_state_flag(), help='If specified, the value must b'
                   'e true. The service will attempt to cancel the job.')
        c.argument('properties_state', help='If specified, the value must be Shipping, which tells the Import/Export se'
                   'rvice that the package for the job has been shipped. The ReturnAddress and DeliveryPackage properti'
                   'es must have been set either in this request or in a previous request, otherwise the request will f'
                   'ail.')
        c.argument('properties_return_address', action=AddReturnAddress, nargs='+', help='Specifies the return address '
                   'information for the job.')
        c.argument('properties_return_shipping', action=AddReturnShipping, nargs='+', help='Specifies the return carrie'
                   'r and customer\'s account with the carrier.')
        c.argument('properties_delivery_package', action=AddDeliveryPackage, nargs='+', help='Contains information abou'
                   't the package being shipped by the customer to the Microsoft data center.')
        c.argument('properties_log_level', help='Indicates whether error logging or verbose logging is enabled.')
        c.argument('properties_backup_drive_manifest', arg_type=get_three_state_flag(), help='Indicates whether the man'
                   'ifest files on the drives should be copied to block blobs.')
        c.argument('properties_drive_list', action=AddDriveList, nargs='+', help='List of drives that comprise the job.'
                   '')

    with self.argument_context('storageimportexport job delete') as c:
        c.argument('job_name', help='The name of the import/export job.')
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name uniquely identifies t'
                   'he resource group within the user subscription.')

    with self.argument_context('storageimportexport bit-locker-key list') as c:
        c.argument('job_name', help='The name of the import/export job.')
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name uniquely identifies t'
                   'he resource group within the user subscription.')
