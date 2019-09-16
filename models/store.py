from db import db

class StoreModel(db.Model):
	__tablename__ = 'stores'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))

	items = db.relationship('ItemModel', lazy='dynamic') # a list of items

	def __init__(self, name):
		self.name = name

	def json(self):
		return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

	@classmethod
	# This method should stay as a classmethod, as it's going to return an object of ItemModel
	def find_by_name(cls, name):
		return cls.query.filter_by(name=name).first()

	def save_to_db(self): # work both for insert and update
		# SQLAlchemy can directly translate from object to row in a database
		db.session.add(self)
		db.session.commit()

	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()