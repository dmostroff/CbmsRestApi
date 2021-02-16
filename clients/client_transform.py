from ClientPersonModel import ClientPersonModel
from CcAccountModel import CcAccountModel
from ClientBankAccountModel import ClientBankAccountModel


def JsonToModel():
    pass

def ClientPersonJsonToModel( client_person_json: str) -> ClientPersonModel:
    retval = ClientPersonModel.parse_obj( client_person_json)
    return retval

def CcAccountJsonToModel( cc_account_json: str) -> CcAccountModel:
    retval = CcAccountModel.parse_obj( cc_account_json)
    return retval

def ClientBankAccountJsonToModel( client_back_account_json: str) -> ClientBankAccountModel:
    retval = ClientBankAccountModel.parse_obj( client_back_account_json)
    return retval
