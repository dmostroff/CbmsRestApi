import os
import sys
import socket

from flask import Flask

isApache = 'APACHE_RUN_DIR' in os.environ.keys()

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# for k in os.environ.keys():
#     print ( f"{k}="+os.getenv(k))


pathRootDir = os.path.join( os.path.dirname(__file__), "static") if isApache else os.path.dirname(__file__)

print ( f"In app: pathRootDir is '{pathRootDir}'; ROOT_DIR: '{ROOT_DIR}'")
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append( pathRootDir)
for subdir in ['admin', 'common', 'database', 'resources', 'models', 'clients']:
    sys.path.append( os.path.join(pathRootDir, subdir))

app= Flask(__name__)

if __name__ == "__main__":
	app.run()

app.url_map.strict_slashes = False

if isApache:
    import cbmsapi.static.router
else:
    with app.app_context():
        import router
