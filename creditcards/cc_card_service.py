import numpy as np
import cc_card_repository as cr
import base_service as bs

from CcCardModel import CcCardModel



#--------------------
# cc_card
#--------------------

@bs.repository_call
def get_cc_cards ():
    return cr.get_cc_cards()

# @bs.repository_call
# def get_cc_card_by_cc_card_id (cc_card_id):
#     return cr.get_cc_card_by_cc_card_id(cc_card_id)

@bs.repository_call_single_row
def get_cc_card (id):
    return cr.get_cc_card_by_id(id)

def upsert_cc_card ( cc_card:CcCardModel):
    df = cr.upsert_cc_card(cc_card)
    id = np.int64(df['cc_card_id'].values[0]).item()
    return get_cc_card_by_id(id)

