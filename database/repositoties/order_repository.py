from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.order import Order
from database.session import provider
from utils.enums.order_status import OrderStatus


class OrderRepository:
    @provider.inject_session
    async def create(
        self,
        order: Order,
        session: AsyncSession,
    ) -> Order:
        session.add(order)
        await session.flush()
        await session.refresh(order)

        return order

    @provider.inject_session
    async def update(
        self,
        order: Order,
        session: AsyncSession,
    ) -> Order:
        session.add(order)
        await session.flush()
        await session.refresh(order)

        return order

    @provider.inject_session
    async def get_all(
        self,
        session: AsyncSession,
    ) -> list[Order]:
        result = await session.execute(select(Order).order_by(Order.created_at.desc()))

        return list(result.scalars().all())

    @provider.inject_session
    async def get_by_id(
        self,
        order_id: int,
        session: AsyncSession,
    ) -> Order | None:
        result = await session.execute(select(Order).where(Order.id == order_id))

        return result.scalar_one_or_none()

    @provider.inject_session
    async def get_by_customer_id(
        self,
        customer_id: int,
        session: AsyncSession,
    ) -> list[Order]:
        result = await session.execute(
            select(Order).where(Order.customer_id == customer_id).order_by(Order.created_at.desc())
        )

        return list(result.scalars().all())

    @provider.inject_session
    async def get_by_status(
        self,
        status: OrderStatus,
        session: AsyncSession,
    ) -> list[Order]:
        result = await session.execute(
            select(Order).where(Order.status == status).order_by(Order.created_at.desc())
        )

        return list(result.scalars().all())

    @provider.inject_session
    async def delete(
        self,
        order: Order,
        session: AsyncSession,
    ) -> None:
        await session.delete(order)
        await session.flush()
