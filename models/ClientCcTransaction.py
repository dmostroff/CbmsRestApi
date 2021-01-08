from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ClientCcTransaction(BaseModel):
    cc_trans_id: int
    client_id: int
    cc_account_id: int
    transaction_date: datetime
    transaction_type: str
    transaction_status: str
    credit: int
    debit: int
    recorded_on: datetime
    