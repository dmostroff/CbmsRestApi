import pgsql_db_layer as db


#######################
# cc_card
#######################
import CcCardModel

def get_cc_card_basesql():
    sql = """
    SELECT id
        , cc_company_id
        , card_name
        , version
        , annual_fee
        , first_year_free
        , recorded_on
    FROM cc_card
"""
    return sql

def get_cc_cards():
    sql = get_cc_card_basesql()
    sql += " ORDER BY cc_company_id, card_name"
    return db.fetchall(sql)

def get_cc_card_by_id(id):
    sql = get_cc_card_basesql()
    sql += """
    WHERE cc_card_id = %s
"""
    return db.fetchall(sql, [id])

# def get_cc_card_by_cc_card_id(cc_card_id):
#     sql = get_cc_card_basesql()
#     sql += """
#     WHERE cc_card_id = %s
# """
#     return db.fetchall(sql, [cc_card_id])

def upsert_cc_card( cc_card:CcCardModel):
    sql = """
    WITH t AS (
        SELECT 
            %s::integer as id
            , %s::integer as cc_company_id
            , %s::text as card_name
            , %s::text as version
            , %s::numeric as annual_fee
            , %s::boolean as first_year_free
            , CURRENT_TIMESTAMP as recorded_on
    ),
    u AS (
        UPDATE cc_card
        SET 
            cc_company_id=t.cc_company_id
            , card_name=t.card_name
            , version=t.version
            , annual_fee=t.annual_fee
            , first_year_free=t.first_year_free
            , recorded_on=t.recorded_on
        FROM t
        WHERE cc_card.id = t.id
        RETURNING cc_card.*
    ),
    i AS (
        INSERT INTO cc_card( cc_company_id,card_name,version,annual_fee,first_year_free,recorded_on)
        SELECT 
            t.cc_company_id
            , t.card_name
            , t.version
            , t.annual_fee
            , t.first_year_free
            , t.recorded_on
        FROM t
        WHERE NOT EXISTS ( SELECT 1 FROM u)
        RETURNING cc_card.*
    )
    SELECT 'INSERT' as ACTION, i.*
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, u.*
    FROM u
"""
    val = [
            cc_card.id
            , cc_card.cc_company_id
            , cc_card.card_name
            , cc_card.version
            , cc_card.annual_fee
            , cc_card.first_year_free
        ]
    return db.fetchall(sql, val)

def insert_cc_card( cc_card:CcCardModel):
    sql = """
    INSERT INTO cc_card( cc_company_id,card_name,version,annual_fee,first_year_free)
    VALUES (%s, %s, %s, %s, %s)
    RETURNING *
    ;
"""
    val = [
            cc_card.cc_company_id
            , cc_card.card_name
            , cc_card.version
            , cc_card.annual_fee
            , cc_card.first_year_free
        ]
    return db.fetchone(sql, val)

# this has a flaw in loop.index > 2
def update_cc_card( cc_card:CcCardModel):
    sql = """
    UPDATE cc_card
    SET cc_company_id = %s
        , card_name = %s
        , version = %s
        , annual_fee = %s
        , first_year_free = %s
        , recorded_on = CURRENT_TIMESTAMP
    WHERE id = %s
    RETURNING *
"""
    val = [
            cc_card.cc_company_id
            , cc_card.card_name
            , cc_card.version
            , cc_card.annual_fee
            , cc_card.first_year_free
            , cc_card.id            
        ]
    return db.fetchone(sql, val)
