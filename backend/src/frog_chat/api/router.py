from fastapi import APIRouter

from frog_chat.api.routes import health, user, message

router = APIRouter()

router.include_router(health.router)
router.include_router(user.router)
router.include_router(message.router)
