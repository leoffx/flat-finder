from google.cloud import storage
from google.oauth2 import service_account

CREDENTIALS_DICT = {
    "type": "...",
    "project_id": "...",
    "private_key_id": "...",
    "private_key": "...",
    "client_email": "...",
    "client_id": "...",
    "auth_uri": "...",
    "token_uri": "...",
    "auth_provider_x509_cert_url": "...",
    "client_x509_cert_url": "..."
}

BUCKET_NAME = "..."


class GcloudClient:
    def __init__(self):

        credentials = service_account.Credentials.from_service_account_info(
            CREDENTIALS_DICT)

        storage_client = storage.Client(
            project=CREDENTIALS_DICT["project_id"], credentials=credentials)
        self.bucket = storage_client.bucket(BUCKET_NAME)

    def download_file(self, file_name):
        blob = self.bucket.blob(file_name)
        try:
            blob.download_to_filename(file_name)
        except Exception as e:
            print(e)
            with open(file_name, 'w+') as f:
                f.write('')

    def upload_file(self, file_name):
        blob = self.bucket.blob(file_name)
        blob.upload_from_filename(file_name)
