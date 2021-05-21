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
            %s::varchar(32) as username
            , %s::varchar(128) as token
    ),
    u AS (
        UPDATE admin.user_login
        SET 
            username=t.username
            , token=t.token
            , exp_date=now()+INTERVAL '5 hour'
        FROM t
        WHERE user_login.username = t.username
        RETURNING user_login.id, user_login.username, user_login.token, user_login.exp_date
    ),
    i AS (
        INSERT INTO admin.user_login( username, token, exp_date)
        SELECT 
            t.username
            , t.token
            , CURRENT_TIMESTAMP
        FROM t
        WHERE NOT EXISTS ( SELECT 1 FROM u)
        RETURNING user_login.id, user_login.username, user_login.token, user_login.exp_date
    )
    SELECT 'INSERT' as ACTION, i.id, i.username, i.token, i.exp_date
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, u.id, u.username, u.token, u.exp_date
    FROM u
    ;
"""
    val = [
            user_login.username
            , user_login.token
        ]
    return db.fetchall(sql, val)

def delete_user_login_by_username(username):
    sql = "DELETE FROM admin.user_login WHERE username = %s"
    return db.execute(sql, [username])

