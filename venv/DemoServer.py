from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok
from PIL import Image

app = Flask(__name__)
run_with_ngrok(app)


@app.route('/', methods=['GET', 'POST', 'PUT'])
@app.route('/hello', methods=['GET', 'POST', 'PUT'])
def hello():
    if request.form["id"] == "1":
        data = ["Hello", 10, "yo"]
    else:
        data = "Hello"
    return jsonify(data)

app.run()