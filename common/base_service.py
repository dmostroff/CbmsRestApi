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

def repository_call_single_row( func):
    def with_repository_call(*args, **kwargs):
        try:
            df = func(*args, **kwargs)
            if df is not None and not df.empty:
                dfjson = df.to_json(orient="records", date_format="iso")
                data = json.loads(dfjson)
                return { 'rc': 1, 'msg': 'Success', 'data': data[0]}
            else:
                return { 'rc': 0, 'msg': 'No data', 'data': None}
        except Exception as e:
            print( sys.exc_info()[1])
            raise e
    return with_repository_call
# print( 'base_service')

def repository_call_single_row_data_only( func):
    def with_repository_call(*args, **kwargs):
        try:
            df = func(*args, **kwargs)
            if df is not None:
                dfjson = df.to_json(orient="records", date_format="iso")
                data = json.loads(dfjson)
                return data[0] if len(data) > 0 else None
            else:
                return None
        except Exception as e:
            print( sys.exc_info()[1])
            raise e
    return with_repository_call
