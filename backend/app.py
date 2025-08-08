# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from cloudant_utils import CloudantClient
from config import Config

app = Flask(__name__)
CORS(app)  # Allow React (port 5173 or 3000) to talk to Flask (5000)

print(f">>>{Config.CLOUDANT_DB_NAME}<<<")

cloudant_client = CloudantClient(
    account_name="f297abe0-76c5-4d75-a58a-57c43e5b6588-bluemix",
    api_key="f0RUugbvJJP1VXzwK4y5fV9WtHmjlaw5XTZRrcj6cKaM",
    url="https://f297abe0-76c5-4d75-a58a-57c43e5b6588-bluemix.cloudantnosqldb.appdomain.cloud",
    database="cloudant-a0"
)

@app.route('/test_db')
def test_db():
    try:
        return jsonify({"status": "Connected", "db": cloudant_client.database}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/store', methods=['POST'])
def store_data():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400
    try:
        document = cloudant_client.insert_document(data)
        return jsonify({"message": "Data inserted", "id": document['_id']}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/data', methods=['GET'])
def get_data():
    try:
        documents = cloudant_client.get_all_documents()
        return jsonify(documents), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
