from flask import jsonify
import os
import json
from cryptography.fernet import Fernet


def init_environ(app, config):
    os.environ['CONNECTION_STRING'] = config['MSSQL']['CONNECTION_STRING']
    # os.environ['UPLOAD_DIR'] = config['System']['UPLOAD_DIR']
    # os.environ['ADD_TO_REF_TABLES'] = config['System']['ADD_TO_REF_TABLES']

    for k in config['System']: os.environ[k] = config['System'][k]
    # fix up the ADD_TO_REF_TABLES to be 1 or 0
    os.environ['ADD_TO_REF_TABLES'] = '1' if os.getenv('ADD_TO_REF_TABLES') == 'True' else '0'
    app.config['ALLOWED_EXTENSIONS'] = { 'xlsx', 'csv' }
    app.config['SECRET_KEY'] = config['System']['SECRET_KEY']

def json_rc_msg( rc = 0, msg = '', data=None, retstatus=200):
    retval = { 'rc': rc }
    if msg is not None and len(msg) > 0: retval['msg'] = msg
    # print( data, type(data))
    if isinstance( data, str):
        data = { 'data': data}
    if data is not None:
        retval = { **retval, **data }
    return retval
    
def df_to_dict( df):
    dfjson =  df_to_json(df)
    return json.loads(dfjson)

def df_to_json( df):
    return df.to_json(orient="records", date_format="iso")

def df_to_json_pretty( df):
    dfjson =  df_to_json(df)
    parsed = json.loads(dfjson)
    return json.dumps(parsed, indent=4)

def json_view( df):
    return jsonify(json.loads(df_to_json(df)) if df is not None else {})

def decrypt( encoded_string):
    key = os.getenv('KEY')
    cipher_suite = Fernet(key)
    return cipher_suite.decrypt( bytes(encoded_string, 'utf-8'))

def encrypt( decoded_string):
    key = os.getenv('KEY')
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt( bytes(decoded_string, 'utf-8'))

