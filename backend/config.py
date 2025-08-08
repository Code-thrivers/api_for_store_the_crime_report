import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    # Watson Assistant
    WATSON_ASSISTANT_API_KEY = os.getenv("WATSON_ASSISTANT_API_KEY")
    WATSON_ASSISTANT_URL = os.getenv("WATSON_ASSISTANT_URL")
    WATSON_ASSISTANT_ID = os.getenv("WATSON_ASSISTANT_ID")

    # Cloudant DB
    CLOUDANT_APIKEY = os.getenv("CLOUDANT_APIKEY")
    CLOUDANT_URL = os.getenv("CLOUDANT_URL")
    CLOUDANT_USERNAME = os.getenv("CLOUDANT_USERNAME")
    CLOUDANT_DB_NAME = os.environ.get('CLOUDANT_DB_NAME','cloudant-a0')
