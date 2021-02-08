from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ClientEmailModel(BaseModel):
    id: int
    client_id: Optional[int] = None
    emailtype: str
    email: str
    isdefault: Optional[bit] = None
    isconfirmed: Optional[bit] = None
    recorded_on: datetime
    