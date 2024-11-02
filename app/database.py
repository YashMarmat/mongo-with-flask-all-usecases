import pymongo

class DuplicateRecordError(Exception):
    """Exception raised when a duplicate record is found in the database."""
    def __init__(self, message="Record already exists in the database"):
        super().__init__(message)

class Database:
    database = None  # Class-level attribute to hold the database instance

    @classmethod
    def initialize(cls, uri):
        """Initialize the database connection and store it in the class attribute."""
        client = pymongo.MongoClient(uri)
        cls.database = client.get_database()  # Store the database instance

    @classmethod
    def save_to_db(cls, data, collection_name):
        """Save a document to the specified collection."""
        if cls.database is None:
            raise Exception("Database not initialized. Call Database.initialize first.")
        return cls.database[collection_name].insert_one(data)

    @classmethod
    def load_from_db_all(cls, collection_name, query={}):
        """Load all documents that match the query from the specified collection."""
        if cls.database is None:
            raise Exception("Database not initialized. Call Database.initialize first.")
        return cls.database[collection_name].find(query)

    @classmethod
    def load_from_db_one(cls, collection_name, query):
        """Load a single document that matches the query from the specified collection."""
        if cls.database is None:
            raise Exception("Database not initialized. Call Database.initialize first.")
        return cls.database[collection_name].find_one(query)
