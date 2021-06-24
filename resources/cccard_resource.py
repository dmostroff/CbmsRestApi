from flask import request
from flask_restful import Resource
import cc_card_service as cs
from creditcards_transform import CcCardModelJsonToModel

class CcCards(Resource):
    def get(self):
        return cs.get_cc_cards()

class CcCard(Resource):
    def get(self, id):
        return cs.get_cc_card(id)

class CcCardPost(Resource):
    def post(self, id):
        cc_card = CcCardModelJsonToModel(request.get_json())
        return cs.post_cc_card( cc_card )