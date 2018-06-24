# slack-commands-server

curl -X POST -F 'text=0x123' -F 'user_id=U8XXXXXXN' -F 'user_name=mister-gros-bot' http://0.0.0.0:5001/users

> db.users.find()
{ "_id" : ObjectId("5b2f6447b252c61fd65be9db"), "wallet" : [ "0x123" ], "slack_user_id" : [ "U8XXXXXXN" ], "slack_user_name" : [ "mister-gros-bot" ] }

curl -X POST -F 'text=0x123' -F 'user_id=U8XXXXXXN' -F 'user_name=mister-gros-bot' https://allstack.fr/slack-commands-server/users
