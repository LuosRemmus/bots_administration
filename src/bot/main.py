from fastapi import APIRouter, Depends

from sqlalchemy import select, delete, insert, update
from sqlalchemy.sql import func
from sqlalchemy.ext.asyncio import AsyncSession
from models.models import bot
from models.database import get_async_session


router = APIRouter(
    prefix="/bots",
    tags=["Bots"]
)


@router.post("/")
async def add_bot(alias: str, description: str, token: str, name: str, session: AsyncSession = Depends(get_async_session)):
    try:
        query = insert(bot).values(
            id=5,
            alias=alias,
            description=description,
            token=token,
            name=name
        )
        await session.execute(query)
        await session.commit()
        return {"status": 200}
    except Exception as ex:
        print(ex)
        return {
            "status": 503,
            "message": "Бот уже есть в базе"
        }


@router.delete("/{bot_id}")
async def delete_bot(bot_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        delete_ = delete(bot).where(bot.c.id == bot_id)
        await session.execute(delete_)
        await session.commit()
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
    except Exception:
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
    except Exception:
        return {
            "status": 503,
            "data": "Database Error. Maybe it's empty or you lose connection."
        }
