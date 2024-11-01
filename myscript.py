import os
from pymongo import MongoClient
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from marshmallow import Schema, fields
from models import Author, Book
from serializers import AuthorSchema, BookSchema
from utils import json_response_err
from database import Database as DB

# to read .env files
load_dotenv()

# app & configs
app = Flask(__name__)
app.config["SECRET_KEY"] = "my random secret key"

# Initializations
DB.initialize()


# Routes
@app.route("/")
def new_homepage():
    try:
        author_data = {"name": "Jack", "books_written": 2}  # mimic data received
        author_schema = AuthorSchema()

        # data verification happens with load (provided by marshmallow)
        valid_data = author_schema.load(author_data)
        new_author = Author(**valid_data)

        # check if same author exists
        author_exists = DB.load_from_db_one('author', {"name": new_author.name})
        if author_exists:
            return json_response_err("name", "name already exists!", "Data save failed!")
        
        # save author in db
        DB.save_to_db(author_data, "author")
        return jsonify({"msg": f"New Author {new_author.name} added."}), 201
    except Exception as err:
        return jsonify({"msg:": "Data save failed!", "errors": err.args}), 404


if __name__ == "__main__":
    # app.run(debug=True, port=8001)
    app.run(debug=True)
