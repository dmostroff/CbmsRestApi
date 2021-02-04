from admin_model import AuthUserModel, AuthUserRoleModel, AuthUserGroupModel
import pgsql_db_layer as db

#######################
# auth_user
#######################
def get_auth_user_basesql():
    sql = """
    SELECT au.id,password,last_login,is_superuser,username,first_name,last_name,email,is_staff,is_active,date_joined, aur.role
    FROM admin.auth_user au
        LEFT OUTER JOIN admin.auth_user_role aur ON aur.user_id = au.id
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


def get_auth_user_by_auth_user_id(auth_user_id):
    sql = get_auth_user_basesql()
    sql += """
    WHERE auth_user_id = %s
"""
    return db.fetchall(sql, [auth_user_id])


def upsert_auth_user(auth_user: AuthUserModel):
    sql = """
    WITH t AS (
        SELECT 
            %s as id
            , %s as password
            , %s as last_login
            , %s as is_superuser
            , %s as username
            , %s as first_name
            , %s as last_name
            , %s as email
            , %s as is_staff
            , %s as is_active
            , %s as date_joined
    ),
    u AS (
        UPDATE admin.auth_user
        SET 
            password=t.password
            , last_login=t.last_login
            , is_superuser=t.is_superuser
            , username=t.username
            , first_name=t.first_name
            , last_name=t.last_name
            , email=t.email
            , is_staff=t.is_staff
            , is_active=t.is_active
            , date_joined=t.date_joined
        FROM t
        WHERE auth_user.id = t.id
        RETURNING id
    ),
    i AS (
        INSERT INTO admin.auth_user( password,last_login,is_superuser,username,first_name,last_name,email,is_staff,is_active,date_joined)
        SELECT 
            t.password
            , t.last_login
            , t.is_superuser
            , t.username
            , t.first_name
            , t.last_name
            , t.email
            , t.is_staff
            , t.is_active
            , t.date_joined
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
        auth_user.id, auth_user.password, auth_user.last_login, auth_user.is_superuser, auth_user.username, auth_user.first_name, auth_user.last_name, auth_user.email, auth_user.is_staff, auth_user.is_active, auth_user.date_joined
    ]
    return db.execute(sql, val)


def insert_auth_user(auth_user: AuthUserModel):
    sql = """
    INSERT INTO admin.auth_user( password,last_login,is_superuser,username,first_name,last_name,email,is_staff,is_active,date_joined)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ;
"""
    val = [
        auth_user.password, auth_user.last_login, auth_user.is_superuser, auth_user.username, auth_user.first_name, auth_user.last_name, auth_user.email, auth_user.is_staff, auth_user.is_active, auth_user.date_joined
    ]
    return db.execute(sql, val)

# this has a flaw in loop.index > 2


def update_auth_user(auth_user: AuthUserModel):
    sql = """
    UPDATE admin.auth_user
    SET password = %s, last_login = %s, is_superuser = %s, username = %s, first_name = %s, last_name = %s, email = %s, is_staff = %s, is_active = %s, date_joined = %s
    WHERE id = %s
"""
    val = [
        auth_user.password, auth_user.last_login, auth_user.is_superuser, auth_user.username, auth_user.first_name, auth_user.last_name, auth_user.email, auth_user.is_staff, auth_user.is_active, auth_user.date_joined, auth_user.id
    ]
    return db.execute(sql, val)


#######################
# auth_user_group
#######################
def get_auth_user_group_basesql():
    sql = """
    SELECT id,user_id,group_id
    FROM admin.auth_user_group
"""
    return sql


def get_auth_user_group():
    sql = get_auth_user_group_basesql()
    return db.fetchall(sql)


def get_auth_user_group_by_id(id):
    sql = get_auth_user_group_basesql()
    sql += """
    WHERE id = %s
"""
    return db.fetchall(sql, [id])


def get_auth_user_group_by_user_id(user_id):
    sql = get_auth_user_group_basesql()
    sql += """
    WHERE user_id = %s
"""
    return db.fetchall(sql, [user_id])


def upsert_auth_user_group(auth_user_group: AuthUserGroupModel):
    sql = """
    WITH t AS (
        SELECT 
            %s as id
            , %s as user_id
            , %s as group_id
    ),
    u AS (
        UPDATE admin.auth_user_group
        SET 
            user_id=t.user_id
            , group_id=t.group_id
        FROM t
        WHERE auth_user_group.id = t.id
        RETURNING id
    ),
    i AS (
        INSERT INTO admin.auth_user_group( user_id,group_id)
        SELECT 
            t.user_id
            , t.group_id
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
        auth_user_group.id, auth_user_group.user_id, auth_user_group.group_id
    ]
    return db.execute(sql, val)


def insert_auth_user_group(auth_user_group: AuthUserGroupModel):
    sql = """
    INSERT INTO admin.auth_user_group( user_id,group_id)
    VALUES (%s, %s)
    ;
"""
    val = [
        auth_user_group.user_id, auth_user_group.group_id
    ]
    return db.execute(sql, val)

# this has a flaw in loop.index > 2


def update_auth_user_group(auth_user_group: AuthUserGroupModel):
    sql = """
    UPDATE admin.auth_user_group
    SET user_id = %s, group_id = %s
    WHERE id = %s
"""
    val = [
        auth_user_group.user_id, auth_user_group.group_id, auth_user_group.id
    ]
    return db.execute(sql, val)


#######################
# auth_user_role
#######################
def get_auth_user_role_basesql():
    sql = """
    SELECT id,user_id,role
    FROM admin.auth_user_role
"""
    return sql


def get_auth_user_roles():
    sql = get_auth_user_role_basesql()
    return db.fetchall(sql)


def get_auth_user_role_by_id(id):
    sql = get_auth_user_role_basesql()
    sql += """
    WHERE id = %s
"""
    return db.fetchall(sql, [id])


def upsert_auth_user_role(auth_user_role: AuthUserRoleModel):
    sql = """
    WITH t AS (
        SELECT 
            %s as id
            , %s as user_id
            , %s as role
    ),
    u AS (
        UPDATE admin.auth_user_role
        SET 
            user_id=t.user_id
            , role=t.role
        FROM t
        WHERE auth_user_role.id = t.id
        RETURNING id
    ),
    i AS (
        INSERT INTO admin.auth_user_role( user_id,role)
        SELECT 
            t.user_id
            , t.role
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
        auth_user_role.id, auth_user_role.user_id, auth_user_role.role
    ]
    return db.execute(sql, val)


def insert_auth_user_role(auth_user_role: AuthUserRoleModel):
    sql = """
    INSERT INTO admin.auth_user_role( user_id,role)
    VALUES (%s, %s)
    ;
"""
    val = [
        auth_user_role.user_id, auth_user_role.role
    ]
    return db.execute(sql, val)

# this has a flaw in loop.index > 2


def update_auth_user_role(auth_user_role: AuthUserRoleModel):
    sql = """
    UPDATE admin.auth_user_role
    SET user_id = %s, role = %s
    WHERE id = %s
"""
    val = [
        auth_user_role.user_id, auth_user_role.role, auth_user_role.id
    ]
    return db.execute(sql, val)
