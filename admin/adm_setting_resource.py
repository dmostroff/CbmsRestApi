from flask import request
from flask_restful import Resource
import adm_setting_service as admserv
from admin_transform import AdmSettingJsonToModel


class AdmSettings(Resource):
    def get(self):
        return admserv.get_adm_settings()

class AdmSetting(Resource):
    def get(self, id):
        return admserv.get_adm_setting_by_id(id)

class AdmSettingPost(Resource):
    def post(self):
        adm_setting = AdmSettingJsonToModel(request.get_json())
        retval = admserv.upsert_adm_setting( adm_setting)
        return retval
