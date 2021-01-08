from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ClientCcPoints(BaseModel):
    cc_points_id: int
    client_id: int
    cc_account_id: int
    sold_to: str
    sold_on: datetime
    sold_points: int
    price: int
    login: str
    pwd: str
    source_info: str
    recorded_on: datetime
    