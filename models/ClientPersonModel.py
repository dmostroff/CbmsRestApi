from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ClientPersonModel(BaseModel):
    client_id: Optional[int] = None
    last_name: str
    first_name: str
    middle_name: Optional[str] = None
    dob: Optional[datetime] = None
    gender: Optional[str] = None
    ssn: Optional[str] = None
    mmn: Optional[str] = None
    email: Optional[str] = None
    pwd: Optional[str] = None
    occupation: Optional[str] = None
    phone: Optional[str] = None
    phone_2: Optional[str] = None
    phone_cell: Optional[str] = None
    phone_official: Optional[str] = None
    client_status: Optional[str] = None
    client_info: Optional[str] = None
    recorded_on: Optional[datetime] = None
    