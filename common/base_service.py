import sys
import common_service as cs

def repository_call( func):
    def with_repository_call(*args, **kwargs):
        try:
            df = func(*args, **kwargs)
            return cs.df_to_dict(df)
        except Exception as e:
            print( sys.exc_info()[1])
            raise e
    return with_repository_call
