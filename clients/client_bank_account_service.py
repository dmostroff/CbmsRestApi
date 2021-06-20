import numpy as np
import client_bank_account_repository as cr
import base_service as bs
from ClientBankAccountModel import ClientBankAccountModel

#--------------------
# client_bank_account
#--------------------

@bs.repository_call
def get_client_bank_accounts ():
    return cr.get_client_bank_accounts()

# @bs.repository_call
# def get_client_bank_account_by_client_bank_account_id (client_bank_account_id):
#     return cr.get_client_bank_account_by_client_bank_account_id(client_bank_account_id)

@bs.repository_call_data
def get_client_bank_account_by_client_id (client_id):
    return cr.get_client_bank_account_by_client_id(client_id)

@bs.repository_call_single_row
def get_client_bank_account_by_id (id):
    return cr.get_client_bank_account_by_id(id)

@bs.repository_call_single_row
def upsert_client_bank_account ( client_bank_account:ClientBankAccountModel):
    return cr.upsert_client_bank_account(client_bank_account)

