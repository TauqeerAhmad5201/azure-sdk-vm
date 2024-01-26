import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

# Replace with your Azure subscription ID and resource group name
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"] = "21521513-b56f-4fea-aefb-a1ea61b32126"
resource_group_name = "python-azure-vm-example-rg"

# Initialize Azure credentials
credential = DefaultAzureCredential()

# Create a Resource Management Client
resource_client = ResourceManagementClient(credential, subscription_id)

def delete_resource_group():
    try:
        # Delete the resource group
        resource_client.resource_groups.begin_delete(resource_group_name)
        print(f"Deleting resource group '{resource_group_name}'...")
    except Exception as e:
        print(f"Error deleting resource group: {str(e)}")

if __name__ == "__main__":
    delete_resource_group()
