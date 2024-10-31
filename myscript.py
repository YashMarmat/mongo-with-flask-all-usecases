import os
from pymongo import MongoClient
from flask import Flask, jsonify, request
from dotenv import load_dotenv

# to read .env files
load_dotenv()

# app & configs
app = Flask(__name__)
app.config["SECRET_KEY"] = "my random secret key"

# MongoDB connection setup
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient('mongodb://root:yash1234@mongodb:27017/test_db?authSource=admin')
db = client['test_db'] # Replace with your database name


@app.route('/')
def homepage():
    new_document = {"name": "Jack", "age": 25}
    doc_exists = db.dummy_table.find_one(new_document)

    if doc_exists:
        print("# Exists")
        all_docs = db.dummy_table.find()

        # Filter (condition: some records may not have age field)
        all_docs = db.dummy_table.find({"age": {"$exists": True}})
        for each_doc in all_docs:
            print(each_doc['age'])
    else:
        print("# Document added.")
        db.dummy_table.insert_one(new_document)

    return jsonify({"message": "Document inserted successfully"}), 201

if __name__ == '__main__':
    # app.run(debug=True, port=8001)
    app.run(debug=True)