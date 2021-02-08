import pgsql_db_layer as db
from admin_model import AdminUserModel


#######################
# auth_user
#######################
def get_auth_user_basesql():
    sql = """
    SELECT id,username,password,first_name,last_name,email,is_superuser,is_staff,is_active,password_hint,roles,created_at
    FROM auth_user
"""
    return sql

def authenticate_user( username, pwd):
    sql = get_auth_user_basesql()
    sql += """
    WHERE username = %s, password = crpyt( %s, password)
"""
    return db.fetchall(sql, [username, pwd])

def get_auth_users():
    sql = get_auth_user_basesql()
    return db.fetchall(sql)

def get_auth_user_by_id(id):
    sql = get_auth_user_basesql()
    sql += """
    WHERE id = %s
"""
    return db.fetchall(sql, [id])

# def get_auth_user_by_auth_user_id(auth_user_id):
#     sql = get_auth_user_basesql()
#     sql += """
#     WHERE auth_user_id = %s
# """
#     return db.fetchall(sql, [auth_user_id])

def upsert_auth_user( auth_user:AuthUserModel):
    sql = """
    WITH t AS (
        SELECT 
            %s as id
            , %s as username
            , %s as password
            , %s as first_name
            , %s as last_name
            , %s as email
            , %s as is_superuser
            , %s as is_staff
            , %s as is_active
            , %s as password_hint
            , %s as roles
    ),
    u AS (
        UPDATE auth_user
        SET 
            username=t.username
            , password=t.password
            , first_name=t.first_name
            , last_name=t.last_name
            , email=t.email
            , is_superuser=t.is_superuser
            , is_staff=t.is_staff
            , is_active=t.is_active
            , password_hint=t.password_hint
            , roles=t.roles
        FROM t
        WHERE auth_user.id = t.id
        RETURNING id
    ),
    i AS (
        INSERT INTO auth_user( username,password,first_name,last_name,email,is_superuser,is_staff,is_active,password_hint,roles)
        SELECT 
            t.username
            , t.password
            , t.first_name
            , t.last_name
            , t.email
            , t.is_superuser
            , t.is_staff
            , t.is_active
            , t.password_hint
            , t.roles
        FROM t
        WHERE NOT EXISTS ( SELECT 1 FROM u)
    )
    SELECT 'INSERT' as ACTION, id
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, id
    FROM u
    ;
    ;
"""
    val = [
            auth_user.id
            , auth_user.username
            , auth_user.password
            , auth_user.first_name
            , auth_user.last_name
            , auth_user.email
            , auth_user.is_superuser
            , auth_user.is_staff
            , auth_user.is_active
            , auth_user.password_hint
            , auth_user.roles
        ]
    return db.execute(sql, val)

def insert_auth_user( auth_user:AuthUserModel):
    sql = """
    INSERT INTO auth_user( username,password,first_name,last_name,email,is_superuser,is_staff,is_active,password_hint,roles)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ;
"""
    val = [
            auth_user.username
            , auth_user.password
            , auth_user.first_name
            , auth_user.last_name
            , auth_user.email
            , auth_user.is_superuser
            , auth_user.is_staff
            , auth_user.is_active
            , auth_user.password_hint
            , auth_user.roles
        ]
    return db.execute(sql, val)

# this has a flaw in loop.index > 2
def update_auth_user( auth_user:AuthUserModel):
    sql = """
    UPDATE auth_user
    SET username = %s, password = %s, first_name = %s, last_name = %s, email = %s, is_superuser = %s, is_staff = %s, is_active = %s, password_hint = %s, roles = %s
    WHERE id = %s
"""
    val = [auth_user.username
            , auth_user.password
            , auth_user.first_name
            , auth_user.last_name
            , auth_user.email
            , auth_user.is_superuser
            , auth_user.is_staff
            , auth_user.is_active
            , auth_user.password_hint
            , auth_user.roles
            , auth_user.id
        ]
    return db.execute(sql, val)
