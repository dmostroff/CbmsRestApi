import client_repository as cr
import base_service as bs
import common_service as cs

#--------------------
# dashboard
#--------------------
@bs.repository_call
def get_client_credit_summary():
    return cr.get_client_credit_summary()
    
#--------------------
# client_cc_history
#--------------------
from ClientCcHistoryModel import ClientCcHistoryModel

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
def post_client_cc_history ( client_cc_history:ClientCcHistoryModel):
    return cr.upsert_client_cc_history(client_cc_history)

@bs.repository_call
def put_client_cc_history (client_cc_history:ClientCcHistoryModel):
    return cr.insert_client_cc_history(client_cc_history)

#--------------------
# client_person
#--------------------
from ClientPersonModel import ClientPersonModel

@bs.repository_call
def get_client_persons ():
    return cr.get_client_persons()

@bs.repository_call
def get_client_person_by_client_id (client_id):
    return cr.get_client_person_by_client_id(client_id)

@bs.repository_call
def get_client_person_by_id (id):
    return cr.get_client_person_by_id(id)

@bs.repository_call
def post_client_person ( client_person:ClientPersonModel):
    return cr.upsert_client_person(client_person)

@bs.repository_call
def put_client_person (client_person:ClientPersonModel):
    return cr.insert_client_person(client_person)

#--------------------
# client_creditline_history
#--------------------
from ClientCreditlineHistoryModel import ClientCreditlineHistoryModel

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
def post_client_creditline_history ( client_creditline_history:ClientCreditlineHistoryModel):
    return cr.upsert_client_creditline_history(client_creditline_history)

@bs.repository_call
def put_client_creditline_history (client_creditline_history:ClientCreditlineHistoryModel):
    return cr.insert_client_creditline_history(client_creditline_history)

#--------------------
# client_address
#--------------------
from ClientAddressModel import ClientAddressModel

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
def post_client_address ( client_address:ClientAddressModel):
    return cr.upsert_client_address(client_address)

@bs.repository_call
def put_client_address (client_address:ClientAddressModel):
    return cr.insert_client_address(client_address)


#--------------------
# client_setting
#--------------------
from ClientSettingModel import ClientSettingModel

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
def post_client_setting ( client_setting:ClientSettingModel):
    return cr.upsert_client_setting(client_setting)

@bs.repository_call
def put_client_setting (client_setting:ClientSettingModel):
    return cr.insert_client_setting(client_setting)

#--------------------
# client_bank_account
#--------------------
from ClientBankAccountModel import ClientBankAccountModel

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
def post_client_bank_account ( client_bank_account:ClientBankAccountModel):
    return cr.upsert_client_bank_account(client_bank_account)

@bs.repository_call
def put_client_bank_account (client_bank_account:ClientBankAccountModel):
    return cr.insert_client_bank_account(client_bank_account)

#--------------------
# client_note
#--------------------
from ClientNoteModel import ClientNoteModel

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
def post_client_note ( client_note:ClientNoteModel):
    return cr.upsert_client_note(client_note)

@bs.repository_call
def put_client_note (client_note:ClientNoteModel):
    return cr.insert_client_note(client_note)


#--------------------
# client_cc_points
#--------------------
from ClientCcPointsModel import ClientCcPointsModel

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
def post_client_cc_points ( client_cc_points:ClientCcPointsModel):
    return cr.upsert_client_cc_points(client_cc_points)

@bs.repository_call
def put_client_cc_points (client_cc_points:ClientCcPointsModel):
    return cr.insert_client_cc_points(client_cc_points)


#--------------------
# client_charges
#--------------------
from ClientChargesModel import ClientChargesModel

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
def post_client_charges ( client_charges:ClientChargesModel):
    return cr.upsert_client_charges(client_charges)

@bs.repository_call
def put_client_charges (client_charges:ClientChargesModel):
    return cr.insert_client_charges(client_charges)


#--------------------
# client_cc_balance_transfer
#--------------------
from ClientCcBalanceTransferModel import ClientCcBalanceTransferModel

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
def post_client_cc_balance_transfer ( client_cc_balance_transfer:ClientCcBalanceTransferModel):
    return cr.upsert_client_cc_balance_transfer(client_cc_balance_transfer)

@bs.repository_call
def put_client_cc_balance_transfer (client_cc_balance_transfer:ClientCcBalanceTransferModel):
    return cr.insert_client_cc_balance_transfer(client_cc_balance_transfer)


#--------------------
# client_cc_action
#--------------------
from ClientCcActionModel import ClientCcActionModel

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
def post_client_cc_action ( client_cc_action:ClientCcActionModel):
    return cr.upsert_client_cc_action(client_cc_action)

@bs.repository_call
def put_client_cc_action (client_cc_action:ClientCcActionModel):
    return cr.insert_client_cc_action(client_cc_action)


#--------------------
# client_self_lender
#--------------------
from ClientSelfLenderModel import ClientSelfLenderModel

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
def post_client_self_lender ( client_self_lender:ClientSelfLenderModel):
    return cr.upsert_client_self_lender(client_self_lender)

@bs.repository_call
def put_client_self_lender (client_self_lender:ClientSelfLenderModel):
    return cr.insert_client_self_lender(client_self_lender)


#--------------------
# client_cc_transaction
#--------------------
from ClientCcTransactionModel import ClientCcTransactionModel

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
def post_client_cc_transaction ( client_cc_transaction:ClientCcTransactionModel):
    return cr.upsert_client_cc_transaction(client_cc_transaction)

@bs.repository_call
def put_client_cc_transaction (client_cc_transaction:ClientCcTransactionModel):
    return cr.insert_client_cc_transaction(client_cc_transaction)

