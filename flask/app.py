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

PORT = os.getenv('FLASK_PORT','80')

def abort_if_user_doesnt_exist(USER_id):
    if USER_id not in USERS:
        abort(404, message="USER {} doesn't exist".format(USER_id))

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True,help="Name cannot be blank!")
parser.add_argument('job_title', type=str)
parser.add_argument('email', type=str)
parser.add_argument('mobile', type=str)

class User(Resource):
    def get(self, USER_id):
        abort_if_user_doesnt_exist(USER_id)
        resp=USERS[USER_id]
        respond=jsonify(resp)
        respond.status_code=200
        return respond
        # return USERS[USER_id], 200

    def delete(self, USER_id):
        abort_if_user_doesnt_exist(USER_id)
        user_num=USERS[USER_id]
        del USERS[USER_id]
        # return '', 204
        # resp=USERS[USER_id]
        # respond=jsonify(resp)
        # respond.status_code=204
        return "User has been deleted",204

    def put(self, USER_id):
        abort_if_user_doesnt_exist(USER_id)
        args = parser.parse_args()
        user = {
            USER_id:{
            'name': args['name'],
            'job_title': args['job_title'],
            'communicate_information':{
               'email':  args['email'],
               'mobile': args['mobile']
                }
                    }
        }
        USERS.update(user)
        respond= jsonify(user)
        respond.status_code=201
        print(respond)
        return respond
        #name = {"name": args["name"]}
        #USERS[USER_id] = name
        #return USERS[USER_id], 201

class UserList(Resource):
    def get(self):
        # respond=jsonify(USERS)
        # respond.status_code=200        
        return USERS, 200

    def post(self):
        args = parser.parse_args()
        USER_id = int(max(USERS.keys()).lstrip('user')) + 1
        USER_id = 'user%i' % USER_id
        user = {
            USER_id:{
            'name': args['name'],
            'job_title': args['job_title'],
            'communicate_information':{
               'email':  args['email'],
               'mobile': args['mobile']
                }
                    }
        }
        USERS.update(user)
        respond= jsonify(user)
        respond.status_code=201
        print(respond)
        return respond
        # return USERS[USER_id], "USER {} has been created or updated".format(USER_id)

api.add_resource(UserList, '/users', '/users/')
api.add_resource(User, '/users/<USER_id>', '/users/<USER_id>/')

# @app.route('/')
# def hello_world():
#     return 'Flask Dockerized'

# @app.route("/get_user")
# def get_user():

#     return jsonify(

#     )


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=PORT)