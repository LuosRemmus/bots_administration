from fastapi import APIRouter

from sqlalchemy import select, delete, insert, update
from sqlalchemy.ext.asyncio import AsyncSession
from models.database import get_async_session
from models.models import bot


router = APIRouter(
    prefix="/bots",
    tags=["Bots"]
)


@router.post("/")
def add_bot(alias: str, description: str, token: str, name: str):
    try:
        return {
            "status": 200,
            "data": {
                "id": "id",
                "new": True
            }
        }
    except Exception as ex:
        print(ex)
        return {
            "status": 503,
            "message": "Бот уже есть в базе"
        }


@router.delete("/{bot_id}")
async def delete_bot(bot_id: int):
    try:
        return {
            "status": 200,
            "data": {
                "id": bot_id,
                "message": "deleted"
            }
        }
    except Exception as ex:
        print(ex)
        return {
            "status": 503,
            "message": "Бот отсутствует в базе"
        }


@router.patch("/{bot_id}")
def update_bot(bot_id: int):
    try:
        pass
    except Exception as ex:
        print(ex)


@router.get("/{bot_id}")
async def get_bot_info(bot_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(bot).where(bot.c.id == bot_id)
        result = await session.execute(query)
        return result.all()
    except:
        return {
            "status": 503,
            "data": "Database Error. Maybe you lose connection."
        }


@router.get("/")
async def get_bots(session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(bot)
        result = await session.execute(query)
        return result.all()
    except:
        return {
            "status": 503,
            "data": "Database Error. Maybe it's empty or you lose connection."
        }
