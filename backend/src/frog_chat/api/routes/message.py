from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from frog_chat.db.database import get_session
from frog_chat.schemas.message import MessageCreate, MessageResponse
from frog_chat.services.messages import message_service


router = APIRouter(prefix="/messages", tags=["messages"])


@router.post(
    "",
    response_model=MessageResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_message_endpoint(data: MessageCreate, user_id: UUID, session: AsyncSession = Depends(get_session)) -> MessageResponse:
    return await message_service.create_message(session=session, data=data, user_id=user_id)


@router.get(
    "",
    response_model=list[MessageResponse],
    status_code=status.HTTP_201_CREATED
)
async def create_message_endpoint(session: AsyncSession = Depends(get_session)) -> list[MessageResponse]:
    return await message_service.get_chat(session=session)
