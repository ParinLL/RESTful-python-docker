from flask import Flask,jsonify,request
from flask_restful import Resource, Api,abort,reqparse
import os

app = Flask(__name__)
api = Api(app)

USERS = {
    "user1": {"name": "John Lee",
              "job_title": "SRE",
              "communicate_information": {
                "email": "jhon.lee@testmail.com",
                "mobile": "09xx-xxx-xxx"
                }
            }
}

PORT = os.getenv('FLASK_PORT','8080')

def abort_if_user_doesnt_exist(USER_id):
    if USER_id not in USERS:
        abort(404, message="USER {} doesn't exist".format(USER_id))

parser = reqparse.RequestParser()
parser.add_argument('name')

class User(Resource):
    def get(self, USER_id):
        abort_if_user_doesnt_exist(USER_id)
        return USERS[USER_id]

    def delete(self, USER_id):
        abort_if_user_doesnt_exist(USER_id)
        del USERS[USER_id]
        return '', 204

    def put(self, USER_id):
        args = parser.parse_args()
        name = {"name": args["name"]}
        USERS[USER_id] = name
        return name, 201

class UserList(Resource):
    def get(self):
        return USERS

    def post(self):
        args = parser.parse_args()
        USER_id = int(max(USERS.keys()).lstrip('user')) + 1
        USER_id = 'user%i' % USER_id
        USERS[USER_id] = {'name': args['name']}
        return USERS[USER_id], 201

api.add_resource(UserList, '/users', '/users/')
api.add_resource(User, '/users/<USER_id>')

# @app.route('/')
# def hello_world():
#     return 'Flask Dockerized'

# @app.route("/get_user")
# def get_user():

#     return jsonify(

#     )


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=PORT)