from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.customer import Customer
from database.session import provider


class UserRepository:
    @provider.inject_session
    async def get_all(
        self,
        session: AsyncSession,
    ) -> list[Customer]:
        result = await session.execute(select(Customer))
        return list(result.scalars().all())

    @provider.inject_session
    async def get_by_id(
        self,
        customer_id: int,
        session: AsyncSession,
    ) -> Customer | None:
        result = await session.execute(select(Customer).where(Customer.id == customer_id))
        return result.scalar_one_or_none()

    @provider.inject_session
    async def get_by_name(
        self,
        name: str,
        session: AsyncSession,
    ) -> Customer | None:
        result = await session.execute(select(Customer).where(Customer.name == name))
        return result.scalar_one_or_none()

    @provider.inject_session
    async def create(
        self,
        customer: Customer,
        session: AsyncSession,
    ) -> Customer:
        session.add(customer)
        await session.flush()
        await session.refresh(customer)
        return customer

    @provider.inject_session
    async def update(
        self,
        customer: Customer,
        session: AsyncSession,
    ) -> Customer:
        session.add(customer)
        await session.flush()
        await session.refresh(customer)
        return customer

    @provider.inject_session
    async def delete(
        self,
        customer: Customer,
        session: AsyncSession,
    ) -> Customer:
        session.add(customer)
        await session.flush()
        await session.refresh(customer)
        return customer
