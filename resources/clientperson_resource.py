from flask import request
from flask_restful import Resource
import client_service as cs
import cc_account_service as cas
from client_transform import ClientPersonJsonToModel

clientPerson = {}
class ClientPersons(Resource):
    def get(self):
        return cs.get_client_persons()

class ClientCreditSummary(Resource):
    def get(self):
        return cs.get_client_credit_summary()

class ClientPerson(Resource):
    def get(self, id):
        client_person = cs.get_client_person_by_id(id)
        client_account = cas.get_cc_account_by_client_id(id)
        # if client_account['rc'] == 1:
        #     retval['']
        return client_account

    def post( self):
        client_person = ClientPersonJsonToModel(request.get_json())
        return cs.post_client_person( client_person)

    def delete(self):
        return cs.delete_client_person_by_id(id)

class ClientPersonPost(Resource):
    def post(self):
        client_person = ClientPersonJsonToModel(request.get_json())
        return cs.post_client_person( client_person)
