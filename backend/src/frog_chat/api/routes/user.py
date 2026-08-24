from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from frog_chat.db.database import get_session
from frog_chat.schemas.user import UserResponse
from frog_chat.services.users import user_service

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_user_endpoint(
    session: AsyncSession = Depends(get_session),
) -> UserResponse:
    return await user_service.create_user(session)


@router.get(
    "",
    response_model=list[UserResponse],
)
async def get_users_endpoint(
    session: AsyncSession = Depends(get_session),
) -> list[UserResponse]:
    return await user_service.get_users(session)
