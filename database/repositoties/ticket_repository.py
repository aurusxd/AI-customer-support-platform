from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.support_ticket import SupportTicket
from database.session import provider
from utils.enums.ticket_status import TicketStatus


class TicketRepository:
    @provider.inject_session
    async def create(
        self,
        ticket: SupportTicket,
        session: AsyncSession,
    ) -> SupportTicket:
        session.add(ticket)
        await session.flush()
        await session.refresh(ticket)

        return ticket

    @provider.inject_session
    async def update(
        self,
        ticket: SupportTicket,
        session: AsyncSession,
    ) -> SupportTicket:
        session.add(ticket)
        await session.flush()
        await session.refresh(ticket)

        return ticket

    @provider.inject_session
    async def get_all(
        self,
        session: AsyncSession,
    ) -> list[SupportTicket]:
        result = await session.execute(
            select(SupportTicket).order_by(SupportTicket.created_at.desc())
        )

        return list(result.scalars().all())

    @provider.inject_session
    async def get_by_id(
        self,
        ticket_id: int,
        session: AsyncSession,
    ) -> SupportTicket | None:
        result = await session.execute(select(SupportTicket).where(SupportTicket.id == ticket_id))

        return result.scalar_one_or_none()

    @provider.inject_session
    async def get_by_customer_id(
        self,
        customer_id: int,
        session: AsyncSession,
    ) -> list[SupportTicket]:
        result = await session.execute(
            select(SupportTicket)
            .where(SupportTicket.customer_id == customer_id)
            .order_by(SupportTicket.created_at.desc())
        )

        return list(result.scalars().all())

    @provider.inject_session
    async def get_by_dialog_id(
        self,
        dialog_id: int,
        session: AsyncSession,
    ) -> list[SupportTicket]:
        result = await session.execute(
            select(SupportTicket)
            .where(SupportTicket.dialog_id == dialog_id)
            .order_by(SupportTicket.created_at.desc())
        )

        return list(result.scalars().all())

    @provider.inject_session
    async def get_by_status(
        self,
        status: TicketStatus,
        session: AsyncSession,
    ) -> list[SupportTicket]:
        result = await session.execute(
            select(SupportTicket)
            .where(SupportTicket.status == status)
            .order_by(SupportTicket.created_at.desc())
        )

        return list(result.scalars().all())

    @provider.inject_session
    async def delete(
        self,
        ticket: SupportTicket,
        session: AsyncSession,
    ) -> None:
        await session.delete(ticket)
        await session.flush()
