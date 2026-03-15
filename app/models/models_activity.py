from sqlalchemy import String, Integer, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .models_base import Base, TimestampMixin



class Activity(Base, TimestampMixin):
    __tablename__ = "activities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    lead_id: Mapped[int] = mapped_column(ForeignKey("leads.id"))

    type: Mapped[str] = mapped_column(String(50))  # call / meeting / email

    description: Mapped[str] = mapped_column(Text)

    lead = relationship("Lead")