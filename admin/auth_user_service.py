import auth_user_repository as aur
import base_service as bs
from admin_model import AuthUserModel
from admin_model import AuthUserGroupModel
from admin_model import AuthUserRoleModel

#--------------------
# auth_user
#--------------------

@bs.repository_call
def get_auth_users ():
    return aur.get_auth_users()

@bs.repository_call
def get_auth_user_by_id (id):
    return aur.get_auth_user_by_id(id)

@bs.repository_call
def post_auth_user ( auth_user:AuthUserModel):
    return aur.upsert_auth_user(auth_user)

@bs.repository_call
def put_auth_user (auth_user:AuthUserModel):
    return aur.insert_auth_user(auth_user)


#--------------------
# auth_user_group
#--------------------

@bs.repository_call
def get_auth_user_groups ():
    return aur.get_auth_user_groups()

@bs.repository_call
def get_auth_user_group_by_id (id):
    return aur.get_auth_user_group_by_id(id)

@bs.repository_call
def post_auth_user_group ( auth_user_group:AuthUserGroupModel):
    return aur.upsert_auth_user_group(auth_user_group)

@bs.repository_call
def put_auth_user_group (auth_user_group:AuthUserGroupModel):
    return aur.insert_auth_user_group(auth_user_group)


#--------------------
# auth_user_role
#--------------------

@bs.repository_call
def get_auth_user_roles ():
    return aur.get_auth_user_roles()

@bs.repository_call
def get_auth_user_role_by_auth_user_id (auth_user_id):
    return aur.get_auth_user_role_by_auth_user_id(auth_user_id)

@bs.repository_call
def get_auth_user_role_by_id (id):
    return aur.get_auth_user_role_by_id(id)

@bs.repository_call
def post_auth_user_role ( auth_user_role:AuthUserRoleModel):
    return aur.upsert_auth_user_role(auth_user_role)

@bs.repository_call
def put_auth_user_role (auth_user_role:AuthUserRoleModel):
    return aur.insert_auth_user_role(auth_user_role)

