import os
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin
from pymongo import MongoClient, results
from dotenv import load_dotenv

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

load_dotenv()

DB_USER = os.getenv("MONGO_INITDB_ROOT_USERNAME")
DB_PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD")

# url = f"mongodb://{DB_USER}:{DB_PASSWORD}@{DB_IP}:27017"
url = f"mongodb://{DB_USER}:{DB_PASSWORD}@mongo:27017"
client = MongoClient(url)
db = client["UMS"]
col = db["user"]


# Todo
# create a replica mongodb set for production
# improve CORS allow


class Visit(Resource):
    def get(self):
        user = col.find({})
        value = list(user)
        return f"Hello World: {value}", 200, {"Access-Control-Allow-Origin": "*"}


class Add(Resource):
    def post(self):
        user = col.insert_one({"name": "daniel"})
        return f"Added {user}", 200, {"Access-Control-Allow-Origin": "*"}


api.add_resource(Visit, "/")
api.add_resource(Add, "/add")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
