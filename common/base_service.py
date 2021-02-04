import sys
import json

def repository_call( func):
    def with_repository_call(*args, **kwargs):
        try:
            df = func(*args, **kwargs)
            dfjson = df.to_json(orient="records", date_format="iso")
            data = json.loads(dfjson)
            return { 'rc': 1, 'msg': 'Success', 'data': data}
        except Exception as e:
            print( sys.exc_info()[1])
            raise e
    return with_repository_call

# print( 'base_service')