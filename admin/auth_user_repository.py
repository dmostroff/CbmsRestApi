import pgsql_db_layer as db


#######################
# auth_user
#######################
from admin_model import AuthUserModel

def get_auth_user_basesql():
    sql = """
    SELECT id,username,password,first_name,last_name,email,is_superuser,is_staff,is_active,password_hint,roles,created_at
    FROM auth_user
"""
    return sql

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
            %s::integer as id
            , %s::character varying as username
            , %s::character varying as password
            , %s::character varying as first_name
            , %s::character varying as last_name
            , %s::character varying as email
            , %s::boolean as is_superuser
            , %s::boolean as is_staff
            , %s::boolean as is_active
            , %s::character varying as password_hint
            , %s::ARRAY as roles
            , %s::timestamp with time zone as created_at
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
            , created_at=t.created_at
        FROM t
        WHERE (auth_user.id = t.id) OR ( auth_user.username = t.username)
        RETURNING auth_user.id
    ),
    i AS (
        INSERT INTO auth_user( username,password,first_name,last_name,email,is_superuser,is_staff,is_active,password_hint,roles,created_at)
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
            , t.created_at
        FROM t
        WHERE NOT EXISTS ( SELECT 1 FROM u)
        RETURNING auth_user.id
    )
    SELECT 'INSERT' as ACTION, id
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, id
    FROM u
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
            , auth_user.created_at
        ]
    return db.fetchall(sql, val)

def insert_auth_user( auth_user:AuthUserModel):
    sql = """
    INSERT INTO auth_user( username,password,first_name,last_name,email,is_superuser,is_staff,is_active,password_hint,roles,created_at)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    RETURNING *
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
            , auth_user.created_at
        ]
    return db.fetchone(sql, val)

# this has a flaw in loop.index > 2
def update_auth_user( auth_user:AuthUserModel):
    sql = """
    UPDATE auth_user
    SET username = %s, password = %s, first_name = %s, last_name = %s, email = %s, is_superuser = %s, is_staff = %s, is_active = %s, password_hint = %s, roles = %s, created_at = %s
    WHERE id = %s
    RETURNING *
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
            , auth_user.created_at
        , auth_user.id            
        ]
    return db.fetchone(sql, val)
