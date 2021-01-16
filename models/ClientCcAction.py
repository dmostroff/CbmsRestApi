from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ClientCcAction(BaseModel):
    cc_account_id: int
    client_id: int
    card_name: str
    card_holder: str
    account: str
    open_date: datetime
    account_info: str
    cc_login: str
    cc_pwd: str
    cc_status: str
    annual_fee_waived: str
    credit_limit: int
    addtional_card: bool
    notes: str
    ccaccount_info: str
    recorded_on: datetime
    