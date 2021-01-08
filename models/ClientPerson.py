from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ClientPerson(BaseModel):
    client_id: int
    last_name: str
    first_name: str
    middle_name: str
    dob: datetime
    gender: str
    ssn: str
    mmn: str
    email: str
    pwd: str
    phone: str
    phone_2: str
    phone_cell: str
    phone_fax: str
    phone_official: str
    client_info: str
    recorded_on: datetime
    