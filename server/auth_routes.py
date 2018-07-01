from flask import Blueprint, request
from web3.auto import w3
from eth_account.messages import defunct_hash_message
import jwt
import datetime
import os
import json

if not os.environ.get("JWT_SECRET"):
    raise Exception('JWT_SECRET environment variable not set')
SECRET_KEY = os.environ.get("JWT_SECRET")

def construct_blueprint(app, mongo):

    auth_routes = Blueprint('auth_routes', __name__)

    @auth_routes.route('/auth', methods=['POST'])
    def auth():
        request_payload = request.get_json()

        claimed_address = request_payload["claimed_address"].lower()
        signed_message = request_payload["signed_message"]
        user = mongo.db.users.find_one({'wallet_address': claimed_address})
        original_message = "I am signing my one-time nonce: " + str(user["nonce"])

        message_hash = defunct_hash_message(text=original_message)
        recovered_address = w3.eth.account.recoverHash(message_hash, signature=signed_message)

        status = claimed_address == recovered_address.lower()

        if status:
            jwt_payload = {
                "address": claimed_address,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=2)
            }
            token = jwt.encode(payload=jwt_payload, key=SECRET_KEY)
            print("Generated Token: {}".format(token.decode()))
            return json.dumps({"token": token.decode()}), 200

        else:
            return "error", 403

    return auth_routes