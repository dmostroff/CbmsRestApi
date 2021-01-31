import os
import sys

# from fastapi import Body, FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.middleware.wsgi import WSGIMiddleware
# from flask import Flask

rootDir = os.path.dirname(__file__)
print ( f"In app: RootDir is '{rootDir}'")
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# for subdir in ['common', 'database', 'resources', 'models', 'clients']:
#     sys.path.append( os.path.join(rootDir, subdir))

print ( __name__)
# app = Flask(__name__)
# app.json_encoder = CustomJSONEncoder

# if __name__ == "__main__":
#     app.run(debug=True)


# @app.route('/', methods=['GET'])
# def read_main():
#     return { 'msg': 'Welcome to CBMS temp 1'}

# set_permissions(app)
# app.wsgi_app = middleware(app.wsgi_app)

# app.url_map.strict_slashes = False
# origins = [
#     'http://localhost',
#     'http://localhost:8080',
# ]

print( 'app DONE')

