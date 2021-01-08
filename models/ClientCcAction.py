from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ClientCcAction(BaseModel):
    cc_action_id: int
    client_id: int
    cc_account_id: int
    ccaction: str
    action_type: str
    action_status: str
    due_date: datetime
    details: str
    recorded_on: datetime
    