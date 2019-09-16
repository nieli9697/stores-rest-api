from db import db

class ItemModel(db.Model):
	__tablename__ = 'items'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	price = db.Column(db.Float(precision=2))

	store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
	store = db.relationship('StoreModel')

	def __init__(self, name, price, store_id):
		self.name = name
		self.price = price
		self.store_id = store_id

	def json(self):
		return {'name': self.name, 'price': self.price}

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