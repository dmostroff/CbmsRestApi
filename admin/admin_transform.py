from admin_model import AuthRoleModel, AdmSettingModel

def JsonToModel():
    pass

def AuthRoleJsonToModel( auth_role_json: str) -> AuthRoleModel:
    retval = AuthRoleModel.parse_obj( auth_role_json)
    return retval

def AdmSettingJsonToModel( adm_setting_json: str) -> AdmSettingModel:
    retval = AdmSettingModel.parse_obj( adm_setting_json)
    return retval

