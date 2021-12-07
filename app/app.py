import os
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient, results

from dotenv import load_dotenv
from pathlib import Path

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


# Todo
# create a local mongodb container
# add environmental variables for testing and deployment
# create a replica mongodb set for

user = col.find({})

print(list(user))

# UserNum.insert_one({
#     "users": 0
# })


# class Get(Resource):
#     def get(self):
#         return "hey world!"


# class Visit(Resource):
#     def get(self):
#         prev_num: UserNum.find({})[0]["users"]
#         new_num = prev_num + 1
#         UserNum.insert({}, {"$set": {"users": new_num}})
#         return str("Hello user " + str(new_num))


# class Add(Resource):
#     def post(self):
#         postedData = request.get_json()
#         dataE = {
#             'Message': postedData,
#             'Status Code': 200
#         }
#         return jsonify(dataE)


# api.add_resource(Add, '/add')
# api.add_resource(Visit, '/hello')
# api.add_resource(Get, '/')


# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
