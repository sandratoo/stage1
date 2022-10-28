from flask import Flask,jsonify
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)

class getall(Resource):
    def get(self):
        all = jsonify({
            "slackUsername": "sandratoo", 
            "backend": True,
            "age": 28,
            "bio": "Hi, my name sandra, a curious and self-starting developer."
        })
        
        return all

api.add_resource(getall,"/get")

if __name__ == "__main__":
    app.run()