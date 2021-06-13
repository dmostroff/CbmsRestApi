from flask_restful import Resource
import cc_company_service as cs

class CcCompanies(Resource):
    def get(self):
        return cs.get_cc_companies()

class CcCompany(Resource):
    def get(self, id):
        return cs.get_cc_company(id)

class CcCompanyPost(Resource):
    def post(self, id):
        cc_company = CcCompanyJsonToModel(request.get_json())
        return cs.upsert_( )