from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route('/users', methods=['POST'])
def user():
    if request.method == 'POST':
        data = request.form  # a multidict containing POST data

        form_dict = data.to_dict(flat=False)
        print(form_dict)

        test_content = "commande bien reçue, payload : " + str(form_dict)

        return test_content, 200

def run():
    app.run(host='0.0.0.0', port=5001, debug=True)

if __name__ == '__main__':
    run()