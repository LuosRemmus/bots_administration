from fastapi import APIRouter, Depends
import logging
from message.models import MessageModel
import starlette.status as status
from telebot import TeleBot
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.models import Bot, Channel
from models.database import get_async_session
import regex

router = APIRouter(prefix="/messages", tags=["Messages"])

async def bot_init(channel_id: int, chat_link: str, msg: str, session: AsyncSession):
    bot_id = await session.scalar(select(Channel.bot_id).where(Channel.id==channel_id))
    token = await session.scalar(select(Bot.token).where(Bot.id==bot_id))
    bot = TeleBot(token)
    msg = msg.replace("***newstr***", "\n")
    bot.send_message(chat_link, msg, parse_mode='html')

    return bot


@router.post("/", status_code=status.HTTP_200_OK)
async def send_message(channel_id: int, message: str, session: AsyncSession = Depends(get_async_session)):
    try:
        message_ = MessageModel(
            channel_id = channel_id,
            message = message
        )
        channel_link_ = await session.scalar(select(Channel.channel_link).where(Channel.id==channel_id))
        await bot_init(channel_id, channel_link_, message_.message, session)
        
        return {
            "status": status.HTTP_200_OK,
            "data": {
                "message_text": message_
            }
        }
    except Exception as ex:
        print(type(ex))
        logging.error(ex)
        return {
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": "Сообщение не отправлено"
        }
