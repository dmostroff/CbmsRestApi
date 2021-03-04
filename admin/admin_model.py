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

class AuthRoleModel(BaseModel):
    id: int
    role: str
    description: Optional[str] = None

class AuthPermissionModel(BaseModel):
    id: int
    permission: str
    description: Optional[str] = None
    codename: str
    
class AuthRolePermissionModel(BaseModel):
    id: int
    role: str
    permission: str

class AdmSettingModel(BaseModel):
    id: int
    prefix: str
    keyname: str
    keyvalue: Optional[str] = None
    