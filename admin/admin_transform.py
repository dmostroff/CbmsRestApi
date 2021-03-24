from admin_model import AuthRoleModel, AdmSettingModel
from admin_model import AuthUserModel, AuthUserSettingModel, UserLoginModel

def JsonToModel():
    pass

def AuthRoleJsonToModel( auth_role_json: str) -> AuthRoleModel:
    retval = AuthRoleModel.parse_obj( auth_role_json)
    return retval

def AdmSettingJsonToModel( adm_setting_json: str) -> AdmSettingModel:
    return AdmSettingModel.parse_obj( adm_setting_json)

def AuthUserJsonToModel( auth_user_json: str) -> AuthUserModel:
    return AuthUserModel.parse_obj( auth_user_json)

def AuthUserSettingJsonToModel( auth_user_setting_json: str) -> AuthUserSettingModel:
    return AuthUserSettingModel.parse_obj( auth_user_setting_json)

def UserLoginJsonToModel( user_login_json: str) -> UserLoginModel:
    return UserLoginModel.parse_obj( user_login_json)