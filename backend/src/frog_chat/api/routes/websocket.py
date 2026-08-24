import uuid

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from frog_chat.db.database import AsyncSessionLocal
from frog_chat.schemas.message import MessageCreate
from frog_chat.services.messages import message_service

router = APIRouter(tags=["websocket"])


class ConnectionManager:
    def __init__(self) -> None:
        self.connections: dict[uuid.UUID, WebSocket] = {}

    async def connect(
        self,
        user_id: uuid.UUID,
        websocket: WebSocket,
    ) -> None:
        await websocket.accept()
        self.connections[user_id] = websocket

    def disconnect(self, user_id: uuid.UUID) -> None:
        self.connections.pop(user_id, None)

    async def broadcast(self, message: str) -> None:
        for connection in self.connections.values():
            await connection.send_text(message)


manager = ConnectionManager()


@router.websocket("/ws/{user_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    user_id: uuid.UUID,
) -> None:
    await manager.connect(user_id, websocket)

    try:
        async with AsyncSessionLocal() as session:
            while True:
                message = await websocket.receive_text()

                saved_message = await message_service.create_message(
                    session=session,
                    data=MessageCreate(message=message),
                    user_id=user_id,
                )

                await manager.broadcast(
                    saved_message.model_dump_json()
                )

    except WebSocketDisconnect:
        manager.disconnect(user_id)
