from flask import Flask, request
from flask_restful import Api, Resource
import os
import sys
from flask_cors import CORS

rootDir = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
for subdir in ['common', 'database', 'clients']:
    sys.path.append( os.path.join(rootDir, subdir))

import client_resource as client
import db_resource as dbr

app = Flask(__name__)
api = Api(app)


api.add_resource( client.ClientPerson, '/client/<id>')
api.add_resource( client.ClientPersonList, '/clients')
api.add_resource( dbr.DatabaseInfo, '/db/<string:name>')

if __name__ == "__main__":
    app.run(port=5000)

