import os
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient, results

from dotenv import load_dotenv

app = Flask(__name__)
api = Api(app)

load_dotenv()

DB_USER = os.getenv('MONGO_USER')
DB_PASSWORD = os.getenv('MONGO_PASSWORD')
DB_IP = os.getenv('MONGO_IP')
DB_PORT = os.getenv('MONGO_PORT')

url = f'mongodb://{DB_USER}:{DB_PASSWORD}@{DB_IP}:{DB_PORT}'
client = MongoClient(url)
db = client["nft-ums"]
col = db["user"]


# # Todo
# environmental variables to work on EC2
# create a replica mongodb set for production


@app.route('/', methods=['GET'])
def add():
    user = col.find({})
    value = list(user)
    return f'Hello World from mongo 0.2: {value}'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
