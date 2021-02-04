import os
import sys
from flask import request
from flask_restful import Resource
import datetime
import jwt
from user_login_service import parse_token


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
        payload = {'username': username, "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=120)}
        jwt_key = os.getenv('JWT_SECRET_KEY')
        try:
            encoded_jwt = jwt.encode(payload, jwt_key, algorithm="HS256")
            return {'username': username, 'pwd': pwd, 'jwt': encoded_jwt}
        except jwt.exceptions.InvalidKeyError:
            return { 'rc': -1, 'msg': 'Invalid key'}
        except Exception as ex:
            return { 'rc': -9, 'msg': str(ex)}

