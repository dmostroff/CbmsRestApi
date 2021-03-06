import pgsql_db_layer as db
import re
from decimal import Decimal


#######################
# client dashboard
#######################
def get_client_credit_summary():
    sql = """
    SELECT cp.id as id
        , MIN(TRIM( CONCAT(cp.last_name, ', ', cp.first_name, ' ', cp.middle_name))) as client_name
        , MIN(TRIM(CONCAT(address_1, ' ', address_2, ' ', city, ' ', state, ' ', zip))) as address
        , MIN(cp.email) AS email
        , MIN(cp.phone) as phone
        , MIN(COALESCE(cca.open_date, '1900-01-01')) as start_date
        , CAST( SUM( CASE WHEN cc_status = 'ACTIVE' THEN cca.credit_limit ELSE 0 END) AS DECIMAL(12,2)) AS total_credit_limit
    FROM client.client_person cp
        LEFT OUTER JOIN client.cc_account cca ON cca.client_id = cp.id
        LEFT OUTER JOIN client.client_address ca ON ca.client_id = cp.id AND ca.address_type = 'primary'
    GROUP BY cp.id
    ORDER BY start_date, client_name
"""
    return db.fetchall(sql)

def get_client_credit_summary_by_client_id( id):
    sql = """
    SELECT cp.id as client_id
        , MIN(TRIM( CONCAT(cp.last_name, ', ', cp.first_name, ' ', cp.middle_name))) as client_name
        , SUM( CASE WHEN cc_status = 'ACTIVE' THEN 1 ELSE 0 END) as number_of_cards
        , MIN(COALESCE(cca.open_date, '1900-01-01')) as start_date
        , CAST( SUM( CASE WHEN cc_status = 'ACTIVE' THEN cca.credit_limit ELSE 0 END) AS DECIMAL(12,2)) AS total_credit_limit
    FROM client.client_person cp
        LEFT OUTER JOIN client.cc_account cca ON cca.client_id = cp.id
    WHERE cp.id = %s
    GROUP BY cp.id
    ORDER BY start_date, client_name
"""
    return db.fetchall(sql, [id])



#######################
# client_person
#######################
from ClientPersonModel import ClientPersonModel

def get_client_person_base_sql():
    sql = """
    SELECT id
        , last_name
        , first_name
        , middle_name
        , dob
        , gender
        , ssn
        , mmn
        , email
        , pwd
        , occupation
        , employer
        , income
        , phone
        , phone_2
        , client_status
        , COALESCE( (SELECT MAX(keyvalue) FROM admin.adm_setting WHERE prefix = 'CLIENTSTATUS' AND keyname = client_status), client_status) as client_status_desc
        , client_info
        , recorded_on
    FROM client_person
"""
    return sql

def get_client_persons():
    sql = get_client_person_base_sql()
    return db.fetchall(sql)

def get_client_person_by_id(id):
    sql = get_client_person_base_sql()
    sql += """
    WHERE id = %s
"""
    return db.fetchall(sql, [id])

def upsert_client_person( client_person:ClientPersonModel):
    if client_person.dob is None:
        client_person.dob = ''
    client_person.income = re.sub( '[^\d\.]', '', client_person.income)
    income = Decimal(client_person.income) if client_person.income > '' else None
    sql = """
    WITH t AS (
        SELECT 
            %s as id
            , %s as last_name
            , %s as first_name
            , %s as middle_name
            , %s as dob
            , %s as gender
            , %s as ssn
            , %s as mmn
            , %s as email
            , %s as pwd
            , %s as occupation
            , %s as employer
            , CAST(%s AS DECIMAL(12,2)) as income
            , %s as phone
            , %s as phone_2
            , %s as client_status
            , to_jsonb(%s::text) as client_info
            , CURRENT_TIMESTAMP as recorded_on
    ),
    u AS (
        UPDATE client_person
        SET 
            last_name=t.last_name
            , first_name=t.first_name
            , middle_name=t.middle_name
            , dob=CASE WHEN t.dob > '' THEN to_date( t.dob, 'YYYY-MM-DD') ELSE null END
            , gender=t.gender
            , ssn=t.ssn
            , mmn=t.mmn
            , email=t.email
            , pwd=t.pwd
            , occupation=t.occupation
            , employer=t.employer
            , income=t.income
            , phone=t.phone
            , phone_2=t.phone_2
            , client_status=t.client_status
            , client_info=t.client_info
            , recorded_on=t.recorded_on
        FROM t
        WHERE client_person.id = t.id
        RETURNING client_person.*
    ),
    i AS (
        INSERT INTO client_person( 
            last_name
            , first_name
            , middle_name
            , dob
            , gender
            , ssn
            , mmn
            , email
            , pwd
            , occupation
            , employer
            , income
            , phone
            , phone_2
            , client_status
            , client_info
            , recorded_on
            )
        SELECT 
            t.last_name
            , t.first_name
            , t.middle_name
            , CASE WHEN t.dob > '' THEN to_date( t.dob, 'YYYY-MM-DD') ELSE null END
            , t.gender
            , t.ssn
            , t.mmn
            , t.email
            , t.pwd
            , t.occupation
            , t.employer
            , t.income
            , t.phone
            , t.phone_2
            , t.client_status
            , t.client_info
            , t.recorded_on
        FROM t
        WHERE NOT EXISTS ( SELECT 1 FROM u)
        RETURNING client_person.*
    )
    SELECT 'INSERT' as ACTION, i.*
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, u.*
    FROM u
    ;
    ;
"""
    val = [
            client_person.id
            , client_person.last_name
            , client_person.first_name
            , client_person.middle_name
            , str(client_person.dob)
            , client_person.gender
            , re.sub( '[^\d]', '', client_person.ssn)
            , client_person.mmn
            , client_person.email
            , client_person.pwd
            , client_person.occupation
            , client_person.employer
            , income
            , re.sub( '[^\d]', '', client_person.phone)
            , re.sub( '[^\d]', '', client_person.phone_2)
            , client_person.client_status
            , client_person.client_info
        ]
    return db.fetchall(sql, val)

def insert_client_person( client_person:ClientPersonModel):
    sql = """
    INSERT INTO client_person( 
		last_name
		, first_name
		, middle_name
		, dob
		, gender
		, ssn
		, mmn
		, email
		, pwd
		, occupation
		, phone
		, phone_2
		, client_status
		, client_info
		)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP)
    ;
"""
    val = [
            client_person.last_name
            , client_person.first_name
            , client_person.middle_name
            , client_person.dob
            , client_person.gender
            , client_person.ssn
            , client_person.mmn
            , client_person.email
            , client_person.pwd
            , client_person.occupation
            , client_person.phone
            , client_person.phone_2
            , client_person.client_status
            , client_person.client_info
            , client_person.recorded_on
        ]
    return db.execute(sql, val)

# this has a flaw in loop.index > 2
def update_client_person( client_person:ClientPersonModel):
    sql = """
    UPDATE client_person
    SET last_name = %s
        , first_name = %s
        , middle_name = %s
        , dob = %s
        , gender = %s
        , ssn = %s
        , mmn = %s
        , email = %s
        , pwd = %s
        , occupation = %s
        , phone = %s
        , phone_2 = %s
        , client_status = %s
        , client_info = %s
        , recorded_on = CURRENT_TIMSTAMP
    WHERE id = %s
"""
    val = [client_person.last_name
            , client_person.first_name
            , client_person.middle_name
            , client_person.dob
            , client_person.gender
            , client_person.ssn
            , client_person.mmn
            , client_person.email
            , client_person.pwd
            , client_person.occupation
            , client_person.phone
            , client_person.phone_2
            , client_person.client_status
            , client_person.client_info
            , client_person.id
        ]
    return db.execute(sql, val)

def delete_client_persons( id):
    sql = """
    DELETE FROM client_person
    WHERE id = %s
"""
    val = [ id ]
    return db.execute(sql, val                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               )


# print( 'client_repository')