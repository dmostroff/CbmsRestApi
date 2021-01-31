# settings.py
import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
#load_dotenv()

# OR, the same with increased verbosity
# load_dotenv(verbose=True)

print( "settings")
print( os.path.dirname(__file__))
print( os.getenv('CONNECTION_STRING'))
print( os.getenv('API_VERSION'))
print( "end settings")
