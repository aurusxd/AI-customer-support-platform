from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models.base import Base

if TYPE_CHECKING:
    from datetime import datetime

    from database.models.channel import Channel
    from database.models.document import Document


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(90), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    document: Mapped[list[Document]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )

    channels: Mapped[list[Channel]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )
