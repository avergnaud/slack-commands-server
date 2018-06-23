from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/users', methods=['POST'])
def user():
    if request.method == 'POST':
        data = request.form  # a multidict containing POST data
        print(data)

        test_content = "commande bien reçue"

        return test_content, 200

def run():
    app.run(host='0.0.0.0', port=5001, debug=True)

if __name__ == '__main__':
    run()