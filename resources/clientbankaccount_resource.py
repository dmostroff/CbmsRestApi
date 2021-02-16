from flask import request
from flask_restful import Resource
import client_bank_account_service as cbas
from client_transform import ClientBankAccountJsonToModel


class ClientBankAccounts(Resource):
    def get(self):
        return cbas.get_client_bank_accounts()

class ClientBankAccountsByClient(Resource):
    def get(self, client_id):
        return cbas.get_client_bank_account_by_client_id(client_id)

class ClientBankAccount(Resource):
    def get(self, id):
        return cbas.get_client_bank_account_by_id(id)

class ClientBankAccountPost(Resource):
    def post(self):
        client_bank_account = ClientBankAccountJsonToModel(request.get_json())
        return cbas.upsert_client_bank_account( client_bank_account)
