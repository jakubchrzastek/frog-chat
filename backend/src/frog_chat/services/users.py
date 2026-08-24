import random
import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from frog_chat.db.models.user import User
from frog_chat.schemas.user import UserResponse
from frog_chat.repositories.users import UserRepository

ADJECTIVES = [
    "Confused",
    "Angry",
    "Sleepy",
    "Funky",
    "Tiny",
    "Dancing",
    "Hungry",
    "Sneaky",
]

NOUNS = [
    "Potato",
    "Frog",
    "Duck",
    "Hamster",
    "Dinosaur",
    "Pickle",
    "Penguin",
    "Banana",
]


def generate_nickname() -> str:
    return f"{random.choice(ADJECTIVES)} {random.choice(NOUNS)}"


class UserService():
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    async def create_user(self, session: AsyncSession) -> UserResponse:
        user_instance = User(
            id=uuid.uuid4(),
            nickname=generate_nickname(),
        )

        user = await self.repository.create(session=session, user=user_instance)

        return UserResponse.model_validate(user)

    async def get_users(self, session: AsyncSession):
        users = await self.repository.get_all(session)

        return [UserResponse.model_validate(user) for user in users]


user_service = UserService(repository=UserRepository())
