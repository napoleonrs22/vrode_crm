from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column
from .models_base import Base, TimestampMixin


class Lead(Base):
    __tablename__ = "leads"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255))
    phone: Mapped[str] = mapped_column(String(50))

    message: Mapped[str] = mapped_column(Text)

    status: Mapped[str] = mapped_column(
        String(50),
        default="new"
    )

    comment: Mapped[str] = mapped_column(Text, nullable=True)