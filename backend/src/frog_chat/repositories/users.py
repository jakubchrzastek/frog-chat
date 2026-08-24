from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from frog_chat.db.models.user import User


class UserRepository:

    async def create(
        self,
        session: AsyncSession,
        user: User,
    ) -> User:
        session.add(user)

        await session.commit()
        await session.refresh(user)

        return user

    async def get_all(self, session: AsyncSession) -> list[User]:
        users = await session.scalars(select(User).order_by(User.created_at.asc()))
        return list(users)
