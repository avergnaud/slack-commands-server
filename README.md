# slack-commands-server

TODO
http://polyglot.ninja/jwt-authentication-python-flask/

## starttup
export LIST_SLACK_VERIF_TOKENS ="abc def"

curl -X POST -F 'text=0x123' -F 'user_id=U8XXXXXXN' -F 'user_name=mister-gros-bot' -F 'token=123' http://0.0.0.0:5001/users

http://localhost:5001/users?wallet_address=0x123

> db.users.find()
{ "_id" : ObjectId("5b2f6447b252c61fd65be9db"), "wallet" : [ "0x123" ], "slack_user_id" : [ "U8XXXXXXN" ], "slack_user_name" : [ "mister-gros-bot" ] }

curl -X POST -F 'text=0x123' -F 'user_id=U8XXXXXXN' -F 'user_name=mister-gros-bot' https://allstack.fr/slack-commands-server/users

https://allstack.fr/slack-commands-server/users?wallet_address=0x456
    
16^40 adresses = 2^160 = 1461501637330902918203684832716283019655932542976

