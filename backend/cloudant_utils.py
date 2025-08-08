import os
from cloudant import Cloudant
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

class CloudantClient:
    def __init__(self):
        account_name = os.getenv("CLOUDANT_ACCOUNT")
        api_key = os.getenv("CLOUDANT_API_KEY")
        url = os.getenv("CLOUDANT_URL")
        database = os.getenv("CLOUDANT_DATABASE")

        if not all([account_name, api_key, url, database]):
            raise ValueError("Missing Cloudant configuration in environment variables.")

        self.client = Cloudant.iam(
            account_name,
            api_key,
            url=url,
            connect=True
        )
        self.db = self._get_or_create_db(database)

    def _get_or_create_db(self, database):
        if database in self.client.all_dbs():
            return self.client[database]
        return self.client.create_database(database)

    def insert_document(self, data):
        doc = self.db.create_document(data)
        if doc.exists():
            return doc
        raise Exception("Document insertion failed.")

    def get_all_documents(self):
        return [doc for doc in self.db]
