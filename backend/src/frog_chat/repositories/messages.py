from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from frog_chat.db.models.message import Message


class MessageRepository:
    async def create(self, session: AsyncSession, message: Message):
        session.add(message)

        await session.commit()
        await session.refresh(message)

        return message

    async def get_chat(self, session: AsyncSession) -> list[Message]:
        messages = await session.scalars(
            select(Message)
            .order_by(Message.created_at.asc())
        )

        return list(messages)
