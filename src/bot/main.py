import logging
from fastapi import APIRouter, Depends

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from bot.models import GetBotModel, PostBotModel, PostRespBotModel, PutBotModel
from models.models import Bot
from models.database import get_async_session
import starlette.status as status
from typing import List

router = APIRouter(
    prefix="/bots",
    tags=["Bots"]
)

logger = logging.getLogger("bot")


@router.post("/", status_code=status.HTTP_200_OK)
async def add_bot(bot_model: PostBotModel, session: AsyncSession = Depends(get_async_session)):
    try:
        bot = Bot(
            alias = bot_model.alias,
            token = bot_model.token,
            description = bot_model.description,
            name = bot_model.name
        )
        session.add(bot)
        await session.commit()
        await session.refresh(bot)
        return {
            "status": status.HTTP_200_OK,
            "data": {
                "id": bot.id,
                "alias": bot.alias,
                "token": bot.token,
                "description": bot.description,
                "name": bot.name,
                "message": "created"
            }
        }
    except Exception as ex:
        logger.error(ex)
        return {
            "status": status.HTTP_409_CONFLICT,
            "message": "Бот уже есть в базе"
        }


@router.delete("/{bot_id}", status_code=status.HTTP_200_OK)
async def delete_bot(bot_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        bot = await session.get(Bot, bot_id)
        await session.delete(bot)
        await session.commit()
        return {
            "status": status.HTTP_200_OK,
            "data": {
                "id": bot_id,
                "message": "deleted"
            }
        }
    except Exception as ex:
        logging.error(ex)
        return {
            "status": status.HTTP_409_CONFLICT,
            "message": "Бот отсутствует в базе"
        }


@router.patch("/{bot_id}", status_code=status.HTTP_200_OK)
async def update_bot(bot_id: int, bot_model: PutBotModel, session: AsyncSession = Depends(get_async_session)):
    try:
        bot = await session.get(Bot, bot_id)
        for field, value in bot_model.__dict__.items():
            if value is not None:
                setattr(bot, field, value)
        await session.commit()
        return {
            "status": status.HTTP_200_OK,
            "data": {
                "id": bot.id,
                "alias": bot.alias,
                "description": bot.description,
                "token": bot.token,
                "name": bot.name,
                "message": "updated"
            }
        }
    except Exception as ex:
        logger.error(ex)
        return {
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": "Ошибка подключения к базе данных."
        } 


@router.get("/{bot_id}", response_model=GetBotModel, status_code=status.HTTP_200_OK)
async def get_bot_info(bot_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        return await session.scalar(select(Bot).where(Bot.id==bot_id))
    except Exception:
        return {
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": "Ошибка подключения к базе данных."
        }


@router.get("/", response_model=List[GetBotModel], status_code=status.HTTP_200_OK)
async def get_bots(session: AsyncSession = Depends(get_async_session)):
    try:
        return (await session.scalars(select(Bot))).fetchall()
    except Exception:
        return {
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": "Ошибка подключения к базе данных."
        }
