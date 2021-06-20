from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ClientAddressModel(BaseModel):
    id: Optional[int] = None
    client_id: int
    address_type: str
    address_1: Optional[str] = None
    address_2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None
    country: Optional[str] = None
    valid_from: Optional[datetime] = None
    valid_to: Optional[datetime] = None
    recorded_on: datetime
    