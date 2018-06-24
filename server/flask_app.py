from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route('/users', methods=['POST'])
def user():
    if request.method == 'POST':
        data_b = request.data  # a multidict containing POST data
        data = data_b.decode('UTF-8')
        data_j = json.loads(data)
        print(data)
        print(data_j)

        test_content = "commande bien reçue, payload : " + data

        return test_content, 200

def run():
    app.run(host='0.0.0.0', port=5001, debug=True)

if __name__ == '__main__':
    run()