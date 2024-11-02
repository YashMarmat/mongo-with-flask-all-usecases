from flask import jsonify
from ..models import Author
from ..serializers import AuthorSchema
from ..database import Database as DB
from ..utils import json_response_err

from . import main

# Routes
@main.route("/", methods=["GET", "POST"])
def new_homepage():
    try:
        author_data = {"name": "Jack 2", "books_written": 2}  # mimic data received
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
