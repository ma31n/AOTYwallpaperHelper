from flask import Flask, jsonify
from albumoftheyearapi import AOTY

app = Flask(__name__)

@app.route("/user/<username>")
def get_user(username):
    client = AOTY()
    info = client.user_ratings_all(username, max_pages=None)
    return jsonify(info)


