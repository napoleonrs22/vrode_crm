from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field

from app.models.models_lead import LeadStatus


class LeadCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    message: Optional[str] = None


class LeadUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    message: Optional[str] = None
    status: Optional[LeadStatus] = None


class LeadResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    message: Optional[str]
    status: LeadStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class LeadListResponse(BaseModel):
    items: list[LeadResponse]
    total: int
    limit: int
    offset: int


class LeadListQuery(BaseModel):
    status: Optional[LeadStatus] = None
    limit: int = Field(default=20, ge=1, le=100)
    offset: int = Field(default=0, ge=0)
