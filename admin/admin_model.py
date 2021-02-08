from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class UserLoginModel(BaseModel):
    id: int
    username: str
    token: str
    exp_date: datetime
    recorded_on: datetime
    
class AuthUserModel(BaseModel):
    id: int
    username: str
    password: str
    first_name: str
    last_name: str
    email: str
    is_superuser: bool
    is_staff: bool
    is_active: bool
    password_hint: Optional[str] = None
    roles: Optional[str] = None
    created_at: datetime

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
    adm_setting_id: int
    prefix: str
    keyname: str
    keyvalue: Optional[str] = None
    