from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ClientBankAccountModel(BaseModel):
    id: int
    client_id: int
    bank_name: str
    account_num: str
    routing_num: Optional[str] = None
    branch_num: Optional[str] = None
    iban: Optional[str] = None
    country: Optional[str] = None
    account_login: Optional[str] = None
    account_pwd: Optional[str] = None
    account_status: Optional[str] = None
    debit_card: Optional[str] = None
    debit_info: Optional[str] = None
    recorded_on: datetime
    