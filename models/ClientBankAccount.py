from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ClientBankAccount(BaseModel):
    bank_account_id: int
    client_id: int
    bank_name: str
    account_num: str
    routing_num: str
    account_login: str
    account_pwd: str
    account_status: str
    debit_card: str
    debit_info: str
    recorded_on: datetime
    