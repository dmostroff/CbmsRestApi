from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ClientCreditlineHistory(BaseModel):
    creditline_id: int
    client_id: int
    cc_account_id: int
    credit_line_date: datetime
    credit_amt: int
    credit_status: str
    recorded_on: datetime
    