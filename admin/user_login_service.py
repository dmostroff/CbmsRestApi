from flask import request
import datetime
import os
import jwt
import json
import auth_user_service as aus
import user_login_repository as ulr
import base_service as bs
from admin_model import UserLoginModel, AuthUserModel
from admin_transform import AuthUserJsonToModel, UserLoginJsonToModel

def parse_token( request):
    authToken = None
    auth = request.headers.get( 'Authorization')
    if auth is not None and 'Bearer ' in auth:
        authToken = auth.split(' ')[1]
    return authToken

def create_token( username):
    jwt_token = None
    payload = {'username': username, "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=120)}
    jwt_key = os.getenv('JWT_SECRET_KEY')
    try:
        jwt_token = jwt.encode(payload, jwt_key, algorithm="HS256")
    except jwt.exceptions.InvalidKeyError:
        print( { 'rc': -1, 'msg': 'Invalid key'})
        raise jwt.exceptions.InvalidKeyError
    except Exception as ex:
        print( str(ex))
        raise ex
    finally:
        return jwt_token

def decrypt_token( auth_token ):
    jwt_token_decode = None
    jwt_key = os.getenv('JWT_SECRET_KEY')
    try:
        jwt_token_decode = jwt.decode(auth_token, jwt_key, algorithm="HS256")
    except jwt.exceptions.InvalidKeyError:
        print( { 'rc': -1, 'msg': 'Invalid key'})
        raise jwt.exceptions.InvalidKeyError
    except Exception as ex:
        print( str(ex))
        raise ex
    finally:
        return jwt_token_decode

#--------------------
# user_login
#--------------------
def login():
    content = request.get_json(silent=True)
    try:
        user_login = login_authenticate( content['username'], content['pwd'])
        if user_login['user'] is None:
            return { 'rc': 0, 'msg': 'Invalid Login', 'data': user_login }
        return { 'rc': 1, 'msg': 'Login successful', 'data': user_login }
    except jwt.exceptions.InvalidKeyError:
        return { 'rc': -1, 'msg': 'Invalid key'}
    except Exception as ex:
        return { 'rc': -9, 'msg': str(ex)}

def login_authenticate( username, password):
    user = aus.authenticate_user( username, password)
    newUserLogin = None
    if user is not None:
        jwt_token = create_token( user['username'])
        userLogin = UserLoginJsonToModel( { 'username': user['username'], 'token': jwt_token })
        newUserLogin = upsert_user_login( userLogin)
        user.pop('password', None)
    else:
        user = aus.get_auth_user_by_username(username)

    return { 'user': user, 'user_login': newUserLogin['data']}

def logout():
    auth_token = parse_token(request)
    jwt_token_decode = decrypt_token(auth_token)
    ulr.delete_user_login_by_username(jwt_token_decode['username'])
    return { 'rc': 0, 'msg': 'Logged out'}

def register():
    auth_user = AuthUserJsonToModel( request.get_json(silent=True))
    try:
        user_login = onboard_register( auth_user)
        return { 'rc': 0, 'msg': 'Login', 'data': user_login }
    except jwt.exceptions.InvalidKeyError:
        return { 'rc': -1, 'msg': 'Invalid key'}
    except Exception as ex:
        return { 'rc': -9, 'msg': str(ex)}

def onboard_register( auth_user:AuthUserModel):
    user = aus.upsert_auth_user( auth_user)
    if user['rc'] == 1:
        return login_authenticate( user['data']['username'], user['data']['password'])
    return user

@bs.repository_call_single_row
def get_user_login():
    pass

@bs.repository_call
def get_user_logins():
    return ulr.get_user_logins()

@bs.repository_call_single_row
def upsert_user_login( userLogin: UserLoginJsonToModel):
    return ulr.upsert_user_login( userLogin)

def authenticate_user( username, password):
    pass

@bs.repository_call
def get_auth_user( username, jwt_token, user_login:UserLoginModel):
    return ulr.upsert_user_login( user_login)

