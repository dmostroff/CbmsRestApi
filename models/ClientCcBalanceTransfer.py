from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ClientCcBalanceTransfer(BaseModel):
    bal_id: int
    client_id: int
    cc_account_id: int
    due_date: datetime
    total: int
    credit_line: int
    recorded_on: datetime
    