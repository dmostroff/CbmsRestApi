import numpy as np
import adm_setting_repository as ar
import base_service as bs

#--------------------
# adm_setting
#--------------------
from admin_model import AdmSettingModel

@bs.repository_call
def get_adm_settings ():
    return ar.get_adm_settings()

@bs.repository_call
def get_adm_setting_by_prefix (prefix):
    return ar.get_adm_setting_by_prefix(prefix)

@bs.repository_call_single_row
def get_adm_setting_by_id (id):
    return ar.get_adm_setting_by_id(id)

# @bs.repository_call
def upsert_adm_setting ( adm_setting:AdmSettingModel):
    df = ar.upsert_adm_setting(adm_setting)
    id = np.int64(df['adm_setting_id'].values[0]).item()
    return get_adm_setting_by_id(id)


@bs.repository_call
def put_adm_setting (adm_setting:AdmSettingModel):
    return ar.insert_adm_setting(adm_setting)

