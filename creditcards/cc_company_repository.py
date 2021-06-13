import pgsql_db_layer as db


#######################
# cc_company
#######################
import CcCompanyModel

def get_cc_company_basesql():
    sql = """
    SELECT cc_company_id,company_name,url,contact,address_1,address_2,city,state,zip,country,phone,phone_2,phone_cell,phone_fax,company_info,recorded_on
    FROM cc_company
"""
    return sql

def get_cc_companies():
    sql = get_cc_company_basesql()
    return db.fetchall(sql)

def get_cc_company_by_id(id):
    sql = get_cc_company_basesql()
    sql += """
    WHERE cc_company_id = %s
"""
    return db.fetchall(sql, [id])

def upsert_cc_company( cc_company:CcCompanyModel):
    sql = """
    WITH t AS (
        SELECT 
            %s::integer as cc_company_id
            , %s::text as company_name
            , %s::text as url
            , %s::text as contact
            , %s::text as address_1
            , %s::text as address_2
            , %s::text as city
            , %s::character as state
            , %s::character varying as zip
            , %s::character as country
            , %s::character varying as phone
            , %s::character varying as phone_2
            , %s::character varying as phone_cell
            , %s::character varying as phone_fax
            , %s::jsonb as company_info
            , %s::timestamp with time zone as recorded_on
    ),
    u AS (
        UPDATE cc_company
        SET 
            company_name=t.company_name
            , url=t.url
            , contact=t.contact
            , address_1=t.address_1
            , address_2=t.address_2
            , city=t.city
            , state=t.state
            , zip=t.zip
            , country=t.country
            , phone=t.phone
            , phone_2=t.phone_2
            , phone_cell=t.phone_cell
            , phone_fax=t.phone_fax
            , company_info=t.company_info
            , recorded_on=t.recorded_on
        FROM t
        WHERE cc_company.cc_company_id = t.cc_company_id
        RETURNING , cc_company.cc_company_id
    ),
    i AS (
        INSERT INTO cc_company( company_name,url,contact,address_1,address_2,city,state,zip,country,phone,phone_2,phone_cell,phone_fax,company_info,recorded_on)
        SELECT 
            t.company_name
            , t.url
            , t.contact
            , t.address_1
            , t.address_2
            , t.city
            , t.state
            , t.zip
            , t.country
            , t.phone
            , t.phone_2
            , t.phone_cell
            , t.phone_fax
            , t.company_info
            , t.recorded_on
        FROM t
        WHERE NOT EXISTS ( SELECT 1 FROM u)
        RETURNING , cc_company.cc_company_id
    )
    SELECT 'INSERT' as ACTION, cc_company_id
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, cc_company_id
    FROM u
"""
    val = [
            cc_company.cc_company_id
            , cc_company.company_name
            , cc_company.url
            , cc_company.contact
            , cc_company.address_1
            , cc_company.address_2
            , cc_company.city
            , cc_company.state
            , cc_company.zip
            , cc_company.country
            , cc_company.phone
            , cc_company.phone_2
            , cc_company.phone_cell
            , cc_company.phone_fax
            , cc_company.company_info
            , cc_company.recorded_on
        ]
    return db.fetchall(sql, val)

def insert_cc_company( cc_company:CcCompanyModel):
    sql = """
    INSERT INTO cc_company( company_name,url,contact,address_1,address_2,city,state,zip,country,phone,phone_2,phone_cell,phone_fax,company_info,recorded_on)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    RETURNING *
    ;
"""
    val = [
            
            cc_company.company_name
            , cc_company.url
            , cc_company.contact
            , cc_company.address_1
            , cc_company.address_2
            , cc_company.city
            , cc_company.state
            , cc_company.zip
            , cc_company.country
            , cc_company.phone
            , cc_company.phone_2
            , cc_company.phone_cell
            , cc_company.phone_fax
            , cc_company.company_info
            , cc_company.recorded_on
        ]
    return db.fetchone(sql, val)

# this has a flaw in loop.index > 2
def update_cc_company( cc_company:CcCompanyModel):
    sql = """
    UPDATE cc_company
    SET company_name = %s, url = %s, contact = %s, address_1 = %s, address_2 = %s, city = %s, state = %s, zip = %s, country = %s, phone = %s, phone_2 = %s, phone_cell = %s, phone_fax = %s, company_info = %s, recorded_on = %s
    WHERE cc_company_id = %s
    RETURNING *
"""
    val = [cc_company.company_name
            , cc_company.url
            , cc_company.contact
            , cc_company.address_1
            , cc_company.address_2
            , cc_company.city
            , cc_company.state
            , cc_company.zip
            , cc_company.country
            , cc_company.phone
            , cc_company.phone_2
            , cc_company.phone_cell
            , cc_company.phone_fax
            , cc_company.company_info
            , cc_company.recorded_on
        , cc_company.cc_company_id            
        ]
    return db.fetchone(sql, val)
