import os
import sys
from flask import request
from flask_restful import Resource
import datetime
import jwt
from user_login_service import parse_token, login


jwt_key = 'junior'

class Login(Resource):
    def get(self):
        authToken = parse_token( request)
        if authToken is not None:
            try:
                jwt_key = os.getenv('JWT_SECRET_KEY')
                payload = jwt.decode(authToken, jwt_key, algorithms=["HS256"])
                exp = datetime.datetime.fromtimestamp( payload['exp'])
                expTime = exp.strftime( "%Y-%m-%d %H:%M:%S")
                return { 'rc': -1, 'msg': payload, 'exp': expTime}
            except jwt.ExpiredSignatureError:
                return { 'rc': -1, 'msg': 'Token expired'}
            except jwt.InvalidSignatureError:
                return { 'rc': -1, 'msg': 'Invalid Signature Error'}
        return { 'rc': -9, 'msg': 'No Authorization Token'}

    def post(self):
        username = request.form['username']
        pwd = request.form['pwd']
        try:
            user_login = login( username, pwd)
            return { 'rc': 0, 'msg': 'Login', 'data': user_login }
        except jwt.exceptions.InvalidKeyError:
            return { 'rc': -1, 'msg': 'Invalid key'}
        except Exception as ex:
            return { 'rc': -9, 'msg': str(ex)}
class Register(Resource):
    def post(self):
        username = request.form['username']
        pwd = request.form['pwd']
        try:
            user_login = register( username, pwd)
            return { 'rc': 0, 'msg': 'Login', 'data': user_login }
        except jwt.exceptions.InvalidKeyError:
            return { 'rc': -1, 'msg': 'Invalid key'}
        except Exception as ex:
            return { 'rc': -9, 'msg': str(ex)}

