from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ClientCreditlineHistoryModel(BaseModel):
    creditline_id: int
    client_id: int
    cc_account_id: int
    credit_line_date: datetime
    credit_amt: Optional[int] = None
    credit_status: Optional[str] = None
    recorded_on: datetime
    