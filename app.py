import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'nieli9697'
api = Api(app)


jwt = JWT(app, authenticate, identity) # jwt creates an endpoint called "/auth"

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register') # when execute a post request to '/register', that's gonna call the UserRegister,
                                            # and that's going to call the post method under the UserRegister class

if __name__ == '__main__': 
	from db import db
	db.init_app(app)
	app.run(port=5000, debug=True)