import client_repository as cr
import common_service as cs

def get_clients():
    clients = cr.get_clientpersons()
    return cs.df_to_dict(clients)

def get_clientperson( id):
    client = cr.get_clientperson_by_id( id)
    return cs.df_to_dict(client)[0] if client.shape[0] > 0 is not None else None

