import pgsql_db_layer as db


#######################
# client_address
#######################
import ClientAddressModel

def get_client_address_basesql():
    sql = """
    SELECT address_id,client_id,address_type,address_1,address_2,city,state,zip,country,valid_from,valid_to,recorded_on
    FROM client_address
"""
    return sql

def get_client_addresss():
    sql = get_client_address_basesql()
    return db.fetchall(sql)

def get_client_address_by_id(id):
    sql = get_client_address_basesql()
    sql += """
    WHERE address_id = %s
"""
    return db.fetchall(sql, [id])

def get_client_address_by_client_id(id):
    sql = get_client_address_basesql()
    sql += """
    WHERE client_id = %s
"""
    return db.fetchall(sql, [id])

# def get_client_address_by_client_address_id(client_address_id):
#     sql = get_client_address_basesql()
#     sql += """
#     WHERE client_address_id = %s
# """
#     return db.fetchall(sql, [client_address_id])

def upsert_client_address( client_address:ClientAddressModel):
    sql = """
    WITH t AS (
        SELECT 
            %s::integer as address_id
            , %s::integer as client_id
            , %s::character varying as address_type
            , %s::text as address_1
            , %s::text as address_2
            , %s::text as city
            , %s::text as state
            , %s::character varying as zip
            , %s::character as country
            , %s::date as valid_from
            , %s::date as valid_to
            , %s::timestamp with time zone as recorded_on
    ),
    u AS (
        UPDATE client_address
        SET 
            client_id=t.client_id
            , address_type=t.address_type
            , address_1=t.address_1
            , address_2=t.address_2
            , city=t.city
            , state=t.state
            , zip=t.zip
            , country=t.country
            , valid_from=t.valid_from
            , valid_to=t.valid_to
            , recorded_on=t.recorded_on
        FROM t
        WHERE client_address.address_id = t.address_id
        RETURNING , client_address.address_id
    ),
    i AS (
        INSERT INTO client_address( client_id,address_type,address_1,address_2,city,state,zip,country,valid_from,valid_to,recorded_on)
        SELECT 
            t.client_id
            , t.address_type
            , t.address_1
            , t.address_2
            , t.city
            , t.state
            , t.zip
            , t.country
            , t.valid_from
            , t.valid_to
            , t.recorded_on
        FROM t
        WHERE NOT EXISTS ( SELECT 1 FROM u)
        RETURNING , client_address.address_id
    )
    SELECT 'INSERT' as ACTION, address_id
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, address_id
    FROM u
"""
    val = [
            client_address.address_id
            , client_address.client_id
            , client_address.address_type
            , client_address.address_1
            , client_address.address_2
            , client_address.city
            , client_address.state
            , client_address.zip
            , client_address.country
            , client_address.valid_from
            , client_address.valid_to
            , client_address.recorded_on
        ]
    return db.fetchall(sql, val)

def insert_client_address( client_address:ClientAddressModel):
    sql = """
    INSERT INTO client_address( client_id,address_type,address_1,address_2,city,state,zip,country,valid_from,valid_to,recorded_on)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    RETURNING *
    ;
"""
    val = [
            client_address.client_id
            , client_address.address_type
            , client_address.address_1
            , client_address.address_2
            , client_address.city
            , client_address.state
            , client_address.zip
            , client_address.country
            , client_address.valid_from
            , client_address.valid_to
            , client_address.recorded_on
        ]
    return db.fetchone(sql, val)

# this has a flaw in loop.index > 2
def update_client_address( client_address:ClientAddressModel):
    sql = """
    UPDATE client_address
    SET client_id = %s, address_type = %s, address_1 = %s, address_2 = %s, city = %s, state = %s, zip = %s, country = %s, valid_from = %s, valid_to = %s, recorded_on = %s
    WHERE address_id = %s
    RETURNING *
"""
    val = [client_address.client_id
            , client_address.address_type
            , client_address.address_1
            , client_address.address_2
            , client_address.city
            , client_address.state
            , client_address.zip
            , client_address.country
            , client_address.valid_from
            , client_address.valid_to
            , client_address.recorded_on
        , client_address.address_id            
        ]
    return db.fetchone(sql, val)
