# slack-commands-server

requiert les variables d'environnement...
LIST_SLACK_VERIF_TOKENS, JWT_SECRET

TODO dans protected_route
http://polyglot.ninja/jwt-authentication-python-flask/

## starttup
### Installation des dépendances
$ pip install -r requirements.txt

$ cp .env.example .env
**Modifier les variables d'environnement du fichier .env**

$ python main.py

curl -X POST -F 'text=0x123' -F 'user_id=U8XXXXXXN' -F 'user_name=mister-gros-bot' -F 'token=123' http://0.0.0.0:5001/users
curl -X POST -F 'text=0xD2e42398E63A9C638444087B3d1E76c3Cf1508FA' -F 'user_id=U8XXXXXXN' -F 'user_name=mister-gros-bot' -F 'token=123' http://0.0.0.0:5001/users

http://localhost:5001/users?wallet_address=0x123

> db.users.find()
{ "_id" : ObjectId("5b2f6447b252c61fd65be9db"), "wallet" : [ "0x123" ], "slack_user_id" : [ "U8XXXXXXN" ], "slack_user_name" : [ "mister-gros-bot" ] }

curl -X POST -F 'text=0x123' -F 'user_id=U8XXXXXXN' -F 'user_name=mister-gros-bot' https://allstack.fr/slack-commands-server/users

https://allstack.fr/slack-commands-server/users?wallet_address=0x456
    
16^40 adresses = 2^160 = 1461501637330902918203684832716283019655932542976

# lecture

https://medium.com/vandium-software/5-easy-steps-to-understanding-json-web-tokens-jwt-1164c0adfcec
http://polyglot.ninja/understanding-jwt-json-web-tokens/
http://polyglot.ninja/jwt-authentication-python-flask/

attention à bien installer PyJWT
https://stackoverflow.com/questions/33198428/jwt-module-object-has-no-attribute-encode
