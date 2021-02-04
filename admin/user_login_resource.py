from flask import request
from flask_restful import Resource
import user_login_service as uls
from admin_model import UserLoginModel

class UserLogins(Resource):
    def get(self):
        return uls.get_user_logins()

class UserLogin(Resource):
    def get(self, username):
        return uls.get_user_login( username)

    def put(self):
        userLogin = UserLogin()
        userLogin.username = request.form['username']
        userLogin.token = request.headers
        newUserLogin = uls.upsert_user_login( userLogin)
        return {'user_login': newUserLogin}
