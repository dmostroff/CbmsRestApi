import cc_account_repository as car
import base_service as bs

#--------------------
# cc_account
#--------------------
from CcAccountModel import CcAccountModel

@bs.repository_call
def get_cc_account ():
    return car.get_cc_account()

@bs.repository_call
def get_cc_account_by_client_id (client_id):
    return car.get_cc_account_by_client_id(client_id)

@bs.repository_call
def get_cc_account_by_id (id):
    return car.get_cc_account_by_id(id)

@bs.repository_call
def post_cc_account ( cc_account:CcAccountModel):
    return car.upsert_cc_account(cc_account)

@bs.repository_call
def put_cc_account (cc_account:CcAccountModel):
    return car.insert_cc_account(cc_account)

#--------------------
# cc_account_promo
#--------------------
from CcAccountPromoModel import CcAccountPromoModel

@bs.repository_call
def get_cc_account_promo ():
    return car.get_cc_account_promo()

@bs.repository_call
def get_cc_account_promo_by_cc_account_id (cc_account_id):
    return car.get_cc_account_promo_by_cc_account_id(cc_account_id)

@bs.repository_call
def get_cc_account_promo_by_id (id):
    return car.get_cc_account_promo_by_id(id)

@bs.repository_call
def post_cc_account_promo ( cc_account_promo:CcAccountPromoModel):
    return car.upsert_cc_account_promo(cc_account_promo)

@bs.repository_call
def put_cc_account_promo (cc_account_promo:CcAccountPromoModel):
    return car.insert_cc_account_promo(cc_account_promo)


