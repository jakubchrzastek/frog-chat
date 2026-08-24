import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from frog_chat.db.models.message import Message
from frog_chat.repositories.messages import MessageRepository
from frog_chat.schemas.message import MessageCreate, MessageResponse


class MessagesService:
    def __init__(self, repository=MessageRepository):
        self.repository = repository

    async def create_message(self, session: AsyncSession, data: MessageCreate, user_id: uuid.UUID) -> MessageResponse:

        message_create = Message(
            id=uuid.uuid4(),
            user_id=user_id,
            message=data.message
        )

        message = await self.repository.create(session, message_create)

        return MessageResponse.model_validate(message)

    async def get_chat(self, session: AsyncSession) -> list[MessageResponse]:
        chat = await self.repository.get_chat(session)

        return [
            MessageResponse.model_validate(message)
            for message in chat
        ]


message_service = MessagesService(repository=MessageRepository())
