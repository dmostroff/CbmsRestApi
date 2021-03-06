import os
import sys
from typing import Optional
import socket

from flask_cors import CORS
from flask_restful import Api

if 'APACHE_RUN_DIR' in os.environ.keys():
    from cbmsapi import app
else:
    from flask import current_app as app

print( 'router BEGIN')
CORS(app)
api = Api(app)


import user_login_service as uls
from user_login_resource import UserLogin
from auth_user_resource import AuthUsers, AuthUser
from auth_user_setting_resource import AuthUserSetting, AuthUserSettingByPrefix, AuthUserSettingPost
from auth_role_resource import AuthRoles, AuthRole, AuthRolePost
from adm_setting_resource import AdmSettings, AdmSettingByPrefix, AdmSetting, AdmSettingPost

from cbmssummary_resource import CBMSSummary

from client_resource import Client
from clientperson_resource import ClientCreditSummary, ClientPersons, ClientPerson, ClientPersonPost
from ccaccount_resource import CcAccounts, CcAccountsByClient, CcAccount, CcAccountPost
from ccaccounttodo_resource import CcAccountTodos, CcAccountTodoByClient, CcAccountTodoByCcAccount, CcAccountTodo, CcAccountTodoPost
from clientbankaccount_resource import ClientBankAccounts, ClientBankAccountsByClient, ClientBankAccount, ClientBankAccountPost

from cccard_resource import CcCards, CcCard
from cccompany_resource import CcCompanies, CcCompanies, CcCompany, CcCompanyPost
from db_resource import DatabaseInfo

@app.before_request
def check_jwt_token():
    pass

@staticmethod
def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
        
# Using an `after_request` callback, we refresh any token that is within 30
# minutes of expiring. Change the timedeltas to match the needs of your application.
# @app.after_request
# def refresh_expiring_jwts(response):
#     try:
#         exp_timestamp = get_jwt()["exp"]
#         now = datetime.now(timezone.utc)
#         target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
#         if target_timestamp > exp_timestamp:
#             access_token = create_access_token(identity=get_jwt_identity())
#             set_access_cookies(response, access_token)
#         return response
#     except (RuntimeError, KeyError):
#         # Case where there is not a valid JWT. Just return the original respone
#         return response


@app.route('/', methods=['GET'])
def read_main():
    return { 'msg': 'Welcome to CBMS', 'version': os.getenv('API_VERSION')}

@app.route('/ping', methods=['GET'])
def ping():
    return { 'ping': socket.gethostname()}

@app.route('/version', methods=['GET'])
def version():
    return { 'version': os.getenv('API_VERSION')}

#-- Login
api.add_resource( UserLogin, '/onboard/<string:name>')
#-- Auth Users
api.add_resource( AuthUsers, '/auth/users')
api.add_resource( AuthUser, '/auth/user/<int:id>')
#-- UserSettings
api.add_resource( AuthUserSettingByPrefix, '/user/setting/<int:user_id>/<string:prefix>')
api.add_resource( AuthUserSetting, '/user/setting/<int:id>')
api.add_resource( AuthUserSettingPost, '/user/setting')
#-- Roles
api.add_resource( AuthRoles, '/auth/roles')
api.add_resource( AuthRole, '/auth/role/<int:id>')
api.add_resource( AuthRolePost, '/auth/role')

#-- Settings
api.add_resource( AdmSettings, '/adm/settings')
api.add_resource( AdmSettingByPrefix, '/adm/setting/<string:prefix>')
api.add_resource( AdmSetting, '/adm/setting/<int:id>')
api.add_resource( AdmSettingPost, '/adm/setting')

#-- CBMS Summary
api.add_resource( CBMSSummary, '/cbms/summary')

#-- Client
api.add_resource( Client, '/client/<int:id>')

#-- ClientPerson
api.add_resource( ClientCreditSummary, '/creditsummary')
api.add_resource( ClientPersons, '/clients')
api.add_resource( ClientPerson, '/client/person/<int:id>')
api.add_resource( ClientPersonPost, '/client/person')

api.add_resource( CcAccounts, '/ccaccounts')
api.add_resource( CcAccountsByClient, '/client/<int:client_id>/ccaccount')
api.add_resource( CcAccount, '/ccaccount/<int:id>')
api.add_resource( CcAccountPost, '/ccaccount')

#-- Client CC Account to do
api.add_resource( CcAccountTodos, '/ccaccounttodos')
api.add_resource( CcAccountTodoByClient, '/client/<int:client_id>/ccaccounttodo')
api.add_resource( CcAccountTodoByCcAccount, '/ccaccount/<int:cc_account_id>/todo')
api.add_resource( CcAccountTodo, '/ccaccounttodo/<int:id>')
api.add_resource( CcAccountTodoPost, '/ccaccounttodo')

#-- ClientBankAcc
api.add_resource( ClientBankAccounts, '/bankaccounts')
api.add_resource( ClientBankAccountsByClient, '/client/<int:client_id>/bankaccount')
api.add_resource( ClientBankAccount, '/bankaccount/<int:id>')
api.add_resource( ClientBankAccountPost, '/bankaccount')

#-- Credit Cards
api.add_resource( CcCards, '/creditcards')
api.add_resource( CcCard, '/creditcard/<int:id>')
api.add_resource( CcCompanies, '/cccompanies')
api.add_resource( CcCompany, '/cccompany/<int:id>')
api.add_resource( CcCompanyPost, '/cccompany')


#-- Database
api.add_resource( DatabaseInfo, '/db/<string:name>')


print( 'router DONE')


#-- ClientCcHistory
# from ClientCcHistory import ClientCcHistory
# @app.route('/client/cc_history', methods=['GET'])
# def get_client_cc_history ():
#     return cs.get_client_cc_history()

# @app.route('/client/{client_id}/cc_history', methods=['GET'])
# def get_client_cc_history_by_client_id (client_id):
#     return cs.get_client_cc_history_by_client_id(client_id)

# @app.route('/client/cc_history/<id>', methods=['GET'])
# def get_client_cc_history_by_id (id):
#     return cs.get_client_cc_history_by_id(id)

# @app.route('/client/cc_history', methods=['POST'])
# def post_client_cc_history ( client_cc_history:ClientCcHistory):
#     return cs.upsert_client_cc_history(client_cc_history)


# # @app.route('/client/person', methods=['GET'])
# # def get_client_person ():
# #     return cs.get_client_person()

# # @app.route('/client/<client_id>/person', methods=['GET'])
# # def get_client_person_by_client_id (client_id):
# #     return cs.get_client_person_by_client_id(client_id)

# # @app.route('/client/person/<id>', methods=['GET'])
# # def get_client_person_by_id (id):
# #     return cs.get_client_person_by_id(id)

# # @app.route('/client/person', methods=['POST'])
# # def post_client_person ( client_person:ClientPerson):
# #     return cs.upsert_client_person(client_person)


# #-- ClientCreditlineHistory
# from ClientCreditlineHistory import ClientCreditlineHistory
# @app.route('/client/creditline_history', methods=['GET'])
# def get_client_creditline_history ():
#     return cs.client_creditline_history()

# @app.route('/client/{client_id}/creditline_history', methods=['GET'])
# def get_client_creditline_history_by_client_id (client_id):
#     return cs.client_creditline_history_by_client_id(client_id)

# @app.route('/client/creditline_history/<id>', methods=['GET'])
# def get_client_creditline_history_by_id (id):
#     return cs.client_creditline_history_by_id(id)

# @app.route('/client/creditline_history', methods=['POST'])
# def post_client_creditline_history ( client_creditline_history:ClientCreditlineHistory):
#     return cs.upsert_client_creditline_history(client_creditline_history)


# #-- ClientAddress
# from ClientAddress import ClientAddress
# @app.route('/client/address', methods=['GET'])
# def get_client_address ():
#     return cs.client_address()

# @app.route('/client/{client_id}/address', methods=['GET'])
# def get_client_address_by_client_id (client_id):
#     return cs.client_address_by_client_id(client_id)

# @app.route('/client/address/<id>', methods=['GET'])
# def get_client_address_by_id (id):
#     return cs.client_address_by_id(id)

# @app.route('/client/address', methods=['POST'])
# def post_client_address ( client_address:ClientAddress):
#     return cs.upsert_client_address(client_address)


# #-- ClientCcAccount
# from CcAccount import CcAccount
# @app.route('/client/cc_account', methods=['GET'])
# def get_cc_account ():
#     return cs.cc_account()

# @app.route('/client/{client_id}/cc_account', methods=['GET'])
# def get_cc_account_by_client_id (client_id):
#     return cs.cc_account_by_client_id(client_id)

# @app.route('/client/cc_account/<id>', methods=['GET'])
# def get_cc_account_by_id (id):
#     return cs.cc_account_by_id(id)

# @app.route('/client/cc_account', methods=['POST'])
# def post_cc_account ( cc_account:CcAccount):
#     return cs.upsert_cc_account(cc_account)


# #-- ClientSettingclie
# from ClientSetting import ClientSetting
# @app.route('/client/setting', methods=['GET'])
# def get_client_setting ():
#     return cs.client_setting()

# @app.route('/client/{client_id}/setting', methods=['GET'])
# def get_client_setting_by_client_id (client_id):
#     return cs.client_setting_by_client_id(client_id)

# @app.route('/client/setting/<id>', methods=['GET'])
# def get_client_setting_by_id (id):
#     return cs.client_setting_by_id(id)

# @app.route('/client/setting', methods=['POST'])
# def post_client_setting ( client_setting:ClientSetting):
#     return cs.upsert_client_setting(client_setting)


# #-- ClientBankAccount
# from ClientBankAccount import ClientBankAccount
# @app.route('/client/bank_account', methods=['GET'])
# def get_client_bank_account ():
#     return cs.client_bank_account()

# @app.route('/client/{client_id}/bank_account', methods=['GET'])
# def get_client_bank_account_by_client_id (client_id):
#     return cs.client_bank_account_by_client_id(client_id)

# @app.route('/client/bank_account/<id>', methods=['GET'])
# def get_client_bank_account_by_id (id):
#     return cs.client_bank_account_by_id(id)

# @app.route('/client/bank_account', methods=['POST'])
# def post_client_bank_account ( client_bank_account:ClientBankAccount):
#     return cs.upsert_client_bank_account(client_bank_account)


# #-- ClientNote
# from ClientNote import ClientNote
# @app.route('/client/note', methods=['GET'])
# def get_client_note ():
#     return cs.client_note()

# @app.route('/client/{client_id}/note', methods=['GET'])
# def get_client_note_by_client_id (client_id):
#     return cs.client_note_by_client_id(client_id)

# @app.route('/client/note/<id>', methods=['GET'])
# def get_client_note_by_id (id):
#     return cs.client_note_by_id(id)

# @app.route('/client/note', methods=['POST'])
# def post_client_note ( client_note:ClientNote):
#     return cs.upsert_client_note(client_note)


# #-- ClientCcPoints
# from ClientCcPoints import ClientCcPoints
# @app.route('/client/cc_points', methods=['GET'])
# def get_client_cc_points ():
#     return cs.client_cc_points()

# @app.route('/client/{client_id}/cc_points', methods=['GET'])
# def get_client_cc_points_by_client_id (client_id):
#     return cs.client_cc_points_by_client_id(client_id)

# @app.route('/client/cc_points/<id>', methods=['GET'])
# def get_client_cc_points_by_id (id):
#     return cs.client_cc_points_by_id(id)

# @app.route('/client/cc_points', methods=['POST'])
# def post_client_cc_points ( client_cc_points:ClientCcPoints):
#     return cs.upsert_client_cc_points(client_cc_points)


# #-- ClientCharges
# from ClientCharges import ClientCharges
# @app.route('/client/charges', methods=['GET'])
# def get_client_charges ():
#     return cs.client_charges()

# @app.route('/client/{client_id}/charges', methods=['GET'])
# def get_client_charges_by_client_id (client_id):
#     return cs.client_charges_by_client_id(client_id)

# @app.route('/client/charges/<id>', methods=['GET'])
# def get_client_charges_by_id (id):
#     return cs.client_charges_by_id(id)

# @app.route('/client/charges', methods=['POST'])
# def post_client_charges ( client_charges:ClientCharges):
#     return cs.upsert_client_charges(client_charges)


# #-- ClientCcBalanceTransfer
# from ClientCcBalanceTransfer import ClientCcBalanceTransfer
# @app.route('/client/cc_balance_transfer', methods=['GET'])
# def get_client_cc_balance_transfer ():
#     return cs.client_cc_balance_transfer()

# @app.route('/client/{client_id}/cc_balance_transfer', methods=['GET'])
# def get_client_cc_balance_transfer_by_client_id (client_id):
#     return cs.client_cc_balance_transfer_by_client_id(client_id)

# @app.route('/client/cc_balance_transfer/<id>', methods=['GET'])
# def get_client_cc_balance_transfer_by_id (id):
#     return cs.client_cc_balance_transfer_by_id(id)

# @app.route('/client/cc_balance_transfer', methods=['POST'])
# def post_client_cc_balance_transfer ( client_cc_balance_transfer:ClientCcBalanceTransfer):
#     return cs.upsert_client_cc_balance_transfer(client_cc_balance_transfer)


# #-- ClientCcAction
# from ClientCcAction import ClientCcAction
# @app.route('/client/cc_action', methods=['GET'])
# def get_client_cc_action ():
#     return cs.client_cc_action()

# @app.route('/client/{client_id}/cc_action', methods=['GET'])
# def get_client_cc_action_by_client_id (client_id):
#     return cs.client_cc_action_by_client_id(client_id)

# @app.route('/client/cc_action/<id>', methods=['GET'])
# def get_client_cc_action_by_id (id):
#     return cs.client_cc_action_by_id(id)

# @app.route('/client/cc_action', methods=['POST'])
# def post_client_cc_action ( client_cc_action:ClientCcAction):
#     return cs.upsert_client_cc_action(client_cc_action)


# #-- ClientSelfLender
# from ClientSelfLender import ClientSelfLender
# @app.route('/client/self_lender', methods=['GET'])
# def get_client_self_lender ():
#     return cs.client_self_lender()

# @app.route('/client/{client_id}/self_lender', methods=['GET'])
# def get_client_self_lender_by_client_id (client_id):
#     return cs.client_self_lender_by_client_id(client_id)

# @app.route('/client/self_lender/<id>', methods=['GET'])
# def get_client_self_lender_by_id (id):
#     return cs.client_self_lender_by_id(id)

# @app.route('/client/self_lender', methods=['POST'])
# def post_client_self_lender ( client_self_lender:ClientSelfLender):
#     return cs.upsert_client_self_lender(client_self_lender)


# #-- ClientCcTransaction
# from ClientCcTransaction import ClientCcTransaction
# @app.route('/client/cc_transaction', methods=['GET'])
# def get_client_cc_transaction ():
#     return cs.client_cc_transaction()

# @app.route('/client/{client_id}/cc_transaction', methods=['GET'])
# def get_client_cc_transaction_by_client_id (client_id):
#     return cs.client_cc_transaction_by_client_id(client_id)

# @app.route('/client/cc_transaction/<id>', methods=['GET'])
# def get_client_cc_transaction_by_id (id):
#     return cs.client_cc_transaction_by_id(id)

# @app.route('/client/cc_transaction', methods=['POST'])
# def post_client_cc_transaction ( client_cc_transaction:ClientCcTransaction):
#     return cs.upsert_client_cc_transaction(client_cc_transaction)

