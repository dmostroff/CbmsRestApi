import datetime
import os
import jwt
import auth_user_service as aus
import user_login_repository as ulr
import base_service as bs
from admin_model import UserLoginModel, AuthUserModel

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

#--------------------
# user_login
#--------------------
def login( username, password):
    user = aus.authenticate_user( username, password)
    newUserLogin = None
    if user is not None:
        userLogin = UserLoginModel()
        userLogin.username = user.username
        userLogin.token = create_token( user.username)
        newUserLogin = ulr.upsert_user_login( userLogin)
    else:
        user = aus.get_auth_user_by_username(username)

    return {'username': username, 'user': user, 'user_login': newUserLogin}

def register( auth_user:AuthUserModel):
    user = aus.upsert_auth_user( auth_user)
    if user['rc'] == 1:
        return login( user['data']['username'], user['data']['password'])
    return user

@bs.repository_call
def get_user_logins():
    return ulr.get_user_logins()

@bs.repository_call
def upsert_user_login( username, jwt_token, ssuser_login:UserLoginModel):
    return ulr.upsert_user_login( user_login)

def authenticate_user( username, password):
    pass

@bs.repository_call
def get_auth_user( username, jwt_token, ssuser_login:UserLoginModel):
    return ulr.upsert_user_login( user_login)

