import pgsql_db_layer as db
from admin_model import AuthRolePermissionModel
from admin_model import AuthRoleModel


#######################
# auth_role_permission
#######################

def get_auth_role_permission_basesql():
    sql = """
    SELECT id,role,permission
    FROM auth_role_permission
"""
    return sql

def get_auth_role_permissions():
    sql = get_auth_role_permission_basesql()
    return db.fetchall(sql)

def get_auth_role_permission_by_id(id):
    sql = get_auth_role_permission_basesql()
    sql += """
    WHERE id = %s
"""
    return db.fetchall(sql, [id])

# def get_auth_role_permission_by_auth_role_id(auth_role_id):
#     sql = get_auth_role_permission_basesql()
#     sql += """
#     WHERE auth_role_id = %s
# """
#     return db.fetchall(sql, [auth_role_id])

def upsert_auth_role_permission( auth_role_permission:AuthRolePermissionModel):
    sql = """
    WITH t AS (
        SELECT 
            %s as id
            , %s as role
            , %s as permission
    ),
    u AS (
        UPDATE auth_role_permission
        SET 
            role=t.role
            , permission=t.permission
        FROM t
        WHERE auth_role_permission.id = t.id
        RETURNING id
    ),
    i AS (
        INSERT INTO auth_role_permission( role,permission)
        SELECT 
            t.role
            , t.permission
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
            auth_role_permission.id
            , auth_role_permission.role
            , auth_role_permission.permission
        ]
    return db.execute(sql, val)

def insert_auth_role_permission( auth_role_permission:AuthRolePermissionModel):
    sql = """
    INSERT INTO auth_role_permission( role,permission)
    VALUES (%s, %s)
    ;
"""
    val = [
            auth_role_permission.role
            , auth_role_permission.permission
        ]
    return db.execute(sql, val)

# this has a flaw in loop.index > 2
def update_auth_role_permission( auth_role_permission:AuthRolePermissionModel):
    sql = """
    UPDATE auth_role_permission
    SET role = %s, permission = %s
    WHERE id = %s
"""
    val = [auth_role_permission.role
            , auth_role_permission.permission
            , auth_role_permission.id
        ]
    return db.execute(sql, val)

#######################
# auth_role
#######################

def get_auth_role_basesql():
    sql = """
    SELECT id,role,description
    FROM auth_role
"""
    return sql

def get_auth_roles():
    sql = get_auth_role_basesql()
    return db.fetchall(sql)

def get_auth_role_by_id(id):
    sql = get_auth_role_basesql()
    sql += """
    WHERE  ANDrole = %s
"""
    return db.fetchall(sql, [id])

# def get_auth_role_by_auth_role_id(auth_role_id):
#     sql = get_auth_role_basesql()
#     sql += """
#     WHERE auth_role_id = %s
# """
#     return db.fetchall(sql, [auth_role_id])

def upsert_auth_role( auth_role:AuthRoleModel):
    sql = """
    WITH t AS (
        SELECT 
            %s as id
            , %s as role
            , %s as description
    ),
    u AS (
        UPDATE auth_role
        SET 
            role=t.role
            , description=t.description
        FROM t
        WHERE  ANDauth_role.role = t.role
        RETURNING id
    ),
    i AS (
        INSERT INTO auth_role( role,description)
        SELECT 
            t.role
            , t.description
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
            auth_role.id
            , auth_role.role
            , auth_role.description
        ]
    return db.execute(sql, val)

def insert_auth_role( auth_role:AuthRoleModel):
    sql = """
    INSERT INTO auth_role( role,description)
    VALUES (%s, %s)
    ;
"""
    val = [
            auth_role.id
            , auth_role.description
        ]
    return db.execute(sql, val)

# this has a flaw in loop.index > 2
def update_auth_role( auth_role:AuthRoleModel):
    sql = """
    UPDATE auth_role
    SET id = %s, description = %s
    WHERE  ANDrole = %s
"""
    val = [auth_role.id
            , auth_role.description
            , auth_role.role
        ]
    return db.execute(sql, val)
