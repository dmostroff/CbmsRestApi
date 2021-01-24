import client_repository as cr
import cc_account_repository as car
import base_service as bs
import common_service as cs

#--------------------
# client_cc_history
#--------------------
from ClientCcHistory import ClientCcHistory

@bs.repository_call
def get_client_cc_history ():
    return cr.get_client_cc_history()

@bs.repository_call
def get_client_cc_history_by_client_id (client_id):
    return cr.get_client_cc_history_by_client_id(client_id)

@bs.repository_call
def get_client_cc_history_by_id (id):
    return cr.get_client_cc_history_by_id(id)

@bs.repository_call
def post_client_cc_history ( client_cc_history:ClientCcHistory):
    return cr.upsert_client_cc_history(client_cc_history)

@bs.repository_call
def put_client_cc_history (client_cc_history:ClientCcHistory):
    return cr.insert_client_cc_history(client_cc_history)

#--------------------
# client_person
#--------------------
from ClientPerson import ClientPerson

@bs.repository_call
def get_client_person ():
    return cr.get_client_person()

@bs.repository_call
def get_client_person_by_client_id (client_id):
    return cr.get_client_person_by_client_id(client_id)

@bs.repository_call
def get_client_person_by_id (id):
    return cr.get_client_person_by_id(id)

@bs.repository_call
def post_client_person ( client_person:ClientPerson):
    return cr.upsert_client_person(client_person)

@bs.repository_call
def put_client_person (client_person:ClientPerson):
    return cr.insert_client_person(client_person)

#--------------------
# client_creditline_history
#--------------------
from ClientCreditlineHistory import ClientCreditlineHistory

@bs.repository_call
def get_client_creditline_history ():
    return cr.get_client_creditline_history()

@bs.repository_call
def get_client_creditline_history_by_client_id (client_id):
    return cr.get_client_creditline_history_by_client_id(client_id)

@bs.repository_call
def get_client_creditline_history_by_id (id):
    return cr.get_client_creditline_history_by_id(id)

@bs.repository_call
def post_client_creditline_history ( client_creditline_history:ClientCreditlineHistory):
    return cr.upsert_client_creditline_history(client_creditline_history)

@bs.repository_call
def put_client_creditline_history (client_creditline_history:ClientCreditlineHistory):
    return cr.insert_client_creditline_history(client_creditline_history)

#--------------------
# client_address
#--------------------
from ClientAddress import ClientAddress

@bs.repository_call
def get_client_address ():
    return cr.get_client_address()

@bs.repository_call
def get_client_address_by_client_id (client_id):
    return cr.get_client_address_by_client_id(client_id)

@bs.repository_call
def get_client_address_by_id (id):
    return cr.get_client_address_by_id(id)

@bs.repository_call
def post_client_address ( client_address:ClientAddress):
    return cr.upsert_client_address(client_address)

@bs.repository_call
def put_client_address (client_address:ClientAddress):
    return cr.insert_client_address(client_address)


#--------------------
# cc_account
#--------------------
from CcAccount import CcAccount

@bs.repository_call
def get_cc_account ():
    return car.get_cc_account()

@bs.repository_call
def get_cc_account_by_client_id (client_id):
    return car.get_by_client_id(client_id)

@bs.repository_call
def get_cc_account_by_id (id):
    return car.get_cc_account_by_id(id)

@bs.repository_call
def post_cc_account ( cc_account:CcAccount):
    return car.upsert_cc_account(cc_account)

@bs.repository_call
def put_cc_account (cc_account:CcAccount):
    return car.insert_cc_account(cc_account)

#--------------------
# client_setting
#--------------------
from ClientSetting import ClientSetting

@bs.repository_call
def get_client_setting ():
    return cr.get_client_setting()

@bs.repository_call
def get_client_setting_by_client_id (client_id):
    return cr.get_client_setting_by_client_id(client_id)

@bs.repository_call
def get_client_setting_by_id (id):
    df = cr.get_client_setting_by_id(id)
    return df

@bs.repository_call
def post_client_setting ( client_setting:ClientSetting):
    return cr.upsert_client_setting(client_setting)

@bs.repository_call
def put_client_setting (client_setting:ClientSetting):
    return cr.insert_client_setting(client_setting)

#--------------------
# client_bank_account
#--------------------
from ClientBankAccount import ClientBankAccount

@bs.repository_call
def get_client_bank_account ():
    return cr.get_client_bank_account()

@bs.repository_call
def get_client_bank_account_by_client_id (client_id):
    return cr.get_client_bank_account_by_client_id(client_id)

@bs.repository_call
def get_client_bank_account_by_id (id):
    return cr.get_client_bank_account_by_id(id)

@bs.repository_call
def post_client_bank_account ( client_bank_account:ClientBankAccount):
    return cr.upsert_client_bank_account(client_bank_account)

@bs.repository_call
def put_client_bank_account (client_bank_account:ClientBankAccount):
    return cr.insert_client_bank_account(client_bank_account)

#--------------------
# client_note
#--------------------
from ClientNote import ClientNote

@bs.repository_call
def get_client_note ():
    return cr.get_client_note()

@bs.repository_call
def get_client_note_by_client_id (client_id):
    return cr.get_client_note_by_client_id(client_id)

@bs.repository_call
def get_client_note_by_id (id):
    return cr.get_client_note_by_id(id)

@bs.repository_call
def post_client_note ( client_note:ClientNote):
    return cr.upsert_client_note(client_note)

@bs.repository_call
def put_client_note (client_note:ClientNote):
    return cr.insert_client_note(client_note)


#--------------------
# client_cc_points
#--------------------
from ClientCcPoints import ClientCcPoints

@bs.repository_call
def get_client_cc_points ():
    return cr.get_client_cc_points()

@bs.repository_call
def get_client_cc_points_by_client_id (client_id):
    return cr.get_client_cc_points_by_client_id(client_id)

@bs.repository_call
def get_client_cc_points_by_id (id):
    return cr.get_client_cc_points_by_id(id)

@bs.repository_call
def post_client_cc_points ( client_cc_points:ClientCcPoints):
    return cr.upsert_client_cc_points(client_cc_points)

@bs.repository_call
def put_client_cc_points (client_cc_points:ClientCcPoints):
    return cr.insert_client_cc_points(client_cc_points)


#--------------------
# client_charges
#--------------------
from ClientCharges import ClientCharges

@bs.repository_call
def get_client_charges ():
    return cr.get_client_charges()

@bs.repository_call
def get_client_charges_by_client_id (client_id):
    return cr.get_client_charges_by_client_id(client_id)

@bs.repository_call
def get_client_charges_by_id (id):
    return cr.get_client_charges_by_id(id)

@bs.repository_call
def post_client_charges ( client_charges:ClientCharges):
    return cr.upsert_client_charges(client_charges)

@bs.repository_call
def put_client_charges (client_charges:ClientCharges):
    return cr.insert_client_charges(client_charges)


#--------------------
# client_cc_balance_transfer
#--------------------
from ClientCcBalanceTransfer import ClientCcBalanceTransfer

@bs.repository_call
def get_client_cc_balance_transfer ():
    return cr.get_client_cc_balance_transfer()

@bs.repository_call
def get_client_cc_balance_transfer_by_client_id (client_id):
    return cr.get_client_cc_balance_transfer_by_client_id(client_id)

@bs.repository_call
def get_client_cc_balance_transfer_by_id (id):
    return cr.get_client_cc_balance_transfer_by_id(id)

@bs.repository_call
def post_client_cc_balance_transfer ( client_cc_balance_transfer:ClientCcBalanceTransfer):
    return cr.upsert_client_cc_balance_transfer(client_cc_balance_transfer)

@bs.repository_call
def put_client_cc_balance_transfer (client_cc_balance_transfer:ClientCcBalanceTransfer):
    return cr.insert_client_cc_balance_transfer(client_cc_balance_transfer)


#--------------------
# client_cc_action
#--------------------
from ClientCcAction import ClientCcAction

@bs.repository_call
def get_client_cc_action ():
    return cr.get_client_cc_action()

@bs.repository_call
def get_client_cc_action_by_client_id (client_id):
    return cr.get_client_cc_action_by_client_id(client_id)

@bs.repository_call
def get_client_cc_action_by_id (id):
    return cr.get_client_cc_action_by_id(id)

@bs.repository_call
def post_client_cc_action ( client_cc_action:ClientCcAction):
    return cr.upsert_client_cc_action(client_cc_action)

@bs.repository_call
def put_client_cc_action (client_cc_action:ClientCcAction):
    return cr.insert_client_cc_action(client_cc_action)


#--------------------
# client_self_lender
#--------------------
from ClientSelfLender import ClientSelfLender

@bs.repository_call
def get_client_self_lender ():
    return cr.get_client_self_lender()

@bs.repository_call
def get_client_self_lender_by_client_id (client_id):
    return cr.get_client_self_lender_by_client_id(client_id)

@bs.repository_call
def get_client_self_lender_by_id (id):
    return cr.get_client_self_lender_by_id(id)

@bs.repository_call
def post_client_self_lender ( client_self_lender:ClientSelfLender):
    return cr.upsert_client_self_lender(client_self_lender)

@bs.repository_call
def put_client_self_lender (client_self_lender:ClientSelfLender):
    return cr.insert_client_self_lender(client_self_lender)


#--------------------
# client_cc_transaction
#--------------------
from ClientCcTransaction import ClientCcTransaction

@bs.repository_call
def get_client_cc_transaction ():
    return cr.get_client_cc_transaction()

@bs.repository_call
def get_client_cc_transaction_by_client_id (client_id):
    return cr.get_client_cc_transaction_by_client_id(client_id)

@bs.repository_call
def get_client_cc_transaction_by_id (id):
    return cr.get_client_cc_transaction_by_id(id)

@bs.repository_call
def post_client_cc_transaction ( client_cc_transaction:ClientCcTransaction):
    return cr.upsert_client_cc_transaction(client_cc_transaction)

@bs.repository_call
def put_client_cc_transaction (client_cc_transaction:ClientCcTransaction):
    return cr.insert_client_cc_transaction(client_cc_transaction)

