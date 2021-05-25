from flask import request
from flask_restful import Resource
import client_service as cs
import cc_account_service as cas
from client_transform import ClientPersonJsonToModel

class Client(Resource):
    def get(self, id):
        client_person = cs.get_client_person_data(id)
        cc_account = cas.get_cc_account_data_by_client(id)
        data = { 'person': client_person, 'cc_account': cc_account }
        return { 'rc': 1, 'msg': 'Success', 'data': data}
