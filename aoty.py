from flask import Flask, jsonify
from flask_cors import CORS
from albumoftheyearapi import AOTY

app = Flask(__name__)
CORS(app, origins=["https://ma31n.github.io"])

@app.route("/user/<username>")
def get_user(username):
    client = AOTY()
    info = client.user_ratings_all(username, max_pages=None)
    return jsonify(info)



