import os
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin
from pymongo import MongoClient, results
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app, support_credentials=True)

api = Api(app)
load_dotenv()

DB_USER = os.getenv("MONGO_USER")
DB_PASSWORD = os.getenv("MONGO_PASSWORD")
DB_IP = os.getenv("MONGO_IP")

url = f"mongodb://{DB_USER}:{DB_PASSWORD}@{DB_IP}:27017"
client = MongoClient(url)
db = client["nft-ums"]
col = db["user"]


# Todo
# create a replica mongodb set for production


class Visit(Resource):
    def get(self):
        user = col.find({})
        value = list(user)
        return f"Hello World: {value}"


api.add_resource(Visit, "/")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
