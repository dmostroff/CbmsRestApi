from flask import request
from flask_restful import Resource
import user_login_service as uls
from admin_model import UserLoginModel

class UserLogins(Resource):
    def get(self):
        funcs = {
            'logins': uls.get_user_logins,
            'users': uls.get_users
        }
        if name in funcs:
            return {name: funcs[name]() }, 200
        return None, 404

class UserLogin(Resource):
    def get(self, username):
        return uls.get_user_login( username)

    def post(self, name):
        funcs = {
            'login': uls.login,
            'logout': uls.logout,
            'register': uls.register,
            'user': uls.get_user_login
        }
        if name in funcs:
            return {name: funcs[name]() }, 200
        return None, 404

    def put(self):
        userLogin = UserLogin()
        userLogin.username = request.form['username']
        userLogin.token = request.headers
        newUserLogin = uls.upsert_user_login( userLogin)
        return {'user_login': newUserLogin}
