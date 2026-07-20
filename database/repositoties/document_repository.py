from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.document import Document
from database.session import provider


class DocumentRepository:
    @provider.inject_session
    async def get_all_by_employee(
        self,
        employee_id: int,
        session: AsyncSession,
    ) -> list[Document]:
        result = await session.execute(
            select(Document).where(
                Document.employee_id == employee_id,
            )
        )

        return list(result.scalars().all())

    @provider.inject_session
    async def get_by_id(
        self,
        file_id: int,
        employee_id: int,
        session: AsyncSession,
    ) -> Document | None:
        result = await session.execute(
            select(Document).where(
                Document.id == file_id,
                Document.employee_id == employee_id,
            )
        )

        return result.scalar_one_or_none()

    @provider.inject_session
    async def create(
        self,
        file: Document,
        session: AsyncSession,
    ) -> Document:
        session.add(file)
        await session.flush()
        await session.refresh(file)

        return file

    @provider.inject_session
    async def update(
        self,
        file: Document,
        session: AsyncSession,
    ) -> Document:
        session.add(file)
        await session.flush()
        await session.refresh(file)

        return file

    @provider.inject_session
    async def delete(
        self,
        file: Document,
        session: AsyncSession,
    ) -> None:
        await session.delete(file)
        await session.flush()
