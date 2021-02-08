from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ClientNoteModel(BaseModel):
    client_note_id: int
    client_id: int
    note: Optional[str] = None
    tags: Optional[str] = None
    recorded_by: str
    recorded_on: datetime
    