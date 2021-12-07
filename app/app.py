from flask import Flask, jsonify, request
from flask_restful import Api, Resource

from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.aNewDB
UserNum = db["UserNum"]

UserNum.insert_one({
    "users": 0
})


class Visit(Resource):
    def get(self):
        prev_num: UserNum.find({})[0]["users"]
        new_num = prev_num + 1
        UserNum.insert({}, {"$set": {"users": new_num}})
        return str("Hello user " + str(new_num))


class Add(Resource):
    def post(self):
        postedData = request.get_json()
        dataE = {
            'Message': postedData,
            'Status Code': 200
        }
        return jsonify(dataE)


api.add_resource(Add, '/add')
api.add_resource(Visit, '/hello')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
