from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ClientCcHistory(BaseModel):
    cc_hist_id: int
    client_id: int
    ccaccount_id: int
    ccevent: str
    ccevent_amt: int
    details: str
    recorded_on: datetime
    