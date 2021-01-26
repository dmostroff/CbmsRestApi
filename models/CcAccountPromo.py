from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class CcAccountPromo(BaseModel):
    promo_id: int
    cc_account_id: int
    offer: str
    loan_amt: int
    bal_transfer_date: datetime
    bal_transfer_amt: int
    promo_info: str
    recorded_on: datetime
    