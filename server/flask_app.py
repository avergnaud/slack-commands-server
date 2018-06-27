from flask_cors import CORS
import json
from bson import json_util
from flask import request,Flask
from flask_pymongo import PyMongo
import os


# conf flask. TODO restrict CORS
app = Flask(__name__)
CORS(app)


# conf mongo
app.config['MONGO_DBNAME'] = 'slack-users-db'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/slack-users-db'
mongo = PyMongo(app)


# conf slack
if not os.environ.get("LIST_SLACK_VERIF_TOKENS"):
    raise Exception('LIST_SLACK_VERIF_TOKENS environment variable not set')
slack_verif_tokens = [i for i in os.environ.get("LIST_SLACK_VERIF_TOKENS").split(" ")]


@app.route('/users', methods=['POST'])
def add_user():
    # récupération des données
    data = request.form
    user_dict = data.to_dict(flat=False)
    # vérification du token slack (https://api.slack.com/slash-commands "Validating the command")
    secret_token = user_dict["token"][0]
    if secret_token not in slack_verif_tokens:
        return "error", 403
    # insert
    user_id = mongo.db.users.insert({"slack_user_id": user_dict["user_id"], "wallet_address": user_dict["text"],
                                     "slack_user_name": user_dict["user_name"]})
    new_user = mongo.db.users.find_one({'_id': user_id})
    # réponse
    retour = "user créé : " + json.dumps(new_user, default=json_util.default)
    return retour, 200


@app.route('/users', methods=['GET'])
def get_user_by_wallet():
    # récupération du wallet
    wallet_address = request.args.get('wallet_address')
    user = mongo.db.users.find_one({'wallet_address': wallet_address})
    if user is not None:
        return json.dumps(user, default=json_util.default), 200
    else:
        return "error", 403



def run():
    app.run(host='0.0.0.0', port=5001, debug=True)


if __name__ == '__main__':
    run()
