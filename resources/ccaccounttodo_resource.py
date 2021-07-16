from flask import request
from flask_restful import Resource
import cc_account_todo_service as cs
from client_transform import CcAccountTodoJsonToModel

class CcAccountTodos(Resource):
    def get(self):
        return cs.get_cc_account_todos()

class CcAccountTodoByClient(Resource):
    def get(self, client_id):
        return cs.get_cc_account_todo_by_client(client_id)

class CcAccountTodoByCcAccount(Resource):
    def get(self, cc_account_id):
        return cs.get_cc_account_todo_by_cc_account(cc_account_id)

class CcAccountTodo(Resource):
    def get(self, id):
        return cs.get_cc_account_todo(id)

class CcAccountTodoPost(Resource):
    def post(self):
        cc_account_todo = CcAccountTodoJsonToModel(request.get_json())
        return cs.post_cc_account_todo( cc_account_todo)
