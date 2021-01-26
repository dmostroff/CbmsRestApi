import pgsql_db_layer as db


#######################
# cc_account_promo
#######################
import CcAccountPromo

def get_cc_account_promo_basesql():
    sql = """
    SELECT promo_id,cc_account_id,offer,loan_amt,bal_transfer_date,bal_transfer_amt,promo_info,recorded_on
    FROM cc_account_promo
"""
    return sql

def get_cc_account_promo():
    sql = get_cc_account_promo_basesql()
    return db.fetchall(sql)

def get_cc_account_promo_by_id(id):
    sql = get_cc_account_promo_basesql()
    sql += """
    WHERE promo_id = %s
"""
    return db.fetchall(sql, [id])

def get_cc_account_promo_by_client_id(client_id):
    sql = get_cc_account_promo_basesql()
    sql += """
    WHERE client_id = %s
"""
    return db.fetchall(sql, [client_id])

def upsert_cc_account_promo( cc_account_promo:CcAccountPromo):
    sql = """
    WITH t AS (
        SELECT 
            %s as promo_id
            , %s as cc_account_id
            , %s as offer
            , %s as loan_amt
            , %s as bal_transfer_date
            , %s as bal_transfer_amt
            , %s as promo_info
            , %s as recorded_on
    ),
    u AS (
        UPDATE cc_account_promo
        SET 
            cc_account_id=t.cc_account_id
            , offer=t.offer
            , loan_amt=t.loan_amt
            , bal_transfer_date=t.bal_transfer_date
            , bal_transfer_amt=t.bal_transfer_amt
            , promo_info=t.promo_info
            , recorded_on=t.recorded_on
        FROM t
        WHERE cc_account_promo.promo_id = t.promo_id
        RETURNING promo_id
    ),
    i AS (
        INSERT INTO cc_account_promo( cc_account_id,offer,loan_amt,bal_transfer_date,bal_transfer_amt,promo_info,recorded_on)
        SELECT 
            t.cc_account_id
            , t.offer
            , t.loan_amt
            , t.bal_transfer_date
            , t.bal_transfer_amt
            , t.promo_info
            , t.recorded_on
        FROM t
        WHERE NOT EXISTS ( SELECT 1 FROM u)
    )
    SELECT 'INSERT' as ACTION, promo_id
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, promo_id
    FROM u
    ;
    ;
"""
    val = [
            cc_account_promo.promo_id
            , cc_account_promo.cc_account_id
            , cc_account_promo.offer
            , cc_account_promo.loan_amt
            , cc_account_promo.bal_transfer_date
            , cc_account_promo.bal_transfer_amt
            , cc_account_promo.promo_info
            , cc_account_promo.recorded_on
        ]
    return db.execute(sql, val)

def insert_cc_account_promo( cc_account_promo:CcAccountPromo):
    sql = """
    INSERT INTO cc_account_promo( cc_account_id,offer,loan_amt,bal_transfer_date,bal_transfer_amt,promo_info,recorded_on)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ;
"""
    val = [
            
            cc_account_promo.cc_account_id
            , cc_account_promo.offer
            , cc_account_promo.loan_amt
            , cc_account_promo.bal_transfer_date
            , cc_account_promo.bal_transfer_amt
            , cc_account_promo.promo_info
            , cc_account_promo.recorded_on
        ]
    return db.execute(sql, val)

# this has a flaw in loop.index > 2
def update_cc_account_promo( cc_account_promo:CcAccountPromo):
    sql = """
    UPDATE cc_account_promo
    SET cc_account_id = %s, offer = %s, loan_amt = %s, bal_transfer_date = %s, bal_transfer_amt = %s, promo_info = %s, recorded_on = %s
    WHERE promo_id = %s
"""
    val = [cc_account_promo.cc_account_id
            , cc_account_promo.offer
            , cc_account_promo.loan_amt
            , cc_account_promo.bal_transfer_date
            , cc_account_promo.bal_transfer_amt
            , cc_account_promo.promo_info
            , cc_account_promo.recorded_on
            , cc_account_promo.promo_id
        ]
    return db.execute(sql, val)

#######################
# cc_account
#######################
import CcAccount

def get_cc_account_basesql():
    sql = """
    SELECT cc_account_id,cc_card_id,client_id,card_name,card_holder,open_date,account_info,cc_login,cc_status,annual_fee_waived,credit_limit,last_checked,last_charge,addtional_card,balance_transfer,notes,ccaccount_info,recorded_on
    FROM cc_account
"""
    return sql

def get_cc_account():
    sql = get_cc_account_basesql()
    return db.fetchall(sql)

def get_cc_account_by_id(id):
    sql = get_cc_account_basesql()
    sql += """
    WHERE cc_account_id = %s
"""
    return db.fetchall(sql, [id])

def get_cc_account_by_cc_account_id(cc_account_id):
    sql = get_cc_account_basesql()
    sql += """
    WHERE cc_account_id = %s
"""
    return db.fetchall(sql, [cc_account_id])

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
    ;
    ;
"""
    val = [
            cc_account.cc_account_id
            , cc_account.cc_card_id
            , cc_account.client_id
            , cc_account.card_name
            , cc_account.card_holder
            , cc_account.open_date
            , cc_account.account_info
            , cc_account.cc_login
            , cc_account.cc_status
            , cc_account.annual_fee_waived
            , cc_account.credit_limit
            , cc_account.last_checked
            , cc_account.last_charge
            , cc_account.addtional_card
            , cc_account.balance_transfer
            , cc_account.notes
            , cc_account.ccaccount_info
            , cc_account.recorded_on
        ]
    return db.execute(sql, val)

def insert_cc_account( cc_account:CcAccount):
    sql = """
    INSERT INTO cc_account( cc_card_id,client_id,card_name,card_holder,open_date,account_info,cc_login,cc_status,annual_fee_waived,credit_limit,last_checked,last_charge,addtional_card,balance_transfer,notes,ccaccount_info,recorded_on)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ;
"""
    val = [
            
            cc_account.cc_card_id
            , cc_account.client_id
            , cc_account.card_name
            , cc_account.card_holder
            , cc_account.open_date
            , cc_account.account_info
            , cc_account.cc_login
            , cc_account.cc_status
            , cc_account.annual_fee_waived
            , cc_account.credit_limit
            , cc_account.last_checked
            , cc_account.last_charge
            , cc_account.addtional_card
            , cc_account.balance_transfer
            , cc_account.notes
            , cc_account.ccaccount_info
            , cc_account.recorded_on
        ]
    return db.execute(sql, val)

# this has a flaw in loop.index > 2
def update_cc_account( cc_account:CcAccount):
    sql = """
    UPDATE cc_account
    SET cc_card_id = %s, client_id = %s, card_name = %s, card_holder = %s, open_date = %s, account_info = %s, cc_login = %s, cc_status = %s, annual_fee_waived = %s, credit_limit = %s, last_checked = %s, last_charge = %s, addtional_card = %s, balance_transfer = %s, notes = %s, ccaccount_info = %s, recorded_on = %s
    WHERE cc_account_id = %s
"""
    val = [cc_account.cc_card_id
            , cc_account.client_id
            , cc_account.card_name
            , cc_account.card_holder
            , cc_account.open_date
            , cc_account.account_info
            , cc_account.cc_login
            , cc_account.cc_status
            , cc_account.annual_fee_waived
            , cc_account.credit_limit
            , cc_account.last_checked
            , cc_account.last_charge
            , cc_account.addtional_card
            , cc_account.balance_transfer
            , cc_account.notes
            , cc_account.ccaccount_info
            , cc_account.recorded_on
            , cc_account.cc_account_id
        ]
    return db.execute(sql, val)
