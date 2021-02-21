import base_service as bs
import db_repository as dr

def get_database_name():
    return dr.get_database_name()

def get_version():
    return dr.get_version()

@bs.repository_call_single_row
def get_connection_info():
    return dr.get_connection_info()

def get_server_name():
    return dr.get_server_name()

