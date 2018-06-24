# slack-commands-server

curl -X POST -i -H "Content-Type:application/x-www-form-urlencoded" -d '{ "slackUser":"adrien", "wallet":"0x123" }' http://0.0.0.0:5001/users

curl -vX POST http://0.0.0.0:5001/users -d @/home/ubuntu/dev3/slack-commands-server/exemple.json --header "Content-Type:application/x-www-form-urlencoded"

curl -X POST -i -H "Content-Type:application/x-www-form-urlencoded" -d '{ "slackUser":"adrien", "wallet":"0x123" }' https://allstack.fr/slack-commands-server/users
