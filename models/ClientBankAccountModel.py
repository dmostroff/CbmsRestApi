from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ClientBankAccountModel(BaseModel):
    bank_account_id: int
    client_id: int
    bank_name: str
    account_num: str
    routing_num: Optional[str] = None
    account_login: Optional[str] = None
    account_pwd: Optional[str] = None
    account_status: Optional[str] = None
    debit_card: Optional[str] = None
    debit_info: Optional[str] = None
    recorded_on: datetime
    