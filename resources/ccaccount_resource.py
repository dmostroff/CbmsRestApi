from flask import request
from flask_restful import Resource
import cc_account_service as cas

print( "in ccaccount_resource")
ccAccount = {}
class CcAccounts(Resource):
    def get(self):
        return cas.get_cc_account()

class CcAccountsByClient(Resource):
    def get(self, client_id):
        return cas.get_cc_account_by_client_id(client_id)

class CcAccount(Resource):
    def get(self, id):
        return cas.get_cc_account_by_id(id)

    def put(self, id):
        ccAccount[id] = request.form['ccAccount']
        return {'ccAccount_id': ccAccount[id]}