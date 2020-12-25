from flask_restful import Resource
import db_repository as dr

class DatabaseInfo(Resource):
    def get(self, name):
        funcs = {
            'database': dr.get_database_name,
            'version': dr.get_version
        }
        if name in funcs:
            return {name: funcs[name]() }, 200
        return None, 404

