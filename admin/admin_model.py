from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class UserLoginModel(BaseModel):
    id: Optional[int] = None
    username: str
    token: Optional[str] = None
    exp_date: Optional[datetime] = None
    recorded_on: Optional[datetime] = None
    
class AuthUserModel(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    email: str
    username: str
    password: str
    password_hint: Optional[str] = None
    is_superuser: Optional[bool] = False
    is_staff: Optional[bool] = True
    is_active: Optional[bool] = True
    roles: List[str] = None
    created_at: Optional[datetime] = None

class AuthUserSettingModel(BaseModel):
    id: Optional[int] = None
    user_id: int
    prefix: str
    keyname: str
    keyvalue: Optional[str] = None
    display_rank: Optional[int] = None

class AuthRoleModel(BaseModel):
    id: Optional[int] = None
    role: str
    description: Optional[str] = None

class AuthPermissionModel(BaseModel):
    id: Optional[int] = None
    permission: str
    description: Optional[str] = None
    codename: str
    
class AuthRolePermissionModel(BaseModel):
    id: Optional[int] = None
    role: str
    permission: str

class AdmSettingModel(BaseModel):
    id: Optional[int] = None
    prefix: str
    keyname: str
    keyvalue: Optional[str] = None
    display_rank: Optional[int] = None
    