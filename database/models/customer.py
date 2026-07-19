from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models.base import Base

if TYPE_CHECKING:
    from datetime import datetime

    from database.models.dialog import Dialog
    from database.models.order import Order
    from database.models.support_ticket import SupportTicket


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    tickets: Mapped[list[SupportTicket]] = relationship(
        back_populates="customer",
        cascade="all, delete-orphan",
    )

    orders: Mapped[list[Order]] = relationship(
        back_populates="customer",
        cascade="all, delete-orphan",
    )

    dialogs: Mapped[list[Dialog]] = relationship(
        back_populates="customer",
        cascade="all, delete-orphan",
    )
