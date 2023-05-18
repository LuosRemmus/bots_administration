import logging
from fastapi import FastAPI

from bot.main import router as bot_router
from channel.main import router as channel_router
from message.main import router as message_router
from task.main import router as task_router
from config import config

logging.basicConfig(level=config.log_level)

app = FastAPI(title="Bot management system")

app.include_router(bot_router)
app.include_router(channel_router)
app.include_router(message_router)
app.include_router(task_router)
