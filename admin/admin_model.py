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
    password: str
    last_login: datetime
    is_superuser: bool
    username: str
    first_name: str
    last_name: str
    email: str
    is_staff: bool
    is_active: bool
    date_joined: datetime
    
class AuthUserRoleModel(BaseModel):
    id: int
    user_id: int
    role: str

class AuthUserGroupModel(BaseModel):
    id: int
    user_id: int
    group_id: int

class AuthRoleModel(BaseModel):
    id: int
    role: str
    description: str

class AuthPermissionModel(BaseModel):
    id: int
    permission: str
    description: str
    codename: str

class AuthRolePermissionModel(BaseModel):
    id: int
    role: str
    permission: str

