from flask import request
from flask_restful import Resource
import client_service as cs

clientPerson = {}
class ClientPersons(Resource):
    def get(self):
        return cs.get_client_persons()

class ClientCreditSummary(Resource):
    def get(self):
        return cs.get_client_credit_summary()
class ClientPerson(Resource):
    def get(self, id):
        return cs.get_client_person_by_client_id(id)

    def put(self, id):
        clientPerson[id] = request.form['clientPerson']
        return {'client_id': clientPerson[id]}

print( 'clientperson_resource')