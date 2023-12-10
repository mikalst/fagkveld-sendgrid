from azure.storage.blob import BlobServiceClient, generate_account_sas
import datetime

def upload_file_to_blob(file_path, connection_string, key, container_name, blob_name) -> str:

    # Create a BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Create a ContainerClient
    container_client = blob_service_client.get_container_client(container_name)

    # Upload the file
    with open(file_path, "rb") as data:
        blob_client = container_client.upload_blob(name=blob_name, data=data, overwrite=True)

        expiry =  datetime.datetime.now() + datetime.timedelta(days=1)
        sas = generate_account_sas('stfagkveldsendgrid', key, 'o', 'r', expiry)

        # Generate a Shared Access Signature (SAS) token with read permissions
        return f'{blob_client.url}?{sas}'