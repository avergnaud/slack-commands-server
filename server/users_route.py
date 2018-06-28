import json
from bson import json_util
from flask import request, Blueprint
import os
from random import randint


# conf slack
if not os.environ.get("LIST_SLACK_VERIF_TOKENS"):
    raise Exception('LIST_SLACK_VERIF_TOKENS environment variable not set')
slack_verif_tokens = [i for i in os.environ.get("LIST_SLACK_VERIF_TOKENS").split(" ")]


def construct_blueprint(app, mongo):

    users_route = Blueprint('users_route', __name__)

    @users_route.route('/users', methods=['POST'])
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

    @users_route.route('/users', methods=['GET'])
    def get_user_by_wallet():
        # récupération du wallet
        wallet_address = request.args.get('wallet_address')
        user = mongo.db.users.find_one({'wallet_address': wallet_address})
        nonce = randint(1000, 9999)
        mongo.db.users.update({"_id":user["_id"]}, {"$set": {"nonce": nonce}})
        if user is not None:
            return json.dumps({"nonce": nonce, "publicAddress": user["wallet_address"][0]}), 200
        else:
            return "error", 403

    return users_route

