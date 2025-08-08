from flask import Flask, request, jsonify
from cloudant_utils import CloudantClient

app = Flask(__name__)
cloudant_client = CloudantClient()

@app.route("/add", methods=["POST"])
def add_document():
    data = request.json
    try:
        doc = cloudant_client.insert_document(data)
        return jsonify({"message": "Document added", "id": doc['_id']}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/docs", methods=["GET"])
def get_documents():
    try:
        docs = cloudant_client.get_all_documents()
        return jsonify(docs), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
