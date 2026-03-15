from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas.lead import LeadCreate, LeadUpdate, LeadResponse
from app.service.lead_service import LeadService

router = APIRouter(prefix="/leads", tags=["Leads"])

service = LeadService()


@router.post("", response_model=LeadResponse)
async def create_lead(data: LeadCreate, db: AsyncSession = Depends(get_db)):

    return await service.create_lead(db, data.model_dump())


@router.get("", response_model=list[LeadResponse])
async def get_leads(db: AsyncSession = Depends(get_db)):

    return await service.get_leads(db)

@router.get("/{lead_id}", response_model=LeadResponse)
async def get_lead(lead_id: int,db: AsyncSession = Depends(get_db)):

    lead = await service.get_lead(db, lead_id)

    
    if not lead:
        raise HTTPException(status_code=404)
    return lead


@router.patch("/{lead_id}", response_model=LeadResponse)
async def update_lead(
        lead_id: int,
        data: LeadUpdate,
        db: AsyncSession = Depends(get_db)
):

    lead = await service.update_lead(
        db,
        lead_id,
        data.model_dump(exclude_none=True)
    )

    if not lead:
        raise HTTPException(status_code=404)

    return lead


@router.delete("/{lead_id}")
async def delete_lead(lead_id: int, db: AsyncSession = Depends(get_db)):

    success = await service.delete_lead(db, lead_id)

    if not success:
        raise HTTPException(status_code=404, detail="Lead not found")

    return {"message": "Lead deleted"}