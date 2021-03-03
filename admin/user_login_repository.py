import pgsql_db_layer as db
from admin_model import UserLoginModel

def get_user_login_base_sql():
    sql = """
    SELECT
	    id,
	    username,
	    token,
	    exp_date,
	    recorded_on,
	FROM admin.user_login
"""
    return sql

def get_user_logins():
    sql = get_user_login_base_sql()
    return db.fetchall(sql)

def get_user_login_by_id(id):
    sql = get_user_login_base_sql()
    sql += """
    WHERE id = %s
    ;
"""
    return db.fetchall(sql, [id])

def get_user_login_by_username(username):
    sql = get_user_login_base_sql()
    sql += """
    WHERE username = %s
    ;
"""
    return db.fetchall(sql, [id])

def upsert_user_login( user_login:UserLoginModel):
    sql = """
    WITH t AS (
        SELECT 
            %s as id
            , %s as username
            , %s as token
            , %s as exp_date
    ),
    u AS (
        UPDATE user_login
        SET 
            username=t.username
            , first_name=t.first_name
            , token=t.token
            , exp_date=t.exp_date
        FROM t
        WHERE user_login.id = t.id
        RETURNING id
    ),
    i AS (
        INSERT INTO user_login( username, token, exp_date)
        SELECT 
            t.username
            , t.token
            , t.exp_date
        FROM t
        WHERE NOT EXISTS ( SELECT 1 FROM u)
    )
    SELECT 'INSERT' as ACTION, id
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, id
    FROM u
    ;
"""
    val = [
            user_login.id
            , user_login.username
            , user_login.token
            , user_login.exp_date
        ]
    return db.execute(sql, val)

def delete_user_login_by_username(username):
    sql = "DELETE FROM admin.user_login WHERE username = %s"
    return db.execute(sql, [username])

