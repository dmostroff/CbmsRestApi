import pgsql_db_layer as db
from ClientBankAccountModel import ClientBankAccountModel


#######################
# client_bank_account
#######################

def get_client_bank_account_basesql():
    sql = """
    SELECT id,client_id,bank_name,account_num,routing_num,branch_num,iban,country,account_login,account_pwd,account_status,debit_card,debit_info,recorded_on
    FROM client.client_bank_account
"""
    return sql

def get_client_bank_accounts():
    sql = get_client_bank_account_basesql()
    return db.fetchall(sql)

def get_client_bank_account_by_id(id):
    sql = get_client_bank_account_basesql()
    sql += """
    WHERE id = %s
"""
    return db.fetchall(sql, [id])

# def get_client_bank_account_by_client_bank_account_id(client_bank_account_id):
#     sql = get_client_bank_account_basesql()
#     sql += """
#     WHERE client_bank_account_id = %s
# """
#     return db.fetchall(sql, [client_bank_account_id])

def upsert_client_bank_account( client_bank_account:ClientBankAccountModel):
    sql = """
    WITH t AS (
        SELECT 
            %s::integer as id
            , %s::integer as client_id
            , %s::text as bank_name
            , %s::text as account_num
            , %s::text as routing_num
            , %s::text as branch_num
            , %s::text as iban
            , %s::character as country
            , %s::text as account_login
            , %s::text as account_pwd
            , %s::character varying as account_status
            , %s::text as debit_card
            , %s::text as debit_info
            , %s::timestamp with time zone as recorded_on
    ),
    u AS (
        UPDATE client.client_bank_account
        SET 
            client_id=t.client_id
            , bank_name=t.bank_name
            , account_num=t.account_num
            , routing_num=t.routing_num
            , branch_num=t.branch_num
            , iban=t.iban
            , country=t.country
            , account_login=t.account_login
            , account_pwd=t.account_pwd
            , account_status=t.account_status
            , debit_card=t.debit_card
            , debit_info=t.debit_info
            , recorded_on=t.recorded_on
        FROM t
        WHERE client_bank_account.id = t.id
        RETURNING client_bank_account.id
    ),
    i AS (
        INSERT INTO client.client_bank_account( client_id,bank_name,account_num,routing_num,branch_num,iban,country,account_login,account_pwd,account_status,debit_card,debit_info,recorded_on)
        SELECT 
            t.client_id
            , t.bank_name
            , t.account_num
            , t.routing_num
            , t.branch_num
            , t.iban
            , t.country
            , t.account_login
            , t.account_pwd
            , t.account_status
            , t.debit_card
            , t.debit_info
            , t.recorded_on
        FROM t
        WHERE NOT EXISTS ( SELECT 1 FROM u)
        RETURNING client_bank_account.id
    )
    SELECT 'INSERT' as ACTION, id
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, id
    FROM u
"""
    val = [
            client_bank_account.id
            , client_bank_account.client_id
            , client_bank_account.bank_name
            , client_bank_account.account_num
            , client_bank_account.routing_num
            , client_bank_account.branch_num
            , client_bank_account.iban
            , client_bank_account.country
            , client_bank_account.account_login
            , client_bank_account.account_pwd
            , client_bank_account.account_status
            , client_bank_account.debit_card
            , client_bank_account.debit_info
            , client_bank_account.recorded_on
        ]
    return db.fetchall(sql, val)

def insert_client_bank_account( client_bank_account:ClientBankAccountModel):
    sql = """
    INSERT INTO client.client_bank_account( client_id,bank_name,account_num,routing_num,branch_num,iban,country,account_login,account_pwd,account_status,debit_card,debit_info,recorded_on)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    RETURNING *
"""
    val = [
            client_bank_account.client_id
            , client_bank_account.bank_name
            , client_bank_account.account_num
            , client_bank_account.routing_num
            , client_bank_account.branch_num
            , client_bank_account.iban
            , client_bank_account.country
            , client_bank_account.account_login
            , client_bank_account.account_pwd
            , client_bank_account.account_status
            , client_bank_account.debit_card
            , client_bank_account.debit_info
            , client_bank_account.recorded_on
        ]
    return db.fetchone(sql, val)

# this has a flaw in loop.index > 2
def update_client_bank_account( client_bank_account:ClientBankAccountModel):
    sql = """
    UPDATE client.client_bank_account
    SET client_id = %s, bank_name = %s, account_num = %s, routing_num = %s, branch_num = %s, iban = %s, country = %s, account_login = %s, account_pwd = %s, account_status = %s, debit_card = %s, debit_info = %s, recorded_on = %s
    WHERE id = %s
    RETURNING *
"""
    val = [client_bank_account.client_id
            , client_bank_account.bank_name
            , client_bank_account.account_num
            , client_bank_account.routing_num
            , client_bank_account.branch_num
            , client_bank_account.iban
            , client_bank_account.country
            , client_bank_account.account_login
            , client_bank_account.account_pwd
            , client_bank_account.account_status
            , client_bank_account.debit_card
            , client_bank_account.debit_info
            , client_bank_account.recorded_on
        , client_bank_account.id            
        ]
    return db.fetchone(sql, val)
