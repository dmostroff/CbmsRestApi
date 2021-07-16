from flask import request
from flask_restful import Resource
import client_service as cs
import cc_account_service as cas
import client_bank_account_service as cbas
import cc_account_todo_service as cats

from client_transform import ClientPersonJsonToModel, clientData

class Client(Resource):
    def get(self, id):
        client_person = cs.get_client_person_data(id)
        credit_summary = cs.get_client_credit_summary_by_client( id)
        addresses = cs.get_client_address_by_client (id)
        cc_accounts = cas.get_cc_account_data_by_client(id)
        bank_accounts = cbas.get_client_bank_account_by_client (id)
        cc_account_todo = cats.get_cc_account_todo_by_client(id)
        # bt = cs.get_client_cc_balance_transfer_by_client_id (id)
        data = clientData( person = client_person,
            credit_summary = credit_summary,
            addresses = addresses,
            bank_accounts = bank_accounts,
            cc_accounts = cc_accounts,
            cc_account_todo = cc_account_todo
            # , balance_transfer = bt
            )
        return { 'rc': 1, 'msg': 'Success', 'data': data}
