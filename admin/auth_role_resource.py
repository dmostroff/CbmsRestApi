from flask_restful import Resource
import auth_role_service as ars

authRole = {}
class AuthRoles(Resource):
    def get(self):
        return ars.get_auth_roles()

class AuthRole(Resource):
    def get(self, id):
        return ars.get_auth_role(id)

    def put(self, id):
        authRole[id] = request.form['authRole']
        return {'authRole_id': authRole[id]}

class AuthPermissions(Resource):
    def get(self):
        return ars.get_auth_permissions()

class AuthPermission(Resource):
    def get(self, id):
        return ars.get_auth_permission(id)

    def put(self, id):
        authPermission[id] = request.form['authPermission']
        return {'authPermission_id': authPermission[id]}

class AuthRolePermissions(Resource):
    def get(self):
        return ars.get_auth_role_permissions()

class AuthRolePermission(Resource):
    def get(self, id):
        return ars.get_auth_role_permission(id)

    def put(self, id):
        authRolePermission[id] = request.form['authRolePermission']
        return {'authRolePermission_id': authRolePermission[id]}