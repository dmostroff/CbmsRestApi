from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ClientChargesModel(BaseModel):
    charge_id: int
    client_id: int
    charge_goal: int
    charged: int
    paid: Optional[int] = None
    fees: Optional[int] = None
    due_on_day: Optional[int] = None
    charge_info: Optional[str] = None
    recorded_on: datetime
    