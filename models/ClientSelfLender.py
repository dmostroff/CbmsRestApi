from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ClientSelfLender(BaseModel):
    self_lender_id: int
    client_id: int
    start_date: datetime
    duration: int
    pay_from: str
    monthly_due_date: int
    termination_date: datetime
    login: str
    pwd: str
    recorded_on: datetime
    