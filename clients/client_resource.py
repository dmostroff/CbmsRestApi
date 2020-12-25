from flask_restful import Resource
import client_service as cps
import common_service as cs

class ClientPersonList(Resource):
    def get(self):
        clients = cps.get_clients()
        return {'clients': clients}, 200

class ClientPerson(Resource):
    def get(self, id):
        client = cps.get_clientperson(id)
        msg = "Success" if client is not None else "Error"
        data = { "client": client} if client is not None else "Not found"
        return cs.json_rc_msg( 0, msg, data)

    # def post(self, name):
    #     existing_client = self._find_client(name)
    #     if existing_client is not None:
    #         return { 'message': 'Client already created'}, 409
    #     data = request.get_json()
    #     new_client = { "name": name, "dob": data['dob'] }

    #     clients.append(new_client)
    #     return {'client': new_client}

