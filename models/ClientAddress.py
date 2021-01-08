from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ClientAddress(BaseModel):
    address_id: int
    client_id: int
    address_type: str
    address_1: str
    address_2: str
    city: str
    state: str
    zip: str
    country: str
    valid_from: datetime
    valid_to: datetime
    recorded_on: datetime
    