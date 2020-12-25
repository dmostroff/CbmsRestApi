import pgsql_db_layer as db

def get_database_name():
    return db.get_database_name()

def get_version():
    return db.get_version()