import logging
from fastapi import APIRouter, Depends

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from bot.models import GetBotModel, PostBotModel, PostRespBotModel, PutBotModel
from models.models import Bot
from models.database import get_async_session
import starlette.status as status

router = APIRouter(
    prefix="/bots",
    tags=["Bots"]
)

logger = logging.getLogger("bot")


@router.post("/", response_model=PostRespBotModel, status_code=status.HTTP_200_OK)
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
        return PostRespBotModel(id=bot.id)
    except Exception as ex:
        logger.error(ex)
        return {
            "status": status.HTTP_409_CONFLICT, # Лучше всё заменить на статусы, а не хардкодить
            "message": "Бот уже есть в базе"
        }


@router.delete("/{bot_id}", status_code=status.HTTP_200_OK)
async def delete_bot(bot_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        await session.delete(bot_id)
        await session.commit()
        return { # Вот эту модель лучше поменять
            "status": status.HTTP_200_OK,
            "data": {
                "id": bot_id,
                "message": "deleted"
            }
        }
        """
        скорее всего подойдёт что то наподобие:
        return bot_id
        """
    except Exception as ex:
        """
        эту ошибку лучше отлавливать последней
        перед ней лучше отловить IntegrityError от алхимии с разными статусами
        """
        logging.error(ex)
        return {
            "status": status.HTTP_409_CONFLICT,
            "message": "Бот отсутствует в базе"
        }


@router.patch("/{bot_id}", status_code=status.HTTP_200)
async def update_bot(bot_id: int, bot_model: PutBotModel, session: AsyncSession = Depends(get_async_session)):
    try:
        bot = await session.get(bot_id)
        for field, value in bot_model.__fields__.items():
            if value is not None:
                setattr(bot, field, value)
        await session.commit()
    except Exception as ex:
        logger.error(ex)
        return {
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "data": "Database Error. Maybe you lose connection."
        } 


@router.get("/{bot_id}", response_model=GetBotModel, status_code=status.HTTP_200_OK)
async def get_bot_info(bot_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        return await session.get(bot_id)
    except Exception:
        return {
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "data": "Database Error. Maybe you lose connection."
        }


@router.get("/", response_model=list[GetBotModel], status_code=status.HTTP_200_OK)
async def get_bots(session: AsyncSession = Depends(get_async_session)):
    try:
        return (await session.scalars(select(Bot))).fetchall()
    except Exception:
        return {
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "data": "Database Error. Maybe it's empty or you lose connection."
        }
