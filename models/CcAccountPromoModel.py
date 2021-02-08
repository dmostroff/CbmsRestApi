from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class CcAccountPromoModel(BaseModel):
    promo_id: int
    cc_account_id: int
    offer: Optional[str] = None
    loan_amt: Optional[int] = None
    bal_transfer_date: Optional[datetime] = None
    bal_transfer_amt: Optional[int] = None
    promo_info: Optional[str] = None
    recorded_on: datetime
    