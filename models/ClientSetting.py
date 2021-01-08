from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ClientSetting(BaseModel):
    client_setting_id: int
    client_id: int
    prefix: str
    keyname: str
    keyvalue: str
    