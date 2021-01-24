from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ClientEmail(BaseModel):
    id: int
    client_id: int
    emailtype: str
    email: str
    isdefault: int
    isconfirmed: int
    recorded_on: datetime
    