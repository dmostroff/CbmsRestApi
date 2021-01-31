import pgsql_db_layer as db


#######################
# client_person
#######################
from ClientPerson import ClientPerson

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

print( 'client_repository')