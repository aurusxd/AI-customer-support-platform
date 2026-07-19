from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models.base import Base
from utils.enums.categories import Categories
from utils.enums.ticket_status import TicketStatus

if TYPE_CHECKING:
    from datetime import datetime

    from database.models.customer import Customer
    from database.models.dialog import Dialog


class SupportTicket(Base):
    __tablename__ = "support_tickets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    dialog_id: Mapped[int] = mapped_column(
        ForeignKey("dialogs.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    category: Mapped[Categories] = mapped_column(
        String(50),
        default=Categories.HELP,
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    status: Mapped[TicketStatus] = mapped_column(
        String(50),
        default=TicketStatus.PROCESSING,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    customer: Mapped[Customer] = relationship(back_populates="tickets")

    dialog: Mapped[Dialog] = relationship(back_populates="tickets")
