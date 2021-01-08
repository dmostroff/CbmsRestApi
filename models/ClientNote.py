from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ClientNote(BaseModel):
    client_note_id: int
    client_id: int
    note: str
    tags: str
    recorded_by: str
    recorded_on: datetime
    