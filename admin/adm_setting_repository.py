import pgsql_db_layer as db


#######################
# adm_setting
#######################
from admin_model import AdmSettingModel

def get_adm_setting_basesql():
    sql = """
    SELECT id, prefix, keyname, keyvalue, display_rank
    FROM admin.adm_setting
"""
    return sql

def get_adm_settings():
    sql = get_adm_setting_basesql()
    sql += " ORDER BY prefix, display_rank"
    return db.fetchall(sql)

def get_adm_setting_by_prefix(prefix):
    sql = get_adm_setting_basesql()
    sql += """
    WHERE prefix = %s
    ORDER BY display_rank
"""
    return db.fetchall(sql, [prefix])


def get_adm_setting_by_id(id):
    sql = get_adm_setting_basesql()
    sql += """
    WHERE id = %s
"""
    df = db.fetchall(sql, [id])
    return df.head(1)

# def get_adm_setting_by_adm_setting_id(adm_setting_id):
#     sql = get_adm_setting_basesql()
#     sql += """
#     WHERE adm_setting_id = %s
# """
#     return db.fetchall(sql, [adm_setting_id])

def upsert_adm_setting( adm_setting:AdmSettingModel):
    sql = """
    WITH t AS (
        SELECT 
            %s::int as id
            , %s::varchar(32) as prefix
            , %s::text as keyname
            , %s::text as keyvalue
    ),
    u AS (
        UPDATE admin.adm_setting
        SET 
            prefix=t.prefix
            , keyname=t.keyname
            , keyvalue=t.keyvalue
        FROM t
        WHERE admin.adm_setting.id = t.id
        RETURNING admin.adm_setting.*
    ),
    i AS (
        INSERT INTO admin.adm_setting( prefix,keyname,keyvalue)
        SELECT 
            t.prefix
            , t.keyname
            , t.keyvalue
        FROM t
        WHERE NOT EXISTS ( SELECT 1 FROM u)
        RETURNING admin.adm_setting.*
    )
    SELECT 'INSERT' as ACTION, i.id
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, u.id
    FROM u
"""
    val = [
            adm_setting.id
            , adm_setting.prefix
            , adm_setting.keyname
            , adm_setting.keyvalue
        ]
    return db.fetchall(sql, val)

def insert_adm_setting( adm_setting:AdmSettingModel):
    sql = """
    INSERT INTO admin.adm_setting( prefix,keyname,keyvalue)
    VALUES (%s, %s, %s)
    RETURNING *
    ;
"""
    val = [
            adm_setting.prefix
            , adm_setting.keyname
            , adm_setting.keyvalue
        ]
    return db.execute(sql, val)

# this has a flaw in loop.index > 2
def update_adm_setting( adm_setting:AdmSettingModel):
    sql = """
    UPDATE admin.adm_setting
    SET sprefix = %s, keyname = %s, keyvalue = %s
    WHERE id = %s
"""
    val = [
            adm_setting.prefix
            , adm_setting.keyname
            , adm_setting.keyvalue
            , adm_setting.id
        ]
    return db.execute(sql, val)
