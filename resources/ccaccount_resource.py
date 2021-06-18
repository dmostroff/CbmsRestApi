from flask import request
from flask_restful import Resource
import cc_account_service as cas
from client_transform import CcAccountJsonToModel

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

class CcAccountPost(Resource):
    def post(self):
        cc_account = CcAccountJsonToModel(request.get_json())
        return cas.post_cc_account( cc_account)
# print( "ccaccount_resource")
