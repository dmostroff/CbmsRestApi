import auth_role_repository as ar
import base_service as bs
from admin_model import AuthRoleModel
from admin_model import AuthPermissionModel
from admin_model import AuthRolePermissionModel

#--------------------
# auth_role
#--------------------

@bs.repository_call
def get_auth_roles ():
    return ar.get_auth_roles()

# @bs.repository_call
# def get_auth_role_by_auth_role_id (auth_role_id):
#     return ar.get_auth_role_by_auth_role_id(auth_role_id)

@bs.repository_call
def get_auth_role_by_id (id):
    return ar.get_auth_role_by_id(id)

@bs.repository_call
def upsert_auth_role ( auth_role:AuthRoleModel):
    return ar.upsert_auth_role(auth_role)

@bs.repository_call
def insert_auth_role (auth_role:AuthRoleModel):
    return ar.insert_auth_role(auth_role)

#--------------------
# auth_permission
#--------------------

@bs.repository_call
def get_auth_permissions ():
    return ar.get_auth_permissions()

# @bs.repository_call
# def get_auth_permission_by_auth_permission_id (auth_permission_id):
#     return ar.get_auth_permission_by_auth_permission_id(auth_permission_id)

@bs.repository_call
def get_auth_permission_by_id (id):
    return ar.get_auth_permission_by_id(id)

@bs.repository_call
def post_auth_permission ( auth_permission:AuthPermissionModel):
    return ar.upsert_auth_permission(auth_permission)

@bs.repository_call
def put_auth_permission (auth_permission:AuthPermissionModel):
    return ar.insert_auth_permission(auth_permission)

#--------------------
# auth_role_permission
#--------------------

@bs.repository_call
def get_auth_role_permissions ():
    return ar.get_auth_role_permissions()

# @bs.repository_call
# def get_auth_role_permission_by_auth_role_id (auth_role_id):
#     return ar.get_auth_role_permission_by_auth_role_id(auth_role_id)

@bs.repository_call
def get_auth_role_permission_by_id (id):
    return ar.get_auth_role_permission_by_id(id)

@bs.repository_call
def post_auth_role_permission ( auth_role_permission:AuthRolePermissionModel):
    return ar.upsert_auth_role_permission(auth_role_permission)

@bs.repository_call
def put_auth_role_permission (auth_role_permission:AuthRolePermissionModel):
    return ar.insert_auth_role_permission(auth_role_permission)
