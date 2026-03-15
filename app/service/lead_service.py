from sqlalchemy.ext.asyncio import AsyncSession
from app.repository.lead_repository import LeadRepository
from app.service.telegram_service import send_notification


class LeadService:

    def __init__(self):

        self.repo = LeadRepository()


    async def create_lead(self, db: AsyncSession, data):

        lead = await self.repo.create(db, data)

        message = (
            f"Новая заявка!\n"
            f"Имя: {lead.name}\n"
            f"Email: {lead.email}\n"
            f"Телефон: {lead.phone}"
        )

        send_notification(message)

        return lead


    async def get_leads(self, db: AsyncSession):
        return await self.repo.get_all(db)

    async def get_lead(self, db: AsyncSession, lead_id: int):
        return await self.repo.get_by_id(db, lead_id)
    
    async def update_lead(self, db: AsyncSession, lead_id: int, data):

        lead = await self.repo.get_by_id(db, lead_id)

        if not lead:
            return None
        return await self.repo.update(db, lead, data)


    async def delete_lead(self, db: AsyncSession, lead_id: int):
        
        lead = await self.repo.get_by_id(db, lead_id)
        if not lead:
            
            return False
        await self.repo.delete(db, lead)
        return True