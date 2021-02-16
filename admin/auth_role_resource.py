from flask import request
from flask_restful import Resource
import auth_role_service as ars
from admin_transform import AuthRoleJsonToModel

class AuthRoles(Resource):
    def get(self):
        return ars.get_auth_roles()

class AuthRole(Resource):
    def get(self, id):
        return ars.get_auth_role_by_id(id)

class AuthRolePost(Resource):
    def post(self):
        auth_role = AuthRoleJsonToModel(request.get_json())
        return ars.upsert_auth_role( auth_role)

class AuthPermissions(Resource):
    def get(self):
        return ars.get_auth_permissions()

class AuthPermission(Resource):
    def get(self, id):
        return ars.get_auth_permission(id)

class AuthPermissionPost(Resource):
    def post(self, id):
        authPermission[id] = request.form['authPermission']
        return {'authPermission_id': authPermission[id]}

class AuthRolePermissions(Resource):
    def get(self):
        return ars.get_auth_role_permissions()

class AuthRolePermission(Resource):
    def get(self, id):
        return ars.get_auth_role_permission(id)

class AuthRolePermissionPost(Resource):
    def post(self, id):
        authRolePermission[id] = request.form['authRolePermission']
        return {'authRolePermission_id': authRolePermission[id]}