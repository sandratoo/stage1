
from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/get", methods=["GET"])
def get_all():
    all = jsonify({
        "slackUsername": "sandratoo", 
        "backend": True,
        "age": 28,
        "bio": "Hi, my name sandra, a curious and self-startind developer."
    })
    
    return all