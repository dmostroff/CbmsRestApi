from flask_restful import Resource
import cc_card_service as cs

class CcCards(Resource):
    def get(self):
        return cs.get_cc_cards()

class CcCard(Resource):
    def get(self, id):
        return cs.get_cc_card(id)

class CcCardPost(Resource):
    def post(self, id):
        cc_card = CcCardJsonToModel(request.get_json())
        return cs.upsert_( )