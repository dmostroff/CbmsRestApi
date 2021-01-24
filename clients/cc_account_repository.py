import pgsql_db_layer as db


#######################
# cc_account
#######################
import CcAccount

def get_cc_account():
    sql = """
    SELECT cc_account_id,cc_card_id,client_id,card_name,card_holder,open_date,account_info,cc_login,cc_status,annual_fee_waived,credit_limit,last_checked,last_charge,addtional_card,balance_transfer,notes,ccaccount_info,recorded_on
    FROM cc_account
"""
    return db.fetchall(sql)

def get_by_client_id(client_id):
    sql = """
    SELECT cc_account_id,cc_card_id,client_id,card_name,card_holder,open_date,account_info,cc_login,cc_status,annual_fee_waived,credit_limit,last_checked,last_charge,addtional_card,balance_transfer,notes,ccaccount_info,recorded_on
    FROM cc_account
    WHERE client_id = %s
"""
    return db.fetchall(sql, [client_id])

def get_cc_account_by_id(id):
    sql = """
    SELECT cc_account_id,cc_card_id,client_id,card_name,card_holder,open_date,account_info,cc_login,cc_status,annual_fee_waived,credit_limit,last_checked,last_charge,addtional_card,balance_transfer,notes,ccaccount_info,recorded_on
    FROM cc_account
    WHERE cc_account_id = %s
"""
    return db.fetchall(sql, [id])

def upsert_cc_account( cc_account:CcAccount):
    sql = """
    WITH t AS (
        SELECT 
            %s as cc_account_id
            , %s as cc_card_id
            , %s as client_id
            , %s as card_name
            , %s as card_holder
            , %s as open_date
            , %s as account_info
            , %s as cc_login
            , %s as cc_status
            , %s as annual_fee_waived
            , %s as credit_limit
            , %s as last_checked
            , %s as last_charge
            , %s as addtional_card
            , %s as balance_transfer
            , %s as notes
            , %s as ccaccount_info
            , %s as recorded_on
    ),
    u AS (
        UPDATE cc_account
        SET 
            cc_card_id=t.cc_card_id
            , client_id=t.client_id
            , card_name=t.card_name
            , card_holder=t.card_holder
            , open_date=t.open_date
            , account_info=t.account_info
            , cc_login=t.cc_login
            , cc_status=t.cc_status
            , annual_fee_waived=t.annual_fee_waived
            , credit_limit=t.credit_limit
            , last_checked=t.last_checked
            , last_charge=t.last_charge
            , addtional_card=t.addtional_card
            , balance_transfer=t.balance_transfer
            , notes=t.notes
            , ccaccount_info=t.ccaccount_info
            , recorded_on=t.recorded_on
        FROM t
        WHERE cc_account.cc_account_id = t.cc_account_id
        RETURNING cc_account_id
    ),
    i AS (
        INSERT INTO cc_account( cc_card_id,client_id,card_name,card_holder,open_date,account_info,cc_login,cc_status,annual_fee_waived,credit_limit,last_checked,last_charge,addtional_card,balance_transfer,notes,ccaccount_info,recorded_on)
        SELECT 
            t.cc_card_id
            , t.client_id
            , t.card_name
            , t.card_holder
            , t.open_date
            , t.account_info
            , t.cc_login
            , t.cc_status
            , t.annual_fee_waived
            , t.credit_limit
            , t.last_checked
            , t.last_charge
            , t.addtional_card
            , t.balance_transfer
            , t.notes
            , t.ccaccount_info
            , t.recorded_on
        FROM t
        WHERE NOT EXISTS ( SELECT 1 FROM u)
    )
    SELECT 'INSERT' as ACTION, cc_account_id
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, cc_account_id
    FROM u
"""
    val = [
            CcAccount.cc_account_id
            , CcAccount.cc_card_id
            , CcAccount.client_id
            , CcAccount.card_name
            , CcAccount.card_holder
            , CcAccount.open_date
            , CcAccount.account_info
            , CcAccount.cc_login
            , CcAccount.cc_status
            , CcAccount.annual_fee_waived
            , CcAccount.credit_limit
            , CcAccount.last_checked
            , CcAccount.last_charge
            , CcAccount.addtional_card
            , CcAccount.balance_transfer
            , CcAccount.notes
            , CcAccount.ccaccount_info
            , CcAccount.recorded_on
        ]
    return db.execute(sql, val)

def insert_cc_account( cc_account:CcAccount):
    sql = """
    INSERT INTO cc_account( cc_card_id,client_id,card_name,card_holder,open_date,account_info,cc_login,cc_status,annual_fee_waived,credit_limit,last_checked,last_charge,addtional_card,balance_transfer,notes,ccaccount_info,recorded_on)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ;
"""
    val = [
            
            CcAccount.cc_card_id
            , CcAccount.client_id
            , CcAccount.card_name
            , CcAccount.card_holder
            , CcAccount.open_date
            , CcAccount.account_info
            , CcAccount.cc_login
            , CcAccount.cc_status
            , CcAccount.annual_fee_waived
            , CcAccount.credit_limit
            , CcAccount.last_checked
            , CcAccount.last_charge
            , CcAccount.addtional_card
            , CcAccount.balance_transfer
            , CcAccount.notes
            , CcAccount.ccaccount_info
            , CcAccount.recorded_on
        ]
    return db.execute(sql, val)

# this has a flaw in loop.index > 2
def update_cc_account( cc_account:CcAccount):
    sql = """
    UPDATE cc_account
    SET cc_card_id = %s, client_id = %s, card_name = %s, card_holder = %s, open_date = %s, account_info = %s, cc_login = %s, cc_status = %s, annual_fee_waived = %s, credit_limit = %s, last_checked = %s, last_charge = %s, addtional_card = %s, balance_transfer = %s, notes = %s, ccaccount_info = %s, recorded_on = %s
    WHERE cc_account_id = %s
"""
    val = [CcAccount.cc_card_id
            , CcAccount.client_id
            , CcAccount.card_name
            , CcAccount.card_holder
            , CcAccount.open_date
            , CcAccount.account_info
            , CcAccount.cc_login
            , CcAccount.cc_status
            , CcAccount.annual_fee_waived
            , CcAccount.credit_limit
            , CcAccount.last_checked
            , CcAccount.last_charge
            , CcAccount.addtional_card
            , CcAccount.balance_transfer
            , CcAccount.notes
            , CcAccount.ccaccount_info
            , CcAccount.recorded_on
            , CcAccount.cc_account_id
        ]
    return db.execute(sql, val)
