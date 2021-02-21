from admin_model import AuthRoleModel, AdmSettingModel, AuthUserModel, UserLoginModel

def JsonToModel():
    pass

def AuthRoleJsonToModel( auth_role_json: str) -> AuthRoleModel:
    retval = AuthRoleModel.parse_obj( auth_role_json)
    return retval

def AdmSettingJsonToModel( adm_setting_json: str) -> AdmSettingModel:
    retval = AdmSettingModel.parse_obj( adm_setting_json)
    return retval

def AuthUserJsonToModel( auth_user_json: str) -> AuthUserModel:
    retval = AuthUserModel.parse_obj( auth_user_json)
    return retval

def UserLoginJsonToModel( user_login_json: str) -> UserLoginModel:
    return UserLoginModel.parse_obj( user_login_json)