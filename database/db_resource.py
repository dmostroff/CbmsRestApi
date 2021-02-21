from flask_restful import Resource
import db_service as ds

class DatabaseInfo(Resource):
    def get(self, name):
        funcs = {
            'database': ds.get_database_name,
            'version': ds.get_version,
            'conn': ds.get_connection_info,
            'server': ds.get_server_name
        }
        if name in funcs:
            return {name: funcs[name]() }, 200
        return None, 404

