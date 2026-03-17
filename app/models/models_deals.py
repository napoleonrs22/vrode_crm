from sqlalchemy import String, Integer, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .models_base import Base, TimestampMixin


class Deal(Base, TimestampMixin):
    __tablename__ = "deals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    lead_id: Mapped[int] = mapped_column(ForeignKey("leads.id"))

    service: Mapped[str] = mapped_column(String(255))

    price: Mapped[float] = mapped_column(Float)

    status: Mapped[str] = mapped_column(String(50), default="open")

    lead = relationship("Lead")
