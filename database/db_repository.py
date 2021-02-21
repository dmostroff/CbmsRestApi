import pgsql_db_layer as db

def get_database_name():
    return db.get_database_name()

def get_version():
    return db.get_version()

def get_server_name():
    return db.get_server_name()

def get_connection_info():
    sql = """SELECT datid
    pid,
    datname,
    usename,
    application_name,
    backend_start,
    client_addr,
    client_hostname,
    client_port,
    query_start
FROM pg_stat_activity
WHERE pid = pg_backend_pid()
"""
    return db.fetchall(sql)