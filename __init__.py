import os
import sys
import socket

from flask import Flask
from flask_cors import CORS

rootDir = os.path.join( os.path.dirname(__file__), "static")
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print ( f"In app: RootDir is '{rootDir}' {ROOT_DIR}")
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append( rootDir)
for subdir in ['common', 'database', 'resources', 'models', 'clients']:
    sys.path.append( os.path.join(rootDir, subdir))

app= Flask(__name__)
CORS(app)

if __name__ == "__main__":
	app.run()

app.url_map.strict_slashes = False

import cbmsapi.router
# print( 'import client_service')
# import client_service as cs
# print( 'import clientperson_resource')
# from clientperson_resource import ClientPersons, ClientPerson
# print( 'import ccaccount_resource')
# from ccaccount_resource import CcAccounts, CcAccountsByClient, CcAccount
# print( 'import DONE')
