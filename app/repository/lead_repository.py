from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.models_lead import Lead

class LeadRepository:

    async def create(self, db: AsyncSession, data: dict):
        lead = Lead(**data)
        db.add(lead)
        await db.commit() 
        await db.refresh(lead) 
        return lead

    async def get_all(self, db: AsyncSession):

        result = await db.execute(select(Lead))
        return result.scalars().all()

    async def get_by_id(self, db: AsyncSession, lead_id: int):
        result = await db.execute(select(Lead).where(Lead.id == lead_id))
        return result.scalar_one_or_none()

    async def update(self, db: AsyncSession, lead: Lead, data: dict):
        for field, value in data.items():
            setattr(lead, field, value)
        
        await db.commit()   
        await db.refresh(lead) 
        return lead

    async def delete(self, db: AsyncSession, lead: Lead):
        await db.delete(lead) 
        await db.commit()     