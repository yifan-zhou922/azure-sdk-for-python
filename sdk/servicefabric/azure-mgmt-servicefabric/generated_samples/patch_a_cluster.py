# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.servicefabric import ServiceFabricManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-servicefabric
# USAGE
    python patch_a_cluster.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ServiceFabricManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.clusters.begin_update(
        resource_group_name="resRg",
        cluster_name="myCluster",
        parameters={
            "properties": {
                "eventStoreServiceEnabled": True,
                "nodeTypes": [
                    {
                        "applicationPorts": {"endPort": 30000, "startPort": 20000},
                        "clientConnectionEndpointPort": 19000,
                        "durabilityLevel": "Bronze",
                        "ephemeralPorts": {"endPort": 64000, "startPort": 49000},
                        "httpGatewayEndpointPort": 19007,
                        "isPrimary": True,
                        "name": "nt1vm",
                        "vmInstanceCount": 5,
                    },
                    {
                        "applicationPorts": {"endPort": 2000, "startPort": 1000},
                        "clientConnectionEndpointPort": 0,
                        "durabilityLevel": "Bronze",
                        "ephemeralPorts": {"endPort": 4000, "startPort": 3000},
                        "httpGatewayEndpointPort": 0,
                        "isPrimary": False,
                        "name": "testnt1",
                        "vmInstanceCount": 3,
                    },
                ],
                "reliabilityLevel": "Bronze",
                "upgradeMode": "Automatic",
                "upgradePauseEndTimestampUtc": "2021-06-25T22:00:00Z",
                "upgradePauseStartTimestampUtc": "2021-06-21T22:00:00Z",
                "upgradeWave": "Wave",
            },
            "tags": {"a": "b"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/servicefabric/resource-manager/Microsoft.ServiceFabric/stable/2021-06-01/examples/ClusterPatchOperation_example.json
if __name__ == "__main__":
    main()