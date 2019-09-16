import sqlite3
from db import db

# This UserModel here is an API, not a REST API, but an API, which exposes two endpoints
# This API, the two methods here, are an interface for other parts of the program to interact with the user thing,
# that includes writing it to the db and retrieving it from db

class UserModel(db.Model): # make the class extend db model = create mappings between the database and these objects
	# Telling SQLAlchemy the table and columns that this model is going to have
	__tablename__ = 'users'
	# The columns should match the properties under the __init__ function
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80))
	password = db.Column(db.String(80))


	def __init__(self, username, password):
		self.username = username
		self.password = password

	def save_to_db(self):
		db.session.add(self)
		db.session.commit() 

	@classmethod
	def find_by_username(cls, username):
		return cls.query.filter_by(username=username).first()

	@classmethod
	def find_by_id(cls, _id):
		return cls.query.filter_by(id=_id).first()