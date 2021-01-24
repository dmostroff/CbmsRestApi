from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class CcAccount(BaseModel):
    cc_account_id: int
    cc_card_id: int
    client_id: int
    card_name: str
    card_holder: str
    open_date: datetime
    account_info: str
    cc_login: str
    cc_status: str
    annual_fee_waived: str
    credit_limit: int
    last_checked: datetime
    last_charge: datetime
    addtional_card: bool
    balance_transfer: str
    notes: str
    ccaccount_info: str
    recorded_on: datetime
    