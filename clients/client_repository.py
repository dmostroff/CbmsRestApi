import pandas as pd
import os
import pgsql_db_layer as db

def get_clientpersons():
    sql = "SELECT * FROM client_person"
    return db.fetchall(sql)

def get_clientperson_by_id( id):
    sql = "SELECT * FROM client_person WHERE client_id = %s"
    return db.fetchall(sql, id)

def get_clientperson_by_last_name( last_name):
    sql = "SELECT * FROM client_person WHERE last_name = ?"
    return db.fetchall(sql, last_name)