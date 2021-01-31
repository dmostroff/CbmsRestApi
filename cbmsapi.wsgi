#!/usr/bin/python

print( 'start')
import os
import sys
# import logging
# logging.basicConfig(stream=sys.stderr)
# logging.info('in wsgi')
sys.path.insert(0,"/var/www/FLASKAPPS/")

rootDir = os.path.dirname(__file__)
print(rootDir)
print( sys.path)
import app as application
print ( 'WSGI Done')
