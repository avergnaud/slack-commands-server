from flask_cors import CORS
from flask import Flask
import server.users_routes
import server.auth_routes
from flask_pymongo import PyMongo


# conf flask. TODO restrict CORS
app = Flask(__name__)
CORS(app)


# conf mongo
app.config['MONGO_DBNAME'] = 'slack-users-db'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/slack-users-db'
mongo = PyMongo(app)


users_route = server.users_routes.construct_blueprint(app, mongo)
app.register_blueprint(users_route)

auth_routes = server.auth_routes.construct_blueprint(app, mongo)
app.register_blueprint(auth_routes)


def run():
    app.run(host='0.0.0.0', port=5001, debug=True)


if __name__ == '__main__':
    run()
