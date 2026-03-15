from pydantic import BaseModel, EmailStr
from typing import Optional


class LeadCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    message: Optional[str] = None



class LeadUpdate(BaseModel):
    status: Optional[str] = None
    comment: Optional[str] = None


class LeadResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    message: Optional[str]
    status: str
    comment: Optional[str]

    class Config:
        from_attributes = True