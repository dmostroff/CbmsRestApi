from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class CcAccountModel(BaseModel):
    cc_account_id: int
    cc_card_id: int
    client_id: int
    card_name: str
    card_holder: str
    open_date: Optional[datetime] = None
    account_info: Optional[str] = None
    cc_login: Optional[str] = None
    cc_status: Optional[str] = None
    annual_fee_waived: Optional[str] = None
    credit_limit: Optional[int] = None
    last_checked: Optional[datetime] = None
    last_charge: Optional[datetime] = None
    addtional_card: Optional[bool] = None
    balance_transfer: Optional[str] = None
    notes: Optional[str] = None
    ccaccount_info: Optional[str] = None
    recorded_on: datetime
    