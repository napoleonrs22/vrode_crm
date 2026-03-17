from sqlalchemy import String, Integer, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .models_base import Base, TimestampMixin


class Message(Base, TimestampMixin):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    lead_id: Mapped[int] = mapped_column(ForeignKey("leads.id"))

    sender: Mapped[str] = mapped_column(String(50))  # client / manager

    platform: Mapped[str] = mapped_column(String(50))  # telegram / whatsapp / site

    text: Mapped[str] = mapped_column(Text)

    lead = relationship("Lead")
