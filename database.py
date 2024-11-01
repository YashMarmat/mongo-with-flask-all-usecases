import pymongo

class DuplicateRecordError(Exception):
    """Exception raised when a duplicate record is found in the database."""
    def __init__(self, message="Record already exists in the database"):
        super().__init__(message)

class Database:
	@classmethod
	def initialize(cls):
		client = pymongo.MongoClient('mongodb://root:yash1234@mongodb:27017/test_db?authSource=admin')
		cls.database = client['test_db']

	@classmethod
	def save_to_db(cls, data, collection_name):
		return cls.database[collection_name].insert_one(data)

	@classmethod
	def load_from_db_all(cls, collection_name, query):
		return cls.database[collection_name].find(query)

	@classmethod
	def load_from_db_one(cls, collection_name, query):
		return cls.database[collection_name].find_one(query)

        