import pgsql_db_layer as db


#######################
# client_person
#######################
import ClientPerson

def get_client_person():
    sql = """
    SELECT client_id,last_name,first_name,middle_name,dob,gender,ssn,mmn,email,pwd,occupation,phone,phone_2,phone_cell,phone_official,client_info,recorded_on
    FROM client_person
"""
    return db.fetchall(sql)

def get_client_person_by_id(id):
    sql = """
    SELECT client_id,last_name,first_name,middle_name,dob,gender,ssn,mmn,email,pwd,occupation,phone,phone_2,phone_cell,phone_official,client_info,recorded_on
    FROM client_person
    WHERE client_id = %s
"""
    return db.fetchall(sql, [id])

def get_client_person_by_client_id(client_id):
    sql = """
    SELECT client_id,last_name,first_name,middle_name,dob,gender,ssn,mmn,email,pwd,occupation,phone,phone_2,phone_cell,phone_official,client_info,recorded_on
    FROM client_person
    WHERE client_id = %s
"""
    return db.fetchall(sql, [client_id])

def upsert_client_person( client_person:ClientPerson):
    sql = """
    WITH t AS (
        SELECT 
            %s as client_id
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
            , %s as phone
            , %s as phone_2
            , %s as phone_cell
            , %s as phone_official
            , %s as client_info
            , %s as recorded_on
    ),
    u AS (
        UPDATE client_person
        SET 
            last_name=t.last_name
            , first_name=t.first_name
            , middle_name=t.middle_name
            , dob=t.dob
            , gender=t.gender
            , ssn=t.ssn
            , mmn=t.mmn
            , email=t.email
            , pwd=t.pwd
            , occupation=t.occupation
            , phone=t.phone
            , phone_2=t.phone_2
            , phone_cell=t.phone_cell
            , phone_official=t.phone_official
            , client_info=t.client_info
            , recorded_on=t.recorded_on
        FROM t
        WHERE client_person.client_id = t.client_id
        RETURNING client_id
    ),
    i AS (
        INSERT INTO client_person( last_name,first_name,middle_name,dob,gender,ssn,mmn,email,pwd,occupation,phone,phone_2,phone_cell,phone_official,client_info,recorded_on)
        SELECT 
            t.last_name
            , t.first_name
            , t.middle_name
            , t.dob
            , t.gender
            , t.ssn
            , t.mmn
            , t.email
            , t.pwd
            , t.occupation
            , t.phone
            , t.phone_2
            , t.phone_cell
            , t.phone_official
            , t.client_info
            , t.recorded_on
        FROM t
        WHERE NOT EXISTS ( SELECT 1 FROM u)
    )
    SELECT 'INSERT' as ACTION, client_id
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, client_id
    FROM u
    ;
    ;
"""
    val = [
            client_person.client_id
            , client_person.last_name
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
            , client_person.phone_cell
            , client_person.phone_official
            , client_person.client_info
            , client_person.recorded_on
        ]
    return db.execute(sql, val)

def insert_client_person( client_person:ClientPerson):
    sql = """
    INSERT INTO client_person( last_name,first_name,middle_name,dob,gender,ssn,mmn,email,pwd,occupation,phone,phone_2,phone_cell,phone_official,client_info,recorded_on)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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
            , client_person.phone_cell
            , client_person.phone_official
            , client_person.client_info
            , client_person.recorded_on
        ]
    return db.execute(sql, val)

# this has a flaw in loop.index > 2
def update_client_person( client_person:ClientPerson):
    sql = """
    UPDATE client_person
    SET last_name = %s, first_name = %s, middle_name = %s, dob = %s, gender = %s, ssn = %s, mmn = %s, email = %s, pwd = %s, occupation = %s, phone = %s, phone_2 = %s, phone_cell = %s, phone_official = %s, client_info = %s, recorded_on = %s
    WHERE client_id = %s
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
            , client_person.phone_cell
            , client_person.phone_official
            , client_person.client_info
            , client_person.recorded_on
        
            , client_person.client_id
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                        
        ]
    return db.execute(sql, val)

#######################
# client_cc_history
#######################
import ClientCcHistory

def get_client_cc_history():
    sql = """
    SELECT cc_hist_id,client_id,ccaccount_id,ccevent,ccevent_amt,details,recorded_on
    FROM client_cc_history
"""
    return db.fetchall(sql)

def get_client_cc_history_by_id(id):
    sql = """
    SELECT cc_hist_id,client_id,ccaccount_id,ccevent,ccevent_amt,details,recorded_on
    FROM client_cc_history
    WHERE cc_hist_id = %s
"""
    return db.fetchall(sql, [id])

def get_client_cc_history_by_client_id(client_id):
    sql = """
    SELECT cc_hist_id,client_id,ccaccount_id,ccevent,ccevent_amt,details,recorded_on
    FROM client_cc_history
    WHERE client_id = %s
"""
    return db.fetchall(sql, [client_id])

def upsert_client_cc_history( client_cc_history:ClientCcHistory):
    sql = """
    WITH t AS (
        SELECT 
            %s as cc_hist_id
            , %s as client_id
            , %s as ccaccount_id
            , %s as ccevent
            , %s as ccevent_amt
            , %s as details
            , %s as recorded_on
    ),
    u AS (
        UPDATE client_cc_history
        SET 
            client_id=t.client_id
            , ccaccount_id=t.ccaccount_id
            , ccevent=t.ccevent
            , ccevent_amt=t.ccevent_amt
            , details=t.details
            , recorded_on=t.recorded_on
        FROM t
        WHERE client_cc_history.cc_hist_id = t.cc_hist_id
        RETURNING cc_hist_id
    ),
    i AS (
        INSERT INTO client_cc_history( client_id,ccaccount_id,ccevent,ccevent_amt,details,recorded_on)
        SELECT 
            t.client_id
            , t.ccaccount_id
            , t.ccevent
            , t.ccevent_amt
            , t.details
            , t.recorded_on
        FROM t
        WHERE NOT EXISTS ( SELECT 1 FROM u)
    )
    SELECT 'INSERT' as ACTION, cc_hist_id
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, cc_hist_id
    FROM u
    ;
    ;
"""
    val = [
            client_cc_history.cc_hist_id
            , client_cc_history.client_id
            , client_cc_history.ccaccount_id
            , client_cc_history.ccevent
            , client_cc_history.ccevent_amt
            , client_cc_history.details
            , client_cc_history.recorded_on
        ]
    return db.execute(sql, val)

def insert_client_cc_history( client_cc_history:ClientCcHistory):
    sql = """
    INSERT INTO client_cc_history( client_id,ccaccount_id,ccevent,ccevent_amt,details,recorded_on)
    VALUES (%s, %s, %s, %s, %s, %s)
    ;
"""
    val = [
            
            client_cc_history.client_id
            , client_cc_history.ccaccount_id
            , client_cc_history.ccevent
            , client_cc_history.ccevent_amt
            , client_cc_history.details
            , client_cc_history.recorded_on
        ]
    return db.execute(sql, val)

# this has a flaw in loop.index > 2
def update_client_cc_history( client_cc_history:ClientCcHistory):
    sql = """
    UPDATE client_cc_history
    SET client_id = %s, ccaccount_id = %s, ccevent = %s, ccevent_amt = %s, details = %s, recorded_on = %s
    WHERE cc_hist_id = %s
"""
    val = [client_cc_history.client_id
            , client_cc_history.ccaccount_id
            , client_cc_history.ccevent
            , client_cc_history.ccevent_amt
            , client_cc_history.details
            , client_cc_history.recorded_on
        
            , client_cc_history.cc_hist_id
            
            
            
            
            
                        
        ]
    return db.execute(sql, val)

#######################
# client_creditline_history
#######################
import ClientCreditlineHistory

def get_client_creditline_history():
    sql = """
    SELECT creditline_id,client_id,cc_account_id,credit_line_date,credit_amt,credit_status,recorded_on
    FROM client_creditline_history
"""
    return db.fetchall(sql)

def get_client_creditline_history_by_id(id):
    sql = """
    SELECT creditline_id,client_id,cc_account_id,credit_line_date,credit_amt,credit_status,recorded_on
    FROM client_creditline_history
    WHERE creditline_id = %s
"""
    return db.fetchall(sql, [id])

def get_client_creditline_history_by_client_id(client_id):
    sql = """
    SELECT creditline_id,client_id,cc_account_id,credit_line_date,credit_amt,credit_status,recorded_on
    FROM client_creditline_history
    WHERE client_id = %s
"""
    return db.fetchall(sql, [client_id])

def upsert_client_creditline_history( client_creditline_history:ClientCreditlineHistory):
    sql = """
    WITH t AS (
        SELECT 
            %s as creditline_id
            , %s as client_id
            , %s as cc_account_id
            , %s as credit_line_date
            , %s as credit_amt
            , %s as credit_status
            , %s as recorded_on
    ),
    u AS (
        UPDATE client_creditline_history
        SET 
            client_id=t.client_id
            , cc_account_id=t.cc_account_id
            , credit_line_date=t.credit_line_date
            , credit_amt=t.credit_amt
            , credit_status=t.credit_status
            , recorded_on=t.recorded_on
        FROM t
        WHERE client_creditline_history.creditline_id = t.creditline_id
        RETURNING creditline_id
    ),
    i AS (
        INSERT INTO client_creditline_history( client_id,cc_account_id,credit_line_date,credit_amt,credit_status,recorded_on)
        SELECT 
            t.client_id
            , t.cc_account_id
            , t.credit_line_date
            , t.credit_amt
            , t.credit_status
            , t.recorded_on
        FROM t
        WHERE NOT EXISTS ( SELECT 1 FROM u)
    )
    SELECT 'INSERT' as ACTION, creditline_id
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, creditline_id
    FROM u
    ;
    ;
"""
    val = [
            client_creditline_history.creditline_id
            , client_creditline_history.client_id
            , client_creditline_history.cc_account_id
            , client_creditline_history.credit_line_date
            , client_creditline_history.credit_amt
            , client_creditline_history.credit_status
            , client_creditline_history.recorded_on
        ]
    return db.execute(sql, val)

def insert_client_creditline_history( client_creditline_history:ClientCreditlineHistory):
    sql = """
    INSERT INTO client_creditline_history( client_id,cc_account_id,credit_line_date,credit_amt,credit_status,recorded_on)
    VALUES (%s, %s, %s, %s, %s, %s)
    ;
"""
    val = [
            
            client_creditline_history.client_id
            , client_creditline_history.cc_account_id
            , client_creditline_history.credit_line_date
            , client_creditline_history.credit_amt
            , client_creditline_history.credit_status
            , client_creditline_history.recorded_on
        ]
    return db.execute(sql, val)

# this has a flaw in loop.index > 2
def update_client_creditline_history( client_creditline_history:ClientCreditlineHistory):
    sql = """
    UPDATE client_creditline_history
    SET client_id = %s, cc_account_id = %s, credit_line_date = %s, credit_amt = %s, credit_status = %s, recorded_on = %s
    WHERE creditline_id = %s
"""
    val = [client_creditline_history.client_id
            , client_creditline_history.cc_account_id
            , client_creditline_history.credit_line_date
            , client_creditline_history.credit_amt
            , client_creditline_history.credit_status
            , client_creditline_history.recorded_on
        
            , client_creditline_history.creditline_id
            
            
            
            
            
                        
        ]
    return db.execute(sql, val)

#######################
# client_address
#######################
import ClientAddress

def get_client_address():
    sql = """
    SELECT address_id,client_id,address_type,address_1,address_2,city,state,zip,country,valid_from,valid_to,recorded_on
    FROM client_address
"""
    return db.fetchall(sql)

def get_client_address_by_id(id):
    sql = """
    SELECT address_id,client_id,address_type,address_1,address_2,city,state,zip,country,valid_from,valid_to,recorded_on
    FROM client_address
    WHERE address_id = %s
"""
    return db.fetchall(sql, [id])

def get_client_address_by_client_id(client_id):
    sql = """
    SELECT address_id,client_id,address_type,address_1,address_2,city,state,zip,country,valid_from,valid_to,recorded_on
    FROM client_address
    WHERE client_id = %s
"""
    return db.fetchall(sql, [client_id])

def upsert_client_address( client_address:ClientAddress):
    sql = """
    WITH t AS (
        SELECT 
            %s as address_id
            , %s as client_id
            , %s as address_type
            , %s as address_1
            , %s as address_2
            , %s as city
            , %s as state
            , %s as zip
            , %s as country
            , %s as valid_from
            , %s as valid_to
            , %s as recorded_on
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
        RETURNING address_id
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
    )
    SELECT 'INSERT' as ACTION, address_id
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, address_id
    FROM u
    ;
    ;
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
    return db.execute(sql, val)

def insert_client_address( client_address:ClientAddress):
    sql = """
    INSERT INTO client_address( client_id,address_type,address_1,address_2,city,state,zip,country,valid_from,valid_to,recorded_on)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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
    return db.execute(sql, val)

# this has a flaw in loop.index > 2
def update_client_address( client_address:ClientAddress):
    sql = """
    UPDATE client_address
    SET client_id = %s, address_type = %s, address_1 = %s, address_2 = %s, city = %s, state = %s, zip = %s, country = %s, valid_from = %s, valid_to = %s, recorded_on = %s
    WHERE address_id = %s
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
    return db.execute(sql, val)

#######################
# client_setting
#######################
import ClientSetting

def get_client_setting():
    sql = """
    SELECT client_setting_id,client_id,prefix,keyname,keyvalue
    FROM client_setting
"""
    return db.fetchall(sql)

def get_client_setting_by_id(id):
    sql = """
    SELECT client_setting_id,client_id,prefix,keyname,keyvalue
    FROM client_setting
    WHERE client_setting_id = %s
"""
    return db.fetchall(sql, [id])

def get_client_setting_by_client_id(client_id):
    sql = """
    SELECT client_setting_id,client_id,prefix,keyname,keyvalue
    FROM client_setting
    WHERE client_id = %s
"""
    return db.fetchall(sql, [client_id])

def upsert_client_setting( client_setting:ClientSetting):
    sql = """
    WITH t AS (
        SELECT 
            %s as client_setting_id
            , %s as client_id
            , %s as prefix
            , %s as keyname
            , %s as keyvalue
    ),
    u AS (
        UPDATE client_setting
        SET 
            client_id=t.client_id
            , prefix=t.prefix
            , keyname=t.keyname
            , keyvalue=t.keyvalue
        FROM t
        WHERE client_setting.client_setting_id = t.client_setting_id
        RETURNING client_setting_id
    ),
    i AS (
        INSERT INTO client_setting( client_id,prefix,keyname,keyvalue)
        SELECT 
            t.client_id
            , t.prefix
            , t.keyname
            , t.keyvalue
        FROM t
        WHERE NOT EXISTS ( SELECT 1 FROM u)
    )
    SELECT 'INSERT' as ACTION, client_setting_id
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, client_setting_id
    FROM u
    ;
    ;
"""
    val = [
            client_setting.client_setting_id
            , client_setting.client_id
            , client_setting.prefix
            , client_setting.keyname
            , client_setting.keyvalue
        ]
    return db.execute(sql, val)

def insert_client_setting( client_setting:ClientSetting):
    sql = """
    INSERT INTO client_setting( client_id,prefix,keyname,keyvalue)
    VALUES (%s, %s, %s, %s)
    ;
"""
    val = [
            
            client_setting.client_id
            , client_setting.prefix
            , client_setting.keyname
            , client_setting.keyvalue
        ]
    return db.execute(sql, val)

# this has a flaw in loop.index > 2
def update_client_setting( client_setting:ClientSetting):
    sql = """
    UPDATE client_setting
    SET client_id = %s, prefix = %s, keyname = %s, keyvalue = %s
    WHERE client_setting_id = %s
"""
    val = [client_setting.client_id
            , client_setting.prefix
            , client_setting.keyname
            , client_setting.keyvalue
        
            , client_setting.client_setting_id
            
            
            
                        
        ]
    return db.execute(sql, val)

#######################
# client_bank_account
#######################
import ClientBankAccount

def get_client_bank_account():
    sql = """
    SELECT bank_account_id,client_id,bank_name,account_num,routing_num,account_login,account_pwd,account_status,debit_card,debit_info,recorded_on
    FROM client_bank_account
"""
    return db.fetchall(sql)

def get_client_bank_account_by_id(id):
    sql = """
    SELECT bank_account_id,client_id,bank_name,account_num,routing_num,account_login,account_pwd,account_status,debit_card,debit_info,recorded_on
    FROM client_bank_account
    WHERE bank_account_id = %s
"""
    return db.fetchall(sql, [id])

def get_client_bank_account_by_client_id(client_id):
    sql = """
    SELECT bank_account_id,client_id,bank_name,account_num,routing_num,account_login,account_pwd,account_status,debit_card,debit_info,recorded_on
    FROM client_bank_account
    WHERE client_id = %s
"""
    return db.fetchall(sql, [client_id])

def upsert_client_bank_account( client_bank_account:ClientBankAccount):
    sql = """
    WITH t AS (
        SELECT 
            %s as bank_account_id
            , %s as client_id
            , %s as bank_name
            , %s as account_num
            , %s as routing_num
            , %s as account_login
            , %s as account_pwd
            , %s as account_status
            , %s as debit_card
            , %s as debit_info
            , %s as recorded_on
    ),
    u AS (
        UPDATE client_bank_account
        SET 
            client_id=t.client_id
            , bank_name=t.bank_name
            , account_num=t.account_num
            , routing_num=t.routing_num
            , account_login=t.account_login
            , account_pwd=t.account_pwd
            , account_status=t.account_status
            , debit_card=t.debit_card
            , debit_info=t.debit_info
            , recorded_on=t.recorded_on
        FROM t
        WHERE client_bank_account.bank_account_id = t.bank_account_id
        RETURNING bank_account_id
    ),
    i AS (
        INSERT INTO client_bank_account( client_id,bank_name,account_num,routing_num,account_login,account_pwd,account_status,debit_card,debit_info,recorded_on)
        SELECT 
            t.client_id
            , t.bank_name
            , t.account_num
            , t.routing_num
            , t.account_login
            , t.account_pwd
            , t.account_status
            , t.debit_card
            , t.debit_info
            , t.recorded_on
        FROM t
        WHERE NOT EXISTS ( SELECT 1 FROM u)
    )
    SELECT 'INSERT' as ACTION, bank_account_id
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, bank_account_id
    FROM u
    ;
    ;
"""
    val = [
            client_bank_account.bank_account_id
            , client_bank_account.client_id
            , client_bank_account.bank_name
            , client_bank_account.account_num
            , client_bank_account.routing_num
            , client_bank_account.account_login
            , client_bank_account.account_pwd
            , client_bank_account.account_status
            , client_bank_account.debit_card
            , client_bank_account.debit_info
            , client_bank_account.recorded_on
        ]
    return db.execute(sql, val)

def insert_client_bank_account( client_bank_account:ClientBankAccount):
    sql = """
    INSERT INTO client_bank_account( client_id,bank_name,account_num,routing_num,account_login,account_pwd,account_status,debit_card,debit_info,recorded_on)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ;
"""
    val = [
            
            client_bank_account.client_id
            , client_bank_account.bank_name
            , client_bank_account.account_num
            , client_bank_account.routing_num
            , client_bank_account.account_login
            , client_bank_account.account_pwd
            , client_bank_account.account_status
            , client_bank_account.debit_card
            , client_bank_account.debit_info
            , client_bank_account.recorded_on
        ]
    return db.execute(sql, val)

# this has a flaw in loop.index > 2
def update_client_bank_account( client_bank_account:ClientBankAccount):
    sql = """
    UPDATE client_bank_account
    SET client_id = %s, bank_name = %s, account_num = %s, routing_num = %s, account_login = %s, account_pwd = %s, account_status = %s, debit_card = %s, debit_info = %s, recorded_on = %s
    WHERE bank_account_id = %s
"""
    val = [client_bank_account.client_id
            , client_bank_account.bank_name
            , client_bank_account.account_num
            , client_bank_account.routing_num
            , client_bank_account.account_login
            , client_bank_account.account_pwd
            , client_bank_account.account_status
            , client_bank_account.debit_card
            , client_bank_account.debit_info
            , client_bank_account.recorded_on
        
            , client_bank_account.bank_account_id
            
            
            
            
            
            
            
            
            
                        
        ]
    return db.execute(sql, val)

#######################
# client_note
#######################
import ClientNote

def get_client_note():
    sql = """
    SELECT client_note_id,client_id,note,tags,recorded_by,recorded_on
    FROM client_note
"""
    return db.fetchall(sql)

def get_client_note_by_id(id):
    sql = """
    SELECT client_note_id,client_id,note,tags,recorded_by,recorded_on
    FROM client_note
    WHERE client_note_id = %s
"""
    return db.fetchall(sql, [id])

def get_client_note_by_client_id(client_id):
    sql = """
    SELECT client_note_id,client_id,note,tags,recorded_by,recorded_on
    FROM client_note
    WHERE client_id = %s
"""
    return db.fetchall(sql, [client_id])

def upsert_client_note( client_note:ClientNote):
    sql = """
    WITH t AS (
        SELECT 
            %s as client_note_id
            , %s as client_id
            , %s as note
            , %s as tags
            , %s as recorded_by
            , %s as recorded_on
    ),
    u AS (
        UPDATE client_note
        SET 
            client_id=t.client_id
            , note=t.note
            , tags=t.tags
            , recorded_by=t.recorded_by
            , recorded_on=t.recorded_on
        FROM t
        WHERE client_note.client_note_id = t.client_note_id
        RETURNING client_note_id
    ),
    i AS (
        INSERT INTO client_note( client_id,note,tags,recorded_by,recorded_on)
        SELECT 
            t.client_id
            , t.note
            , t.tags
            , t.recorded_by
            , t.recorded_on
        FROM t
        WHERE NOT EXISTS ( SELECT 1 FROM u)
    )
    SELECT 'INSERT' as ACTION, client_note_id
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, client_note_id
    FROM u
    ;
    ;
"""
    val = [
            client_note.client_note_id
            , client_note.client_id
            , client_note.note
            , client_note.tags
            , client_note.recorded_by
            , client_note.recorded_on
        ]
    return db.execute(sql, val)

def insert_client_note( client_note:ClientNote):
    sql = """
    INSERT INTO client_note( client_id,note,tags,recorded_by,recorded_on)
    VALUES (%s, %s, %s, %s, %s)
    ;
"""
    val = [
            
            client_note.client_id
            , client_note.note
            , client_note.tags
            , client_note.recorded_by
            , client_note.recorded_on
        ]
    return db.execute(sql, val)

# this has a flaw in loop.index > 2
def update_client_note( client_note:ClientNote):
    sql = """
    UPDATE client_note
    SET client_id = %s, note = %s, tags = %s, recorded_by = %s, recorded_on = %s
    WHERE client_note_id = %s
"""
    val = [client_note.client_id
            , client_note.note
            , client_note.tags
            , client_note.recorded_by
            , client_note.recorded_on
        
            , client_note.client_note_id
            
            
            
            
                        
        ]
    return db.execute(sql, val)

#######################
# client_charges
#######################
import ClientCharges

def get_client_charges():
    sql = """
    SELECT charge_id,client_id,charge_goal,charged,paid,fees,due_on_day,charge_info,recorded_on
    FROM client_charges
"""
    return db.fetchall(sql)

def get_client_charges_by_id(id):
    sql = """
    SELECT charge_id,client_id,charge_goal,charged,paid,fees,due_on_day,charge_info,recorded_on
    FROM client_charges
    WHERE charge_id = %s
"""
    return db.fetchall(sql, [id])

def get_client_charges_by_client_id(client_id):
    sql = """
    SELECT charge_id,client_id,charge_goal,charged,paid,fees,due_on_day,charge_info,recorded_on
    FROM client_charges
    WHERE client_id = %s
"""
    return db.fetchall(sql, [client_id])

def upsert_client_charges( client_charges:ClientCharges):
    sql = """
    WITH t AS (
        SELECT 
            %s as charge_id
            , %s as client_id
            , %s as charge_goal
            , %s as charged
            , %s as paid
            , %s as fees
            , %s as due_on_day
            , %s as charge_info
            , %s as recorded_on
    ),
    u AS (
        UPDATE client_charges
        SET 
            client_id=t.client_id
            , charge_goal=t.charge_goal
            , charged=t.charged
            , paid=t.paid
            , fees=t.fees
            , due_on_day=t.due_on_day
            , charge_info=t.charge_info
            , recorded_on=t.recorded_on
        FROM t
        WHERE client_charges.charge_id = t.charge_id
        RETURNING charge_id
    ),
    i AS (
        INSERT INTO client_charges( client_id,charge_goal,charged,paid,fees,due_on_day,charge_info,recorded_on)
        SELECT 
            t.client_id
            , t.charge_goal
            , t.charged
            , t.paid
            , t.fees
            , t.due_on_day
            , t.charge_info
            , t.recorded_on
        FROM t
        WHERE NOT EXISTS ( SELECT 1 FROM u)
    )
    SELECT 'INSERT' as ACTION, charge_id
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, charge_id
    FROM u
    ;
    ;
"""
    val = [
            client_charges.charge_id
            , client_charges.client_id
            , client_charges.charge_goal
            , client_charges.charged
            , client_charges.paid
            , client_charges.fees
            , client_charges.due_on_day
            , client_charges.charge_info
            , client_charges.recorded_on
        ]
    return db.execute(sql, val)

def insert_client_charges( client_charges:ClientCharges):
    sql = """
    INSERT INTO client_charges( client_id,charge_goal,charged,paid,fees,due_on_day,charge_info,recorded_on)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ;
"""
    val = [
            
            client_charges.client_id
            , client_charges.charge_goal
            , client_charges.charged
            , client_charges.paid
            , client_charges.fees
            , client_charges.due_on_day
            , client_charges.charge_info
            , client_charges.recorded_on
        ]
    return db.execute(sql, val)

# this has a flaw in loop.index > 2
def update_client_charges( client_charges:ClientCharges):
    sql = """
    UPDATE client_charges
    SET client_id = %s, charge_goal = %s, charged = %s, paid = %s, fees = %s, due_on_day = %s, charge_info = %s, recorded_on = %s
    WHERE charge_id = %s
"""
    val = [client_charges.client_id
            , client_charges.charge_goal
            , client_charges.charged
            , client_charges.paid
            , client_charges.fees
            , client_charges.due_on_day
            , client_charges.charge_info
            , client_charges.recorded_on
        
            , client_charges.charge_id
            
            
            
            
            
            
            
                        
        ]
    return db.execute(sql, val)

#######################
# client_cc_points
#######################
import ClientCcPoints

def get_client_cc_points():
    sql = """
    SELECT cc_points_id,client_id,cc_account_id,sold_to,sold_on,sold_points,price,login,pwd,source_info,recorded_on
    FROM client_cc_points
"""
    return db.fetchall(sql)

def get_client_cc_points_by_id(id):
    sql = """
    SELECT cc_points_id,client_id,cc_account_id,sold_to,sold_on,sold_points,price,login,pwd,source_info,recorded_on
    FROM client_cc_points
    WHERE cc_points_id = %s
"""
    return db.fetchall(sql, [id])

def get_client_cc_points_by_client_id(client_id):
    sql = """
    SELECT cc_points_id,client_id,cc_account_id,sold_to,sold_on,sold_points,price,login,pwd,source_info,recorded_on
    FROM client_cc_points
    WHERE client_id = %s
"""
    return db.fetchall(sql, [client_id])

def upsert_client_cc_points( client_cc_points:ClientCcPoints):
    sql = """
    WITH t AS (
        SELECT 
            %s as cc_points_id
            , %s as client_id
            , %s as cc_account_id
            , %s as sold_to
            , %s as sold_on
            , %s as sold_points
            , %s as price
            , %s as login
            , %s as pwd
            , %s as source_info
            , %s as recorded_on
    ),
    u AS (
        UPDATE client_cc_points
        SET 
            client_id=t.client_id
            , cc_account_id=t.cc_account_id
            , sold_to=t.sold_to
            , sold_on=t.sold_on
            , sold_points=t.sold_points
            , price=t.price
            , login=t.login
            , pwd=t.pwd
            , source_info=t.source_info
            , recorded_on=t.recorded_on
        FROM t
        WHERE client_cc_points.cc_points_id = t.cc_points_id
        RETURNING cc_points_id
    ),
    i AS (
        INSERT INTO client_cc_points( client_id,cc_account_id,sold_to,sold_on,sold_points,price,login,pwd,source_info,recorded_on)
        SELECT 
            t.client_id
            , t.cc_account_id
            , t.sold_to
            , t.sold_on
            , t.sold_points
            , t.price
            , t.login
            , t.pwd
            , t.source_info
            , t.recorded_on
        FROM t
        WHERE NOT EXISTS ( SELECT 1 FROM u)
    )
    SELECT 'INSERT' as ACTION, cc_points_id
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, cc_points_id
    FROM u
    ;
    ;
"""
    val = [
            client_cc_points.cc_points_id
            , client_cc_points.client_id
            , client_cc_points.cc_account_id
            , client_cc_points.sold_to
            , client_cc_points.sold_on
            , client_cc_points.sold_points
            , client_cc_points.price
            , client_cc_points.login
            , client_cc_points.pwd
            , client_cc_points.source_info
            , client_cc_points.recorded_on
        ]
    return db.execute(sql, val)

def insert_client_cc_points( client_cc_points:ClientCcPoints):
    sql = """
    INSERT INTO client_cc_points( client_id,cc_account_id,sold_to,sold_on,sold_points,price,login,pwd,source_info,recorded_on)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ;
"""
    val = [
            
            client_cc_points.client_id
            , client_cc_points.cc_account_id
            , client_cc_points.sold_to
            , client_cc_points.sold_on
            , client_cc_points.sold_points
            , client_cc_points.price
            , client_cc_points.login
            , client_cc_points.pwd
            , client_cc_points.source_info
            , client_cc_points.recorded_on
        ]
    return db.execute(sql, val)

# this has a flaw in loop.index > 2
def update_client_cc_points( client_cc_points:ClientCcPoints):
    sql = """
    UPDATE client_cc_points
    SET client_id = %s, cc_account_id = %s, sold_to = %s, sold_on = %s, sold_points = %s, price = %s, login = %s, pwd = %s, source_info = %s, recorded_on = %s
    WHERE cc_points_id = %s
"""
    val = [client_cc_points.client_id
            , client_cc_points.cc_account_id
            , client_cc_points.sold_to
            , client_cc_points.sold_on
            , client_cc_points.sold_points
            , client_cc_points.price
            , client_cc_points.login
            , client_cc_points.pwd
            , client_cc_points.source_info
            , client_cc_points.recorded_on
        
            , client_cc_points.cc_points_id
            
            
            
            
            
            
            
            
            
                        
        ]
    return db.execute(sql, val)

#######################
# client_cc_balance_transfer
#######################
import ClientCcBalanceTransfer

def get_client_cc_balance_transfer():
    sql = """
    SELECT bal_id,client_id,cc_account_id,due_date,total,credit_line,recorded_on
    FROM client_cc_balance_transfer
"""
    return db.fetchall(sql)

def get_client_cc_balance_transfer_by_id(id):
    sql = """
    SELECT bal_id,client_id,cc_account_id,due_date,total,credit_line,recorded_on
    FROM client_cc_balance_transfer
    WHERE bal_id = %s
"""
    return db.fetchall(sql, [id])

def get_client_cc_balance_transfer_by_client_id(client_id):
    sql = """
    SELECT bal_id,client_id,cc_account_id,due_date,total,credit_line,recorded_on
    FROM client_cc_balance_transfer
    WHERE client_id = %s
"""
    return db.fetchall(sql, [client_id])

def upsert_client_cc_balance_transfer( client_cc_balance_transfer:ClientCcBalanceTransfer):
    sql = """
    WITH t AS (
        SELECT 
            %s as bal_id
            , %s as client_id
            , %s as cc_account_id
            , %s as due_date
            , %s as total
            , %s as credit_line
            , %s as recorded_on
    ),
    u AS (
        UPDATE client_cc_balance_transfer
        SET 
            client_id=t.client_id
            , cc_account_id=t.cc_account_id
            , due_date=t.due_date
            , total=t.total
            , credit_line=t.credit_line
            , recorded_on=t.recorded_on
        FROM t
        WHERE client_cc_balance_transfer.bal_id = t.bal_id
        RETURNING bal_id
    ),
    i AS (
        INSERT INTO client_cc_balance_transfer( client_id,cc_account_id,due_date,total,credit_line,recorded_on)
        SELECT 
            t.client_id
            , t.cc_account_id
            , t.due_date
            , t.total
            , t.credit_line
            , t.recorded_on
        FROM t
        WHERE NOT EXISTS ( SELECT 1 FROM u)
    )
    SELECT 'INSERT' as ACTION, bal_id
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, bal_id
    FROM u
    ;
    ;
"""
    val = [
            client_cc_balance_transfer.bal_id
            , client_cc_balance_transfer.client_id
            , client_cc_balance_transfer.cc_account_id
            , client_cc_balance_transfer.due_date
            , client_cc_balance_transfer.total
            , client_cc_balance_transfer.credit_line
            , client_cc_balance_transfer.recorded_on
        ]
    return db.execute(sql, val)

def insert_client_cc_balance_transfer( client_cc_balance_transfer:ClientCcBalanceTransfer):
    sql = """
    INSERT INTO client_cc_balance_transfer( client_id,cc_account_id,due_date,total,credit_line,recorded_on)
    VALUES (%s, %s, %s, %s, %s, %s)
    ;
"""
    val = [
            
            client_cc_balance_transfer.client_id
            , client_cc_balance_transfer.cc_account_id
            , client_cc_balance_transfer.due_date
            , client_cc_balance_transfer.total
            , client_cc_balance_transfer.credit_line
            , client_cc_balance_transfer.recorded_on
        ]
    return db.execute(sql, val)

# this has a flaw in loop.index > 2
def update_client_cc_balance_transfer( client_cc_balance_transfer:ClientCcBalanceTransfer):
    sql = """
    UPDATE client_cc_balance_transfer
    SET client_id = %s, cc_account_id = %s, due_date = %s, total = %s, credit_line = %s, recorded_on = %s
    WHERE bal_id = %s
"""
    val = [client_cc_balance_transfer.client_id
            , client_cc_balance_transfer.cc_account_id
            , client_cc_balance_transfer.due_date
            , client_cc_balance_transfer.total
            , client_cc_balance_transfer.credit_line
            , client_cc_balance_transfer.recorded_on
        
            , client_cc_balance_transfer.bal_id
            
            
            
            
            
                        
        ]
    return db.execute(sql, val)

#######################
# client_cc_action
#######################
import ClientCcAction

def get_client_cc_action():
    sql = """
    SELECT cc_action_id,client_id,cc_account_id,ccaction,action_type,action_status,due_date,details,recorded_on
    FROM client_cc_action
"""
    return db.fetchall(sql)

def get_client_cc_action_by_id(id):
    sql = """
    SELECT cc_action_id,client_id,cc_account_id,ccaction,action_type,action_status,due_date,details,recorded_on
    FROM client_cc_action
    WHERE cc_action_id = %s
"""
    return db.fetchall(sql, [id])

def get_client_cc_action_by_client_id(client_id):
    sql = """
    SELECT cc_action_id,client_id,cc_account_id,ccaction,action_type,action_status,due_date,details,recorded_on
    FROM client_cc_action
    WHERE client_id = %s
"""
    return db.fetchall(sql, [client_id])

def upsert_client_cc_action( client_cc_action:ClientCcAction):
    sql = """
    WITH t AS (
        SELECT 
            %s as cc_action_id
            , %s as client_id
            , %s as cc_account_id
            , %s as ccaction
            , %s as action_type
            , %s as action_status
            , %s as due_date
            , %s as details
            , %s as recorded_on
    ),
    u AS (
        UPDATE client_cc_action
        SET 
            client_id=t.client_id
            , cc_account_id=t.cc_account_id
            , ccaction=t.ccaction
            , action_type=t.action_type
            , action_status=t.action_status
            , due_date=t.due_date
            , details=t.details
            , recorded_on=t.recorded_on
        FROM t
        WHERE client_cc_action.cc_action_id = t.cc_action_id
        RETURNING cc_action_id
    ),
    i AS (
        INSERT INTO client_cc_action( client_id,cc_account_id,ccaction,action_type,action_status,due_date,details,recorded_on)
        SELECT 
            t.client_id
            , t.cc_account_id
            , t.ccaction
            , t.action_type
            , t.action_status
            , t.due_date
            , t.details
            , t.recorded_on
        FROM t
        WHERE NOT EXISTS ( SELECT 1 FROM u)
    )
    SELECT 'INSERT' as ACTION, cc_action_id
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, cc_action_id
    FROM u
    ;
    ;
"""
    val = [
            client_cc_action.cc_action_id
            , client_cc_action.client_id
            , client_cc_action.cc_account_id
            , client_cc_action.ccaction
            , client_cc_action.action_type
            , client_cc_action.action_status
            , client_cc_action.due_date
            , client_cc_action.details
            , client_cc_action.recorded_on
        ]
    return db.execute(sql, val)

def insert_client_cc_action( client_cc_action:ClientCcAction):
    sql = """
    INSERT INTO client_cc_action( client_id,cc_account_id,ccaction,action_type,action_status,due_date,details,recorded_on)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ;
"""
    val = [
            
            client_cc_action.client_id
            , client_cc_action.cc_account_id
            , client_cc_action.ccaction
            , client_cc_action.action_type
            , client_cc_action.action_status
            , client_cc_action.due_date
            , client_cc_action.details
            , client_cc_action.recorded_on
        ]
    return db.execute(sql, val)

# this has a flaw in loop.index > 2
def update_client_cc_action( client_cc_action:ClientCcAction):
    sql = """
    UPDATE client_cc_action
    SET client_id = %s, cc_account_id = %s, ccaction = %s, action_type = %s, action_status = %s, due_date = %s, details = %s, recorded_on = %s
    WHERE cc_action_id = %s
"""
    val = [client_cc_action.client_id
            , client_cc_action.cc_account_id
            , client_cc_action.ccaction
            , client_cc_action.action_type
            , client_cc_action.action_status
            , client_cc_action.due_date
            , client_cc_action.details
            , client_cc_action.recorded_on
        
            , client_cc_action.cc_action_id
            
            
            
            
            
            
            
                        
        ]
    return db.execute(sql, val)

#######################
# client_cc_transaction
#######################
import ClientCcTransaction

def get_client_cc_transaction():
    sql = """
    SELECT cc_trans_id,client_id,cc_account_id,transaction_date,transaction_type,transaction_status,credit,debit,recorded_on
    FROM client_cc_transaction
"""
    return db.fetchall(sql)

def get_client_cc_transaction_by_id(id):
    sql = """
    SELECT cc_trans_id,client_id,cc_account_id,transaction_date,transaction_type,transaction_status,credit,debit,recorded_on
    FROM client_cc_transaction
    WHERE cc_trans_id = %s
"""
    return db.fetchall(sql, [id])

def get_client_cc_transaction_by_client_id(client_id):
    sql = """
    SELECT cc_trans_id,client_id,cc_account_id,transaction_date,transaction_type,transaction_status,credit,debit,recorded_on
    FROM client_cc_transaction
    WHERE client_id = %s
"""
    return db.fetchall(sql, [client_id])

def upsert_client_cc_transaction( client_cc_transaction:ClientCcTransaction):
    sql = """
    WITH t AS (
        SELECT 
            %s as cc_trans_id
            , %s as client_id
            , %s as cc_account_id
            , %s as transaction_date
            , %s as transaction_type
            , %s as transaction_status
            , %s as credit
            , %s as debit
            , %s as recorded_on
    ),
    u AS (
        UPDATE client_cc_transaction
        SET 
            client_id=t.client_id
            , cc_account_id=t.cc_account_id
            , transaction_date=t.transaction_date
            , transaction_type=t.transaction_type
            , transaction_status=t.transaction_status
            , credit=t.credit
            , debit=t.debit
            , recorded_on=t.recorded_on
        FROM t
        WHERE client_cc_transaction.cc_trans_id = t.cc_trans_id
        RETURNING cc_trans_id
    ),
    i AS (
        INSERT INTO client_cc_transaction( client_id,cc_account_id,transaction_date,transaction_type,transaction_status,credit,debit,recorded_on)
        SELECT 
            t.client_id
            , t.cc_account_id
            , t.transaction_date
            , t.transaction_type
            , t.transaction_status
            , t.credit
            , t.debit
            , t.recorded_on
        FROM t
        WHERE NOT EXISTS ( SELECT 1 FROM u)
    )
    SELECT 'INSERT' as ACTION, cc_trans_id
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, cc_trans_id
    FROM u
    ;
    ;
"""
    val = [
            client_cc_transaction.cc_trans_id
            , client_cc_transaction.client_id
            , client_cc_transaction.cc_account_id
            , client_cc_transaction.transaction_date
            , client_cc_transaction.transaction_type
            , client_cc_transaction.transaction_status
            , client_cc_transaction.credit
            , client_cc_transaction.debit
            , client_cc_transaction.recorded_on
        ]
    return db.execute(sql, val)

def insert_client_cc_transaction( client_cc_transaction:ClientCcTransaction):
    sql = """
    INSERT INTO client_cc_transaction( client_id,cc_account_id,transaction_date,transaction_type,transaction_status,credit,debit,recorded_on)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ;
"""
    val = [
            
            client_cc_transaction.client_id
            , client_cc_transaction.cc_account_id
            , client_cc_transaction.transaction_date
            , client_cc_transaction.transaction_type
            , client_cc_transaction.transaction_status
            , client_cc_transaction.credit
            , client_cc_transaction.debit
            , client_cc_transaction.recorded_on
        ]
    return db.execute(sql, val)

# this has a flaw in loop.index > 2
def update_client_cc_transaction( client_cc_transaction:ClientCcTransaction):
    sql = """
    UPDATE client_cc_transaction
    SET client_id = %s, cc_account_id = %s, transaction_date = %s, transaction_type = %s, transaction_status = %s, credit = %s, debit = %s, recorded_on = %s
    WHERE cc_trans_id = %s
"""
    val = [client_cc_transaction.client_id
            , client_cc_transaction.cc_account_id
            , client_cc_transaction.transaction_date
            , client_cc_transaction.transaction_type
            , client_cc_transaction.transaction_status
            , client_cc_transaction.credit
            , client_cc_transaction.debit
            , client_cc_transaction.recorded_on
        
            , client_cc_transaction.cc_trans_id
            
            
            
            
            
            
            
                        
        ]
    return db.execute(sql, val)

#######################
# client_email
#######################
import ClientEmail

def get_client_email():
    sql = """
    SELECT id,client_id,emailtype,email,isdefault,isconfirmed,recorded_on
    FROM client_email
"""
    return db.fetchall(sql)

def get_client_email_by_id(id):
    sql = """
    SELECT id,client_id,emailtype,email,isdefault,isconfirmed,recorded_on
    FROM client_email
    WHERE id = %s
"""
    return db.fetchall(sql, [id])

def get_client_email_by_client_id(client_id):
    sql = """
    SELECT id,client_id,emailtype,email,isdefault,isconfirmed,recorded_on
    FROM client_email
    WHERE client_id = %s
"""
    return db.fetchall(sql, [client_id])

def upsert_client_email( client_email:ClientEmail):
    sql = """
    WITH t AS (
        SELECT 
            %s as id
            , %s as client_id
            , %s as emailtype
            , %s as email
            , %s as isdefault
            , %s as isconfirmed
            , %s as recorded_on
    ),
    u AS (
        UPDATE client_email
        SET 
            client_id=t.client_id
            , emailtype=t.emailtype
            , email=t.email
            , isdefault=t.isdefault
            , isconfirmed=t.isconfirmed
            , recorded_on=t.recorded_on
        FROM t
        WHERE client_email.id = t.id
        RETURNING id
    ),
    i AS (
        INSERT INTO client_email( client_id,emailtype,email,isdefault,isconfirmed,recorded_on)
        SELECT 
            t.client_id
            , t.emailtype
            , t.email
            , t.isdefault
            , t.isconfirmed
            , t.recorded_on
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
            client_email.id
            , client_email.client_id
            , client_email.emailtype
            , client_email.email
            , client_email.isdefault
            , client_email.isconfirmed
            , client_email.recorded_on
        ]
    return db.execute(sql, val)

def insert_client_email( client_email:ClientEmail):
    sql = """
    INSERT INTO client_email( client_id,emailtype,email,isdefault,isconfirmed,recorded_on)
    VALUES (%s, %s, %s, %s, %s, %s)
    ;
"""
    val = [
            
            client_email.client_id
            , client_email.emailtype
            , client_email.email
            , client_email.isdefault
            , client_email.isconfirmed
            , client_email.recorded_on
        ]
    return db.execute(sql, val)

# this has a flaw in loop.index > 2
def update_client_email( client_email:ClientEmail):
    sql = """
    UPDATE client_email
    SET client_id = %s, emailtype = %s, email = %s, isdefault = %s, isconfirmed = %s, recorded_on = %s
    WHERE id = %s
"""
    val = [client_email.client_id
            , client_email.emailtype
            , client_email.email
            , client_email.isdefault
            , client_email.isconfirmed
            , client_email.recorded_on
        
            , client_email.id
            
            
            
            
            
                        
        ]
    return db.execute(sql, val)

#######################
# client_self_lender
#######################
import ClientSelfLender

def get_client_self_lender():
    sql = """
    SELECT self_lender_id,client_id,start_date,duration,pay_from,monthly_due_date,termination_date,login,pwd,recorded_on
    FROM client_self_lender
"""
    return db.fetchall(sql)

def get_client_self_lender_by_id(id):
    sql = """
    SELECT self_lender_id,client_id,start_date,duration,pay_from,monthly_due_date,termination_date,login,pwd,recorded_on
    FROM client_self_lender
    WHERE self_lender_id = %s
"""
    return db.fetchall(sql, [id])

def get_client_self_lender_by_client_id(client_id):
    sql = """
    SELECT self_lender_id,client_id,start_date,duration,pay_from,monthly_due_date,termination_date,login,pwd,recorded_on
    FROM client_self_lender
    WHERE client_id = %s
"""
    return db.fetchall(sql, [client_id])

def upsert_client_self_lender( client_self_lender:ClientSelfLender):
    sql = """
    WITH t AS (
        SELECT 
            %s as self_lender_id
            , %s as client_id
            , %s as start_date
            , %s as duration
            , %s as pay_from
            , %s as monthly_due_date
            , %s as termination_date
            , %s as login
            , %s as pwd
            , %s as recorded_on
    ),
    u AS (
        UPDATE client_self_lender
        SET 
            client_id=t.client_id
            , start_date=t.start_date
            , duration=t.duration
            , pay_from=t.pay_from
            , monthly_due_date=t.monthly_due_date
            , termination_date=t.termination_date
            , login=t.login
            , pwd=t.pwd
            , recorded_on=t.recorded_on
        FROM t
        WHERE client_self_lender.self_lender_id = t.self_lender_id
        RETURNING self_lender_id
    ),
    i AS (
        INSERT INTO client_self_lender( client_id,start_date,duration,pay_from,monthly_due_date,termination_date,login,pwd,recorded_on)
        SELECT 
            t.client_id
            , t.start_date
            , t.duration
            , t.pay_from
            , t.monthly_due_date
            , t.termination_date
            , t.login
            , t.pwd
            , t.recorded_on
        FROM t
        WHERE NOT EXISTS ( SELECT 1 FROM u)
    )
    SELECT 'INSERT' as ACTION, self_lender_id
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, self_lender_id
    FROM u
    ;
    ;
"""
    val = [
            client_self_lender.self_lender_id
            , client_self_lender.client_id
            , client_self_lender.start_date
            , client_self_lender.duration
            , client_self_lender.pay_from
            , client_self_lender.monthly_due_date
            , client_self_lender.termination_date
            , client_self_lender.login
            , client_self_lender.pwd
            , client_self_lender.recorded_on
        ]
    return db.execute(sql, val)

def insert_client_self_lender( client_self_lender:ClientSelfLender):
    sql = """
    INSERT INTO client_self_lender( client_id,start_date,duration,pay_from,monthly_due_date,termination_date,login,pwd,recorded_on)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ;
"""
    val = [
            
            client_self_lender.client_id
            , client_self_lender.start_date
            , client_self_lender.duration
            , client_self_lender.pay_from
            , client_self_lender.monthly_due_date
            , client_self_lender.termination_date
            , client_self_lender.login
            , client_self_lender.pwd
            , client_self_lender.recorded_on
        ]
    return db.execute(sql, val)

# this has a flaw in loop.index > 2
def update_client_self_lender( client_self_lender:ClientSelfLender):
    sql = """
    UPDATE client_self_lender
    SET client_id = %s, start_date = %s, duration = %s, pay_from = %s, monthly_due_date = %s, termination_date = %s, login = %s, pwd = %s, recorded_on = %s
    WHERE self_lender_id = %s
"""
    val = [client_self_lender.client_id
            , client_self_lender.start_date
            , client_self_lender.duration
            , client_self_lender.pay_from
            , client_self_lender.monthly_due_date
            , client_self_lender.termination_date
            , client_self_lender.login
            , client_self_lender.pwd
            , client_self_lender.recorded_on
        
            , client_self_lender.self_lender_id
            
            
            
            
            
            
            
            
                        
        ]
    return db.execute(sql, val)
