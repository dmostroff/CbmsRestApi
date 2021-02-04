import user_login_repository as ulr
import base_service as bs
from admin_model import UserLoginModel

def parse_token( request):
    authToken = None
    auth = request.headers.get( 'Authorization')
    if auth is not None and 'Bearer ' in auth:
        authToken = auth.split(' ')[1]
    return authToken
#--------------------
# user_login
#--------------------
@bs.repository_call
def get_user_logins():
    return ulr.get_user_logins()

@bs.repository_call
def upsert_user_login( username, jwt_token, user_login:UserLoginModel):
    return ulr.upsert_user_login( user_login)

