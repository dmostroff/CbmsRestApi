from flask import request
from flask_restful import Resource
import auth_user_service as aus
from admin_transform import AuthUserSettingJsonToModel


class AuthUserSetting(Resource):
    def get(self, id):
        return aus.get_auth_user_setting_by_id(id)

    def delete( self, id):
        return aus.delete_auth_user_setting(id)

class AuthUserSettingByPrefix(Resource):
    def get(self, user_id, prefix):
        return aus.get_auth_user_setting_by_prefix(user_id, prefix)

    def delete( self, user_id, prefix):
        return aus.delete_auth_user_setting_by_id(user_id, prefix)

class AuthUserSettingPost(Resource):
    def post(self):
        auth_user_setting = AuthUserSettingJsonToModel(request.get_json())
        retval = aus.upsert_auth_user_setting( auth_user_setting)
        return retval
