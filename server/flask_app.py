from flask_cors import CORS
from flask import Flask
import server.users_routes
import server.auth_routes
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# conf flask. TODO restrict CORS
app = Flask(__name__)
CORS(app)

if not os.getenv("MONGO_DBNAME"):
    raise Exception('MONGO_DBNAME environment variable not set')

if not os.getenv('MONGO_URI'):
    raise Exception('MONGO_URI environment variable not set')

# conf mongo
app.config['MONGO_DBNAME'] = os.getenv('MONGO_DBNAME')
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo = PyMongo(app)

users_route = server.users_routes.construct_blueprint(app, mongo)
app.register_blueprint(users_route)

auth_routes = server.auth_routes.construct_blueprint(app, mongo)
app.register_blueprint(auth_routes)


def run():
    app.run(host='0.0.0.0', port=5001, debug=True)


if __name__ == '__main__':
    run()
