from flask_restful import Resource
import auth_user_service as aus

authUserRole = {}
class AuthUserRoles(Resource):
    def get(self):
        return aus.get_auth_user_role()

class AuthUserRole(Resource):
    def get(self, id):
        return as.get_auth_user_role(id)

    def put(self, id):
        authUserRole[id] = request.form['authUserRole']
        return {'authUserRole_id': authUserRole[id]}