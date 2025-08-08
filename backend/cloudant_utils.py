from cloudant import Cloudant

class CloudantClient:
    def __init__(self, account_name, api_key, url, database):  # Using 'database' as parameter
        self.client = Cloudant.iam(
            account_name,
            api_key,
            url=url,
            connect=True
        )
        self.database = database  # Store as db_name internally
        self.db = self._get_or_create_db()

    def _get_or_create_db(self):
        if self.database in self.client.all_dbs():
            return self.client[self.database]
        return self.client.create_database(self.database)

    def insert_document(self, data):
        doc = self.db.create_document(data)
        if doc.exists():
            return doc
        raise Exception("Document insertion failed.")

    def get_all_documents(self):
        return [doc for doc in self.db]