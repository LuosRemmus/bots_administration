from fastapi import APIRouter, Depends
import logging

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from channel.models import GetChannelModel, PostChannelModel, PostRespChannelModel
from models.models import Channel, Bot
from models.database import get_async_session
import starlette.status as status
from typing import List

router = APIRouter(prefix="/channels", tags=["Channels"])

logger = logging.getLogger("channel")

@router.post("/", status_code=status.HTTP_200_OK)
async def bind(channel_model: PostChannelModel, session: AsyncSession = Depends(get_async_session)):
    try:
        channel = Channel(
            channel_link = channel_model.channel_link,
            bot_link = channel_model.bot_link,
            bot_id = channel_model.bot_id
        )
        session.add(channel)

        await session.commit()
        await session.refresh(channel)
        return {
            "status": status.HTTP_200_OK,
            "data": {
                "id": channel.id,
                "channel_link": channel_model.channel_link,
                "bot_link": channel_model.bot_link,
                "bot_id": channel_model.bot_id
            }
        }
        # return PostRespChannelModel(id=channel.id)
    except Exception as ex:
        logger.error(ex)
        return {
            "status": status.HTTP_409_CONFLICT,
            "message": "Задан некорректный идентификатор канала"
        }


@router.delete("/{channel_id}", status_code=status.HTTP_200_OK)
async def delete_channel(channel_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        channel = await session.get(Channel, channel_id)
        await session.delete(channel)
        await session.commit()
        return {
            "status": status.HTTP_200_OK,
            "data": {
                "id": channel_id,
                "message": "deleted"
            }
        }
    except Exception as ex:
        logging.error(ex)
        return {
            "status": status.HTTP_409_CONFLICT,
            "message": "Канал отсутствует в базе"
        }



@router.get("/{channel_id}", response_model=GetChannelModel, status_code=status.HTTP_200_OK)
async def channel_info(channel_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        return await session.scalar(select(Channel).where(Channel.id==channel_id))
    except Exception as ex:
        logging.error(ex)
        return {
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": "Данный идентификатор отсутствует в базе"
        }


@router.get("/", response_model=List[GetChannelModel], status_code=status.HTTP_200_OK)
async def get_channels(session: AsyncSession = Depends(get_async_session)):
    try:
        return (await session.scalars(select(Channel))).fetchall()
    except Exception as ex:
        logging.error(ex)
        return {
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": "Ошибка подключения к базе данных"
        }
