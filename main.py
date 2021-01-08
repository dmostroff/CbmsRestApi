import os
import sys
from typing import Optional

from fastapi import Body, FastAPI
from enum import Enum

rootDir = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
for subdir in ['common', 'database', 'models', 'clients']:
    sys.path.append( os.path.join(rootDir, subdir))


app = FastAPI()

import client_service as cs
import client_resource as cr

@app.get('/')
def read_main():
    return { 'msg': 'Welcome to CBMS'}

#-- ClientCcHistory
import ClientCcHistory
@app.get('/client/cc_history')
def get_client_cc_history ():
    return cs.get_client_cc_history()

@app.get('/client/cc_history/{id}')
def get_client_cc_history_by_id (id):
    return cs.get_client_cc_history_by_id(id)

@app.post('/client/cc_history')
async def post_client_cc_history ( client_cc_history:ClientCcHistory.ClientCcHistory):
    return cs.upsert_client_cc_history(client_cc_history)


#-- ClientPerson
import ClientPerson
@app.get('/client/person')
async def get_client_person ():
    return cs.get_client_person()

@app.get('/client/person/{id}')
def get_client_person_by_id (id):
    return cs.get_client_person_by_id(id)

@app.post('/client/person')
def post_client_person ( client_person:ClientPerson.ClientPerson):
    return cs.upsert_client_person(client_person)


#-- ClientCreditlineHistory
import ClientCreditlineHistory
@app.get('/client/creditline_history')
def get_client_creditline_history ():
    return cs.get_client_creditline_history()

@app.get('/client/creditline_history/{id}')
def get_client_creditline_history_by_id (id):
    return cs.get_client_creditline_history_by_id(id)

@app.post('/client/creditline_history')
def post_client_creditline_history ( client_creditline_history:ClientCreditlineHistory.ClientCreditlineHistory):
    return cs.upsert_client_creditline_history(client_creditline_history)


#-- ClientAddress
import ClientAddress
@app.get('/client/address')
def get_client_address ():
    return cs.get_client_address()

@app.get('/client/address/{id}')
def get_client_address_by_id (id):
    return cs.get_client_address_by_id(id)

@app.post('/client/address')
def post_client_address ( client_address:ClientAddress.ClientAddress):
    return cs.upsert_client_address(client_address)


#-- ClientCcAccount
import ClientCcAccount
@app.get('/client/cc_account')
def get_client_cc_account ():
    return cs.get_client_cc_account()

@app.get('/client/cc_account/{id}')
def get_client_cc_account_by_id (id):
    return cs.get_client_cc_account_by_id(id)

@app.post('/client/cc_account')
def post_client_cc_account ( client_cc_account:ClientCcAccount.ClientCcAccount):
    return cs.upsert_client_cc_account(client_cc_account)


#-- ClientSetting
import ClientSetting
@app.get('/client/setting')
def get_client_setting ():
    return cs.get_client_setting()

@app.get('/client/setting/{id}')
def get_client_setting_by_id (id):
    return cs.get_client_setting_by_id(id)

@app.post('/client/setting')
def post_client_setting ( client_setting:ClientSetting.ClientSetting):
    return cs.upsert_client_setting(client_setting)


#-- ClientBankAccount
import ClientBankAccount
@app.get('/client/bank_account')
def get_client_bank_account ():
    return cs.get_client_bank_account()

@app.get('/client/bank_account/{id}')
def get_client_bank_account_by_id (id):
    return cs.get_client_bank_account_by_id(id)

@app.post('/client/bank_account')
def post_client_bank_account ( client_bank_account:ClientBankAccount.ClientBankAccount):
    return cs.upsert_client_bank_account(client_bank_account)


#-- ClientNote
import ClientNote
@app.get('/client/note')
def get_client_note ():
    return cs.get_client_note()

@app.get('/client/note/{id}')
def get_client_note_by_id (id):
    return cs.get_client_note_by_id(id)

@app.post('/client/note')
def post_client_note ( client_note:ClientNote.ClientNote):
    return cs.upsert_client_note(client_note)


#-- ClientCcPoints
import ClientCcPoints
@app.get('/client/cc_points')
def get_client_cc_points ():
    return cs.get_client_cc_points()

@app.get('/client/cc_points/{id}')
def get_client_cc_points_by_id (id):
    return cs.get_client_cc_points_by_id(id)

@app.post('/client/cc_points')
def post_client_cc_points ( client_cc_points:ClientCcPoints.ClientCcPoints):
    return cs.upsert_client_cc_points(client_cc_points)


#-- ClientCharges
import ClientCharges
@app.get('/client/charges')
def get_client_charges ():
    return cs.get_client_charges()

@app.get('/client/charges/{id}')
def get_client_charges_by_id (id):
    return cs.get_client_charges_by_id(id)

@app.post('/client/charges')
def post_client_charges ( client_charges:ClientCharges.ClientCharges):
    return cs.upsert_client_charges(client_charges)


#-- ClientCcBalanceTransfer
import ClientCcBalanceTransfer
@app.get('/client/cc_balance_transfer')
def get_client_cc_balance_transfer ():
    return cs.get_client_cc_balance_transfer()

@app.get('/client/cc_balance_transfer/{id}')
def get_client_cc_balance_transfer_by_id (id):
    return cs.get_client_cc_balance_transfer_by_id(id)

@app.post('/client/cc_balance_transfer')
def post_client_cc_balance_transfer ( client_cc_balance_transfer:ClientCcBalanceTransfer.ClientCcBalanceTransfer):
    return cs.upsert_client_cc_balance_transfer(client_cc_balance_transfer)


#-- ClientCcAction
import ClientCcAction
@app.get('/client/cc_action')
def get_client_cc_action ():
    return cs.get_client_cc_action()

@app.get('/client/cc_action/{id}')
def get_client_cc_action_by_id (id):
    return cs.get_client_cc_action_by_id(id)

@app.post('/client/cc_action')
def post_client_cc_action ( client_cc_action:ClientCcAction.ClientCcAction):
    return cs.upsert_client_cc_action(client_cc_action)


#-- ClientSelfLender
import ClientSelfLender
@app.get('/client/self_lender')
def get_client_self_lender ():
    return cs.get_client_self_lender()

@app.get('/client/self_lender/{id}')
def get_client_self_lender_by_id (id):
    return cs.get_client_self_lender_by_id(id)

@app.post('/client/self_lender')
def post_client_self_lender ( client_self_lender:ClientSelfLender.ClientSelfLender):
    return cs.upsert_client_self_lender(client_self_lender)


#-- ClientCcTransaction
import ClientCcTransaction
@app.get('/client/cc_transaction')
def get_client_cc_transaction ():
    return cs.get_client_cc_transaction()

@app.get('/client/cc_transaction/{id}')
def get_client_cc_transaction_by_id (id):
    return cs.get_client_cc_transaction_by_id(id)

@app.post('/client/cc_transaction')
def post_client_cc_transaction ( client_cc_transaction:ClientCcTransaction.ClientCcTransaction):
    return cs.upsert_client_cc_transaction(client_cc_transaction)
