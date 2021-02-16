import numpy as np
import auth_user_repository as ar
import base_service as bs
from admin_model import AuthUserModel

#--------------------
# auth_user
#--------------------

@bs.repository_call
def get_auth_users ():
    return ar.get_auth_users()

# @bs.repository_call
# def get_auth_user_by_auth_user_id (auth_user_id):
#     return ar.get_auth_user_by_auth_user_id(auth_user_id)

@bs.repository_call_single_row
def get_auth_user_by_id (id):
    return ar.get_auth_user_by_id(id)

def upsert_auth_user ( auth_user:AuthUserModel):
    df = ar.upsert_auth_user(auth_user)
    id = np.int64(df['id'].values[0]).item()
    return get_auth_user_by_id(id)

