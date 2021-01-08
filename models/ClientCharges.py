from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ClientCharges(BaseModel):
    charge_id: int
    client_id: int
    charge_goal: int
    charged: int
    paid: int
    fees: int
    due_on_day: int
    charge_info: str
    recorded_on: datetime
    